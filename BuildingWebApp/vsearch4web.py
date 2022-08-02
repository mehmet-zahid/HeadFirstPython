from vsearch import search4letters
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return entry_page()


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    return str(search4letters(phrase, letters))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/results', methods=['GET', 'POST'])
def result_page():
    return render_template('results.html', the_title='Here are your results:', the_results=do_search(),
                           the_phrase=request.form['phrase'], the_letters=request.form['letters'])


app.run(debug=True)

