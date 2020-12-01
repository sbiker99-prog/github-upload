'''
Created on 24.11.2020

@author: sbiker99-prog
'''

class MaxSum(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
      
    def calc(self, ls):
        res = [0,0]
        for i in range(len(ls)):
            res = [max(res), max(min(res), ls[i])]
        return res[0] + res[1]       
    
    def calc_max_efficient(self, ls):
        ceil_val = max(ls)
        ceil_index = ls.index(ceil_val)
        ls[ceil_index] = 0
        sec_val = max(ls) 
        return ceil_val + sec_val