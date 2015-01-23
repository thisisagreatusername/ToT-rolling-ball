from time import sleep


#Raumgroesse
xlength = 10
ylenght = 20

#Start-Koordinaten
# X und Y Koordinaten zu beginn
coords = [0, 0]

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
    if coords[1] >= ylenght:
        v[1] = v[1] * -1
    #Wenn das Objekt an die untere Begrenzung in X-Richtung stößt prallt es ab
    if coords[0] <= 0:
        v[0] = v[0] * -1
    #Wenn das Objekt an die untere Begrenzung in Y-Richtung stößt prallt es ab
    if coords[1] <= 0:
        v[1] = v[1] * -1
