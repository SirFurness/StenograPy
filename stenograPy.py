# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:49:21 2018
@author: Joel Velez and Eric Paul
"""

def getInputFilename():
  return input("Input the name of the input file (with extension):\n")

def getOutputFilename():
  return input("Input the name of the output file (with extension):\n")

def getInputString():
  return input("Please input the string to encode:\n")

def turnStringOfBinaryIntoListOfInts(b):
  outputList = []
  for char in b:
    if char == '0' or char == '1':
      outputList.append(int(char))
  return outputList

def insertStr(string, strToInsert, index):
    return string[:index] + strToInsert + string[index:]

def findWhereZeroesMustBeAdded(bytesSeparatedBySpace):
  currentByteLength = 0
  currentByteStartIndex = 0
  locationsToChange = []
  for index in range(len(bytesSeparatedBySpace)):
    if bytesSeparatedBySpace[index] == ' ' and currentByteLength < 8:
      locationsToChange.append((8-currentByteLength, currentByteStartIndex))
      currentByteStartIndex = index+1
      currentByteLength = 0
    elif index == len(bytesSeparatedBySpace)-1 and currentByteLength < 7:
      locationsToChange.append((7-currentByteLength, currentByteStartIndex))
    else:
      currentByteLength += 1
  return locationsToChange

def addZeroesAtEachLocation(locationsToChange, bytesSeparatedBySpace):
  zeroesAdded = 0
  output = bytesSeparatedBySpace
  for (zeroesToBeAdded, oldIndex) in locationsToChange:
    index = oldIndex + zeroesAdded
    stringToBeAdded = "0" * zeroesToBeAdded
    output = insertStr(output, stringToBeAdded, index)
    zeroesAdded += zeroesToBeAdded
  return output

def makeBytesLengthEight(bytesSeparatedBySpace):
  locationsToChange = findWhereZeroesMustBeAdded(bytesSeparatedBySpace)
  output = addZeroesAtEachLocation(locationsToChange, bytesSeparatedBySpace)
  return output

def convertStringToBinary(input):
  byteList = bytes(input, "ascii")
  bytesSeparatedBySpace = ' '.join(["{0:b}".format(x) for x in byteList])
  formatedBytesSeparatedBySpace = makeBytesLengthEight(bytesSeparatedBySpace)
  listOfInts = turnStringOfBinaryIntoListOfInts(formatedBytesSeparatedBySpace)
  return listOfInts

def encodeFile(binary, inputFilename, outputFilename):
  with open(inputFilename, "rb") as inputFile, open(outputFilename, "wb") as outputFile:
    currentBit = 0
    byte = inputFile.read(1)
    while byte:
      if currentBit < len(binary):
        encodedByte = encodeByte(byte, binary[currentBit])
        outputFile.write(encodedByte)
        currentBit += 1
      else:
        encodedByte = encodeByte(byte, 0)
        outputFile.write(encodedByte)
      byte = inputFile.read(1)

def encodeByte(byte, bit):
  if bit == 0:
    return bytes([byte[0] & 254])
  else:
    return bytes([byte[0] | 1])

def encode():
  inputString = getInputString()
  binary = convertStringToBinary(inputString)

  inputFilename = getInputFilename()
  outputFilename = getOutputFilename()

  encodeFile(binary, inputFilename, outputFilename)

def decodeFile(filename):
  binary = ""
  output = ""
  with open(filename, "rb") as inputFile:
    byte = inputFile.read(1)
    bitsProcessed = 0
    while byte:
      if bitsProcessed == 8:
        if int(binary,2) == 0:
          break
        output += chr(int(binary, 2))
        binary = ""
        bitsProcessed = 0
      decodedByte = decodeByte(byte)
      binary += decodedByte
      byte = inputFile.read(1)
      bitsProcessed += 1
  print(output)

def decodeByte(byte):
  return str(byte[0] & 1)

def decode():
  filename = input("Input the name of the file (with extension):\n")

  decodeFile(filename)

if __name__ == "__main__":
  choice = input("E to encode, D to decode")
  if choice == "E":
    encode()
  elif choice == "D":
    decode()
