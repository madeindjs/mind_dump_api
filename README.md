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
$ python3 server.py
~~~

Create thought:

~~~bash
$ curl -X POST -d "content=Alexandre, Ruby est bien mieux que Python"  http://localhost:5000/thoughts/
~~~
~~~json
{
    "content":"Alexandre, Ruby est bien mieux que Python",
    "id":1,
    "tags": [
        {"content":"Alexandre","label":"PER"},
        {"content":"Ruby","label":"MISC"},
        {"content":"Python","label":"MISC"}
    ]
}
~~~

You can retrieve this though using:

~~~bash
$ curl http://localhost:5000/thoughts/1
~~~

Or all thoughts:

~~~bash
$ curl http://localhost:5000/thoughts/
~~~

#### Import yours posts

You may want import many files in Mind Dump. Here a Bash one liner

~~~bash
$ for file in ~/Documents/Posts/*.txt; do  curl -X POST --data "content=$(cat $file)" http://localhost:5000/thoughts/  ; done
~~~

## Installation

~~~bash
$ pip3 install -r REQUIREMENTS.txt
$ python3 -m spacy download fr # and other lang if needed
~~~

