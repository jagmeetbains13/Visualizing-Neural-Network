# Dr. Vishal Bhardwaj [IISER Mohali]
# Jagmeet Singh [IISER Mohali]
#Usage python Weight_1.py ./path_to_h5_file

import sys
import os
import pickle
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

branch_names = ["B_ThrustB", "B_ThrustO", "B_CosTBTO","B_CosTBz","B_cc1","B_cc2","B_cc3","B_cc4","B_cc5","B_cc6","B_cc7","B_cc8","B_cc9",
"B_mm2","B_et","B_hso00","B_hso01","B_hso02","B_hso03","B_hso04","B_hso10","B_hso12","B_hso14","B_hso20",
"B_hso22","B_hso24","B_hoo0","B_hoo1","B_hoo2","B_hoo3","B_hoo4","B_qpElectron","B_qpFSC","B_qpFastHadron",
"B_qpIntermediateElectron","B_qpIntermediateMuon","B_qpIntermediateKinLepton","B_qpKaon","B_qpKaonPion","B_qpKinLepton",
"B_qpLambda","B_qpMaximumPstar","B_qpMuon","B_qpSlowPion"]

Outputs = ["Signal", "Background"]

from keras.models import load_model
path = sys.argv[1]
model=load_model(path)
from keras.utils import plot_model

weights = []
no_layers = len(model.layers)

for i in range(no_layers):
	weights.append(model.layers[i].get_weights())

from numpy import ndarray

Wi = []
for i in range(no_layers):
	dim1 = len(weights[i][0])
	dim2 = len(weights[i][1])
	Wi.append([ndarray((dim1,dim2),float),ndarray((dim2),float)])

import visweight

for i in range(no_layers):
	#1D Plots
	fil_name = "Layer_" + str(i) + "_i_M1.png"
	visweight.fill_plot_1D(Wi[i][0],weights[i],0, fil_name)
	
	fil_name = "Layer_" + str(i) + "_o_M1.png"
	visweight.fill_plot_1D(Wi[i][1],weights[i],1,fil_name)
	
	#2D Plots
	fil_name = "Layer_" + str(i) + "_Input_Weight_M1.png"
	plot_name = "Layer " + str(i) + " Weight Map"
	visweight.fill_plot_2D(Wi[i][0],weights[i],25,7,-10,10,'horizontal', plot_name,0.9,fil_name)
	       
import nnplot


fig1=plt.figure(figsize=(15,10))
plt.xticks(fontsize=0)
plt.yticks(fontsize=0)
plt.axis('off')
ax1 = fig1.add_subplot(111)#, aspect='equal')

dim1 = len(weights[0][0])
dim2 = len(weights[0][1])


y1 = 0.16
h1 = 0.643


nnplot.Myrectangle(ax1,0.10,y1,0.05,h1,1,'salmon','salmon',0.3)
nnplot.Myrectangle(ax1,0.10,y1,0.05,h1,1,'salmon')
nnplot.DrawLine(ax1,0.10,y1,0.05,h1,dim1,'salmon')
nnplot.WriteVariables(ax1,0.15-0.1,0.16,0.05,0.65,dim1,branch_names)


#Input Layer


nnplot.DrawConnectionsWModif(ax1,0.10,y1,0.05,h1,dim1, 0.25,0.05,0.1,0.9,dim2,Wi[0][0])
print('Layer 0 done')
plt.text(0.05,0.01,'Input Variables', fontsize=15,color='blue',family='monospace')

#Hidden Layers
num_hidden = no_layers - 1
x1 = 0.25
y1 = 0.05

for i in range(num_hidden):
	i = i+1
	dim1 = len(weights[i][0])
	dim2 = len(weights[i][1]) 
	nnplot.Myrectangle(ax1,x1,y1,0.1,0.9,1,'salmon')
	nnplot.DrawBoxesWModif(ax1,x1,y1,0.1,0.9,dim1,Wi[i-1][1])
	nnplot.DrawConnectionsWModif(ax1,x1,y1,0.1,0.9,dim1, x1+0.2  , y1  ,0.1,0.9,dim2,Wi[i][0])
	print('Layer ' + str(i) +  ' done')
	lname = 'Hidden Layer ' + str(i)
	plt.text(x1,0.01,lname, fontsize=15,color='blue',family='monospace')
	x1 = x1 + 0.2
	y1 = y1 



nnplot.Myrectangle(ax1,x1,0.2,0.05,0.15,1,'blue','blue',0.7)
nnplot.Myrectangle(ax1,x1,0.65,0.05,0.15,1,'red','red',0.7)
#nnplot.DrawLine(ax1,x1,0.2,0.05,0.6,dim2,'salmon')
#nnplot.WriteVariables(ax1,x1+0.2,0.27,0.05,0.6,dim2,Outputs)
nnplot.WriteVariables(ax1,x1+0.17,0.2,0.05,0.13,1,["SIGNAL"])
nnplot.WriteVariables(ax1,x1+0.17,0.65,0.05,0.13,1,["BACKGROUND"])

plt.text(x1,0.01,'Output NN', fontsize=15,color='blue',family='monospace')
plt.savefig("Final_Network_256_M1.png", format='png',dpi=300)

