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

song_staffs = {}

for idx, m in enumerate(song_measures):
    chords = m[0].replace(")", "").split("(")
    chords.pop(0)
    notes = m[1].replace("]", "").split("[")
    notes.pop(0)

    measures = {}
    for midx, mdata in enumerate(chords):
        data = [mdata, notes[midx]]
        measures[f"Measure {str(midx + 1)}"] = data

    song_staffs[f"Staff {str(idx + 1)}"] = measures


score = stream.Score()
part = stream.Part()

score.insert(metadata.Metadata())
score.metadata.title = song_title
score.metadata.composer = song_composer

part.append(clef.TrebleClef())
part.append(key.KeySignature(song_key))
part.append(meter.TimeSignature(song_time))

for k, v in song_staffs.items():
    for m in v.values():
        m_chords, m_notes = m[0].split(), m[1].split()
        measure = stream.Measure()
        
        for idx, n in enumerate(m_notes):
            if n == "RS":
                measure.leftBarline = bar.Repeat(direction="start")
            elif n == "RE":
                measure.rightBarline = bar.Repeat(direction="end")
            elif n == "CODA":
                measure.append(repeat.Coda())
            elif n == "ToCoda":
                measure.append(expressions.TextExpression("To Coda"))
            elif n == "NEW":
                measure.append(layout.SystemLayout(isNew=True))
            elif n == "RDB":
                measure.rightBarline = bar.Barline("double")
            elif n == "LDB":
                measure.leftBarline = bar.Barline("double")
            elif n == "FB":
                measure.rightBarline = bar.Barline("final")
            else:
                pitch, length = n.split("/")
                length = float(length)
                if pitch == "rest":
                    measure.append(note.Rest(quarterLength=length))
                else:
                    measure.append(note.Note(pitch, quarterLength=length))
        
        part.append(measure)

score.append(part)
# score.show("musicxml.pdf")