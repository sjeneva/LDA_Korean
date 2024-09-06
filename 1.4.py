from googletrans import Translator, LANGUAGES
import os
import time

def translate_text_with_retry(text, dest_language='en', attempts=3):
    for attempt in range(attempts):
        try:
            return translate_text(text, dest_language)
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(2 ** attempt)  # Exponential backoff
    return None

def translate_text(text, dest_language='en'):
    """Translate the given text to the specified destination language."""
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_language)
        return translated.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return None

def translate_file(file_path, dest_language='en'):
    """Translate the content of a file to the specified destination language."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return translate_text(text, dest_language)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def translate_articles(source_directory_path, dest_directory_path, dest_language='en'):
    """Translate all text files in the specified source directory and save them to the destination directory."""
    for filename in os.listdir(source_directory_path):
        if filename.endswith('.txt'):  # Process only .txt files
            source_file_path = os.path.join(source_directory_path, filename)
            translated_text = translate_file(source_file_path, dest_language)
            if translated_text:
                new_filename = f"translated_{filename}"
                new_file_path = os.path.join(dest_directory_path, new_filename)
                try:
                    with open(new_file_path, 'w', encoding='utf-8') as new_file:
                        new_file.write(translated_text)
                    print(f"Translated and saved {new_filename}")
                except Exception as e:
                    print(f"Error writing to file {new_filename}: {e}")

if __name__ == "__main__":
    source_directory_path = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\1.3_Korea_KLN_extracted_articles'
    dest_directory_path = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\1.4.NC_Korea_KLN_Translate'
    translate_articles(source_directory_path, dest_directory_path)
