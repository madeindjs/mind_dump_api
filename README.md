# Mind Dump

Export all your thoughts and let Natural Language Processing [Spacy](https://spacy.io/) organize them.

## Usage

### Import

~~~bash
$ python3 add.py "Bonjour Lorène, je pense que je vais passer te voir cette après midi à Croix Rousse"
$ # OR
$ echo "Bonjour Lorène, je pense que je vais passer te voir cette après midi à Croix Rousse" | python3 add.py
~~~

### Export

It will highlight recognized word:

- `+` for persons
- `@` for locations
- `:` for organisations
- `?` for others

Exemple:

~~~bash
$ python3 export.py
2019-10-14 13:26 - Bonjour +[Lorène], je pense que je vais passer te voir cette après midi à @[Croix Rousse]
~~~

### Server

~~~bash
$ env FLASK_APP=server.py flask run
~~~

## Installation

~~~bash
$ pip3 install -r REQUIREMENTS.txt
$ python3 -m spacy download fr # and other lang if needed
~~~
