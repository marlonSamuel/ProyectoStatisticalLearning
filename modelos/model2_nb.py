#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
import numpy as np


# In[211]:


X_train = pd.read_csv('X_train.csv')
Y_train = pd.read_csv('Y_train.csv')

class NaiveBayes():
    def fit(self,X,y):
        data = X.copy()
        data['passenger_survived'] = y['passenger_survived']
        self.priors = data.groupby('passenger_survived').size().div(len(data))#priors probabilities
        self.classes = sorted(y['passenger_survived'].unique()) #get classes
        self.probs_c = [[],[]]
        
        for d in data[X.columns.values]:
            a = data.groupby([d, 'passenger_survived']).size().div(len(data)).div(self.priors, axis=0, level='passenger_survived')
            #self.po = data.groupby(d).size().div(len(data))
            for i,p in enumerate(self.probs_c):
                pro = [a[i][0],a[i][1]]
                p.append(pro)
    
    def predictPior(self,x,probs_priori):
        prob = 1
        for i,v in enumerate(probs_priori):
            prob *= v[x[i]]
        return prob
    
    def _predict(self,x):
        probabilities = []
        for i, c in enumerate(self.classes):
            prior = self.priors[i]
            prior_pred = self.predictPior(x,self.probs_c[i])
            probabilities.append(prior*prior_pred)
        probabilities = probabilities/sum(probabilities)
        return self.classes[np.argmax(probabilities)],probabilities
    
    def predict(self,X):
        predictions = []
        probabilities = []
        for x in X:
            pred = self._predict(x)
            predictions.append(pred[0])
            probabilities.append(pred[1])
        return predictions,probabilities
    


# In[228]:

def getPredicts(X_test):
	nb = NaiveBayes()
	nb.fit(X_train,Y_train)
	preds = nb.predict(np.array(X_test))
	return preds

