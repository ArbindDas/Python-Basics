class Student:
    
    # ---------- Default constructor ----------
    def __init__(self):
        # Initialize default values for a new Student object
        self.id = 1            # Default ID
        self.name = "Arbind"   # Default name
        self.password = "12333" # Default password

    # ---------- Class method as a parameterized constructor ----------
    @classmethod
    def with_details(cls, id, name, password):
        # cls() calls the default constructor to create a new Student object
        obj = cls()            
        
        # Overwrite the default values with the values provided
        obj.id = id           
        obj.name = name       
        obj.password = password  
        
        # Return the newly created object with custom values
        return obj            

    # ---------- Method to print object attributes ----------
    def printValues(self):
        print(self.id)        # Print ID of the student
        print(self.name)      # Print name of the student
        print(self.password)  # Print password of the student

# ---------- Create a Student object using the parameterized constructor ----------
student1 = Student.with_details(1, "Arbind", "dfdsfdfd")  

# ---------- Print the values of the object ----------
student1.printValues()
