# Jon Person
# Assignment: This assignment is to familiarize us with object-oriented programming.
# We need to define the following properties: Number of Gears (1 - 15), Current Gear (should default to 1),
# Number of Wheels (1, 2, 3, or 4), Brake Type ("hand brakes" or "foot brakes")
# We also need to define the following methods: Set & Get Number of Gears, Set & Get Current Gear, Set &
# Get Number of Wheels,
# Set & Get Brake Type, Reset Gears: Set gear back to 1,
# Increase Gear: Increase Current Gear by 1, do not allow going over Number of Gears,
# Decrease Gear: Decrease Current Gear by 1, do not allow going under 1

# This is a big one, wow.

# Start by defining the class, 'Bike', as well as its properties

class Bike:
    # Now, we instantiate the bike and define each of its properties
    # The four required properties are: (1) the number of gear (1-15), (2)the current gear, (3) the number of wheels, and
    # (4) brake type
    def __init__(self, gear_number, current_gear, wheels, brakes):
        # Our number of gears can be any integer between 1 and 15
        # If it's outside of that range, then we want to call an error
        if isinstance(gear_number, int) and (gear_number >= 1) and (gear_number <= 15):
            self.gear_number = gear_number
        elif isinstance(gear_number, int) and (gear_number >= 1) and (gear_number > 15):
            print("ERROR: Gear must be between integer between 1 and 15, resetting to allowed max (15).")
            self.gear_number = 15
        elif isinstance(gear_number, int) and (gear_number < 1) and (gear_number <= 15):
            print("ERROR: Gear must be between integer between 1 and 15, resetting to allowed max (15).")
            self.gear_number = 15
        else:
            print("ERROR: Gear must be between integer between 1 and 15, resetting to allowed max (15).")
            self.gear_number = 15
        # The current gear cannot exceed the maximum number of gears
        # The current gear can also not be below 1
        # In either case, we want to print an error message
        if isinstance(current_gear, int) and (current_gear >= 1) and current_gear <= self.gear_number:
            self.current_gear = current_gear
        # The current gear cannot exceed the maximum number of gears
        elif isinstance(current_gear, int) and (current_gear >= 1) and current_gear > self.gear_number:
            print("ERROR: Current gear cannot exceed gear number. Resetting current gear to default (1)")
            self.current_gear = 1
        # The current gear can also not be below 1
        elif isinstance(current_gear, int) and (current_gear < 1) and current_gear <= self.gear_number:
            print("ERROR: Current gear cannot be below 1. Resetting current gear to default (1)")
            self.current_gear = 1
        else:
            print("ERROR: Invalid entry for current_gear; resetting to first gear(default)")
            self.gear_number = 1
        # Our number of wheels needs to be 1, 2, 3, or 4
        if isinstance(wheels, int) and (wheels >= 1) and (wheels <= 4):
            self.wheels = wheels
        # Any number below 1 needs to trigger an error and reset it to the default (2)
        elif isinstance(wheels, int) and (wheels < 1):
            print("ERROR: That's just a pogo-stick. Resetting number of wheels to default number (2).")
            self.wheels = 2
        # Any number below 4 needs to trigger an error and reset it to the default (2)
        elif isinstance(wheels, int) and (wheels > 4):
            print("ERROR: Compensating for something? Too many wheels. Resetting to default number (2).")
            self.wheels = 2
        else:
            print("Invalid number of wheels. Resetting to default number (2).")
            self.wheels = 2
        # We can only accept hand brakes or foot brakes as the types of brakes on our bike
        # I'm including brakes and brake because I don't want anyone to get dinged on a technicality
        if brakes in ["hand brakes", "hand brake", "foot brake", "foot brakes"]:
            self.brakes = brakes
        else:
            print("Invalid type of brakes. Resetting to default (hand brakes)")
            self.brakes = "hand brakes"

    # If you increase your gear, you cannot exceed the gear number
    def increase_gear(self):
        if self.current_gear + 1 <= self.gear_number:
            self.current_gear = self.current_gear + 1
            print(f"The current gear is now {self.current_gear}.")
        # Increasing your current gear beyond the gear number should return an error message and reset your gear to 1
        elif self.current_gear + 1 > self.gear_number:
            print("ERROR: Current gear cannot exceed gear number; resetting to first gear(default).")
            self.current_gear = 1
            print(f"Number of Gears: {self.gear_number}")
            print(f"Current Gear: {self.current_gear}")
            print(f"Number of Wheels: {self.wheels}")
            print(f"Brake Type: {self.brakes}")

    # This function allows you to decrease your gear
    def decrease_gear(self):
        if self.current_gear - 1 >= 1:
            self.current_gear = self.current_gear - 1
            print(f"The current gear is now {self.current_gear}.")
        # If you decrease your gear below 1, you will receive an error message and your gear reset to default (1)
        elif self.current_gear - 1 < 1:
            print("ERROR: Current gear cannot be below 1; resetting to first gear(default)")
            self.current_gear = 1
            print(f"Number of Gears: {self.gear_number}")
            print(f"Current Gear: {self.current_gear}")
            print(f"Number of Wheels: {self.wheels}")
            print(f"Brake Type: {self.brakes}")

    #You should only be able to reset your brakes to either hand brakes or foot brakes
    def set_brakes(self, brakes):
        if brakes in ("hand brakes", "hand brake", "foot brakes", "foot brake"):
            self.brakes = brakes
        # If you don't use one of the prescribed types, you will receive an error and the brakes reset to hand brakes
        else:
            print("ERROR: Invalid brake type. Setting to default ('hand brakes').")
            self.brakes = "hand brakes"

