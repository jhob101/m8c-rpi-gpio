import subprocess
import time

# Define the paths to your script files
hardware_keys_script = "gpio-hardware-keys.py"
volume_control_script = "gpio-volume-control.py"

# Start the hardware keys script as a separate process
hardware_keys_process = subprocess.Popen(["python3", hardware_keys_script])

# Wait for a few seconds (adjust as needed)
time.sleep(5)

# Start the volume control script as a separate process
volume_control_process = subprocess.Popen(["python3", volume_control_script])

# Optionally, you can wait for the processes to complete (if needed)
# hardware_keys_process.wait()
# volume_control_process.wait()

# Keep the main script running or perform other tasks
try:
    while True:
        time.sleep(0.01)  # Add a slight delay to reduce CPU usage
        # pass  # Keep the main script running

except KeyboardInterrupt:
    # Optionally, you can terminate the subprocesses when the main script is terminated
    hardware_keys_process.terminate()
    volume_control_process.terminate()
    pass
