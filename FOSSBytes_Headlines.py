''' Install libnotify-bin using command "sudo apt-get install libnotify-bin" if an error occurs regarding gi/types.py
upgrade the library using "sudo apt-get install libnotify-bin --upgrade" it will solve the error, bug has been fixed.
If you get a warning regarding BeautifulSoup just add.. "lxml" in --> soup = BeautifulSoup(r.content,"lxml")
still getting an error.. "pip install pysocks" will work fine. Still getting an error, there must be a configuration problem
with your machine
 '''

import requests
from bs4 import *
from gi.repository import Notify
from time import sleep


def getFoss(title, message):
    Notify.init("a")
    notifyme = Notify.Notification.new(title, message, "Description:")
    notifyme.show()
    return

url = "http://fossbytes.com/"

while True:
    f = requests.get(url)
    soup = BeautifulSoup(f.content, "lxml")

    tech_head = soup.find_all("h2", {"itemprop": "headline"})
    tech_desription = soup.find_all("h2", {"itemprop": "description"})

    for info in tech_head:
        getFoss("Tech news", info.text,)
        sleep(60)
