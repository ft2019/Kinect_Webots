from controller import Robot
from controller import RangeFinder
from controller import Robot,Camera
import numpy as np
import cv2
import matplotlib.pyplot as plt
class Enumerate(object):
    def __init__(self, names):
        for number, name in enumerate(names.split()):
            setattr(self, name, number)


class Slave (Robot):
    timeStep =32
    maxSpeed = 10.0
    mindistance=1.0
    motors = []
    range = []
    kinectvalues=[]
    

    def boundSpeed(self, speed):
        return max(-self.maxSpeed, min(self.maxSpeed, speed))

    def initialization(self):
        self.motors.append(self.getMotor("back right wheel"))
        self.motors.append(self.getMotor("back left wheel"))
        self.motors.append(self.getMotor("front right wheel"))
        self.motors.append(self.getMotor("front left wheel"))
        self.kinectcolor = self.getCamera("kinect color")
        self.kinectrange = self.getRangeFinder("kinect range")
        self.kinectcolor.enable(self.timeStep)
        self.kinectrange.enable(self.timeStep)
        self.motors[0].setPosition(float("inf"))
        self.motors[1].setPosition(float("inf"))
        self.motors[2].setPosition(float("inf"))
        self.motors[3].setPosition(float("inf"))
        self.motors[0].setVelocity(0.0)
        self.motors[1].setVelocity(0.0)
        self.motors[2].setVelocity(0.0)
        self.motors[3].setVelocity(0.0)
    def run(self):
        iteration=0
        while self.step(self.timeStep) != -1:
              iteration=iteration+1
              self.step(self.timeStep)
              image=self.kinectrange.getRangeImage()
              kinectvalue=self.kinectrange.rangeImageGetDepth(image,200 , 50, 55)
              print(kinectvalue)
              self.motors[0].setVelocity(3)#right
              self.motors[1].setVelocity(2)#left
              self.motors[2].setVelocity(3)#right
              self.motors[3].setVelocity(2)#left
              print("iteration = "+ str(iteration))

controller = Slave()
controller.initialization()
controller.run()