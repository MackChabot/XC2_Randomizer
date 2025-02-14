from IDs import EnemyBattleMusicMOVs, NonBattleMusicMOVs, NonBattleMusicIDs, ReplacementNonBattleMusicMOVs, ValidEnemyMusicIDs, ValidEnemyMusicWAVs
import JSONParser
import Helper
import json
import random

# RSC_BgmCondition:
# An area usually has 2-3 conditions. If it has 3, its a weather related condition (music is adjusted for weather), usually can tell via large condition value
# condition of 454 is daytime
# condition of 453 is night time
# condition of 1 is debug area, only one this is tied to is gormott area theme
# priority column, value 0 is highest priority, will always play if given a choice of multiple songs. prio goes down as prio # goes up
# I don't know what causes the cave music and gormott lower music to play over other themes tbh.
# Torna fight themes overlap with base game file names ("m0x.wav"->"m2x.wav"), so you can't use them as enemy battle themes in the base game because those point to other themes used in cutscenes in the game.

# Adding new IDs doesn't seem to work
# Reusing other IDs also doesn't seem to work
# Looking like you won't be able to hear all battle themes in game
# So then we keep CHR_EnArrange the same, and randomize the .wav files and place a set number of them into the IDs that work with CHR_EnArrange

def MusicShuffle(OptionsRunDict):
    if OptionsRunDict["Music"]["subOptionObjects"]["Seperate Battle and \nEnvironment Themes"]["subOptionTypeVal"].get():
        with open("./_internal/JsonOutputs/common/RSC_BgmList.json", 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data['rows']:
                if row["$id"] in ValidEnemyMusicIDs:
                    row["filename"] = random.choice(ValidEnemyMusicWAVs)
                    continue
                elif row["$id"] in NonBattleMusicIDs:
                    row["filename"] = random.choice(ReplacementNonBattleMusicMOVs)
                    continue
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        with open("./_internal/JsonOutputs/common/RSC_BgmCondition.json", 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data['rows']:
                if row["$id"] == 34: # Spirit Crucible BGM Calls track m72.wav, which overlaps with a battle theme also called m72.wav, this causes issues when randomized, my code thought it was battle theme, and it is a battle theme for 
                    row["BgmIDB"] = random.choice(NonBattleMusicIDs)
                    row["BgmIDC"] = random.choice(NonBattleMusicIDs)
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        with open("./_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for row in data['rows']: # same issue with track m72.wav, which plays for the teammate fights before the architect (it's mid too), so we replace it with zeke's theme :D (top tier)
                if row["BGMID"] == 49:
                    row["BGMID"] = 16
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
    else:
        JSONParser.ChangeJSONFile(["common/RSC_BgmList.json"], ["filename"], NonBattleMusicMOVs + EnemyBattleMusicMOVs, NonBattleMusicMOVs + EnemyBattleMusicMOVs)
    Helper.ColumnAdjust("./_internal/JsonOutputs/common/EVT_listBf.json", ["opBgm","edBgm"], 0)


