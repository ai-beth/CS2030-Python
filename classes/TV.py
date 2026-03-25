#Description: Create a class to control TV operations

class TV:

    #Contructor init methos
    def __init__(self):
        self.channel = 1 # default channel
        self.volumeLevel = 1 # default volume
        self.on = False # off by default

    #Method for TV on
    def turnOn(self):
        self.on = True #TV on


    #method for tv off
    def turnOff(self):
        self.on = False # TV Off

    #Method for getting the channel
    def getChannel(self):
        return self.channel


    #Method for setting the channel
    def setChannel(self, channel):

        #TV needs to be on and the channel range is 1 - 120
        if self.on and 1 <= self.channel <= 120:
            self.channel = channel

    #Method for getting the volume
    def getVolume(self):
        return self.volumeLevel

    #Method for setting the Volume
    def setVolume(self, volumeLevel):

        #TV needs to be on and the volume needs range 1 - 7
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    #Method for channeling up
    def channelUp(self):

        #Check if tv is on and the channel is less than 120
        if self.on and self.channel < 120:
            self.channel += 1

    #Method for channeling down
    def channelDown(self):

        #Check if tv is on and channel is > 1
        if self.on and self.channel > 1:
            self.channel -= 1

    #Method for volume up
    def volumeUp(self):

        #Check if tv is on and volume is < 7
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    #Method to turn vollume down
    def volumeDown(self):

        #Check if the tv is on and volume is greater than 1
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1

            
        
        
