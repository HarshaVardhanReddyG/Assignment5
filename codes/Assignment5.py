# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fEZxZgollo5k94Kk_NMkDqMeeLC82nWC
"""

import numpy as np
from numpy import random as RN 
#Total possible outcomes
N=4
#no of outcomes favourable for F
n_1=3
#no of outcomes favourable for E and F
n_2=1
#respective theoritical probabilities
pr_1=n_1/N
pr_2=n_2/N
#initialising all the frequencies to 0
x_1=0
x_2=0
#(b,b)=1,(b,g)=2,(g,b)=3,(g,g)=4 (say)
for i in range(N):
    x = np.random.choice([i for i in range(1,5)])
    if (x==1 or x==2 or x==3):
        x_1+=1
    if (x==1):
        x_2+=1
print("Theoritical probabilities are ",pr_1,pr_2)
print("Experimental probabilities are",x_1/N,x_2/N)