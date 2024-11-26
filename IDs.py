import Helper

#HELPFUL VARIABLES
AuxCores = Helper.inclRange(17001, 17424) + Helper.inclRange(15001, 15406) # These are all aux cores in ITM_OrbEquip and ITM_Orb
WeaponChips = Helper.InclRange(10001, 10060)
CoreCrystals = Helper.InclRange(45001,45057)
Accessories = Helper.InclRange(1,687)
PreciousItems = Helper.InclRange(25001, 25499)
PouchItems =  [x for x in Helper.InclRange(40001,40428) if x not in ([40106, 40107, 40280, 40282, 40284, 40285, 40300, 40387] + Helper.InclRange(40350, 40363) + Helper.InclRange(40389, 40402))]   
AutoAttacks = [1, 2, 3, 8, 9, 10, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 43, 44, 45, 50, 51, 52, 57, 58, 59, 64, 65, 66, 67, 68, 69, 78, 79, 80, 81, 82, 83, 92, 93, 94, 95, 96, 97, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 302, 303, 304, 309, 310, 311, 316, 317, 318, 323, 324, 325, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 582, 583, 584, 592, 593, 594, 602, 603, 604, 612, 613, 614, 622, 623, 624, 632, 633, 634, 642, 643, 644, 652, 653, 654, 662, 663, 664, 672, 673, 674, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726]
ArtDebuffs = [0,1,2,3,4,5,6,7,8,9,16,17,21]
ArtBuffs = [0,11,12,13,14,15,21,23,24,25,30,35]
DriverSkillTrees = Helper.InclRange(1,270)
HitReactions = Helper.InclRange(0,14)
ButtonCombos = Helper.InclRange(1,5)
BladeBattleSkills = Helper.InclRange(1,270)
BladeFieldSkills = Helper.InclRange(1,74)
BladeSpecials = Helper.InclRange(1,269)
BladeTreeUnlockConditions = Helper.InclRange(1,1768)
BladeNames = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 52, 53, 54, 55, 78, 79, 56, 58, 57, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 59, 75, 76, 77, 45, 46, 47, 48, 49, 50, 51, 45, 57, 45, 49, 50, 51, 76, 102, 103, 104, 105, 106, 107, 108]
BackgroundMusic = Helper.InclRange(1,62) + Helper.InclRange(64,100) + Helper.InclRange(117,128) + [132,133,141,142,149,150,153,154] + Helper.InclRange(157,169) + Helper.InclRange(176,180)
Jingles = Helper.InclRange(102,116)
CollectionPointMaterials = [x for x in Helper.InclRange(30001,30445) if x not in [30232, 30233, 30237, 30236, 30243, 30244, 30245, 30246]]
AllValues = Helper.InclRange(0,10000000)
Deeds = Helper.InclRange(25249,25300)
InvalidMusicIDS = [63, 129, 131, 134, 135, 136, 137, 138, 139, 140, 143, 144, 145, 146, 147, 148, 151, 152, 155, 156, 170, 171, 172, 173, 174]
ValidMusicIDs = [x for x in (Helper.InclRange(1,62) + Helper.InclRange(64,100) + Helper.InclRange(117,128) + [132,133,141,142,149,150,153,154] + Helper.InclRange(157,169) + Helper.InclRange(176,180)) if x not in InvalidMusicIDS]
ValidMusicFileNames = ['m24.wav', 'm74.wav', 'm10.wav', 'm72.wav', 'm100.wav', 'm09.wav', 'm301.wav', 'm79.wav', 'm13.wav', 'm01a.wav', 'm48.wav', 'm45.wav', 'm50.wav', 'm99.wav', 'm47.wav', 'm281.wav', 'm58.wav', 'm103.wav', 'm91.wav', 'm64.wav', 'm56.wav', 'm41.wav', 'm34.wav', 'event/m100_loop.wav', 'm87.wav', 'm53.wav', 'm57.wav', 'm22.wav', 'm37.wav', 'm90.wav', 'm302.wav', 'm86.wav', 'm63.wav', 'm44.wav', 'event/m14_loop.wav', 'm71.wav', 'm04.wav', 'm16.wav', 'm26.wav', 'm203.wav', 'm81.wav', 'm97.wav', 'event/m18_loop.wav', 'm55.wav', 'm240.wav', 'm01c.wav', 'm51.wav', 'm27.wav', 'm88.wav', 'm42.wav', 'm96.wav', 'm80.wav', 'm253.wav', 'm95.wav', 'm12.wav', 'm52.wav', 'm49.wav', 'm83.wav', 'm89.wav', 'm06.wav', 'm01b.wav', 'm202.wav', 'm18.wav', 'm69.wav', 'm39.wav', 'm14.wav', 'm02.wav', 'm59.wav', 'm46.wav', 'm93.wav', 'm61.wav', 'm241.wav', 'm62.wav', 'm15.wav', 'm20.wav', 'm77.wav', 'm67.wav', 'm38.wav', 'm19.wav', 'm30.wav', 'm252.wav', 'm282.wav', 'm73.wav', 'm283.wav', 'm76.wav', 'm92.wav', 'm68.wav', 'm43.wav', 'm31.wav', 'm303.wav', 'm07.wav', 'm28.wav', 'm66.wav', 'm36.wav', 'm11.wav', 'm23.wav', 'm78.wav', 'm17.wav', 'm65.wav', 'm03.wav', 'm75.wav', 'm249.wav', 'm85.wav', 'm84.wav', 'm05.wav', 'm21.wav', 'm304.wav', 'm82.wav', 'm32.wav', 'm25.wav', 'm29.wav', 'm54.wav', 'm33.wav', 'm70.wav', 'event/m97_bf04120110_2.wav', 'm94.wav', 'm98.wav', 'm248.wav', 'm60.wav', 'm40.wav', 'm01.wav', 'm35.wav']