# This function displays the current brake type
    def get_brakes(self):
        print(f"The current brake type is {self.brakes}.")

# This function displays the current gear
    def get_current_gear(self):
        print(f"Current gear is {self.current_gear}.")

# This function resets the current gear to 1
    def reset_current_gear(self):
        self.current_gear = 1
        print("Current gear has been reset to 1.")

# This function gives us the number of gears
    def get_number_of_gears(self):
        print(f"Number of gears is {self.gear_number}.")

# This function allows us to set the number of gears
    def set_gear_number(self, gear_number):
        if isinstance(gear_number, int) and (gear_number >= 1) and (gear_number <= 15):
            self.gear_number = gear_number

        else:
            print("ERROR: Gear must be between integer between 1 and 15, resetting to maximum allowed (15).")
            self.gear_number = 15

# This function allows us to set the number of gears
    def set_current_gear(self, current_gear):
        if isinstance(current_gear, int) and (current_gear >= 1) and (current_gear <= self.gear_number):
            self.current_gear = current_gear
        elif isinstance(current_gear, int) and (current_gear >= 1) and current_gear > self.gear_number:
            print("ERROR: Current gear cannot exceed gear number. Resetting current gear to default (1)")
            self.current_gear = 1
        elif isinstance(current_gear, int) and (current_gear < 1) and current_gear <= self.gear_number:
            print("ERROR: Current gear cannot exceed gear number. Resetting current gear to default (1)")
            self.current_gear = 1
        else:
            print("ERROR: Invalid current gear, resetting to default (1).")
            self.current_gear = 1

# This function allows us to set the number of wheels
    def set_wheel_number(self, wheels):
        if isinstance(wheels, int) and (wheels >= 1) and (wheels <= 4):
            self.wheels = wheels
        else:
            print("Invalid number of wheels. Resetting to default number (2).")
            self.wheels = 2

# This function will give us the current wheel number
    def get_wheel_number(self):
        print(f"The number of wheels is {self.wheels}.")


Jon_bike = Bike(10,10,2, "hand brake")

print(f"Number of Gears: {Jon_bike.gear_number}")
print(f"Current Gear: {Jon_bike.current_gear}")
print(f"Number of Wheels: {Jon_bike.wheels}")
print(f"Brake Type: {Jon_bike.brakes}")
print()
print("Let's try setting and getting the number of gears to 11. Press [ENTER] to continue")
input()
Jon_bike.set_gear_number(11)
Jon_bike.get_number_of_gears()
print()
print("Let's try setting and getting the current gear to 11. Press [ENTER] to continue")
input()
Jon_bike.set_current_gear(11)
Jon_bike.get_current_gear()
print()
print("Let's try increasing the gear past max. Press [ENTER] to continue")
input()
Jon_bike.increase_gear()
print()
print("Let's try decreasing the gear below zero. Press [ENTER] to continue")
input()
Jon_bike.decrease_gear()
print()
print("Let's try setting and getting the number of wheels to 4. Press [ENTER] to continue")
input()
Jon_bike.set_wheel_number(4)
Jon_bike.get_wheel_number()
print()
print("Let's try setting and getting (and failing) the number of wheels to 5. Press [ENTER] to continue")
input()
Jon_bike.set_wheel_number(5)
Jon_bike.get_wheel_number()
print()
print("What about fewer wheels than 1? Will it still fail? Press [ENTER] to continue")
input()
Jon_bike.set_wheel_number(0)
Jon_bike.get_wheel_number()
print()
print("Let's try changing to foot brakes now. Press [ENTER] to continue")
input()
Jon_bike.set_brakes("foot brakes")
Jon_bike.get_brakes()
print()
print("Got any electric brakes? Press [ENTER] to continue")
input()
Jon_bike.set_brakes("electric brakes")
Jon_bike.get_brakes()
print()
print("Let's try setting and getting the current gear to 8. Press [ENTER] to continue")
input()
Jon_bike.set_current_gear(8)
Jon_bike.get_current_gear()
print()
print("Now reset the current gear. Press [ENTER] to continue")
input()
Jon_bike.reset_current_gear()
Jon_bike.get_current_gear()
print()
print()
print("I think that's everything. Thanks Ken!")