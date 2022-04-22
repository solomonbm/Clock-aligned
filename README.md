# Clock-aligned
The following Python program I wrote in order to find the answer, and illustrate it nicely, to the problem I once thought about, which is - in which time of the day on an analog clock, which is continuous in regards to the seconds hand’s movement, will the three hands be on a one straight line (you can imagine why this isn’t a straight forward question).
Most of the code are bits and pieces I found online, but there was still a lot of work that needed to be done.
All the calculations, and the setup of the graphic image of the clock (which is just a couple of circles and lines put together on a plane) are not straight forward, but pretty neat in my opinion. This program uses "CodeSculptor's" simplegui module. 
Enjoy! 

In order to run this program, you need to do the following:
####1)	Go to http://www.codeskulptor.org/
####2)	Delete all the code from the code section (on the left)
####3)	Copy the code from the py file attached (clock_aligned.py) to the code section
####4)	Click the triangle “Play” button on the top left (above the code section)
####5)	Click “Start”, and the clock will start moving at around 10 times faster than an ordinary clock, and will run until the 6 hour mark (in order not to exhaust you too much), whilst printing on the left hand side of the small screen the time at which the three hands (seconds, minuets and hours) are aligned.
####6)	The accuracy is for 360 slices of the circle, meaning that two hands are on the same line if they share the same ‘slice’ out of the 360 slices, or their slices are 180 degrees from one another.  

![clock-aligned-screenshot](https://cloud.githubusercontent.com/assets/21333475/20100730/6d0ea50c-a5c7-11e6-8003-789efde9ce1d.png)
