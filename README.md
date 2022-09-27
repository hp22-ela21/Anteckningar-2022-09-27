# Anteckningar 2022-09-27
Implementering av MQTT i Python (del I). Enkel realisering av publicering via en klient samt prenumeration via en server.

Filen repetition.py utgörs av ett litet program där tre lysdioder togglas mellan att blinka var 100:e millisekund eller vara
släckta via nedtryckning av en tryckknapp. Eventdetektering men en callback-rutin aktiveras på stigande flank på tryckknappens pin,
där lysdiodernas tillstånd togglas vid detekterad event. Denna uppgift användes för repetition av biblioteket RPi.GPIO.

Filen client.py innehåller programkod för att realisera en MQTT-klient via biblioteket paho.mqtt. Denna klient ansluts till host 
broker.hivemq.com och publicerar meddelanden som matas in från tangenbordet till topic python/mqtt/1. 

Filen server.py innehåller programkod för att realisera en MQTT-server som prenumererar på tidigare nämnda topic. 
När en klient publicerar ett meddelande till detta topic så tar denna server emot detta och skriver ut i terminalen.