# easySearch
## Prepare your data
put your files in `data` the folder

## Preparing Dependencies
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
>>> h = search("PUT_YOUR_QUERY_HERE")
>>> beautiful_print(h)
```
