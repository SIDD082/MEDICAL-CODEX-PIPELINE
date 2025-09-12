import pandas as pandasLibrary
from common_functions import makeTimestamp, cleanText, readLines

def parseLines(linesList):
    rowsList = []
    stampText = makeTimestamp()
    headerDone = False
    indexNumber = 0
    while indexNumber < len(linesList):
        lineText = linesList[indexNumber]
        rawText = lineText.strip()
        if rawText == "":
            indexNumber = indexNumber + 1
            continue
        if '|' in rawText:
            partsList = rawText.split('|')
        else:
            partsList = rawText.split('\t')
            if len(partsList) == 1:
                partsList = rawText.split()
        if headerDone == False:
            headerDone = True
            if len(partsList) > 0:
                firstValue = partsList[0]
                if firstValue.isdigit() == False:
                    indexNumber = indexNumber + 1
                    continue
        if len(partsList) >= 8:
            conceptId = cleanText(partsList[4]) if len(partsList) > 4 else ""
            activeText = cleanText(partsList[2]) if len(partsList) > 2 else ""
            termIndex = 7
            if len(partsList) <= 7:
                termIndex = len(partsList) - 2
            if termIndex >= 0:
                termText = cleanText(partsList[termIndex])
                if activeText == '1':
                    if conceptId != "" and termText != "":
                        rowMap = {"code": conceptId, "description": termText, "last_updated": stampText}
                        rowsList.append(rowMap)
        indexNumber = indexNumber + 1
    return rowsList

def main():
    inputPathText = 'input\sct2_Description_Full-en_US1000124_20250301.txt'
    linesList = readLines(inputPathText)
    rowsList = parseLines(linesList)
    if len(rowsList) == 0:
        print("no rows snomed")
        return
    data_Df = pandasLibrary.DataFrame(rowsList, columns=["code","description","last_updated"])
    data_Df.to_csv('output/csv/snomed_clean.csv', index=False)
    # write a smaller file separately so I can open it easier
    if len(rowsList) > 20000:
        smallList = rowsList[0:20000]
        small_Df = pandasLibrary.DataFrame(smallList, columns=["code","description","last_updated"])
        small_Df.to_csv('output/csv/snomed_clean_small.csv', index=False)
        print("made small snomed file")
    print("done snomed")

if __name__ == "__main__":
    main()
