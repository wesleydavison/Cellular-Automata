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

        self.mapTable[key1] = [self.stateSet[0]] #L,S1 -> S0
        self.mapTable[key2] = [self.stateSet[1]] #X,S2 -> S1
        self.mapTable[key3] = [self.stateSet[1], self.stateSet[2]] #X,S3 -> S1 & S2
        self.mapTable[key4] = [self.stateSet[3]] #A,S4 -> S3
        self.mapTable[key5] = [self.stateSet[3]] #M,S4 -> S3
        self.mapTable[key6] = [self.stateSet[4]] #X,S5 -> S4
        self.mapTable[key7] = [self.stateSet[5]] #K,empty-> S5
        
        
    def map(self, in_symbol, in_states):
        symbol_filt = in_symbol
        if in_symbol not in self.inputAlphabet:
            print "symbol " + in_symbol + " not in alphabet. Substituting by 'X'"
            symbol_filt = 'X'
        out_states = []
        for st in in_states:  
            if self.mapTable.has_key((symbol_filt, st)):
                out_states = out_states + self.mapTable[(symbol_filt, st)]
        if len(out_states) is 0:
            out_states.append('empty')
        
        return out_states
        

        