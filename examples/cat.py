class Cat:
    def __init__(self, name, colour, status = "free"):
        #Your code here
        #Add code that sets the name and colour of the cat based on the given parameters
        self.name = name
        self.colour = colour
        #sets the status of the cat as "free"
        self.status = status
    
    def collect(self):
        #Your code here
        #Add code that sets the status of the cat as "in collection"
        self.status = "in collection"

        #print a success message
        print(f"Cat {self.name} added to collection!")


    def rename(self):
        #your code here
        #Add code that:
        #1. Asks user for a new name for the cat
        new_name = input("Change the name of the cat: ")
        #2. Changes the name of the cat to the name given by user
        self.name = new_name
        print(f"Cat {self.name} succesfully renamed")