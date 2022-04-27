from datetime import datetime
from bs4 import BeautifulSoup
import re
import requests
import numpy as np
import pandas as pd


class Date:
    '''
    This class is used to represent a date.

    Attributes:
        _day_of_month (tuple): The days in each month of the year
        _month_str (tuple): The names of the months
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.
    '''
    _day_of_month =(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    _month_str = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

    def __init__(self, day: int, month: int, year: int):
        if not self.is_date_valid(day, month, year):
            raise ValueError('Date not valid')

        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return "{0}-{1}-{2}".format(self.day, self.month, self.year)

    def __repr__(self):
        '''
        This function is used to return the string representation of the date.

        Returns:
            str: The string representation of the date.
        '''
        return "{0}-{1}-{2}".format(self.day, self.month, self.year)

    def __eq__(self, other):
        
        
        return self.year == other.year and self.month == other.month and \
            self.day == other.day

    def __lt__(self, other):
        '''
        This function is used to compare the date with other date.

        Args:
            other (Date): The other date to be compared with.

        Returns:
            bool: True if the date is less than the other date,
            False otherwise.
        '''
        if self.year < other.year:
            return True
        elif self.year==other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
        return False

    @staticmethod
    def is_leap_year(year: int) -> bool:
        '''
        This method checks if a year is a leap year

        Args:
            year (int): The year to check
        Returns:
            (bool): True if the year is a leap year, False otherwise
        '''
        return year % 4 == 0

    def is_date_valid(self, day: int, month: int, year: int) -> bool:
        '''
        This method is used to check if the date is valid.

        Args:
            day (int): The day of the date.
            month (int): The month of the date.
            year (int): The year of the date.

        Returns:
            bool: True if the date is valid, False otherwise.
        '''
        current_day = self._day_of_month[month - 1]
        if self.is_leap_year(year) and month == 2:
            current_day += 1

        return year >= 0 and month >= 1 and month <= 12 and \
            day >= 1 and day <= current_day

    @classmethod
    def from_string(cls, date_as_string):
        '''
        This function is used to create a date from a string.

        Args:
            date_as_string (str): The string representation of the date.

        Returns:
            Date: The date created from the string.
        '''
        day = int(date_as_string.split('-')[0])
        month = int(date_as_string.split('-')[1])
        year = int(date_as_string.split('-')[2])
        return cls(day, month, year)

    @classmethod
    def today(cls):
        '''
        This function is used to create a date from a string.

        Args:
            date_as_string (str): The string representation of the date.

        Returns:
            Date: The date created from the string.
        '''
        cur_day = datetime.now()
        day, month, year = cur_day.day, cur_day.month, cur_day.year
        return cls(day, month, year)

    def to_Wiki_Format(self):
        '''
        Returns the date into a format legible by the Wikipedia URL

        Returns:
            (str): String that can be appended to the Wikipedia URL
                   For example 'July_31'
        '''
        return f'{self._month_str[self.month - 1]}_{self.day}'


class Scraper:
    '''
    ### Summary

    Attributes:
        ###
    '''

    def __init__(self):
        self.ROOT = 'https://en.wikipedia.org/wiki/'

    def _get_soup(self, date: str) -> BeautifulSoup:
        # private method, you don't need a docstring
        r = requests.get(self.ROOT + date)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    def _get_birth_header(self, date: str) -> BeautifulSoup:
        # Private
        soup = self._get_soup(date)
        span = soup.find(
            'span', {'class': 'mw-headline'}, text=re.compile("Births"))
        # If the list is empty because it didn't find anything
        if not span:
            raise ValueError('The given date has no birth data')
        h2 = span.find_parent()
        return h2

    def _get_celebrity_list(self, date: str) -> list:
        # Add <ul> tags until you find the next <h2> tag
        next_node = self._get_birth_header(date)
        celebrities_list = []
        while True:
            next_node = next_node.find_next_sibling()
            if getattr(next_node, 'name') == 'ul':
                celebrities_list.extend(next_node.find_all('li'))
            elif getattr(next_node, 'name') == 'h2':
                break
        return celebrities_list

    def _clean_li(self, li: BeautifulSoup) -> str:
        # Private method
        li_complete = li.text.split('–')
        name_complete = li_complete[1].split(',')
        name = name_complete[0].strip()
        return name

    def get_celebrities(self, date: str = None) -> list:
        '''
        Add a proper docstring
        '''
        if date is None:
            date = 'January_1'
        cel_list = self._get_celebrity_list(date)
        celebrities = []
        for li in cel_list:
            celebrities.append(self._clean_li(li))
        return celebrities


if __name__ == '__main__':
    date_object = Date(27, 3, 1991)
    scraper = Scraper()
    celebrities = scraper.get_celebrities('February_30')
    print(celebrities)
