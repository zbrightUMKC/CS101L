import time # We will use this to make our clock count seconds accurately
class Clock():
    # We are building a clock class that will elt us build clock objects that act like real life clocks.
    def __init__(self, hour = 0, minute = 0, second = 0, mode = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.mode = mode # mode 0 = standard 23-hour clock, mode 1 = 12-hour am/pm
    def __str__(self):
        #Supports printing for both clock modes
        if self.mode == 0:
            return '{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second)
        else: # 12am and 12pm work as edge cases so I had to add a seperate branch for those hours
            if self.hour > 12:
                return '{:02}:{:02}:{:02} pm'.format((self.hour - 12), self.minute, self.second)
            elif self.hour == 12:
                return '{:02}:{:02}:{:02} pm'.format(12, self.minute, self.second)
            elif self.hour == 0:
                return '{:02}:{:02}:{:02} am'.format(12, self.minute, self.second)
            else:
                return '{:02}:{:02}:{:02} am'.format(self.hour, self.minute, self.second)
    def tick(self):
        # Increments clock object, nested if-else statments ensure clock math is conducted correctly
        if self.second < 59:
            self.second += 1
        else:
            self.second = 0
            if self.minute < 59:
                self.minute += 1
            else:
                self.minute = 0
                if self.hour < 23:
                    self.hour += 1
                else:
                    self.hour = 0
if __name__ == '__main__':
    # Get user input and set to attributes of clock instance
    hour = int(input('What is the current hour ==> '))
    minute = int(input('What is the current minute ==> '))
    second = int(input('What is the current second ==> '))
    clock = Clock(hour, minute, second, 1)
    # Time on Clock object will start from user inputted values, we increment the clock, and in real time print the updated time every second.
    while True:
        print(clock)
        clock.tick()
        time.sleep(1)
        # This loop is infinite, program must be stopped by some means outside the program