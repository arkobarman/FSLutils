import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import cm

print('Name of desired color map:', sys.argv[1])
print('Available colormaps:')
print(plt.colormaps())

plt.imshow(np.random.rand(10,10), cmap=sys.argv[1])
cbar = plt.colorbar()
cbar.solids.set_edgecolor('face')
plt.draw()
plt.show()

norm = colors.Normalize(vmin=0, vmax=254)

cmap = cm.get_cmap(sys.argv[1])

with open(sys.argv[1] + '.cmap', 'w') as f:
	for i in range(255):
		rgba = cmap(norm(i))
		f.write('{:.6f} {:.6f} {:.6f}\n'.format(rgba[0], rgba[1], rgba[2]))
