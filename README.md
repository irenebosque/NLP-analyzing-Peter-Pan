# NLP - Analyzing Peter Pan
This is a small project to kick-off my Natural language processing (NLP) journey. It is based on the project "Discover Insights into Classic Texts" from the course *"Apply Natural Language Processing with Python skill Path"* of [CodeCademy.com](https://www.codecademy.com/paths/natural-language-processing/tracks/nlp-language-parsing/modules/nlp-language-parsing/projects/nlp-regex-parsing-project)



![Alt Text](https://media.giphy.com/media/lDR0wnXboVr8c/giphy.gif)

# Goal
The goal of this project is to perform a simple analysis of the classical book *Peter Pan* and to discover who are the most mentioned characters. The file containing the book was downloaded from [Project Gutenberg](https://www.gutenberg.org/ebooks/16).

# Installation
##  Create a virtual environment (optional)
```
virtualenv --python=/usr/bin/python3.6 ~/NLP
source ~/NLP/bin/activate
```

## Clone the repository
In a terminal,  clone this repository wherever you want:
```shell
git clone https://github.com/irenebosque/NLP-analyzing-Peter-Pan.git
```

## Install additional requirements
Then, in the terminal copy/paste the following:

```shell
pip install nltk
python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

```
# Run the code
To perform the analysis you need to run the file called `script.py`
```shell
python script.py
```


# Analysis of the results

The most relevant final results are:
```shell
((('peter', 'NN'),), 319)
((('wendy', 'NN'),), 180)
((('hook', 'NN'),), 127)
((('john', 'NN'),), 116)
((('michael', 'NN'),), 71)

```

Looking at most_common_np_chunks, you can identify characters of importance in the text such as Peter, Wendy, Hook, John and Michael, 
based on their frequency. 
