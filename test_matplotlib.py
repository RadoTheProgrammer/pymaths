print(2^3)
import matplotlib.pyplot as plt
import random
X=[random.random()-0.5 for i in range(0,100)]
Y=[random.random()-0.5 for i in range(0,100)]
plt.scatter(X,Y)
plt.show()

X=[i for i in range(-50,50)]
Y=[x**2 for x in X]
plt.plot(X,Y)
plt.show()
