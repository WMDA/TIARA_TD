#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:14:00 2020
@author: daniel
"""

import os
import pandas as pd
import numpy as np
import scipy.optimize as sp
import math
import sys

'''
Currently does not as code has not been completed, please do not run
untill completed.
'''

def find_files():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if 'Tiara_DelayDiscount_RespFiles' in root:
                return root

def simulatechoice(k,sir,ldr,delay):
    value = (ldr/(1 +k*delay))-sir
    choice=[]
    for i in value:
        if i>=0:
             choice.append(1)
        else:
            choice.append(0)
    return choice

def getPchoice(df,k):
    df=df.astype(float)
    p_choice=[]
    for index,row in df.iterrows():
        if row.Choices==1:
            pchoice= np.exp(row.LDR/(1+ (k* row.Delay))) / (np.exp(row.SIR) + np.exp(row.LDR/(1+ k*row.Delay)))
            p_choice.append(pchoice)
        else:
             pchoice = (1 -(np.exp(row.LDR/(1 + k*row.Delay)) / (np.exp(row.SIR) + np.exp(row.LDR/(1 + k*row.Delay)))))
             p_choice.append(pchoice)
    return p_choice

def generateloglik(k):
    p=getPchoice(df,k)
    sumloglik=(-1)*(sum(np.log(p)))
    return sumloglik

os.chdir()
root=os.getcwd()

kvalues=[]
participants=[]
for r, dirs, files in os.walk(root):
    for file in files:
        if file.endswith('forfit.csv'):
            participant = file.strip('_forfit.csv')
            participants.append(participant)
            df=pd.read_csv(file)
            kvalue=sp.fminbound(generateloglik,0,1)
            kvalues.append(kvalue)
            print(participant,' : ',kvalue)

df= {'Participants':participants,'Kvalues':kvalues}
kvalues_df= pd.DataFrame(df)

kvalues_df.to_csv('kvalues.csv',index=False)
