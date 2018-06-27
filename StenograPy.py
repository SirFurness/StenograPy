# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:49:21 2018
@author: Joel Velez and Eric Paul
"""

def getInputString():
  return input("Please input the string to encode:\n")

def convertStringToBinary(input):
  a_bytes = bytes(s, "ascii")
  b = ' '.join(["{0:b}".format(x) for x in a_bytes])
  return b

def getInputFilename():
  return input("Input the name of the input file (with extension):\n")

def getOutputFilename():
  return input("Input the name of the output file (with extension):\n")

def encodeFile(binary, inputFilename, outputFilename):
  with open(inputFilename, "rb") as inputFile, open(outputFilename, "w") as outputFile:
    currentBit = 0
    byte = inputFile.read(1)
    while byte:
      encodedByte = encodeByte(byte, binary[currentBit])
      outputFile.write(encodedByte)
      currentBit += 1
      byte = inputFile.read(1)

def encodeByte(byte, bit):
  if bit == 0:
    return bytes(byte[0] & b'\xfe'[0])
  else:
    return bytes(byte[0] | b'\xff'[0])


if __name__ == "__main__":
  input = getInputString()
  binary = convertStringToBinary(input)

  inputFilename = getInputFilename()
  outputFilename = getOutputFilename()

  encodeFile(binary, inputFilename, outputFilename)
