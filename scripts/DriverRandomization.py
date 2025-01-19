import json
import random
from IDs import Lv1ArtCDs, Lv1DamageRatios, EnhancementSets, ValidArtIDs, EvasionEnhancementIDs, SpecialEffectArtIDs, ArtDebuffs, AutoAttacks, ArtBuffs, HitReactions, HitReactionDistribution, OriginalAOECaptionIDs
import JSONParser
import Helper
import IDs

driver_ids = [1, 2, 3, 4, 6]  # Would need modifications to include Vandham, Malos, and Jin (Or Lora, Addam, Hugo, etc)
art_ids = list(range(1, 1000))

driver_names = ['Rex', 'Nia', 'Tora', 'Morag', 'Zeke']
original_driver_tables = dict()

# TODO: How to dynamically populate these?
original_driver_ids = {'Rex': 1, 'Nia': 2, 'Zeke': 3, 'Tora': 4, 'Morag': 6}
new_driver_ids = {'Rex': 2, 'Nia': 1, 'Zeke': 3, 'Tora': 4, 'Morag': 6}

def DriverRandomization(OptionsRunDict):

    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Dr.json"], driver_ids, PopulateOriginalDriverTables)

    GiveNiaAegisSwordArts()

    JSONParser.ChangeJSONLineWithCallback(["common/CHR_Dr.json"], driver_ids, ReplaceRexWithNia)

    JSONParser.ChangeJSONLineWithCallback(["common/BTL_Arts_Dr.json"], art_ids, ReplaceRexArtsWithNiaArts)

def GiveNiaAegisSwordArts():
    nias_monado_arts = []

    def CopyMonadoArts(row):
        if row['WpnType'] == 33 and row['Driver'] == original_driver_ids['Nia']:
            nias_monado_arts.append([row])

    JSONParser.ChangeJSONLineWithCallback(["common/BTL_Arts_Dr.json"], art_ids, CopyMonadoArts)

    # Convert Monado to Aegis Sword
    for art in nias_monado_arts:
        art[0]['WpnType'] = 1

    JSONParser.ExtendJSONFile("common/BTL_Arts_Dr.json", nias_monado_arts)



def PopulateOriginalDriverTables(row):
    for driver in driver_names:
        if row['$id'] == original_driver_ids[driver]:
            original_driver_tables[driver] = dict(row)

def CopyDriverRow(copyTo, copyFrom):
    for key, value in copyTo.items():
        if key == 'Name':
            continue
        copyTo[key] = copyFrom[key]

def ReplaceRexWithNia(row):
    # Turn Rex into Nia
    if row['$id'] == original_driver_ids['Rex']:
        CopyDriverRow(row, original_driver_tables['Nia'])

    # Turn Nia into Rex
    elif row['$id'] == original_driver_ids['Nia']:
        CopyDriverRow(row, original_driver_tables['Rex'])

def ReplaceRexArtsWithNiaArts(row):
    #for driver in driver_names:
    #    if row['Driver'] == original_driver_ids[driver]:
    #        row['Driver'] == new_driver_ids[driver]

    # Move Rex Arts over to the new Driver which is "Rex"
    if row['Driver'] == original_driver_ids['Rex']:
        row['Driver'] == new_driver_ids['Rex']

    # Move Nia Arts over to the new Driver which is "Nia"
    elif row['Driver'] == original_driver_ids['Nia']:
        row['Driver'] == new_driver_ids['Nia']

#TODO: Things that are swapped properly
# ( ) Auto Attacks
# ( ) Arts
# ( ) Skill Trees
# ( ) Favorite Pouch Items
# ( ) Primary Blade
# ( ) 2D Model (Menu)
# ( ) 3D Model (Overworld)
# ( ) Walking/Running Animations
# ( ) Heart to heart requirements? (What should this do?)
# ( ) Whoever replaces rex should get the wind knuckled?
# ( ) Pulling blades in general (specifically once we get characters like Vandham, Jin, and Malos working)
# ( ) Auto Attacks
# ( ) Auto Attacks
