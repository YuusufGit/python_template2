import random as rnd





leaf = None

System_Name = input("Input a name real quick: ")
leaf = rnd.Random(System_Name)

Size = None
Atmosphere = None
Water = None


def roll(): #acts as a dice. Generates the number from 1 through 6
    return leaf.randint(1, 6)



def rolltaketwo(rollamount, characteristic, modifier = 0): #rolls a specified amount and adds or minus a number

    total = 0
    for i in range(rollamount):
        total += roll()
   
    #------------------------------------------------------

    if characteristic == "Size": #Handle World Size conditions
        if (total + modifier) < 0:  #can't be less than 0
             return 0
        elif (total + modifier) > 10: #can't be greater than 10
            return 12
        elif (total + modifier) >= 0 and (total + modifier) <= 10: #Just right. Neither less than 0 or greater than 10
            return total + modifier
    
    #------------------------------------------------------

    if characteristic == "Atmosphere": #Handle atmoshpere conditions
        if Size == 0:                  #if size is 0, then atmoshpere is 0
            return 0
        elif (total + modifier) > 15: #can't be more than 15
            return 15
        elif (total + modifier) < 0:
            return 0                #can't be less than 0
        else:
            return total + modifier #between 0 and 15

    #------------------------------------------------------
    if characteristic == "Water": #Handle hydrographics/water conditions.
        if Size == 0 or Size == 1:
            return 0
        elif (total + modifier) < 0: #can't be less than 0
            return 0
        elif (total + modifier) > 10: #cant be more than 10
            return 10
            
        else:
            return total + modifier
            

    #------------------------------------------------------
    

    if characteristic == "Population": #Handles conditions for world population
       
        if (total + modifier) < 0: #can't be less than 0
            return 0
        
        elif (total + modifier) > 10: #can't be greater than 10
            return 10

        else:
            return total + modifier #between 0 and 10

    #-------------------------------------------------------------------------------
    if characteristic == "Starport":
        return(total + modifier)

    #------------------------------------------------------------------------------
    if characteristic == "Government":
        if Population == 0:
            return 0
        elif (total + modifier) < 0: #can't be less than 0
            return 0
        elif (total + modifier) > 15: #can't be greater than 15
            return 15
        else:                          #between 0 and 15
            return total + modifier

    #--------------------------------------------------------------------------------
    if characteristic == "Law_Level":
        if Government == 0:
            return 0
        elif (total + modifier) < 0: #can't be less than 0
            return 0
        elif (total + modifier) > 10: #can't be greater than 10
            return 10
        else:                          #between 0 and 10
            return total + modifier
    #---------------------------------------------------------------------------------
    if characteristic == "Tech_Level":
    
        if (Water == 0 or Water == 10) and (Population >= 6) and ((total + modifier) < 4): #An "atleast 4 condition"
            return 4
        elif (Atmosphere == 4 or Atmosphere == 7 or Atmosphere == 9) and ((total + modifier) < 5): #An "atleast 5 condition"
            return 5
        elif (Atmosphere <= 3 or (Atmosphere >= 10 and Atmosphere <= 12)) and ((total + modifier) < 7): #An "atleast 7 condition"
            return 7
        elif (Atmosphere == 13 or Atmosphere == 14) and Water == 10 and ((total + modifier) < 7): #An "atleast 7 condition"
            return 7
        else:
            return total + modifier

    #--------------------------------------------------------------------------------
    if characteristic == "Planetoid":
        return(total + modifier)
    
    #---------------------------------------------------------------
    if characteristic == "Gas_Presence":
        return (total + modifier)

    #-----------------------------------
    if characteristic == "Naval":
        return (total + modifier)
    
    #------------------------------------------------------------
    if characteristic == "Scout":
        return(total + modifier)

    #---------------------------------------------------------------
    if characteristic == "PirateBase":
        return (total + modifier)

    
#---------------------------------------------------------------




def set_water(Water, Atmosphere):
        #water-------------------------------------------
    if Atmosphere == 0 or Atmosphere == 1 or Atmosphere == 10 or Atmosphere == 11 or Atmosphere == 12:
        Water = rolltaketwo(2, "Water", -4)
    elif Atmosphere == 14:
        Water = rolltaketwo(2, "Water", -2)
    else:
        Water = rolltaketwo(2, "Water", -7)
    return Water

