import os
import pandas as pd

def merge_text_files_to_excel_by_topic(input_dir, output_excel_file):
    # Dictionaries to store the contents of each text file by topic
    topic_contents = {
        'Topic 0': [],
        'Topic 1': []
    }

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.txt'):
            file_path = os.path.join(input_dir, file_name)
            with open(file_path, 'r', encoding='utf-8') as infile:
                file_content = infile.read()
                # Split the content by topics and add to the corresponding list
                for topic in topic_contents:
                    if topic in file_content:
                        start_index = file_content.index(topic) + len(topic)
                        topic_content = file_content[start_index:]
                        # Assuming that each file only contains one of the topics
                        topic_contents[topic].append(topic_content.strip())
                        break

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    with pd.ExcelWriter(output_excel_file, engine='xlsxwriter') as writer:
        for topic, contents in topic_contents.items():
            # Create a DataFrame from the list
            df = pd.DataFrame(contents, columns=['Content'])
            # Write each DataFrame to a different worksheet.
            df.to_excel(writer, sheet_name=topic, index=False)

# Input directory containing text files
input_dir = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\3.3_Korea_KLN_사회_extracted_articles'

# Output Excel file name
output_excel_file = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\3.4_Korea_KLN_사회_extracted_articles.xlsx'

# Merge the files into an Excel file by topic
merge_text_files_to_excel_by_topic(input_dir, output_excel_file)