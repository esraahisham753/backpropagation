import numpy as np
import math
from tkinter import  messagebox

def sigmoid(v, a):
    f = float(1)/float(1+math.exp(-a * v))
    return  f


def hyperbolic(v, a):
    f = float(1 - math.exp(- a * v)) / float(1 + math.exp(- a * v))
    return f


def prepare_data():
    samples = [] #list of samples, each element is a list of four features corresponding to one sample
    labels = []
    dataset = open("IrisData.txt",'r')
    dataset.readline()#throw the first line of the file
    #collect samples
    for i in range(0, 150):
        sample_features = []  # list of features of one sample to append as an element of samples list
        line = dataset.readline()
        sample_features = line.split(',')   #get list of features from the line
        sample_features = sample_features[0:4]   #remove the last element of split(label)
        samples.append(sample_features)  #append the list of features as single element of samples list
    #prepare labels
    #class1 labels
    for j in range (0, 50):
        labels.append(1)
    #class2 labels
    for k in range(0, 50):
        labels.append(2)
    #class3 labels
    for c in range(0, 50):
        labels.append(3)
    return samples, labels


def train(m, eta, num_hidden_layers, hidden_neuorons_per_layer, bias, activation):
    samples, labels = prepare_data() #return all samples and labels for 150 sample
    #get class 1 training samples and labels
    samples1 = samples[0:30]
    labels1 = labels[0:30]
    #get class 2 training samples and labels
    samples2 = samples[50:80]
    labels2 = labels[50:80]
    #get class 3 training samples and labels
    samples3 = samples[100:130]
    labels3 = labels[100:130]
    #concatenate training samples and labels
    train_samples = samples1 + samples2 + samples3
    trian_labels = labels1 + labels2 + labels3
    #loop through num epochs
    for i in range(0, m):
        #loop through training samples
        for j in range(0, 90):
            input = []
            # add bias to input vector
            if(bias == 1):
                input.append(bias)
            # Add sample features to input vector
            for f in range(0, 4):
                input.append(float(train_samples[j][f]))
            num_features = 4
            # loop through hidden layers
            for k in range(0, num_hidden_layers):
                #loop through each neuoron
                #initialize list to carry the outputs of all neuorons in the hidden layer
                hidden_layer_output = []
                for l in range(0, hidden_neuorons_per_layer[k]):
                    #generate random weights if bias and if not bias
                    random_weights = 0
                    if(bias == 1):
                        random_weights = np.random.uniform(low = 0, high = 1, size=(num_features + 1, 1))
                    else:
                        random_weights = np.random.uniform(low = 0, high = 1, size = (num_features, 1))
                    #compute weighted sum
                    v = np.dot(input, random_weights)
                    yk = 0
                    #apply activation function
                    if(activation == "sigmoid"):
                        yk = sigmoid(v, 1)
                    elif(activation == "hyperbolic"):
                        yk = hyperbolic(v, 1)
                    #add this output to list of this hidden layer output to use as next layer input
                    hidden_layer_output.append(yk)
                #prepare next layer input from current output
                input = []
                if(bias == 1):
                    input.append(1)
                for c in range(0, hidden_neuorons_per_layer[k]):
                    input.append(hidden_layer_output[c])
                num_features = hidden_neuorons_per_layer[k]
            #calculate output for the 3 neuorons
            final_output = []
            for w in range(0, 3):
                random_weights = 0
                if(bias == 1):
                    random_weights = np.random.uniform(low = 0, high = 1, size=(num_features + 1, 1))
                else:
                    random_weights = np.random.uniform(low = 0, high = 1, size=(num_features, 1))
                v = np.dot(input, random_weights)
                yk = 0
                if(activation == "sigmoid"):
                    yk = sigmoid(v, 1)
                elif(activation == "hyperbolic"):
                    yk = sigmoid(v, 1)
                final_output.append(yk)
    messagebox.showinfo("success", "feedforward done successfully")



