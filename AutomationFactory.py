class AutomationFactory:
    def __init__(self,width,height,length,mass):
        #Edge case for if values are negative
        if width < 0 or height < 0 or length < 0 or mass < 0:
            return ValueError ("Values cannot be negative")
        
        self.width = width
        self.height = height
        self.length = length
        self.volume = width * height * length
        self.mass = mass

    def is_bulky(self):
        return (
            self.volume >= 1000000 or 
            self.width >= 150 or 
            self.height >= 150 or
            self.length >= 150
        )
    
    def is_heavy(self):
        return self.mass >= 20

    def sort(self):
        bulky = self.is_bulky()
        heavy = self.is_heavy()

        if bulky and heavy:
            return "REJECTED"
        if bulky or heavy:
            return "SPECIAL"
        else:
            return "STANDARD"
        
#TestCases
package1 = AutomationFactory(100,150,60,10)
print(package1.sort())  

package2 = AutomationFactory(300,300,300,20)
print(package2.sort())

package3 = AutomationFactory(40,40,40,10)
print(package3.sort())
