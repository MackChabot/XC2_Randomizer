import Enhancements, IDs, JSONParser


IDStart = 0
CustomAccessoriesDictList = []
NameDictList = []

class CustomAcc:
    id = 0
    Name = 0
    DebugName = ""
    ArmorType = 0
    Enhance1 = 0
    AddAtr = 0
    Price = 0
    Rarity = 0
    Flag = {
        "NoSell": 0,
        "EqPC01": 1,
        "EqPC02": 1,
        "EqPC03": 1,
        "EqPC04": 1,
        "EqPC05": 1,
        "EqPC06": 1,
        "EqPC07": 1,
        "EqPC08": 1,
        "EqPC09": 1,
        "EqPC10": 1,
        "EqPC11": 1,
        "EqPC12": 1
    }
    PArmor = 0
    EArmor = 0
    Bns_HpMax = 0
    Bns_Strength = 0
    Bns_PowEther = 0
    Bns_Dex = 0
    Bns_Agility = 0
    Bns_Luck = 0
    Enhance2 = 0
    Icon = 0
    Zone = 0
    Zone2 = 0
    IraZone = 0
    IraZone2 = 0
    sortJP = 181800
    sortGE = 126900
    sortFR = 39400
    sortSP = 27000
    sortIT = 37300
    sortGB = 27300
    sortCN = 145100
    sortTW = 68900
    Driver = 0
    Model = ""
    def __init__(self, Name, RENAMELATER, Price = 5000, Icon = 0, PArmor = 0, EArmor = 0, HP = 0, Str = 0, Eth = 0, Dex = 0, Agi = 0, Lck = 0):
        global IDStart
        global CustomAccessoriesDictList
        IDStart += 1
        IDs.CustomAccessoriesIds.append(IDStart)
        self.Name = Name
        self.Enhance1 = RENAMELATER.id
        self.Price = Price
        self.Rarity = RENAMELATER.Rarity
        self.PArmor = PArmor
        self.EArmor = EArmor
        self.Bns_HpMax = HP
        self.Bns_Strength = Str
        self.Bns_PowEther = Eth
        self.Bns_Dex = Dex
        self.Bns_Agility = Agi
        self.Bns_Luck = Lck
        self.Icon = Icon
        self.id = IDStart

        myNameDict = {          
            "$id": self.id,
            "style": 36,
            "name": self.Name
            } 

        
        
        CustomAccessoryDict = {
        "$id": self.id,
        "Name": self.id,
        "DebugName": self.DebugName,
        "ArmorType": self.ArmorType,
        "Enhance1": self.Enhance1,
        "AddAtr": self.AddAtr,
        "Price": self.Price * (self.Rarity + 1),
        "Rarity": self.Rarity,
        "Flag": self.Flag,
        "PArmor": self.PArmor,
        "EArmor": self.EArmor,
        "Bns_HpMax": self.Bns_HpMax,
        "Bns_Strength": self.Bns_Strength,
        "Bns_PowEther": self.Bns_PowEther,
        "Bns_Dex": self.Bns_Dex,
        "Bns_Agility": self.Bns_Agility,
        "Bns_Luck": self.Bns_Luck,
        "Enhance2": self.Enhance2,
        "Icon": self.Icon,
        "Zone": self.Zone,
        "Zone2": self.Zone2,
        "IraZone": self.IraZone,
        "IraZone2": self.IraZone2,
        "sortJP": self.sortJP,
        "sortGE": self.sortGE,
        "sortFR": self.sortFR,
        "sortSP": self.sortSP,
        "sortIT": self.sortIT,
        "sortGB": self.sortGB,
        "sortCN": self.sortCN,
        "sortTW": self.sortTW,
        "Driver": self.Driver,
        "Model": self.Model
        }
        
        CustomAccessoriesDictList.append(CustomAccessoryDict)
        NameDictList.append(myNameDict)
        
        
def CreateCustomAccessories():
    Enhancements.RunCustomEnhancements(9999)
    
    # Icons
    Boots = 0
    Helm = 1
    Vest = 2
    Necklace = 3
    Belt = 4
    Backpack= 5
    Gloves = 6
    Dice = 7
    Ring = 8
    Medal = 9
    
    # Prices
    Free = 0
    Cheap = 100
    Average = 1000
    Expensive = 2000
    Luxury = 5000
    Fortune = 10000
    
    while IDStart < 687:


        
        
        # Boots = 0
        # Helm = 1
        # Vest = 2
        # Necklace = 3
        # Belt = 4
        # Backpack= 5
        # Gloves = 6
        # Dice = 7
        # Ring = 8
        # Medal = 9

        JSONParser.ReplaceJSONFile("common/ITM_PcEquip.json", CustomAccessoriesDictList)
        JSONParser.ReplaceJSONFile("common_ms/itm_pcequip.json", NameDictList)
        
    # Dont Work for now
    # 
