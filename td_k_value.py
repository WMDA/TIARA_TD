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



'''
Currently does not as code has not been completed, please do not run 
untill completed. 
'''

def find_files():
    #Works on my system at home but needs further testing.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if 'Tiara_DelayDiscount_RespFiles' in root:
                return root

def simulatechoice(k,sir,ldr,delay):
    value = (ldr/(1 +k*delay))-sir
    if value>=0:
        return 1
    else:
        return 0

def getPchoice(k,sir,ldr,delay,realchoice):
    if realchoice==1:
        p_choice=mat.exp()

def generateloglik(cur_k,length):
    choiceprobabilities= np.zeros(len(choices))
    for i in choiceprobabilities:
        choiceprobabilities= 

root=find_files()

for i in root:
    if "forfit" in i:
        df = read.csv(i)
        x,y=sp.fmin(generateloglik())