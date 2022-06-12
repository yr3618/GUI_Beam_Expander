# GUI_Beam_Expander
This is the code that was created for the LEGO variable beam expander presented in my 4th year Master's thesis. The user interface has multiple aims:
1-Facilitate the use of the beam expander
2-Control the electronic components in the beam expander

This code runs on Raspberry Pi. Raspberry Pi are nano-computers, and once they are connected to a screen and keyboard, can be used to run this code. 


Because of a failure to connect two identical distance sensor with the Pi, the code is not complete. The GUI is created (GUI.py), and the code that reads value from the distance sensor VL53l0X and moves the motor accordingly is also functional. Due to lack of time, a second distance sensor was not purchased or tried.  Future work will include reading values from these new sensor and moving the second motor according to the sensor readings. Then, the moving_motor.py file needs to be changed into a function (for now it is a simple python file, so it can be tested easily) that will be called by the GUI when the user uses it.

The GUI was multiple windows. It offers the option to use an interferometer (not available yet). This is a good device to try to build with LEGO after beam expanders.

The following libraries are necessary to run current codes:

-Tkinter: the library used to create the GUI.

-Pillow: python imaging library, to visualise images. Pillow is used to display the LOGO created for this GUI. The LOGO is shared in this git hub repository. It was created using canva.com

-RPIO, the GPIO module for the Raspberry Pi.

-busio: library to interact via i2c.

-adafruit_vl53l0x: library to read values from the distance sensor vl53l0x

-csv: to read the csv files containing all the references values for the distance between the lenses

-time




