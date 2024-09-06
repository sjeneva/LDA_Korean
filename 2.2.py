import os

def read_file(file_path):
    """
    Read the content of a file and return it.
    This function is used to load the tokenized text that will be cleaned.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()


def remove_duplicates(file_content):
    """
    Remove duplicate lines from the file content.
    This function takes the content of a file (as a list of lines), converts it to a set
    (automatically removing duplicates since sets cannot have duplicate elements),
    and then converts it back to a list to effectively remove duplicated lines.
    """
    unique_content = set(file_content)
    return list(unique_content)


def process_files(source_directory, result_directory):
    """
    Process files to remove duplicates and save the results.
    This function iterates over all .txt files in the source directory, removes duplicates
    from their content, and saves the cleaned content to new files in the result directory.
    If the result directory doesn't exist, it's created.
    """
    # Ensure the result directory exists
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)

    for filename in os.listdir(source_directory):
        if filename.endswith('.txt'):
            source_file_path = os.path.join(source_directory, filename)
            result_file_path = os.path.join(result_directory, filename)

            # Read the content of the source file
            content = read_file(source_file_path)

            # Remove duplicate lines from the content
            cleaned_content = remove_duplicates(content)

            # Save the cleaned content to the result file
            with open(result_file_path, 'w', encoding='utf-8') as file:
                file.writelines(cleaned_content)

            print(f"Processed and saved cleaned file: {filename}")

def process_directory(source_directory, result_directory):
    """
    Process all text files in the source directory and save the results in the result directory.

    Args:
    source_directory: The directory containing the original text files.
    result_directory: The directory where the preprocessed files will be saved.
    """
    # Ensure the result directory exists
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)

    stop_words = nlp.Defaults.stop_words  # Get spaCy's default English stop words

    for filename in os.listdir(source_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(source_directory, filename)
            result_file_path = os.path.join(result_directory, filename)

            cleaned_lines = preprocess_file(file_path, stop_words)

            with open(result_file_path, 'w', encoding='utf-8') as result_file:
                result_file.write("\n".join(cleaned_lines))

            print(f"Processed and saved: {filename}")

if __name__ == "__main__":
    # Directories: You have a source directory with the tokenized texts (`Tokenized_Texts`)
    # and a result directory where the cleaned (duplicate-free) texts will be saved (`Cleaned_Texts`).
    source_directory = r'2.1_Korea_KLN_사회_extracted_articles'
    result_directory = r'2.2345_Korea_KLN_사회_extracted_articles'
    process_files(source_directory, result_directory)
# dd
