#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys, codecs

entrance = True
kitchen = False
living = False
bedroom = False
washroom = False

with codecs.open('actions_sjis.txt', 'r', 'sjis') as f:
    action_list = f.readlines()

action_list.pop(0)

for i in range(6):
    total_time = 0
    #for aline in action_list:

    while True:
        aline = random.choice(action_list).strip()
        action, duration, b_entrance, b_kitchen, b_living, b_bedroom, b_washroom = aline.split('\t')
        if (kitchen and b_kitchen == '1') or (entrance and b_entrance == '1') or (living and b_living == '1') or (washroom and b_washroom == '1') or (bedroom and b_bedroom == '1'):
            if total_time >= 30:
                break
            print('0:{0:02d} {1}'.format(total_time, action))
            total_time += int(duration)
    print('----')
