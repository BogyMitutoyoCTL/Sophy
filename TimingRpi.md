None of the Raspberry Pi models has RTC (Real-time-clock).
So, the RPi takes time from a network time server or from user input at boot time.
A real-time hardware clock battery backup, such as the DS1307, may be added.

When connected to the internet the RPi can be accurate to the milliseconds, but not to the microseconds.
For our project this will be enough to take a network time server as a timing programme.
We estimate accuracy to about 16 milliseconds.    
