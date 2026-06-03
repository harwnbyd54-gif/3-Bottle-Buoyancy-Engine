<img width="1161" height="592" alt="تنزيل (1)" src="https://github.com/user-attachments/assets/702232c5-0b57-466b-af24-ab9cbe48f1a3" />


https://github.com/user-attachments/assets/265ca425-e3a0-43fc-8e74-89c2c70b375a

<img width="1200" height="600" alt="buoyancy_engine" src="https://github.com/user-attachments/assets/bf49c48d-b45a-4b47-840e-9b651261a14c" />
# 🚀 3-Bottle Buoyancy Engine Simulation

An advanced dynamic simulation and physics playground built in Python. This project models a mechanical engine driven by buoyancy forces acting on three rotating bottles partially submerged in water. The bottles are mounted on a three-way crankshaft configuration, offset by 120 degrees from each other, demonstrating how buoyant potential energy converts into continuous rotational kinetic energy.

---

## 📐 Physics & Mathematical Modeling

The engine updates its state frame-by-frame by balancing gravity, buoyancy, and medium drag (fluid/air resistance) for each bottle based on its vertical position (\(y\)):

1. **Submerged Bottle (\(y < 0\)):** Experience an upward buoyant force exceeding gravity, alongside high viscous resistance from water:
   \[F_{net} = (\rho_{water} \cdot V_{bottle} \cdot g) - (m_{bottle} \cdot g)\]
   \[F_{drag} = C_{fluid} \cdot \omega\]

2. **Exposed Bottle (\(y \ge 0\)):** Affected solely by downward gravity with negligible air drag:
   \[F_{net} = - (m_{bottle} \cdot g)\]
   \[F_{drag} = C_{air} \cdot \omega\]

3. **Torque and Kinematics Integration:**
   * **Net Torque:** \(\tau = F_{net} \cdot x - F_{drag}\)
   * **Angular Acceleration:** \(\alpha = \frac{\sum \tau}{I}\) (where total system Moment of Inertia \(I = 3 \cdot m \cdot r^2\))
   * **State Updates (\(dt\)):** 
     \[\omega_{new} = \omega + \alpha \cdot dt\]
     \[\theta_{new} = \theta + \omega_{new} \cdot dt\]

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd 3-bottle-buoyancy-engine
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the simulation:**
   ```bash
   python simulation.py
   ```

---

## 🎥 Exporting Animation to Video/GIF
The script runs interactively by default. If you want to render and save the real-time simulation as an `mp4` video or an animated `gif` to display on your GitHub profile:
1. Ensure you have `ffmpeg` installed on your system.
2. Uncomment the final lines inside `simulation.py`:
   ```python
   # ani.save('buoyancy_engine.mp4', writer='ffmpeg', fps=30)
   # ani.save('buoyancy_engine.gif', writer='pillow', fps=30)
   ```
3. Run the script again to generate the files.

---

## 🤝 Contributing
Contributions, issue reports, and optimizations are welcome! Feel free to fork the repository and submit a pull request if you want to implement fluid dynamics, wave mechanics, or dynamic volume changes.
