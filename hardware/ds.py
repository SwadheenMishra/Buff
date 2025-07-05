from ultraS import UltrasonicSensor
import time

TRIG_PIN = 5 # The ESP32 pin GPIO23 connected to TRIG pin of the ultrasonic sensor
ECHO_PIN = 18 # The ESP32 pin GPIO22 connected to ECHO pin of the ultrasonic sensor

sensor = UltrasonicSensor(trig_pin=TRIG_PIN, echo_pin=ECHO_PIN)
sensor.set_detection_threshold(140)  # Set detection threshold to 140 cm
sensor.enable_filter(num_samples=20)  # Enable filtering and set number of samples to 20

def get_distance():
    sensor.loop()  # Perform measurement cycle
    distance = sensor.get_distance()
    if distance and distance < 100:
        return round(distance, 1)
    return 100