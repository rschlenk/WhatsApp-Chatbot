# -*- coding: utf-8 -*-
"""
WhatsApp Chatbot
Interacts with WhatsApp Web using Selenium

@author: Ralph
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import textanalyzer
import time


# define some constants
bot = u'\U0001F916'  # Timon
#bot = u'\U0001F47E'  # Yunis
homename = 'xxxxxx'
homenumber = 'xxxxxxxxxxxx'  # set to own number
chat = 'xxxxxxxxxxxx'  # set to target chat 
welcome = '*_' + 'WhatsApp Chatbot wurde gestartet.' + '_*'


def select_chat(dest):
    # select the chatlist box
    chatlistbox_xpath = '//input[@type="text"]'
    chatlistbox = wait.until(EC.presence_of_element_located((
        By.XPATH, chatlistbox_xpath)))
    time.sleep(5)
    chatlistbox.send_keys('{}'.format(dest))
    chatlistbox.send_keys(Keys.ENTER)
    print('    target chat selected')
    time.sleep(10)  # need to load chat

def send_message(title, msg=''):
    print('message with title "{}"'.format(title))

    # select the input box
    inputbox_xpath = "//div[@contenteditable='true']"
    inputbox = wait.until(EC.presence_of_element_located((
        By.XPATH, inputbox_xpath)))
    time.sleep(2)
    if msg:
        inputbox.send_keys(bot + ' : ' + title + Keys.SHIFT + Keys.ENTER + Keys.SHIFT + msg)
    elif title:
        inputbox.send_keys(bot + ' : ' + title)
    else:
        print('    message NOT sent')
        return
    inputbox.send_keys(Keys.ENTER)
    print('    message sent')

    # wait until message is sent
    msgtime_xpath = '//span[@data-icon="msg-time"]'
    wait.until(EC.invisibility_of_element_located(
        (By.XPATH, msgtime_xpath)))
    print('    message delivered')
    time.sleep(2)


print(u'\U0001F916' + ' WhatsApp Chatbot ' + u'\U0001F916' + ' started')

#driver = webdriver.Chrome(executable_path="./chromedriver")  # driver must be in same directory
driver = webdriver.Firefox(executable_path="./geckodriver")  # driver must be in same directory
driver.set_page_load_timeout(60 * 5)  # might take time until window opens
wait = WebDriverWait(driver, 1000)

print('authenticating with WhatsApp Web')
driver.get('https://web.whatsapp.com/')
input('>>> please scan QR code - press ENTER when done <<<\n')
time.sleep(10)  # maybe need some time to load
print('sending welcome status message to {}'.format(homenumber))
select_chat(homenumber)
send_message(welcome)
print()

print('changing to chat \"{}\"'.format(chat))
select_chat(chat)

print('\n>>> close browser window to stop <<<\n')

msg_list_old = []
while True:
    chat_list = driver.find_elements_by_class_name('vW7d1')  # chat history
    msg_list_maxlen = 1  # keep it at 1 for the moment
    msg_list = []  # previous 0..maxlen messages without bot contributions
    if chat_list:
        for i in range(-1, -min(msg_list_maxlen, len(chat_list))-1, -1):
            if chat_list[i].get_attribute('innerHTML').find(bot + '\"> : ') < 0:
                msg_list.append(chat_list[i].text)
    if msg_list and msg_list != msg_list_old:
        msgcomplete = (msg_list[0][:-6]).split('\n')  # remove timestamp and split string
        if len(msgcomplete) > 1:
            msgname = msgcomplete[0]
            msgtext = msgcomplete[1]
        else:
            msgname = homename
            msgtext = msgcomplete[0]
        print('analyzing text "{}"'.format(msgtext))
        if msgtext:
            (t, m) = textanalyzer.analyze_text(msgtext)
            send_message(t, m)
    msg_list_old = msg_list.copy()
    time.sleep(5)

#driver.close()
