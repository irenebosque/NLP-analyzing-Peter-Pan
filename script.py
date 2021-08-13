from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter


# import text of choice here
text = open("peter_pan.txt", encoding='utf-8').read().lower()


# sentence and word tokenize text here
word_tokenized_text = word_sentence_tokenize(text)


# create a list to hold part-of-speech tagged sentences here
pos_tagged_text = []

# create a for loop through each word tokenized sentence here
for word in word_tokenized_text:

    # part-of-speech tag each sentence and append to list of pos-tagged sentences here
    pos_tagged_text.append(pos_tag(word))


# define noun phrase chunk grammar here
np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

# create noun phrase RegexpParser object here
np_chunk_parser = RegexpParser(np_chunk_grammar)


# create a list to hold noun phrase chunked sentences
np_chunked_text = []


# create a for loop through each pos-tagged sentence here
for sentence in pos_tagged_text:
    # chunk each sentence and append to lists here
    np_chunked_text.append(np_chunk_parser.parse(sentence))

# store and print the most common NP-chunks here
most_common_np_chunks = np_chunk_counter(np_chunked_text)

for i in most_common_np_chunks:
    print(i)

