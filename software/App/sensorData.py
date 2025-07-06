import serial

PORT = "/dev/tty.usbserial-0001"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)

def get_distance():
    if ser.in_waiting > 0:
        try:
            line = ser.readline().decode('utf-8').strip()
            print(f"Raw serial: {line}")  # Debugging
            return float(line)
        except ValueError:
            print("Invalid line received, skipping.")
            return None
    return None

if __name__ == "__main__":
    while True:
        distance = get_distance()
        if distance is not None:
            print("Distance:", distance)
