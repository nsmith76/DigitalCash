'''
Customer 
Created by Noah Smith, Zach Cook and Chris Jansma 12/7/19.

'''
#Bank Keys
bankKeyN = 571
bankKeyD = 59 
bankKeyE = 29

#Library Imports
import sys
import random
import hashlib
import pickle

#Customer Class to be referenced by DigitalCash.py
class CustomerClass(object):
    def __init__(self, identity):
        print("Customer oject has been created")
        self.identity = identity
        
    #Method to Reveal Identiy Strings
    def revealIdentityStrings(self,nbitValue,MONUM):

        moneyOrder = []
        fileName = "BitCommitNums" + str(MONUM) + ".txt"
        with open(fileName) as inputfile:
            for line in inputfile:
                moneyOrder.append(line.strip())
        print(moneyOrder)
        firstRow = moneyOrder[0]
        fourthRowPAIR = moneyOrder[3]
        I11R = firstRow[1]
        
        I12S = fourthRowPAIR[3]
        I12S = fourthRowPAIR[1]
        
        returnMO = []
        if nbitValue == 0: 
            #Need to Obtain Left Half (I11R)
            I11R

        elif nbitValue == 1: 
            #Need to Obtain Right Half (I12S)
            I12S

    #Method to unblind Signed Money Orders
    def unblindSignedMO(self, moneyOrder):
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
        returnMO.append(int(valueofMO) ** bankKeyE % bankKeyN)
        returnMO.append(int(uniqueness) ** bankKeyE % bankKeyN)
        returnMO.append(int(I11R) ** bankKeyE % bankKeyN)
        returnMO.append(int(I11S) ** bankKeyE % bankKeyN)
        returnMO.append(int(I12R) ** bankKeyE % bankKeyN)
        returnMO.append(int(I12S) ** bankKeyE % bankKeyN)
        returnMO.append(int(I21R) ** bankKeyE % bankKeyN)
        returnMO.append(int(I21S) ** bankKeyE % bankKeyN)
        returnMO.append(int(I22R) ** bankKeyE % bankKeyN)
        returnMO.append(int(I22S) ** bankKeyE % bankKeyN)
        return returnMO

    #Method to Create a Money Order
    def createMO(self, valueOfMoneyOrder, IDofMO): 

        #Validation that a new unique uniquenessString was generated
        IDList = []
        with open ('custusedIDs.txt', 'rb') as var:
           IDList = pickle.load(var)
        uniquenessString = randomInt(100,500)
        while True:
            if uniquenessString in IDList: 
                uniquenessString = randomInt(100,500)
            else: 
                IDList.append(uniquenessString)
                break
            
        #Save UIDs to usedIDs.txt                                                
        with open('custusedIDs.txt', 'wb') as var:
            pickle.dump(IDList, var)

        #Start of new Base Money Order
        customerID = self.identity
        baseMoneyOrder = []
        baseMoneyOrder.append(valueOfMoneyOrder)
        baseMoneyOrder.append(uniquenessString)
        baseMoneyOrder.append(self.identity)
        #Output Base Money Order to File
        baseMOFileName = "BaseMO" + str(IDofMO+1) + ".txt"
        writeFile(baseMOFileName,baseMoneyOrder)

        #Secret Split MO Start
        secretSplitMO = []
        secretSplitMO.append(valueOfMoneyOrder)
        secretSplitMO.append(uniquenessString)
        I11 = getSecretSplitting(self)  
        I12 = getSecretSplitting(self) 
        I21 = getSecretSplitting(self)
        I22 = getSecretSplitting(self)
        secretSplit = []
        I11L = I11[0]
        I11R = I12[0]
        I12L = I21[0]
        I12R = I22[0]
        secretSplit.append([I11L,I11R])
        secretSplit.append([I12L,I12R])
        secretSplitMO.append(secretSplit)
        #OutputSSMO to File
        secretSplitMOFileName = "SecretSplitMO" + str(IDofMO+1) + ".txt"
        writeFile(secretSplitMOFileName,secretSplitMO)
        #OutputSSN to File
        secretSplitNumberMOFileName = "PRNG_SS" + str(IDofMO+1) + ".txt"
        writeFile(secretSplitNumberMOFileName,secretSplit)

        #Start of Bit Commitment
        BCRawOutput = []
        BCRawOutput =performBitCommitment(I11,I12,I21,I22)
        #Values Generated in BC
        BCOutput = BCRawOutput[0]
        #Random Numbers used in BC
        BCRANDNUMS = BCRawOutput[1]
        R111 = BCRANDNUMS[0]
        R112 = BCRANDNUMS[1]
        R121 = BCRANDNUMS[2]
        R122 = BCRANDNUMS[3]
        S111 = BCRANDNUMS[4]
        S112 = BCRANDNUMS[5]
        S121 = BCRANDNUMS[6]
        S122 = BCRANDNUMS[7]
        R211 = BCRANDNUMS[8]
        R212 = BCRANDNUMS[9]
        R221 = BCRANDNUMS[10]
        R222 = BCRANDNUMS[11]
        S211 = BCRANDNUMS[12]
        S212 = BCRANDNUMS[13]
        S221 = BCRANDNUMS[14]
        S222 = BCRANDNUMS[15]
        #Output PRNG Numbers
        randIntBCFileName = "PRNG_BC" + str(IDofMO+1) + ".txt"
        writeFile(randIntBCFileName,BCRANDNUMS)

        #BitCommitNumsn.txt
        bitCommingNumsFileName = "BitCommitNums" + str(IDofMO+1) + ".txt"
        R11 = I11[0]
        S11 = I11[1]
        R12 = I12[0]
        S12 = I12[1]
        I11R = BCOutput[0]
        I11S = BCOutput[1]
        I12R = BCOutput[2]
        I12S = BCOutput[3]
        BCNUMS = []
        BCNUMS.append([R11,I11R])
        BCNUMS.append([S11,I11S])
        BCNUMS.append([R12,I12R])
        BCNUMS.append([S12,I12S])
        writeFile(bitCommingNumsFileName,BCNUMS)   

        R21 = I21[0]
        S21 = I21[1]
        R22 = I22[0]
        S22 = I22[1]
        #BitCommitMOn.txt                       #Do we want to make output into Ciphertext? Yes 
        bitCommitFileName = "BitCommitMO" + str(IDofMO+1) + ".txt"
        BitCommitMO = []
        BitCommitMO.append(valueOfMoneyOrder)
        BitCommitMO.append(uniquenessString)
        BitCommitMO.append(R21)
        BitCommitMO.append(S21)
        BitCommitMO.append(R22)
        BitCommitMO.append(S22)
        BitCommitMO.append(R11)
        BitCommitMO.append(S11)
        BitCommitMO.append(R12)
        BitCommitMO.append(S12)
        writeFile(bitCommitFileName,BitCommitMO)

        #Start Of Blinding 
        blindedMO = blindMO(BitCommitMO)
        #BlindedMOn.txt                      #Do we want to make output into Ciphertext? Yes 
        blindedMOFileName = "BlindedMO" + str(IDofMO+1) + ".txt"
        writeFile(blindedMOFileName,blindedMO)

        #Start of Unblinding 
        unblindedMO = unblindMO(blindedMO)
        #UnblindedMOn.txt
        blindedMOFileName = "UnblindedMO" + str(IDofMO+1) + ".txt"
        writeFile(blindedMOFileName,unblindedMO)

        #Start of Reveal
        revealedMO = revealMO(unblindedMO,R11,R111,R112,S11,S111,S112,R12,R121,R122,S12,S121,S122,I11R,I12R,I11S,I12S,valueOfMoneyOrder,uniquenessString)
        #BitCommitRevealMOn.txt
        revealMOFileName = "BitCommitRevealMO" + str(IDofMO+1) + ".txt"
        writeFile(revealMOFileName,revealedMO)

        #Start of Joining
        joinedMO = joinMO(revealMO,R11,S11,valueOfMoneyOrder,uniquenessString)
        joinedFileName = "SecretJoinMO" + str(IDofMO+1) + ".txt"
        writeFile(joinedFileName,joinedMO)



