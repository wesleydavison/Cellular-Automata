'''
Created on Aug 25, 2010

@author: Davison
'''

from MappingTable import MappingTable

class Cell:
    '''
    This class represents a cell of an automata
    '''
    def __init__(self):
        self.mappingTable = MappingTable()
        
    def receiveSignal(self):
        print self.mappingTable.map('K', 'empty')
        


        
        