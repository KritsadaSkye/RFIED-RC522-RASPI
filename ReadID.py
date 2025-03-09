import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
import csv
import requests

line_token = ""  # ใส่ LINE Notify Token ของคุณ
reader = SimpleMFRC522()

def readCSV(datafile):
    infile = open("data.csv", "r")
    csv_obj = csv.reader(infile)
    all_list = [row for row in csv_obj]
    infile.close()
    return all_list

print("Entering?")

class READ:
    def __init__(self):
        self.data = None

    def readID(self):
        print("hello")
        datafile = "data.csv"
        self.data = readCSV(datafile)
        while (reader.read()):
            id_text = reader.read()
            self.id_card = int(id_text)
            self.check()

    def check(self):
        for i in range(len(self.data)):
            if (self.id_card == int(self.data[i][0])):
                print("Welcome")
                self.sendLine(f"Accessing by: {self.id_card}")
                sleep(2)
                return
        print("Get out!!")
        sleep(2)

    def sendLine(self, message):
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": f"Bearer {line_token}"}
        data = {"message": message}
        response = requests.post(url, headers=headers, data=data)
        return response.status_code

try:
    READ_obj = READ()
    READ_obj.readID()
finally:
    GPIO.cleanup()  