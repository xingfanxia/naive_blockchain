'''
blockchain of the naive_blockchain
Created by Xingfan Xia
@10:24 PM 01-20-2018
'''

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

	@property
	def last_block(self):
		"""
		:return: the last block in chain
		"""
		pass

	def new_block(self):
		pass

	def new_translation(self):
		pass

	@staticmethod
	def hash(block):
		pass
	
