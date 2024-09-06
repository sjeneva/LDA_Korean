from konlpy.tag import Okt
from gensim import corpora, models
import gensim
def main():

documents = [

]


# Initialize Korean tokenizer
okt = Okt()

# Tokenization and preprocessing
texts = []
for document in documents:
    tokens = okt.nouns(document)  # Using nouns for simplicity; you can adjust this as needed
    texts.append(tokens)

    # Create a dictionary and corpus needed for LDA
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    # Apply LDA model
    lda_model = gensim.models.LdaMulticore(corpus, num_topics=3, id2word=dictionary, passes=15, workers=3)

    # Print the topics
    topics = lda_model.print_topics(num_words=4)
    for topic in topics:
        print(topic)

if __name__ == '__main__':
    main()