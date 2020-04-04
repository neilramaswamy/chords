from musthe import Note, Chord
from typing import List

def are_notes_equal(n1: Note, n2: Note) -> bool:
    """
    Returns whether `n1` and `n2` are the same note, disregarding octave or enharmonic equivalence.
    Checks note name and accidental value to determine this equality.
    """
    letters_equal = n1.letter == n2.letter
    accidentals_equal = n1.accidental == n2.accidental

    return letters_equal and accidentals_equal


assert(are_notes_equal(Note("A4"), Note("A4")))
assert(are_notes_equal(Note("E#3"), Note("E#5")))
assert(not are_notes_equal(Note("B#"), Note("C")))


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