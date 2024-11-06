from transformers import pipeline

nlp_QA = pipeline("question-answering", model = "bert-large-uncased-whole-word-masking-finetuned-squad")

context = """
Arduino UNO R3 is a microcontroller board developed by Arduino. It is an adaptable board made for tasks that need a tiny form factor. The Arduino UNO's salient characteristics and details are shown below:
Microcontroller: The ATmega328P microcontroller, which is also utilized in the Arduino Nano, is generally used in the Arduino UNO R3. This microcontroller runs at 16 MHz and features 32KB of flash memory, 2KB of SRAM, and 1KB of EEPROM for storing programs.
Digital and Analog I/O: The UNO R3 has 6 analog input pins and 14 digital input/output pins, including 6 PWM output pins.
Voltage and Current: An external power source or a USB connection can be used to power the board. It can withstand a maximum voltage of 20V and is best used in the 7–12V voltage range. 50mA and 200mA, respectively, are the maximum current draws from the 3.3V and 5V pins.
Programming: Arduino UNO R3 may be programmed using the Arduino IDE. The computer language is built on the C/C++ standard. Either an external programmer or a USB-to-serial connection can be used to program the UNO R3.


Based on the ESP8266 WiFi module, the NodeMCU is an open-source IoT (Internet of Things) development platform. It is a great option for applications that need internet access since it combines the features of a microcontroller with integrated WiFi connectivity. The NodeMCU's salient characteristics and details are shown below:
The ESP8266 WiFi module, which includes a microcontroller (usually based on the Tensilica Xtensa architecture) and a WiFi transceiver, is the cornerstone of the NodeMCU. Both computing power and wireless connection are provided by this module.
Programming: Those acquainted with the Arduino environment may quickly get started by utilizing the NodeMCU, which can be programmed using the Arduino IDE. Other tools and programming languages, such as Lua and MicroPython, can also be used to create it.
Wi-Fi: ESP8266 module includes built-in WiFi capabilities, enabling projects to connect to the internet and communicate with other hardware or online services.
GPIO Pins: The NodeMCU board has many General-Purpose Input/Output (GPIO) pins that may be utilized for a variety of tasks, including digital input/output, analog input, and PWM (Pulse Width Modulation) output.
Power: An easy way to upload your code to the NodeMCU board and connect with it through USB is to use the USB-to-serial converter, which is often included with the board.


The concentration of dissolved solids in a liquid is measured using an electrical device called a TDS sensor, sometimes referred to as a total dissolved solids sensor. It is often utilized in a variety of sectors and applications, including industrial operations, hydroponics, aquarium care, and checking the purity of water. Total Dissolved Solids (TDS) is the term used to describe the total amount of all inorganic and organic compounds that are suspended as molecular, ionized, or microgranular particles in a liquid. This comprises metals, cations, anions, salts, minerals, and occasionally even trace quantities of biological material.
"""

answer = nlp_QA(question = "What is TDS sensor?", context = context)

print(answer)