#START OF CALLED CLASSES TO AID GENERATION OF FILES / NUMBERS 
def joinMO(MO,R11,S11,valueOfMoneyOrder,uniquenessString):
   Identity = R11^S11 
   returnMO = []
   returnMO.append(valueOfMoneyOrder)
   returnMO.append(uniquenessString)
   returnMO.append(Identity)
   return returnMO

#Method to Reveal a MO
def revealMO(MO,R11,R111,R112,S11,S111,S112,R12,R121,R122,S12,S121,S122,I11R,I12R,I11S,I12S,valueOfMoneyOrder,uniquenessString):
    VAR1 = [(I11R[0]^R111^R112),(I11S[0]^S111^S112)]
    VAR3 = [(I12R[0]^R121^R122),(I12S[0]^S121^S122)]
    returnList = []
    returnList.append(valueOfMoneyOrder)
    returnList.append(uniquenessString)
    returnList.append(VAR1)
    returnList.append(VAR3)
    return returnList


#Method to Unblind an MO
def unblindMO(MO):
    #BANK RSA KEY
    unblindedMO = []
    #Value
    unblindedMO.append(int(MO[0]) ** bankKeyD % bankKeyN) #Ciphertext number, does output have to be Characters?
    #Uniqueness
    unblindedMO.append(int(MO[1]) ** bankKeyD % bankKeyN) #Enhancement: Convert Numbers to Characters
    #R21
    unblindedMO.append(int(MO[2]) ** bankKeyD % bankKeyN)
    #S21
    unblindedMO.append(int(MO[3]) ** bankKeyD % bankKeyN)
    #R22
    unblindedMO.append(int(MO[4]) ** bankKeyD % bankKeyN)
    #S22
    unblindedMO.append(int(MO[5]) ** bankKeyD % bankKeyN)
    #R11
    unblindedMO.append(int(MO[6]) ** bankKeyD % bankKeyN)
    #S11
    unblindedMO.append(int(MO[7]) ** bankKeyD % bankKeyN)
    #R12
    unblindedMO.append(int(MO[8]) ** bankKeyD % bankKeyN)
    #S12
    unblindedMO.append(int(MO[9]) ** bankKeyD % bankKeyN)
    return unblindedMO

