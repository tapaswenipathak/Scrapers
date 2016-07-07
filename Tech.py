#!/usr/bin/env python

import requests
from bs4 import *
from gi.repository import Notify
from time import sleep

def getFoss(title,message):
	Notify.init("a")
	notifyme=Notify.Notification.new(title,message,"Description:")
	notifyme.show()
	return

url="http://fossbytes.com/"

while True:
	f=requests.get(url)
	soup=BeautifulSoup(f.content)

	tech_head=soup.find_all("h2",{"itemprop":"headline"})
	tech_desription=soup.find_all("h2",{"itemprop":"description"})

	for info in tech_head:
		getFoss("Tech news",info.text,)
		sleep(60)

