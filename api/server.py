from flask import Flask, render_template, request, url_for
from service import do_grading, do_bootstrapping

app = Flask(__name__)

@app.route("/")
def render_landing():
    return render_template('landing.html')

@app.route("/quiz")
def render_quiz():
    return render_template('quiz.html')

@app.route("/bootstrap")
def bootstrap():
    """
    Provides a note and "operation" on which to start quizzing a user. We need this bootstrapping
    to start the quiz; responses to /submit (for grading) will come back with another set of data
    on which to quiz.
    """
    # TODO: Return a note and operation given a quiz type (either `chord` or `scale`).
    quizType = request.args.get('quizType', 'chord') # Default to a 'chord' quiz

    return do_bootstrapping(quizType), 200

@app.route('/submit', methods=['POST'])
def grade_submission():
    body = request.get_json()

    quizType = body['quizType'] # `chord` or `scale`
    letter = body['letter'] # Musical note off which the chord/scale is based
    operation = body['operation'] # mixo/min7/maj7/etc.
    submission = body['submission'] # string of the space-separated notes a user submitted

    return do_grading(quizType, letter, operation, submission), 200

@app.errorhandler(404)
def fallback(e):
    return "This does not exist!"

if __name__ == '__main__':
    app.run(debug=True)