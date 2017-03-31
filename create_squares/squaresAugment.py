import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(1, 63, 10)
y = np.random.randint(1, 63, 10)

dy, dx = [grid.astype(int) for grid in np.mgrid[-3:3:15j, -3:3:15j]]
Y = dy[None, :, :] + y[:, None, None]
X = dx[None, :, :] + x[:, None, None]

img = np.zeros((64, 64))
img[Y, X] = 1

plt.imshow(img)
plt.show()