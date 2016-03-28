#Kodi python skript för att avläsa det givarna läst av, körs varje 30 sekund
import os
import xbmc
import xbmcgui
import time


while 1:
	filename = "/opt/skript/system/system.txt"
	file = open(filename, "r")
	lines = file.read().splitlines()
	file.close()
	
	xbmcgui.Window( 10000 ).setProperty( 'InneTemp' , lines[0] )
	
	xbmcgui.Window( 10000 ).setProperty( 'UteTemp' , lines[1] )

	xbmcgui.Window( 10000 ).setProperty( 'KylTemp' , lines[2] )
	
	xbmcgui.Window( 10000 ).setProperty( 'VattenGivare' , lines[3] )
	
	xbmcgui.Window( 10000 ).setProperty( 'Volten' , lines[4] )
	
	time.sleep(30)