BladeDefenseDistribution = [0,0,0,0,5,5,5,5,5,5,5,10,10,10,10,10,15,15,15,15,15,15,15,15,20,20,20,20,20,20,20,20,25,25,25,30,30,35,35,40,40,45,50,55,60,65,70,75,80,85,90,95,100]
BladeModDistribution = [0,0,0,5,5,5,10,10,10,10,10,15,15,15,20,20,20,25,25,25,25,25,30,30,30,30,35,35,40,40,45,45,50,70,100]

InvalidEnemies = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 183, 188, 192, 194, 200, 205, 207, 209, 210, 211, 213, 215, 218, 224, 226, 228, 230, 246, 255, 257, 259, 261, 263, 264, 265, 272, 273, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 306, 311, 312, 314, 316, 317, 321, 322, 327, 328, 330, 331, 333, 334, 335, 336, 337, 338, 340, 343, 344, 353, 354, 355, 357, 358, 360, 361, 362, 363, 364, 366, 368, 370, 371, 377, 378, 379, 380, 381, 382, 387, 388, 397, 398, 400, 402, 408, 410, 412, 416, 417, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 438, 439, 440, 441, 442, 443, 444, 449, 452, 453, 460, 465, 467, 469, 471, 472, 473, 478, 480, 482, 484, 486, 494, 499, 502, 505, 507, 509, 511, 514, 516, 518, 520, 522, 524, 526, 527, 528, 529, 530, 531, 537, 539, 541, 543, 545, 554, 556, 574, 575, 580, 582, 584, 585, 586, 587, 589, 590, 592, 594, 595, 596, 597, 599, 605, 606, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 698, 700, 702, 704, 724, 725, 726, 727, 728, 737, 799, 801, 803, 805, 807, 813, 818, 820, 846, 883, 885, 887, 889, 897, 900, 921, 923, 925, 927, 956, 1012, 1013, 1014, 1021, 1024, 1103, 1105, 1107, 1129, 1130, 1133, 1136, 1179, 1180, 1252, 1253, 1257, 1259, 1263, 1274, 1275, 1278, 1280, 1285, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318, 1323, 1325, 1327, 1328, 1331, 1332, 1333, 1334, 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1346, 1347, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1390, 1392, 1394, 1401, 1403, 1409, 1411, 1420, 1426, 1427, 1428, 1446, 1447, 1449, 1450, 1451, 1452, 1453, 1475, 1480, 1481, 1492, 1493, 1494, 1495, 1504, 1505, 1506, 1509, 1510, 1514, 1517, 1520, 1521, 1523, 1524, 1525, 1533, 1538, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1568, 1569, 1593, 1599, 1615, 1620, 1641, 1654, 1668, 1669, 1671, 1672, 1673, 1685, 1700, 1724, 1725, 1726, 1727, 1731, 1750, 1751, 1752, 1753, 1787, 1788, 1789, 1805, 1806, 1807, 1881, 1883, 1885, 1887]
ValidEnemies =  [x for x in Helper.InclRange(0,1888) if x not in (InvalidEnemies)]

