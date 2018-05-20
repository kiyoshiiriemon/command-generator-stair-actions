#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys, codecs

with codecs.open('people.txt', 'r', 'utf8') as f:
    people = f.readlines()

with codecs.open('locations.txt', 'r', 'utf8') as f:
    locations = f.readlines()

with codecs.open('actions.txt', 'r', 'utf8') as f:
    actions = f.readlines()

#p = random.choice(people).strip()
l = random.choice(locations).strip()
a = random.choice(actions).strip()

people2 = random.sample(set(people), 2)
p = people2[0].strip()
p2 = people2[1].strip()
a = a.replace('誰かを', p2 + 'を')
a = a.replace('誰かが誰かに', p2 + 'に')

print(p + "が" + l + "で" + a)

