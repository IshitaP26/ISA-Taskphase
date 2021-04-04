# Convolutional Neural Network

**Definition**

A deep learning algorithm that can take an input and evaluate the importance that must be assigned to the various aspects of the image and then differentiate one another, is the convolutional neural network. In order to capture the spatial and temporal dependencies in an image, various filters are applied, which results in a certain activation. Upon applying these filters repeatedly, a map of activations is created which is called a feature map. This then includes the locations and strength of a certain feature in the image and detects it, allowing it further classify the image. These are mainly used for image recognition systems and classification problems.

**Workings**

This neural network is made of neurons which have the capability of learning weights and biases through the training sets. This is done when each neuron takes a weighted sum of the inputs and passes it through an activation function which produces a certain output. There are four major parts to the entire process:
                                            
                                            1. Convolution layer
                                            2. ReLU actication layer
                                            3. Pooling layer
                                            4. Fully connected layer

**Convolution Layer**
The convolution of the image is the first action that takes place. Here the different features each have their respective convolution filters and the entire convolutional neural network algorithm learns which features combine to create a certain output like a number or a letter. The layer that is used to perform this function is called the kernel, which in itself is a matrix that traverses the entire pixel matrix image, performing a dot product matrix multiplication with each of the parts of the image that it hovers over. The dot products are then summed to result in a single final value representing that portion of the pixel matrix. After the kernel performs the same function all over the pixel matrix, the output is a 2D array containing a filtered representation of the input and is called a feature map. 

An important aspect to note is that the kernel matrix is always smaller than the input matrix which is why it must be applied systematically throughout the matrix. This gives it a higher opportunity of detecting the feature that it is looking for within the image. This ability of giving importance to the fact of whether the feature is present rather than where it is present is called translation invariance and is one of the most unique factors of CNN.


**ReLU Activation Layer**
Once the feature map has been created, each of the values of the feature map is processed by the activation function, which in this case is the rectified linear unit(ReLU) transform function. This works in a way such that if the input is above a certain threshold quantity, the node is activated, otherwise it is not. So all the values of the featured matrix that are negative, have the output of zero while all the values that are greater than or equal to zero remain the same. This serves the purpose of removing all the negative values from the feature map. 


**Pooling Layer**
After this comes the pooling layer in which the image is shrunk into a smaller size. To do this, a certain matrix size is chosen and from each of the windows created by the matrix, the maximum value is taken to be inserted into the smaller structure. The purpose of this action is to lower the amount of computational power needed to process a certain set of data.

**Fully Connected Layer**
Once the pooling is done, the 2D data is flattened into a single linear vector and then entered as input for the fully connected layer so as to finally classify the immage based on the values in the single lined vector.

**Resources used**
1. https://machinelearningmastery.com/convolutional-layers-for-deep-learning-neural-networks/
2. https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53
3. https://www.edureka.co/blog/convolutional-neural-network/








