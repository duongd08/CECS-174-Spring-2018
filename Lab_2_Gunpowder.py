#This lab is done by Daniel Duong and Cameron Kovacik.
import math

gunpowder = float(input('Enter gunpowder:'))
angle = float(input('Enter the angle:'))
theta = (math.pi / 180) * angle
acceleration = 9.8
velocity = 10 * gunpowder
velocity_height = (velocity * math.sin(theta)) 
velocity_ground = (velocity * math.cos(theta))
apex = velocity_height / acceleration
time = 2 * apex
total_distance = velocity_ground * time

print('How many kg of gunpowder?:', gunpowder)
print('What angle?:', angle)
print('Your shot landed:', format(total_distance, '.2f'), 'meters')


