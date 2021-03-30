class LunchVendingMachine:

  
  def __init__(self,bunsIn,meatIn,ketchupIn,lettuceIn,tomatoesIn,picklesIn,doughIn,sauceIn,CheeseIn,iceCreamIn,bowlsIn,conesIn):
    self.buns = bunsIn
    self.meat = meatIn
    self.ketchup = ketchupIn
    self.lettuce = lettuceIn
    self.tomatoes = tomatoesIn
    self.dough = doughIn
    self.sauce = sauceIn
    self.cheese = CheeseIn
    self.iceCream = iceCreamIn
    self.bowls = bowlsIn
    self.cones = conesIn
    self.pickles = picklesIn


  

  #1 bun, 1 meat patty, 1 ketchup, 2 lettuce, 1 tomato,3pickles
  def makeHamburger(self,quantity):
    if self.buns < quantity or self.meat < quantity or self.ketchup < quantity or self.lettuce < quantity * 2 or self.tomatoes < quantity or self.pickles < quantity * 3:
      return False
    else:
      self.buns -= quantity
      self.meat -= quantity
      self.ketchup -= quantity
      self.lettuce -= quantity * 2
      self.tomatoes -= quantity
      self.pickles -= quantity * 3
      return True

  def selection(self):
    print("Welcome to the Lunch Machine!")
    print("What do you want today?")
    choice = input ("A - Hamburger  B - Cheese Pizza  C - Ice Cream")

    if choice == "A":
      burgerCount = int(input("How Many Burgers Do You Want?"))
      if self.makeHamburger(burgerCount) == True:
        if burgerCount == 1:
          print("Here is your burger")
        else:
          print("Here are your burgers")
      else:
        print("We can't complete that order")


MyVendingMachines = LunchVendingMachine(20,5,6,30,15,7,3,2,8,3,6,8)

MyVendingMachines.selection()



  
  
  
  
  #Hamburger
    #Buns
    #Meat Patty
    #Ketchup
    #Lettuce
    #Tomatoes
    #Pickles

  #Cheese Pizza
    #Dough
    #Tomato Sauce
    #Cheese
    #Oven

  #Ice Cream
    #Bowls
    #Ice Cream
    #Cupsss
    #Cones.
