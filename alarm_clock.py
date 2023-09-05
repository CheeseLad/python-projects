#!/usr/bin/env python3
# SOUND FILE: https://assets.mixkit.co/active_storage/sfx/1004/1004.wav

from playsound import playsound
import time

#ASNI to make terminal look fancy

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm_clock(secs):
  time_elapsed = 0

  print(CLEAR)
  while time_elapsed < secs:
    time.sleep(1)
    time_elapsed += 1

    time_left = secs - time_elapsed
    minutes_left = time_left // 60
    seconds_left = time_left % 60

    print(f"{CLEAR_AND_RETURN}Alarm will start in: {minutes_left:02d}:{seconds_left:02d}")

  playsound("alarm.mp3")


try:
  minutes = int(input("How many minutes to wait: "))
except ValueError:
  print("Please enter a number.")
try:
  seconds = int(input("How many seconds to wait: "))
except ValueError:
  print("Please enter a number.")
total_seconds = minutes * 60 + seconds
alarm_clock(total_seconds)

