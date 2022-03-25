# ⌥ + ⇧ multi cursor
# pip freeze > requirements.txt
from flask import Flask, render_template, jsonify
from symptoms import get_symptoms, get_sample, get_exam

app = Flask("__name__")


@app.route('/')
def index():
    new_call = {
        "life_functions": get_symptoms(), "sample": get_sample(), "exam": get_exam()
    }

    return render_template("index.html", new_call=new_call)


@app.route('/background_process_test')
def background_process_test():
    new_call = {
        "life_functions": get_symptoms(), "sample": get_sample(), "exam": get_exam()
    }
    return jsonify(new_call=new_call)


if __name__ == "__main__":
    app.run()
