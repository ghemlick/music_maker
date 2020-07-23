# music_maker

Music Maker Python Project

Designed by Gabrielle Hemlick

Summer 2018


## Desired Input and Output

Input:
1. Ask user for a key signature
2. Ask user for a time signature
3. Ask user for a number of measures

Output:

Melody

Example: if there are 4 measures of 3/4 in D, it should print 12 notes in the key of D. 



## Provided Data

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





## Steps to get started
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


## Hint

-	The code above the comment line is the “source code” and the code below the line is what the user will see. I made a function to handle the key signature. 
-	See if you can make functions to handle the time signature and number of measures. 

import random

C = ["C", "D", "E", "F", "G", "A", "B"]

G = ["G", "A", "B", "C", "D", "E", "F#"]

D = ["D", "E", "F#", "G", "A", "B", "C#"]

A = ["A", "B", "C#", "D", "E", "F#", "G#"]

E = ["E", "F#", "G#", "A", "B", "C#", "D#"]

B = ["B", "C#", "D#", "E", "F#", "G#", "A#"]

Fsharp = ["F#", "G#", "A#", "B", "C#", "D#", "E#"]

Csharp = ["C#", "D#", "E#", "F#", "G#", "A#", "B#"]

notes = []

def get_keysignature(input_key):

  if input_key == "C":
  
    notes = C
    
    return notes
    
  elif input_key == "G":
  
    notes = G
    
    return notes
    
  elif input_key == "D":
  
    notes = D
    
    return notes
    
  elif input_key == "A":
  
    notes = A
    
    return notes
    
  elif input_key == "E":
  
    notes = E
    
    return notes
    
  elif input_key == "B":
  
    notes = B
    
    return notes
    
  elif input_key == "F#":
  
    notes = Fsharp
    
    return notes
    
  elif input_key == "C#":
  
    notes = Csharp
    
    return notes
    
  else:
  
    print("Error: please enter a valid key signature.")
    
    return "ERROR"

time = input("Enter a time signature:")

beats = 0

if time == "2/4":

    beats = 2
  
elif time == "3/4":

    beats = 3
  
elif time == "4/4":

    beats = 4
  
else:

    print("Error: please enter a valid time signature.")

measures = int(input("Enter a number of measures between 1-16:"))

for i in range(measures * beats):

    print(notes[random.randint(0, 6)])

##############################################################

key_inputted = raw_input("Enter a key signature:")

key = get_keysignature(key_inputted)
