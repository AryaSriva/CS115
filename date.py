'''
Created on 12/2/22
@author:   Aryaman
Pledge:    I pledge my honor that I have abided by the Stevens Honor System


CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year as the
            calling object(self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent same calendar date,
            whether or not they are in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def tomorrow(self):
        '''changes the calendar date of self to the calendar date of the next day'''
        DIM = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        self.day += 1
        if self.isLeapYear() and self.month == 2:
            if self.day == 30:
                self.day = 1
                self.month += 1
        else:
            if self.day == DIM[self.month] + 1:
                if self.month == 12:
                    self.day = 1
                    self.month = 1
                    self.year += 1
                else:
                    self.month += 1
                    self.day = 1

    def yesterday(self):
        '''changes the calendar date of self to the calendar date of the previous day'''
        DIM = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        self.day -= 1
        if self.isLeapYear() and self.month == 3:
            if self.day == 0:
                self.day = 29
                self.month -= 1
        else:
            if self.day == 0:
                if self.month == 1:
                    self.day = 31
                    self.month = 12
                    self.year -= 1
                else:
                    self.month -= 1
                    self.day = DIM[self.month]

    def addNDays(self, N):
        '''changes the calendar date of self to the calendar date after N days'''
        print(self)
        for i in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        '''changes the calendar date of self to the calendar date N days prior'''
        print(self)
        for i in range(N):
            self.yesterday()
            print(self)

    def isBefore(self, d2):
        '''Checks if self is a calendar date before d2, if it is, return True, otherwise return False'''
        if self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month < d2.month:
                return True
            elif self.month == d2.month:
                if self.day < d2.day:
                    return True
        else:
            return False

    def isAfter(self, d2):
        '''Checks if self is a calendar date after d2, if it is, return True, otherwise return False'''
        if self.isBefore(d2) or self.equals(d2):
            return False
        else:
            return True

    def diff(self, d2):
        '''returns the number of days between self and d2 which
            is an integer representing self - d2'''
        day1 = self.copy()
        day2 = d2.copy()
        i = 0
        while day1.isBefore(day2):
            day1.tomorrow()
            i += 1
        while day1.isAfter(day2):
            day2.tomorrow()
            i += 1
        if self.isBefore(d2):
            return i*-1
        else:
            return i

    def dow(self):
        '''returns the day of the week of the calendar date of self'''
        diffFromKnown = {0:'Wednesday', 1:'Thursday', 2:'Friday', 3:'Saturday',
                         4:'Sunday', 5:'Monday', 6:'Tuesday'}
        knownDate = Date(11, 9, 2011)
        return diffFromKnown[self.diff(knownDate)%7]
        

    
            
        
        