# The Following are IDs corresponding to items I want to shuffle in for race mode, increasing in power level the further in the list they are:
HPUp = [2, 154, 298, 3, 155, 299, 4, 156, 300, 498, 499, 500]
StrUp = [5, 157, 301, 6, 158, 302, 7, 159, 303, 501, 502, 503]
EthUp = [8, 160, 304, 9, 161, 305, 10, 162, 306, 504, 505, 506]
DexUp = [11, 163, 307, 12, 164, 308, 13, 165, 309, 507, 508, 509]
AgiUp = [14, 166, 310, 15, 167, 311, 16, 168, 312, 510, 511, 512]
LucUp = [17, 169, 313, 18, 170, 314, 19, 171, 315, 513, 514, 515]
AutoHeal = [32, 184, 328, 33, 185, 329, 34, 186, 330, 516, 517, 518]
CritHeal = [35, 35, 187, 331, 36, 188, 332, 37, 332, 333, 189, 333]
CritDmg = [38, 190, 334, 39, 191, 335, 40, 192, 336, 519, 520, 521]
AtkTwice = [41, 193, 337, 42, 194, 338, 43, 195, 339, 522, 523, 524]
DmgHigherLv = [53, 205, 349, 54, 206, 350, 55, 207, 351, 534, 535, 536]
BrkLen = [59, 211, 355, 60, 212, 356, 61, 213, 357, 540, 541, 542]
TopLen = [62, 214, 358, 63, 215, 359, 64, 216, 360, 543, 544, 545]
LauLen = [65, 217, 361, 66, 218, 362, 67, 219, 363, 546, 547, 548]
AutoDmg = [68, 220, 364, 69, 221, 365, 70, 222, 366, 549, 550, 551]
AggroDwn = [76, 228, 372, 77, 229, 373, 78, 230, 374, 558, 559, 560]
AggroUp = [79, 231, 375, 80, 232, 376, 81, 233, 377, 561, 562, 563]
AggroStart = [82, 234, 378, 83, 235, 379, 84, 236, 380, 564, 565, 566]
HealArtEff = [91, 243, 387, 92, 244, 388, 93, 245, 389, 567, 568, 569]
CancelHeal = [95, 247, 391, 96, 248, 392, 97, 249, 393, 573, 574, 575]
SpecCDs = [98, 250, 394, 99, 251, 395, 100, 252, 396, 576, 577, 578]
CancelDmg = [101, 253, 397, 102, 254, 398, 103, 255, 399, 579, 580, 581]
PartyGge = [109, 111, 112, 112, 400, 402, 259, 110, 402, 403, 401, 403]
HPPotEff = [141, 285, 429, 142, 286, 430, 143, 287, 431, 431, 431, 431]
BrkResRed = [144, 144, 288, 288, 432, 432, 582, 582, 583, 583, 584, 584]
RiskyDmg = [486, 486, 487, 487, 488, 488, 489, 489, 490, 490, 491, 491]
NoRecoil = [118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118, 118]

AllRaceModeItemTypeIDs = [HPUp, StrUp, EthUp, DexUp, AgiUp, LucUp, AutoHeal, CritHeal, CritDmg, AtkTwice, DmgHigherLv, BrkLen, TopLen, LauLen, AutoDmg, AggroDwn, AggroUp, AggroStart, HealArtEff, CancelHeal, SpecCDs, CancelDmg, PartyGge, HPPotEff, BrkResRed, RiskyDmg, NoRecoil]

