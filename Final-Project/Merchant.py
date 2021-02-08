'''
Merchant 
Created by Noah Smith, Zach Cook and Chris Jansma 12/7/19.
'''

#Library Imports
import random 

#Bank Keys
bankKeyE = 29
bankKeyN = 571
bankKeyD = 59

#Merchant Class to be Called by DigitalCash.py
class MerchantClass(object):
    def __init__(self):
        print("Merchant oject has been created")
        
    #Method to Generate n-bit value
    def generatenBitValue(self):
        value = random.randint(0,1)
        return value

    #Method for Merchant to Unblined the Signed Money Order
    def unblindSignedMO(self, MO):
        #BANK RSA KEY
        unblindedMO = []
        #Money Order Value $$$
        unblindedMO.append(int(MO[0]) ** bankKeyE % bankKeyN) 
        #Uniqueness
        unblindedMO.append(int(MO[1]) ** bankKeyE % bankKeyN) 
        #R21
        unblindedMO.append(int(MO[2]) ** bankKeyE % bankKeyN)
        #S21
        unblindedMO.append(int(MO[3]) ** bankKeyE % bankKeyN)
        #R22
        unblindedMO.append(int(MO[4]) ** bankKeyE % bankKeyN)
        #S22
        unblindedMO.append(int(MO[5]) ** bankKeyE % bankKeyN)
        #R11
        unblindedMO.append(int(MO[6]) ** bankKeyE % bankKeyN)
        #S11
        unblindedMO.append(int(MO[7]) ** bankKeyE % bankKeyN)
        #R12
        unblindedMO.append(int(MO[8]) ** bankKeyE % bankKeyN)
        #S12
        unblindedMO.append(int(MO[9]) ** bankKeyE % bankKeyN)
        return unblindedMO