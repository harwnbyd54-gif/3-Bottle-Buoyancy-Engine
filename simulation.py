import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- PHYSICAL SETUP & PARAMETERS ---
GRAVITY = 9.81         # Acceleration due to gravity (m/s^2)
WATER_DENSITY = 1000   # Density of water (kg/m^3)
FLUID_DRAG = 0.6       # Drag coefficient inside water (viscosity resistance)
AIR_DRAG = 0.05        # Drag coefficient in the air
CRANK_RADIUS = 0.5     # Radius of the crankshaft offset (meters)
BOTTLE_VOLUME = 0.002  # Volume of each bottle (2 Liters = 0.002 m^3)
BOTTLE_MASS = 0.05     # Mass of the empty plastic bottle (0.05 kg)

# Three-way crankshaft configuration (120 degrees offset between each bottle)
angles_offsets = np.array([0, 2 * np.pi / 3, 4 * np.pi / 3])

# --- INITIAL STATE CONDITIONS ---
theta = 0.0            # Initial crankshaft rotation angle (radians)
omega = 2.0            # Initial angular velocity (rad/s) to start the system
dt = 0.02              # Time step for simulation physics (seconds)

time_history = []
omega_history = []
current_time = 0.0

# --- MATPLOTLIB UI SETUP ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle("Dynamic Simulation & Energy Curve of the 3-Bottle Buoyancy Engine", fontsize=14, fontweight='bold')

# Left Subplot: Mechanical View
ax1.set_xlim(-1.2, 1.2)
ax1.set_ylim(-1.2, 1.2)
ax1.set_aspect('equal')
ax1.axhline(0, color='blue', linestyle='--', lw=2, label='Water Surface Line')
line_crank, = ax1.plot([], [], 'o-', color='black', lw=3, label='3-Way Crankshaft')

bottles_water, = ax1.plot([], [], 'ob', markersize=16, label='Submerged (Water)')
bottles_air, = ax1.plot([], [], 'or', markersize=16, label='Exposed (Air)')

velocity_text = ax1.text(-1.1, 1.0, '', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
ax1.legend(loc='upper right')
ax1.grid(True, linestyle=':')
ax1.set_title("Mechanical Engine View")

# Right Subplot: Real-Time Dynamic Curve
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 15)
ax2.set_title("Angular Velocity over Time")
ax2.set_xlabel("Time (seconds)")
ax2.set_ylabel("Angular Velocity (rad/s)")
line_energy, = ax2.plot([], [], 'g-', lw=2, label=r'Velocity $\omega$')
ax2.grid(True)
ax2.legend(loc='upper right')

def update(frame):
    global theta, omega, current_time, time_history, omega_history

    total_net_torque = 0.0
    bottle_positions = np.zeros((3, 2))

    for i in range(3):
        bottle_angle = theta + angles_offsets[i]
        x = CRANK_RADIUS * np.cos(bottle_angle)
        y = CRANK_RADIUS * np.sin(bottle_angle)
        bottle_positions[i] = [x, y]

        if y < 0:
            net_force = (WATER_DENSITY * BOTTLE_VOLUME * GRAVITY) - (BOTTLE_MASS * GRAVITY)
            drag = FLUID_DRAG * omega
        else:
            net_force = -(BOTTLE_MASS * GRAVITY)
            drag = AIR_DRAG * omega

        torque = net_force * x - drag
        total_net_torque += torque

    moment_of_inertia = 3 * BOTTLE_MASS * (CRANK_RADIUS ** 2)
    alpha = total_net_torque / moment_of_inertia
    omega += alpha * dt
    theta += omega * dt

    current_time += dt
    time_history.append(current_time)
    omega_history.append(omega)

    if current_time > ax2.get_xlim()[1]:
        ax2.set_xlim(0, current_time + 5)
    if omega > ax2.get_ylim()[1]:
        ax2.set_ylim(0, omega + 5)

    water_mask = bottle_positions[:, 1] < 0
    air_mask = bottle_positions[:, 1] >= 0

    # ربط النقاط بالمركز (0,0) لرسم أذرع الكرنك الميكانيكي بشكل صحيح
    crank_x = []
    crank_y = []
    for pos in bottle_positions:
        crank_x.extend([0, pos[0]])
        crank_y.extend([0, pos[1]])
        
    line_crank.set_data(crank_x, crank_y)
    bottles_water.set_data(bottle_positions[water_mask, 0], bottle_positions[water_mask, 1])
    bottles_air.set_data(bottle_positions[air_mask, 0], bottle_positions[air_mask, 1])

    velocity_text.set_text(f'Angle: {theta:.2f} rad\nOmega: {omega:.2f} rad/s')
    line_energy.set_data(time_history, omega_history)

    return line_crank, bottles_water, bottles_air, velocity_text, line_energy

ani = animation.FuncAnimation(fig, update, frames=300, interval=20, blit=False)
plt.tight_layout()

# --- خيارات الحفظ التلقائي (احذف علامة # لتفعيل الحفظ بعد تثبيت ffmpeg) ---
# ani.save('buoyancy_engine.mp4', writer='ffmpeg', fps=30)
# ani.save('buoyancy_engine.gif', writer='pillow', fps=30)

plt.show()

