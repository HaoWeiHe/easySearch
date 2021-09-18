from gensim.utils import tokenize
from  heapq import heappop, heappush

class earsySearch():
	def __init__(self, NUM = 10):
		self._num = NUM 
		self.glove_input_file = 'model/glove.6B.200d.txt'
		self.word2vec_output_file = 'model/glove.6B.200d.txt.w2v'
		self.model = self.load_mode()
		self.ignore = ["data/.keep"]

	def train(self):
		from gensim.scripts.glove2word2vec import glove2word2vec
		glove2word2vec(self.glove_input_file , self.word2vec_output_file)

	def load_mode(self):
		from gensim.models import KeyedVectors
		model = KeyedVectors.load_word2vec_format(self.word2vec_output_file, binary = False, limit = 500000)
		return model

	def search(self, target_word = ""):
		import os
		
		if target_word not in self.model.wv:
			target_word = target_word.lower()
		if target_word not in self.model.wv:
			return "OOV"

		h = [] 
		for root, _, files in os.walk("data", topdown=False):
			for name in files:
				hi_score, rtr_w = 0, ""
				filename = os.path.join(root, name)
				with open(filename) as file:  
					if filename in self.ignore :
						continue
					data = file.read() 
					for w in set(list(tokenize(data, deacc = True))):
						#OOV 
						if w not in self.model.wv:
							continue
						score = self.model.wv.similarity(target_word, w)
						if score > hi_score:
							hi_score = score
							rtr_w = w
				heappush(h,(hi_score,filename))
				if len(h) > self._num:
					heappop(h)
		return h

	def beautifulPrint(self, h):
		while h:
			data = heappop(h)
			if data == "OOV":
				print("sorry, the input query doesn't exist in our dictionary")
			print("{}:\tscore:{:0.3f}".format(data[1],data[0]))