from time import sleep
import random

#Raumgroesse
xlength = 10
ylength = 20
#Sollen die Start-Koordinaten zufaellig gew�hlt werden?
startcoordsZufall = True
#Soll der Bewegungsverktor zufaellig gew�hlt werden?
vZufall = True


#Start-Koordinaten
# X und Y Koordinaten zu beginn
coords = [0, 0]
#Wenn zufaellig:
if startcoordsZufall == True:
    xlength = random.randrange(0, xlength, 1)
    ylength = random.randrange(0, ylength, 1)

#Richtungs-Vektor
#Vershiebung in X und Y-Richtung
v = [1, 2]




running = True
print coords
while running==True:
    coords[0] = coords[0] + v[0]
    coords[1] = coords[1] + v[1]
    print coords
    sleep(1)
    #Wenn das Objekt an die obere Begrenzung in X-Richtung stößt prallt es ab
    if coords[0] >= xlength:
        v[0] = v[0] * -1
    #Wenn das Objekt an die obere Begrenzung in Y-Richtung stößt prallt es ab
    if coords[1] >= ylength:
        v[1] = v[1] * -1
    #Wenn das Objekt an die untere Begrenzung in X-Richtung stößt prallt es ab
    if coords[0] <= 0:
        v[0] = v[0] * -1
    #Wenn das Objekt an die untere Begrenzung in Y-Richtung stößt prallt es ab
    if coords[1] <= 0:
        v[1] = v[1] * -1
