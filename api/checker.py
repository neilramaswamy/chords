from musthe import Note, Chord, Letter, Scale
from typing import List
from random import choice, sample

notes = [x for x in Letter.letters]

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

# Quiz on the Greek modes
def scale_quiz() -> None:
    note = choice(notes)
    scale = sample(Scale.greek_modes_set, 1)[0]

    inp = input(f"Enter space-separateed notess for {note} {scale}: ")

    correct_scale = Scale(Note(note), scale)
    correct_notes = [str(correct_scale[i]) for i in range(len(correct_scale))]

    # TODO: Better answer-checking algorithm
    if inp.split(' ') == correct_notes:
        print("You got the correct scale!")
    else:
        print("You got it wrong!")

def quiz() -> None:
    note = choice(notes)
    chord_key, chord_name  = choice(list(Chord.names.items()))
    print(chord_name, chord_key)

    inp = input(f"Enter space-separated notes for {note} {chord_name}: ")

    target_chord = Chord(Note(note), chord_key)
    
    # TODO: More-intelligent parsing to account for upper-case characters.
    submission = inp.split(' ')
    is_correct = are_chords_equal(target_chord, submission)

    print("You were right!") if is_correct else print("You were wrong.")


if __name__ == "__main__":
    scale_quiz()
