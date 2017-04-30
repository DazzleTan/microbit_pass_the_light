# microbit_pass_the_light

Microbit "firefly" project inspired by example provided in microbit documentation.

### Requirements:
1. Multiple microbits (I used four)
2. Micropython text editor compatible with microbit.  I used Mu.

### What it looks like in action:

The program assigns ordinal ids to the microbits via a variable.  The program begins when microbit one puts out a message signaling for microbit two to flash.  The microbit flashes and sends a signal to three, three sends a signal to four, and four sends a signal back to one.

Additionally, micro bit four has been given a special privilege: if you press the "a" button on microbit four, all other microbits will light up.


