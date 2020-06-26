# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:48:12 2020

@author: senpai
"""

import numpy as np

def getValueProb(c, x,means,variances):
        mean = means[c]
        var = variances[c]
        numerator = np.exp(- (x-mean)**2 / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator

    
def predict(x,classes,means,variances,priors):
    posts = []
    for i,c in enumerate(classes):
        prior = np.log(priors[i])#obtenemos la probabilidad de la clase
        post = np.sum(np.log(getValueProb(i,x,means,variances)))
        post = post + prior
        posts.append(post)
    return classes[np.argmax(posts)]#retornamos la probabilidad mayor