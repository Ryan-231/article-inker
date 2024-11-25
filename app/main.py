# Run by typing python3 main.py

# import basics
import os

# import stuff for our web server
from flask import Flask, request, redirect, url_for, render_template, session
from utils import get_base_url
from markupsafe import Markup
# import stuff for our models
from aitextgen import aitextgen

# load up a model from memory. Note you may not need all of these options.
# ai = aitextgen(model_folder="model/",
#                tokenizer_file="model/aitextgen.tokenizer.json", to_gpu=False)

# change to true to use gpu for this project, will make load times faster
ai = aitextgen(model="distilgpt2", to_gpu=False)


# setup the server
# port may need to be changed if there are multiple flask servers running on same server
port = 12345
base_url = get_base_url(port)


# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
    app = Flask(__name__)
else:
    app = Flask(__name__, static_url_path=base_url+'static')

app.secret_key = os.urandom(64)

# set up the routes and logic for the webserver

# decide which model to use based on user input
story_genre = ''
def genre_text_generation(genre_type):
    if genre_type == 'Horror':
        file_dest = 'model/horror'
    if genre_type == 'Dad Jokes':
        file_dest = 'model/dadjokes'
    if genre_type == 'Drama':
        file_dest = 'model/drama'
    if genre_type == 'Poetry':
        file_dest = 'model/poetry'
    return file_dest

@app.route(f'{base_url}')
def home():
    return render_template('index.html', ans=None)


@app.route(f'{base_url}', methods=['POST'])
def home_post():
    return redirect(url_for('results'))


@app.route(f'{base_url}/results')
def results():
    if 'data' in session:
        data = session['data']
        print(data)
        return render_template('index.html', generated=data)
    else:
        return render_template('index.html', generated=None)


# take prompt and genre from user and send to the correct model, then take its response
@app.route(f'{base_url}/generate_text/', methods=["POST"])
def generate_text():
    """
    view function that will return json response for generated text.
    """
    prompt = request.form['prompt']
    genre_type = request.form['genre']
    print("genre", genre_type, "prompt", prompt)
    story_genre = genre_text_generation(genre_type)
    ai = aitextgen(model_folder = story_genre, to_gpu=False)
    if prompt is not None:
        if genre_type == "Dad Jokes":
            generated = ai.generate(
                n=1,
                batch_size=3,
                prompt=str(prompt),
                max_length=20,
                temperature=0.9,
                return_as_list=True
            )
        elif genre_type == "Horror":
            generated = ai.generate(
                n=1,
                batch_size=3,
                prompt=str(prompt),
                max_length=400,
                temperature=0.9,
                return_as_list=True
            )
        elif genre_type == "Drama":
            generated = ai.generate(
                n=1,
                batch_size=3,
                prompt=str(prompt),
                max_length=400,
                temperature=0.9,
                return_as_list=True
            )
        elif genre_type == "Poetry":
            generated = ai.generate(
                n=1,
                batch_size=3,
                prompt=str(prompt),
                max_length=300,
                temperature=0.9,
                return_as_list=True
            )
            
            #print("BEFORE: ",generated)
            symbols = "! @ # $ % ^ & * ( ) _ - + = { } [ ] ."
            symbols = symbols.split()
            result = []
            article = generated[0]
            article = article[:]

            for i,c in enumerate(article):
                if c.isupper() and article[i-1].islower():
                    result.append("<br>")
                result.append(c)
            result = "".join(result)
            generated[0]= Markup(result)

    #print("AFTER: ",generated)
    data = {'generated_ls': generated}
    session['data'] = generated[0]
    return redirect(url_for('results'))

if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'localhost'

    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host='0.0.0.0', port=port, debug=True)
