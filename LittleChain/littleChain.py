import datetime 
import time
import hashlib
class littleBlock:
    
    def __init__(self,dataIn):
        self.index = None
        self.prevHash = None
        self.data = dataIn
        self.nonce = 0
        self.timestamp = datetime.datetime.now().isoformat()


    def getHash(self):
        c = str(self.index) + str(self.nonce) + str(self.data) + str(self.timestamp) + str(self.prevHash)
        self.hash = hashlib.sha256(c.encode()).hexdigest()
        return self.hash

    def checkDiff(self,diff):
        for i in range(0,diff):
            if self.hash[i] != "0":
                return False
        return True

    def mine(self,diff):
        print("Mining block " + str(self.index)+"... ")
        d = time.time()
        self.getHash()
        while not self.checkDiff(diff):
            self.nonce += 1
            self.getHash()
        dt = time.time()-d
        print("Mined in" + str(dt) +" "+self.hash)
        return self.hash

class Chain:
    
    def __init__(self,diff):
        self.diff = diff
        self.blocks = []
        self.number = 0

    def createGenesis(self):
        b = littleBlock("")
        b.index = 0
        b.prehash = "0"
        b.mine(self.diff)
        self.number += 1
        self.blocks.append(b)
    
    def addBlock(self, newBlock):
        newBlock.prevHash = self.getPrevHash()
        newBlock.index = self.number
        newBlock.mine(self.diff)
        self.number += 1
        self.blocks.append(newBlock)

    def getPrevHash(self):
        ph = self.blocks[len(self.blocks)-1].getHash()
        return ph

    def isChainValid(self):
        for i in range(1,len(self.blocks)):
            if i == 0:
                prevHash = "0"
            else:
                prevHash = self.blocks[i-1].getHash()

            if self.blocks[i].prevHash!=prevHash:
                print("Chain is not Valid") 
                return False

            if self.blocks[i].prevHash != self.blocks[i-1].getHash():
                print("hash of block "+ str(i) + " is wrong")
                return False
            
            if not self.blocks[i].checkDiff(self.diff):
                print("No proof of work for block " + str(i))
                return False

        print("Confirmed! Chian is Valid.")
        return True

    def printChain(self):
        for b in self.blocks:
            print("-"*80)
            print("Block " + str(b.index))
            print("Payment :" + str(b.data))
            print("Hash " + str(b.hash))
            print("Previous Hash " + str(b.prevHash))
            print("-"*80)
            print("")