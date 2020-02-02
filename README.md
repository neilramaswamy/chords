# Chords
An application that helps you learn the notes in common jazz chords. Because 570 is hard.

Users will be prompted with a chord, given a chance to vocally dictate the notes, and then they will be told if their dictation was correct. I'm leaning toward vocal dictation (pitch ignorant, however) since speaking is faster than typing, and it more-closely parallels the type of recall needed for Jazz (or, at least, the type of recall that I'd like to have).

Here's a more-concrete idea of what an interaction with this app will look like:

- Front-end displays a chord like "A7#5"
- Front-end pauses for a set amount of time then starts recording audio.
- User dictates the notes that they think are in the chord: "A", "C#", "E#", "G".
- Back-end verifies their answer and sends the result to the front-end, which tells the user how they did.

This will likely turn into a web app whose frontend will be written in Typescript and whose backend will be written in Python. Each "end" will be running its own server. The Python ("verification" server, API) will use GCP's Speech-to-Text to turn audio into a string, which we can more-easily parse.
