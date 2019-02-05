# Vishal Bhardwaj
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy import ndarray


import matplotlib.patches as patches
from matplotlib import lines
def Myrectangle(ax1,x1,y1,width, height,Linewidth='2',Edgecolor='red',FColor='none',Alpha=1):
    ax1.add_patch(
        patches.Rectangle(
            (x1, y1),   # (x,y)
            width,          # width
            height,          # height
            linewidth=Linewidth,
            edgecolor=Edgecolor,
            facecolor=FColor,
            alpha=Alpha
        )
    )



 
 
    
def DrawLine(ax1,x1,y1,width,height,Ndim,Color='r'):
    for i in range(Ndim-1):
        x2 = x1+width
        y1= y1 + height/Ndim
        X=[x1,x2]
        Y=[y1,y1]
        line = matplotlib.lines.Line2D(X, Y, lw=1., color=Color, alpha=0.5)
        ax1.add_line(line)

#Optimized Draw




def DrawBoxesWModif(ax1,x1,y1,width,height,Ndim, Weight):
    MaxAlpha=np.amax(Weight)
    MinAlpha=np.amin(Weight)
    iMODE=10
    if (MinAlpha*MaxAlpha < 0):
        iMODE=-10
        
    len_i=len(Weight)
    AlphaArr = ndarray((len_i,), float)
    AlphaArrP = ndarray((len_i,), float)
    AlphaArrM = ndarray((len_i,), float)

    for i in range(Ndim):
                AlphaArr[i]=0
    
    if (iMODE >0):
        Diff_W=abs(MaxAlpha) - abs(MinAlpha)
        for i in range(Ndim):
            if(Weights[i]>0):
                AlphaArr[i]=(abs(Weight[i])-abs(MinAlpha))/Diff_W
            else:
                AlphaArr[i]=(abs(Weight[i])-abs(MaxAlpha))/abs(Diff_W)
              
                    
    if (iMODE<0):
        Diff_P=MaxAlpha
        Diff_M=abs(MinAlpha)
        for i in range(Ndim):
            if (Weight[i]>0):
                AlphaArr[i]=(abs(Weight[i]))/Diff_P
            if (Weight[i]<0):
                AlphaArr[i]=(abs(Weight[i]))/Diff_M
        
    for i in range(Ndim):
        x2 = x1+width
        y1= y1 + height/Ndim
        y=y1-height/Ndim
        if (Weight[i]>0):
            Alpha=AlphaArr[i]
            Myrectangle(ax1,x1,y,width, height/Ndim,1,'green','green',Alpha)
        elif (Weight[i]<0):
            Alpha=AlphaArr[i]
            Myrectangle(ax1,x1,y,width, height/Ndim,1,'red','red',Alpha)
        else:
            Myrectangle(ax1,x1,y,width, height/Ndim,1,'red','red',0)






def WriteVariables(ax1,x1,y1,width,height,Ndim,Labels):
    font = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'medium',
        'size': 9,
        }
    for i in range(Ndim):
        x2 = x1+width
        y1= y1 + height/(Ndim+1)
        X=[x1,x2]
        Y=[y1,y1]
        name=Labels[i]
        plt.text(x1-0.1,y1, name, fontdict=font)