# The following are Aux Cores to be equipped in Race Mode, increasing in power level, the further along the list they are:
# This is genuinely fucked up btw, there's no fast way to get these
AuxCrit = [17001, 17001, 17002, 17002, 17003, 17003, 17004, 17004, 17005, 17005, 17352, 17352]
PhysDef = [x + 5 for x in AuxCrit[:10]] + [x + 1 for x in AuxCrit[-2:]]
EthDef = [x + 5 for x in PhysDef[:10]] + [x + 1 for x in PhysDef[-2:]]
BlockRate = [x + 5 for x in EthDef[:10]] + [x + 1 for x in EthDef[-2:]]
BeastHnt = [x + 5 for x in BlockRate[:10]] + [x + 1 for x in BlockRate[-2:]]
InsHnt = [x + 5 for x in BeastHnt[:10]] + [x + 1 for x in BeastHnt[-2:]]
AirHnt = [x + 5 for x in InsHnt[:10]] + [x + 1 for x in InsHnt[-2:]]
AquaHnt = [x + 5 for x in AirHnt[:10]] + [x + 1 for x in AirHnt[-2:]]
HumHnt = [x + 5 for x in AquaHnt[:10]] + [x + 1 for x in AquaHnt[-2:]]
MacHnt = [x + 5 for x in HumHnt[:10]] + [x + 1 for x in HumHnt[-2:]]
TitHnt = [x + 5 for x in MacHnt[:10]] + [x + 1 for x in MacHnt[-2:]]
BldCmbBst = [17056, 17056, 17057, 17057, 17058, 17058, 17059, 17059, 17060, 17060, 17061, 17061]
FusCmbBst = [17062, 17062, 17063, 17063, 17064, 17064, 17065, 17065, 17066, 17066, 17363, 17363]
AggAtkUp = [17077, 17077, 17078, 17078, 17079, 17079, 17080, 17080, 17081, 17081, 17365, 17365]
IndAtkUp = [x + 5 for x in AggAtkUp[:10]] + [x + 1 for x in AggAtkUp[-2:]]
OutAtkUp = [x + 5 for x in IndAtkUp[:10]] + [x + 1 for x in IndAtkUp[-2:]]
FirDef = [x + 5 for x in OutAtkUp[:10]] + [x + 1 for x in OutAtkUp[-2:]]
WatDef = [x + 5 for x in FirDef[:10]] + [x + 1 for x in FirDef[-2:]]
EarDef = [x + 5 for x in WatDef[:10]] + [x + 2 for x in WatDef[-2:]]
WindDef = [x + 5 for x in EarDef[:10]] + [x - 1 for x in EarDef[-2:]] 
ElecDef = [x + 5 for x in WindDef[:10]] + [x + 2 for x in WindDef[-2:]]
IceDef = [x + 5 for x in ElecDef[:10]] + [x + 1 for x in ElecDef[-2:]] 
DarkDef = [x + 5 for x in IceDef[:10]] + [x + 2 for x in IceDef[-2:]] 
LigDef = [x + 5 for x in DarkDef[:10]] + [x - 1 for x in DarkDef[-2:]]
EvaFoc = [x + 22 for x in LigDef[:10]] + [x + 2 for x in LigDef[-2:]]
SwiEva = [x + 5 for x in EvaFoc[:10]] + [x + 1 for x in EvaFoc[-2:]]
EmgGuard = [x + 5 for x in SwiEva[:10]] + [x + 1 for x in SwiEva[-2:]]
Endure = [x + 5 for x in EmgGuard[:10]] + [x + 1 for x in EmgGuard[-2:]]
HPAtkUp = [x + 5 for x in Endure[:10]] + [x + 1 for x in Endure[-2:]]
SpkDef = [17174, 17174, 17175, 17175, 17175, 17176, 17176, 17177, 17177, 17177, 17178, 17178]
BrkRes = [x + 10 for x in HPAtkUp[:10]] + [x + 1 for x in HPAtkUp[-2:]]
TopRes = [x + 5 for x in BrkRes[:10]] + [x + 1 for x in BrkRes[-2:]]
LauRes = [x + 5 for x in TopRes[:10]] + [x + 1 for x in TopRes[-2:]]
SmaRes = [x + 5 for x in LauRes[:10]] + [x + 1 for x in LauRes[-2:]]
BlowRes = [x + 5 for x in SmaRes[:10]] + [x + 1 for x in SmaRes[-2:]]
KBRes = [x + 5 for x in BlowRes[:10]] + [x + 1 for x in BlowRes[-2:]]
AnnulRes = [x + 35 for x in SpkDef]
BldShqRes = [x + 5 for x in AnnulRes]
AASneak = [x + 15 for x in KBRes[:10]] + [x + 1 for x in KBRes[-2:]]
AggBoost = [x + 5 for x in AASneak[:10]] + [x + 1 for x in AASneak[-2:]]
ArtSneak = [x + 5 for x in AggBoost[:10]] + [x + 1 for x in AggBoost[-2:]]
ArtAggUp = [x + 5 for x in ArtSneak[:10]] + [x + 1 for x in ArtSneak[-2:]]
ArtHeal = [x + 5 for x in ArtAggUp[:10]] + [x + 1 for x in ArtAggUp[-2:]]
MoveHeal = [x + 5 for x in ArtHeal[:10]] + [x + 1 for x in ArtHeal[-2:]]
DamHeal = [x + 5 for x in MoveHeal[:10]] + [x + 1 for x in MoveHeal[-2:]]
AMSee = [x + 5 for x in DamHeal[:10]] + [x + 1 for x in DamHeal[-2:]]
PMSee = [x + 5 for x in AMSee[:10]] + [x + 1 for x in AMSee[-2:]]
ReflDmg = [x + 5 for x in PMSee[:10]] + [x + 1 for x in PMSee[-2:]]
RngUp = [x + 55 for x in BldShqRes]
OpeArt = [x + 10 for x in ReflDmg[:10]] + [x + 1 for x in ReflDmg[-2:]]
Telepathy = [x + 10 for x in RngUp]
HelpHand = [x + 5 for x in Telepathy]
AffMaxShld = [x + 15 for x in OpeArt[:10]] + [x + 1 for x in OpeArt[-2:]]
AffMaxAtk = [x + 5 for x in AffMaxShld[:10]] + [x + 1 for x in AffMaxShld[-2:]]
AffMaxEvd = [x + 5 for x in AffMaxAtk[:10]] + [x + 1 for x in AffMaxAtk[-2:]]
HntChem = [x + 20 for x in HelpHand]
StS = [x + 5 for x in HntChem]
FstBldSwp = [17314, 17314, 17315, 17315, 17316, 17316, 17317, 17317, 17318, 17318, 17319, 17319]
Lv1SpecUp = [x + 21 for x in AffMaxEvd[:10]] + [x + 1 for x in AffMaxEvd[-2:]]
Lv2SpecUp = [x + 5 for x in Lv1SpecUp[:10]] + [x + 1 for x in Lv1SpecUp[-2:]]
Lv3SpecUp = [x + 5 for x in Lv2SpecUp[:10]] + [x + 1 for x in Lv2SpecUp[-2:]]
Lv4SpecUp = [x + 5 for x in Lv3SpecUp[:10]] + [x + 1 for x in Lv3SpecUp[-2:]]
AffMaxAcc = [x + 5 for x in Lv4SpecUp[:10]] + [x + 1 for x in Lv4SpecUp[-2:]]
Jamming = [x + 5 for x in AffMaxAcc[:10]] + [x + 1 for x in AffMaxAcc[-2:]]

