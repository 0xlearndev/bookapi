import flask
import urllib.request
import requests
import json
from flask import request, jsonify, render_template
from bs4 import BeautifulSoup

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Our data
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'synopsis': 'The coldsleep itself was dreamless.',
     'published': '1992',
     'rating': 9,
     'pic': "https://images.macmillan.com/folio-assets/macmillan_us_frontbookcovers_350W/9780812515282.jpg",
     'link': "https://www.goodreads.com/book/show/77711.A_Fire_Upon_the_Deep"},

    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'synopsis': 'Some inhabitants of a peaceful kingdom cannot tolerate the act of cruelty that underlies its happiness.',
     'published': '1973',
     'rating': 5,
     'pic': "https://m.media-amazon.com/images/I/41srw9ZyJrL.jpg",
     'link': "https://www.goodreads.com/book/show/92625.The_Ones_Who_Walk_Away_from_Omelas"},
     
    {'id': 2,
     'title': 'Another one',
     'author': 'Bilawal Riaz',
     'synopsis': 'None yet',
     'published': '1993',
     'rating': 10,
     'pic': "https://static.wikia.nocookie.net/20thcenturyboys/images/a/a6/Friend.jpg/revision/latest/scale-to-width-down/340?cb=20100213163313",
     'link': "https://google.com"},
]




# Homepage
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', status='home')

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        status = "noid"
        return render_template('index.html', status=status)

    results = []
    found = 'no'
    status = ''
    print(results)

    for book in books:
        if id == book['id']:
            found = 'yes'
            results.append(book)
        else:
            found = 'no'
    
    if len(results) > 0:
        status = 'found'
    else:
        status = 'not found'
    
    print(results)
    return render_template('index.html', output=results, json=jsonify(results), notfound=found, status=status)

app.run()