def set_Population(Size, Atmosphere, Water):
    
    if Size <= 2:
        Population = rolltaketwo(2, "Population", -1)
    elif Atmosphere >= 10:
        Population = rolltaketwo(2, "Population", -2)
    elif Atmosphere == 6:
        Population = rolltaketwo(2, "Population", 3)
    elif Atmosphere == 5 or Atmosphere == 8:
        Population = rolltaketwo(2, "Population", 1)
    elif Water == 0 and Atmosphere < 3:
        Population = rolltaketwo(2, "Population", -2)
    else:
        Population = rolltaketwo(2, "Population", -2)

    return Population

def determine_Tech_modifier():
        givemodifier = 0
        if Star_Port == "A":
            givemodifier += 6
        elif Star_Port == "B":
            givemodifier += 4
        elif Star_Port == "C":
            givemodifier += 2
        elif Star_Port == "X":
            givemodifier -= 4
    
        if Size <= 1:
            givemodifier += 2
        elif Size <= 4:
            givemodifier += 1
    
        if Atmosphere <= 3 or Atmosphere >= 10:
            givemodifier += 1
    
        if Water == 0 or Water == 9:
            givemodifier += 1
        elif Water == 10:
            givemodifier += 2
    
        if (Population <= 5 and Population > 0) or Population == 9:
            givemodifier += 1
        elif Population == 10:
            givemodifier += 2
        elif Population == 11:
            givemodifier += 3
        elif Population == 12:
            givemodifier += 4

        if Government == 0 or Government == 5:
            givemodifier += 1
        elif Government == 7:
            givemodifier += 2
        elif Government == 13 or Government == 14:
            givemodifier -= 2

        return givemodifier

def determine_starport():                              #
    
        rolll = rolltaketwo(2, "Starport") #Roll 2D6       #
        if rolll <= 2:                                     #
            return "X" # No starport                       #
        elif rolll <= 4:                            
            return "E" # Frontier 
        elif rolll <= 6: 
            return "D" # Poor 
        elif rolll <= 8: 
            return "C" # Routine 
        elif rolll <= 10: 
            return "B" # Good                              #
        elif rolll >= 11:                                  #
            return "A"                                     #
    #-------------------------------------------------------

def determine_trade_codes(): 
        trade_codes = []
        if 4 <= Atmosphere <= 9 and 4 <= Water <= 8 and 5 <= Population <= 7: 
            trade_codes.append("Ag") 

        if Size == 0 and Atmosphere == 0 and Water == 0: 
            trade_codes.append("As") 
        
        if Population == 0 and Government == 0 and Law_Level == 0:
            trade_codes.append("Barren")
        

        if Atmosphere >= 2 and Water == 0: 
            trade_codes.append("De") 
        
        if Atmosphere >= 10 and Water >= 1:
            trade_codes.append("Fl")
        
        if Atmosphere == 5 or Atmosphere == 6 or Atmosphere == 8 and 4 <= Water <= 9 and 4<= Population <= 8:
            trade_codes.append("Ga")

        if Population >= 9: 
            trade_codes.append("Hi") 
    
        if Tech_Level >= 12:
            trade_codes.append("Ht")
        
        if 0 <= Atmosphere <= 1 and Water >= 1:
            trade_codes.append("Ic")
        
        if 0 <= Atmosphere <= 2 or Atmosphere == 4 or Atmosphere == 7 or Atmosphere == 9 and Population >= 9:
            trade_codes.append("In")
        
        if 1<= Population <= 3:
            trade_codes.append("Lo")

        if 0 <= Atmosphere <= 3 and 0 <= Atmosphere <= 3 and Population >= 6:
            trade_codes.append("Na")

        if 4 <= Population <= 6:
            trade_codes.append("Ni")
        
        if 2<= Atmosphere <= 5 and 0 <= Water <= 3:
            trade_codes.append("Po")
        
        if Atmosphere == 6 and Atmosphere == 8 and 6 <= Population <= 8:
            trade_codes.append("Ri")
        
        if Water == 10:
            trade_codes.append("Wa")
        
        if Atmosphere == 0:
            trade_codes.append("Va")
        elif trade_codes:
            return trade_codes
        else:
            return "Idk"


        return trade_codes

