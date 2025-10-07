import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import numpy as np

x = np.arange(0, 100)
y = []

for i in x:
    y.append(round(math.sqrt(i), 2))

def conv_to_rad(deg):
    return deg * (np.pi / 180)

def find_angle_hyp(p_x, p_y):
    return math.degrees(math.atan2(p_y, p_x))

p_x = 1
p_y = 1
theta = 45

fig, ax = plt.subplots()
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)

def update(frame):
    ax.grid()
    frame +=1
    global p_x, p_y
    p_1 = [p_x, 0]
    p_2 = [p_y, 0]
    ax.plot(p_1, p_2, color='blue')
    theta = find_angle_hyp(p_x, p_y) + 90
    p_x = p_x + float(round(np.cos(conv_to_rad(theta)), 2))
    p_y = p_y + float(round(np.sin(conv_to_rad(theta)), 2))
    p_1 = [p_x, p_1[0]]
    p_2 = [p_y, p_2[0]]
    ax.plot(p_1, p_2, color='blue')
    if frame == 60:
        p_1 = [p_x, 0]
        p_2 = [p_y, 0]
        ax.plot(p_1, p_2, color='blue')
    
    
ani = animation.FuncAnimation(fig=fig, func=update, frames=60, interval=50, repeat=False)
plt.show()