RaceModeAuxCoreIDs = [AuxCrit, PhysDef, EthDef, BlockRate, BeastHnt, InsHnt, AirHnt, AquaHnt, HumHnt, MacHnt, TitHnt, BldCmbBst, FusCmbBst, AggAtkUp, IndAtkUp, OutAtkUp, FirDef, WatDef, EarDef, WindDef, ElecDef, IceDef, DarkDef, LigDef, EvaFoc, SwiEva, EmgGuard, Endure, HPAtkUp, SpkDef, BrkRes, TopRes, LauRes, SmaRes, BlowRes, KBRes, AnnulRes, BldShqRes, AASneak, AggBoost, ArtSneak, ArtAggUp, ArtHeal, MoveHeal, DamHeal, AMSee, PMSee, ReflDmg, RngUp, OpeArt, Telepathy, HelpHand, AffMaxShld, AffMaxAtk, AffMaxEvd, HntChem, StS, FstBldSwp, Lv1SpecUp, Lv2SpecUp, Lv3SpecUp, Lv4SpecUp, AffMaxAcc, Jamming]

A1RaceModeCoreChipIDs = [10002, 10009, 10010, 10003, 10011, 10017, 10018, 10019, 10005, 10006, 10007]
A2RaceModeCoreChipIDs = [10025, 10026, 10027, 10013, 10014, 10015, 10033, 10034, 10035, 10029, 10030, 10031, 10041, 10042, 10043]
A3RaceModeCoreChipIDs = [10021, 10022, 10023, 10037, 10038, 10039, 10045, 10046, 10047, 10049, 10050, 10051, 10055, 10056, 10057]
A4RaceModeCoreChipIDs = [10004, 10008, 10012, 10016, 10020, 10024, 10028, 10032, 10036, 10040, 10044, 10048, 10052, 10053, 10054, 10058, 10059, 10060]  