#Method to Blind an MO
def blindMO(MO):
    #BANK PUBLIC RSA KEY
    bankKeyE = 29
    bankKeyN = 571
    blindedMO = []
    #Value of MO 
    blindedMO.append(int(MO[0]) ** bankKeyE % bankKeyN) #Ciphertext number, does output have to be Characters?
    #Uniqueness
    blindedMO.append(int(MO[1]) ** bankKeyE % bankKeyN) #Enhancement: Convert Numbers to Characters
    #I11R
    blindedMO.append(int(MO[2]) ** bankKeyE % bankKeyN)
    #I11S
    blindedMO.append(int(MO[3]) ** bankKeyE % bankKeyN)
    #I12R
    blindedMO.append(int(MO[4]) ** bankKeyE % bankKeyN)
    #I12S
    blindedMO.append(int(MO[5]) ** bankKeyE % bankKeyN)
    #I21R
    blindedMO.append(int(MO[6]) ** bankKeyE % bankKeyN)
    #I21S
    blindedMO.append(int(MO[7]) ** bankKeyE % bankKeyN)
    #I22R
    blindedMO.append(int(MO[8]) ** bankKeyE % bankKeyN)
    #I22S
    blindedMO.append(int(MO[9]) ** bankKeyE % bankKeyN)
    return blindedMO

#Method to Perform Bit Commitment
def performBitCommitment(I11,I12,I21,I22):
    #0=R    1=S
    R11 = I11[0]
    S11 = I11[1]
    R12 = I12[0]
    S12 = I12[1]
    #0=R    1=S
    R21 = I21[0]
    S21 = I21[1]
    R22 = I22[0]
    S22 = I22[1]
        
    #Generate More Random Numbers
    R111 = randomNumberwithLength(len(str(R11)))
    R112 = randomNumberwithLength(len(str(R12)))
    R121 = randomNumberwithLength(len(str(R11)))
    R122 = randomNumberwithLength(len(str(R12)))
    S111 = randomNumberwithLength(len(str(S11)))
    S112 = randomNumberwithLength(len(str(S12)))
    S121 = randomNumberwithLength(len(str(S11)))
    S122 = randomNumberwithLength(len(str(S12)))
    R211 = randomNumberwithLength(len(str(R11)))
    R212 = randomNumberwithLength(len(str(R12)))
    S211 = randomNumberwithLength(len(str(R11)))
    S212 = randomNumberwithLength(len(str(R12)))
    R221 = randomNumberwithLength(len(str(S11)))
    R222 = randomNumberwithLength(len(str(S12)))
    S221 = randomNumberwithLength(len(str(S11)))
    S222 = randomNumberwithLength(len(str(S12)))

    #BC Money Order
    I11R = [(R11^R111^R112),R111]
    I11S = [(S11^S111^S112),S111]
    I12R = [(R12^R121^R122),R121]
    I12S = [(S12^S121^S122),S121]

    #BC Money Order
    I21R = [(R21^R211^R212),R211]
    I21S = [(S21^S211^S212),S211]
    I22R = [(R22^R221^R222),R221]
    I22S = [(S22^S221^S222),S221]

    outputValue = []
    outputValue.append(I11R)
    outputValue.append(I11S)
    outputValue.append(I12R)
    outputValue.append(I12S)
    #Second BC
    outputValue.append(I21R)
    outputValue.append(I21S)
    outputValue.append(I22R)
    outputValue.append(I22S)

    outputValue2 = []
    outputValue2.append(R111)
    outputValue2.append(R112)
    outputValue2.append(R121)
    outputValue2.append(R122)
    outputValue2.append(S111)
    outputValue2.append(S112)
    outputValue2.append(S121)
    outputValue2.append(S122)
    #Second BC
    outputValue2.append(R211)
    outputValue2.append(R212)
    outputValue2.append(R221)
    outputValue2.append(R222)
    outputValue2.append(S211)
    outputValue2.append(S212)
    outputValue2.append(S221)
    outputValue2.append(S222)

    returnValue = []
    returnValue.append(outputValue)
    returnValue.append(outputValue2)

    return returnValue

#Method to Perform Secret Splitting
def getSecretSplitting(self):
    R = randomNumberwithLength(len(str(self.identity)))
    S = R ^ self.identity
    returnList = [R,S]
    return(returnList)

#Custom Methods for Easy Data Export
def randomNumberwithLength(length):
    lower = 10**(length-1)
    upper = 10**length - 1
    return random.randint(lower, upper)
        
#Method to Write Lists to New FIle Lines
def writeFile(fileName,outputList):  
    outFile = open(fileName,"w")                 
    for value in outputList:
        outFile.write(str(value)+ '\n')
    outFile.close()

#Method to Create Ints between two numbers easily
def randomInt(min,max):
    randomNumber = random.randint(min,max)
    return int(randomNumber)