def Make_Planetoid_Belts(Size):
    Planetoid_Belts = 0

    def check_if_belts(Size):
        if Size == 0:
            return True
        roll_result = rolltaketwo(2, "Planetoid")

        return roll_result >= 4

    def determine_planetoid_belts():
        roll_result = roll() - 3
        return max(roll_result, 1)

    has_Belt_system = check_if_belts(Size)
    #Planetoid_Belts = None
    if has_Belt_system:
        Planetoid_Belts = determine_planetoid_belts()
    else:
        Planetoid_Belts = 0
    return Planetoid_Belts

def check_Naval(Star_Port):
    if Star_Port in ["A", "B"]:
        roll_result = rolltaketwo(2, "Naval")
        if roll_result >= 8:
            return True
    return False

def check_Scout(Star_Port):
    if Star_Port in ["X", "E"]:
        return 0
    elif Star_Port == "C":
        roll_result = rolltaketwo(2, "Scout", -1)
        return roll_result
    elif Star_Port == "B":
        roll_result = rolltaketwo(2, "Scout", -2)
        if roll_result >= 7:
            return roll_result
        
    elif Star_Port == "A":
        roll_result = rolltaketwo(2, "Scout", -3)
        if roll_result >= 7:
            return roll_result
        
    else:
        roll_result = rolltaketwo(2, "Scout")
        if roll_result >= 7:
            return roll_result

def check_PirateBase(Star_Port, Naval_Base):
    if  not (Star_Port == "A" or Naval_Base == True):
        roll_result = rolltaketwo(2, "PirateBase")
        if roll_result >= 12:
            return True
    return False
    
def check_Gas_Presence():
    roll_result = rolltaketwo(2, "Gas_Presence")
    if roll_result >= 5:
        finalroll = roll() - 3
        return max(finalroll, 1)   
    else:
        return 0

def determine_base_code(naval, scout, pirate):

    if naval and scout:
        return "A"  # Naval Base and Scout Base/Outpost
    elif scout and pirate:
        return "G"  # Scout Base/Outpost and Pirate Base
    elif naval:
        return "N"  # Naval Base
    elif pirate:
        return "P"  # Pirate Base
    elif scout:
        return "S"  # Scout Base/Outpost
    else:
        return "None"  # No notable base

def determine_travel_zone(Atmosphere, Government, Law_Level):
    Zone = []
    if (Atmosphere >= 10 or Government in [0, 7, 10] or Law_Level == 0 or Law_Level >= 9):
        Zone.append("Amber")
        #return "Amber"  # Meets criteria for Amber Zone
    if Atmosphere == 15 and Government == 15 and Law_Level == 10: 
        Zone.append("Red")
        #return "Red" # Automatically assign Red Zone if criteria are met
    if len(Zone) > 0 and (Zone[0] == "Red" or Zone[0] == "Amber"):
        return Zone
    else:
        return "Green"  



def assign_polity(Population, Tech_Level):
    # Choose polity type based on world characteristics
    if Population > 8 or Tech_Level > 10:
        polity_options = ["Empire", "Federation", "Trade Union"]
    else:
        polity_options = ["Independent", "Confederation"]

    return rnd.choice(polity_options)


def determine_trade_routes(world):#if the world has good tech, and pop export
                                #if the world has agriculture, and ice and others then it imports

    # First End Point Types
    if world["Tech_Level"] > 9:
        return "export"
    elif world["Population"] > 8:
        return "export"
    elif world["Trade_Codes"]:
        for i in world["Trade_Codes"]:
            if i in ["Ag", "Ic", "Fl", "De"]:
             return "import" 

    Helprand = rnd.randint(1, 100)  # Generate a random number between 1 and 100

    # If random value is above 79, mark as import, otherwise export
    if Helprand >= 79:
        return "import"
    else:
        return "export"



