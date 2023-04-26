import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = x
plt.title("Линейная зависимость")
plt.xlabel("место события")
plt.ylabel("высота рисунка")
plt.grid()
plt.plot(x, y, "r--")
plt.show()
