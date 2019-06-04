from flask import render_template
from app import app
from app.models import Order
from app.forms import BestelFormulier

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/bestellen')
def bestellen():
    title = "Bestellen"
    form = BestelFormulier()
    return render_template('bestellen.html', title=title, form=form)


@app.route('/gegevens', methods=['POST'])
def gegevens():
    return render_template('gegevens.html')
