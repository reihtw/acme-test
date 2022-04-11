class WorkHour:
    
    def __init__(self, employee: str,  workhour_string: str) -> None:
        
        day, hours = workhour_string[:2], workhour_string[2:]
        
        starthour, endhour = hours.split('-')
        
        self.__employee = employee
        self.__day = day
        self.__starthour = self.__hour_conversor(starthour)
        self.__endhour = self.__hour_conversor(endhour)
    
    @property
    def employee(self):
        return self.__employee
    
    @property
    def day(self):
        return self.__day
    
    @property
    def starthour(self):
        return self.__starthour
    
    @property
    def endhour(self):
        return self.__endhour
    
    def __hour_conversor(self, hour: str) -> int:
        """Convert a hour in a string format to int

        Args:
            hour (str): hour in a string format '10:00'

        Returns:
            int: hour in int format 1000
        """
        hour, min = hour.split(':')
        hour_int = int(hour) * 100 + int(min)
        return hour_int
    
    def get_relations(self, workhours_list: list, relations_dict: dict):
        """Method to find if the employee workhour was the same time frame as the other employees in a list,
        and save the relations found in a dictionary.

        Args:
            workhours_list (list): list of the workhours already found in the file
            relations_dict (dict): dictionary of the workhours relations and their counters 
        """
        
        if self in workhours_list:
            # it will return all the indexes of the same workhours with the same time frame on the list
            occurrances = [index for index, item in enumerate(workhours_list) if item == self]
            
            for o in occurrances:
                other = workhours_list[o]
                
                # checking if it is a workhour of a different employee
                if self.employee == other.employee:
                    continue
                
                # creates the relation string - Example: ASTRID-RENE
                relation = f'{self.employee}-{other.employee}'
                
                # if the relation workhour was found before, it will increment the counter
                # otherwise it will create a new key on relations dictionary and start its 
                # counter at 1.
                if relation in relations_dict:
                    relations_dict[relation] += 1
                else:
                    relations_dict[relation] = 1
    
    def __eq__(self, __o: object) -> bool:
        """Method to compare if a workhour has the same time frame as the other.

        Args:
            __o (WorkHour): other workhour object to be compared

        Returns:
            bool: Returns true if the employees have been at the office within the same time frame
        """
        
        if self.day != __o.day:
            return False
        
        # Put the starthour and endhour of both objects in a list and then sort it
        # Example:
        #   [1000, 900, 1200, 1100] -> [900, 1000, 1100, 1200]
        hours_list = [self.starthour, __o.starthour, self.endhour, __o.endhour]
        hours_list.sort()
        
        # If they have the same time frame the result will be [starthour, starthour, endhour, endhour]
        # If they don't the result will be [starthour, endhour, intialhour, endhour]
        if self.starthour == hours_list[2] or __o.starthour == hours_list[2]:
            return False

        return True    
    
    def __repr__(self) -> str:
        return f'{self.day}{self.starthour}-{self.endhour}'
    
    