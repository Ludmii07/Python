""" 
Realizar un programa en Python que consulte el día de la semana en el que esta e imprema el mensaje "¡FELIZ
FIN DE SEMANA!", si el día es sabado o domingo. En el caso de ser otro dia indicar que se debe ir al colegio
a estudiar.

"""

día = input ("Ingrese el día de la semana en el que está:")
if día == "sabado" or día == "domingo":
    print ("¡Feliz fin de semana!")
else:
    print ("Hoy se debe ir al colgio!")