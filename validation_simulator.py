import random
import time

# Define acceptable ranges for each subsystem
REQUIREMENTS = {
    "navigation_accuracy_m": (0, 5),  # meters
    "battery_level_percent": (70, 100),  # percent
    "temperature_celsius": (-10, 40),  # Celsius
    "communication_link": (True, True),  # must be True
}


# Function to simulate telemetry data
def generate_telemetry():
    return {
        "navigation_accuracy_m": round(random.uniform(0, 10), 2),
        "battery_level_percent": random.randint(50, 100),
        "temperature_celsius": round(random.uniform(-20, 50), 1),
        "communication_link": random.choice([True, False]),
    }


# Function to validate telemetry
def validate_telemetry(telemetry):
    results = {}
    for key, value in telemetry.items():
        min_val, max_val = (
            REQUIREMENTS[key]
            if isinstance(REQUIREMENTS[key], tuple)
            else (REQUIREMENTS[key], REQUIREMENTS[key])
        )
        if isinstance(value, bool):
            results[key] = value == min_val
        else:
            results[key] = min_val <= value <= max_val
    return results


# Run simulation
def run_simulation(cycles=5):
    print("Starting Subsystem Validation...\n")
    for i in range(cycles):
        print(f"--- Test Cycle {i+1} ---")
        telemetry = generate_telemetry()
        validation = validate_telemetry(telemetry)
        for key, value in telemetry.items():
            status = "PASS" if validation[key] else "FAIL"
            print(f"{key}: {value} => {status}")
        print("")
        time.sleep(1)  # simulate delay between cycles


if __name__ == "__main__":
    run_simulation(10)
