from flask import Flask, render_template, request
from markupsafe import Markup
from spacy.displacy.render import DEFAULT_LABEL_COLORS
import en_core_web_sm

app = Flask(__name__)

def ent_name(name):
    return f'<span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem;">{name}</span>'

def ent_box(children, color):
    return f'<mark style="background: {color}; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">{children}</mark>'

def entity(children, name):
    if type(children) is str:
        children = [children]

    children.append(ent_name(name))
    color = DEFAULT_LABEL_COLORS[name]
    return ent_box(''.join(children), color)

def render(doc):
    children = []
    last_idx = 0
    for ent in doc.ents:
        children.append(doc.text[last_idx:ent.start_char])
        children.append(
            entity(doc.text[ent.start_char:ent.end_char], ent.label_))
        last_idx = ent.end_char
    children.append(doc.text[last_idx:])
    return Markup(''.join(children))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def analyze():
    text = request.form['textarea']
    nlp = en_core_web_sm.load()
    doc = nlp(text)
    output = render(doc)
    return output

if __name__ == '__main__':
    app.run()