# personal-ai-assistant-robot
This is a personal AI assistant robot. Powered by OpenAI's Realtime API and having the ability to integrate with smart home devices, it can have a conversation in real time, answer questions, perform tasks and move around, all whilst being able to display information and animations on its front facing oled, and control its build in addressable led lights. This inital version (v1) is a basic MVP to test how everything will come together, but future versions will include temperature, light intensity and touch sensors, a camera and an auto charging dock. As this project doesn't require any custom PCB's I have not included any PCB files.

I began this project mainly because I was getting frustrated with my alexa not being able to understand anything more complex than 'set a timer', and now with how advanced LLM's are getting I thought It would be a nice opportunity to create my own version of a home assistant who could actually hold a conversaion but also do everything the alexa could (appart from 'speaker' aspect). All whilst having the enjoyment that comes from working on a project like this.

## The Body (Empty)
<img width="1550" height="1002" alt="topSideView" src="https://github.com/user-attachments/assets/c8710ac6-5989-4444-bfcc-a6535e1a4ae0" />
<img width="1802" height="1100" alt="sideBottomView" src="https://github.com/user-attachments/assets/0861e141-88cd-4451-90b5-9bbd7138ccbd" />
<img width="1406" height="1006" alt="frontBottomView" src="https://github.com/user-attachments/assets/06fcdeb0-3484-4fad-aefe-177b9ae6faf7" />

With this inital design (v1):
- the Raspberry Pi screws into the top (the mouting holes can be seen in the image above)
- the oled slides into two channels behind the opening on the front side
- the speaker sticks behind the grill (double sided tape comes pre applied with the speaker)
- the usb mic sits flush in the circular opening on the fronts side
- the n20 motors are inserted into the two rear wheels to spin the rubber tracks

## Wiring Diagram
Bellow is a wiring diagram to represent how all the components (listed in the BOM) will be wired, I have not included the 7.4v 18650 battery connection to the XL4015 as the wiring there is self explanatory, also the digital to analog converter on the right represents the PCM2704 part as I could not find the part visual anywhere on the internet
<img width="4195" height="2266" alt="WiringDiagram" src="https://github.com/user-attachments/assets/97fb0fba-7560-407d-b7bd-3fc1051d0ecf" />

