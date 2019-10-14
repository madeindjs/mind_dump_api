from flask import Flask, escape, request, jsonify
from add import import_sentence
from mind_dump.models import Though


app = Flask(__name__)

@app.route('/')
def hello():

    thoughs_export = []

    thoughs = (Though.select())

    for though in thoughs:
        thoughs_export.append({
            'id': though.id,
            'content': though.content,
            'tags': [{'label': word.label, 'content': word.content} for word in though.words]
        })
    name = request.args.get("name", "World")

    return jsonify(thoughs_export)