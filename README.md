[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

# Named Entity Recognizer

A web-app built using Flask to extract named enities from text.

## See the app in action 

Open on Deta [(link)](https://entityrecog-1-i7449443.deta.app)\
Open on Render (Slower) [(link)](https://named-entity-recognizer.onrender.com)

## Used Frameworks and Libraries

Flask [(link)](https://github.com/pallets/flask)\
Spacy by [explosion.ai](https://explosion.ai/) | Repo [(link)](https://github.com/explosion/spaCy)

## Screenshot

![Screenshot](screenshots/scr-cap-1.gif?raw=true "App in action")

Article Source: [The New Yorker, 'Two Bands' by Adam Gopnik](https://www.newyorker.com/magazine/2013/12/23/two-bands)

## How to deploy locally

### Replicate the project

Clone the repository:
```bash
  $ git clone git@github.com:sarbhanub/spacy-ner.git
```

Preparing a venv:
```bash
  $ python -m venv .venv && .venv\Scripts\activate

```

Installing the requirements:
```bash
  $ pip install -r requirements.txt
```

Run:
```bash
  $ python app.py
```
