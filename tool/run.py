from gensim.utils import tokenize
from  heapq import heappop, heappush

class earsySearch():
	def __init__(self):
		self._num = 10
		self.glove_input_file = 'model/glove.6B.200d.txt'
		self.word2vec_output_file = 'model/glove.6B.200d.txt.w2v'
		self.model = self.load_mode()
	
	def train(self):
		from gensim.scripts.glove2word2vec import glove2word2vec
		glove2word2vec(self.glove_input_file , self.word2vec_output_file)

	def load_mode(self):
		from gensim.models import KeyedVectors
		model = KeyedVectors.load_word2vec_format(self.word2vec_output_file, binary=False,limit=500000)
		return model

	def search(self, target_word = ""):
		import os
		h = []
		for root, _, files in os.walk("data", topdown=False):
			for name in files:
				filename = os.path.join(root, name)
				with open(filename) as file:  
					data = file.read() 
					for w in set(list(tokenize(data, deacc = True))):
						score = self.model.wv.similarity(target_word, w)
						heappush(h,(score, w, filename))
						if len(h) > self._num:
							heappop(h)
		return h

	def beautifulPrint(self, h):
		while h:
			data = heappop(h)
			print("{}:\t{}\tscore:{}".format(data[2],data[1],data[0]))