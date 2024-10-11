class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    
    # Converting height numbers to string
    def __str__(self):
        output = str(self.feet) + " feet," + str(self.inches) + " inches"
        return output
    
    def __gt__(self, other):
        # Converting both objects' height into inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        return height_A_inches > height_B_inches
    
    def __ge__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A >= height_inches_B
    
    def __ne__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A != height_inches_B
    
print( Height(4, 6) > Height(4, 5) )    # Returns true
print( Height(4, 5) >= Height(4, 5) )   # Returns true
print( Height(5, 9) != Height(5, 10) )  # Returns true