from music21 import *
def write(filename):
  
     me = MidiEvent(mt)
     me.type = "NOTE_ON"
     me.channel = 1
     me.time = None #d
     me.pitch = p
     me.velocity = v
     mt.events.append(me)
