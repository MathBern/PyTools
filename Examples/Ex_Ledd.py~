import sys

import matplotlib.pyplot as plt

sys.path.append("/home2/matheus15/Tratamento_de_Dados/PyTools/PyTools")

import __init__ as PT

def plot_Ledd_masses_1_100():
	list_masses =range(1,101)	
	list_L = []	
	for m in list_masses:
		list_L.append(PT.Ledd_L0(m))
	
	plt.scatter(list_masses,list_L)
	plt.show()

plot_Ledd_masses_1_100()
