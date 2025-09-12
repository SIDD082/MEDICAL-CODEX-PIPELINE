import pandas as pd
from common_functions import makeTimestamp, cleanText, readLines, rowsToCsv

# I read the whole file and split by spaces. I keep code and description.

def buildRows(linesList):
    rowsList = []
    stampText = makeTimestamp()
    indexNumber = 0
    while indexNumber < len(linesList):
        lineText = linesList[indexNumber]
        lineText = lineText.rstrip('\n')
        if lineText.strip() == "":
            indexNumber = indexNumber + 1
            continue
        partsList = lineText.split()
        if len(partsList) >= 4:
            codeText = partsList[1].upper()
            descriptionParts = partsList[3:]
            descriptionText = " ".join(descriptionParts)
            descriptionText = cleanText(descriptionText)
            if descriptionText == "":
                indexNumber = indexNumber + 1
                continue
            rowMap = {"code": codeText, "description": descriptionText, "last_updated": stampText}
            rowsList.append(rowMap)
        indexNumber = indexNumber + 1
    return rowsList

def main():
    inputPathText = 'data/icd10cm_order_2026.txt'
    tryFile = False
    tryFileObject = None
    try:
        tryFileObject = open(inputPathText, 'r', encoding='utf-8')
        tryFile = True
        tryFileObject.close()
    except:
        print("file missing icd10cm")
    if tryFile == False:
        return
    linesList = readLines(inputPathText)
    rowsList = buildRows(linesList)
    if len(rowsList) == 0:
        print("no rows icd10cm")
        return
    rowsToCsv(rowsList, 'output/csv/icd10cm_clean.csv')
    print("done icd10cm")

if __name__ == "__main__":
    main()
