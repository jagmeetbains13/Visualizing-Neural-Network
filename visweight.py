# Vishal Bhardwaj
#
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy import ndarray

def plot_1D(X, array, save_fig='NONE'):
    plt.plot(X, array, linewidth=0,marker='.')


def fill_plot_1D(array, weight, ibin=1, save_file='NONE'):
    iR=len(array)
    XX = ndarray(iR,float)
    for i in range(iR):
        array[i]= weight[ibin][i]
        XX[i]=i
        
    plt.plot(XX, array, linewidth=0,marker='.')
    if save_file != "NONE":
        plt.savefig(save_file)#, format='svg')
        #plt.show()
    else:
        plt.show()

        


def plot_2D(array, save_fig='NONE'):
    fig = plt.figure(figsize=(30,15))
    
    ax = fig.add_subplot(111)
    ax.set_title('Layer1_Weights')
    imgplot = plt.imshow(Wi_0_0)
    imgplot.set_cmap('bwr') #spectral #Greys
    ax = fig.add_subplot(111)
    ax.set_title('Weights MAP')
    imgplot = plt.matshow(Wi_0)







def fill_plot_2D_NO(array,weight,X1=15,X2=22,hori='horizontal',save_file='NONE'):
    iR = len(array)
    jR = len(array[0])
    
    for i in range(iR):
        for j in range(jR):
            array[i][j]= weight[0][i][j]

    fig = plt.figure(figsize=(X1, X2))
    ax = fig.add_subplot(111)
    ax.set_title('Weight Map')
    imgplot = plt.imshow(array)
    imgplot.set_cmap('bwr')
    ax.set_aspect('equal')
    
    cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)
    plt.colorbar(orientation=hori)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    if save_file != "NONE":
        plt.savefig(save_file)#, format='svg')
        plt.show()
    else:
        plt.show()
   



def fill_plot_2D(array,weight,X1=15,X2=22,vMIN=-12,vMAX=12,hori='horizontal',TITLE='Weights',SHRINK=1,save_file='NONE'):
    iR = len(array)
    jR = len(array[0])
    
    for i in range(iR):
        for j in range(jR):
            array[i][j]= weight[0][i][j]

    fig = plt.figure(figsize=(X1, X2))
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)

    ax = fig.add_subplot(111)
    ax.set_title(TITLE, fontsize=28)
    imgplot = plt.imshow(array,vmin=vMIN,vmax=vMAX)
    imgplot.set_cmap('bwr')
    ax.set_aspect('equal')
    
    cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)
    plt.colorbar(orientation=hori,shrink=SHRINK)
    if save_file != "NONE":
        plt.savefig(save_file)#, format='svg')
        #plt.show()
    else:
        plt.show()


        
