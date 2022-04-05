class clockTime:
    hours = 0
    minutes = 0
    seconds = 0

    def setHour(self, hours):
        self.hours = hours

    def setMinutes(self, minutes):
        self.minutes = minutes

    def setSeconds(self, seconds):
        self.seconds = seconds

    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def showTime(self):
        return '{}:{}:{}'.format(self.hours,self.minutes,self.seconds)

try:
    hours = int(input('Enter Hours: '))
    if hours not in range(0,23):
        raise Exception
    minutes = int(input('Enter Minutes: '))
    if minutes not in range(0,59):
        raise Exception
    seconds = int(input('Enter Seconds: '))
    if seconds not in range(0,59):
        raise Exception

    clock = clockTime()
    clock.setHour(hours)
    clock.setMinutes(minutes)
    clock.setSeconds(seconds)
    print('The time is', clock.showTime())

except:
    print('Invalid Input')