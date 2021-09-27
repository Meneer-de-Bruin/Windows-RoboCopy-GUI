#!/usr/bin/env python
# -*- coding: utf-8 -*-

splash_image = "image\eKBlogoA_clr300.jpg"
splash_text = "RoboCopy"

#help text
help = 'RoboCopy GUI is een simpele frontend voor RoboCopy t.b.v. KB Digitalisering.\n\n\
Voordat deze GUI werkt moet men in de directory waarin het programma staat het bestand "robocopy.rcj" zetten of aanmaken. \
Dit bestand bevat de opties die meegegeven \
moeten worden aan RoboCopy. Dit bestand moet als eerste twee regels het volgende bevatten:\n\
  /NOSD\n\
  /NODD\n\n\
Bij het starten van de RoboCopy job wordt de source foldernaam gebruikt om een nieuwe folder aan te maken in de destination folder. \
Als deze naam al bestaat dan wordt de inhoud daarvan overschreven.\n\
Ook wordt bij het starten van een RoboCopy job een log aangemaakt. \
Het laatste deel van de source folder naam (als het goed is de batch naam) wordt gebruikt als onderdeel van de log naam.\n\n\
Het programma start een RoboCopy job op in de achtergrond. Je kan dus na het starten van een RoboCopy job direct daarna onmiddelijke een nieuwe job opstarten. Let \
op elke job gebruikt de resources van de PC. ALs je meerdere jobs opstart kan het zijn dat dit vertragend werkt op alle lopende jobs.'
