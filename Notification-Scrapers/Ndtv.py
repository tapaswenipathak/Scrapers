from bs4 import *
import requests
from time import sleep
from gi.repository import Notify

def getnotif(title, message):
	Notify.init("Test")
	notif=Notify.Notification.new(title,message)
	notif.show()
	return

url="http://www.ndtv.com/top-stories?pfrom=home-topstories"

while True:

	r=requests.get(url)
	soup=BeautifulSoup(r.content)

	data=soup.find_all("div",{"class":"nstory_header"})

	for items in data:
		getnotif("Top stories",items.text)
		sleep(60)




