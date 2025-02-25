import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np

# Read the CSV log file.
# Expected columns:
# nationality, target_x, target_z, radar_heading, radar_x, radar_z, range, fov, lock_condition
data = pd.read_csv("new_log.txt", header=None, 
                   names=["nationality", "target_x", "target_z", "radar_heading", "radar_x", "radar_z", "range", "fov", "lock_condition"])

# Extract target positions and lock condition over time.
target_x = data["target_x"].values
target_z = data["target_z"].values
lock_condition = data["lock_condition"].values

# Radar parameters.
# Here radar_heading is an array (one value per frame) so it can be animated.
radar_heading = data["radar_heading"].values  
radar_x = data["radar_x"].values[0]
radar_z = data["radar_z"].values[0]
radar_range = data["range"].values[0]
radar_fov = data["fov"].values[0]

# Create the figure and axis.
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Determine plot limits based on target positions and radar range.
min_x = min(np.min(target_x), radar_x - radar_range)
max_x = max(np.max(target_x), radar_x + radar_range)
min_z = min(np.min(target_z), radar_z - radar_range)
max_z = max(np.max(target_z), radar_z + radar_range)
ax.set_xlim(min_x, max_x)
ax.set_ylim(min_z, max_z)

# Draw a circle to represent the radar range.
radar_circle = plt.Circle((radar_x, radar_z), radar_range, color='blue', fill=False, linestyle='--', label="Radar Range")
ax.add_patch(radar_circle)

# Create the radar wedge (FOV) using the initial heading.
initial_heading = radar_heading[0]
theta1 = initial_heading - radar_fov / 2.
theta2 = initial_heading + radar_fov / 2.
wedge = patches.Wedge((radar_x, radar_z), radar_range, theta1, theta2,
                      color='blue', alpha=0.2, label="Radar FOV")
ax.add_patch(wedge)

# Create a plot object for the target.
target_dot, = ax.plot([], [], 'o', markersize=8)

# Label the plot.
ax.set_xlabel("X coordinate")
ax.set_ylabel("Z coordinate")
ax.set_title("Radar and Target Animation")
ax.legend(loc="upper right")

# Animation update function.
def animate(i):
    # Update target position.
    x = target_x[i]
    z = target_z[i]
    target_dot.set_data([x], [z])
    
    # Update target color based on lock condition.
    if lock_condition[i]:
        target_dot.set_color('green')
    else:
        target_dot.set_color('red')
    
    # Update radar heading (wedge angles).
    current_heading = radar_heading[i]
    new_theta1 = current_heading - radar_fov / 2.
    new_theta2 = current_heading + radar_fov / 2.
    wedge.set_theta1(new_theta1)
    wedge.set_theta2(new_theta2)
    
    return target_dot, wedge

# Create the animation.
ani = animation.FuncAnimation(fig, animate, frames=len(target_x), interval=1, blit=False, repeat=True)

# Display the animated plot.
plt.show()
