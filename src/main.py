import xml.etree.ElementTree as ET
from io import StringIO

# Create the root element
score_partwise = ET.Element("score-partwise", version="4.0")

# Create the part-list element
part_list = ET.SubElement(score_partwise, "part-list")

# Create the score-part element
score_part = ET.SubElement(part_list, "score-part", id="P1")
part_name = ET.SubElement(score_part, "part-name")
part_name.text = "Music"

# Create the part element
part = ET.SubElement(score_partwise, "part", id="P1")

# Create the first measure
measure = ET.SubElement(part, "measure", number="1")

# Create the attributes for the measure
attributes = ET.SubElement(measure, "attributes")

# Divisions element
divisions = ET.SubElement(attributes, "divisions")
divisions.text = "1"

# Key element
key = ET.SubElement(attributes, "key")
fifths = ET.SubElement(key, "fifths")
fifths.text = "0"

# Time element
time = ET.SubElement(attributes, "time")
beats = ET.SubElement(time, "beats")
beats.text = "4"
beat_type = ET.SubElement(time, "beat-type")
beat_type.text = "4"

# Clef element
clef = ET.SubElement(attributes, "clef")
sign = ET.SubElement(clef, "sign")
sign.text = "G"
line = ET.SubElement(clef, "line")
line.text = "2"

# Create a note
note = ET.SubElement(measure, "note")

# Pitch element
pitch = ET.SubElement(note, "pitch")
step = ET.SubElement(pitch, "step")
step.text = "C"
octave = ET.SubElement(pitch, "octave")
octave.text = "4"

# Duration element
duration = ET.SubElement(note, "duration")
duration.text = "4"

# Type element
note_type = ET.SubElement(note, "type")
note_type.text = "whole"

# Create the XML tree from the root
tree = ET.ElementTree(score_partwise)

# Create a string buffer to write the XML content
xml_str = StringIO()

# Write the DOCTYPE declaration followed by the XML tree to the buffer
xml_str.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
xml_str.write('<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "partwise.dtd">\n')
tree.write(xml_str, encoding="UTF-8", xml_declaration=False)

# Get the XML string
xml_content = xml_str.getvalue()

# Write the XML content to a file
with open("musicxml_example_with_doctype.xml", "w", encoding="UTF-8") as file:
    file.write(xml_content)

print("XML file with DOCTYPE has been created successfully.")
