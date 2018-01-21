'''
blockchain of the naive_blockchain
Created by Xingfan Xia
@10:24 PM 01-20-2018
'''
import hashlib, json, time

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

		# The Genesis Block
		self.new_block(previous_hash=1, proof=99)

	@property
	def last_block(self):
		"""
		:return: the last block in chain
		"""
		return self.chain[-1]

	def new_block(self, proof, previous_hash=None):
		"""
		Create a new Block in the Blockchain

		:param proof: <int> The proof of work given by working the proof of work algorithm
		:param previous_hash: (Optional) <str> Hash of previous Block in the Blockchain
		:return: <dict> New Block
		"""

		block = {
			'index': len(self.chain) + 1,
			'timestamp': time.time(),
			'transactions': self.current_transactions,
			'proof': proof,
			'previous_hash': previous_hash or self.hash_block(self.last_block)
		}

		self.current_transactions = [] # Reset current ledge of transactions
		self.chain.append(block)

		return block

	
	def new_transaction(self, sender, recipient, amount):
		"""
		:param sender: <str> hash address of Sender
		:param recipient: <str> hash address of Recipient
		:param amount: <float> amount of transaction value
		:return: <int> index pointer to the block that holds this transaction in the chain
		"""
		self.current_transactions.append({
				'sender': sender,
				'recipient': recipient,
				'amount': amount
			}
		)
		return self.last_block['index'] + 1

	@staticmethod
	def hash_block(block):
		"""
		Create a SHA-256 hash of a Block

		:param block: <dict> Block to be hashed
		:return: <str> hash_str
		"""

		block_str = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(block_str).hexdigest()

	@staticmethod
	def validate_proof(last_proof, proof):
		"""
		Validate if the hash of  f'{last_proof}{proof}'.encode() has leading \
		digits 23333

		:param last_proof: <int> Previous proof
		:param proof: <int> Current proof
		:return: <bool> True if having leading '23333'; vice versa
		"""
		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()

		return guess_hash[:5] == '23333'


	def proof_of_work(self, last_proof):
		"""
		Naive proof of work algorithm:
			- p for proof, p' for last proof
			- Find a integer p s.t. hash(pp') has leading '23333'

		:param last_proof: <int> last proof
		:return:  <int> proof
		"""
		proof = 0
		while self.validate_proof(last_proof, proof) is False:
			proof += 1

		return proof