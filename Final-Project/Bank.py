'''
Bank 
Created by Noah Smith, Zach Cook and Chris Jansma 12/7/19.
'''

import random
import pickle

#Bank Keys
bankKeyE = 29
bankKeyN = 571
bankKeyD = 59 

#Created Bank Class
class BankClass(object):
    def __init__(self):
        print("Bank oject has been created")

    #Method to validate that a MO's uniqueness hasn't been duplicated
    def validateUID(self, UMOID):
        returnStr = ''
        with open ('bankusedIDs.txt', 'rb') as var:
            IDList = pickle.load(var)
            if UMOID in IDList: 
                returnStr = "Failure! This MO has been used before."
            else: 
                returnStr = "Success! No match. This is a new MO."
                                                           
        with open('bankusedIDs.txt', 'wb') as var:
            pickle.dump(IDList, var)
        return returnStr

    #Method of Bank Signing the Blinded MO 
    def blindSignatureProtocol(self, orderNumber):
        moneyOrder = []
        fileName = "BlindedMO" + str(orderNumber) + ".txt"
        with open(fileName) as inputfile:
            for line in inputfile:
                moneyOrder.append(line.strip())
        valueofMO = moneyOrder[0]
        uniqueness = moneyOrder[1]
        I11R = int(moneyOrder[2])
        I11S = int(moneyOrder[3])
        I12R = int(moneyOrder[4])
        I12S = int(moneyOrder[5])
        I21R = int(moneyOrder[6])
        I21S = int(moneyOrder[7])
        I22R = int(moneyOrder[8])
        I22S = int(moneyOrder[9])

        returnMO = []
        #Value of Money Order
        returnMO.append(int(valueofMO)**bankKeyD%bankKeyN)
        returnMO.append(int(uniqueness)**bankKeyD%bankKeyN)
        returnMO.append(int(I11R)**bankKeyD%bankKeyN)
        returnMO.append(int(I11S)**bankKeyD%bankKeyN)
        returnMO.append(int(I12R)**bankKeyD%bankKeyN)
        returnMO.append(int(I12S)**bankKeyD%bankKeyN)
        returnMO.append(int(I21R)**bankKeyD%bankKeyN)
        returnMO.append(int(I21S)**bankKeyD%bankKeyN)
        returnMO.append(int(I22R)**bankKeyD%bankKeyN)
        returnMO.append(int(I22S)**bankKeyD%bankKeyN)
        return returnMO