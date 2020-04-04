from musthe import Note, Chord, Letter, Scale
from typing import List
from random import choice, sample
from equality import are_chords_equal

notes = [x for x in Letter.letters]

def do_grading(quizType, letter, operation, submission):
    """
    This is the function that requests for grading come to. quizType is whether the user is quizzing
    on chords or scales; letter is the the note on which the exercise is based; operation is the
    type of chord/scale; submission is a string of the user's answer.
    """
    validate_letter(letter)
    
    if quizType == 'chord':
        return grade_chord(letter, operation, submission)
    elif quizType == 'scale':
        return grade_scale(letter, operation, submission)
    else:
        raise ValueError("Unrecognized quiz type")

def validate_letter(letter):
    # We only support letters not containing accidentals
    # This probably should be fixed
    if letter not in notes:
        raise ValueError("Unsupported note trying to be accessed")

def grade_chord(letter, operation, submission):
    # TODO: Validate operation fully
    correct_chord = Chord(Note(letter), operation) # Operation is the chord quality "key" (minmaj7/aug7/etc.
    is_correct = are_chords_equal(correct_chord, submission.split(' '))

    return {'is_correct': is_correct}

def grade_scale(letter, operation, submission):
    # TODO: Validate operation fully
    correct_scale = Scale(Note(letter), operation) # Operation should be the greek mode
    correct_notes = [str(correct_scale[i]) for i in range(len(correct_scale))]

    # TODO: Much better checking algorithm. Levenshtein distance?
    if submission.split(' ') == correct_notes:
        return {'is_correct': True}
    else:
        return {'is_correct': False}


# Returns a note and operation
def do_bootstrapping(quizType):
    note = choice(notes)

    if quizType == 'chord':
        operation_id, operation_name = choice(list(Chord.names.items()))

        return {'note': note, 'operation_id': operation_id, 'operation_name': operation_name}
    elif quizType == 'scale':
        operation_id = choice(list(Scale.greek_modes_set))
        operation_name = operation_id

        return {'note': note, 'operation_id': operation_id, 'operation_name': operation_name}
    else:
        raise ValueError('Unsupported quiz type found during bootstrapping')