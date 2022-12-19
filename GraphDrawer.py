import matplotlib.pyplot as plt
import numpy as np
def main():
    print("Do you wanna draw how much Graph: 1 or more than 1: ")
    x=int(input("Please enter do you wanna draw how much graph back to back: "))
    if (x==1):
        allProcess()
    elif(x>1):
        for i in range(x):
            allProcess()

def allProcess():
    xname = input("Please enter the name of X axis: ")
    yname = input("Please enter the name of Y axis: ")
    title = input("Please enter the name of your graph: ")
    #color=input("Please write a first letter of color: ")
    list1 = []
    list2 = []
    x = input("Please enter the X value: ")
    while (x != 'end'):
        y = input("Please enter the Y value: ")
        list1.append(x)
        list2.append(y)
        x = input("Please enter the X value: ")
    converter(list1, list2)
    xlist = np.array(list1)
    ylist = np.array(list2)
    drawer(xname, yname, xlist, ylist, title)


def drawer(xname, yname, list1, list2, title):
    plt.plot(list1, list2, "r")
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.show()


def converter(list1, list2):
    for i in range(len(list1)):
        list1[i] = float(list1[i])
    for i in range(len(list2)):
        list2[i] = float(list2[i])
    return list1, list2

main()