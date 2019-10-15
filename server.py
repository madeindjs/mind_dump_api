from flask import Flask, escape, request, jsonify
from flask_cors import CORS
from add import import_sentence
from mind_dump.models import Though, ThoughWord, Word
from peewee import JOIN
import mistune


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    markdown = mistune.Markdown()

    with open('./README.md', 'r') as content_file:
        content = content_file.read()
        return markdown(content)

@app.route('/thoughts/')
def index():
    thoughts_export = []
    thoughts = (
        Though.select(Though, Word)
              .join(ThoughWord, JOIN.LEFT_OUTER)
              .join_from(ThoughWord, Word, JOIN.LEFT_OUTER)
              .order_by(Though.created_at.desc())
    )

    for though in thoughts:
        thoughts_export.append(though.to_object())

    return jsonify([though.to_object() for though in thoughts])

@app.route('/thoughts/<int:id>/', methods=['GET'])
def get(id):
    though = Though.get_by_id(id)
    return jsonify(though.to_object())

@app.route("/thoughts/", methods=['POST'])
def create():
    print(request.form['content'])
    though = import_sentence(request.form['content'])
    return jsonify(though.to_object())


if __name__ == "__main__":
    app.run()