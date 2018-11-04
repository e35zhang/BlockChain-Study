from littleChain import *
from badGuy import *

c = Chain(4)
c.createGenesis()
c.addBlock(littleBlock("A -$8; C +$8"))
c.addBlock(littleBlock("A -$8; C +$8"))
c.addBlock(littleBlock("C -$6; A +$6"))
c.addBlock(littleBlock("F -$3; I +$3"))
c.addBlock(littleBlock("L -$9; W +$9"))
c.addBlock(littleBlock("S -$5.5; O +$5.5"))

c.isChainValid()

Hack(c,1,"L -$1000; H +$1000")
c.isChainValid()
c.printChain()
print("len",len(c.blocks[0].hash))