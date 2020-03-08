'''
Created on 12/02/19
@author:   Jonathan Joshua
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System." - Jonathan Joshua

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
        '''Returns a new object with the same month, day, year as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date, whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
        self.day == d2.day

    def tomorrow(self):
        '''change the calling object so
that it represents one calendar day after the date it originally represented. This means
that self.day will definitely change. What's more, self.month and self.year might change.'''
        DIM = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        self.day += 1
        if self.isLeapYear():
            DIM[2] = 29
        if self.day > DIM[self.month]:
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        return self

    def yesterday(self):
        '''change the calling object
so that it represents one calendar day before the date it originally represented.
Again, self.day will definitely change, and self.month and self.year might change.'''
        DIM = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        self.day -= 1
        if self.isLeapYear():
            DIM[2] = 29
        if self.day < 1:
            self.day = DIM[self.month-1]
            if self.month == 1:
                self.month = 12
                self.year -= 1
            else:
                self.month -= 1
        return self

    def addNDays(self, N):
        '''should not return anything. Rather, it should change the calling object so that it
represents N calendar days after the date it originally represented.'''
        i = 0
        print self()
        while i < N:
            self.tomorrow()
            print self()
            i += 1

    def subNDays(self, N):
        '''should not return anything. Rather, it should change the calling object so that it
represents N calendar days before the date it originally represented. You might consider
using yesterday and a for loop to implement this!'''
        i = 0
        print self()
        while i < N:
            self.yesterday()
            print self()
            i += 1

    def isBefore(self, d2):
        '''should return True if the calling object is a calendar date before the input
named d2 (which will always be an object of type Date). If self and d2 represent the same day,
this method should return False. Similarly, if self is after d2, this should returnFalse.'''
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
        '''should return True if the calling object is a calendar date after the input
named d2 (which will always be an object of type Date). If self and d2 represent the same day,
this method should return False. Similarly, if self is before d2, this should returnFalse.'''
        if self.equals(d2):
            return False
        elif self.isBefore(d2):
            return False
        else:
            return True

    def diff(self, d2):
        '''should return an integer representing the number of days between self and d2.
You can think of it as returning the integer representing 
self - d2'''
        if self.equals(d2):
            return 0
        date1 = self.copy()
        date2 = d2.copy()
        days = 0
        while date1.equals(date2) == False:
            if date1.isBefore(date2):
                date1.tomorrow()
                days -= 1
            else:
                date2.tomorrow()
                days += 1
        return days

    def dow(self):
        '''should return a string that indicates the day of the week (dow) of the object (of
type Date) that calls it. That is, this method returns one of the following strings: ‘Monday’,
‘Tuesday’, ‘Wednesday’, ‘Thursday’, ‘Friday’, ‘Saturday’, or ‘Sunday’.'''
        DOW = ['Wednesday','Thursday','Friday','Saturday',"Sunday","Monday","Tuesday"]
        known = 3
        kdate = Date(11,9,2011)
        day = self.diff(kdate) 
        days = day % 7
        print days
        return DOW[days]
