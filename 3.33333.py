import os
import spacy
import pandas as pd
from gensim import corpora, models

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")


def preprocess_file(file_path):
    """
    Preprocess the content of a file by filtering out specific parts of speech.
    Retains only nouns, verbs, adjectives, and adverbs.

    Args:
    file_path: Path to the file to be processed.

    Returns:
    A list of cleaned and preprocessed tokens from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        doc = nlp(text)
        tokens = [token.text for token in doc if token.pos_ in ['NOUN', 'VERB', 'ADJ', 'ADV'] and not token.like_url]
    return tokens


def process_files(input_dir):
    """
    Process all text files in the input directory and perform LDA topic modeling.

    Args:
    input_dir: Directory containing text files to be processed.

    Returns:
    A list of dictionaries with filename and topic information.
    """
    data = []
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_dir, filename)
            tokens = preprocess_file(file_path)

            if tokens:
                dictionary = corpora.Dictionary([tokens])
                corpus = [dictionary.doc2bow(tokens)]

                if corpus:
                    lda_model = models.LdaModel(
                        corpus=corpus,
                        id2word=dictionary,
                        num_topics=2,
                        random_state=100,
                        update_every=1,
                        chunksize=1000,
                        passes=10,
                        alpha='auto',
                        per_word_topics=True
                    )

                    topic_info = {"Filename": filename}
                    for idx in range(lda_model.num_topics):
                        words_and_probs = lda_model.show_topic(idx, topn=5)
                        topic_info[f"Topic {idx}"] = ", ".join(
                            [f"{word} ({prob:.2f})" for word, prob in words_and_probs])

                    data.append(topic_info)

    return data


def save_to_excel(data, output_filepath):
    """
    Save the processed data to an Excel file.

    Args:
    data: List of dictionaries containing filename and topic information.
    output_filepath: Path to save the Excel file.
    """
    df = pd.DataFrame(data)
    df.to_excel(output_filepath, index=False)


if __name__ == "__main__":
    input_dir = r'KOR_1'
    output_filepath = r'KOR_1.xlsx'

    data = process_files(input_dir)
    save_to_excel(data, output_filepath)

    print(f"Topics extracted and saved to {output_filepath}")
