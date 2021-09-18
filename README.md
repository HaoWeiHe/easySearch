# easySearch
This project aims to help you to find out the similarity query under your folder. (Noticed that if this kind of action happened frequently and the corpus isn't modified that much, highly recommend searching for a search engine, eg. Elasticsearch)

## Prepare Your Data
Put your files in `data` the folder

## Prepare Dependencies
- conda env create -f freeze.yml
- download pre-trained word2vec model 
 ```
!wget http://nlp.stanford.edu/data/glove.6B.zip
!unzip glove.6B.zip
mv glove.6B.200d.txt.w2v model

```
## Usage
Get the result
```
>>> from tool import search, beautiful_print
>>> res = search("PUT_YOUR_QUERY_HERE")
>>> beautiful_print(res)
```

The result will come with two types of information- file name and its score.
It may look as follows 
```
data/apple.txt: score:0.571
data/amz.txt: score:0.366
```