from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import Order
from app.forms import BestelFormulier, GegevensFormulier

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
    prijs = int(aantal)*5+7
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
            prijs=prijs,
        )
        db.session.add(order)
        db.session.commit()
        flash('Bedankt voor uw bestelling!')
        return redirect(url_for('index'))
    return render_template('gegevens.html', title=title, aantal=aantal, prijs=prijs, form=form)

@app.route('/bestellingen')
def bestellingen():
    title = "Bestellingen"
    return render_template('bestellingen.html', title=title, bestellingen=Order.query.all())
