# -*- coding: utf-8 -*-
"""
Simplebot
... for testing textanalyzer component

@author: Timon, Yunis, Ralph
"""

import textanalyzer


while True:
    satz = input("Du: ")
    if not satz:
        break;
    print('Chatbot: ' + (textanalyzer.analyze_text(satz)[0]))
    print('Chatbot: ' + (textanalyzer.analyze_text(satz)[1]))




# analyze textfile for automated bot testing
if False:
    chatlist = []
    with open('klassenchat.txt', 'r', encoding='utf-8') as chat:
        for line in chat.readlines():
            line = line.rstrip()  # remove trailing '\n'
            if line:
                chatlist.append(line)
        if chatlist:
            for i  in range(0, len(chatlist)):
                #print(chatlist[i])
                print((textanalyzer.analyze_text(chatlist[i])[0]))
