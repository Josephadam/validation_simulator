
<body>

  <h1>🚀 Spacecraft Subsystem Validation Simulator</h1>

  <p>This Python project simulates a validation system for key spacecraft subsystems, including:</p>
  <ul>
    <li>Navigation Accuracy</li>
    <li>Battery Level</li>
    <li>Internal Temperature</li>
    <li>Communication Link Status</li>
  </ul>

  <h2>🔧 Features</h2>
  <ul>
    <li>Simulates telemetry data across multiple test cycles</li>
    <li>Validates each subsystem reading against defined thresholds</li>
    <li>Logs pass/fail status per subsystem</li>
    <li>Fully CLI-based — lightweight and runs locally</li>
  </ul>

  <h2>💻 Tech Used</h2>
  <ul>
    <li>Python 3</li>
    <li>No external libraries required</li>
  </ul>

  <h2>📦 How to Run</h2>
  <pre>
git clone https://github.com/your-username/spacecraft-subsystem-simulator.git
cd spacecraft-subsystem-simulator
python spacecraft_simulator.py
  </pre>

  <h2>📄 Output Example</h2>
  <pre>
--- Test Cycle 1 ---
navigation_accuracy_m: 3.21 => PASS
battery_level_percent: 85 => PASS
temperature_celsius: 12.7 => PASS
communication_link: True => PASS
  </pre>

  <h2>🛰️ Purpose</h2>
  <p>This simulator was built to demonstrate skills in software testing, system validation, and data simulation. It can be extended to include CSV export, dashboards, or hardware-in-the-loop testing components.</p>

  <h2>📫 Contact</h2>
  <p>Made by a Computer Science student passionate about aerospace systems and embedded software development.</p>

</body>
</html>
