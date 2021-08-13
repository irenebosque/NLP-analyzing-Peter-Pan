# NLP-discoverIng-insights-into-books
This is a small project to kick-off my Natural language processing (NLP) journey. It is based on the project "Discover Insights into Classic Texts" from the course "Apply Natural Language Processing with Python skill Path" of CodeCademy.com

![Alt Text](https://media.giphy.com/media/lDR0wnXboVr8c/giphy.gif)
# Installation
##  Create a virtual environment (optional)
```
virtualenv --python=/usr/bin/python3.6 ~/NLP
source ~/NLP/bin/activate
pip install nltk
```
## Install additional requirements
Open a new terminal and paste the following

```shell
python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

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