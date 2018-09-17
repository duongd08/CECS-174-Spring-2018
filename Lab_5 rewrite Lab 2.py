# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:30:13 2018

@author: camer


"""
#Cameron Kovacik and Daniel Duong
import math

def main():
    target = get_target_distance()
    gunpowder = get_gunpowder()
    angle = get_angle()
    distance = calculate_distance(gunpowder, angle)
    hit = abs(target - distance)
    hit_target = False
    while hit_target == False:
        hit_target = is_hit(distance, target)
        if target < distance:
            print("\nYour shot landed, {:0.2f}".format(hit),'m long of the target')
            gunpowder = get_gunpowder()
            angle = get_angle()
            distance = calculate_distance(gunpowder, angle)
            hit_target = is_hit(distance, target)
            hit = abs(target-distance)
        else:
            print("\nYour shot landed, {:0.2f}".format(abs(hit)),'m short of the target')
            gunpowder = get_gunpowder()
            angle = get_angle()
            distance = calculate_distance(gunpowder, angle)
            hit_target = is_hit(distance, target)
            hit = abs(target - distance)
    print("It's a hit!\nYou win!")
    
def get_target_distance():
    target = int(input('Please enter a distance between 0 and 1000: '))
    while not 0 <= target <= 1000:
        target = int(input('Please enter a distance between 0 and 1000: '))
    return target

def get_gunpowder():
    gunpowder = float(input("Please enter a gunpowder amount: "))
    while not gunpowder >= 0:
        gunpowder = float(input("Please enter a gunpowder amount: "))
    return gunpowder
        

def get_angle():
    angle = float(input("Please enter your angle: "))
    while not 1 <= angle <= 89:
        angle = float(input("Please enter your angle: "))
    return angle


def calculate_distance(gunpowder, angle):
    theta = ((math.pi/ 180) * angle)
    acceleration = 9.8
    velocity = 10 * gunpowder
    velocity_height = (velocity * math.sin(theta))
    velocity_ground = (velocity * math.cos(theta))
    apex = velocity_height / acceleration
    time = 2 * apex
    distance = velocity_ground * time
    return distance


def is_hit(distance, target):
    #print(distance, target)
    hit = abs(target - distance)
    if hit <= 1:
        return True
    else:
        return False
    
    


    
    
    
    

    
    
    
    
    
    
    
main()