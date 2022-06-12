# GUI_Beam_Expander
This is the code that was created for the LEGO variable beam expander presented in my 4th year Master's thesis. The user interface has multiple aims:
1-Facilitate the use of the beam expander
2-Control the electronic components in the beam expander

This code runs on Raspberry Pi. Raspberry Pi are nano-computers, and once they are connected to a screen and keyboard, can be used to run this code. 

The following libraries are necessary to run the code:
-Tkinter: the library used to create the GUI.
-Pillow: python imaging library, to visualise images. Pillow is used to display the LOGO created for this GUI. 
The LOGO is shared in this git hub repository. It was created using canva.com
-RPIO, the GPIO module for the Raspberry Pi.
-busio: library to interact via i2c.
-adafruit_vl53l0x: library to read values from the distance sensor vl53l0x
-csv: to read the csv files containing all the references values for the distance between the lenses
-time


Note: it is important to use the line:


