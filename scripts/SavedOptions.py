from tkinter import ttk
import tkinter as tk

def saveData(DataList, Filename):
    with open(Filename, 'w') as file:
        for saveData in DataList:
            try:
                file.write(f"{saveData.get()}" + '\n')
            except:
                file.write(f"{saveData}" + '\n')


def loadData(DataList, Filename):
    try:
        with open(Filename, 'a+') as file:
            file.seek(0)
            savedLines = file.readlines()
            for i in range(len(savedLines)):
                DataList[i].set(savedLines[i].strip())
    except:
        print("Error Loading Settings Saved Values (Likely an option was added or removed)")