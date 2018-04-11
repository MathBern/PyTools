'''
'''

import numpy as np
import pandas as pd

M0 = 1.99e33
L0 = 3.9e33
G_ = 6.67259e-8
m_H = 1.6733e-24
c = 2.99792458e10
sigma_Thomsom = 6.65248e-25

def Ledd_L0(mass_M0): #Return L_Eddington/L_Sun for a star, given its mass.
	return (M0/L0)*4*np.pi*G_*(mass_M0)*m_H*c/sigma_Thomsom

def HelloWorld():
	return "Hello World!"

def Transpose_Table(tableName):
	df = pd.read_csv(tableName, comment = '#')
	return df.T

def Reverse_word(word):
	return word.reverse()
