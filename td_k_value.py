#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:14:00 2020

@author: daniel
"""

import os
import pandas as pd

os.chdir('')

df = pd.read_csv('')

def simulatechoice(k,sir,ldr,delay):
    value = (ldr/(1 +k*delay))-sir
    if value>=0:
        return 1
    else:
        return 0
