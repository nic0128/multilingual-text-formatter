"""
This program formats song lyrics (or any transcript) written in a
non-English writing system into blocks that combine the original
text, its Romanized transcription and its English translation.
The program takes three text files as input:
(1) The original lyrics in a writing script other than English
    (e.g. Japanese, Chinese, Korean, etc.)
(2) A Romanized version of those lyrics
(3) the English translation.
Each text file is assumed to have each line of text correspond to
the same line across all files. 
The program outputs a new text file in the following format:

<Romanized line>
<Original line>
<English translation> 

<Romanized line>
<Original line>
<English translation>  

..... repeated for all remaining lines 

The program also ensures that all input files contain the same
number of lines and accounts for cases where certain lines may be
identical across files (ex. K-pop & J-pop often have English lines,
which do not need translation & romanization). This program is
intended to be used for adding custom lyrics to music files,
preparing lyrics for lyric videos, or preparing references for
studying another language, all of which are tasks that would be
time-consuming to do manually.

"""

import os

# ensures required directories exist exists
os.makedirs("output", exist_ok=True)
os.makedirs("inputs", exist_ok=True)

# creates required input files if they don't exist
with open("inputs/original.txt", "a"):
    pass
with open("inputs/romanized.txt", "a"):
    pass
with open("inputs/translated.txt", "a"):
    pass

# reads lines in text file, ensures they're not empty
def line_format(txt_file):
    try:
        with open(txt_file, "r") as file:
            lines = file.readlines()
            
            if len(lines) == 0:
                raise ValueError(f"The file \"{txt_file}\" is empty. Please add text.")

            return lines

    except:
        raise ValueError("One or more input files cannot be read. Make sure inputs are not empty and are valid.")

# If all three lines are identical only include one (used only for comparison)
def check_identical(line):
    cleaned = ""
    index = 0
    
    while index < len(line):
        if line[index].isalnum(): # only includes alphanumeric characters in comparison
            cleaned += line[index].lower()
        index += 1
    
    # lines are considered identical when their 'cleaned' versions (without punctuation, special chars...) are the same
    return cleaned

# groups lines for output
def lines_grouping():
    # lines in the three input files are put into lists 
    original_lines = line_format("inputs/original.txt")
    romanized_lines = line_format("inputs/romanized.txt")
    translated_lines = line_format("inputs/translated.txt")
    
    # input files must have the same number of corresponding lines
    if not (len(original_lines) == len(romanized_lines) == len(translated_lines)):
        raise ValueError("Input files must have the same number of lines.")
        
    output = [] # list of the final lines formatted
    
    for line in range(len(romanized_lines)):

        # Skip lines where all three are empty or only whitespace
        if romanized_lines[line].strip() == "" and original_lines[line].strip() == "" and translated_lines[line].strip() == "":
            continue
            
        # If all three lines are identical only include one
        if check_identical(romanized_lines[line]) == check_identical(original_lines[line]) == check_identical(translated_lines[line]):
            if translated_lines[line] != "\n":   # identical newlines not checked as 'identical'
                output.append(translated_lines[line].strip("\n") + "\n")
                output.append("\n")   # separates blocks of related lines
            continue
    
        # append lines to output if not empty
        if romanized_lines[line].strip() != "":
            output.append(romanized_lines[line].strip() + "\n")
            output.append(original_lines[line].strip() + "\n") # remove newlines already in input to avoid double newlines
            output.append(translated_lines[line].strip() + "\n")
            output.append("\n")
        else:
            continue
        
    if len(output) == 0:
        raise ValueError("No valid lines were produced from the input files. Ensure that lines are not all empty.")
    
    # removes any extra line breaks at the end of the output
    while output[-1] == "\n":
        output.pop()
    output[-1] = output[-1].rstrip("\n")   # if the last line ends with \n
    output[-1] = output[-1].rstrip(" ")    # if the last line ends with space(s)
    
    # write output to txt file
    with open("output/output.txt", "w") as file:
        for line in output:
            file.write(line)
    
    # prints output
    for line in output:
        print(line, end="")
        
    print("\n\n" + "-"*40 + "\n\nOutput successfully produced (see above)\nSaved to output/output.txt")
       
lines_grouping()
