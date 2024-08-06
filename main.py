
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