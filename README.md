# Visualizing-Neural-Network

To visualise the model weights trained using Tensorflow/Keras from the .h5 file is a big problem in deep neural networks.
Here, we wrote the code which loads the model from the .h5 file and plots the trained model using the weights generated.
![Model Visualisation](https://github.com/jagmeetbains13/Visualizing-Neural-Network/blob/master/Images/Final_Network_256_M1.png)

## Description
The .h5 file contains the weights of the neural network that has been trained.
### Above Example
Red color corresponds to the positive value of weights with brightest color having largest value.
Green color corresponds to the negative value of weights with brightest color having largest negative value.

The first layer(input layer) has 44 features that has been used to train and test the neural network.
The network has three hidden layers with 64 nodes in each layer with the dense connections.
The network has two output units as the final layer.

### Coding Files
Weight_1.py is the file that loads the .h5 file and creates the graph as given above.

nnplot.py file contains the functions to draw various shapes and lines to generate the final graph. The functions use the weight array and drawing co-ordinates as input arguments.
'''
 Myrectangle(ax1,x1,y1,width, height,Linewidth='2',Edgecolor='red',FColor='none',Alpha=1)
'''
