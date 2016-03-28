#Kodi python skript för att starta om datorn.
#Dialog ruta visas innan så man kan välja ja eller nej
#Skapad av Andreas Olsson för Husvagn/Husbil Pc projektet
import os
import xbmc
import xbmcgui

startaom=xbmcgui.Dialog().yesno("Cabby Pc","Vill du starta om Cabby Pc?",yeslabel="Ja",nolabel="Nej")
if startaom:
   xbmc.executebuiltin('XBMC.Quit');
   os.system("sudo reboot");
