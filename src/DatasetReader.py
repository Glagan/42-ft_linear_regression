import csv
import src.Normalizer as nm


def read(path):
    oX = []
    oY = []
    with open(path) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        header = False
        for row in csvReader:
            if header == False:
                header = True
                continue
            oX.append(float(row[0]))
            oY.append(float(row[1]))
    X = nm.minMaxNormalizeList(oX, min(oX), max(oX))
    Y = nm.minMaxNormalizeList(oY, min(oY), max(oY))
    return oX, oY, X, Y
