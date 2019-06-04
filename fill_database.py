#!/usr/bin/env python3
from app import db
from app.models import Flashcard, Lesson

default_image = "https://upload.wikimedia.org/wikipedia/commons/2/20/Flag_of_the_Netherlands.svg"

lesson_greetings = Lesson(name="Groeten", description="Leer mensen groeten in het Duits", image=default_image)



lesson_greetings.flashcards.append(Flashcard(image=default_image, dutch="hallo", german="hallo"))
lesson_greetings.flashcards.append(Flashcard(image=default_image, dutch="dag", german="tschüss"))
lesson_greetings.flashcards.append(Flashcard(image=default_image, dutch="goede dag", german="guten Tag"))
lesson_greetings.flashcards.append(Flashcard(image=default_image, dutch="goede avond", german="guten Abend"))
lesson_greetings.flashcards.append(Flashcard(image=default_image, dutch="tot ziens", german="auf wiedersehen"))
lesson_greetings.flashcards.append(Flashcard(image=default_image, dutch="tot straks", german="bis bald"))

db.session.add(lesson_greetings)
db.session.commit()
