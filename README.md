# Visualizing-Neural-Network

To visualise the model weights trained using Tensorflow/Keras from the .h5 file is a big problem in deep neural networks.
Here, we wrote the code which loads the model from the .h5 file and plots the trained model using the weights generated.
![Model Visualisation](https://github.com/jagmeetbains13/Visualizing-Neural-Network/blob/master/Images/Final_Network_256_M1.png)

## Description
The .h5 file contains the weights of the neural network that has been trained. By using the values of the weights, a graph can be drawn which tells about the importance of each link and node in the neural network. This is a very good way to visualise the model without exploring the .h5 file.
### Above Example
- Red color corresponds to the positive value of weights with brightest color having largest value.
- Green color corresponds to the negative value of weights with brightest color having largest negative value.

- The first layer(input layer) has 44 features that has been used to train and test the neural network.
The network has three hidden layers with 64 nodes in each layer with the dense connections.
The network has two output units as the final layer.

### Files
- [Weight_1.py](https://github.com/jagmeetbains13/Visualizing-Neural-Network/blob/master/Weight_1.py) is the file that loads the .h5 file and creates the graph as given above.

- [nnplot.py](https://github.com/jagmeetbains13/Visualizing-Neural-Network/blob/master/nnplot.py) file contains the functions to draw various shapes and lines to generate the final graph. These functions are imported in the [Weight_1.py](https://github.com/jagmeetbains13/Visualizing-Neural-Network/blob/master/Weight_1.py) file. The functions use the weight array, co-ordinates, width, height and color as input arguments. matplotlib functions are used to draw the shapes and lines in the graph.
```
# Functions in the nnplot.py file::

 Myrectangle(ax1,x1,y1,width, height,Linewidth='2',Edgecolor='red',FColor='none',Alpha=1)
 DrawLine(ax1,x1,y1,width,height,Ndim,Color='r')
 DrawBoxesWModif(ax1,x1,y1,width,height,Ndim, Weight)
 WriteVariables(ax1,x1,y1,width,height,Ndim,Labels)
 DrawConnectionsWModif(ax1, x1_0, y1_0, width_0, height_0, Ndim_0,
                          x1_1, y1_1, width_1, height_1, Ndim_1, Weight)
 DrawConnectionsWLastModif(ax1, x1_0, y1_0, width_0, height_0, Ndim_0,
                              x1_1, y1_1, width_1, height_1, Ndim_1, Weight)
                              
```

### Main Code
```
branch_names = ["B_ThrustB", "B_ThrustO",    "B_CosTBTO","B_CosTBz","B_cc1","B_cc2","B_cc3","B_cc4","B_cc5","B_cc6","B_cc7","B_cc8","B_cc9","B_mm2","B_et","B_hso00","B_hso01","B_hso02","B_hso03","B_hso04","B_hso10","B_hso12","B_hso14","B_hso20","B_hso22","B_hso24","B_hoo0","B_hoo1","B_hoo2","B_hoo3","B_hoo4","B_qpElectron","B_qpFSC","B_qpFastHadron","B_qpIntermediateElectron","B_qpIntermediateMuon","B_qpIntermediateKinLepton","B_qpKaon","B_qpKaonPion","B_qpKinLepton","B_qpLambda","B_qpMaximumPstar","B_qpMuon","B_qpSlowPion"]

Outputs = ["Signal", "Background"]

```
branch_names and Outputs are the labels for the input layer and output layer respectively.
