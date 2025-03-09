import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
import csv

reader = SimpleMFRC522()

try:
    print("Place your card to save your card")
    while (reader.read()):
        data = ""
        id, text = reader.read()
        with open("data.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([id])
        print(f"ID: {id}")
        print("write data successfully")
        sleep(2)
finally:
    GPIO.cleanup()