def DrawConnectionsWModif(ax1, x1_0, y1_0, width_0, height_0, Ndim_0,
                          x1_1, y1_1, width_1, height_1, Ndim_1, Weight):
    MaxAlpha=np.amax(Weight)
    MinAlpha=np.amin(Weight)
    iMODE=10
    if (MinAlpha*MaxAlpha < 0):
        iMODE=-10
        
    len_i=len(Weight)
    len_j=len(Weight[0])
    AlphaArr = ndarray((len_i, len_j), float)
    AlphaArrP = ndarray((len_i, len_j), float)
    AlphaArrM = ndarray((len_i, len_j), float)
    for i in range(Ndim_0):
            for j in range (Ndim_1):
                AlphaArr[i][j]=0

    if (iMODE >0):
        Diff_W=abs(MaxAlpha) - abs(MinAlpha)
        for i in range(Ndim_0):
            for j in range (Ndim_1):
                if(Weights[i][j]>0):
                    AlphaArr[i][j]=(abs(Weight[i][j])-abs(MinAlpha))/abs(Diff_W)
                else:
                    AlphaArr[i][j]=(abs(Weight[i][j])-abs(MaxAlpha))/abs(Diff_W)
                       
    if (iMODE<0):
        Diff_P=MaxAlpha
        Diff_M=abs(MinAlpha)
        for i in range(Ndim_0):
            for j in range (Ndim_1):
                if (Weight[i][j]>0):
                    AlphaArr[i][j]=(abs(Weight[i][j]))/abs(Diff_P)
                if (Weight[i][j]<0):
                    AlphaArr[i][j]=(abs(Weight[i][j]))/abs(Diff_M)
    
    for i in range(Ndim_0):
        x2_0 = x1_0+width_0
        y1_0= y1_0 + height_0/Ndim_0
        y2_0 = y1_0 - 0.5*(height_0/Ndim_0)
        y11_1 = y1_1
        for j in range(Ndim_1):
                x2_1=x1_1
                y11_1= y11_1 + height_1/Ndim_1
                y2_1 = y11_1 - 0.5*(height_1/Ndim_1)
                X=[x2_0,x1_1]
                Y=[y2_0,y2_1]
                if(Weight[i][j]>0):
                    line = matplotlib.lines.Line2D(X, Y, lw=0.35, color='g', alpha=AlphaArr[i][j])
                else :
                    line = matplotlib.lines.Line2D(X, Y, lw=0.35, color='red', alpha=AlphaArr[i][j])
                ax1.add_line(line)
             



  
def DrawConnectionsWLastModif(ax1, x1_0, y1_0, width_0, height_0, Ndim_0,
                              x1_1, y1_1, width_1, height_1, Ndim_1, Weight):
    MaxAlpha=np.amax(Weight)
    MinAlpha=np.amin(Weight)
    iMODE=10
    if (MinAlpha*MaxAlpha < 0):
        iMODE=-10
        
    len_i=len(Weight)
    AlphaArr = ndarray((len_i, ), float)
    for i in range(Ndim_0):
        AlphaArr[i]=0

    if (iMODE >0):
        Diff_W=abs(MaxAlpha) - abs(MinAlpha)
        for i in range(Ndim_0):
            AlphaArr[i]=(abs(Weight[i])-abs(MinAlpha))/abs(Diff_W)

    if (iMODE<0):
        print('Negative Min and Positive Max')
        Diff_P=MaxAlpha
        Diff_M=abs(MinAlpha)
        for i in range(Ndim_0):
            if (Weight[i]>0):
                AlphaArr[i]=(abs(Weight[i]))/abs(Diff_P)
            elif (Weight[i]<0):
                AlphaArr[i]=(abs(Weight[i]))/abs(Diff_M)
            else:
                AlphaArr[i]=0

    for i in range(Ndim_0):
        x2_0 = x1_0+width_0
        y1_0= y1_0 + height_0/Ndim_0
        y2_0 = y1_0 - 0.5*(height_0/Ndim_0)
        y11_1 = y1_1
        x2_1=x1_1
        y11_1= y11_1 + height_1/Ndim_1
        y2_1 = y11_1 - 0.5*(height_1/Ndim_1)
        X=[x2_0,x1_1]
        Y=[y2_0,y2_1]
        if(Weight[i]>0):
            line = matplotlib.lines.Line2D(X, Y, lw=0.25, color='green', alpha=AlphaArr[i])
        else :
            line = matplotlib.lines.Line2D(X, Y, lw=0.25, color='red', alpha=AlphaArr[i])
        ax1.add_line(line)

