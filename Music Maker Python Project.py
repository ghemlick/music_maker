""" 
Music Maker Python Project
Designed by Gabrielle Hemlick
For use by The Coding School
Summer 2018


*Desired Input and Output*

Input:
1. Ask user for a key signature
2. Ask user for a time signature
3. Ask user for a number of measures

Output:
Melody
Example: if there are 4 measures of 3/4 in D, it should print 12 notes in the key of D. 



*Provided Data*

Key Signatures as Lists:
C = ["C", "D", "E", "F", "G", "A", "B"]
G = ["G", "A", "B", "C", "D", "E", "F#"]
D = ["D", "E", "F#", "G", "A", "B", "C#"]
A = ["A", "B", "C#", "D", "E", "F#", "G#"]
E = ["E", "F#", "G#", "A", "B", "C#", "D#"]
B = ["B", "C#", "D#", "E", "F#", "G#", "A#"]
Fsharp = ["F#", "G#", "A#", "B", "C#", "D#", "E#"]
Csharp = ["C#", "D#", "E#", "F#", "G#", "A#", "B#"]

Time signatures:
2/4
3/4
4/4

Number of Measures:
1-16




*Steps to get started*
1.	Try figuring out the logic of this project on paper.
Example: 
1. ask for inputs
...
...
6. Use for loop
2.	Ask the user for a key, time, and number of measures. Store these values.
3.	Create an empty list called notes: 
notes = []
4.	Write a group of conditional statements for the key signature to determine what key was inputted. When the computer reaches the correct key in your group of conditionals, assign the premade list of notes in the given key to your empty notes list. 
5.	If the user did not input one of our premade keys, print 
"Error: please enter a valid key signature."


"""









# *Solution*

import random


# POSSIBLE SCALES

C = ["C", "D", "E", "F", "G", "A", "B"]
G = ["G", "A", "B", "C", "D", "E", "F#"]
D = ["D", "E", "F#", "G", "A", "B", "C#"]
A = ["A", "B", "C#", "D", "E", "F#", "G#"]
E = ["E", "F#", "G#", "A", "B", "C#", "D#"]
B = ["B", "C#", "D#", "E", "F#", "G#", "A#"]
Fsharp = ["F#", "G#", "A#", "B", "C#", "D#", "E#"]
Csharp = ["C#", "D#", "E#", "F#", "G#", "A#", "B#"]


# INPUT: key signature
# OUTPUT: list of notes in desired key

def set_scale(input_key):
  if input_key == "C":
    return C
  elif input_key == "G":
    return G
  elif input_key == "D":
    return D
  elif input_key == "A":
    return A
  elif input_key == "E":
    return E
  elif input_key == "B":
    return B
  elif input_key == "F#":
    return Fsharp
  elif input_key == "C#":
    return Csharp
  else:
    print("Error: please enter a valid key signature.")
    return "ERROR"



# INPUT: time signature
# OUTPUT: number of beats per measure

def set_meter(time_sig):
  if time_sig == "2/4":
    return 2
  elif time_sig == "3/4":
    return 3
  elif time_sig == "4/4":
    return 4
  else:
    print("Error: please enter a valid time signature.")



# USER INPUTS

key_inputted = raw_input("Enter a key signature:")
scale = set_scale(key_inputted)

time_sig = raw_input("Enter a time signature:")
beats = set_meter(time_sig)

measures = int(raw_input("Enter a number of measures between 1-16:"))



# PRINTING NOTES

for i in range(measures * beats):
  print(scale[random.randint(0, 6)])

