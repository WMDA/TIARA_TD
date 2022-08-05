#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:58:01 2020

@author: daniel
"""

import pandas as pd
import scipy.io as sio
import os
import numpy as np

root=('/home/daniel/Documents/M_Neuroscience/TD_dissertation/BRCTIARA_responseFiles/Data/onset_csv')
os.chdir(root)

matfile=sio.loadmat('/home/daniel/Documents/M_Neuroscience/TD_dissertation/BRCTIARA_responseFiles/Tiara_DelayDiscount_RespFiles/onset_BRCTIARA019_A.mat')
#print(matfile['names'])

df = pd.read_csv('BRCTiara_DelayDiscounting_019_A.csv').dropna()

ll= df.loc[df['Chosen']== 100]


ll_mat=matfile['onsets'][0]
ss_mat=matfile['onsets'][1]
#ll_onset= ll['']

ss= df.loc[(df['Chosen'] < 100) | (df['Chosen']>100)]
#onset=df['']