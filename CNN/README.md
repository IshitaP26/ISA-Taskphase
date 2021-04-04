# Convolutional Neural Network

**Definition**

A deep learning algorithm that can take an input and evaluate the importance that must be assigned to the various aspects of the image and then differentiate one another. In order to capture the spatial and temporal dependencies in an image, various filters are applied, which results in a certain activation. Upon applying these filters repeatedly, a map of activations is created which is called a feature map. This then includes the locations and strength of a certain feature in the image and detect it. These are mainly used for image recognition systems and classification problems.

This neural network is made of neurons which have the capability of learning weights and biases through the training sets. This is done when each neuron takes a weighted sum of the inputs and passes it through an activation function which produces a certain output. 

The convolution of the image is the first action to take place. Here the different features each have their respective convolution filters and the entire convolutional neural network algorithm learns which features combine to create a certain output like a number or a letter. The activation function used is the rectified linear unit transform function. This works such that if the input is above a certain threshold quantity, the node is activated. After this comes the pooling layer in which the image is shrunk into a smaller size. To do this a window size is chosen and from each of the windows the maximum value is taken to be inserted into the smaller structure. The layers are then all stacked up





