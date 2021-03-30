class Car:

  #Constructor Method - Waiter that takes the order for your Car.
  def __init__(self,whatColor,wheelSizeInput,model,isElectric,engineHp):
    self.color = whatColor
    self.wheelSize = wheelSizeInput
    self.type = model
    self.electric = isElectric
    self.horsepower = engineHp

  def drive(self):
    print("We're driving down the road!")

  def turn(self):
    print("Turning now!")

  def stop(self):
    print("Screeeech!!!")



AdamsCar = Car("Lime Green",5,"Tesla",True,100000)


#Concatenation

AdamsCar.drive()
AdamsCar.turn()








#Object Oriented Programming
#Classes - Blueprints for building Objects / Instances
#Parameters - How you customize...
#Functions / Methods - What your thing can do.



#What do you need to build a car?
#Metal
#Engine
#Tires
#People that know how to build it
#Brakes
#steering wheel
#leather
#Engine Parts
#Wheels
#Gasoline / Fuel
#Door Handles

#How can you customize a car?
#Paint color....
#GPS
#Better Engines.
#Interior A/C
#Custom Wheels
#Steering
#Type / Model

#What can a car do?
#Travel long distances at high speed.
#Take you wheere you need to go.
#Drive
#Turn - Left/Right
#forward/backwards
#Speed up
#slow down
#Play Music
