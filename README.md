# Qups Store
Dit is Qups store. Met deze app kunnen wij bekers verkopen.

Lees de LICENSE.md voor gebruik.

## De Qups Store draaien

De Qups Store vereist python 3.

Stappen voor installatie:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Maak een nieuw bestaand aan genaamd .flaskenv met daarin het volgende:
```bash
FLASK_APP=qups-store.py
SECRET_KEY=somepassword
ADMIN_PASSWORD=wachtwoord-voor-bestellingen-pagina
MAIL_USERNAME=qupsteam@gmail.com
MAIL_PASSWORD=password
MAIL_ADDRESS=qupsteam@gmail.com
MAIL_SERVER=smtp.googlemail.com
MAIL_PORT=587
MAIL_USE_TLS=1
```
Vervang de SECRET_KEY en ADMIN_PASSWORD voor ingewikkelde, veilige wachtwoorden. Vul het gmail wachtwoord in bij MAIL_PASSWORD.

Debug modus kan als volgt aangezet worden in hetzelfde bestand:
```bash
FLASK_DEBUG=1
```

Maak de database aan:
```bash
python -m flask db init
python -m flask db migrate
python -m flask db upgrade
```

Starten:
```bash
python -m flask run
```
