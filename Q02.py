"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q2
To accept an object mass in kilograms and velocity in meters per second and display its momentum. Momentum is calculated as e=mc2 where m is the mass of the object and c is its velocity.

Explaination Video Link: https://www.youtube.com/watch?v=5biTgAF1hcc&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=3&pp=iAQB
"""

# Setup Code

import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

###########################################
# Real Code Starts

mass = float(input("Enter mass: "))
velocity = float(input("Enter velocity: "))

# momentum = mass * velocity * velocity

momentum = mass * (velocity**2)

print(
    f"Momentum of mass {mass}kg and velocity {velocity}m/s is {momentum}kgm/s")
