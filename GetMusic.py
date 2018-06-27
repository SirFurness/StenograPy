import music21 as m21
import sys

def addMidiExtension(fileName):
    if fileName[len(fileName)-4:] == ".mid":
        return fileName
    return fileName+".mid"
    
def getMidiFile():
    fileName = input("Input midi file name: ")

    name = addMidiExtension(fileName)
    
    try:
        music = m21.converter.parse(name)
        return music
    except:
        print("Could not open midi file!")
        getMidiFile()