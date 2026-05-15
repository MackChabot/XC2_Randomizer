import json
from scripts import Helper, JSONParser
import random, copy
from XC2.XC2_Scripts import IDs, Options

def CustomCoreCrystalRando():
    if HasRanOnce():
        return
    RandomizeCrystalList()
    ApplyNewBladeNames()
    FixOpeningSoftlock()
    FixRoc()
    FixArtReleaseLevels()
    RareBladeProbabilityEqualizer()
    LandofChallengeRelease()
    NewGamePlusBladeBalancing()

def RareBladeProbabilityEqualizer(): # makes it so all blades are equally likely to be pulled
    Helper.ColumnAdjust("XC2/JsonOutputs/common/BLD_RareList.json", ["Condition", "Assure1", "Assure2", "Assure3", "Assure4", "Assure5"] , 0)
    Helper.ColumnAdjust("XC2/JsonOutputs/common/BLD_RareList.json", ["Prob1", "Prob2", "Prob3", "Prob4", "Prob5"] , 1)

def LandofChallengeRelease(): #frees shulk, elma, fiora from land of challenge restriction
    Helper.SubColumnAdjust("XC2/JsonOutputs/common/CHR_Bl.json", "Flag", "OnlyChBtl", 0)

def FixArtReleaseLevels(): # Fixes issue with NG+ blades having incredibly high level requirements for arts
    with open("XC2/JsonOutputs/common/BTL_Arts_Dr.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        for art in artData["rows"]:
            if art["ReleaseLv1"] > 10:
                for i in range(1, 6):
                    art[f"ReleaseLv{i}"] = random.choice([3,5,7,9])
        JSONParser.CloseFile(artData, artFile)

def FixRoc(): # Fixes Roc softlock as you need to pull him legit for a quest
    rocCrystalId = None
    with open("XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as cryFile:
        cryData = json.load(cryFile)
        for cry in cryData["rows"]:
            if cry["BladeID"] == 1008:
                cry["Condition"] = 2212
                rocCrystalId = cry["$id"]
                break
        JSONParser.CloseFile(cryData, cryFile)
    with open("XC2/JsonOutputs/common/MNU_BladeCreate.json", 'r+', encoding='utf-8') as blFile:
        blData = json.load(blFile)
        for bl in blData["rows"]:
            if bl["$id"] == 2:
                bl["limited_item"] = rocCrystalId
        JSONParser.CloseFile(blData, blFile)

def FixOpeningSoftlock(): # Game doesnt like it if we open cores before a certain point in the game iirc
    StartingCondListRow = Helper.GetMaxValue("XC2/JsonOutputs/common/FLD_ConditionList.json", "$id") + 1
    StartingCondScenarioRow = Helper.GetMaxValue("XC2/JsonOutputs/common/FLD_ConditionScenario.json", "$id") + 1
    with open("XC2/JsonOutputs/common/FLD_ConditionList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data["rows"].append({"$id": StartingCondListRow, "Premise": 0, "ConditionType1": 1, "Condition1": StartingCondScenarioRow, "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0, "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        JSONParser.CloseFile(data, file)
    with open("XC2/JsonOutputs/common/FLD_ConditionScenario.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data["rows"].append({"$id": StartingCondScenarioRow, "ScenarioMin": 2001, "ScenarioMax": 10048, "NotScenarioMin": 0, "NotScenarioMax": 0})
        JSONParser.CloseFile(data, file)
    with open("XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["BladeID"] != 1008:
                row["Condition"] = StartingCondListRow
        JSONParser.CloseFile(data, file)    

def HasRanOnce():
    '''Checks if the crystals have been randomized already'''
    with open("XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as cryFile:
        cryData = json.load(cryFile)
        for cry in cryData["rows"]:
            if cry["$id"] == 45002 and cry["Price"] != 0:
                return True
        return False
    
def RandomizeCrystalList():
    CrystalCount = 0
    
    BladeIDsGroup = Helper.RandomGroup()
    for id in IDs.CoreCrystalBladeIDs:
        BladeIDsGroup.AddNewData(id)

    with open("XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as cryFile:
        cryData = json.load(cryFile)
        for cry in cryData["rows"]:
            
            if cry["$id"] not in IDs.CustomCrystalIDs:
                continue
            
            chosenBladeID = BladeIDsGroup.SelectRandomMember()
            CrystalCount += 1
            cry["BladeID"] = chosenBladeID
            cry["Price"] = 5000
            cry["Condition"] = 0
            cry["ValueMax"] = 1
            cry["NoMultiple"] = CrystalCount*11 # 11 was here because it worked weirdly the nomultiple value it needed a difference of 10 or something to work
            
        JSONParser.CloseFile(cryData, cryFile)
    
def ApplyNewBladeNames(): # Dont love this because it loops back over everything and applies new things. Would be better to do it all the same time 
    CorrespondingBladeIDs = Helper.AdjustedFindBadValuesList("XC2/JsonOutputs/common/ITM_CrystalList.json",["$id"], IDs.CustomCrystalIDs, "BladeID")
    CorrespondingBladeNameIDs = Helper.AdjustedFindBadValuesList("XC2/JsonOutputs/common/CHR_Bl.json", ["$id"], CorrespondingBladeIDs, "Name")
    CorrespondingBladeNames = Helper.AdjustedFindBadValuesList("XC2/JsonOutputs/common_ms/chr_bl_ms.json", ["$id"], CorrespondingBladeNameIDs, "name")

    with open("XC2/JsonOutputs/common_ms/itm_crystal.json", "r+", encoding='utf-8') as file:     
        IDNumbers = Helper.InclRange(16, 58)
        data = json.load(file)
        for i in range(0, len(IDNumbers)):
            data["rows"].append({"$id": IDNumbers[i], "style": 36, "name": f"{CorrespondingBladeNames[i]}\'s Core Crystal"})
        JSONParser.CloseFile(data, file)
    with open("XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            for i in range(0, len(CorrespondingBladeIDs)):
                if row["BladeID"] == CorrespondingBladeIDs[i]:
                    row["Name"] = IDNumbers[i]
                    break
        JSONParser.CloseFile(data, file)

def NewGamePlusBladeBalancing():
    ''' Make NG+ blades balanced by starting them at lower power and allowing chips to be put in their weapons'''
    
    # Edit their default weapons to be on par with lead chips (baby starting chips) and add new ones
    with open("XC2/JsonOutputs/common/ITM_PcWpn.json", "r+", encoding='utf-8') as wpnFile:     
        with open("XC2/JsonOutputs/common/ITM_PcWpnChip.json", "r+", encoding='utf-8') as chipFile:
            wpnData = json.load(wpnFile)
            chipData = json.load(chipFile)
            
            # Fix default weapons
            for wpn in wpnData["rows"]:
                if wpn["$id"] in [5971, 5972, 5973, 5974, 5975, 5976, 5977]:
                    wpn["Rank"] = 1
                    wpn["Damage"] = random.randrange(10,20)
                    wpn["CriRate"] = random.choice([5,10,15,20]) 
                    wpn["Flag"]["Private"] = 0

            wpnsById = {item['$id']: item for item in wpnData["rows"]}

            newWpnId = wpnData['rows'][-1]['$id'] + 1

            # TODO: Each chip needs the weapons set for CreateWpnN for N=[20-26]
            for chip in chipData["rows"]:
                for wpnType in range(20,27): # CreateWeapons 20-26 which correspond to those NG+ blade weapons
                    # Determine the base weapon
                    wpnType2BaseWpnType = {
                        20 : 2, # Calamity Scythe (Akhos) => Catalyst Scimitar
                        21 : 11, # Cobra Bardiche (Patroka) => Megalance
                        22 : 7, # Infinity Fans (Mikhail) => Whipswords
                        23 : 3, # Brilliant Twinblades (Obrona) => Twin Rings
                        24 : 12, # Decimation Cannon (Perdido) => Ether Cannon
                        25 : 13, # Rockrending Gauntlets (Cressidus) => Shield Hammer
                        26 : 14  # Sword Tonfa (Sever) => Chroma Katana
                    }

                    # ModelBaseWeapon - The original NG+ weapon (for things like resources, etc.)
                    modelBaseWpn = copy.deepcopy(wpnsById[5971 - 20 + wpnType])

                    # StatsBaseWeapon - A weapon for this chip from a similar weapon type, listed above (for stats)
                    statsBaseWpnType = wpnType2BaseWpnType[wpnType]
                    statsBaseWpn = copy.deepcopy(wpnsById[chip[f"CreateWpn{statsBaseWpnType}"]])

                    # Create the new weapon
                    newWeapon = copy.deepcopy(modelBaseWpn)
                    statsToCopy = ['Rank', 'Damage', 'Stability', 'CriRate', 'GuardRate', 'Enhance1', 'PArmor', 'EArmor', 'Enhance2']
                    for stat in statsToCopy:
                        newWeapon[stat] = statsBaseWpn[stat]
                    newWeapon['$id'] = newWpnId

                    # Add the new weapon to the table
                    wpnData['rows'].append(newWeapon)

                    # Set this new weapon on the weapon chip
                    chip[f"CreateWpn{wpnType}"] = newWpnId

                    # Increment the weapon ID for the next weapon
                    newWpnId = newWpnId + 1
                    
            JSONParser.CloseFile(chipData, chipFile)     
            JSONParser.CloseFile(wpnData, wpnFile)
        
    # Allow chip building on these blades
    with open("XC2/JsonOutputs/common/CHR_Bl.json", "r+", encoding='utf-8') as blFile:
        blData = json.load(blFile)
        for bl in blData["rows"]:
            # TODO: This happens post blade randomization, so these IDs are not correct
            #if bl["$id"] in [1043, 1044, 1045, 1046, 1047, 1048, 1049]:
            if True:
                #bl["Flag"]["OnlyWpn"] = 0
                bl["Flag"]["NoBuildWpn"] = 0     
        JSONParser.CloseFile(blData, blFile)


    # TODO: Testing. To make sure NG+ blades work, make sure they're the only blades I get on my practice file
    with open("XC2/JsonOutputs/common/BLD_RareList.json", "r+", encoding='utf-8') as gachaFile:
        gachaData = json.load(gachaFile)
        mikhailCore = copy.deepcopy(gachaData["rows"][0])
        mikhailCore['$id'] = gachaData["rows"][-1]['$id'] + 1
        mikhailCore['Blade'] = 1045
        gachaData['rows'].append(mikhailCore)
        poppibusterCore = copy.deepcopy(gachaData["rows"][0])
        poppibusterCore['$id'] = gachaData["rows"][-1]['$id'] + 1
        poppibusterCore['Blade'] = 1105
        gachaData['rows'].append(poppibusterCore)
        for gacha in gachaData["rows"]:
            gacha['Condition'] = 0
            for i in range(1,6):
                # Guarantee at least one NG+ blade and one non NG+ blade
                if gacha['Blade'] in [1045, 1105]:
                    gacha[f"Prob{i}"] = 10
                    gacha[f"Assure{i}"] = 1
                else:
                    gacha[f"Prob{i}"] = 0
                    gacha[f"Assure{i}"] = 0

        JSONParser.CloseFile(gachaData, gachaFile)



        
    