import radio
import random

#The following import statement may look new to you
#We are merely specifying the functions in the library that will be used
#Rather than preceding library function calls with "microbit.", we just use the name "button_a" for instance.
from microbit import display, Image, button_a, sleep

# my_id is the id of this microbit.  Call id is the next microbit in the ordinal sequence
# when assigning the last microbit's call_id, be sure to assign the value of the first microbit! (ie. if 4 are being used, microbit four will call microbit 1)
my_id = 'one'
call_id = 'two'
everyone_called = 'fire'

# Create the "flash" animation frames. Can you work out how it's done? Me neither! still working on it.
myflash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# The radio won't work unless it's switched on.
radio.on()

# Event loop.
while True:
    # Button A sends a call to the next microbit in sequence.  Used to kick off program
    if button_a.was_pressed():
        radio.send(call_id)
    # Button B sends a call out to all other microbits to light up.
    if button_b.was_pressed():
        radio.send(everyone_called)
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == my_id or incoming == everyone_called:
        incoming = 'nothing'
        sleep(random.randint(50, 350))
        display.show(myflash, delay=100, wait=False)
        sleep(1000)
        radio.send(call_id)

