from musthe import Note, Chord, Letter, Scale
from random import choice, sample
from equality import are_chords_equal

notes = [x for x in Letter.letters]

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

def chord_quiz() -> None:
    note = choice(notes)
    chord_key, chord_name  = choice(list(Chord.names.items()))

    inp = input(f"Enter space-separated notes for {note} {chord_name}: ")

    target_chord = Chord(Note(note), chord_key)
    
    # TODO: More-intelligent parsing to account for upper-case characters.
    submission = inp.split(' ')
    is_correct = are_chords_equal(target_chord, submission)

    print("You were right!") if is_correct else print("You were wrong.")


if __name__ == "__main__":
    scale_quiz()
