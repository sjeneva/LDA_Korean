import os
from konlpy.tag import Okt

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

input_dir = r'2.6_Korea_KLN_사회_extracted_articles'
output_dir = r'2.7_Korea_KLN_사회_extracted_articles'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

tokenizer = Okt()

for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_dir, filename)
        text = read_text_file(file_path)
        nouns = tokenizer.nouns(text)

        # Filter out one-letter nouns
        filtered_nouns = [noun for noun in nouns if len(noun) > 1]

        output_file_path = os.path.join(output_dir, f'nouns_{filename}')
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for noun in filtered_nouns:
                output_file.write(noun + '\n')
filtered_nouns = [noun for noun in nouns if len(noun) > 1]

print(f"Nouns extracted and saved to the directory: {output_dir}")
