'''
Digital Cash
Created by Noah Smith, Zach Cook and Chris Jansma 12/7/19.

Usage of Program: 
python3 DigitalCash.py 

Limitations: 
Money Order Amount can only be whole dollar values.
Values cannot be over the number of 571.
'''

#Team Created Classes
import Customer
import Bank
import Merchant
import random

identity = int(input("Please enter your ID: "))
numOfMoneyOrders = int(input("How many money orders would you like to make today?: "))
valueofMO = []

#definitions 
def writeFile(fileName,outputList):  
    outFile = open(fileName,"w")                 
    for value in outputList:
        outFile.write(str(value)+ '\n')
    outFile.close()

#Start of Program
Alice = Customer.CustomerClass(identity=identity)
Bob = Bank.BankClass()
Merchant = Merchant.MerchantClass() 

for i in range(numOfMoneyOrders):
    inputVal = int(input("What is the value of the Money Order " + str((i+1)) + "?: "))
    valueofMO.append(inputVal)

for i in range(numOfMoneyOrders):
    Alice.createMO(valueOfMoneyOrder=valueofMO[i],IDofMO=i)

#Pick Random MO Number between 1 and numofMoneyOrders
randomMO = random.randint(1,numOfMoneyOrders)

#Blind Signature Money Order
signedMO = Bob.blindSignatureProtocol(randomMO)
signedMOFileName = "SignedBlindedMO" + str(randomMO) + ".txt"
writeFile(signedMOFileName,signedMO)

unblindSignedMOFileName = "SignedUnblindedMO" + str(randomMO) + ".txt"
unblindSignedMO = Alice.unblindSignedMO(signedMO)
writeFile(unblindSignedMOFileName,unblindSignedMO)

merchantUnblindFileName = "MerchantUnblind" + str(randomMO) + ".txt"
merchantUnblindMO = Merchant.unblindSignedMO(signedMO)
writeFile(merchantUnblindFileName,merchantUnblindMO)
if merchantUnblindMO == unblindSignedMO:
    print("Success! The signature is valid.")
else: 
    print("Failure! The signature is NOT valid.")

print(Bob.validateUID(unblindSignedMO[1]))

nbitval = Merchant.generatenBitValue()
Alice.revealIdentityStrings(nbitValue=nbitval,MONUM=randomMO)