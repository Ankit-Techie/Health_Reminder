import pygame
import datetime
import time


def play_audio(file, p):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while True:
        a = input()
        if a == p:
            pygame.mixer.music.stop()
            break


def log(txt):
    with open("log", "a") as f:
        f.write(f"{txt + time.asctime()}\n")


a = (int(datetime.datetime.now().hour))

initial_water = time.time()
initial_eyes_exercise = time.time()
initial_exercise = time.time()
print("WELCOME TO OFFICE HOURS MODE!")

while 9 <= a <= 17:
    if time.time() - initial_water > 40*60:
        print("Reminder to drink water enter drank or Drank:")
        play_audio("water.mp3", "drank" or "Drank")
        initial_water = time.time()
        log("Water drank at: ")
    elif time.time() - initial_eyes_exercise > 30 * 60:
        print("Reminder to do your eyes exercise enter done or Done:")
        play_audio("eyes exercise.mp3exercise.mp3", "done" or "Done")
        initial_eyes_exercise = time.time()
        log("Eyes exercise done at: ")
    elif time.time() - initial_exercise > 45 * 60:
        print("Reminder to do your physical exercise enter done or Done:")
        play_audio("exercise.mp3", "done" or "Done")
        initial_exercise = time.time()
        log("Physical Exercise done at: ")
