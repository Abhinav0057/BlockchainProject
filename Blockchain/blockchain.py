import datetime  # for timestamp
import hashlib  # for hasing the block
import json  # for json files work
from uuid import uuid4  # generate pseudo random numers..


class Blockchain:  # defining our blockchain class
    def __init__(self):
        self.chain = []
        self.trasactions = []
        # proof=1, for the genesis block.
        self.create_block(proof=1, previous_hash='0')
        self.nodes = set()  # crates nodes unordederd set

    def create_block(self, proof, previous_hash):  # create a block
        own_hash = hashlib.sha256(
            str(proof**3 - proof**4).encode()).hexdigest()
        block = {'index': len(self.chain)+1,
               'timestamp': str(datetime.datetime.now()),
               'proof': proof,
               'previous_hash': previous_hash,
               'own_hash': own_hash,
               'trasactions': self.trasactions}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):  # hasing function to find the nonce
        new_proof = 1
        check_proof = False
        while check_proof is False:
             hash_operation = hashlib.sha256(
                 str(proof**3-previous_proof**3-proof+proof*3.14).encode()).hexdigest()
            if hash_operation[:2] == '000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self,block):
        encoded_block=json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    def is_block_valid(self, chain):
        previous_block=chain[0]
        block_index=1
        while block_index < len(chain):
            block=chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof=previous_block['proof']
            proof=block['proof']
            hash_operation=hashlib.sha256(str(proof**3-previous_proof**3-proof+proof*3.14).encode()).hexdigest()
            if hash_operation[:4]!='000':
                return False
            previous_block=block
            block_index+=1
        return True
    
    
    
        
