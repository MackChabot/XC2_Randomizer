import json

from scripts import Helper, JSONParser, PopupDescriptions
import random, copy


def PreRandoLogic():
    # TODO: should happen before ALL randomization
    WeakenDefaultNGPlusBladeWeapons() # TODO: Because blade rando copies damage of previous weapon
    DefineModifiedWeaponsForNGPlusBlades() # TODO: Because the new weapons should be given random effects from weapon rando


def PostRandoLogic():
    # TODO: doesn't really matter when it happens
    # TODO: At least before AllowNGPlusWeaponModification(), since AllowNGPlusWeaponModification shifts everything down in the blade table and rewrites the gacha table
    AddAllBladesToGacha()
    RareBladeProbabilityEqualizer()

    # TODO: Should happen after ALL randomization, period
    AllowNGPlusWeaponModification() # Because it gets modified


# def HasRanOnce():
#     # Checks if custom weapons have been added
#     with open("XC2/JsonOutputs/common/ITM_PcWpn.json", 'r+', encoding='utf-8') as cryFile:
#         cryData = json.load(cryFile)
#         for cry in reversed(cryData["rows"]):
#             if cry["$id"] > 6409: # The last ID in the default table
#                 return True
#     return False


def WeakenDefaultNGPlusBladeWeapons():
    ngplus_def_wpns = [5971, 5972, 5973, 5974, 5975, 5976, 5977]

    # Edit their default weapons to be on par with lead chips (baby starting chips)
    with open("XC2/JsonOutputs/common/ITM_PcWpn.json", "r+", encoding='utf-8') as wpnFile:
        wpnData = json.load(wpnFile)

        # Fix default weapons
        for wpn in wpnData["rows"]:
            if wpn["$id"] in ngplus_def_wpns:
                wpn["Rank"] = 1
                wpn["Damage"] = random.randrange(10, 20)
                wpn["CriRate"] = random.choice([5, 10, 15, 20])
                wpn["Flag"]["Private"] = 0

        JSONParser.CloseFile(wpnData, wpnFile)


def AllowNGPlusWeaponModification():
    ngplus_blades = [1043, 1044, 1045, 1046, 1047, 1048, 1049]

    old_to_new_ids = dict()

    # Move the NG+ blades to a vacant ID in the blade table
    # Also allow chip building on NG+ blades (NoBuildWpn = 0)
    with open("XC2/JsonOutputs/common/CHR_Bl.json", "r+", encoding='utf-8') as bladeFile:
        bladeData = json.load(bladeFile)
        for blade in bladeData["rows"]:
            old_id = blade["$id"]
            if old_id in ngplus_blades:
                new_id = bladeData["rows"][-1]["$id"] + 1
                old_to_new_ids[old_id] = new_id
                moved_blade = copy.deepcopy(blade)
                moved_blade["$id"] = new_id
                moved_blade["Flag"]["NoBuildWpn"] = 0
                bladeData["rows"].append(moved_blade)
        JSONParser.CloseFile(bladeData, bladeFile)

    # Modify every reference to the old blades in other tables
    # TODO: Is there anywhere else in this randomizer where we modify these tables in ways that utilize the above hardcoded IDs?
    tables_with_blade_references = {
        "BLD_BladeList": ["StatusID"],
        "BLD_RareList": ["Blade"],
        "BTL_Bl_Personality": ["BLC_C", "BLC_D"], # TODO: Not used
        "CHR_Dr": ["DefBlade1"],
        "CHR_EnArrange": ["BladeID"],
        "FLD_ConditionPT": ["PCID1", "PCID2", "PCID3"],# TODO: Not used
        "FLD_QuestHints": ["MainChar1", "MainChar2", "MainChar3", "MainChar4"],# TODO: Not used
        "FLD_QuestTalk": ["NpcID"],# TODO: Not used
        "FLD_QuestUse": ["bladeID"],# TODO: Not used
        "FLD_randomTalk": ["talk0", "talk1"],# TODO: Not used
        "ITM_CrystalList": ["BladeID"],
        "MNU_EventTheater": ["maincast", "blade_id"],# TODO: Not used
    }
    for table, fields in tables_with_blade_references.items():
        with open(f"XC2/JsonOutputs/common/{table}.json", "r+", encoding='utf-8') as tableFile:
            tableData = json.load(tableFile)
            for row in tableData["rows"]:
                for field in fields:
                    if row[field] in ngplus_blades:
                        row[field] = old_to_new_ids[row[field]]
            JSONParser.CloseFile(tableData, tableFile)


