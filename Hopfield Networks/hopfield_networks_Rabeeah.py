from math import *
import numpy as np
from matplotlib import pyplot as plt
from submission import *

def seven_segment(pattern):

    def to_bool(a):
        if a==1:
            return True
        return False

    def hor(d):
        if d:
            print(" _ ")
        else:
            print("   ")

    def vert(d1, d2, d3):
        word = ""

        if d1:
            word = "|"
        else:
            word = " "

        if d3:
            word += "_"
        else:
            word += " "

        if d2:
            word += "|"
        else:
            word += " "

        print(word)

    pattern_b = list(map(to_bool,pattern))

    hor(pattern_b[0])
    vert(pattern_b[1], pattern_b[2], pattern_b[3])
    vert(pattern_b[4], pattern_b[5], pattern_b[6])

    number = 0

    for i in range(0,4):
        if pattern_b[7+i]:
            number += pow(2,i)
    print(int(number))

submission=Submission("Rabeeah Masood")
submission.header("Rabeeah Masood")


six = [1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1]
three = [1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1]
one = [-1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1]  #these are lists, NOT ARRAYS

seven_segment(three)
seven_segment(six)
seven_segment(one)


def weightMatrix(a, b, c):
    shape = (11, 11)
    W = np.zeros(shape)
    for i in range(11):
        for j in range(11):
            if i != j:
                W[i, j] = 1/3 * (a[i]*a[j] + b[i]*b[j] + c[i]*c[j])
    return W

weight_matrix = weightMatrix(one, three, six)

submission.section("Weight matrix")
submission.matrix_print("W",weight_matrix)

#defining a step function for the individual neurons
def stepFunction(value):
    if value < 0:
        return -1
    elif value >= 0:
        return 1

threshold = 0

#given a state, update the state using the weight matrix
def stateUpdate(vector, weights):
    newVector = [0,0,0,0,0,0,0,0,0,0,0]
    for i in range(11):
        summation = 0
        for j in range(11):
            if i!=j:
                summation += (vector[j] * weights[i,j]) - threshold
        newVector[i] = stepFunction(summation)
    return newVector

#defining an energy function that decreases as the state converges
def energy(vector, weights):
    sum = 0
    for i in range(11):
        for j in range(11):
            sum += vector[i] * weights[i,j] * vector[j]
    energy = -1/2 * sum
    energy = round(energy,1)
    return energy

def hopRunfield(vector, weights):
    attractorStates = []
    unstableList = []
    energyList = []
    stateList = []
    stateList.append(vector)
    submission.seven_segment(vector)
    submission.print_number(energy(vector, weights))
    energyList.append(energy(vector, weights))
    newVector = stateUpdate(vector, weights)
    toContinue = True

    while (toContinue):
        if newVector not in stateList:
            submission.seven_segment(newVector)
            submission.print_number(energy(newVector, weights))
            vector = newVector
            newVector = stateUpdate(vector, weights)
            energyList.append(energy(vector, weights))
            stateList.append(vector)
            if vector not in attractorStates:
                attractorStates.append(vector)

        elif (newVector in stateList and stateList[len(stateList) - 2] == newVector):
            unstableList.append(stateList[len(stateList) - 2])
            unstableList.append(stateList[len(stateList) - 1])
            print("unstable attractor states found after {0} iterations.".format(len(stateList)-1))
            print("List of States: {0}".format(stateList))
            print("Attractor States: {0} , {1} ".format(stateList[len(stateList) - 2], stateList[len(stateList) - 1]))
            print("List of energies at each iteration: {0}".format(energyList))
            seven_segment(stateList[len(stateList) - 2])
            seven_segment(stateList[len(stateList) - 1])
            plt.xlabel("Iterations")
            plt.ylabel("Energy")
            plt.plot(energyList)
            plt.show()
            return ((stateList[len(stateList) - 2]), (stateList[len(stateList) - 1]))

        elif (newVector in stateList and stateList[len(stateList) - 1] == newVector):
            print("Attractor found after {0} iterations.".format(len(stateList)-1))
            print("List of States: {0}".format(stateList))
            print("Attractor State: {0}".format(vector))
            print("List of energies at each iteration: {0}".format(energyList))
            seven_segment(vector)
            plt.xlabel("Iterations")
            plt.ylabel("Energy")
            plt.plot(energyList)
            plt.show()
            return newVector

print("test1")
submission.section("Test 1")

test1=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]
seven_segment(test1)

submission.qquad()

##this prints a space
submission.qquad()

hopRunfield(test1, weight_matrix)

print("test2")
submission.section("Test 2")

test2 =[1,1,1,1,1,1,1,-1,-1,-1,-1]

energy2 = energy(test2, weight_matrix)

submission.qquad()

##this prints a space
submission.qquad()

hopRunfield(test2, weight_matrix)

submission.bottomer()
