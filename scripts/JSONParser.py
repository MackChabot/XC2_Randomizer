import json, random, os, IDs


def ChangeJSONFile(Filename, keyWords, rangeofValuesToReplace = [], rangeValidReplacements = [], InvalidTargetIDs = [], SliderOdds = 100, IgnoreID_AND_Key = [["",""]]): # make this a function to reuse, check the settings ot see if we even do this

    # print(f"Valid Replacements: {Replacements}")
    SliderOdds = IDs.CurrentSliderOdds
    rangeValidReplacements.extend(IDs.ValidReplacements)
    rangeValidReplacements = [x for x in rangeValidReplacements if x not in IDs.InvalidReplacements]
    for name in Filename:
        filePath = "./_internal/JsonOutputs/" + name
        if not os.path.exists(filePath):
          #print(filePath + " filepath does not exist.")
          continue
        with open(filePath, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for item in data['rows']:
                if not item["$id"] in InvalidTargetIDs:
                    for key in item:  
                        if ([item["$id"], key] not in IgnoreID_AND_Key):       
                            if key in keyWords:
                                if (((rangeofValuesToReplace == []) or (item[key] in rangeofValuesToReplace)) and (SliderOdds > random.randint(0,100))):
                                    item[key] = random.choice(rangeValidReplacements)
                            elif key == "Flag":
                                for flag, flagVal in item[key].items():
                                    if flag in keyWords:
                                        if ((flagVal in rangeofValuesToReplace) and (SliderOdds > random.randint(0,100))):
                                            item[key][flag] = random.choice(rangeValidReplacements)                                
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    IDs.ValidReplacements.clear()
    IDs.InvalidReplacements.clear()
    IDs.CurrentSliderOdds = 100


def ChangeJSONLine(filenames, ids, keys, replacement):
    for name in filenames:
        filePath = "./_internal/JsonOutputs/" + name
        if not os.path.exists(filePath):
          #print(filePath + " filepath does not exist.")
          continue
        with open(filePath, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for item in data['rows']:
                if item["$id"] in ids:
                   for key in keys:
                    item[key] = replacement

            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
            
def ExtendJSONFile(filePath, additionsList = []):
    with open("./_internal/JsonOutputs/" + filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for item in additionsList:
            data["rows"].extend(item)
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)