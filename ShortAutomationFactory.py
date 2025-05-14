def sort(width,height,length,mass):
    #Edge case to avoid negative values
    if width < 0 or height < 0 or length < 0 or mass < 0:
        return ValueError ("Input values can't be negative")
    
    #volume to calculate dimension of package in cm^3
    volume = width * height * length
    #If its bulky width,height,length in cm
    bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    #if its heavy mass in kg
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
    

#Test Cases
print(sort(100,150,60,10))
print(sort(300,300,300,20))
print(sort(40,40,40,10))