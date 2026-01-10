import time
import random  # For simulation; replace with sensor input in hardware setup

# Voltage thresholds (adjust for your region/system)
UNDER_VOLTAGE = 190.0
OVER_VOLTAGE = 220.0
NORMAL_MIN = UNDER_VOLTAGE
NORMAL_MAX = OVER_VOLTAGE
RELAY_PIN = 18  # Simulated GPIO pin (use RPi.GPIO or similar for hardware)

def read_voltage():
    """Simulate voltage reading (replace with ADC/sensor like ZMPT101B)."""
    return round(random.uniform(180, 240), 1)

def relay_control(state):
    """Simulate relay: HIGH=ON (load connected), LOW=OFF (protected)."""
    global relay_status
    relay_status = state
    print(f"Relay: {'ON' if state else 'OFF'}")

def protection_system():
    relay_status = True  # Start with load connected
    print("Protection System Active. Ctrl+C to stop.")
    
    try:
        while True:
            voltage = read_voltage()
            status = "Unknown"
            
            if voltage < UNDER_VOLTAGE:
                status = "UNDER VOLTAGE"
                relay_control(False)  # Cut load
                print(f"ALERT: {status} ({voltage}V) - Load Disconnected!")
            elif voltage > OVER_VOLTAGE:
                status = "OVER VOLTAGE"
                relay_control(False)  # Cut load
                print(f"ALERT: {status} ({voltage}V) - Load Disconnected!")
            else:
                status = "NORMAL"
                if not relay_status:  # Reconnect if recovered
                    relay_control(True)
                print(f"OK: {status} ({voltage}V)")
            
            time.sleep(0.5)  # Sample rate
    except KeyboardInterrupt:
        print("System Stopped.")

if __name__ == "__main__":
    protection_system()