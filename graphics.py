from matplotlib.pyplot import subplots
import numpy as np

rng = np.random.default_rng()

fig, ax = subplots(figsize=(8,8))

x = rng.standard_normal(100)
y = rng.standard_normal(100)

ax.plot(x,y);

fig, ax = subplots(figsize=(8,8))
ax.scatter(x, y, marker='o')
ax.set_xlabel("this is the x-axis")
ax.set_ylabel("this is the y-label")
ax.set_title("Plot of X vs Y")
fig.set_size_inches(6,4)
fig

fig, axes = subplots(nrows=2, ncols=3, figsize=(15,5))
axes[0, 1].plot(x,y, 'o')
axes[1][0].plot(x,y)
axes[1,2].scatter(x, y, marker='+')
fig

axes[0,1].set_xlim([-1,1])
fig.savefig("Figure.jpg")
fig.savefig("Figure.png", dpi=400)
fig.savefig("Figure.pdf", dpi=200);

fig, ax = subplots(figsize=(8,8))
x = np.linspace(-np.pi, np.pi, 50)
y = x
f = np.multiply.outer(np.cos(y), 1 / (1 + x**2))
ax.contour(x, y, f);

fig, ax = subplots(figsize=(8,8))
ax.contour(x, y, f, levels=45);

fig, ax = subplots(figsize = (8,8))
ax.imshow(f);