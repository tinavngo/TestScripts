class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    
    # Converting height numbers to string
    def __str__(self):
        output = str(self.feet) + " feet," + str(self.inches) + " inches"
        return output
    
    # Creating the method to subtract
    def __sub__(self, other):
        # Converting both objects' height into inches - A = 69, B = 45
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        # Subtracting total inches - 24
        total_height_inches = height_A_inches - height_B_inches

        output_feet = total_height_inches // 12

        output_inches = total_height_inches - (output_feet * 12)

        return Height(output_feet, output_inches)
    

person_A_height = Height(5, 9)
person_B_height = Height(3, 9)

height_difference = person_A_height - person_B_height
print("Total height is: ", height_difference)