from music21 import *

def getMidiFile():
    fileName = input("Input midi file name: ")

    music = converter.parse(fileName)
    music.show()

getMidiFile()
