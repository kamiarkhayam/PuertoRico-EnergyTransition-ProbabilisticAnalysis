import os

def write_temoa_input_file_fd(template_path, new_file_path, new_file_name, \
                        sunnyRatios, windyRatios, populationProj, perCapitaProj, ngPriceProj, urnPriceProj,\
                        e_ngVarProj, e_ngFixProj, e_ngInvProj, e_nucVarProj, e_nucFixProj, e_nucInvProj, \
                        e_solInvProj, e_windInvProj, e_hydInvProj, e_battInvProj,\
                        e_solFixProj, e_windFixProj, e_hydFixProj, e_battFixProj,\
                        e_hydCF, solCf, windCf1, windCf2, windCf3, windCf4):
    
    with open(template_path) as f:
        lines = f.readlines()
        f.close()
        
        #SegFracs Edit
        sunny7_12 = sunnyRatios[0] * windyRatios[0]
        sunny12_17 = sunnyRatios[0] * windyRatios[1]
        sunny17_24 = sunnyRatios[0] * windyRatios[2]
        sunny24_31 = sunnyRatios[0] * windyRatios[3]
        sunny31_38 = sunnyRatios[0] * windyRatios[4]
        sunnyOther = sunnyRatios[0] * windyRatios[5]
        
        partsunny7_12 = sunnyRatios[1] * windyRatios[0]
        partsunny12_17 = sunnyRatios[1] * windyRatios[1]
        partsunny17_24 = sunnyRatios[1] * windyRatios[2]
        partsunny24_31 = sunnyRatios[1] * windyRatios[3]
        partsunny31_38 = sunnyRatios[1] * windyRatios[4]
        partsunnyOther = sunnyRatios[1] * windyRatios[5]
        
        cloudy7_12 = sunnyRatios[2] * windyRatios[0]
        cloudy12_17 = sunnyRatios[2] * windyRatios[1]
        cloudy17_24 = sunnyRatios[2] * windyRatios[2]
        cloudy24_31 = sunnyRatios[2] * windyRatios[3]
        cloudy31_38 = sunnyRatios[2] * windyRatios[4]
        cloudyOther = sunnyRatios[2] * windyRatios[5]
        
        
        lines[225] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w7_12\',\'day\','+str(sunny7_12/2)+',\'sunny-w7_12 - Day\');\n'
        lines[226] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w7_12\',\'night\','+str(sunny7_12/2)+',\'sunny-w7_12 - Night\');\n'
        lines[227] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w12_17\',\'day\','+str(sunny12_17/2)+',\'sunny-w12_17 - Day\');\n'
        lines[228] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w12_17\',\'night\','+str(sunny12_17/2)+',\'sunny-w12_17 - Night\');\n'
        lines[229] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w17_24\',\'day\','+str(sunny17_24/2)+',\'sunny-w17_24 - Day\');\n'
        lines[230] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w17_24\',\'night\','+str(sunny17_24/2)+',\'sunny-w17_24 - Night\');\n'
        lines[231] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w24_31\',\'day\','+str(sunny24_31/2)+',\'sunny-w24_31 - Day\');\n'
        lines[232] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w24_31\',\'night\','+str(sunny24_31/2)+',\'sunny-w24_31 - Night\');\n'
        lines[233] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w31_38\',\'day\','+str(sunny31_38/2)+',\'sunny-w31_38 - Day\');\n'
        lines[234] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w31_38\',\'night\','+str(sunny31_38/2)+',\'sunny-w31_38 - Night\');\n'
        lines[235] = 'INSERT INTO `SegFrac` VALUES (\'sunny-wother\',\'day\','+str(sunnyOther/2)+',\'sunny-wother - Day\');\n'
        lines[236] = 'INSERT INTO `SegFrac` VALUES (\'sunny-wother\',\'night\','+str(sunnyOther/2)+',\'sunny-wother - Night\');\n'
        
        lines[238] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w7_12\',\'day\','+str(partsunny7_12/2)+',\'partsunny-w7_12 - Day\');\n'
        lines[239] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w7_12\',\'night\','+str(partsunny7_12/2)+',\'partsunny-w7_12 - Night\');\n'
        lines[240] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w12_17\',\'day\','+str(partsunny12_17/2)+',\'partsunny-w12_17 - Day\');\n'
        lines[241] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w12_17\',\'night\','+str(partsunny12_17/2)+',\'partsunny-w12_17 - Night\');\n'
        lines[242] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w17_24\',\'day\','+str(partsunny17_24/2)+',\'partsunny-w17_24 - Day\');\n'
        lines[243] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w17_24\',\'night\','+str(partsunny17_24/2)+',\'partsunny-w17_24 - Night\');\n'
        lines[244] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w24_31\',\'day\','+str(partsunny24_31/2)+',\'partsunny-w24_31 - Day\');\n'
        lines[245] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w24_31\',\'night\','+str(partsunny24_31/2)+',\'partsunny-w24_31 - Night\');\n'
        lines[246] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w31_38\',\'day\','+str(partsunny31_38/2)+',\'partsunny-w31_38 - Day\');\n'
        lines[247] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w31_38\',\'night\','+str(partsunny31_38/2)+',\'partsunny-w31_38 - Night\');\n'
        lines[248] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-wother\',\'day\','+str(partsunnyOther/2)+',\'partsunny-wother - Day\');\n'
        lines[249] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-wother\',\'night\','+str(partsunnyOther/2)+',\'partsunny-wother - Night\');\n'
        
        lines[251] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w7_12\',\'day\','+str(cloudy7_12/2)+',\'cloudy-w7_12 - Day\');\n'
        lines[252] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w7_12\',\'night\','+str(cloudy7_12/2)+',\'cloudy-w7_12 - Night\');\n'
        lines[253] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w12_17\',\'day\','+str(cloudy12_17/2)+',\'cloudy-w12_17 - Day\');\n'
        lines[254] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w12_17\',\'night\','+str(cloudy12_17/2)+',\'cloudy-w12_17 - Night\');\n'
        lines[255] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w17_24\',\'day\','+str(cloudy17_24/2)+',\'cloudy-w17_24 - Day\');\n'
        lines[256] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w17_24\',\'night\','+str(cloudy17_24/2)+',\'cloudy-w17_24 - Night\');\n'
        lines[257] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w24_31\',\'day\','+str(cloudy24_31/2)+',\'cloudy-w24_31 - Day\');\n'
        lines[258] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w24_31\',\'night\','+str(cloudy24_31/2)+',\'cloudy-w24_31 - Night\');\n'
        lines[259] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w31_38\',\'day\','+str(cloudy31_38/2)+',\'cloudy-w31_38 - Day\');\n'
        lines[260] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w31_38\',\'night\','+str(cloudy31_38/2)+',\'cloudy-w31_38 - Night\');\n'
        lines[261] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-wother\',\'day\','+str(cloudyOther/2)+',\'cloudy-wother - Day\');\n'
        lines[262] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-wother\',\'night\','+str(cloudyOther/2)+',\'cloudy-wother - Night\');\n'
        
        
        #Demand Specific Distribution edit
        lines[762] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w7_12\',\'day\',\'DMND\','+str(sunny7_12/2)+',\'\');\n'
        lines[763] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w7_12\',\'night\',\'DMND\','+str(sunny7_12/2)+',\'\');\n'
        lines[764] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w12_17\',\'day\',\'DMND\','+str(sunny12_17/2)+',\'\');\n'
        lines[765] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w12_17\',\'night\',\'DMND\','+str(sunny12_17/2)+',\'\');\n'
        lines[766] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w17_24\',\'day\',\'DMND\','+str(sunny17_24/2)+',\'\');\n'
        lines[767] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w17_24\',\'night\',\'DMND\','+str(sunny17_24/2)+',\'\');\n'
        lines[768] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w24_31\',\'day\',\'DMND\','+str(sunny24_31/2)+',\'\');\n'
        lines[769] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w24_31\',\'night\',\'DMND\','+str(sunny24_31/2)+',\'\');\n'
        lines[770] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w31_38\',\'day\',\'DMND\','+str(sunny31_38/2)+',\'\');\n'
        lines[771] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w31_38\',\'night\',\'DMND\','+str(sunny31_38/2)+',\'\');\n'
        lines[772] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-wother\',\'day\',\'DMND\','+str(sunnyOther/2)+',\'\');\n'
        lines[773] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-wother\',\'night\',\'DMND\','+str(sunnyOther/2)+',\'\');\n'
        
        lines[775] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w7_12\',\'day\',\'DMND\','+str(partsunny7_12/2)+',\'\');\n'
        lines[776] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w7_12\',\'night\',\'DMND\','+str(partsunny7_12/2)+',\'\');\n'
        lines[777] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w12_17\',\'day\',\'DMND\','+str(partsunny12_17/2)+',\'\');\n'
        lines[778] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w12_17\',\'night\',\'DMND\','+str(partsunny12_17/2)+',\'\');\n'
        lines[779] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w17_24\',\'day\',\'DMND\','+str(partsunny17_24/2)+',\'\');\n'
        lines[780] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w17_24\',\'night\',\'DMND\','+str(partsunny17_24/2)+',\'\');\n'
        lines[781] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w24_31\',\'day\',\'DMND\','+str(partsunny24_31/2)+',\'\');\n'
        lines[782] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w24_31\',\'night\',\'DMND\','+str(partsunny24_31/2)+',\'\');\n'
        lines[783] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w31_38\',\'day\',\'DMND\','+str(partsunny31_38/2)+',\'\');\n'
        lines[784] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w31_38\',\'night\',\'DMND\','+str(partsunny31_38/2)+',\'\');\n'
        lines[785] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-wother\',\'day\',\'DMND\','+str(partsunnyOther/2)+',\'\');\n'
        lines[786] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-wother\',\'night\',\'DMND\','+str(partsunnyOther/2)+',\'\');\n'
        
        lines[788] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w7_12\',\'day\',\'DMND\','+str(cloudy7_12/2)+',\'\');\n'
        lines[789] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w7_12\',\'night\',\'DMND\','+str(cloudy7_12/2)+',\'\');\n'
        lines[790] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w12_17\',\'day\',\'DMND\','+str(cloudy12_17/2)+',\'\');\n'
        lines[791] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w12_17\',\'night\',\'DMND\','+str(cloudy12_17/2)+',\'\');\n'
        lines[792] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w17_24\',\'day\',\'DMND\','+str(cloudy17_24/2)+',\'\');\n'
        lines[793] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w17_24\',\'night\',\'DMND\','+str(cloudy17_24/2)+',\'\');\n'
        lines[794] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w24_31\',\'day\',\'DMND\','+str(cloudy24_31/2)+',\'\');\n'
        lines[795] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w24_31\',\'night\',\'DMND\','+str(cloudy24_31/2)+',\'\');\n'
        lines[796] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w31_38\',\'day\',\'DMND\','+str(cloudy31_38/2)+',\'\');\n'
        lines[797] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w31_38\',\'night\',\'DMND\','+str(cloudy31_38/2)+',\'\');\n'
        lines[798] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-wother\',\'day\',\'DMND\','+str(cloudyOther/2)+',\'\');\n'
        lines[799] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-wother\',\'night\',\'DMND\','+str(cloudyOther/2)+',\'\');\n'
        
        
        #Demand
        demand2025 = populationProj['2025'] * perCapitaProj['2025'] / (277.78 * 10**6)
        demand2030 = populationProj['2030'] * perCapitaProj['2030'] / (277.78 * 10**6)
        demand2035 = populationProj['2035'] * perCapitaProj['2035'] / (277.78 * 10**6)
        demand2040 = populationProj['2040'] * perCapitaProj['2040'] / (277.78 * 10**6)
        demand2045 = populationProj['2045'] * perCapitaProj['2045'] / (277.78 * 10**6)
        demand2049 = populationProj['2050'] * perCapitaProj['2050'] / (277.78 * 10**6)
        
        
        lines[813] = 'INSERT INTO `Demand` VALUES (\'R1\',2025,\'DMND\','+str(demand2025)+',\'\',\'\');\n'
        lines[814] = 'INSERT INTO `Demand` VALUES (\'R1\',2030,\'DMND\','+str(demand2030)+',\'\',\'\');\n'
        lines[815] = 'INSERT INTO `Demand` VALUES (\'R1\',2035,\'DMND\','+str(demand2035)+',\'\',\'\');\n'
        lines[816] = 'INSERT INTO `Demand` VALUES (\'R1\',2040,\'DMND\','+str(demand2040)+',\'\',\'\');\n'
        lines[817] = 'INSERT INTO `Demand` VALUES (\'R1\',2045,\'DMND\','+str(demand2045)+',\'\',\'\');\n'
        lines[818] = 'INSERT INTO `Demand` VALUES (\'R1\',2049,\'DMND\','+str(demand2049)+',\'\',\'\');\n'
        
        #NG Price Edit
        ngPrice2025 = ngPriceProj['2025']
        ngPrice2030 = ngPriceProj['2030']
        ngPrice2035 = ngPriceProj['2035']
        ngPrice2040 = ngPriceProj['2040']
        ngPrice2045 = ngPriceProj['2045']
        ngPrice2049 = ngPriceProj['2050']
        
        lines[833] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPNG\',2020,'+str(ngPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[834] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPNG\',2020,'+str(ngPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[835] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPNG\',2020,'+str(ngPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[836] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2020,'+str(ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[837] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2020,'+str(ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[838] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2020,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[839] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPNG\',2025,'+str(ngPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[840] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPNG\',2025,'+str(ngPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[841] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPNG\',2025,'+str(ngPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[842] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2025,'+str(ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[843] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2025,'+str(ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[844] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2025,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[845] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPNG\',2030,'+str(ngPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[846] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPNG\',2030,'+str(ngPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[847] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2030,'+str(ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[848] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2030,'+str(ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[849] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2030,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[850] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPNG\',2035,'+str(ngPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[851] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2035,'+str(ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[852] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2035,'+str(ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[853] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2035,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[854] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2040,'+str(ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[855] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2040,'+str(ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[856] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2040,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[857] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2045,'+str(ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[858] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2045,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[859] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2049,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        
        #Uranium Price Edit
        urnPrice2025 = urnPriceProj['2025']
        urnPrice2030 = urnPriceProj['2030']
        urnPrice2035 = urnPriceProj['2035']
        urnPrice2040 = urnPriceProj['2040']
        urnPrice2045 = urnPriceProj['2045']
        urnPrice2049 = urnPriceProj['2050']
        
        lines[861] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPURN\',2025,'+str(urnPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[862] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPURN\',2025,'+str(urnPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[863] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPURN\',2025,'+str(urnPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[864] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPURN\',2025,'+str(urnPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[865] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2025,'+str(urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[866] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2025,'+str(urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[867] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPURN\',2030,'+str(urnPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[868] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPURN\',2030,'+str(urnPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[869] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPURN\',2030,'+str(urnPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[870] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2030,'+str(urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[871] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2030,'+str(urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[872] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPURN\',2035,'+str(urnPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[873] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPURN\',2035,'+str(urnPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[874] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2035,'+str(urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[875] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2035,'+str(urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[876] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPURN\',2040,'+str(urnPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[877] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2040,'+str(urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[878] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2040,'+str(urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[879] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2045,'+str(urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[880] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2045,'+str(urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[881] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2049,'+str(urnPrice2049)+',\'$M/PJ\',\'\');\n'
        
        #E_NG Var Price Edit
        e_ng_var2025 = e_ngVarProj['2025']
        e_ng_var2030 = e_ngVarProj['2030']
        e_ng_var2035 = e_ngVarProj['2035']
        e_ng_var2040 = e_ngVarProj['2040']
        e_ng_var2045 = e_ngVarProj['2045']
        e_ng_var2049 = e_ngVarProj['2050']
        
        lines[883] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'E_NGCC\',2020,'+str(e_ng_var2025)+',\'$M/PJ\',\'\');\n'
        lines[884] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NGCC\',2020,'+str(e_ng_var2030)+',\'$M/PJ\',\'\');\n'
        lines[885] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NGCC\',2020,'+str(e_ng_var2035)+',\'$M/PJ\',\'\');\n'
        lines[886] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2020,'+str(e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[887] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2020,'+str(e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[888] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2020,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[889] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'E_NGCC\',2025,'+str(e_ng_var2025)+',\'$M/PJ\',\'\');\n'
        lines[890] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NGCC\',2025,'+str(e_ng_var2030)+',\'$M/PJ\',\'\');\n'
        lines[891] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NGCC\',2025,'+str(e_ng_var2035)+',\'$M/PJ\',\'\');\n'
        lines[892] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2025,'+str(e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[893] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2025,'+str(e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[894] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2025,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[895] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NGCC\',2030,'+str(e_ng_var2030)+',\'$M/PJ\',\'\');\n'
        lines[896] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NGCC\',2030,'+str(e_ng_var2035)+',\'$M/PJ\',\'\');\n'
        lines[897] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2030,'+str(e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[898] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2030,'+str(e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[899] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2030,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[900] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NGCC\',2035,'+str(e_ng_var2035)+',\'$M/PJ\',\'\');\n'
        lines[901] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2035,'+str(e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[902] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2035,'+str(e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[903] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2035,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[904] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2040,'+str(e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[905] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2040,'+str(e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[906] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2040,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[907] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2045,'+str(e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[908] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2045,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[909] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2049,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        
        #E_NUC Var Price Edit
        e_urn_var2025 = e_nucVarProj['2025']
        e_urn_var2030 = e_nucVarProj['2030']
        e_urn_var2035 = e_nucVarProj['2035']
        e_urn_var2040 = e_nucVarProj['2040']
        e_urn_var2045 = e_nucVarProj['2045']
        e_urn_var2049 = e_nucVarProj['2050']
        
        lines[911] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'E_NUCLEAR\',2025,'+str(e_urn_var2025)+',\'$M/PJ\',\'\');\n'
        lines[912] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NUCLEAR\',2025,'+str(e_urn_var2030)+',\'$M/PJ\',\'\');\n'
        lines[913] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NUCLEAR\',2025,'+str(e_urn_var2035)+',\'$M/PJ\',\'\');\n'
        lines[914] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NUCLEAR\',2025,'+str(e_urn_var2040)+',\'$M/PJ\',\'\');\n'
        lines[915] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2025,'+str(e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[916] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2025,'+str(e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[917] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NUCLEAR\',2030,'+str(e_urn_var2030)+',\'$M/PJ\',\'\');\n'
        lines[918] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NUCLEAR\',2030,'+str(e_urn_var2035)+',\'$M/PJ\',\'\');\n'
        lines[919] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NUCLEAR\',2030,'+str(e_urn_var2040)+',\'$M/PJ\',\'\');\n'
        lines[920] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2030,'+str(e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[921] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2030,'+str(e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[922] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NUCLEAR\',2035,'+str(e_urn_var2035)+',\'$M/PJ\',\'\');\n'
        lines[923] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NUCLEAR\',2035,'+str(e_urn_var2040)+',\'$M/PJ\',\'\');\n'
        lines[924] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2035,'+str(e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[925] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2035,'+str(e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[926] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NUCLEAR\',2040,'+str(e_urn_var2040)+',\'$M/PJ\',\'\');\n'
        lines[927] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2040,'+str(e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[928] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2040,'+str(e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[929] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2045,'+str(e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[930] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2045,'+str(e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[931] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2049,'+str(e_urn_var2049)+',\'$M/PJ\',\'\');\n'
       
        #Investment Costs Price Edit
        e_ng_inv2025 = e_ngInvProj['2025']
        e_ng_inv2030 = e_ngInvProj['2030']
        e_ng_inv2035 = e_ngInvProj['2035']
        e_ng_inv2040 = e_ngInvProj['2040']
        e_ng_inv2045 = e_ngInvProj['2045']
        e_ng_inv2049 = e_ngInvProj['2050']
        
        e_sol_inv2025 = e_solInvProj['2025']
        e_sol_inv2030 = e_solInvProj['2030']
        e_sol_inv2035 = e_solInvProj['2035']
        e_sol_inv2040 = e_solInvProj['2040']
        e_sol_inv2045 = e_solInvProj['2045']
        e_sol_inv2049 = e_solInvProj['2050']
        
        e_wind_inv2025 = e_windInvProj['2025']
        e_wind_inv2030 = e_windInvProj['2030']
        e_wind_inv2035 = e_windInvProj['2035']
        e_wind_inv2040 = e_windInvProj['2040']
        e_wind_inv2045 = e_windInvProj['2045']
        e_wind_inv2049 = e_windInvProj['2050']
        
        e_nuc_inv2025 = e_nucInvProj['2025']
        e_nuc_inv2030 = e_nucInvProj['2030']
        e_nuc_inv2035 = e_nucInvProj['2035']
        e_nuc_inv2040 = e_nucInvProj['2040']
        e_nuc_inv2045 = e_nucInvProj['2045']
        e_nuc_inv2049 = e_nucInvProj['2050']
        
        e_hyd_inv2025 = e_hydInvProj['2025']
        e_hyd_inv2030 = e_hydInvProj['2030']
        e_hyd_inv2035 = e_hydInvProj['2035']
        e_hyd_inv2040 = e_hydInvProj['2040']
        e_hyd_inv2045 = e_hydInvProj['2045']
        e_hyd_inv2049 = e_hydInvProj['2050']
       
        e_batt_inv2025 = e_battInvProj['2025']
        e_batt_inv2030 = e_battInvProj['2030']
        e_batt_inv2035 = e_battInvProj['2035']
        e_batt_inv2040 = e_battInvProj['2040']
        e_batt_inv2045 = e_battInvProj['2045']
        e_batt_inv2049 = e_battInvProj['2050']
        
        lines[1001] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2025,'+str(e_ng_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1002] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2025,'+str(e_sol_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1003] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2025,'+str(e_wind_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1004] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2025,'+str(e_nuc_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1005] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2025,'+str(e_hyd_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1007] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2025,'+str(e_batt_inv2025)+',\'$M/GW\',\'\');\n'
        
        lines[1013] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2030,'+str(e_ng_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1014] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2030,'+str(e_sol_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1015] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2030,'+str(e_wind_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1016] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2030,'+str(e_nuc_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1017] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2030,'+str(e_hyd_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1019] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2030,'+str(e_batt_inv2030)+',\'$M/GW\',\'\');\n'
        
        lines[1025] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2035,'+str(e_ng_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1026] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2035,'+str(e_sol_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1027] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2035,'+str(e_wind_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1028] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2035,'+str(e_nuc_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1029] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2035,'+str(e_hyd_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1031] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2035,'+str(e_batt_inv2035)+',\'$M/GW\',\'\');\n'
        
        lines[1037] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2040,'+str(e_ng_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1038] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2040,'+str(e_sol_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1039] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2040,'+str(e_wind_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1040] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2040,'+str(e_nuc_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1041] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2040,'+str(e_hyd_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1043] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2040,'+str(e_batt_inv2040)+',\'$M/GW\',\'\');\n'
         
        lines[1049] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2045,'+str(e_ng_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1050] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2045,'+str(e_sol_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1051] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2045,'+str(e_wind_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1052] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2045,'+str(e_nuc_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1053] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2045,'+str(e_hyd_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1055] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2045,'+str(e_batt_inv2045)+',\'$M/GW\',\'\');\n'
        
        lines[1061] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2049,'+str(e_ng_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1062] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2049,'+str(e_sol_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1063] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2049,'+str(e_wind_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1064] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2049,'+str(e_nuc_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1065] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2049,'+str(e_hyd_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1067] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2049,'+str(e_batt_inv2049)+',\'$M/GW\',\'\');\n'
        

        
        #E_NG Fix Price Edit
        e_ng_fix2020 = e_ngFixProj['2020']
        e_ng_fix2025 = e_ngFixProj['2025']
        e_ng_fix2030 = e_ngFixProj['2030']
        e_ng_fix2035 = e_ngFixProj['2035']
        e_ng_fix2040 = e_ngFixProj['2040']
        e_ng_fix2045 = e_ngFixProj['2045']
        e_ng_fix2049 = e_ngFixProj['2050']
        
        lines[1087] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_NGCC\',2020,'+str(e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1088] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NGCC\',2020,'+str(e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1089] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NGCC\',2020,'+str(e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1090] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2020,'+str(e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1091] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2020,'+str(e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1092] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2020,'+str(e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1093] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_NGCC\',2025,'+str(e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1094] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NGCC\',2025,'+str(e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1095] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NGCC\',2025,'+str(e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1096] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2025,'+str(e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1097] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2025,'+str(e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1098] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2025,'+str(e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1099] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NGCC\',2030,'+str(e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1100] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NGCC\',2030,'+str(e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1101] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2030,'+str(e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1102] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2030,'+str(e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1103] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2030,'+str(e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1104] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NGCC\',2035,'+str(e_ng_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1105] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2035,'+str(e_ng_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1106] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2035,'+str(e_ng_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1107] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2035,'+str(e_ng_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1108] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2040,'+str(e_ng_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1109] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2040,'+str(e_ng_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1110] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2040,'+str(e_ng_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1111] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2045,'+str(e_ng_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1112] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2045,'+str(e_ng_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1113] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2049,'+str(e_ng_fix2049)+',\'$M/GWyr\',\'\');\n'
        
        
        #E_SOL Fix Price Edit
        e_sol_fix2020 = e_solFixProj['2020']
        e_sol_fix2025 = e_solFixProj['2025']
        e_sol_fix2030 = e_solFixProj['2030']
        e_sol_fix2035 = e_solFixProj['2035']
        e_sol_fix2040 = e_solFixProj['2040']
        e_sol_fix2045 = e_solFixProj['2045']
        e_sol_fix2049 = e_solFixProj['2050']
        
        lines[1115] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_SOLPV\',2020,'+str(e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1116] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_SOLPV\',2020,'+str(e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1117] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_SOLPV\',2020,'+str(e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1118] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2020,'+str(e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1119] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2020,'+str(e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1120] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2020,'+str(e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1121] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_SOLPV\',2025,'+str(e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1122] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_SOLPV\',2025,'+str(e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1123] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_SOLPV\',2025,'+str(e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1124] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2025,'+str(e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1125] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2025,'+str(e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1126] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2025,'+str(e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1127] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_SOLPV\',2030,'+str(e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1128] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_SOLPV\',2030,'+str(e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1129] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2030,'+str(e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1130] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2030,'+str(e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1131] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2030,'+str(e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1132] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_SOLPV\',2035,'+str(e_sol_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1133] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2035,'+str(e_sol_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1134] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2035,'+str(e_sol_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1135] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2035,'+str(e_sol_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1136] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2040,'+str(e_sol_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1137] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2040,'+str(e_sol_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1138] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2040,'+str(e_sol_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1139] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2045,'+str(e_sol_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1140] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2045,'+str(e_sol_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1141] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2049,'+str(e_sol_fix2049)+',\'$M/GWyr\',\'\');\n'
        
        #E_WIND Fix Price Edit
        e_wind_fix2020 = e_windFixProj['2020']
        e_wind_fix2025 = e_windFixProj['2025']
        e_wind_fix2030 = e_windFixProj['2030']
        e_wind_fix2035 = e_windFixProj['2035']
        e_wind_fix2040 = e_windFixProj['2040']
        e_wind_fix2045 = e_windFixProj['2045']
        e_wind_fix2049 = e_windFixProj['2050']
        
        lines[1143] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_WIND\',2020,'+str(e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1144] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_WIND\',2020,'+str(e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1145] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_WIND\',2020,'+str(e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1146] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2020,'+str(e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1147] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2020,'+str(e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1148] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2020,'+str(e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1149] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_WIND\',2025,'+str(e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1150] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_WIND\',2025,'+str(e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1151] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_WIND\',2025,'+str(e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1152] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2025,'+str(e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1153] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2025,'+str(e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1154] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2025,'+str(e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1155] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_WIND\',2030,'+str(e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1156] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_WIND\',2030,'+str(e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1157] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2030,'+str(e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1158] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2030,'+str(e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1159] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2030,'+str(e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1160] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_WIND\',2035,'+str(e_wind_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1161] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2035,'+str(e_wind_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1162] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2035,'+str(e_wind_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1163] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2035,'+str(e_wind_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1164] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2040,'+str(e_wind_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1165] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2040,'+str(e_wind_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1166] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2040,'+str(e_wind_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1167] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2045,'+str(e_wind_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1168] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2045,'+str(e_wind_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1169] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2049,'+str(e_wind_fix2049)+',\'$M/GWyr\',\'\');\n'
        
        
        #E_HYDRO Fix Price Edit
        e_hyd_fix2025 = e_hydFixProj['2025']
        e_hyd_fix2030 = e_hydFixProj['2030']
        e_hyd_fix2035 = e_hydFixProj['2035']
        e_hyd_fix2040 = e_hydFixProj['2040']
        e_hyd_fix2045 = e_hydFixProj['2045']
        e_hyd_fix2049 = e_hydFixProj['2050']
        
        lines[1171] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_HYDRO\',2025,'+str(e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1172] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_HYDRO\',2025,'+str(e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1173] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_HYDRO\',2025,'+str(e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1174] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_HYDRO\',2025,'+str(e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1175] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2025,'+str(e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1176] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2025,'+str(e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1177] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_HYDRO\',2030,'+str(e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1178] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_HYDRO\',2030,'+str(e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1179] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_HYDRO\',2030,'+str(e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1180] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2030,'+str(e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1181] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2030,'+str(e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1182] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_HYDRO\',2035,'+str(e_hyd_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1183] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_HYDRO\',2035,'+str(e_hyd_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1184] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2035,'+str(e_hyd_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1185] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2035,'+str(e_hyd_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1186] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_HYDRO\',2040,'+str(e_hyd_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1187] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2040,'+str(e_hyd_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1188] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2040,'+str(e_hyd_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1189] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2045,'+str(e_hyd_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1190] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2045,'+str(e_hyd_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1191] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2049,'+str(e_hyd_fix2049)+',\'$M/GWyr\',\'\');\n'

        
        #E_NUCLEAR Fix Price Edit
        e_nuc_fix2025 = e_nucFixProj['2025']
        e_nuc_fix2030 = e_nucFixProj['2030']
        e_nuc_fix2035 = e_nucFixProj['2035']
        e_nuc_fix2040 = e_nucFixProj['2040']
        e_nuc_fix2045 = e_nucFixProj['2045']
        e_nuc_fix2049 = e_nucFixProj['2050']
        
        lines[1215] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_NUCLEAR\',2025,'+str(e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1216] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NUCLEAR\',2025,'+str(e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1217] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NUCLEAR\',2025,'+str(e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1218] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NUCLEAR\',2025,'+str(e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1219] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2025,'+str(e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1220] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2025,'+str(e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1221] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NUCLEAR\',2030,'+str(e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1222] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NUCLEAR\',2030,'+str(e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1223] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NUCLEAR\',2030,'+str(e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1224] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2030,'+str(e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1225] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2030,'+str(e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1226] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NUCLEAR\',2035,'+str(e_nuc_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1227] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NUCLEAR\',2035,'+str(e_nuc_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1228] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2035,'+str(e_nuc_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1229] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2035,'+str(e_nuc_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1230] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NUCLEAR\',2040,'+str(e_nuc_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1231] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2040,'+str(e_nuc_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1232] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2040,'+str(e_nuc_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1233] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2045,'+str(e_nuc_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1234] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2045,'+str(e_nuc_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1235] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2049,'+str(e_nuc_fix2049)+',\'$M/GWyr\',\'\');\n'
        
        
        #E_BATT Fix Price Edit
        e_batt_fix2025 = e_battFixProj['2025']
        e_batt_fix2030 = e_battFixProj['2030']
        e_batt_fix2035 = e_battFixProj['2035']
        e_batt_fix2040 = e_battFixProj['2040']
        e_batt_fix2045 = e_battFixProj['2045']
        e_batt_fix2049 = e_battFixProj['2050']
        
        lines[1237] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_BATT\',2025,'+str(e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1238] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_BATT\',2025,'+str(e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1239] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BATT\',2025,'+str(e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1240] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BATT\',2025,'+str(e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1241] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2025,'+str(e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1242] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2025,'+str(e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1243] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_BATT\',2030,'+str(e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1244] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BATT\',2030,'+str(e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1245] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BATT\',2030,'+str(e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1246] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2030,'+str(e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1247] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2030,'+str(e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1248] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BATT\',2035,'+str(e_batt_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1249] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BATT\',2035,'+str(e_batt_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1250] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2035,'+str(e_batt_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1251] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2035,'+str(e_batt_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1252] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BATT\',2040,'+str(e_batt_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1253] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2040,'+str(e_batt_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1254] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2040,'+str(e_batt_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1255] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2045,'+str(e_batt_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1256] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2045,'+str(e_batt_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1257] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2049,'+str(e_batt_fix2049)+',\'$M/GWyr\',\'\');\n'
        
        
        #Capacity factor SOL edit
        e_sol_cf = solCf
        
        lines[1290] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'day\',\'E_SOLPV\','+str(e_sol_cf)+',\'\');\n'
        lines[1292] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'day\',\'E_SOLPV\','+str(e_sol_cf)+',\'\');\n'
        lines[1294] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'day\',\'E_SOLPV\','+str(e_sol_cf)+',\'\');\n'
        lines[1296] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'day\',\'E_SOLPV\','+str(e_sol_cf)+',\'\');\n'
        lines[1298] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'day\',\'E_SOLPV\','+str(e_sol_cf)+',\'\');\n'
        lines[1300] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-wother\',\'day\',\'E_SOLPV\','+str(e_sol_cf)+',\'\');\n'
        lines[1302] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'day\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        lines[1304] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'day\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        lines[1306] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'day\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        lines[1308] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'day\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        lines[1310] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'day\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        lines[1312] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-wother\',\'day\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        lines[1313] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-wother\',\'night\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        
        
        #Capacity factor WIND edit
        e_wind_cf_7_12 = windCf1 * (9.5 * 1.609)**3 + windCf2 * (9.5 * 1.609)**2 + windCf3 * (9.5 * 1.609) + windCf4
        e_wind_cf_12_17 = windCf1 * (14.5 * 1.609)**3 + windCf2 * (14.5 * 1.609)**2 + windCf3 * (14.5 * 1.609) + windCf4
        e_wind_cf_17_24 = windCf1 * (20.5 * 1.609)**3 + windCf2 * (20.5 * 1.609)**2 + windCf3 * (20.5 * 1.609) + windCf4
        e_wind_cf_24_31 = min(windCf1 * (27.5 * 1.609)**3 + windCf2 * (27.5 * 1.609)**2 + windCf3 * (27.5 * 1.609) + windCf4, 1)
        e_wind_cf_31_38 = min(windCf1 * (34.5 * 1.609)**3 + windCf2 * (34.5 * 1.609)**2 + windCf3 * (34.5 * 1.609) + windCf4, 1)
        
        lines[1327] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'day\',\'E_WIND\','+str(e_wind_cf_7_12)+',\'\');\n'
        lines[1328] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'night\',\'E_WIND\','+str(e_wind_cf_7_12)+',\'\');\n'
        lines[1329] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'day\',\'E_WIND\','+str(e_wind_cf_12_17)+',\'\');\n'
        lines[1330] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'night\',\'E_WIND\','+str(e_wind_cf_12_17)+',\'\');\n'
        lines[1331] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'day\',\'E_WIND\','+str(e_wind_cf_17_24)+',\'\');\n'
        lines[1332] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'night\',\'E_WIND\','+str(e_wind_cf_17_24)+',\'\');\n'
        lines[1333] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'day\',\'E_WIND\','+str(e_wind_cf_24_31)+',\'\');\n'
        lines[1334] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'night\',\'E_WIND\','+str(e_wind_cf_24_31)+',\'\');\n'
        lines[1335] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'day\',\'E_WIND\','+str(e_wind_cf_31_38)+',\'\');\n'
        lines[1336] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'night\',\'E_WIND\','+str(e_wind_cf_31_38)+',\'\');\n'
        lines[1339] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'day\',\'E_WIND\','+str(e_wind_cf_7_12)+',\'\');\n'
        lines[1340] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'night\',\'E_WIND\','+str(e_wind_cf_7_12)+',\'\');\n'
        lines[1341] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'day\',\'E_WIND\','+str(e_wind_cf_12_17)+',\'\');\n'
        lines[1342] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'night\',\'E_WIND\','+str(e_wind_cf_12_17)+',\'\');\n'
        lines[1343] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'day\',\'E_WIND\','+str(e_wind_cf_17_24)+',\'\');\n'
        lines[1344] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'night\',\'E_WIND\','+str(e_wind_cf_17_24)+',\'\');\n'
        lines[1345] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'day\',\'E_WIND\','+str(e_wind_cf_24_31)+',\'\');\n'
        lines[1346] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'night\',\'E_WIND\','+str(e_wind_cf_24_31)+',\'\');\n'
        lines[1347] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'day\',\'E_WIND\','+str(e_wind_cf_31_38)+',\'\');\n'
        lines[1348] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'night\',\'E_WIND\','+str(e_wind_cf_31_38)+',\'\');\n'
        lines[1351] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w7_12\',\'day\',\'E_WIND\','+str(e_wind_cf_7_12)+',\'\');\n'
        lines[1352] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w7_12\',\'night\',\'E_WIND\','+str(e_wind_cf_7_12)+',\'\');\n'
        lines[1353] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w12_17\',\'day\',\'E_WIND\','+str(e_wind_cf_12_17)+',\'\');\n'
        lines[1354] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w12_17\',\'night\',\'E_WIND\','+str(e_wind_cf_12_17)+',\'\');\n'
        lines[1355] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w17_24\',\'day\',\'E_WIND\','+str(e_wind_cf_17_24)+',\'\');\n'
        lines[1356] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w17_24\',\'night\',\'E_WIND\','+str(e_wind_cf_17_24)+',\'\');\n'
        lines[1357] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w24_31\',\'day\',\'E_WIND\','+str(e_wind_cf_24_31)+',\'\');\n'
        lines[1358] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w24_31\',\'night\',\'E_WIND\','+str(e_wind_cf_24_31)+',\'\');\n'
        lines[1359] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w31_38\',\'day\',\'E_WIND\','+str(e_wind_cf_31_38)+',\'\');\n'
        lines[1360] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w31_38\',\'night\',\'E_WIND\','+str(e_wind_cf_31_38)+',\'\');\n'
        
        
        #Capacity factor HYDRO edit
        lines[1364] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1365] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1366] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1367] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1368] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1369] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1370] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1371] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1372] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1373] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1374] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-wother\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1375] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-wother\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        
        lines[1376] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1377] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1378] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1379] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1380] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1381] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1382] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1383] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1384] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1385] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1386] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-wother\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1387] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-wother\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
       
        lines[1388] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w7_12\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1389] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w7_12\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1390] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w12_17\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1391] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w12_17\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1392] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w17_24\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1393] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w17_24\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1394] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w24_31\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1395] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w24_31\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1396] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w31_38\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1397] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w31_38\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1398] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-wother\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1399] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-wother\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        
    with open(os.path.join(new_file_path, new_file_name), 'w') as fp:
        for L in lines:
            fp.writelines(L)
        
        fp.close()
        
    return demand2049




def write_temoa_input_file_bau(template_path, new_file_path, new_file_name, \
                        sunnyRatios, windyRatios, populationProj, perCapitaProj, ngPriceProj, urnPriceProj, coalPriceProj, dslPriceProj, oilPriceProj, \
                        e_ngVarProj, e_ngFixProj, e_ngInvProj, e_nucVarProj, e_nucFixProj, e_nucInvProj, e_coalVarProj, e_coalFixProj, e_coalInvProj,\
                        e_bioVarProj, e_bioFixProj, e_bioInvProj, e_bioMaxCap, bioPrice,\
                        e_solInvProj, e_windInvProj, e_hydInvProj, e_battInvProj, \
                        e_solFixProj, e_windFixProj, e_hydFixProj, e_battFixProj, \
                        e_hydCF, solCf, windCf1, windCf2, windCf3, windCf4):
   
    with open(template_path) as f:
        lines = f.readlines()
        f.close()
        
        #SegFracs Edit
        sunny7_12 = sunnyRatios[0] * windyRatios[0]
        sunny12_17 = sunnyRatios[0] * windyRatios[1]
        sunny17_24 = sunnyRatios[0] * windyRatios[2]
        sunny24_31 = sunnyRatios[0] * windyRatios[3]
        sunny31_38 = sunnyRatios[0] * windyRatios[4]
        sunnyOther = sunnyRatios[0] * windyRatios[5]
        
        partsunny7_12 = sunnyRatios[1] * windyRatios[0]
        partsunny12_17 = sunnyRatios[1] * windyRatios[1]
        partsunny17_24 = sunnyRatios[1] * windyRatios[2]
        partsunny24_31 = sunnyRatios[1] * windyRatios[3]
        partsunny31_38 = sunnyRatios[1] * windyRatios[4]
        partsunnyOther = sunnyRatios[1] * windyRatios[5]
        
        cloudy7_12 = sunnyRatios[2] * windyRatios[0]
        cloudy12_17 = sunnyRatios[2] * windyRatios[1]
        cloudy17_24 = sunnyRatios[2] * windyRatios[2]
        cloudy24_31 = sunnyRatios[2] * windyRatios[3]
        cloudy31_38 = sunnyRatios[2] * windyRatios[4]
        cloudyOther = sunnyRatios[2] * windyRatios[5]
        
        
        lines[225] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w7_12\',\'day\','+str(sunny7_12/2)+',\'sunny-w7_12 - Day\');\n'
        lines[226] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w7_12\',\'night\','+str(sunny7_12/2)+',\'sunny-w7_12 - Night\');\n'
        lines[227] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w12_17\',\'day\','+str(sunny12_17/2)+',\'sunny-w12_17 - Day\');\n'
        lines[228] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w12_17\',\'night\','+str(sunny12_17/2)+',\'sunny-w12_17 - Night\');\n'
        lines[229] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w17_24\',\'day\','+str(sunny17_24/2)+',\'sunny-w17_24 - Day\');\n'
        lines[230] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w17_24\',\'night\','+str(sunny17_24/2)+',\'sunny-w17_24 - Night\');\n'
        lines[231] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w24_31\',\'day\','+str(sunny24_31/2)+',\'sunny-w24_31 - Day\');\n'
        lines[232] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w24_31\',\'night\','+str(sunny24_31/2)+',\'sunny-w24_31 - Night\');\n'
        lines[233] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w31_38\',\'day\','+str(sunny31_38/2)+',\'sunny-w31_38 - Day\');\n'
        lines[234] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w31_38\',\'night\','+str(sunny31_38/2)+',\'sunny-w31_38 - Night\');\n'
        lines[235] = 'INSERT INTO `SegFrac` VALUES (\'sunny-wother\',\'day\','+str(sunnyOther/2)+',\'sunny-wother - Day\');\n'
        lines[236] = 'INSERT INTO `SegFrac` VALUES (\'sunny-wother\',\'night\','+str(sunnyOther/2)+',\'sunny-wother - Night\');\n'
        
        lines[238] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w7_12\',\'day\','+str(partsunny7_12/2)+',\'partsunny-w7_12 - Day\');\n'
        lines[239] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w7_12\',\'night\','+str(partsunny7_12/2)+',\'partsunny-w7_12 - Night\');\n'
        lines[240] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w12_17\',\'day\','+str(partsunny12_17/2)+',\'partsunny-w12_17 - Day\');\n'
        lines[241] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w12_17\',\'night\','+str(partsunny12_17/2)+',\'partsunny-w12_17 - Night\');\n'
        lines[242] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w17_24\',\'day\','+str(partsunny17_24/2)+',\'partsunny-w17_24 - Day\');\n'
        lines[243] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w17_24\',\'night\','+str(partsunny17_24/2)+',\'partsunny-w17_24 - Night\');\n'
        lines[244] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w24_31\',\'day\','+str(partsunny24_31/2)+',\'partsunny-w24_31 - Day\');\n'
        lines[245] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w24_31\',\'night\','+str(partsunny24_31/2)+',\'partsunny-w24_31 - Night\');\n'
        lines[246] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w31_38\',\'day\','+str(partsunny31_38/2)+',\'partsunny-w31_38 - Day\');\n'
        lines[247] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w31_38\',\'night\','+str(partsunny31_38/2)+',\'partsunny-w31_38 - Night\');\n'
        lines[248] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-wother\',\'day\','+str(partsunnyOther/2)+',\'partsunny-wother - Day\');\n'
        lines[249] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-wother\',\'night\','+str(partsunnyOther/2)+',\'partsunny-wother - Night\');\n'
        
        lines[251] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w7_12\',\'day\','+str(cloudy7_12/2)+',\'cloudy-w7_12 - Day\');\n'
        lines[252] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w7_12\',\'night\','+str(cloudy7_12/2)+',\'cloudy-w7_12 - Night\');\n'
        lines[253] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w12_17\',\'day\','+str(cloudy12_17/2)+',\'cloudy-w12_17 - Day\');\n'
        lines[254] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w12_17\',\'night\','+str(cloudy12_17/2)+',\'cloudy-w12_17 - Night\');\n'
        lines[255] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w17_24\',\'day\','+str(cloudy17_24/2)+',\'cloudy-w17_24 - Day\');\n'
        lines[256] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w17_24\',\'night\','+str(cloudy17_24/2)+',\'cloudy-w17_24 - Night\');\n'
        lines[257] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w24_31\',\'day\','+str(cloudy24_31/2)+',\'cloudy-w24_31 - Day\');\n'
        lines[258] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w24_31\',\'night\','+str(cloudy24_31/2)+',\'cloudy-w24_31 - Night\');\n'
        lines[259] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w31_38\',\'day\','+str(cloudy31_38/2)+',\'cloudy-w31_38 - Day\');\n'
        lines[260] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w31_38\',\'night\','+str(cloudy31_38/2)+',\'cloudy-w31_38 - Night\');\n'
        lines[261] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-wother\',\'day\','+str(cloudyOther/2)+',\'cloudy-wother - Day\');\n'
        lines[262] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-wother\',\'night\','+str(cloudyOther/2)+',\'cloudy-wother - Night\');\n'
        
        
        #Demand Specific Distribution edit
        lines[762] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w7_12\',\'day\',\'DMND\','+str(sunny7_12/2)+',\'\');\n'
        lines[763] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w7_12\',\'night\',\'DMND\','+str(sunny7_12/2)+',\'\');\n'
        lines[764] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w12_17\',\'day\',\'DMND\','+str(sunny12_17/2)+',\'\');\n'
        lines[765] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w12_17\',\'night\',\'DMND\','+str(sunny12_17/2)+',\'\');\n'
        lines[766] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w17_24\',\'day\',\'DMND\','+str(sunny17_24/2)+',\'\');\n'
        lines[767] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w17_24\',\'night\',\'DMND\','+str(sunny17_24/2)+',\'\');\n'
        lines[768] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w24_31\',\'day\',\'DMND\','+str(sunny24_31/2)+',\'\');\n'
        lines[769] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w24_31\',\'night\',\'DMND\','+str(sunny24_31/2)+',\'\');\n'
        lines[770] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w31_38\',\'day\',\'DMND\','+str(sunny31_38/2)+',\'\');\n'
        lines[771] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w31_38\',\'night\',\'DMND\','+str(sunny31_38/2)+',\'\');\n'
        lines[772] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-wother\',\'day\',\'DMND\','+str(sunnyOther/2)+',\'\');\n'
        lines[773] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-wother\',\'night\',\'DMND\','+str(sunnyOther/2)+',\'\');\n'
        
        lines[775] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w7_12\',\'day\',\'DMND\','+str(partsunny7_12/2)+',\'\');\n'
        lines[776] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w7_12\',\'night\',\'DMND\','+str(partsunny7_12/2)+',\'\');\n'
        lines[777] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w12_17\',\'day\',\'DMND\','+str(partsunny12_17/2)+',\'\');\n'
        lines[778] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w12_17\',\'night\',\'DMND\','+str(partsunny12_17/2)+',\'\');\n'
        lines[779] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w17_24\',\'day\',\'DMND\','+str(partsunny17_24/2)+',\'\');\n'
        lines[780] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w17_24\',\'night\',\'DMND\','+str(partsunny17_24/2)+',\'\');\n'
        lines[781] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w24_31\',\'day\',\'DMND\','+str(partsunny24_31/2)+',\'\');\n'
        lines[782] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w24_31\',\'night\',\'DMND\','+str(partsunny24_31/2)+',\'\');\n'
        lines[783] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w31_38\',\'day\',\'DMND\','+str(partsunny31_38/2)+',\'\');\n'
        lines[784] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w31_38\',\'night\',\'DMND\','+str(partsunny31_38/2)+',\'\');\n'
        lines[785] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-wother\',\'day\',\'DMND\','+str(partsunnyOther/2)+',\'\');\n'
        lines[786] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-wother\',\'night\',\'DMND\','+str(partsunnyOther/2)+',\'\');\n'
        
        lines[788] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w7_12\',\'day\',\'DMND\','+str(cloudy7_12/2)+',\'\');\n'
        lines[789] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w7_12\',\'night\',\'DMND\','+str(cloudy7_12/2)+',\'\');\n'
        lines[790] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w12_17\',\'day\',\'DMND\','+str(cloudy12_17/2)+',\'\');\n'
        lines[791] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w12_17\',\'night\',\'DMND\','+str(cloudy12_17/2)+',\'\');\n'
        lines[792] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w17_24\',\'day\',\'DMND\','+str(cloudy17_24/2)+',\'\');\n'
        lines[793] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w17_24\',\'night\',\'DMND\','+str(cloudy17_24/2)+',\'\');\n'
        lines[794] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w24_31\',\'day\',\'DMND\','+str(cloudy24_31/2)+',\'\');\n'
        lines[795] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w24_31\',\'night\',\'DMND\','+str(cloudy24_31/2)+',\'\');\n'
        lines[796] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w31_38\',\'day\',\'DMND\','+str(cloudy31_38/2)+',\'\');\n'
        lines[797] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w31_38\',\'night\',\'DMND\','+str(cloudy31_38/2)+',\'\');\n'
        lines[798] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-wother\',\'day\',\'DMND\','+str(cloudyOther/2)+',\'\');\n'
        lines[799] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-wother\',\'night\',\'DMND\','+str(cloudyOther/2)+',\'\');\n'
        
        
        #Demand
        demand2025 = populationProj['2025'] * perCapitaProj['2025'] / (277.78 * 10**6)
        demand2030 = populationProj['2030'] * perCapitaProj['2030'] / (277.78 * 10**6)
        demand2035 = populationProj['2035'] * perCapitaProj['2035'] / (277.78 * 10**6)
        demand2040 = populationProj['2040'] * perCapitaProj['2040'] / (277.78 * 10**6)
        demand2045 = populationProj['2045'] * perCapitaProj['2045'] / (277.78 * 10**6)
        demand2049 = populationProj['2050'] * perCapitaProj['2050'] / (277.78 * 10**6)
        
        
        lines[813] = 'INSERT INTO `Demand` VALUES (\'R1\',2025,\'DMND\','+str(demand2025)+',\'\',\'\');\n'
        lines[814] = 'INSERT INTO `Demand` VALUES (\'R1\',2030,\'DMND\','+str(demand2030)+',\'\',\'\');\n'
        lines[815] = 'INSERT INTO `Demand` VALUES (\'R1\',2035,\'DMND\','+str(demand2035)+',\'\',\'\');\n'
        lines[816] = 'INSERT INTO `Demand` VALUES (\'R1\',2040,\'DMND\','+str(demand2040)+',\'\',\'\');\n'
        lines[817] = 'INSERT INTO `Demand` VALUES (\'R1\',2045,\'DMND\','+str(demand2045)+',\'\',\'\');\n'
        lines[818] = 'INSERT INTO `Demand` VALUES (\'R1\',2049,\'DMND\','+str(demand2049)+',\'\',\'\');\n'
        
        #NG Price Edit
        ngPrice2025 = ngPriceProj['2025']
        ngPrice2030 = ngPriceProj['2030']
        ngPrice2035 = ngPriceProj['2035']
        ngPrice2040 = ngPriceProj['2040']
        ngPrice2045 = ngPriceProj['2045']
        ngPrice2049 = ngPriceProj['2050']
        
        lines[833] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPNG\',2020,'+str(ngPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[834] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPNG\',2020,'+str(ngPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[835] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPNG\',2020,'+str(ngPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[836] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2020,'+str(ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[837] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2020,'+str(ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[838] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2020,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[839] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPNG\',2025,'+str(ngPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[840] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPNG\',2025,'+str(ngPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[841] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPNG\',2025,'+str(ngPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[842] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2025,'+str(ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[843] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2025,'+str(ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[844] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2025,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[845] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPNG\',2030,'+str(ngPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[846] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPNG\',2030,'+str(ngPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[847] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2030,'+str(ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[848] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2030,'+str(ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[849] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2030,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[850] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPNG\',2035,'+str(ngPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[851] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2035,'+str(ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[852] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2035,'+str(ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[853] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2035,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[854] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2040,'+str(ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[855] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2040,'+str(ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[856] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2040,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[857] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2045,'+str(ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[858] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2045,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[859] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2049,'+str(ngPrice2049)+',\'$M/PJ\',\'\');\n'
        
        #Uranium Price Edit
        urnPrice2025 = urnPriceProj['2025']
        urnPrice2030 = urnPriceProj['2030']
        urnPrice2035 = urnPriceProj['2035']
        urnPrice2040 = urnPriceProj['2040']
        urnPrice2045 = urnPriceProj['2045']
        urnPrice2049 = urnPriceProj['2050']
        
        lines[861] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPURN\',2025,'+str(urnPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[862] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPURN\',2025,'+str(urnPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[863] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPURN\',2025,'+str(urnPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[864] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPURN\',2025,'+str(urnPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[865] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2025,'+str(urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[866] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2025,'+str(urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[867] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPURN\',2030,'+str(urnPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[868] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPURN\',2030,'+str(urnPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[869] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPURN\',2030,'+str(urnPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[870] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2030,'+str(urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[871] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2030,'+str(urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[872] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPURN\',2035,'+str(urnPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[873] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPURN\',2035,'+str(urnPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[874] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2035,'+str(urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[875] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2035,'+str(urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[876] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPURN\',2040,'+str(urnPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[877] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2040,'+str(urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[878] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2040,'+str(urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[879] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2045,'+str(urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[880] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2045,'+str(urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[881] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2049,'+str(urnPrice2049)+',\'$M/PJ\',\'\');\n'
        
        #E_NG Var Price Edit
        e_ng_var2025 = e_ngVarProj['2025']
        e_ng_var2030 = e_ngVarProj['2030']
        e_ng_var2035 = e_ngVarProj['2035']
        e_ng_var2040 = e_ngVarProj['2040']
        e_ng_var2045 = e_ngVarProj['2045']
        e_ng_var2049 = e_ngVarProj['2050']
        
        lines[883] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'E_NGCC\',2020,'+str(e_ng_var2025)+',\'$M/PJ\',\'\');\n'
        lines[884] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NGCC\',2020,'+str(e_ng_var2030)+',\'$M/PJ\',\'\');\n'
        lines[885] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NGCC\',2020,'+str(e_ng_var2035)+',\'$M/PJ\',\'\');\n'
        lines[886] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2020,'+str(e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[887] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2020,'+str(e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[888] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2020,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[889] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'E_NGCC\',2025,'+str(e_ng_var2025)+',\'$M/PJ\',\'\');\n'
        lines[890] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NGCC\',2025,'+str(e_ng_var2030)+',\'$M/PJ\',\'\');\n'
        lines[891] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NGCC\',2025,'+str(e_ng_var2035)+',\'$M/PJ\',\'\');\n'
        lines[892] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2025,'+str(e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[893] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2025,'+str(e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[894] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2025,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[895] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NGCC\',2030,'+str(e_ng_var2030)+',\'$M/PJ\',\'\');\n'
        lines[896] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NGCC\',2030,'+str(e_ng_var2035)+',\'$M/PJ\',\'\');\n'
        lines[897] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2030,'+str(e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[898] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2030,'+str(e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[899] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2030,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[900] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NGCC\',2035,'+str(e_ng_var2035)+',\'$M/PJ\',\'\');\n'
        lines[901] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2035,'+str(e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[902] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2035,'+str(e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[903] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2035,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[904] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2040,'+str(e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[905] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2040,'+str(e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[906] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2040,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[907] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2045,'+str(e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[908] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2045,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[909] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2049,'+str(e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        
        #E_NUC Var Price Edit
        e_urn_var2025 = e_nucVarProj['2025']
        e_urn_var2030 = e_nucVarProj['2030']
        e_urn_var2035 = e_nucVarProj['2035']
        e_urn_var2040 = e_nucVarProj['2040']
        e_urn_var2045 = e_nucVarProj['2045']
        e_urn_var2049 = e_nucVarProj['2050']
        
        lines[911] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'E_NUCLEAR\',2025,'+str(e_urn_var2025)+',\'$M/PJ\',\'\');\n'
        lines[912] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NUCLEAR\',2025,'+str(e_urn_var2030)+',\'$M/PJ\',\'\');\n'
        lines[913] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NUCLEAR\',2025,'+str(e_urn_var2035)+',\'$M/PJ\',\'\');\n'
        lines[914] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NUCLEAR\',2025,'+str(e_urn_var2040)+',\'$M/PJ\',\'\');\n'
        lines[915] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2025,'+str(e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[916] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2025,'+str(e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[917] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NUCLEAR\',2030,'+str(e_urn_var2030)+',\'$M/PJ\',\'\');\n'
        lines[918] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NUCLEAR\',2030,'+str(e_urn_var2035)+',\'$M/PJ\',\'\');\n'
        lines[919] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NUCLEAR\',2030,'+str(e_urn_var2040)+',\'$M/PJ\',\'\');\n'
        lines[920] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2030,'+str(e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[921] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2030,'+str(e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[922] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NUCLEAR\',2035,'+str(e_urn_var2035)+',\'$M/PJ\',\'\');\n'
        lines[923] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NUCLEAR\',2035,'+str(e_urn_var2040)+',\'$M/PJ\',\'\');\n'
        lines[924] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2035,'+str(e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[925] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2035,'+str(e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[926] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NUCLEAR\',2040,'+str(e_urn_var2040)+',\'$M/PJ\',\'\');\n'
        lines[927] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2040,'+str(e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[928] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2040,'+str(e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[929] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2045,'+str(e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[930] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2045,'+str(e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[931] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2049,'+str(e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        
        
       
        #Investment Costs Price Edit
        
        e_ng_inv2025 = e_ngInvProj['2025']
        e_ng_inv2030 = e_ngInvProj['2030']
        e_ng_inv2035 = e_ngInvProj['2035']
        e_ng_inv2040 = e_ngInvProj['2040']
        e_ng_inv2045 = e_ngInvProj['2045']
        e_ng_inv2049 = e_ngInvProj['2050']
        
        e_sol_inv2025 = e_solInvProj['2025']
        e_sol_inv2030 = e_solInvProj['2030']
        e_sol_inv2035 = e_solInvProj['2035']
        e_sol_inv2040 = e_solInvProj['2040']
        e_sol_inv2045 = e_solInvProj['2045']
        e_sol_inv2049 = e_solInvProj['2050']
        
        e_wind_inv2025 = e_windInvProj['2025']
        e_wind_inv2030 = e_windInvProj['2030']
        e_wind_inv2035 = e_windInvProj['2035']
        e_wind_inv2040 = e_windInvProj['2040']
        e_wind_inv2045 = e_windInvProj['2045']
        e_wind_inv2049 = e_windInvProj['2050']
        
        e_nuc_inv2025 = e_nucInvProj['2025']
        e_nuc_inv2030 = e_nucInvProj['2030']
        e_nuc_inv2035 = e_nucInvProj['2035']
        e_nuc_inv2040 = e_nucInvProj['2040']
        e_nuc_inv2045 = e_nucInvProj['2045']
        e_nuc_inv2049 = e_nucInvProj['2050']
        
        e_hyd_inv2025 = e_hydInvProj['2025']
        e_hyd_inv2030 = e_hydInvProj['2030']
        e_hyd_inv2035 = e_hydInvProj['2035']
        e_hyd_inv2040 = e_hydInvProj['2040']
        e_hyd_inv2045 = e_hydInvProj['2045']
        e_hyd_inv2049 = e_hydInvProj['2050']
       
        e_batt_inv2025 = e_battInvProj['2025']
        e_batt_inv2030 = e_battInvProj['2030']
        e_batt_inv2035 = e_battInvProj['2035']
        e_batt_inv2040 = e_battInvProj['2040']
        e_batt_inv2045 = e_battInvProj['2045']
        e_batt_inv2049 = e_battInvProj['2050']
        
        lines[1001] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2025,'+str(e_ng_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1002] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2025,'+str(e_sol_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1003] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2025,'+str(e_wind_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1004] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2025,'+str(e_nuc_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1005] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2025,'+str(e_hyd_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1007] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2025,'+str(e_batt_inv2025)+',\'$M/GW\',\'\');\n'
         
        lines[1013] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2030,'+str(e_ng_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1014] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2030,'+str(e_sol_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1015] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2030,'+str(e_wind_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1016] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2030,'+str(e_nuc_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1017] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2030,'+str(e_hyd_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1019] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2030,'+str(e_batt_inv2030)+',\'$M/GW\',\'\');\n'
        
        lines[1025] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2035,'+str(e_ng_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1026] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2035,'+str(e_sol_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1027] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2035,'+str(e_wind_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1028] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2035,'+str(e_nuc_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1029] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2035,'+str(e_hyd_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1031] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2035,'+str(e_batt_inv2035)+',\'$M/GW\',\'\');\n'
        
        lines[1037] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2040,'+str(e_ng_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1038] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2040,'+str(e_sol_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1039] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2040,'+str(e_wind_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1040] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2040,'+str(e_nuc_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1041] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2040,'+str(e_hyd_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1043] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2040,'+str(e_batt_inv2040)+',\'$M/GW\',\'\');\n'
        
        lines[1049] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2045,'+str(e_ng_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1050] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2045,'+str(e_sol_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1051] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2045,'+str(e_wind_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1052] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2045,'+str(e_nuc_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1053] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2045,'+str(e_hyd_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1055] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2045,'+str(e_batt_inv2045)+',\'$M/GW\',\'\');\n'
        
        lines[1061] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2049,'+str(e_ng_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1062] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2049,'+str(e_sol_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1063] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2049,'+str(e_wind_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1064] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2049,'+str(e_nuc_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1065] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2049,'+str(e_hyd_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1067] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2049,'+str(e_batt_inv2049)+',\'$M/GW\',\'\');\n'
        

        
        #E_NG Fix Price Edit
        e_ng_fix2020 = e_ngFixProj['2020']
        e_ng_fix2025 = e_ngFixProj['2025']
        e_ng_fix2030 = e_ngFixProj['2030']
        e_ng_fix2035 = e_ngFixProj['2035']
        e_ng_fix2040 = e_ngFixProj['2040']
        e_ng_fix2045 = e_ngFixProj['2045']
        e_ng_fix2049 = e_ngFixProj['2050']
        
        lines[1087] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_NGCC\',2020,'+str(e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1088] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NGCC\',2020,'+str(e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1089] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NGCC\',2020,'+str(e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1090] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2020,'+str(e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1091] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2020,'+str(e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1092] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2020,'+str(e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1093] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_NGCC\',2025,'+str(e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1094] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NGCC\',2025,'+str(e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1095] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NGCC\',2025,'+str(e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1096] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2025,'+str(e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1097] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2025,'+str(e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1098] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2025,'+str(e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1099] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NGCC\',2030,'+str(e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1100] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NGCC\',2030,'+str(e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1101] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2030,'+str(e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1102] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2030,'+str(e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1103] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2030,'+str(e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1104] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NGCC\',2035,'+str(e_ng_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1105] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2035,'+str(e_ng_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1106] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2035,'+str(e_ng_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1107] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2035,'+str(e_ng_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1108] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2040,'+str(e_ng_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1109] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2040,'+str(e_ng_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1110] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2040,'+str(e_ng_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1111] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2045,'+str(e_ng_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1112] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2045,'+str(e_ng_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1113] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2049,'+str(e_ng_fix2049)+',\'$M/GWyr\',\'\');\n'
        
        
        #E_SOL Fix Price Edit
        e_sol_fix2020 = e_solFixProj['2020']
        e_sol_fix2025 = e_solFixProj['2025']
        e_sol_fix2030 = e_solFixProj['2030']
        e_sol_fix2035 = e_solFixProj['2035']
        e_sol_fix2040 = e_solFixProj['2040']
        e_sol_fix2045 = e_solFixProj['2045']
        e_sol_fix2049 = e_solFixProj['2050']
        
        lines[1115] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_SOLPV\',2020,'+str(e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1116] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_SOLPV\',2020,'+str(e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1117] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_SOLPV\',2020,'+str(e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1118] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2020,'+str(e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1119] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2020,'+str(e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1120] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2020,'+str(e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1121] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_SOLPV\',2025,'+str(e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1122] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_SOLPV\',2025,'+str(e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1123] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_SOLPV\',2025,'+str(e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1124] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2025,'+str(e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1125] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2025,'+str(e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1126] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2025,'+str(e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1127] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_SOLPV\',2030,'+str(e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1128] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_SOLPV\',2030,'+str(e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1129] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2030,'+str(e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1130] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2030,'+str(e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1131] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2030,'+str(e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1132] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_SOLPV\',2035,'+str(e_sol_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1133] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2035,'+str(e_sol_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1134] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2035,'+str(e_sol_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1135] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2035,'+str(e_sol_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1136] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2040,'+str(e_sol_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1137] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2040,'+str(e_sol_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1138] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2040,'+str(e_sol_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1139] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2045,'+str(e_sol_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1140] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2045,'+str(e_sol_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1141] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2049,'+str(e_sol_fix2049)+',\'$M/GWyr\',\'\');\n'
        
        #E_WIND Fix Price Edit
        e_wind_fix2020 = e_windFixProj['2020']
        e_wind_fix2025 = e_windFixProj['2025']
        e_wind_fix2030 = e_windFixProj['2030']
        e_wind_fix2035 = e_windFixProj['2035']
        e_wind_fix2040 = e_windFixProj['2040']
        e_wind_fix2045 = e_windFixProj['2045']
        e_wind_fix2049 = e_windFixProj['2050']
        
        lines[1143] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_WIND\',2020,'+str(e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1144] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_WIND\',2020,'+str(e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1145] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_WIND\',2020,'+str(e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1146] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2020,'+str(e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1147] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2020,'+str(e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1148] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2020,'+str(e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1149] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_WIND\',2025,'+str(e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1150] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_WIND\',2025,'+str(e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1151] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_WIND\',2025,'+str(e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1152] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2025,'+str(e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1153] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2025,'+str(e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1154] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2025,'+str(e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1155] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_WIND\',2030,'+str(e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1156] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_WIND\',2030,'+str(e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1157] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2030,'+str(e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1158] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2030,'+str(e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1159] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2030,'+str(e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1160] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_WIND\',2035,'+str(e_wind_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1161] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2035,'+str(e_wind_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1162] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2035,'+str(e_wind_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1163] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2035,'+str(e_wind_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1164] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2040,'+str(e_wind_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1165] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2040,'+str(e_wind_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1166] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2040,'+str(e_wind_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1167] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2045,'+str(e_wind_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1168] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2045,'+str(e_wind_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1169] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2049,'+str(e_wind_fix2049)+',\'$M/GWyr\',\'\');\n'
        
        
        #E_HYDRO Fix Price Edit
        e_hyd_fix2025 = e_hydFixProj['2025']
        e_hyd_fix2030 = e_hydFixProj['2030']
        e_hyd_fix2035 = e_hydFixProj['2035']
        e_hyd_fix2040 = e_hydFixProj['2040']
        e_hyd_fix2045 = e_hydFixProj['2045']
        e_hyd_fix2049 = e_hydFixProj['2050']
        
        lines[1171] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_HYDRO\',2025,'+str(e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1172] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_HYDRO\',2025,'+str(e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1173] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_HYDRO\',2025,'+str(e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1174] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_HYDRO\',2025,'+str(e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1175] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2025,'+str(e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1176] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2025,'+str(e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1177] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_HYDRO\',2030,'+str(e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1178] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_HYDRO\',2030,'+str(e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1179] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_HYDRO\',2030,'+str(e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1180] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2030,'+str(e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1181] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2030,'+str(e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1182] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_HYDRO\',2035,'+str(e_hyd_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1183] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_HYDRO\',2035,'+str(e_hyd_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1184] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2035,'+str(e_hyd_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1185] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2035,'+str(e_hyd_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1186] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_HYDRO\',2040,'+str(e_hyd_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1187] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2040,'+str(e_hyd_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1188] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2040,'+str(e_hyd_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1189] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2045,'+str(e_hyd_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1190] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2045,'+str(e_hyd_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1191] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2049,'+str(e_hyd_fix2049)+',\'$M/GWyr\',\'\');\n'
        
       
        #E_NUCLEAR Fix Price Edit
        e_nuc_fix2025 = e_nucFixProj['2025']
        e_nuc_fix2030 = e_nucFixProj['2030']
        e_nuc_fix2035 = e_nucFixProj['2035']
        e_nuc_fix2040 = e_nucFixProj['2040']
        e_nuc_fix2045 = e_nucFixProj['2045']
        e_nuc_fix2049 = e_nucFixProj['2050']
        
        lines[1215] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_NUCLEAR\',2025,'+str(e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1216] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NUCLEAR\',2025,'+str(e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1217] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NUCLEAR\',2025,'+str(e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1218] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NUCLEAR\',2025,'+str(e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1219] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2025,'+str(e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1220] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2025,'+str(e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1221] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NUCLEAR\',2030,'+str(e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1222] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NUCLEAR\',2030,'+str(e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1223] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NUCLEAR\',2030,'+str(e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1224] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2030,'+str(e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1225] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2030,'+str(e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1226] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NUCLEAR\',2035,'+str(e_nuc_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1227] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NUCLEAR\',2035,'+str(e_nuc_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1228] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2035,'+str(e_nuc_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1229] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2035,'+str(e_nuc_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1230] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NUCLEAR\',2040,'+str(e_nuc_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1231] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2040,'+str(e_nuc_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1232] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2040,'+str(e_nuc_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1233] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2045,'+str(e_nuc_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1234] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2045,'+str(e_nuc_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1235] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2049,'+str(e_nuc_fix2049)+',\'$M/GWyr\',\'\');\n'
        
        
        #E_BATT Fix Price Edit
        e_batt_fix2025 = e_battFixProj['2025']
        e_batt_fix2030 = e_battFixProj['2030']
        e_batt_fix2035 = e_battFixProj['2035']
        e_batt_fix2040 = e_battFixProj['2040']
        e_batt_fix2045 = e_battFixProj['2045']
        e_batt_fix2049 = e_battFixProj['2050']
        
        lines[1237] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_BATT\',2025,'+str(e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1238] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_BATT\',2025,'+str(e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1239] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BATT\',2025,'+str(e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1240] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BATT\',2025,'+str(e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1241] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2025,'+str(e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1242] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2025,'+str(e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1243] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_BATT\',2030,'+str(e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1244] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BATT\',2030,'+str(e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1245] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BATT\',2030,'+str(e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1246] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2030,'+str(e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1247] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2030,'+str(e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1248] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BATT\',2035,'+str(e_batt_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1249] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BATT\',2035,'+str(e_batt_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1250] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2035,'+str(e_batt_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1251] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2035,'+str(e_batt_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1252] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BATT\',2040,'+str(e_batt_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1253] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2040,'+str(e_batt_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1254] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2040,'+str(e_batt_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1255] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2045,'+str(e_batt_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1256] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2045,'+str(e_batt_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1257] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2049,'+str(e_batt_fix2049)+',\'$M/GWyr\',\'\');\n'
        
        
        #Capacity factor SOL edit
        e_sol_cf = solCf
        
        lines[1290] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'day\',\'E_SOLPV\','+str(e_sol_cf)+',\'\');\n'
        lines[1292] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'day\',\'E_SOLPV\','+str(e_sol_cf)+',\'\');\n'
        lines[1294] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'day\',\'E_SOLPV\','+str(e_sol_cf)+',\'\');\n'
        lines[1296] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'day\',\'E_SOLPV\','+str(e_sol_cf)+',\'\');\n'
        lines[1298] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'day\',\'E_SOLPV\','+str(e_sol_cf)+',\'\');\n'
        lines[1300] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-wother\',\'day\',\'E_SOLPV\','+str(e_sol_cf)+',\'\');\n'
        lines[1302] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'day\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        lines[1304] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'day\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        lines[1306] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'day\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        lines[1308] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'day\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        lines[1310] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'day\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        lines[1312] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-wother\',\'day\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        lines[1313] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-wother\',\'night\',\'E_SOLPV\','+str(0.7 * e_sol_cf)+',\'\');\n'
        
        
        #Capacity factor WIND edit
        e_wind_cf_7_12 = windCf1 * (9.5 * 1.609)**3 + windCf2 * (9.5 * 1.609)**2 + windCf3 * (9.5 * 1.609) + windCf4
        e_wind_cf_12_17 = windCf1 * (14.5 * 1.609)**3 + windCf2 * (14.5 * 1.609)**2 + windCf3 * (14.5 * 1.609) + windCf4
        e_wind_cf_17_24 = windCf1 * (20.5 * 1.609)**3 + windCf2 * (20.5 * 1.609)**2 + windCf3 * (20.5 * 1.609) + windCf4
        e_wind_cf_24_31 = min(windCf1 * (27.5 * 1.609)**3 + windCf2 * (27.5 * 1.609)**2 + windCf3 * (27.5 * 1.609) + windCf4, 1)
        e_wind_cf_31_38 = min(windCf1 * (34.5 * 1.609)**3 + windCf2 * (34.5 * 1.609)**2 + windCf3 * (34.5 * 1.609) + windCf4, 1)
        
        lines[1327] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'day\',\'E_WIND\','+str(e_wind_cf_7_12)+',\'\');\n'
        lines[1328] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'night\',\'E_WIND\','+str(e_wind_cf_7_12)+',\'\');\n'
        lines[1329] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'day\',\'E_WIND\','+str(e_wind_cf_12_17)+',\'\');\n'
        lines[1330] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'night\',\'E_WIND\','+str(e_wind_cf_12_17)+',\'\');\n'
        lines[1331] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'day\',\'E_WIND\','+str(e_wind_cf_17_24)+',\'\');\n'
        lines[1332] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'night\',\'E_WIND\','+str(e_wind_cf_17_24)+',\'\');\n'
        lines[1333] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'day\',\'E_WIND\','+str(e_wind_cf_24_31)+',\'\');\n'
        lines[1334] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'night\',\'E_WIND\','+str(e_wind_cf_24_31)+',\'\');\n'
        lines[1335] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'day\',\'E_WIND\','+str(e_wind_cf_31_38)+',\'\');\n'
        lines[1336] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'night\',\'E_WIND\','+str(e_wind_cf_31_38)+',\'\');\n'
        lines[1339] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'day\',\'E_WIND\','+str(e_wind_cf_7_12)+',\'\');\n'
        lines[1340] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'night\',\'E_WIND\','+str(e_wind_cf_7_12)+',\'\');\n'
        lines[1341] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'day\',\'E_WIND\','+str(e_wind_cf_12_17)+',\'\');\n'
        lines[1342] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'night\',\'E_WIND\','+str(e_wind_cf_12_17)+',\'\');\n'
        lines[1343] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'day\',\'E_WIND\','+str(e_wind_cf_17_24)+',\'\');\n'
        lines[1344] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'night\',\'E_WIND\','+str(e_wind_cf_17_24)+',\'\');\n'
        lines[1345] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'day\',\'E_WIND\','+str(e_wind_cf_24_31)+',\'\');\n'
        lines[1346] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'night\',\'E_WIND\','+str(e_wind_cf_24_31)+',\'\');\n'
        lines[1347] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'day\',\'E_WIND\','+str(e_wind_cf_31_38)+',\'\');\n'
        lines[1348] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'night\',\'E_WIND\','+str(e_wind_cf_31_38)+',\'\');\n'
        lines[1351] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w7_12\',\'day\',\'E_WIND\','+str(e_wind_cf_7_12)+',\'\');\n'
        lines[1352] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w7_12\',\'night\',\'E_WIND\','+str(e_wind_cf_7_12)+',\'\');\n'
        lines[1353] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w12_17\',\'day\',\'E_WIND\','+str(e_wind_cf_12_17)+',\'\');\n'
        lines[1354] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w12_17\',\'night\',\'E_WIND\','+str(e_wind_cf_12_17)+',\'\');\n'
        lines[1355] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w17_24\',\'day\',\'E_WIND\','+str(e_wind_cf_17_24)+',\'\');\n'
        lines[1356] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w17_24\',\'night\',\'E_WIND\','+str(e_wind_cf_17_24)+',\'\');\n'
        lines[1357] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w24_31\',\'day\',\'E_WIND\','+str(e_wind_cf_24_31)+',\'\');\n'
        lines[1358] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w24_31\',\'night\',\'E_WIND\','+str(e_wind_cf_24_31)+',\'\');\n'
        lines[1359] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w31_38\',\'day\',\'E_WIND\','+str(e_wind_cf_31_38)+',\'\');\n'
        lines[1360] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w31_38\',\'night\',\'E_WIND\','+str(e_wind_cf_31_38)+',\'\');\n'
        
        
        #Capacity factor HYDRO edit
        lines[1364] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1365] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1366] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1367] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1368] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1369] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1370] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1371] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1372] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1373] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1374] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-wother\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1375] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-wother\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        
        lines[1376] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1377] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1378] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1379] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1380] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1381] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1382] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1383] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1384] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1385] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1386] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-wother\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1387] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-wother\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
       
        lines[1388] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w7_12\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1389] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w7_12\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1390] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w12_17\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1391] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w12_17\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1392] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w17_24\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1393] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w17_24\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1394] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w24_31\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1395] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w24_31\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1396] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w31_38\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1397] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w31_38\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1398] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-wother\',\'day\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        lines[1399] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-wother\',\'night\',\'E_HYDRO\','+str(e_hydCF)+',\'\');\n'
        
        
        #E_BIO Var Price Edit
        e_bio_var2025 = e_bioVarProj['2025']
        e_bio_var2030 = e_bioVarProj['2030']
        e_bio_var2035 = e_bioVarProj['2035']
        e_bio_var2040 = e_bioVarProj['2040']
        e_bio_var2045 = e_bioVarProj['2045']
        e_bio_var2049 = e_bioVarProj['2050']
        
        lines[1604] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'E_BIO\',2025,'+str(e_bio_var2025)+',\'$M/PJ\',\'\');\n'
        lines[1605] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_BIO\',2025,'+str(e_bio_var2030)+',\'$M/PJ\',\'\');\n'
        lines[1606] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_BIO\',2025,'+str(e_bio_var2035)+',\'$M/PJ\',\'\');\n'
        lines[1607] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_BIO\',2025,'+str(e_bio_var2040)+',\'$M/PJ\',\'\');\n'
        lines[1608] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_BIO\',2025,'+str(e_bio_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1609] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_BIO\',2025,'+str(e_bio_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1610] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_BIO\',2030,'+str(e_bio_var2030)+',\'$M/PJ\',\'\');\n'
        lines[1611] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_BIO\',2030,'+str(e_bio_var2035)+',\'$M/PJ\',\'\');\n'
        lines[1612] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_BIO\',2030,'+str(e_bio_var2040)+',\'$M/PJ\',\'\');\n'
        lines[1613] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_BIO\',2030,'+str(e_bio_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1614] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_BIO\',2030,'+str(e_bio_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1615] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_BIO\',2035,'+str(e_bio_var2035)+',\'$M/PJ\',\'\');\n'
        lines[1616] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_BIO\',2035,'+str(e_bio_var2040)+',\'$M/PJ\',\'\');\n'
        lines[1617] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_BIO\',2035,'+str(e_bio_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1618] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_BIO\',2035,'+str(e_bio_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1619] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_BIO\',2040,'+str(e_bio_var2040)+',\'$M/PJ\',\'\');\n'
        lines[1620] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_BIO\',2040,'+str(e_bio_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1621] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_BIO\',2040,'+str(e_bio_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1622] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_BIO\',2045,'+str(e_bio_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1623] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_BIO\',2045,'+str(e_bio_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1624] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_BIO\',2049,'+str(e_bio_var2049)+',\'$M/PJ\',\'\');\n'
        
        #E_BIO Cap Price Edit
        e_bio_inv2025 = e_bioInvProj['2025']
        e_bio_inv2030 = e_bioInvProj['2030']
        e_bio_inv2035 = e_bioInvProj['2035']
        e_bio_inv2040 = e_bioInvProj['2040']
        e_bio_inv2045 = e_bioInvProj['2045']
        e_bio_inv2049 = e_bioInvProj['2050']
        lines[1625] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BIO\',2025,'+str(e_bio_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1626] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BIO\',2030,'+str(e_bio_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1627] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BIO\',2035,'+str(e_bio_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1628] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BIO\',2040,'+str(e_bio_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1629] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BIO\',2045,'+str(e_bio_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1630] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BIO\',2049,'+str(e_bio_inv2049)+',\'$M/GW\',\'\');\n'
        
        #E_BIO Fix Price Edit
        e_bio_fix2025 = e_bioFixProj['2025']
        e_bio_fix2030 = e_bioFixProj['2030']
        e_bio_fix2035 = e_bioFixProj['2035']
        e_bio_fix2040 = e_bioFixProj['2040']
        e_bio_fix2045 = e_bioFixProj['2045']
        e_bio_fix2049 = e_bioFixProj['2050']
        
        lines[1631] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_BIO\',2025,'+str(e_bio_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1632] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_BIO\',2025,'+str(e_bio_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1633] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BIO\',2025,'+str(e_bio_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1634] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BIO\',2025,'+str(e_bio_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1635] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BIO\',2025,'+str(e_bio_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1636] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BIO\',2025,'+str(e_bio_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1637] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_BIO\',2030,'+str(e_bio_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1638] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BIO\',2030,'+str(e_bio_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1639] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BIO\',2030,'+str(e_bio_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1640] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BIO\',2030,'+str(e_bio_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1641] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BIO\',2030,'+str(e_bio_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1642] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BIO\',2035,'+str(e_bio_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1643] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BIO\',2035,'+str(e_bio_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1644] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BIO\',2035,'+str(e_bio_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1645] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BIO\',2035,'+str(e_bio_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1646] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BIO\',2040,'+str(e_bio_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1647] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BIO\',2040,'+str(e_bio_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1648] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BIO\',2040,'+str(e_bio_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1649] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BIO\',2045,'+str(e_bio_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1650] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BIO\',2045,'+str(e_bio_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1651] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BIO\',2049,'+str(e_bio_fix2049)+',\'$M/GWyr\',\'\');\n'
        
        
        #E_BIO Max Capacity Edit
        lines[1722] = 'INSERT INTO `MaxCapacity` VALUES (\'R1\',\'2025\',\'E_BIO\','+str(e_bioMaxCap)+',\'GW\',\'\');\n'
        lines[1723] = 'INSERT INTO `MaxCapacity` VALUES (\'R1\',\'2030\',\'E_BIO\','+str(e_bioMaxCap)+',\'GW\',\'\');\n'
        lines[1724] = 'INSERT INTO `MaxCapacity` VALUES (\'R1\',\'2035\',\'E_BIO\','+str(e_bioMaxCap)+',\'GW\',\'\');\n'
        lines[1725] = 'INSERT INTO `MaxCapacity` VALUES (\'R1\',\'2040\',\'E_BIO\','+str(e_bioMaxCap)+',\'GW\',\'\');\n'
        lines[1726] = 'INSERT INTO `MaxCapacity` VALUES (\'R1\',\'2045\',\'E_BIO\','+str(e_bioMaxCap)+',\'GW\',\'\');\n'
        lines[1727] = 'INSERT INTO `MaxCapacity` VALUES (\'R1\',\'2049\',\'E_BIO\','+str(e_bioMaxCap)+',\'GW\',\'\');\n'
        
        
        #Coal Price Edit
        coalPrice2025 = coalPriceProj['2025']
        coalPrice2030 = coalPriceProj['2030']
        coalPrice2035 = coalPriceProj['2035']
        coalPrice2040 = coalPriceProj['2040']
        coalPrice2045 = coalPriceProj['2045']
        coalPrice2049 = coalPriceProj['2050']
        
        lines[1826] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPCOAL\',2020,'+str(coalPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[1827] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPCOAL\',2020,'+str(coalPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[1828] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPCOAL\',2020,'+str(coalPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[1829] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPCOAL\',2020,'+str(coalPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1830] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPCOAL\',2020,'+str(coalPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1831] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPCOAL\',2020,'+str(coalPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1832] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPCOAL\',2025,'+str(coalPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[1833] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPCOAL\',2025,'+str(coalPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[1834] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPCOAL\',2025,'+str(coalPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[1835] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPCOAL\',2025,'+str(coalPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1836] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPCOAL\',2025,'+str(coalPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1837] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPCOAL\',2025,'+str(coalPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1838] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPCOAL\',2030,'+str(coalPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[1839] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPCOAL\',2030,'+str(coalPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[1840] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPCOAL\',2030,'+str(coalPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1841] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPCOAL\',2030,'+str(coalPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1842] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPCOAL\',2030,'+str(coalPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1843] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPCOAL\',2035,'+str(coalPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[1844] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPCOAL\',2035,'+str(coalPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1845] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPCOAL\',2035,'+str(coalPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1846] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPCOAL\',2035,'+str(coalPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1847] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPCOAL\',2040,'+str(coalPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1848] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPCOAL\',2040,'+str(coalPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1849] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPCOAL\',2040,'+str(coalPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1850] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPCOAL\',2045,'+str(coalPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1851] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPCOAL\',2045,'+str(coalPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1852] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPCOAL\',2049,'+str(coalPrice2049)+',\'$M/PJ\',\'\');\n'
        
        
        #Diesel Price Edit
        dslPrice2025 = dslPriceProj['2025']
        dslPrice2030 = dslPriceProj['2030']
        dslPrice2035 = dslPriceProj['2035']
        dslPrice2040 = dslPriceProj['2040']
        dslPrice2045 = dslPriceProj['2045']
        dslPrice2049 = dslPriceProj['2050']
        
        lines[1854] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPDSL\',2020,'+str(dslPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[1855] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPDSL\',2020,'+str(dslPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[1856] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPDSL\',2020,'+str(dslPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[1857] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPDSL\',2020,'+str(dslPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1858] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPDSL\',2020,'+str(dslPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1859] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPDSL\',2020,'+str(dslPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1860] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPDSL\',2025,'+str(dslPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[1861] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPDSL\',2025,'+str(dslPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[1862] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPDSL\',2025,'+str(dslPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[1863] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPDSL\',2025,'+str(dslPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1864] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPDSL\',2025,'+str(dslPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1865] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPDSL\',2025,'+str(dslPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1866] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPDSL\',2030,'+str(dslPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[1867] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPDSL\',2030,'+str(dslPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[1868] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPDSL\',2030,'+str(dslPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1869] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPDSL\',2030,'+str(dslPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1870] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPDSL\',2030,'+str(dslPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1871] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPDSL\',2035,'+str(dslPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[1872] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPDSL\',2035,'+str(dslPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1873] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPDSL\',2035,'+str(dslPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1874] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPDSL\',2035,'+str(dslPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1875] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPDSL\',2040,'+str(dslPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1876] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPDSL\',2040,'+str(dslPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1877] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPDSL\',2040,'+str(dslPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1878] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPDSL\',2045,'+str(dslPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1879] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPDSL\',2045,'+str(dslPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1880] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPDSL\',2049,'+str(dslPrice2049)+',\'$M/PJ\',\'\');\n'
        
        
        #Oil Price Edit
        oilPrice2025 = oilPriceProj['2025']
        oilPrice2030 = oilPriceProj['2030']
        oilPrice2035 = oilPriceProj['2035']
        oilPrice2040 = oilPriceProj['2040']
        oilPrice2045 = oilPriceProj['2045']
        oilPrice2049 = oilPriceProj['2050']
        
        lines[1882] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPOIL\',2020,'+str(oilPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[1883] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPOIL\',2020,'+str(oilPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[1884] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPOIL\',2020,'+str(oilPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[1885] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPOIL\',2020,'+str(oilPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1886] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPOIL\',2020,'+str(oilPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1887] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPOIL\',2020,'+str(oilPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1888] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPOIL\',2025,'+str(oilPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[1889] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPOIL\',2025,'+str(oilPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[1890] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPOIL\',2025,'+str(oilPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[1891] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPOIL\',2025,'+str(oilPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1892] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPOIL\',2025,'+str(oilPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1893] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPOIL\',2025,'+str(oilPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1894] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPOIL\',2030,'+str(oilPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[1895] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPOIL\',2030,'+str(oilPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[1896] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPOIL\',2030,'+str(oilPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1897] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPOIL\',2030,'+str(oilPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1898] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPOIL\',2030,'+str(oilPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1899] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPOIL\',2035,'+str(oilPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[1900] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPOIL\',2035,'+str(oilPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1901] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPOIL\',2035,'+str(oilPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1902] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPOIL\',2035,'+str(oilPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1903] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPOIL\',2040,'+str(oilPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[1904] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPOIL\',2040,'+str(oilPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1905] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPOIL\',2040,'+str(oilPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1906] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPOIL\',2045,'+str(oilPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[1907] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPOIL\',2045,'+str(oilPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[1908] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPOIL\',2049,'+str(oilPrice2049)+',\'$M/PJ\',\'\');\n'
        
        #E_COAL Price Edit
        e_coal_var2025 = e_coalVarProj['2025']
        e_coal_var2030 = e_coalVarProj['2030']
        e_coal_var2035 = e_coalVarProj['2035']
        e_coal_var2040 = e_coalVarProj['2040']
        e_coal_var2045 = e_coalVarProj['2045']
        e_coal_var2049 = e_coalVarProj['2050']
        
        lines[1910] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'E_COAL\',2020,'+str(e_coal_var2025)+',\'$M/PJ\',\'\');\n'
        lines[1911] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_COAL\',2020,'+str(e_coal_var2030)+',\'$M/PJ\',\'\');\n'
        lines[1912] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_COAL\',2020,'+str(e_coal_var2035)+',\'$M/PJ\',\'\');\n'
        lines[1913] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_COAL\',2020,'+str(e_coal_var2040)+',\'$M/PJ\',\'\');\n'
        lines[1914] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_COAL\',2020,'+str(e_coal_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1915] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_COAL\',2020,'+str(e_coal_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1916] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'E_COAL\',2025,'+str(e_coal_var2025)+',\'$M/PJ\',\'\');\n'
        lines[1917] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_COAL\',2025,'+str(e_coal_var2030)+',\'$M/PJ\',\'\');\n'
        lines[1918] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_COAL\',2025,'+str(e_coal_var2035)+',\'$M/PJ\',\'\');\n'
        lines[1919] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_COAL\',2025,'+str(e_coal_var2040)+',\'$M/PJ\',\'\');\n'
        lines[1920] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_COAL\',2025,'+str(e_coal_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1921] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_COAL\',2025,'+str(e_coal_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1922] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_COAL\',2030,'+str(e_coal_var2030)+',\'$M/PJ\',\'\');\n'
        lines[1923] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_COAL\',2030,'+str(e_coal_var2035)+',\'$M/PJ\',\'\');\n'
        lines[1924] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_COAL\',2030,'+str(e_coal_var2040)+',\'$M/PJ\',\'\');\n'
        lines[1925] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_COAL\',2030,'+str(e_coal_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1926] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_COAL\',2030,'+str(e_coal_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1927] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_COAL\',2035,'+str(e_coal_var2035)+',\'$M/PJ\',\'\');\n'
        lines[1928] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_COAL\',2035,'+str(e_coal_var2040)+',\'$M/PJ\',\'\');\n'
        lines[1929] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_COAL\',2035,'+str(e_coal_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1930] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_COAL\',2035,'+str(e_coal_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1931] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_COAL\',2040,'+str(e_coal_var2040)+',\'$M/PJ\',\'\');\n'
        lines[1932] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_COAL\',2040,'+str(e_coal_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1933] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_COAL\',2040,'+str(e_coal_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1934] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_COAL\',2045,'+str(e_coal_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1935] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_COAL\',2045,'+str(e_coal_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1936] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_COAL\',2049,'+str(e_coal_var2049)+',\'$M/PJ\',\'\');\n'
        
        
        #E_COAL Inv Price Edit
        e_coal_inv2025 = e_coalInvProj['2025']
        e_coal_inv2030 = e_coalInvProj['2030']
        e_coal_inv2035 = e_coalInvProj['2035']
        e_coal_inv2040 = e_coalInvProj['2040']
        e_coal_inv2045 = e_coalInvProj['2045']
        e_coal_inv2049 = e_coalInvProj['2050']
        lines[1994] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_COAL\',2025,'+str(e_coal_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1995] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_COAL\',2030,'+str(e_coal_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1996] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_COAL\',2035,'+str(e_coal_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1997] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_COAL\',2040,'+str(e_coal_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1998] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_COAL\',2045,'+str(e_coal_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1999] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_COAL\',2049,'+str(e_coal_inv2049)+',\'$M/GW\',\'\');\n'
        
        
        #E_COAL Fix Price Edit
        e_coal_fix2020 = e_coalFixProj['2020']
        e_coal_fix2025 = e_coalFixProj['2025']
        e_coal_fix2030 = e_coalFixProj['2030']
        e_coal_fix2035 = e_coalFixProj['2035']
        e_coal_fix2040 = e_coalFixProj['2040']
        e_coal_fix2045 = e_coalFixProj['2045']
        e_coal_fix2049 = e_coalFixProj['2050']
        
        lines[2015] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_COAL\',2020,'+str(e_coal_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[2016] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_COAL\',2020,'+str(e_coal_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[2017] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_COAL\',2020,'+str(e_coal_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[2018] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_COAL\',2020,'+str(e_coal_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[2019] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_COAL\',2020,'+str(e_coal_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[2020] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_COAL\',2020,'+str(e_coal_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[2021] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_COAL\',2025,'+str(e_coal_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[2022] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_COAL\',2025,'+str(e_coal_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[2023] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_COAL\',2025,'+str(e_coal_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[2024] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_COAL\',2025,'+str(e_coal_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[2025] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_COAL\',2025,'+str(e_coal_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[2026] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_COAL\',2025,'+str(e_coal_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[2027] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_COAL\',2030,'+str(e_coal_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[2028] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_COAL\',2030,'+str(e_coal_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[2029] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_COAL\',2030,'+str(e_coal_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[2030] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_COAL\',2030,'+str(e_coal_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[2031] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_COAL\',2030,'+str(e_coal_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[2032] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_COAL\',2035,'+str(e_coal_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[2033] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_COAL\',2035,'+str(e_coal_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[2034] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_COAL\',2035,'+str(e_coal_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[2035] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_COAL\',2035,'+str(e_coal_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[2036] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_COAL\',2040,'+str(e_coal_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[2037] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_COAL\',2040,'+str(e_coal_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[2038] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_COAL\',2040,'+str(e_coal_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[2039] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_COAL\',2045,'+str(e_coal_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[2040] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_COAL\',2045,'+str(e_coal_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[2041] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_COAL\',2049,'+str(e_coal_fix2049)+',\'$M/GWyr\',\'\');\n'
        
        
        # IMPBIO Price Edit
        lines[2253] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPBIO\',2025,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2254] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPBIO\',2025,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2255] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPBIO\',2025,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2256] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPBIO\',2025,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2257] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPBIO\',2025,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2258] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPBIO\',2025,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2259] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPBIO\',2030,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2260] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPBIO\',2030,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2261] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPBIO\',2030,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2262] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPBIO\',2030,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2263] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPBIO\',2030,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2264] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPBIO\',2035,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2265] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPBIO\',2035,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2266] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPBIO\',2035,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2267] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPBIO\',2035,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2268] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPBIO\',2040,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2269] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPBIO\',2040,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2270] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPBIO\',2040,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2271] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPBIO\',2045,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2272] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPBIO\',2045,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[2273] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPBIO\',2049,' + str(bioPrice)+',\'$M/PJ\',\'\');\n'
         
        
    with open(os.path.join(new_file_path, new_file_name), 'w') as fp:
        for L in lines:
            fp.writelines(L)
        
        fp.close()
        
    return demand2049


def write_temoa_input_file_fr(template_path, new_file_path, new_file_name,
                        sunnyRatios, windyRatios, populationProj, perCapitaProj, ngPriceProj, urnPriceProj,
                        e_ngVarProj, e_ngFixProj, e_ngInvProj, e_nucVarProj, e_nucFixProj, e_nucInvProj,
                        e_bioVarProj, e_bioFixProj, e_bioInvProj, e_bioMaxCap, bioPrice,
                        e_solInvProj, e_windInvProj, e_hydInvProj, e_battInvProj,
                        e_solFixProj, e_windFixProj, e_hydFixProj, e_battFixProj,
                        e_hydCF, solCf, windCf1, windCf2, windCf3, windCf4):

    with open(template_path) as f:
        lines = f.readlines()
        f.close()

        # SegFracs Edit
        sunny7_12 = sunnyRatios[0] * windyRatios[0]
        sunny12_17 = sunnyRatios[0] * windyRatios[1]
        sunny17_24 = sunnyRatios[0] * windyRatios[2]
        sunny24_31 = sunnyRatios[0] * windyRatios[3]
        sunny31_38 = sunnyRatios[0] * windyRatios[4]
        sunnyOther = sunnyRatios[0] * windyRatios[5]

        partsunny7_12 = sunnyRatios[1] * windyRatios[0]
        partsunny12_17 = sunnyRatios[1] * windyRatios[1]
        partsunny17_24 = sunnyRatios[1] * windyRatios[2]
        partsunny24_31 = sunnyRatios[1] * windyRatios[3]
        partsunny31_38 = sunnyRatios[1] * windyRatios[4]
        partsunnyOther = sunnyRatios[1] * windyRatios[5]

        cloudy7_12 = sunnyRatios[2] * windyRatios[0]
        cloudy12_17 = sunnyRatios[2] * windyRatios[1]
        cloudy17_24 = sunnyRatios[2] * windyRatios[2]
        cloudy24_31 = sunnyRatios[2] * windyRatios[3]
        cloudy31_38 = sunnyRatios[2] * windyRatios[4]
        cloudyOther = sunnyRatios[2] * windyRatios[5]

        lines[225] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w7_12\',\'day\','+str(
            sunny7_12/2)+',\'sunny-w7_12 - Day\');\n'
        lines[226] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w7_12\',\'night\','+str(
            sunny7_12/2)+',\'sunny-w7_12 - Night\');\n'
        lines[227] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w12_17\',\'day\','+str(
            sunny12_17/2)+',\'sunny-w12_17 - Day\');\n'
        lines[228] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w12_17\',\'night\','+str(
            sunny12_17/2)+',\'sunny-w12_17 - Night\');\n'
        lines[229] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w17_24\',\'day\','+str(
            sunny17_24/2)+',\'sunny-w17_24 - Day\');\n'
        lines[230] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w17_24\',\'night\','+str(
            sunny17_24/2)+',\'sunny-w17_24 - Night\');\n'
        lines[231] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w24_31\',\'day\','+str(
            sunny24_31/2)+',\'sunny-w24_31 - Day\');\n'
        lines[232] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w24_31\',\'night\','+str(
            sunny24_31/2)+',\'sunny-w24_31 - Night\');\n'
        lines[233] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w31_38\',\'day\','+str(
            sunny31_38/2)+',\'sunny-w31_38 - Day\');\n'
        lines[234] = 'INSERT INTO `SegFrac` VALUES (\'sunny-w31_38\',\'night\','+str(
            sunny31_38/2)+',\'sunny-w31_38 - Night\');\n'
        lines[235] = 'INSERT INTO `SegFrac` VALUES (\'sunny-wother\',\'day\','+str(
            sunnyOther/2)+',\'sunny-wother - Day\');\n'
        lines[236] = 'INSERT INTO `SegFrac` VALUES (\'sunny-wother\',\'night\','+str(
            sunnyOther/2)+',\'sunny-wother - Night\');\n'

        lines[238] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w7_12\',\'day\','+str(
            partsunny7_12/2)+',\'partsunny-w7_12 - Day\');\n'
        lines[239] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w7_12\',\'night\','+str(
            partsunny7_12/2)+',\'partsunny-w7_12 - Night\');\n'
        lines[240] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w12_17\',\'day\','+str(
            partsunny12_17/2)+',\'partsunny-w12_17 - Day\');\n'
        lines[241] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w12_17\',\'night\','+str(
            partsunny12_17/2)+',\'partsunny-w12_17 - Night\');\n'
        lines[242] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w17_24\',\'day\','+str(
            partsunny17_24/2)+',\'partsunny-w17_24 - Day\');\n'
        lines[243] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w17_24\',\'night\','+str(
            partsunny17_24/2)+',\'partsunny-w17_24 - Night\');\n'
        lines[244] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w24_31\',\'day\','+str(
            partsunny24_31/2)+',\'partsunny-w24_31 - Day\');\n'
        lines[245] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w24_31\',\'night\','+str(
            partsunny24_31/2)+',\'partsunny-w24_31 - Night\');\n'
        lines[246] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w31_38\',\'day\','+str(
            partsunny31_38/2)+',\'partsunny-w31_38 - Day\');\n'
        lines[247] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-w31_38\',\'night\','+str(
            partsunny31_38/2)+',\'partsunny-w31_38 - Night\');\n'
        lines[248] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-wother\',\'day\','+str(
            partsunnyOther/2)+',\'partsunny-wother - Day\');\n'
        lines[249] = 'INSERT INTO `SegFrac` VALUES (\'partsunny-wother\',\'night\','+str(
            partsunnyOther/2)+',\'partsunny-wother - Night\');\n'

        lines[251] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w7_12\',\'day\','+str(
            cloudy7_12/2)+',\'cloudy-w7_12 - Day\');\n'
        lines[252] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w7_12\',\'night\','+str(
            cloudy7_12/2)+',\'cloudy-w7_12 - Night\');\n'
        lines[253] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w12_17\',\'day\','+str(
            cloudy12_17/2)+',\'cloudy-w12_17 - Day\');\n'
        lines[254] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w12_17\',\'night\','+str(
            cloudy12_17/2)+',\'cloudy-w12_17 - Night\');\n'
        lines[255] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w17_24\',\'day\','+str(
            cloudy17_24/2)+',\'cloudy-w17_24 - Day\');\n'
        lines[256] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w17_24\',\'night\','+str(
            cloudy17_24/2)+',\'cloudy-w17_24 - Night\');\n'
        lines[257] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w24_31\',\'day\','+str(
            cloudy24_31/2)+',\'cloudy-w24_31 - Day\');\n'
        lines[258] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w24_31\',\'night\','+str(
            cloudy24_31/2)+',\'cloudy-w24_31 - Night\');\n'
        lines[259] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w31_38\',\'day\','+str(
            cloudy31_38/2)+',\'cloudy-w31_38 - Day\');\n'
        lines[260] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-w31_38\',\'night\','+str(
            cloudy31_38/2)+',\'cloudy-w31_38 - Night\');\n'
        lines[261] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-wother\',\'day\','+str(
            cloudyOther/2)+',\'cloudy-wother - Day\');\n'
        lines[262] = 'INSERT INTO `SegFrac` VALUES (\'cloudy-wother\',\'night\','+str(
            cloudyOther/2)+',\'cloudy-wother - Night\');\n'

        # Demand Specific Distribution edit
        lines[762] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w7_12\',\'day\',\'DMND\','+str(
            sunny7_12/2)+',\'\');\n'
        lines[763] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w7_12\',\'night\',\'DMND\','+str(
            sunny7_12/2)+',\'\');\n'
        lines[764] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w12_17\',\'day\',\'DMND\','+str(
            sunny12_17/2)+',\'\');\n'
        lines[765] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w12_17\',\'night\',\'DMND\','+str(
            sunny12_17/2)+',\'\');\n'
        lines[766] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w17_24\',\'day\',\'DMND\','+str(
            sunny17_24/2)+',\'\');\n'
        lines[767] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w17_24\',\'night\',\'DMND\','+str(
            sunny17_24/2)+',\'\');\n'
        lines[768] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w24_31\',\'day\',\'DMND\','+str(
            sunny24_31/2)+',\'\');\n'
        lines[769] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w24_31\',\'night\',\'DMND\','+str(
            sunny24_31/2)+',\'\');\n'
        lines[770] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w31_38\',\'day\',\'DMND\','+str(
            sunny31_38/2)+',\'\');\n'
        lines[771] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-w31_38\',\'night\',\'DMND\','+str(
            sunny31_38/2)+',\'\');\n'
        lines[772] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-wother\',\'day\',\'DMND\','+str(
            sunnyOther/2)+',\'\');\n'
        lines[773] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'sunny-wother\',\'night\',\'DMND\','+str(
            sunnyOther/2)+',\'\');\n'

        lines[775] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w7_12\',\'day\',\'DMND\','+str(
            partsunny7_12/2)+',\'\');\n'
        lines[776] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w7_12\',\'night\',\'DMND\','+str(
            partsunny7_12/2)+',\'\');\n'
        lines[777] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w12_17\',\'day\',\'DMND\','+str(
            partsunny12_17/2)+',\'\');\n'
        lines[778] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w12_17\',\'night\',\'DMND\','+str(
            partsunny12_17/2)+',\'\');\n'
        lines[779] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w17_24\',\'day\',\'DMND\','+str(
            partsunny17_24/2)+',\'\');\n'
        lines[780] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w17_24\',\'night\',\'DMND\','+str(
            partsunny17_24/2)+',\'\');\n'
        lines[781] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w24_31\',\'day\',\'DMND\','+str(
            partsunny24_31/2)+',\'\');\n'
        lines[782] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w24_31\',\'night\',\'DMND\','+str(
            partsunny24_31/2)+',\'\');\n'
        lines[783] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w31_38\',\'day\',\'DMND\','+str(
            partsunny31_38/2)+',\'\');\n'
        lines[784] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-w31_38\',\'night\',\'DMND\','+str(
            partsunny31_38/2)+',\'\');\n'
        lines[785] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-wother\',\'day\',\'DMND\','+str(
            partsunnyOther/2)+',\'\');\n'
        lines[786] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'partsunny-wother\',\'night\',\'DMND\','+str(
            partsunnyOther/2)+',\'\');\n'

        lines[788] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w7_12\',\'day\',\'DMND\','+str(
            cloudy7_12/2)+',\'\');\n'
        lines[789] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w7_12\',\'night\',\'DMND\','+str(
            cloudy7_12/2)+',\'\');\n'
        lines[790] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w12_17\',\'day\',\'DMND\','+str(
            cloudy12_17/2)+',\'\');\n'
        lines[791] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w12_17\',\'night\',\'DMND\','+str(
            cloudy12_17/2)+',\'\');\n'
        lines[792] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w17_24\',\'day\',\'DMND\','+str(
            cloudy17_24/2)+',\'\');\n'
        lines[793] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w17_24\',\'night\',\'DMND\','+str(
            cloudy17_24/2)+',\'\');\n'
        lines[794] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w24_31\',\'day\',\'DMND\','+str(
            cloudy24_31/2)+',\'\');\n'
        lines[795] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w24_31\',\'night\',\'DMND\','+str(
            cloudy24_31/2)+',\'\');\n'
        lines[796] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w31_38\',\'day\',\'DMND\','+str(
            cloudy31_38/2)+',\'\');\n'
        lines[797] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-w31_38\',\'night\',\'DMND\','+str(
            cloudy31_38/2)+',\'\');\n'
        lines[798] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-wother\',\'day\',\'DMND\','+str(
            cloudyOther/2)+',\'\');\n'
        lines[799] = 'INSERT INTO `DemandSpecificDistribution` VALUES (\'R1\',\'cloudy-wother\',\'night\',\'DMND\','+str(
            cloudyOther/2)+',\'\');\n'

        # Demand
        demand2025 = populationProj['2025'] * \
            perCapitaProj['2025'] / (277.78 * 10**6)
        demand2030 = populationProj['2030'] * \
            perCapitaProj['2030'] / (277.78 * 10**6)
        demand2035 = populationProj['2035'] * \
            perCapitaProj['2035'] / (277.78 * 10**6)
        demand2040 = populationProj['2040'] * \
            perCapitaProj['2040'] / (277.78 * 10**6)
        demand2045 = populationProj['2045'] * \
            perCapitaProj['2045'] / (277.78 * 10**6)
        demand2049 = populationProj['2050'] * \
            perCapitaProj['2050'] / (277.78 * 10**6)

        lines[813] = 'INSERT INTO `Demand` VALUES (\'R1\',2025,\'DMND\','+str(
            demand2025)+',\'\',\'\');\n'
        lines[814] = 'INSERT INTO `Demand` VALUES (\'R1\',2030,\'DMND\','+str(
            demand2030)+',\'\',\'\');\n'
        lines[815] = 'INSERT INTO `Demand` VALUES (\'R1\',2035,\'DMND\','+str(
            demand2035)+',\'\',\'\');\n'
        lines[816] = 'INSERT INTO `Demand` VALUES (\'R1\',2040,\'DMND\','+str(
            demand2040)+',\'\',\'\');\n'
        lines[817] = 'INSERT INTO `Demand` VALUES (\'R1\',2045,\'DMND\','+str(
            demand2045)+',\'\',\'\');\n'
        lines[818] = 'INSERT INTO `Demand` VALUES (\'R1\',2049,\'DMND\','+str(
            demand2049)+',\'\',\'\');\n'

        # NG Price Edit
        ngPrice2025 = ngPriceProj['2025']
        ngPrice2030 = ngPriceProj['2030']
        ngPrice2035 = ngPriceProj['2035']
        ngPrice2040 = ngPriceProj['2040']
        ngPrice2045 = ngPriceProj['2045']
        ngPrice2049 = ngPriceProj['2050']

        lines[833] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPNG\',2020,'+str(
            ngPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[834] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPNG\',2020,'+str(
            ngPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[835] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPNG\',2020,'+str(
            ngPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[836] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2020,'+str(
            ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[837] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2020,'+str(
            ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[838] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2020,'+str(
            ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[839] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPNG\',2025,'+str(
            ngPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[840] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPNG\',2025,'+str(
            ngPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[841] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPNG\',2025,'+str(
            ngPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[842] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2025,'+str(
            ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[843] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2025,'+str(
            ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[844] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2025,'+str(
            ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[845] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPNG\',2030,'+str(
            ngPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[846] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPNG\',2030,'+str(
            ngPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[847] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2030,'+str(
            ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[848] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2030,'+str(
            ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[849] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2030,'+str(
            ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[850] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPNG\',2035,'+str(
            ngPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[851] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2035,'+str(
            ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[852] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2035,'+str(
            ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[853] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2035,'+str(
            ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[854] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPNG\',2040,'+str(
            ngPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[855] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2040,'+str(
            ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[856] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2040,'+str(
            ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[857] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPNG\',2045,'+str(
            ngPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[858] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2045,'+str(
            ngPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[859] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPNG\',2049,'+str(
            ngPrice2049)+',\'$M/PJ\',\'\');\n'

        # Uranium Price Edit
        urnPrice2025 = urnPriceProj['2025']
        urnPrice2030 = urnPriceProj['2030']
        urnPrice2035 = urnPriceProj['2035']
        urnPrice2040 = urnPriceProj['2040']
        urnPrice2045 = urnPriceProj['2045']
        urnPrice2049 = urnPriceProj['2050']

        lines[861] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPURN\',2025,'+str(
            urnPrice2025)+',\'$M/PJ\',\'\');\n'
        lines[862] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPURN\',2025,'+str(
            urnPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[863] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPURN\',2025,'+str(
            urnPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[864] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPURN\',2025,'+str(
            urnPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[865] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2025,'+str(
            urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[866] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2025,'+str(
            urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[867] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPURN\',2030,'+str(
            urnPrice2030)+',\'$M/PJ\',\'\');\n'
        lines[868] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPURN\',2030,'+str(
            urnPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[869] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPURN\',2030,'+str(
            urnPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[870] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2030,'+str(
            urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[871] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2030,'+str(
            urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[872] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPURN\',2035,'+str(
            urnPrice2035)+',\'$M/PJ\',\'\');\n'
        lines[873] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPURN\',2035,'+str(
            urnPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[874] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2035,'+str(
            urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[875] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2035,'+str(
            urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[876] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPURN\',2040,'+str(
            urnPrice2040)+',\'$M/PJ\',\'\');\n'
        lines[877] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2040,'+str(
            urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[878] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2040,'+str(
            urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[879] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPURN\',2045,'+str(
            urnPrice2045)+',\'$M/PJ\',\'\');\n'
        lines[880] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2045,'+str(
            urnPrice2049)+',\'$M/PJ\',\'\');\n'
        lines[881] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPURN\',2049,'+str(
            urnPrice2049)+',\'$M/PJ\',\'\');\n'

        # E_NG Var Price Edit
        e_ng_var2025 = e_ngVarProj['2025']
        e_ng_var2030 = e_ngVarProj['2030']
        e_ng_var2035 = e_ngVarProj['2035']
        e_ng_var2040 = e_ngVarProj['2040']
        e_ng_var2045 = e_ngVarProj['2045']
        e_ng_var2049 = e_ngVarProj['2050']

        lines[883] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'E_NGCC\',2020,'+str(
            e_ng_var2025)+',\'$M/PJ\',\'\');\n'
        lines[884] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NGCC\',2020,'+str(
            e_ng_var2030)+',\'$M/PJ\',\'\');\n'
        lines[885] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NGCC\',2020,'+str(
            e_ng_var2035)+',\'$M/PJ\',\'\');\n'
        lines[886] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2020,'+str(
            e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[887] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2020,'+str(
            e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[888] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2020,'+str(
            e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[889] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'E_NGCC\',2025,'+str(
            e_ng_var2025)+',\'$M/PJ\',\'\');\n'
        lines[890] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NGCC\',2025,'+str(
            e_ng_var2030)+',\'$M/PJ\',\'\');\n'
        lines[891] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NGCC\',2025,'+str(
            e_ng_var2035)+',\'$M/PJ\',\'\');\n'
        lines[892] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2025,'+str(
            e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[893] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2025,'+str(
            e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[894] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2025,'+str(
            e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[895] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NGCC\',2030,'+str(
            e_ng_var2030)+',\'$M/PJ\',\'\');\n'
        lines[896] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NGCC\',2030,'+str(
            e_ng_var2035)+',\'$M/PJ\',\'\');\n'
        lines[897] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2030,'+str(
            e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[898] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2030,'+str(
            e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[899] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2030,'+str(
            e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[900] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NGCC\',2035,'+str(
            e_ng_var2035)+',\'$M/PJ\',\'\');\n'
        lines[901] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2035,'+str(
            e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[902] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2035,'+str(
            e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[903] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2035,'+str(
            e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[904] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NGCC\',2040,'+str(
            e_ng_var2040)+',\'$M/PJ\',\'\');\n'
        lines[905] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2040,'+str(
            e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[906] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2040,'+str(
            e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[907] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NGCC\',2045,'+str(
            e_ng_var2045)+',\'$M/PJ\',\'\');\n'
        lines[908] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2045,'+str(
            e_ng_var2049)+',\'$M/PJ\',\'\');\n'
        lines[909] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NGCC\',2049,'+str(
            e_ng_var2049)+',\'$M/PJ\',\'\');\n'

        # E_NUC Var Price Edit
        e_urn_var2025 = e_nucVarProj['2025']
        e_urn_var2030 = e_nucVarProj['2030']
        e_urn_var2035 = e_nucVarProj['2035']
        e_urn_var2040 = e_nucVarProj['2040']
        e_urn_var2045 = e_nucVarProj['2045']
        e_urn_var2049 = e_nucVarProj['2050']

        lines[911] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'E_NUCLEAR\',2025,'+str(
            e_urn_var2025)+',\'$M/PJ\',\'\');\n'
        lines[912] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NUCLEAR\',2025,'+str(
            e_urn_var2030)+',\'$M/PJ\',\'\');\n'
        lines[913] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NUCLEAR\',2025,'+str(
            e_urn_var2035)+',\'$M/PJ\',\'\');\n'
        lines[914] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NUCLEAR\',2025,'+str(
            e_urn_var2040)+',\'$M/PJ\',\'\');\n'
        lines[915] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2025,'+str(
            e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[916] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2025,'+str(
            e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[917] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_NUCLEAR\',2030,'+str(
            e_urn_var2030)+',\'$M/PJ\',\'\');\n'
        lines[918] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NUCLEAR\',2030,'+str(
            e_urn_var2035)+',\'$M/PJ\',\'\');\n'
        lines[919] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NUCLEAR\',2030,'+str(
            e_urn_var2040)+',\'$M/PJ\',\'\');\n'
        lines[920] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2030,'+str(
            e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[921] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2030,'+str(
            e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[922] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_NUCLEAR\',2035,'+str(
            e_urn_var2035)+',\'$M/PJ\',\'\');\n'
        lines[923] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NUCLEAR\',2035,'+str(
            e_urn_var2040)+',\'$M/PJ\',\'\');\n'
        lines[924] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2035,'+str(
            e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[925] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2035,'+str(
            e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[926] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_NUCLEAR\',2040,'+str(
            e_urn_var2040)+',\'$M/PJ\',\'\');\n'
        lines[927] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2040,'+str(
            e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[928] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2040,'+str(
            e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[929] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_NUCLEAR\',2045,'+str(
            e_urn_var2045)+',\'$M/PJ\',\'\');\n'
        lines[930] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2045,'+str(
            e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        lines[931] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_NUCLEAR\',2049,'+str(
            e_urn_var2049)+',\'$M/PJ\',\'\');\n'
        # Investment Costs Price Edit
        e_ng_inv2025 = e_ngInvProj['2025']
        e_ng_inv2030 = e_ngInvProj['2030']
        e_ng_inv2035 = e_ngInvProj['2035']
        e_ng_inv2040 = e_ngInvProj['2040']
        e_ng_inv2045 = e_ngInvProj['2045']
        e_ng_inv2049 = e_ngInvProj['2050']

        e_sol_inv2025 = e_solInvProj['2025']
        e_sol_inv2030 = e_solInvProj['2030']
        e_sol_inv2035 = e_solInvProj['2035']
        e_sol_inv2040 = e_solInvProj['2040']
        e_sol_inv2045 = e_solInvProj['2045']
        e_sol_inv2049 = e_solInvProj['2050']

        e_wind_inv2025 = e_windInvProj['2025']
        e_wind_inv2030 = e_windInvProj['2030']
        e_wind_inv2035 = e_windInvProj['2035']
        e_wind_inv2040 = e_windInvProj['2040']
        e_wind_inv2045 = e_windInvProj['2045']
        e_wind_inv2049 = e_windInvProj['2050']

        e_nuc_inv2025 = e_nucInvProj['2025']
        e_nuc_inv2030 = e_nucInvProj['2030']
        e_nuc_inv2035 = e_nucInvProj['2035']
        e_nuc_inv2040 = e_nucInvProj['2040']
        e_nuc_inv2045 = e_nucInvProj['2045']
        e_nuc_inv2049 = e_nucInvProj['2050']

        e_hyd_inv2025 = e_hydInvProj['2025']
        e_hyd_inv2030 = e_hydInvProj['2030']
        e_hyd_inv2035 = e_hydInvProj['2035']
        e_hyd_inv2040 = e_hydInvProj['2040']
        e_hyd_inv2045 = e_hydInvProj['2045']
        e_hyd_inv2049 = e_hydInvProj['2050']
        
        e_batt_inv2025 = e_battInvProj['2025']
        e_batt_inv2030 = e_battInvProj['2030']
        e_batt_inv2035 = e_battInvProj['2035']
        e_batt_inv2040 = e_battInvProj['2040']
        e_batt_inv2045 = e_battInvProj['2045']
        e_batt_inv2049 = e_battInvProj['2050']
        

        lines[1001] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2025,'+str(
            e_ng_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1002] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2025,'+str(
            e_sol_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1003] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2025,'+str(
            e_wind_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1004] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2025,'+str(
            e_nuc_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1005] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2025,'+str(
            e_hyd_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1007] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2025,'+str(
            e_batt_inv2025)+',\'$M/GW\',\'\');\n'
       
        lines[1013] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2030,'+str(
            e_ng_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1014] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2030,'+str(
            e_sol_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1015] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2030,'+str(
            e_wind_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1016] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2030,'+str(
            e_nuc_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1017] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2030,'+str(
            e_hyd_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1019] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2030,'+str(
            e_batt_inv2030)+',\'$M/GW\',\'\');\n'
        
        lines[1025] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2035,'+str(
            e_ng_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1026] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2035,'+str(
            e_sol_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1027] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2035,'+str(
            e_wind_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1028] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2035,'+str(
            e_nuc_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1029] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2035,'+str(
            e_hyd_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1031] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2035,'+str(
            e_batt_inv2035)+',\'$M/GW\',\'\');\n'
        
        lines[1037] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2040,'+str(
            e_ng_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1038] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2040,'+str(
            e_sol_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1039] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2040,'+str(
            e_wind_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1040] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2040,'+str(
            e_nuc_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1041] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2040,'+str(
            e_hyd_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1043] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2040,'+str(
            e_batt_inv2040)+',\'$M/GW\',\'\');\n'
        
        lines[1049] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2045,'+str(
            e_ng_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1050] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2045,'+str(
            e_sol_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1051] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2045,'+str(
            e_wind_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1052] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2045,'+str(
            e_nuc_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1053] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2045,'+str(
            e_hyd_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1055] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2045,'+str(
            e_batt_inv2045)+',\'$M/GW\',\'\');\n'
        
        lines[1061] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NGCC\',2049,'+str(
            e_ng_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1062] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_SOLPV\',2049,'+str(
            e_sol_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1063] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_WIND\',2049,'+str(
            e_wind_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1064] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_NUCLEAR\',2049,'+str(
            e_nuc_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1065] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_HYDRO\',2049,'+str(
            e_hyd_inv2049)+',\'$M/GW\',\'\');\n'
        lines[1067] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BATT\',2049,'+str(
            e_batt_inv2049)+',\'$M/GW\',\'\');\n'
        
        # E_NG Fix Price Edit
        e_ng_fix2020 = e_ngFixProj['2020']
        e_ng_fix2025 = e_ngFixProj['2025']
        e_ng_fix2030 = e_ngFixProj['2030']
        e_ng_fix2035 = e_ngFixProj['2035']
        e_ng_fix2040 = e_ngFixProj['2040']
        e_ng_fix2045 = e_ngFixProj['2045']
        e_ng_fix2049 = e_ngFixProj['2050']

        lines[1087] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_NGCC\',2020,'+str(
            e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1088] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NGCC\',2020,'+str(
            e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1089] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NGCC\',2020,'+str(
            e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1090] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2020,'+str(
            e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1091] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2020,'+str(
            e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1092] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2020,'+str(
            e_ng_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1093] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_NGCC\',2025,'+str(
            e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1094] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NGCC\',2025,'+str(
            e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1095] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NGCC\',2025,'+str(
            e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1096] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2025,'+str(
            e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1097] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2025,'+str(
            e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1098] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2025,'+str(
            e_ng_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1099] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NGCC\',2030,'+str(
            e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1100] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NGCC\',2030,'+str(
            e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1101] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2030,'+str(
            e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1102] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2030,'+str(
            e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1103] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2030,'+str(
            e_ng_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1104] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NGCC\',2035,'+str(
            e_ng_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1105] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2035,'+str(
            e_ng_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1106] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2035,'+str(
            e_ng_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1107] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2035,'+str(
            e_ng_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1108] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NGCC\',2040,'+str(
            e_ng_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1109] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2040,'+str(
            e_ng_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1110] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2040,'+str(
            e_ng_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1111] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NGCC\',2045,'+str(
            e_ng_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1112] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2045,'+str(
            e_ng_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1113] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NGCC\',2049,'+str(
            e_ng_fix2049)+',\'$M/GWyr\',\'\');\n'

        # E_SOL Fix Price Edit
        e_sol_fix2020 = e_solFixProj['2020']
        e_sol_fix2025 = e_solFixProj['2025']
        e_sol_fix2030 = e_solFixProj['2030']
        e_sol_fix2035 = e_solFixProj['2035']
        e_sol_fix2040 = e_solFixProj['2040']
        e_sol_fix2045 = e_solFixProj['2045']
        e_sol_fix2049 = e_solFixProj['2050']

        lines[1115] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_SOLPV\',2020,'+str(
            e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1116] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_SOLPV\',2020,'+str(
            e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1117] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_SOLPV\',2020,'+str(
            e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1118] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2020,'+str(
            e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1119] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2020,'+str(
            e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1120] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2020,'+str(
            e_sol_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1121] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_SOLPV\',2025,'+str(
            e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1122] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_SOLPV\',2025,'+str(
            e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1123] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_SOLPV\',2025,'+str(
            e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1124] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2025,'+str(
            e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1125] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2025,'+str(
            e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1126] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2025,'+str(
            e_sol_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1127] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_SOLPV\',2030,'+str(
            e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1128] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_SOLPV\',2030,'+str(
            e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1129] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2030,'+str(
            e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1130] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2030,'+str(
            e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1131] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2030,'+str(
            e_sol_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1132] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_SOLPV\',2035,'+str(
            e_sol_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1133] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2035,'+str(
            e_sol_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1134] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2035,'+str(
            e_sol_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1135] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2035,'+str(
            e_sol_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1136] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_SOLPV\',2040,'+str(
            e_sol_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1137] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2040,'+str(
            e_sol_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1138] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2040,'+str(
            e_sol_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1139] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_SOLPV\',2045,'+str(
            e_sol_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1140] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2045,'+str(
            e_sol_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1141] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_SOLPV\',2049,'+str(
            e_sol_fix2049)+',\'$M/GWyr\',\'\');\n'

        # E_WIND Fix Price Edit
        e_wind_fix2020 = e_windFixProj['2020']
        e_wind_fix2025 = e_windFixProj['2025']
        e_wind_fix2030 = e_windFixProj['2030']
        e_wind_fix2035 = e_windFixProj['2035']
        e_wind_fix2040 = e_windFixProj['2040']
        e_wind_fix2045 = e_windFixProj['2045']
        e_wind_fix2049 = e_windFixProj['2050']

        lines[1143] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_WIND\',2020,'+str(
            e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1144] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_WIND\',2020,'+str(
            e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1145] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_WIND\',2020,'+str(
            e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1146] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2020,'+str(
            e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1147] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2020,'+str(
            e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1148] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2020,'+str(
            e_wind_fix2020)+',\'$M/GWyr\',\'\');\n'
        lines[1149] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_WIND\',2025,'+str(
            e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1150] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_WIND\',2025,'+str(
            e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1151] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_WIND\',2025,'+str(
            e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1152] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2025,'+str(
            e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1153] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2025,'+str(
            e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1154] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2025,'+str(
            e_wind_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1155] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_WIND\',2030,'+str(
            e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1156] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_WIND\',2030,'+str(
            e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1157] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2030,'+str(
            e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1158] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2030,'+str(
            e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1159] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2030,'+str(
            e_wind_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1160] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_WIND\',2035,'+str(
            e_wind_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1161] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2035,'+str(
            e_wind_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1162] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2035,'+str(
            e_wind_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1163] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2035,'+str(
            e_wind_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1164] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_WIND\',2040,'+str(
            e_wind_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1165] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2040,'+str(
            e_wind_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1166] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2040,'+str(
            e_wind_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1167] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_WIND\',2045,'+str(
            e_wind_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1168] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2045,'+str(
            e_wind_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1169] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_WIND\',2049,'+str(
            e_wind_fix2049)+',\'$M/GWyr\',\'\');\n'

        # E_HYDRO Fix Price Edit
        e_hyd_fix2025 = e_hydFixProj['2025']
        e_hyd_fix2030 = e_hydFixProj['2030']
        e_hyd_fix2035 = e_hydFixProj['2035']
        e_hyd_fix2040 = e_hydFixProj['2040']
        e_hyd_fix2045 = e_hydFixProj['2045']
        e_hyd_fix2049 = e_hydFixProj['2050']

        lines[1171] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_HYDRO\',2025,'+str(
            e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1172] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_HYDRO\',2025,'+str(
            e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1173] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_HYDRO\',2025,'+str(
            e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1174] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_HYDRO\',2025,'+str(
            e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1175] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2025,'+str(
            e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1176] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2025,'+str(
            e_hyd_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1177] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_HYDRO\',2030,'+str(
            e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1178] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_HYDRO\',2030,'+str(
            e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1179] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_HYDRO\',2030,'+str(
            e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1180] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2030,'+str(
            e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1181] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2030,'+str(
            e_hyd_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1182] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_HYDRO\',2035,'+str(
            e_hyd_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1183] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_HYDRO\',2035,'+str(
            e_hyd_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1184] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2035,'+str(
            e_hyd_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1185] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2035,'+str(
            e_hyd_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1186] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_HYDRO\',2040,'+str(
            e_hyd_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1187] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2040,'+str(
            e_hyd_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1188] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2040,'+str(
            e_hyd_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1189] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_HYDRO\',2045,'+str(
            e_hyd_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1190] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2045,'+str(
            e_hyd_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1191] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_HYDRO\',2049,'+str(
            e_hyd_fix2049)+',\'$M/GWyr\',\'\');\n'

    
        # E_NUCLEAR Fix Price Edit
        e_nuc_fix2025 = e_nucFixProj['2025']
        e_nuc_fix2030 = e_nucFixProj['2030']
        e_nuc_fix2035 = e_nucFixProj['2035']
        e_nuc_fix2040 = e_nucFixProj['2040']
        e_nuc_fix2045 = e_nucFixProj['2045']
        e_nuc_fix2049 = e_nucFixProj['2050']

        lines[1215] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_NUCLEAR\',2025,'+str(
            e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1216] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NUCLEAR\',2025,'+str(
            e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1217] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NUCLEAR\',2025,'+str(
            e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1218] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NUCLEAR\',2025,'+str(
            e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1219] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2025,'+str(
            e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1220] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2025,'+str(
            e_nuc_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1221] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_NUCLEAR\',2030,'+str(
            e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1222] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NUCLEAR\',2030,'+str(
            e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1223] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NUCLEAR\',2030,'+str(
            e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1224] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2030,'+str(
            e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1225] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2030,'+str(
            e_nuc_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1226] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_NUCLEAR\',2035,'+str(
            e_nuc_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1227] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NUCLEAR\',2035,'+str(
            e_nuc_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1228] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2035,'+str(
            e_nuc_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1229] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2035,'+str(
            e_nuc_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1230] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_NUCLEAR\',2040,'+str(
            e_nuc_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1231] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2040,'+str(
            e_nuc_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1232] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2040,'+str(
            e_nuc_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1233] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_NUCLEAR\',2045,'+str(
            e_nuc_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1234] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2045,'+str(
            e_nuc_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1235] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_NUCLEAR\',2049,'+str(
            e_nuc_fix2049)+',\'$M/GWyr\',\'\');\n'

        # E_BATT Fix Price Edit
        e_batt_fix2025 = e_battFixProj['2025']
        e_batt_fix2030 = e_battFixProj['2030']
        e_batt_fix2035 = e_battFixProj['2035']
        e_batt_fix2040 = e_battFixProj['2040']
        e_batt_fix2045 = e_battFixProj['2045']
        e_batt_fix2049 = e_battFixProj['2050']

        lines[1237] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_BATT\',2025,'+str(
            e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1238] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_BATT\',2025,'+str(
            e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1239] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BATT\',2025,'+str(
            e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1240] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BATT\',2025,'+str(
            e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1241] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2025,'+str(
            e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1242] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2025,'+str(
            e_batt_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1243] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_BATT\',2030,'+str(
            e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1244] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BATT\',2030,'+str(
            e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1245] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BATT\',2030,'+str(
            e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1246] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2030,'+str(
            e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1247] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2030,'+str(
            e_batt_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1248] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BATT\',2035,'+str(
            e_batt_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1249] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BATT\',2035,'+str(
            e_batt_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1250] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2035,'+str(
            e_batt_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1251] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2035,'+str(
            e_batt_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1252] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BATT\',2040,'+str(
            e_batt_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1253] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2040,'+str(
            e_batt_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1254] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2040,'+str(
            e_batt_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1255] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BATT\',2045,'+str(
            e_batt_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1256] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2045,'+str(
            e_batt_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1257] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BATT\',2049,'+str(
            e_batt_fix2049)+',\'$M/GWyr\',\'\');\n'

        # Capacity factor SOL edit
        e_sol_cf = solCf

        lines[1290] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'day\',\'E_SOLPV\','+str(
            e_sol_cf)+',\'\');\n'
        lines[1292] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'day\',\'E_SOLPV\','+str(
            e_sol_cf)+',\'\');\n'
        lines[1294] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'day\',\'E_SOLPV\','+str(
            e_sol_cf)+',\'\');\n'
        lines[1296] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'day\',\'E_SOLPV\','+str(
            e_sol_cf)+',\'\');\n'
        lines[1298] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'day\',\'E_SOLPV\','+str(
            e_sol_cf)+',\'\');\n'
        lines[1300] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-wother\',\'day\',\'E_SOLPV\','+str(
            e_sol_cf)+',\'\');\n'
        lines[1302] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'day\',\'E_SOLPV\','+str(
            0.7 * e_sol_cf)+',\'\');\n'
        lines[1304] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'day\',\'E_SOLPV\','+str(
            0.7 * e_sol_cf)+',\'\');\n'
        lines[1306] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'day\',\'E_SOLPV\','+str(
            0.7 * e_sol_cf)+',\'\');\n'
        lines[1308] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'day\',\'E_SOLPV\','+str(
            0.7 * e_sol_cf)+',\'\');\n'
        lines[1310] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'day\',\'E_SOLPV\','+str(
            0.7 * e_sol_cf)+',\'\');\n'
        lines[1312] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-wother\',\'day\',\'E_SOLPV\','+str(
            0.7 * e_sol_cf)+',\'\');\n'
        lines[1313] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-wother\',\'night\',\'E_SOLPV\','+str(
            0.7 * e_sol_cf)+',\'\');\n'

        # Capacity factor WIND edit
        e_wind_cf_7_12 = windCf1 * \
            (9.5 * 1.609)**3 + windCf2 * (9.5 * 1.609)**2 + \
            windCf3 * (9.5 * 1.609) + windCf4
        e_wind_cf_12_17 = windCf1 * \
            (14.5 * 1.609)**3 + windCf2 * (14.5 * 1.609)**2 + \
            windCf3 * (14.5 * 1.609) + windCf4
        e_wind_cf_17_24 = windCf1 * \
            (20.5 * 1.609)**3 + windCf2 * (20.5 * 1.609)**2 + \
            windCf3 * (20.5 * 1.609) + windCf4
        e_wind_cf_24_31 = min(windCf1 * (27.5 * 1.609)**3 + windCf2 *
                              (27.5 * 1.609)**2 + windCf3 * (27.5 * 1.609) + windCf4, 1)
        e_wind_cf_31_38 = min(windCf1 * (34.5 * 1.609)**3 + windCf2 *
                              (34.5 * 1.609)**2 + windCf3 * (34.5 * 1.609) + windCf4, 1)

        lines[1327] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'day\',\'E_WIND\','+str(
            e_wind_cf_7_12)+',\'\');\n'
        lines[1328] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'night\',\'E_WIND\','+str(
            e_wind_cf_7_12)+',\'\');\n'
        lines[1329] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'day\',\'E_WIND\','+str(
            e_wind_cf_12_17)+',\'\');\n'
        lines[1330] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'night\',\'E_WIND\','+str(
            e_wind_cf_12_17)+',\'\');\n'
        lines[1331] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'day\',\'E_WIND\','+str(
            e_wind_cf_17_24)+',\'\');\n'
        lines[1332] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'night\',\'E_WIND\','+str(
            e_wind_cf_17_24)+',\'\');\n'
        lines[1333] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'day\',\'E_WIND\','+str(
            e_wind_cf_24_31)+',\'\');\n'
        lines[1334] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'night\',\'E_WIND\','+str(
            e_wind_cf_24_31)+',\'\');\n'
        lines[1335] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'day\',\'E_WIND\','+str(
            e_wind_cf_31_38)+',\'\');\n'
        lines[1336] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'night\',\'E_WIND\','+str(
            e_wind_cf_31_38)+',\'\');\n'
        lines[1339] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'day\',\'E_WIND\','+str(
            e_wind_cf_7_12)+',\'\');\n'
        lines[1340] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'night\',\'E_WIND\','+str(
            e_wind_cf_7_12)+',\'\');\n'
        lines[1341] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'day\',\'E_WIND\','+str(
            e_wind_cf_12_17)+',\'\');\n'
        lines[1342] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'night\',\'E_WIND\','+str(
            e_wind_cf_12_17)+',\'\');\n'
        lines[1343] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'day\',\'E_WIND\','+str(
            e_wind_cf_17_24)+',\'\');\n'
        lines[1344] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'night\',\'E_WIND\','+str(
            e_wind_cf_17_24)+',\'\');\n'
        lines[1345] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'day\',\'E_WIND\','+str(
            e_wind_cf_24_31)+',\'\');\n'
        lines[1346] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'night\',\'E_WIND\','+str(
            e_wind_cf_24_31)+',\'\');\n'
        lines[1347] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'day\',\'E_WIND\','+str(
            e_wind_cf_31_38)+',\'\');\n'
        lines[1348] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'night\',\'E_WIND\','+str(
            e_wind_cf_31_38)+',\'\');\n'
        lines[1351] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w7_12\',\'day\',\'E_WIND\','+str(
            e_wind_cf_7_12)+',\'\');\n'
        lines[1352] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w7_12\',\'night\',\'E_WIND\','+str(
            e_wind_cf_7_12)+',\'\');\n'
        lines[1353] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w12_17\',\'day\',\'E_WIND\','+str(
            e_wind_cf_12_17)+',\'\');\n'
        lines[1354] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w12_17\',\'night\',\'E_WIND\','+str(
            e_wind_cf_12_17)+',\'\');\n'
        lines[1355] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w17_24\',\'day\',\'E_WIND\','+str(
            e_wind_cf_17_24)+',\'\');\n'
        lines[1356] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w17_24\',\'night\',\'E_WIND\','+str(
            e_wind_cf_17_24)+',\'\');\n'
        lines[1357] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w24_31\',\'day\',\'E_WIND\','+str(
            e_wind_cf_24_31)+',\'\');\n'
        lines[1358] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w24_31\',\'night\',\'E_WIND\','+str(
            e_wind_cf_24_31)+',\'\');\n'
        lines[1359] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w31_38\',\'day\',\'E_WIND\','+str(
            e_wind_cf_31_38)+',\'\');\n'
        lines[1360] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w31_38\',\'night\',\'E_WIND\','+str(
            e_wind_cf_31_38)+',\'\');\n'

        # Capacity factor HYDRO edit
        lines[1364] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1365] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w7_12\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1366] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1367] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w12_17\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1368] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1369] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w17_24\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1370] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1371] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w24_31\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1372] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1373] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-w31_38\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1374] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-wother\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1375] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'sunny-wother\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'

        lines[1376] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1377] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w7_12\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1378] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1379] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w12_17\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1380] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1381] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w17_24\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1382] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1383] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w24_31\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1384] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1385] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-w31_38\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1386] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-wother\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1387] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'partsunny-wother\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'

        lines[1388] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w7_12\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1389] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w7_12\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1390] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w12_17\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1391] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w12_17\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1392] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w17_24\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1393] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w17_24\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1394] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w24_31\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1395] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w24_31\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1396] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w31_38\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1397] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-w31_38\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1398] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-wother\',\'day\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'
        lines[1399] = 'INSERT INTO `CapacityFactorTech` VALUES (\'R1\', \'cloudy-wother\',\'night\',\'E_HYDRO\','+str(
            e_hydCF)+',\'\');\n'

        # E_BIO Var Price Edit
        e_bio_var2025 = e_bioVarProj['2025']
        e_bio_var2030 = e_bioVarProj['2030']
        e_bio_var2035 = e_bioVarProj['2035']
        e_bio_var2040 = e_bioVarProj['2040']
        e_bio_var2045 = e_bioVarProj['2045']
        e_bio_var2049 = e_bioVarProj['2050']

        lines[1604] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'E_BIO\',2025,'+str(
            e_bio_var2025)+',\'$M/PJ\',\'\');\n'
        lines[1605] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_BIO\',2025,'+str(
            e_bio_var2030)+',\'$M/PJ\',\'\');\n'
        lines[1606] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_BIO\',2025,'+str(
            e_bio_var2035)+',\'$M/PJ\',\'\');\n'
        lines[1607] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_BIO\',2025,'+str(
            e_bio_var2040)+',\'$M/PJ\',\'\');\n'
        lines[1608] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_BIO\',2025,'+str(
            e_bio_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1609] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_BIO\',2025,'+str(
            e_bio_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1610] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'E_BIO\',2030,'+str(
            e_bio_var2030)+',\'$M/PJ\',\'\');\n'
        lines[1611] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_BIO\',2030,'+str(
            e_bio_var2035)+',\'$M/PJ\',\'\');\n'
        lines[1612] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_BIO\',2030,'+str(
            e_bio_var2040)+',\'$M/PJ\',\'\');\n'
        lines[1613] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_BIO\',2030,'+str(
            e_bio_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1614] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_BIO\',2030,'+str(
            e_bio_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1615] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'E_BIO\',2035,'+str(
            e_bio_var2035)+',\'$M/PJ\',\'\');\n'
        lines[1616] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_BIO\',2035,'+str(
            e_bio_var2040)+',\'$M/PJ\',\'\');\n'
        lines[1617] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_BIO\',2035,'+str(
            e_bio_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1618] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_BIO\',2035,'+str(
            e_bio_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1619] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'E_BIO\',2040,'+str(
            e_bio_var2040)+',\'$M/PJ\',\'\');\n'
        lines[1620] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_BIO\',2040,'+str(
            e_bio_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1621] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_BIO\',2040,'+str(
            e_bio_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1622] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'E_BIO\',2045,'+str(
            e_bio_var2045)+',\'$M/PJ\',\'\');\n'
        lines[1623] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_BIO\',2045,'+str(
            e_bio_var2049)+',\'$M/PJ\',\'\');\n'
        lines[1624] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'E_BIO\',2049,'+str(
            e_bio_var2049)+',\'$M/PJ\',\'\');\n'

        # E_BIO Cap Price Edit
        e_bio_inv2025 = e_bioInvProj['2025']
        e_bio_inv2030 = e_bioInvProj['2030']
        e_bio_inv2035 = e_bioInvProj['2035']
        e_bio_inv2040 = e_bioInvProj['2040']
        e_bio_inv2045 = e_bioInvProj['2045']
        e_bio_inv2049 = e_bioInvProj['2050']
        lines[1625] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BIO\',2025,'+str(
            e_bio_inv2025)+',\'$M/GW\',\'\');\n'
        lines[1626] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BIO\',2030,'+str(
            e_bio_inv2030)+',\'$M/GW\',\'\');\n'
        lines[1627] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BIO\',2035,'+str(
            e_bio_inv2035)+',\'$M/GW\',\'\');\n'
        lines[1628] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BIO\',2040,'+str(
            e_bio_inv2040)+',\'$M/GW\',\'\');\n'
        lines[1629] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BIO\',2045,'+str(
            e_bio_inv2045)+',\'$M/GW\',\'\');\n'
        lines[1630] = 'INSERT INTO `CostInvest` VALUES (\'R1\',\'E_BIO\',2049,'+str(
            e_bio_inv2049)+',\'$M/GW\',\'\');\n'

        # E_BIO Fix Price Edit
        e_bio_fix2025 = e_bioFixProj['2025']
        e_bio_fix2030 = e_bioFixProj['2030']
        e_bio_fix2035 = e_bioFixProj['2035']
        e_bio_fix2040 = e_bioFixProj['2040']
        e_bio_fix2045 = e_bioFixProj['2045']
        e_bio_fix2049 = e_bioFixProj['2050']

        lines[1631] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2025,\'E_BIO\',2025,'+str(
            e_bio_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1632] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_BIO\',2025,'+str(
            e_bio_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1633] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BIO\',2025,'+str(
            e_bio_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1634] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BIO\',2025,'+str(
            e_bio_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1635] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BIO\',2025,'+str(
            e_bio_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1636] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BIO\',2025,'+str(
            e_bio_fix2025)+',\'$M/GWyr\',\'\');\n'
        lines[1637] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2030,\'E_BIO\',2030,'+str(
            e_bio_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1638] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BIO\',2030,'+str(
            e_bio_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1639] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BIO\',2030,'+str(
            e_bio_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1640] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BIO\',2030,'+str(
            e_bio_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1641] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BIO\',2030,'+str(
            e_bio_fix2030)+',\'$M/GWyr\',\'\');\n'
        lines[1642] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2035,\'E_BIO\',2035,'+str(
            e_bio_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1643] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BIO\',2035,'+str(
            e_bio_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1644] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BIO\',2035,'+str(
            e_bio_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1645] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BIO\',2035,'+str(
            e_bio_fix2035)+',\'$M/GWyr\',\'\');\n'
        lines[1646] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2040,\'E_BIO\',2040,'+str(
            e_bio_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1647] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BIO\',2040,'+str(
            e_bio_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1648] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BIO\',2040,'+str(
            e_bio_fix2040)+',\'$M/GWyr\',\'\');\n'
        lines[1649] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2045,\'E_BIO\',2045,'+str(
            e_bio_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1650] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BIO\',2045,'+str(
            e_bio_fix2045)+',\'$M/GWyr\',\'\');\n'
        lines[1651] = 'INSERT INTO `CostFixed` VALUES (\'R1\',2049,\'E_BIO\',2049,'+str(
            e_bio_fix2049)+',\'$M/GWyr\',\'\');\n'

        # E_BIO Max Capacity Edit
        lines[1722] = 'INSERT INTO `MaxCapacity` VALUES (\'R1\',\'2025\',\'E_BIO\','+str(
            e_bioMaxCap)+',\'GW\',\'\');\n'
        lines[1723] = 'INSERT INTO `MaxCapacity` VALUES (\'R1\',\'2030\',\'E_BIO\','+str(
            e_bioMaxCap)+',\'GW\',\'\');\n'
        lines[1724] = 'INSERT INTO `MaxCapacity` VALUES (\'R1\',\'2035\',\'E_BIO\','+str(
            e_bioMaxCap)+',\'GW\',\'\');\n'
        lines[1725] = 'INSERT INTO `MaxCapacity` VALUES (\'R1\',\'2040\',\'E_BIO\','+str(
            e_bioMaxCap)+',\'GW\',\'\');\n'
        lines[1726] = 'INSERT INTO `MaxCapacity` VALUES (\'R1\',\'2045\',\'E_BIO\','+str(
            e_bioMaxCap)+',\'GW\',\'\');\n'
        lines[1727] = 'INSERT INTO `MaxCapacity` VALUES (\'R1\',\'2049\',\'E_BIO\','+str(
            e_bioMaxCap)+',\'GW\',\'\');\n'

        # IMPBIO Price Edit
        lines[1761] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2025,\'S_IMPBIO\',2025,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1762] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPBIO\',2025,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1763] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPBIO\',2025,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1764] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPBIO\',2025,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1765] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPBIO\',2025,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1766] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPBIO\',2025,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1767] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2030,\'S_IMPBIO\',2030,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1768] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPBIO\',2030,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1769] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPBIO\',2030,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1770] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPBIO\',2030,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1771] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPBIO\',2030,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1772] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2035,\'S_IMPBIO\',2035,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1773] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPBIO\',2035,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1774] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPBIO\',2035,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1775] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPBIO\',2035,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1776] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2040,\'S_IMPBIO\',2040,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1777] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPBIO\',2040,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1778] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPBIO\',2040,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1779] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2045,\'S_IMPBIO\',2045,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1780] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPBIO\',2045,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'
        lines[1781] = 'INSERT INTO `CostVariable` VALUES (\'R1\',2049,\'S_IMPBIO\',2049,' + str(
            bioPrice)+',\'$M/PJ\',\'\');\n'

    with open(os.path.join(new_file_path, new_file_name), 'w') as fp:
        for L in lines:
            fp.writelines(L)

        fp.close()

    return demand2049