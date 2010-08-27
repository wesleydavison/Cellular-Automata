'''
Created on Aug 25, 2010

@author: Davison
'''

from MappingTable import MappingTable
#import threading


#class Cell(threading.Thread):
class Cell():
    '''
    This class represents a cell of an automata
    '''
    def __init__(self):
        self.actualState = ["empty"]
        self.mappingTable = MappingTable()
        #threading.Thread.__init__(self)
        
    def receiveSignal(self,signal, in_states):
        self.actualState = self.mappingTable.map(signal, in_states)
    
    def sendSignal(self):
        return self.actualState
    
    
    #def setState(self, newState):
    #    self.actualState = newState
        
    #def run(self):
    #    return self.receiveSignal()