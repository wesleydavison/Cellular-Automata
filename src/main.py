'''
Created on Aug 25, 2010

@author: davison
'''

from CellularAutomata import Cell

if __name__ == '__main__':
    
    list_cell = []
        
    #input_string = 'LLVMVK'
    input_string = 'KPMVLL'
    for i in range(6):
        list_cell.append(Cell())
        
    out_signal = ['empty']
    for i in range(5):
        list_cell[i].receiveSignal(input_string[i], out_signal)
        out_signal = list_cell[i].sendSignal()
        
    for i in range(len(list_cell)):
        print "cell state " + str(i+1) + " is " + str(list_cell[i].sendSignal())
        i = i + 1            
        
   
