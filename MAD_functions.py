# -*- coding: utf-8 -*-
"""
Created on Fri Jul 08 15:34:31 2016

@author: Michela
"""
import numpy as np

def doubleMAD_mask(y,thresh):
    '''It returns a boolean vector where the trues are associated to the good values and the falses with the ouliers'''
    # warning: this function does not check for NANs
    # nor does it address issues when 
    # more than 50% of your data have identical values
    m = np.median(y)
    abs_dev = np.abs(y - m)
    left_mad = np.median(abs_dev[y<=m])
    right_mad = np.median(abs_dev[y>m])
    y_mad = np.zeros(len(y))
    y_mad[y < m] = left_mad
    y_mad[y > m] = right_mad
    control_var= abs_dev/y_mad
    control_var[y==m]=0
    return control_var<thresh
    
    
def MAD_mask(y,thresh):
    m = np.median(y)
    abs_dev = np.abs(y - m)
    y_mad=np.median(abs_dev)
    control_var= abs_dev/y_mad
    control_var[y==m]=0
    return control_var<thresh   
    
    
def MADhigh_mask(y, thresh):
    m = np.median(y)
    abs_dev = np.abs(y - m)
    right_mad = np.median(abs_dev[y>=m])
    y_mad = np.zeros(len(y))
    y_mad[y > m] = right_mad
    control_var = np.zeros(len(y))
    control_var[y>m]= abs_dev[y>m]/y_mad[y>m]
    return control_var<thresh    
    
    
def MADhigh(y):
    m = np.median(y)
    abs_dev = np.abs(y - m)
    right_mad = np.median(abs_dev[y>=m])
    return right_mad  
    
def MAD(y):
    m = np.median(y)
    abs_dev = np.abs(y - m)
    y_mad=np.median(abs_dev)
    return y_mad   
    
def doubleMAD(y):
    m = np.median(y)
    abs_dev = np.abs(y - m)
    left_mad = np.median(abs_dev[y<=m])
    right_mad = np.median(abs_dev[y>m])
    return left_mad, right_mad
    