def DefineModifiedWeaponsForNGPlusBlades():
    # Edit their default weapons to be on par with lead chips (baby starting chips) and add new ones
    with open("XC2/JsonOutputs/common/ITM_PcWpn.json", "r+", encoding='utf-8') as wpnFile:
        with open("XC2/JsonOutputs/common/ITM_PcWpnChip.json", "r+", encoding='utf-8') as chipFile:
            wpnData = json.load(wpnFile)
            chipData = json.load(chipFile)

            wpnsById = {item['$id']: item for item in wpnData["rows"]}
            newWpnId = wpnData['rows'][-1]['$id'] + 1

            # TODO: Each chip needs the weapons set for CreateWpnN for N=[20-26]
            for chip in chipData["rows"]:
                for wpnType in range(20, 27):  # CreateWeapons 20-26 which correspond to those NG+ blade weapons
                    # ModelBaseWeapon - The original NG+ weapon (for things like resources, etc.)
                    modelBaseWpn = copy.deepcopy(wpnsById[5971 - 20 + wpnType])

                    # StatsBaseWeapon - A similar weapon for this chip, used to get similar stats
                    wpnType2BaseWpnType = {
                        20: 2,  # Calamity Scythe (Akhos) => Catalyst Scimitar
                        21: 11,  # Cobra Bardiche (Patroka) => Megalance
                        22: 7,  # Infinity Fans (Mikhail) => Whipswords
                        23: 3,  # Brilliant Twinblades (Obrona) => Twin Rings
                        24: 12,  # Decimation Cannon (Perdido) => Ether Cannon
                        25: 13,  # Rockrending Gauntlets (Cressidus) => Shield Hammer
                        26: 14  # Sword Tonfa (Sever) => Chroma Katana
                    }
                    statsBaseWpnType = wpnType2BaseWpnType[wpnType]
                    statsBaseWpn = copy.deepcopy(wpnsById[chip[f"CreateWpn{statsBaseWpnType}"]])

                    # Create the new weapon
                    newWeapon = copy.deepcopy(modelBaseWpn)
                    statsToCopy = ['Rank', 'Damage', 'Stability', 'CriRate', 'GuardRate', 'Enhance1', 'PArmor',
                                   'EArmor', 'Enhance2']
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


def AddAllBladesToGacha():
    with open("XC2/JsonOutputs/common/BLD_RareList.json", "r+", encoding='utf-8') as gachaFile:
        gachaData = json.load(gachaFile)

        # Mikhail, Poppibuster, Shulk, Fiora, Elma
        bladeToAdd = [1045, 1105, 1106, 1107, 1111]

        # Get list of blades already in gacha
        bladesInGacha = []
        for gacha in gachaData["rows"]:
            bladesInGacha.append(gacha["Blade"])

        for newBlade in bladeToAdd:
            # Only add the blade if not in gacha already
            # Note: Some options may have already added these blades

            if newBlade not in bladesInGacha:
                # Copy the first row just to get the schema right
                newGacha = copy.deepcopy(gachaData["rows"][0])

                newGacha['$id'] = gachaData["rows"][-1]['$id'] + 1
                newGacha['Blade'] = newBlade
                gachaData['rows'].append(newGacha)

        JSONParser.CloseFile(gachaData, gachaFile)


def RareBladeProbabilityEqualizer():
    Helper.ColumnAdjust("XC2/JsonOutputs/common/BLD_RareList.json", ["Condition", "Assure1", "Assure2", "Assure3", "Assure4", "Assure5"], 0)
    Helper.ColumnAdjust("XC2/JsonOutputs/common/BLD_RareList.json", ["Prob1", "Prob2", "Prob3", "Prob4", "Prob5"], 1)

    # TODO Testing: Make all blades basically guaranteed, for testing
    # TODO: Delete this
    Helper.ColumnAdjust("XC2/JsonOutputs/common/BLD_RareList.json",["Assure1", "Assure2", "Assure3", "Assure4", "Assure5"], 1)
    Helper.ColumnAdjust("XC2/JsonOutputs/common/BLD_RareList.json", ["Prob1", "Prob2", "Prob3", "Prob4", "Prob5"], 64)


def Description():
    Desc = PopupDescriptions.Description()
    Desc.Header("All Blades Are Created Equal")
    Desc.Image("BladeRandomization.png", "XC2", 700)
    Desc.Text("TODO")
    return Desc