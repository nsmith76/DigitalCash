# Digital Cash Project

## Objective:
To implement a protocol for the use of electronic cash using various protocols for maintaining secrecy, anonymity, authenticity, integrity, and mutual trust.


## Installation

Download this repository:
```bash
git clone https://github.com/nsmith76/DigitalCash
cd DigitalCash/Final-Project/
```

## Usage Input

```bash
$ python3 DigitalCash.py
     Please enter your ID: <user input>
     How many money orders would you like to make today?: <user input>
     What is the value of Money Order X?: <user input> 
```

## Expected Outputs

#### Text File Outputs n Replaced with Money Order Number in FileName
BaseMO1.txt, BaseMO2.txt, BaseMO3.txt representing three base money orders containing the amount and customer ID and different uniqueness strings.

PRNG_SSn.txt containing the pseudo-random integers used in the secret-splitting protocol

SecretSplitMOn.txt representing the split base money order

PRNG_BCn.txt containing the pseudo-random integers used in the bit commitment protocol

BitCommitNumsn.txt containing the two pseudo-random integers, actual value  used in the bit commitment protocol

BitCommitMOn.txt representing the bit-committed money order

BlindedMOn.txt representing the blinded money order

UnblindedMOn.txt representing the unblinded money order

BitCommitRevealMOn.txt representing the revealed bit-committed money order

SecretJoinMOn.txt representing the joined money order.

SignedUnblindedMOn.txt representing the signed unblinded money order

--- UsedMOn.txt with revealed halves of the identity string.

SignedBlindedMOn.txt representing the signed blinded money order.

### Console Outputs

Message displaying if the signature is valid or not.

Message displaying if the money order has been used before or not.

Message displaying if the bank’s signature is valid or not.

### Known Limitations 
Money order value's cannot be larger than 571. 
Program can only have 571 runs before reduplication of unique money order IDs. 
The money order value can only be a whole dollar amount, no decimal. 

## License
[MIT]https://choosealicense.com/licenses/mit/
