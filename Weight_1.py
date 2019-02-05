#Author: Dr. Vishal Bhardwaj [IISER Mohali]
#
#Usage python Weight_1.py ./path_to_h5_file

import sys
import os
import pickle
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#branch_names="""cosbt, costhr, mthro,
#mthrs, deltaz, 
#qrnn, k_lr0, cosb, 
#cone1, cone2, cone3,
#cone4, cone5, cone6,
#cone7, cone8, cone9""".split(",")
#branch_names = [c.strip() for c in branch_names]


branch_names = ["B_ThrustB", "B_ThrustO", "B_CosTBTO","B_CosTBz","B_cc1","B_cc2","B_cc3","B_cc4","B_cc5","B_cc6","B_cc7","B_cc8","B_cc9",
"B_mm2","B_et","B_hso00","B_hso01","B_hso02","B_hso03","B_hso04","B_hso10","B_hso12","B_hso14","B_hso20",
"B_hso22","B_hso24","B_hoo0","B_hoo1","B_hoo2","B_hoo3","B_hoo4","B_qpElectron","B_qpFSC","B_qpFastHadron",
"B_qpIntermediateElectron","B_qpIntermediateMuon","B_qpIntermediateKinLepton","B_qpKaon","B_qpKaonPion","B_qpKinLepton",
"B_qpLambda","B_qpMaximumPstar","B_qpMuon","B_qpSlowPion"]

Outputs = ["Signal", "Background"]

from keras.models import load_model
path = sys.argv[1]
#model=load_model("CC_SGD_44_64_64_64_2_nodropout.h5")
model=load_model(path)
from keras.utils import plot_model

weights = []
no_layers = len(model.layers)

for i in range(no_layers):
	weights.append(model.layers[i].get_weights())

#weights_0 = model.layers[0].get_weights()
#weights_1 = model.layers[1].get_weights()
#weights_2 = model.layers[2].get_weights()
#weights_3 = model.layers[3].get_weights()
#weights_4 = model.layers[4].get_weights()
#weights_5 = model.layers[5].get_weights()
#weights_6 = model.layers[6].get_weights()


from numpy import ndarray

Wi = []
for i in range(no_layers):
	dim1 = len(weights[i][0])
	dim2 = len(weights[i][1])
	Wi.append([ndarray((dim1,dim2),float),ndarray((dim2),float)])

#Wi_0_0 = ndarray((17,256),float)   Wi[0][0]
#Wi_0_1 = ndarray((256),float)      Wi[0][1]  

#Wi_2_0 = ndarray((256,128),float)  
#Wi_2_1 = ndarray((128),float)

#Wi_4_0 = ndarray((128,64),float)
#Wi_4_1 = ndarray((64),float)

#Wi_6_0 = ndarray((64),float)
#Wi_6_1 = ndarray((1),float)

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
	       
#myfuncs.visweight.fill_plot_1D(Wi_4_1,weights_4,1,"Layer_4_o_M1.png")
#myfuncs.visweight.fill_plot_1D(Wi_2_1,weights_2,1, "Layer_2_o_M1.png")
#myfuncs.visweight.fill_plot_1D(Wi_0_1,weights_0,1,"Layer_0_o_M1.png")

#myfuncs.visweight.fill_plot_1D(Wi_6_0,weights_6,0, "Layer_6_i_M1.png")
#myfuncs.visweight.fill_plot_1D(Wi_6_1,weights_6,1,"Layer_6_o_M1.png")


#myfuncs.visweight.fill_plot_2D(Wi_4_0,weights_4, 18,25,-10,10,'vertical', 'Layer 4 Weight Map',1,'Layer_4_Input_Weight_M1.png')
#myfuncs.visweight.fill_plot_2D(Wi_2_0,weights_2,15,25,-10,10,'vertical', 'Layer 2 Weight Map',0.8,'Layer_2_Input_Weight_M1.png')
#myfuncs.visweight.fill_plot_2D(Wi_0_0,weights_0,25,7,-10,10,'horizontal', 'Layer 0 Weight Map',0.9,'Layer_0_Input_Weight_M1.png')




#import myfuncs.nnplot

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

#myfuncs.nnplot.DrawConnectionsWModif(ax1,0.10,0.2,0.05,0.6,17, 0.25,0.05,0.1,0.9,256,Wi_0_0)
#print('Layer 1 done')
#plt.text(0.05,0.01,'Input Variables', fontsize=15,color='blue',family='monospace')


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



#myfuncs.nnplot.Myrectangle(ax1,0.25,0.05,0.1,0.9,1,'salmon')
#myfuncs.nnplot.DrawBoxesWModif(ax1,0.25,0.05,0.1,0.9,256,Wi_0_1)
#myfuncs.nnplot.DrawConnectionsWModif(ax1,0.25,0.05,0.1,0.9,256, 0.45,0.15,0.1,0.7,128,Wi_2_0)
#print('Layer 2 done')
#plt.text(0.25,0.01,'Hidden Layer 1', fontsize=15,color='blue',family='monospace')

#myfuncs.nnplot.Myrectangle(ax1,0.45,0.15,0.1,0.7,1,'salmon')
#myfuncs.nnplot.DrawBoxesWModif(ax1,0.45,0.15,0.1,0.7,128,Wi_2_1)
#myfuncs.nnplot.DrawConnectionsWModif(ax1,0.45,0.15,0.1,0.7,128, 0.65,0.25,0.1,0.5,64,Wi_4_0)
#print('Layer 3 done')
#plt.text(0.45,0.01,'Hidden Layer 2', fontsize=15,color='blue',family='monospace')



#myfuncs.nnplot.Myrectangle(ax1,0.65,0.55,0.1,0.2,1,'salmon')
###scaled=pow(10,90)
#myfuncs.nnplot.DrawBoxesWModif(ax1,0.65,0.25,0.1,0.5,64,Wi_4_1)

#myfuncs.nnplot.DrawConnectionsWLastModif(ax1,0.65,0.25,0.1,0.5,64, 0.85,0.475,0.1,0.05,1,Wi_6_0)
#print('Layer 4 done, Here is your plot. Please wait for a minute..')
#plt.text(0.65,0.01,'Hidden Layer 3', fontsize=15,color='blue',family='monospace')


#nnplot.Myrectangle(ax1,x1,y1,0.1,0.03,1,'salmon','salmon',0.5)

nnplot.Myrectangle(ax1,x1,0.2,0.05,0.15,1,'blue','blue',0.7)
nnplot.Myrectangle(ax1,x1,0.65,0.05,0.15,1,'red','red',0.7)
#nnplot.DrawLine(ax1,x1,0.2,0.05,0.6,dim2,'salmon')
#nnplot.WriteVariables(ax1,x1+0.2,0.27,0.05,0.6,dim2,Outputs)
nnplot.WriteVariables(ax1,x1+0.17,0.2,0.05,0.13,1,["SIGNAL"])
nnplot.WriteVariables(ax1,x1+0.17,0.65,0.05,0.13,1,["BACKGROUND"])

plt.text(x1,0.01,'Output NN', fontsize=15,color='blue',family='monospace')
plt.savefig("Final_Network_256_M1.png", format='png',dpi=300)

