#!/usr/bin/python3

import os
import importlib
import re

def showGates():
    print("\nHere's a list of all the gates available:")
    files = os.listdir("gates")
    gates = []
    for i in range(0, len(files)):
        if  re.search("^_", files[i]) is None:
            gates.append(files[i].split(".", maxsplit=2)[0])
    for i in range(0, len(gates)):
        print(gates[i])

def newGate():
    gateName = input("\nEnter your name for this gate: ")
    if gateName == "AndGate" or gateName == "NotGate":
        print("Cannot Overwrite And or Not gates")
        return
    functionFile = open(os.path.join("gates", gateName + ".py"), "w")
    inputs = input("Name your inputs: ").split(" ")
    functionFile.write("# ")
    for i in range(0, len(inputs)-1):
        functionFile.write(inputs[i]+" ")
    functionFile.write(inputs[len(inputs)-1]+"\n")
    functionFile.write("def function (inputs):\n")
    for i in range(0, len(inputs)):
        functionFile.write("    "+inputs[i]+" = "+"inputs["+str(i)+"]\n")
    showGates()
    print("\nType 'help'for help:\n")
    outputList=[]
    while True:
        command = input().split(" ")
        if command[0]=="help":
            print("\nThe syntax goes like this: NameOfGate  nameOfOutputOfGate  inputs...")
            print("The two special commands are output and end")
            print("output connects the output of a gate to the output of the gate your making.")
            print("end exits the program and finish the gate's file.\n")
        elif command[0]=="end":
            functionFile.write("    return ")
            for i in range(0, len(outputList)):
                if i > 0:
                    functionFile.write(", ")
                functionFile.write(outputList[i])
            return
        elif command[0]=="output":
            outputList.append(command[1])
        else:
            functionFile.write("    import gates."+ command[0]+ "\n")
            functionFile.write("    "+command[1]+" = gates."+command[0]+".function([")
            for i in range(2, len(command)-1):
                functionFile.write(command[i]+", ")
            functionFile.write(command[len(command)-1]+"])\n")

def executeGate():
    showGates()
    gateName = input("\nEnter the name of the gate to execute: ")
    gate = importlib.import_module("gates."+gateName)
    functionFile = open(os.path.join("gates", gateName + ".py"), "r")
    inputsFromFile = functionFile.readline().split(" ")
    inputs = []
    values = []
    loopOn = input("Enter 'L' to loop indefinitely (^c to break) or anthing else to run once: ")
    if loopOn == "L":
        while True:
            for i in range(1, len(inputsFromFile)):
                inputs.append(inputsFromFile[i].replace("\n", ""))
                values.append(inputs[i-1])
                values[i-1]=int(input("Enter the value for "+str(inputs[i-1])+": "))
                if values[i -1]>1 or values[i -1]<0:
                    print("Error, inputs can only ever be 1 or 0.")
                    i=0
            for i in gate.function(values):
                print(i, end="")
            print()
    else:
        for i in range(1, len(inputsFromFile)):
            inputs.append(inputsFromFile[i].replace("\n", ""))
            inputs[i-1]=int(input("Enter the value for "+str(inputs[i-1])+": "))
            if inputs[i -1]>1 or inputs[i -1]<0:
                print("Error, inputs can only ever be 1 or 0.")
                i=0
        for i in gate.function(inputs):
            print(i, end="")
        print()

if __name__ == "__main__":
    selection= input("Welcome: type 'n' for a new gate, 'e'to execute a gate: ")
    if selection == "n":
        newGate()
    elif selection == "e":
        executeGate()
