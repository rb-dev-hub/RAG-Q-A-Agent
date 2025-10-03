import nltk
from nltk.tokenize import sent_tokenize

# Download the 'punkt' tokenizer model if not already downloaded
#nltk.download('punkt')

def chunk_text(input_text, max_sentences=2):
    sentences = sent_tokenize(input_text)
    chunks = []
    for i in range(0,len(sentences),max_sentences):
        #chunk = sentences[i:i+max_sentences]
        chunk = "".join(sentences[i:i+max_sentences])
        chunks.append(chunk)
    return chunks


