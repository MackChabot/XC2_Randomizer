import json
from tkinter import filedialog
import tkinter as tk

def InclRange(start, end):
     return list(range(start, end+1))

def StartsWith(startingWord, lowNum, highNum):
    listofWords = []
    for i in range(lowNum, highNum + 1):
        listofWords.append(startingWord + str(i))
    return listofWords

def InsertHelper(insertIndex,  lowNum, highNum, mainString = str, pathTo = str):
    listOfFiles = []
    for i in range(lowNum, highNum):
        listOfFiles.append(pathTo + mainString[:insertIndex] + f"{i:02}" + mainString[insertIndex:]) # fstring allows us to format with 2 digits like xc2 wants
    #print(listOfFiles)
    return listOfFiles

def FindValues(filePath, keyWordList, keywordBadValueList, returnedKeyWordValue): # used to find a list of values from a file with certain characteristsics that i want to remove
    bad_values_found = []
    with open(filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data['rows']:
            for key, value in row.items():
                if key in keyWordList and value in keywordBadValueList:
                    bad_values_found.append(row[returnedKeyWordValue]) 
    
    # print("FindValues: " + bad_values_found)
    return(bad_values_found)

def AdjustedFindBadValuesList(filePath, keyWordList, keywordBadValueList, returnedKeyWordValue): # if one keywordBadValueList has 2 matches, it won't return the second one. 
    bad_values_found = []
    with open(filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for j in range(0, len(keyWordList)):
            for i in range(0, len(keywordBadValueList)):
                for row in data['rows']:
                    if row[keyWordList[j]] == keywordBadValueList[i]:
                        bad_values_found.append(row[returnedKeyWordValue])
                        break
    #print(bad_values_found)
    return(bad_values_found)

def FindSubOptionValuesList(filePath, dictName, subDictName, subDictValue, returndictValue):
    bad_values = []
    with open(filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row[dictName][subDictName] == subDictValue:
                bad_values.append(row[returndictValue])
    print(bad_values)
    return(bad_values)


def DirectoryChoice(FileDescription, EntryField):
    Directory = filedialog.askdirectory(title=FileDescription)
    if (Directory != ""):
        EntryField.delete(0, tk.END)
        EntryField.insert(0, Directory)

def OptionCarveouts(ValidValuesList, ToggleableIndexValues, stateOfButton = None):
    # print("Updated Valid Values: " + str(stateOfButton))
    if stateOfButton.get() == True:
        ValidValuesList += ToggleableIndexValues
    else:
        ValidValuesList[:] = [x for x in ValidValuesList if x not in ToggleableIndexValues]
    # print(ValidValuesList, end='\n\n')


def SubColumnAdjust(filename, colName, adjustedSubColName, desiredValue): #when your column you want to adjust is nested inside a dict
    with open(filename, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            row[colName][adjustedSubColName] = desiredValue
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ColumnAdjust(filename, clearedCols, desiredValue):
    with open(filename, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for k in range(0, len(clearedCols)):
            for row in data["rows"]:
                for key, value in row.items():
                    if key != clearedCols[k]:
                        continue
                    row[clearedCols[k]] = desiredValue
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)