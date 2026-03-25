#Description +: Testing hte TV Class

#import TV
from TV import TV

#Create a main function
def main():
    
    #Create a TV object
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)


    #create a seconf tv object
    tv2 = TV()
    tv2.turnOn
    tv2.channelUp()
    tv2.setChannel(3)
    tv2.volumeUp
    tv2.volumeUp()

    #Display tv1 status
    print(f"Tv1 channel is {tv1.getChannel()} and \
volume level is {tv1.getVolume()}. \n")

    print(f"Tv2 channel is {tv2.getChannel()} and \
volume level is {tv2.getVolume()}. \n")

#invoke main
main()

          

    
