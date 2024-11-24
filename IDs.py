import Helper

#HELPFUL VARIABLES
AuxCores = Helper.InclRange(17001, 17424)# These are all aux cores in ITM_OrbEquip
# AuxCores = Helper.inclRange(15001, 15406) These are all aux cores in ITM_Orb but missing some from orb equip so probably want to use these
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

BladeDefenseDistribution = [0,0,0,0,5,5,5,5,5,5,5,10,10,10,10,10,15,15,15,15,15,15,15,15,20,20,20,20,20,20,20,20,25,25,25,30,30,35,35,40,40,45,50,55,60,65,70,75,80,85,90,95,100]
BladeModDistribution = [0,0,0,5,5,5,10,10,10,10,10,15,15,15,20,20,20,25,25,25,25,25,30,30,30,30,35,35,40,40,45,45,50,70,100]


ValidEnemies =  [x for x in Helper.InclRange(0,1888) if x not in ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 183, 188, 192, 194, 200, 205, 207, 209, 211, 213, 215, 218, 224, 226, 228, 230, 246, 255, 257, 259, 261, 263, 264, 265, 272, 273, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 306, 311, 312, 314, 316, 317, 321, 322, 327, 328, 330, 331, 333, 334, 335, 336, 337, 338, 340, 343, 344, 353, 354, 355, 357, 358, 360, 361, 362, 363, 364, 366, 368, 370, 371, 377, 378, 379, 380, 381, 382, 387, 388, 397, 398, 400, 402, 408, 410, 412, 416, 417, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 438, 439, 440, 441, 442, 443, 444, 449, 452, 453, 460, 465, 467, 469, 471, 472, 473, 478, 480, 482, 484, 486, 494, 499, 502, 505, 507, 509, 511, 514, 516, 518, 520, 522, 524, 526, 527, 528, 529, 530, 531, 537, 539, 541, 543, 545, 554, 556, 574, 575, 580, 582, 584, 585, 586, 587, 589, 590, 592, 594, 595, 596, 597, 599, 605, 606, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 698, 700, 702, 704, 737, 799, 801, 803, 805, 807, 813, 818, 820, 883, 885, 887, 889, 897, 900, 921, 923, 925, 927, 956, 1012, 1013, 1014, 1021, 1024, 1103, 1105, 1107, 1129, 1130, 1133, 1136, 1179, 1180, 1252, 1253, 1257, 1259, 1263, 1274, 1275, 1278, 1280, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1305, 1306, 1307, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318, 1323, 1325, 1327, 1328, 1331, 1332, 1333, 1334, 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1346, 1390, 1392, 1394, 1401, 1403, 1409, 1411, 1426, 1427, 1428, 1446, 1447, 1449, 1450, 1451, 1452, 1453, 1475, 1480, 1481, 1492, 1493, 1494, 1495, 1504, 1505, 1506, 1509, 1510, 1514, 1517, 1520, 1523, 1524, 1525, 1538, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1615, 1620, 1654, 1668, 1669, 1671, 1672, 1673, 1685, 1750, 1751, 1752, 1753, 1887])]