import time
import os

def speak(text):
    print(f"Ev Asistanı: {text}")
    os.system(f"termux-tts-speak '{text}'")

def listen_and_respond():
    print("Brand New Day ev yapay zekası aktif ve dinliyor...")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    speak("Brand New Day ev sistemleri çevrimiçi. Dinliyorum efendim.")
    listen_and_respond()
