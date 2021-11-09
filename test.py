test = "Pixel GraphicsExplorationRoguelikeTurn-Based StrategySingleplayerDynamic NarrationProcedural GenerationRogueliteIndieStory RichChoices MatterHex GridDinosaursLovecraftianModdableStrategyLootAdventure2DRetro"
test2 = "FPSShooterMultiplayerCompetitiveActionTeam-BasedeSportsTacticalFirst-PersonPvPOnline Co-OpCo-opStrategyMilitaryWarDifficultTradingRealisticFast-PacedModdable"
res = ""
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
number = '0123456789'
flag = False
counter = 0

for i in test2:
    if counter != 0:
        if i == " " or i == '-':
            flag = True
            res += i
        elif i in number:
            if test2[counter+1] in number and test2[counter-1] not in number:
                res += ','
                res += i
            elif (test2[counter+1] in number or test2[counter+1] == "'") and test2[counter-1] in number:
                res += i
            else:
                
                res += ','
                res += i
                flag = True
        elif i in uppercase and flag == True:
            flag = False
            res += i
        elif i in uppercase and flag == False:
            if test2[counter+1] == 'P' and i == 'R':
                res += ','
                res += i
            elif i == 'P' and test2[counter+1] == 'G':
                res += i
            elif i == 'G' and test2[counter-1] == 'P':
                res += i
            else:
                res += ","
                res += i
        else:
            flag = False
            res += i
        counter += 1
    else:
        res += i
        counter += 1
print(res)
    
