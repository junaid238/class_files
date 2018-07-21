# # import all the required libraries
# import pandas as pd
# import numpy as np
# import math
# import operator

# # load data from the csv file 
# data = pd.read_csv("iris.csv")
# # data --> data frame --> pandas df
# # print(type(data))

# # head() gives first five rows of the dataframe 
# print(data.head())

# # make a euclidean distance calculator function
# # calculate distance bw two data points
# def euclideanDistance(data1, data2, length):
#     distance = 0
#     for x in range(length):
#         distance += np.square(data1[x] - data2[x])
#     return np.sqrt(distance)

# def knn(trainingSet, testInstance, k):
#     distances = {}
#     sort = {}
#     length = testInstance.shape[1]
#     # print(testInstance.shape , " from shape ")
#     # print(length , " from length")
#     # print(len(trainingSet) , " trainingSet")
#     # print("start " , trainingSet.iloc[0] , " iloc 0")
#     # print("start " , trainingSet.iloc[1] , " iloc 1")
#     # dist = euclideanDistance(testInstance, trainingSet.iloc[0], length)
#     # dist1 = euclideanDistance(testInstance, trainingSet.iloc[1], length)
#     # print("start " , dist , " dist")
#     # print("start " , dist1 , " dist")
#     for x in range(len(trainingSet)):
#       dist = euclideanDistance(testInstance, trainingSet.iloc[x], length)
#       distances[x] = dist[0]
#     sorted_d = sorted(distances.items(), key=operator.itemgetter(1)) 
#     neighbors = []
#     for x in range(k):
#         neighbors.append(sorted_d[x][0])
#     classVotes = {}
#     for x in range(len(neighbors)):
#         response = trainingSet.iloc[neighbors[x]][-1]
#         if response in classVotes:
#             classVotes[response] += 1
#         else:
#             classVotes[response] = 1
#     sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
#     # print(distances)
#     # print(sorted_d)
#     # print(classVotes)
#     # print(sortedVotes)
#     return(sortedVotes[0][0], neighbors)

# testSet = [[7.2, 3.6, 5.1, 2.5]]
# test = pd.DataFrame(testSet)

# k = 1
# result,neigh = knn(data, test, k)
# # print(result)
# # print(neigh)

# https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
# Example of kNN implemented from Scratch in Python

import csv
import random
import math
import operator

#splitting of data into 67/33 or 70/30 format split = 0.70
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    # get the file data from csvfile
    with open(filename, 'rb') as csvfile:
        # capture data into a data object 
        lines = csv.reader(csvfile)
        # type cast each of the line to a list 
        dataset = list(lines)
        # itereate over them to generate random trainingSet and testSet using random.random()
        # len(dataset)-1 as first row will be headers item
        for x in range(len(dataset)-1):
            # for y in range(4):
            #     # ???
            #     dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                # random trainingSet is generated 
                trainingSet.append(dataset[x])
            else:
                # random testSet is generated
                testSet.append(dataset[x])

# calculating distane b/w two datapoints based on length
def euclideanDistance(instance1, instance2, length):
    # declaratoin of distance as 0
    distance = 0
    # if instance1 contains 2-d length = 2
    for x in range(length):
        # [a,b,c] [x,y,z]
        distance += pow((instance1[x] - instance2[x]), 2)
    # sqrt (distance b/w points)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        # calling euclideanDistance to get dist 
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        # distances b/w training points and testpoints in list
        # distances --> [[a,b,c], dist]
        distances.append((trainingSet[x], dist))
    # sort distances list as per shortest distance
    distances.sort(key=operator.itemgetter(1))
    # neighbors for getting k values based on k assumed
    neighbors = []
    # iterating in distances to get k neighbors 
    for x in range(k):
        # make neighbors list with least "k" distance values 
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0
    
def main():
    # prepare data
    trainingSet=[]
    testSet=[]
    split = 0.67
    loadDataset('iris.data', split, trainingSet, testSet)
    print 'Train set: ' + repr(len(trainingSet))
    print 'Test set: ' + repr(len(testSet))
    # generate predictions
    predictions=[]
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
    
main()