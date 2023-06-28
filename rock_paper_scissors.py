#!/usr/bin/env python3

import random

p1 = input().lower()
randint = random.randint(1, 3)

if randint == 1:
    p2 = "rock"
elif randint == 2:
    p2 = "paper"
elif randint == 3:
    p2 = "scissors"