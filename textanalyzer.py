# -*- coding: utf-8 -*-
"""
Textanalyzer
Chatbot text analysis component

@author: Timon, Yunis, Ralph
"""

import random
import re


sm = u'\U0001F642'  # Smiley

Begruessung = ('hi', 'hallo', 'hey', 'moin', 'moinsen', 'hello', 'servus', 'ciao', 'salut', 'jo')
Doch = ('doch')
Hae = ('hä', 'hä?', 'hää', 'häää')
Verneinung = ('nope', 'nichts', 'ne', 'nein', 'nö', 'noap', 'no', 'nicht', 'not')
Schule = ('schule')
Warum = ('warum', 'wieso')
Weil = ('weil baum', 'wegen dir', 'wieso nicht')
Kannst = ('kannst', 'könntest', 'kann' , 'konnte')
Nein = ('ne', 'nein', 'nö')
Ausdruecke = ('doof', 'scheiße', 'blöd', 'blöde', 'öde', 'öd', 'Adelheid', 'popo', 'kaka')
Jokes = ('alles was beine hat '+sm, 'ich nicht '+sm, 'du '+sm, 'ein bein '+sm, 'deine mudda mit mir ins Bett '+sm,
         'ich nicht mit dir '+sm)

HA = ('mathe', 'deutsch', 'latein', 'englisch', 'geo', 'geographie', 'erdkunde', 'physik')
#auf = ('auf', 'gemacht')
#haben = ('ham', 'haben', 'hatten', 'habt', 'hattet')
HAantwort = ('Buch S. ')
Hausaufgaben = HAantwort + str(random.randint(10,200)) + '/' + str(random.randint(1,13))

		 
def analyze_text(text):
    satz = text.lower()
    woerter = satz.split(' ')
    resp_title = ''  # title in bold + italics
    resp_msg = ''  # message below title (if present) only in italics
    resp = ''
    # first analyze words...
    for wort in woerter:
        wort = re.sub('[!?. #$@€]', '', wort)  # delete special characters
        if wort in Begruessung:
            resp = Begruessung[random.randint(0, len(Begruessung) -1)]
        elif wort in Doch:
            resp = 'oh'
        elif wort in Hae:
            resp = Hae[random.randint(0, len(Hae) - 1)]
        elif wort in Schule:
            resp = ('schule ist ' + (Ausdruecke[random.randint(0, len(Ausdruecke) - 1)]))
        elif wort in HA:  # TODO: specify using (HA + haben + auf)
            resp = Hausaufgaben
        #elif wort in ('was'):
        #	 resp = 'nichts'
        elif wort in Kannst:
            resp = Nein[random.randint(0, len(Nein) - 1)]
        elif wort in Warum:
            resp = Weil[random.randint(0, len(Weil) - 1)]
        elif wort in Verneinung:
            resp = 'doch'
    # ...then check if whole sentence matches
    if satz in ('was get', 'was geht', 'wat geht'):
        resp = Jokes[random.randint(0, len(Jokes) - 1)]
    elif satz in ('jmd on'):
        resp = Begruessung[random.randint(0, len(Begruessung) - 1)]

    if resp:  # add formatting for WhatsApp
        resp_title = '*_' + resp + '_*'

    return (resp_title, resp_msg)

