def encode(df, column, maxValue):
    resDict = {}
    resOrder = []
    for i in df.index:
        totColumn = str(df.at[i,column])
        totColumn = totColumn.split(",")
        for j in totColumn:
            if j == 'nan':
                j = 'None'
            j = j.strip()

            if column == 'publisher':
                j += ' (Publisher)'
            if column == 'developer':
                j += ' (Developer)'
            if j not in resDict.keys():
                resDict[j] = 1
            else:
                resDict[j] += 1

    for i in sorted(resDict, key = resDict.get,reverse = True):
        if len(resOrder) < maxValue: 
            resOrder.append(i)

    for u in resOrder:
        for i in df.index:
            col = str(df.at[i,column])
            col = col.split(',')
            if u in col:
                df.at[i,u] = 1
            else: df.at[i,u] = 0   
    
    return df

def calcValue(df, column):
    resDict = {}
    
    for i in df.index:
        totColumn = str(df.at[i,column])
        totColumn = totColumn.split(",")
        for j in totColumn:
            if len(j) > 0:
                if j == 'nan':
                    j = 'None'
                j = j.strip()
                if column == 'publisher':
                    j += ' (Publisher)'
                if column == 'developer':
                    j += ' (Developer)'
                if j not in resDict.keys():
                    resDict[j] = 1
                else:
                    resDict[j] += 1

    for i in sorted(resDict, key = resDict.get):
        print(i, resDict[i])