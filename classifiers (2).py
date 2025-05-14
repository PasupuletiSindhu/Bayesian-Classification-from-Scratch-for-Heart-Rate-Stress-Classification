''' Import Libraries'''
import pandas as pd
import numpy as np


class Classifier:
    ''' This is a class prototype for any classifier. It contains two empty methods: predict, fit'''
    def __init__(self):
        self.model_params = {}
        pass
    
    def predict(self, x):
        '''This method takes in x (numpy array) and returns a prediction y'''
        raise NotImplementedError
    
    def fit(self, x, y):
        '''This method is used for fitting a model to data: x, y'''
        raise NotImplementedError

            
class Prior(Classifier):
    
    def __init__(self):
        ''' Your code here '''
        super().__init__()
    

    def predict(self, x):
        '''This method takes in x (numpy array) and returns a prediction y'''
        return max(self.model_params, key=self.model_params.get)
    
    def fit(self, x, y):
        '''This method is used for fitting a model to data: x (numpy array), y (numpy array)'''
        uni = []
        freq = []
        
        for label in y:
            if label in uni:
                idx = uni.index(label)
                freq[idx] += 1
            else:
                uni.append(label)
                freq.append(1)
        
        total = len(y)
        self.model_params = {uni[i]: freq[i] / total for i in range(len(uni))}
        