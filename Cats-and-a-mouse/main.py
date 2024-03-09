#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the catAndMouse function below.
def catAndMouse(x, y, z):

    # calculate the absolute distance of mouse fromm each cat
    mouse_from_cat_a = abs(z - x)  # distance of mouse from cat a
    mouse_from_cat_b = abs(z - y)  # distance of mouse from cat b

    # If mouse is near to cat a then print "Cat A"
    # If mouse is near to cat b then print "Cat B"
    # Otherwies print "Mouse C" because both cats reach the mouse at the same time

    if mouse_from_cat_a < mouse_from_cat_b:
        return "Cat A"
    elif mouse_from_cat_a > mouse_from_cat_b:
        return "Cat B"
    else:
        return "Mouse C"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        fptr.write(result + '\n')

    fptr.close()
