import datetime  # for timestamp
import hashlib  # for hasing the block
import json  # for json files work
from uuid import uuid4  # generate pseudo random numers..
from flask import Flask 


class Blockchain:  # defining our blockchain class
    def __init__(self):
        self.chain = []
        self.trasactions = []
        # proof=1, for the genesis block.
        self.create_block(proof=1, previous_hash='0')
       # self.nodes = set()  # crates nodes unordederd set

    def create_block(self, proof, previous_hash):  # create a block
                block = {'index': len(self.chain)+1,
               'timestamp': str(datetime.datetime.now()),
               'proof': proof,
               'previous_hash': previous_hash,
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
                 str(new_proof**3-previous_proof**3-new_proof+previous_proof*3.14).encode()).hexdigest()
            if hash_operation[:4]!='0000':
                check_proof = False
                new_proof= new_proof+1
            else:
                check_proof=True
            
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
            hash_operation= hashlib.sha256(
                 str(new_proof**3-previous_proof**3-new_proof+previous_proof*3.14).encode()).hexdigest()
            if hash_operation[:4]!='0000':
                return False
            previous_block=block
            block_index+=1
        return True
     
    
   
        
    

app=Flask(__name__)

# creating node address on the port 5000




blockchain=Blockchain()

@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block=blockchain.get_previous_block()
    previous_proof=previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash=blockchain.hash(previous_block)
 
    block = blockchain.create_block(proof, previous_hash)
  
    response={'message':"New block has been mined and added",
               'index':block['index'],
               'timestamp':block['timestamp'],
               'proof': block['proof'],
               'previous_hash': block['previous_hash'],
               'trasactions':block['trasactions']}
    return response, 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    response={'chain':blockchain.chain,
              'len':len(blockchain.chain)}
    return response, 200
    
app.run(host='0.0.0.0', port=5000)

    
    
    
        
