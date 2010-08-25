'''
Created on Aug 25, 2010

@author: davison
'''

class MappingTable:
    '''
    Table of information present on a cell of an automata.
    '''
    def __init__(self):
        self.mapTable = {}
        self.stateSet = ['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'empty']
        self.inputAlphabet = ['L', 'A', 'M', 'K']
        
        #creating mapping
        self.createMapTable()
    
    def createMapTable(self):
        key1 = ('L', self.stateSet[1])
        key2 = ('X', self.stateSet[2])
        key3 = ('X', self.stateSet[3])
        key4 = ('A', self.stateSet[4])
        key5 = ('M', self.stateSet[4])
        key6 = ('X', self.stateSet[5])
        key7 = ('K', self.stateSet[6])

        self.mapTable[key1] = self.stateSet[0]
        self.mapTable[key2] = self.stateSet[1]
        self.mapTable[key3] = self.stateSet[2]
        self.mapTable[key4] = self.stateSet[3]
        self.mapTable[key5] = self.stateSet[3]
        self.mapTable[key6] = self.stateSet[4]
        self.mapTable[key7] = self.stateSet[5]
        
        
    def map(self, in_symbol, in_state):
        return self.mapTable[(in_symbol, in_state)]
        
        

        