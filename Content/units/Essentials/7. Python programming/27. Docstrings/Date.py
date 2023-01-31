'''
This module contains a class for representing the date.
It also contains a function for printing the date in a
readable format.
'''
class Date:
    '''
    This class is used to represent a date.

    Attributes:
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.
    '''
    def __init__(self, year, month, day):
        '''
        See help(Date) for accurate signature
        '''
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        '''
        This function is used to return the string representation of the date.

        Returns:
            str: The string representation of the date.
        '''
        return "{0}-{1}-{2}".format(self.year, self.month, self.day)

    def __repr__(self):
        '''
        This function is used to return the string representation of the date.

        Returns:
            str: The string representation of the date.
        '''
        return "{0}-{1}-{2}".format(self.year, self.month, self.day)

    def __eq__(self, other):
        '''
        This function is used to compare the date with other date.

        Args:
            other (Date): The other date to be compared with.

        Returns:
            bool: True if the date is equal to the other date, False otherwise.
        '''
        return self.year == other.year and self.month == other.month and \
            self.day == other.day

    def __lt__(self, other):
        '''
        This function is used to compare the date with other date.

        Args:
            other (Date): The other date to be compared with.

        Returns:
            bool: True if the date is less than the other date, False otherwise.
        '''
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
        return False
        
    
    @staticmethod
    def is_date_valid(year, month, day):
        '''
        This function is used to check if the date is valid.

        Args:
            year (int): The year of the date.
            month (int): The month of the date.
            day (int): The day of the date.

        Returns:
            bool: True if the date is valid, False otherwise.
        '''
        return year >= 0 and month >= 1 and month <= 12 and \
            day >= 1 and day <= 31

    @classmethod
    def from_string(cls, date_as_string: str) -> Date:
        '''
        This function is used to create a date from a string.

        Args:
            date_as_string (str): The string representation of the date.

        Returns:
            Date: The date created from the string.
        '''
        year, month, day = map(int, date_as_string.split('-'))
        return cls(year, month, day)

def display_date(date):
    '''
    This function is used to print the date in a readable format.

    Args:
        date (Date): The date to be printed.
    '''
    print(str(date))