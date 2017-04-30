import radio
import random
from microbit import display, Image, button_a, button_b, sleep

# Create the "flash" animation frames. Can you work out how it's done?
myflash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# The radio won't work unless it's switched on.
radio.on()

# Event loop.
while True:
    # Button A sends a "flash" message.
    if button_a.was_pressed():
        radio.send('four')  # a-ha
    if button_b.was_pressed():
        radio.send('fire')
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == 'three' or incoming == 'fire':
        incoming = 'nothing'
        # If there's an incoming "flash" message display
        # the firefly flash animation after a random short
        # pause.
        sleep(random.randint(50, 350))
        display.show(myflash, delay=100, wait=False)
        # Randomly re-broadcast the flash message after a
        # slight delay.
        sleep(3000)
        radio.send('four')
        #if random.randint(0, 9) == 0:
            #sleep(500)
            #radio.send('flash')  # a-ha
    