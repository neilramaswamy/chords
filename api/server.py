from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('index.html', movie="The Bee Movie")

@app.errorhandler(404)
def fallback(e):
    return "This does not exist!"

if __name__ == '__main__':
    app.run(debug=True)