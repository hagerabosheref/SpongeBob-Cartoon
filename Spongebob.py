import turtle ,os
from pygame import mixer
import time


#################
#screen 
sc=turtle.Screen()
sc.title("Spongebob")
sc.setup(1500,700)
sc.bgcolor("#FFFFFF")
sc.bgpic("images/background.png")


#################
#audio function
def audio (file):
    mixer.init() 
    mixer.music.load(file) # Loading the song
    mixer.music.set_volume(0.7) # Setting the volume
    mixer.music.play() # Start playing the song


#################
#music
audio("sound/spongebob.mp3")


#################
# title story
def titleStory():
    time.sleep(2)
    sc.bgpic("images/bubbles.png")
    sc.bgcolor(0.60160, 0, 0.99220)
    title=turtle.Turtle()
    title.hideturtle()
    title.color("#FFFFFF")
    title.write("Friendship Day",align="center",font=("arial",50,"bold"))
    audio("sound/FriendshipDay.wav")
    time.sleep(3)
    title.clear()
    story()


#################
#story
def story():
    sc.bgpic("nopic")
    sc.bgcolor("#E0EAFC")
    sc.bgpic("images/story.png") # i made it by adobe illustrator


    #################
    #spongebob
    spongebob=turtle.Turtle()
    spongebob.up()
    spongebob.goto(465,20)
    sc.addshape(os.path.expanduser("~/Desktop/Spongebob Cartoon/images/spongebobpic.gif"))
    spongebob.shape(os.path.expanduser("~/Desktop/Spongebob Cartoon/images/spongebobpic.gif"))
    time.sleep(2)
    audio("sound/audioOne.wav")


    #################
    #text
    text=turtle.Turtle()
    text.color("#000000")
    text.up()
    text.hideturtle()
    text.goto(0,-300)
    text.write("Today is Friendship Day.I will go to Squidward and Patrick's house to find out what they brought me and to give them their gifts",align="center",font=("arial",15,"bold"))
    

    for i in range (9):
        ycurrent=spongebob.ycor()
        spongebob.sety(ycurrent-20)
        time.sleep(0.5)
        
    for i in range(19):
        spongebob.bk(24)
        time.sleep(0.5)
    
    text.clear()
    for i in range(5):
        ycurrent=spongebob.ycor()
        spongebob.sety(ycurrent+20)
        time.sleep(0.5)


    audio("sound/audioTwo.wav")   
    text.write("Hello Squidward. Happy Friendship Day. What did you bring me on Friendship Day?",align="center",font=("arial",15,"bold"))
    time.sleep(5)
    text.clear()


    #################
    #Squidward
    Squidward=turtle.Turtle()
    Squidward.up()
    Squidward.goto(20,20)
    sc.addshape(os.path.expanduser("~/Desktop/Spongebob Cartoon/images/Squidward.gif"))
    Squidward.shape(os.path.expanduser("~/Desktop/Spongebob Cartoon/images/Squidward.gif"))
    audio("sound/audioThree.wav")
    text.write("Hello SpongeBob.Happy friendship day.This gift is for you.",align="center",font=("arial",15,"bold"))
    time.sleep(5) 
    text.clear()
    audio("sound/audiosix.wav")
    text.write("Thanks. this gift is for you.",align="center",font=("arial",15,"bold"))
    time.sleep(2) 
    text.clear()
    Squidward.hideturtle()


    for i in range(5):
        ycurrent=spongebob.ycor()
        spongebob.sety(ycurrent-20)
        time.sleep(0.5)

    for i in range(19):
        spongebob.bk(24)
        time.sleep(0.5)

    for i in range(5):
        ycurrent=spongebob.ycor()
        spongebob.sety(ycurrent+20)
        time.sleep(0.5)


    audio("sound/audiofour.wav")
    text.write("Hi Patrick.Happy friendship day.What did you bring me on friendship day?",align="center",font=("arial",15,"bold"))
    time.sleep(5) 
    text.clear()
 

    #################
    #patrick
    Patrick=turtle.Turtle()
    Patrick.up()
    Patrick.goto(-450,20)
    sc.addshape(os.path.expanduser("~/Desktop/Spongebob Cartoon/images/Patrickpic.gif"))
    Patrick.shape(os.path.expanduser("~/Desktop/Spongebob Cartoon/images/Patrickpic.gif"))
    audio("sound/audiofive.wav")
    text.write("Hello SpongeBob.Happy friendship day.This gift is for you.",align="center",font=("arial",15,"bold"))
    time.sleep(5)
    text.clear() 
    audio("sound/audiosix.wav")
    text.write("Thanks. this gift is for you.",align="center",font=("arial",15,"bold"))
    time.sleep(2)
    text.clear()


    #################
    #the end
    time.sleep(2)
    spongebob.hideturtle()
    Patrick.hideturtle()
    sc.bgpic("images/bubbles.png")
    sc.bgcolor(0.60160, 0, 0.99220)
    end=turtle.Turtle()
    end.hideturtle()
    end.color("#FFFFFF")
    end.write("THE END",align="center",font=("arial",50,"bold"))
    audio("sound/end.mp3")


turtle.ontimer(titleStory,44*1000)   #44*1000 
turtle.done()


