# ⌥ + ⇧ multi cursor
# pip freeze > requirements.txt
from flask import Flask, render_template, jsonify
from symptoms import Symptoms

app = Flask("__name__")


@app.route('/')
def index():
    symptoms = Symptoms()
    new_call = symptoms.symptoms

    return render_template("index.html", new_call=new_call)


@app.route('/background_process_test')
def background_process_test():
    symptoms = Symptoms()
    new_call = symptoms.symptoms
    return jsonify(new_call=new_call)


if __name__ == "__main__":
    app.run()