def MakePlanet():
    global Size, Atmosphere, Water, Population, Star_Port, Government, Law_Level, Tech_Level, Trade_Codes, Planetoid_Belts, Gas_Presence, Naval_Base, Scout_Base, Pirate_Base, Base_code, Travel_Zone, Polities, Routes
    #-----------------------------------------------------
    Size = rolltaketwo(2, "Size", -2)

    Atmosphere = rolltaketwo(2, "Atmosphere", -7)

    #water-------------------------------------------
    Water = set_water(Water, Atmosphere)


    #Population----------------------------------------------

    Population = set_Population(Size, Atmosphere, Water)



    #Starport-----------------------------------
    Star_Port = determine_starport()

    #Government & Law_Level----------------------------------------------------------

    Government = rolltaketwo(2, "Government", -7)#                                   #

    Law_Level = rolltaketwo(2, "Law_Level", -7)#                                     #

    #Technology level-----------------------------------------------------------------

    Tech_Level = rolltaketwo(1, "Tech_Level", determine_Tech_modifier())

    #Trade_Codes------------------------------------------------------------------------
    
    Trade_Codes = determine_trade_codes()

    #Planetoid Belts--------------------------------------------------------------------
    Planetoid_Belts = Make_Planetoid_Belts(Size)
        
    #Gas Prescense---------------------------------------------------------------------
    Gas_Presence = check_Gas_Presence()

    #Naval---------------------------------------------------------------------------
    Naval_Base = check_Naval(Star_Port)

    #Scout Base-------------------------------------------
    Scout_Base = check_Scout(Star_Port)

    #Pirate Base----------------------------------------
    Pirate_Base = check_PirateBase(Star_Port, Naval_Base)

    #Base code------------------------------------------
    Base_code = determine_base_code(Naval_Base, Scout_Base, Pirate_Base)

    #Travel zone----------------------------------------------------------------
    Travel_Zone = determine_travel_zone(Atmosphere, Government, Law_Level)

    #Polities------------------------------------------------------------------
    Polities = assign_polity(Population, Tech_Level)

    #Route----------------------------------------------------------------
    mini_characters = {"Population": Population, "Tech_Level" : Tech_Level, "Trade_Codes" : Trade_Codes}
    Routes = determine_trade_routes(mini_characters)

    #Dictionary-----------------------------------------------------------------------
    Dict_Characteristics = {"Size" : Size, "Atmosphere" : Atmosphere, 
            "Water" : Water, "Population" : Population, "Star_Port" : Star_Port, 
            "Government" : Government, "Law_Level" : Law_Level, "Tech_Level" : Tech_Level,
            "Trade_Codes" : Trade_Codes, "Planetoid_Belts" : Planetoid_Belts, "Naval_Base" : Naval_Base,
            "Scout_Base" : Scout_Base, "Pirate_Base" : Pirate_Base, "Gas_Presence" : Gas_Presence,
            "Base_code" : Base_code, "Travel_Zone" : Travel_Zone, "Polities" : Polities, "Routes" : Routes}



    #For the planet asteroids. First check if it has planets. Make a function
    return Dict_Characteristics



StoreValues = MakePlanet()



print("Size: " + str(StoreValues["Size"]))
print("Atmosphere: " + str(StoreValues["Atmosphere"]))
print("Water: " + str(StoreValues["Water"]))
print("Population: " + str(StoreValues["Population"]))
print("StarPort: " + StoreValues["Star_Port"])
print("Government: " + str(StoreValues["Government"]))
print("Law_Level: " + str(StoreValues["Law_Level"]))
print("Tech_Level: " + str(StoreValues["Tech_Level"]))
print("Trade_Codes: " + str(StoreValues["Trade_Codes"]))
print("Planetoid_Belts: " + str(StoreValues["Planetoid_Belts"]))
print("Gas Presence: " + str(StoreValues["Gas_Presence"]))
print("Is there naval: " + str(StoreValues["Naval_Base"]))
print("Scout: " + str(StoreValues["Scout_Base"]))
print("PirateBase: " + str(StoreValues["Pirate_Base"]))
print("Base Code: " + str(StoreValues["Base_code"]))
print("Travel_Zone: " + str(StoreValues["Travel_Zone"]))
print("Polity: " + str(StoreValues["Polities"]))
print("Routes: " + str(StoreValues["Routes"]))


#Yourinput = input("What do you want: ")

#print("It didn't matter :P")