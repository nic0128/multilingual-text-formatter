# Multilingual Text Formatter

Developed as an academic project in Fall 2025.
<br><br>
This program formats song lyrics (or any transcript) written in a non-English writing system into blocks that combine the original text, its Romanized transcription and its English translation. The program takes three text files as input:
1. The original lyrics in a writing script other than English (e.g. Japanese, Chinese, Korean, etc.)
2. A Romanized version of those lyrics
3. The English translation.

Each text file is assumed to have each line of text correspond to the same line across all files.

The program outputs a new text file in the following format:
<br><br>

\<Romanized line\>

\<Original line\>

\<English translation\> 
<br><br>

\<Romanized line\>

\<Original line\>

\<English translation\>  
<br><br>
..... repeated for all remaining lines
<br><br>

The program also ensures that all input files contain the same number of lines and accounts for cases where certain lines may be identical across files (ex. K-pop \& J-pop often have English lines, which do not need translation \& romanization). This program is intended to be used for adding custom lyrics to music files, preparing lyrics for lyric videos, or preparing references for studying another language, all of which are tasks that would be time-consuming to do manually.

## Sample Data

The Japanese lyrics of the traditional song Furusato (ふるさと) is provided as a sample input. The original Japanese lyrics are in the public domain.

Sourced from
[Mama Lisa's World](https://www.mamalisa.com/?t=es&p=3201)
