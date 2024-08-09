
import matplotlib.pyplot as plt

def trajectoire_balle(x):
    position = 10*x - 5*(x**2) 
    return position

xs = [x/100 for x in list(range(201))]
ys = [trajectoire_balle(x) for x in xs]
plt.plot(xs, ys)
plt.title('Trajectoire d\'une balle lancée')
plt.xlabel('Position horizontale de la balle')
plt.ylabel('Position verticale de la balle')
plt.axhline(y = 0) #dessine une ligne horizontale à travers l'axe y
plt.show()
plt.savefig('trajectoire_balle.png')

xs2 = [0.1, 2]
ys2 = [trajectoire_balle(0.1), 0]
xs3 = [0.2, 2]
ys3 = [trajectoire_balle(0.2), 0]
xs4 = [0.3, 2]
ys4 = [trajectoire_balle(0.3), 0]
plt.title('Trajectoire d\'une balle lancée avec les lignes de visée' )
plt.xlabel('Position horizontale de la balle')
plt.ylabel('Position verticale de la balle')
plt.plot(xs, ys, xs2, ys2, xs3, ys3, xs4, ys4)
plt.show()

"""
   Trajectoire d'une balle hypothétique lancée, où un segment 
   représente la ligne visée du voltigeur sur la balle et les 
   segments notés A et B indiquent les longueurs dont le 
   rapport forme la tangente qui nous intéresse.
"""
xs5 = [0.3, 0.3]
ys5 = [0, trajectoire_balle(0.3)]
xs6 = [0.3, 2]
ys6 = [0,0]
plt.title('Trajectoire d\'une balle lancée, calcul de la tangente' )
plt.xlabel('Position horizontale de la balle')
plt.ylabel('Position verticale de la balle')
plt.plot(xs, ys, xs4, ys4, xs5, ys5, xs6, ys6 )
plt.text(0.31, trajectoire_balle(0.3)/2, 'A', fontsize = 16)
plt.text((0.3 + 2)/2, 0.05, 'B', fontsize = 16)
plt.show()
