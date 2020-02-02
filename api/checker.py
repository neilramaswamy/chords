from musthe import Note, Chord
from typing import List
from random import choice

notes = ["A", "B", "C", "D", "E", "F", "G"]

data = {
    "major": "M",
    "minor": "m",
    "dominant 7": "dom7"
}

def are_notes_equal(n1: Note, n2: Note) -> bool:
    """
    Returns whether `n1` and `n2` are the same note, disregarding octave. Checks
    note name and accidental values to determine this equality.
    """
    letters_equal = n1.letter == n2.letter
    accidentals_equal = n1.accidental == n2.accidental

    return letters_equal and accidentals_equal

def are_chords_equal(c1: Chord, notes: List[str]) -> bool:
    """
    Returns whether two chords have the same notes in the same order, not 
    considering octave.
    """
    chord_notes = c1.notes

    if not len(chord_notes) is len(notes):
        return False
    
    for i in range(len(chord_notes)):
        if not are_notes_equal(chord_notes[i], Note(notes[i])):
            return False

    return True

def quiz() -> None:
    note = choice(notes)
    chord_name, chord_key = choice(list(data.items()))
    print(chord_name, chord_key)

    inp = input(f"Enter space-separated notes for {note} {chord_name}: ")
    
    target_chord = Chord(Note(note), chord_key)
    submission = inp.split(' ')
    is_correct = are_chords_equal(target_chord, submission)

    print("You were right!") if is_correct else print("You were wrong.")

if __name__ == "__main__":
    quiz()