from datetime import datetime
import pandas as pandasLibrary

def makeTimestamp():
    return datetime.now().isoformat(timespec="seconds")

def cleanText(textValue):
    if textValue is None:
        return ""
    textString = str(textValue)
    textString = textString.strip()
    return textString

def readLines(filePathText):
    try:
        fileObject = open(filePathText,'r',encoding='utf-8')
        linesList = fileObject.readlines()
        fileObject.close()
        return linesList
    except:
        print("file missing " + filePathText)
        return []

def rowsToCsv(rowsList, outPathText):
    data_Df = pandasLibrary.DataFrame(rowsList, columns=["code","description","last_updated"])
    data_Df.to_csv(outPathText, index=False)