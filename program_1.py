# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):    
    miles = 0.0
    miles = kilometers * 0.62137119
    # Return the variable to the calling function
    return round(miles, 5)

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    # Get User Input
    kilometers = float(input("Enter the kilometers: "))
    miles = kilometer_conversion(kilometers)
    print('In miles this distance is: ', miles)
    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    
    # Display the miles
