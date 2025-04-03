from music21 import *

notation_file = "src/notation.txt"

notation_text = open(notation_file, "r", encoding="utf-8")

keys = {
    "C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5, "F#": 6, "C#": 7,
    "F": -1, "Bb": -2, "Eb": -3, "Ab": -4, "Db": -5, "Gb": -6, "Cb": -7
}

raw_song_measures = []

for idx, line in enumerate(notation_text.readlines()):
    if "Title: " in line:
        song_title = line[7:].strip()
    if "Composer: " in line:
        song_composer = line[10:].strip()
    
    if "Tempo: " in line:
        song_tempo = int(line[7:].strip())
    if "Swing: " in line and "True" in line:
        song_swing = True
    elif "Swing: " in line and "False" in line:
        song_swing = False
    
    if "Key: " in line:
        song_key = keys[line[5:].strip()]
    if "Time: " in line:
        song_time = line[6:].strip()
    
    if idx >= 11 and line.strip() != "":
        raw_song_measures.append(line.strip())

song_measures = []

for idx in range(0, len(raw_song_measures), 2):
    chords_notes = []
    chords_notes.append(raw_song_measures[idx])
    chords_notes.append(raw_song_measures[idx + 1])
    song_measures.append(chords_notes)

for m in song_measures:
    chords = m[0].replace(")", "").split("(")
    chords.pop(0)
    notes = m[1].replace("]", "").split("[")
    notes.pop(0)
    print(chords, notes)