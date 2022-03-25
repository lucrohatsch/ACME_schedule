
class Person():
    def __init__(self,name :str) -> None:
        """
        Person has a name and a schedule dict
        """
        self.name=name
        self.schedule={}
    
    def works(self,day :str, hours :list)->None:
        """
        Adds the time range for the given day.
        """
        self.schedule[day] = hours