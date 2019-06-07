from flask_mail import Message
from app import mail, db
from app.models import Order
import os
import sys

class Mailer(object):
    def __init__(self, ordernummer):
        self.ordernummer = ordernummer
        self.email = os.environ.get('MAIL_ADDRESS')

    def send(self):
        order = Order.query.get(self.ordernummer)
        if not order or not self.email:
            return "Order not found"
        totaalprijs = order.aantal*5+7
        msg = Message("Uw bestelling by Qups",
            sender = self.email,
            recipients = [order.email])
        msg.body = "Beste {} {},\n\
Bedankt voor uw bestelling bij Qups!\n\n\
U heeft de volgende bestelling gedaan:\n\
{} x Qups stalen beker 300 ml a €5,- per stuk\n\
Verzodenkosten: €{}\n\
Totaalprijs: €{}\n\n\
Om uw bestelling af te ronden vragen wij u om €{} euro over te maken naar de volgende rekening:\n\
NL97 INGB 0008 5948 02\n\
T.n.v: HR W F Wijsman\n\
O.v.v: order {}\n\n\
Nadat wij uw betaling hebben ontvangen, zullen wij uw bestelling zo snel mogelijk versturen. U heeft uw bestelling dan binnen 3 werkdagen in huis.\n\n\
Met vriendelijke groet,\n\
Het Qups Team\n\n\
Tel: +31 06 8142 5046\n\
Amstelcampus\n\
Weesperzijde 190\n\
1097 DZ Amsterdam".format(order.voornaam, order.achternaam, order.aantal, 7, totaalprijs, totaalprijs, self.ordernummer)
        msg_qups = Message("Nieuwe bestelling by Qups",
            sender = self.email,
            recipients = [self.email])
        msg_qups.body = "De volgende bestelling is zojuist geplaatst:\n\
{} x Qups stalen beker\n\
Verzodenkosten: €{}\n\
Totaalprijs: €{}\n\n\
Gegevens van de besteller:\n\
Naam: {} {}\n\
Adres: {}\n\
       {} {}\n\
Email: {}\n".format(order.aantal, 7, totaalprijs, order.voornaam, order.achternaam, order.adres, order.postcode, order.plaats, order.email)
        try:
            mail.send(msg)
            mail.send(msg_qups)
        except Exception as e:
            return(str(e))
