#Kodi python skript för att avsluta systemet med en dialog ruta.
#Klickar man på Ja så stängs datorn av, nej så händer inget.
#Konstruerad av Andreas Olsson för Husvagn/Husbils pc projektet
import os
import xbmc
import xbmcgui

avsluta=xbmcgui.Dialog().yesno("Cabby Pc","Vill du avsluta Cabby Pc?",yeslabel="Ja",nolabel="Nej")
if avsluta:
   xbmc.executebuiltin('XBMC.Quit');
   os.system("sudo shutdown now");
