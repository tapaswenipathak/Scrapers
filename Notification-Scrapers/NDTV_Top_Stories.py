''' Install libnotify-bin using command "sudo apt-get install libnotify-bin" if an error occurs regarding gi/types.py
upgrade the library using "sudo apt-get install libnotify-bin --upgrade" it will solve the error, bug has been fixed.
If you get a warning regarding BeautifulSoup just add.. "lxml" in --> soup = BeautifulSoup(r.content,"lxml")
still getting an error.. "pip install pysocks" will work fine. Still getting an error, there must be a configuration problem
with your machine
 '''

from bs4 import *
import requests
from time import sleep
from gi.repository import Notify

def getnotif(title, message):
	Notify.init("Test")
	notif=Notify.Notification.new(title,message, "Description:")
	notif.show()
	return

url="http://www.ndtv.com/top-stories?pfrom=home-topstories"

while True:

	r=requests.get(url)
	soup=BeautifulSoup(r.content,"lxml")

	data=soup.find_all("div",{"class":"nstory_header"})

	for items in data:
		getnotif("Top stories",items.text)
		sleep(60)
