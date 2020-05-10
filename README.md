# Pick-and-Place-3-DOF-Robotic-Arm
This is a project for the design of a 3 dof robotic arm with opencv color detection


## 1. STAGES OF THE PROJECT
###### 1.1. Basic Task:
To make a robotic arm with three servo motors which can move to a coordinate given to it by the user.
###### 1.2. Advanced Task 1:
This included finding the pixel values of the centroid of any object (having a contradicting colour with the background) using OpenCV-Python.
###### 1.3. Advanced Task 2:
This included distinguishing between two colours ( I used red and blue) and finding the pixel values of their centroids separately so that the arm could pick and place the objects in two different positions.


## 2. SOFTWARE REQUIREMENTS
The basic software or libraries that needed to be installed are:
###### • Python: I used Python IDLE (version 2.7.13). Basic knowledge of python and its syntax is a must for this project.
###### • Arduino: The Arduino software is needed to control the microprocessor (ATMega32).
###### • OpenCV: The OpenCV library downloaded from their official site. OpenCV (Open Source Computer Vision) is a library of programming functions mainly aimed at real-time computer vision.
###### • Numpy: NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices.

## 3. HARDWARE REQUIREMENTS
The basic hardware components that are required:
###### 3.1. ServoMotors
3.1.1 Futaba (S3003)
-Torque (4.2 kg-cm)
- Used as the elbow motor
- controlled by the TIMER0

3.1.2 GO TECK (GS-5515 MG)
-Torque (13 kg-cm)
-Used as the shoulder motor
- Controlled by the OCR1A value of TIMER1

3.1.3 HSR(5990 TG)
-Torque (23 kg-cm)
- used as the base motor
- Controlled by the OCR1B value of TIMER1.

###### 3.2. L293D motor driver:
The L293D Motor Driver is used to control the electromagnet.
###### 3.3. Webcamera:
I used a Logitech C170 Webcam for taking up the image.
###### 3.4. Microcontroller: 
Arduino Uno board is used for the project. The Arduino UNO is a widely used open-source microcontroller board based on the ATmega328P microcontroller.


## 6. Configuration of the TIMERS
Timers can be used as a waveform generator if the OC1A and OC1B pins are set as output. The TCCR registers of the timer determine how the waveform generator works. When the TCNTn register reaches the top or compare match, the waveform generator is informed. Then the waveform generator changes the state of the OC0 pin according to the mode.
###### 6.1. TIMER1:
TIMER1 has been set to the fast PWM mode. The timer counts up until it reaches the top( here the ICR1) and then rolls over to zero. For the fast PWM mode, the WGM11, WGM12 and WGM13 bits are set to 1. The COM1A1 and COM1B1 bits are set to get a non inverted PWM. In this mode the OC1A and OC1B values clear on Compare match, and the output is high when the compare level is above the waveform level and low otherwise.
###### 6.2. TIMER0:
The Timer0 is also used in fast PWM non- inverted mode but with a prescaler of 256. The COM0A1 bit has been set for the non-inverted mode. WGM00 and WGM01 are set for the fast PWM mode.
###### 6.3. OCR values and servo angle:

6.3.1. GoTeck(GS-5515MG)

6.3.1.1. 0 deg =150(OCR1A)

6.3.1.2. 90 deg=370(OCR1A)

6.3.1.3. 180 deg=590(OCR1A)

6.3.2. HSR 5990 TG

6.3.2.1. 0 deg=180(OCR1B)

6.3.2.2. 90 deg=390(OCR1B)

6.3.2.3. 180 deg=600(OCR1B)

6.3.3. Futaba S3003

6.3.3.1. 0 deg = 50 (OCR0A)

6.3.3.2. 90 deg = 100 (OCR0A)

6.3.3.3. 180 deg = 150(OCR0A)


## 7. ADVANCED TASK 1
###### 7.1. Objective: 
To get the pixel values of the centroid of any shape of an object.
###### 7.2. Approach: 
Firstly, here the image is being captured by an external camera and pre-processed in python compiler using opencv library.
The outline of the object is being traced and later the center of the contour i.e. the centroid location is determinrd.

7.2.1. The image is converted to grayscale.

7.2.2. Blurring to reduce the background noise so as to percept the object boundary clearly.

7.2.3. Binarization(here used threshing)

7.2.4. Compute the centre of the contour.

## 9. ADVANCED TASK 2
###### 9.1.Objective:
To differentiate between two colours and find the centroid separately
###### 9.2. Approach:
• Blurred the image using the cv2.Gaussianblur command

• The blurred image is then threshed with a certain threshold whose value is being decided on the lightning condition.

• Here the image is not converted to grayscale but to HSV

• The HSV converted image will be handled twice separately, one where it will detect only blue colour and the other when it will detect only red colour.

• For the colour detection, lower and upper ranges are fixed for each colour.

• The images are then separately dealt with for finding the contours.


