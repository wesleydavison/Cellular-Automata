'''
Created on Aug 25, 2010

@author: Davison
'''

from MappingTable import MappingTable
import threading

class Cell(threading.Thread):
    '''
    This class represents a cell of an automata
    '''
    def __init__(self):
        self.mappingTable = MappingTable()
        
    def receiveSignal(self):
        print self.mappingTable.map('K', 'empty')
        
    def run(self):
        print self.receiveSignal()