from flask import render_template, flash, redirect, url_for
from app import app, db, mail
from app.models import Order
from app.forms import BestelFormulier, GegevensFormulier
from flask_mail import Message
from app.mailer import Mailer
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/bestellen', methods=['POST', 'GET'])
def bestellen():
    title = "Bestellen"
    form = BestelFormulier()
    if form.validate_on_submit():
        return redirect('/gegevens/{}'.format(form.aantal.data))
    return render_template('bestellen.html', title=title, form=form)

@app.route('/gegevens/<aantal>', methods=['POST', 'GET'])
def gegevens(aantal):
    title = "Afronden"
    perstukprijs = 5
    verzendkosten = 7
    aantal = int(aantal)
    form = GegevensFormulier()
    if form.validate_on_submit():
        order=Order(
            voornaam=form.voornaam.data,
            achternaam = form.achternaam.data,
            email = form.email.data,
            adres=form.adres.data,
            postcode=form.postcode.data,
            plaats=form.postcode.data,
            aantal=aantal,
            prijs=perstukprijs*aantal+verzendkosten,
        )
        db.session.add(order)
        db.session.commit()
        mailer = Mailer(order.id)
        flash('Bedankt voor uw bestelling!')
        return redirect(url_for('index'))
    return render_template('gegevens.html', title=title, aantal=aantal, perstukprijs=perstukprijs, verzendkosten=verzendkosten, form=form)

@app.route('/bestellingen/<key>')
def bestellingen(key):
    title = "Bestellingen"
    password = os.environ.get('ADMIN_PASSWORD')
    if not key or key != password:
        return redirect(url_for('index'))
    return render_template('bestellingen.html', title=title, bestellingen=Order.query.all())
