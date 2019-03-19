from microbit import *

display.scroll("Hello, MicroPython!")






from microbit import*
display.show(Image.SKULL)






from microbit import *

boat = Image("05050:"
             "05050:"
             "05050:"
             "99999:"
             "09990")

display.show(boat)

shopping=["Eggs","BAcon","Tomatoes"]
Primes=[2,3,5,7,11,13,17,19]
mixed up list=["hello",1.234,Image.HAPPY]






from microbit import *

boat1 = Image("05050:"
              "05050:"
              "05050:"
              "99999:"
              "09990")

boat2 = Image("00000:"
              "05050:"
              "05050:"
              "05050:"
              "99999")

boat3 = Image("00000:"
              "00000:"
              "05050:"
              "05050:"
              "05050")

boat4 = Image("00000:"
              "00000:"
              "00000:"
              "05050:"
              "05050")

boat5 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "05050")

boat6 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")

all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
display.show(all_boats, delay=200)

could make an image fade in and out using the the dimfunction of the LED going bright to less bright then back to bright*






from microbit import*
sleep(5000)
display.show(str(button_a.get_presses()))







from microbit import*
while running_time()<10000:
    display.show(Image.ASLEEP)
display.show(Image.SURPRISED)






from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        break
    else:
        display.show(Image.SAD)

display.clear()






from microbit import*
import random
names=["Mary", "Bill", "Kam"]
display.scroll(random.choice(names))






from microbit import*
import random
display.scroll(str(random.randint(1,6)))

because of the while true we added a button must be pressed for anything to happen*





from microbit import *
import random

random.seed(1337)
while True:
    if button_a.was_pressed():
        display.show(str(random.randint(1, 6)))






 from microbit import *

while True:
            reading = accelerometer.get_x()
            if reading > 20:
                display.show("R")
            elif reading < -20:
                display.show("L")
            else:
                display.show("-")





from microbit import*
while True:
    gesture=accelerometer.current_gesture()
    if gesture=="face up":
        display.show(Image.HAPPY)
    else:
        display.show(Image.ANGRY)





from microbit import *
import random

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it"
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

while True:
    display.show("8")
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(answers))


if you wanted an always positive answere you divide the list into positve and negative then set to display random of positve when button a is pressed and negative when b is pressed*







