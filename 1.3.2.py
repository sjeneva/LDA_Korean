import glob
import os
import pandas as pd
import re

# Define paths
directory_path = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\Korea_KLN_사회_extracted_articles'
output_dir = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics'
os.makedirs(output_dir, exist_ok=True)

# Define the markers for extraction
markers = [
    {"start": "###", "end": "* _기"}  # Add more markers as needed
]

# This will hold our data
data = []

# Compile regex pattern for finding the title
title_re = re.compile(r'\* __입력 (.+?)\n')


# Function to extract content between markers
def extract_content(content, start_marker, end_marker):
    start_index = content.find(start_marker)
    end_index = content.find(end_marker, start_index)
    if start_index != -1 and end_index != -1:
        return content[start_index + len(start_marker):end_index].strip()
    return None


# Process each .txt file
for file_path in glob.glob(os.path.join(directory_path, '*.txt')):
    filename = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract the title
    title_search = title_re.search(content)
    title = title_search.group(1) if title_search else "No Title Found"

    extracted_texts = []
    for marker in markers:
        extracted_text = extract_content(content, marker["start"], marker["end"])
        if extracted_text:
            extracted_texts.append(extracted_text)

    # Combine all extracted texts (if any) or note that no content was found
    combined_text = "\n\n---\n\n".join(extracted_texts) if extracted_texts else "Content not found between markers."
    data.append({'Title': title, 'Text': combined_text})

# Convert to DataFrame and save to Excel
df = pd.DataFrame(data)
excel_file_path = os.path.join(output_dir, 'Korea_KLN_사회_extracted_articles.xlsx')
df.to_excel(excel_file_path, index=False)

print(f"Data has been saved to {excel_file_path}.")