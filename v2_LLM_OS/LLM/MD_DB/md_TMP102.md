**[TMP102](https://www.ti.com/product/TMP102)**

[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397)
## **TMP102 Low-Power Digital Temperature Sensor With SMBus and Two-Wire Serial ** **Interface in SOT563**

##### **1 Features**

- SOT563 package (1.6mm × 1.6mm) is a 68%
smaller footprint than SOT-23

- Accuracy without calibration:

–
2.0°C (maximum) from –25°C to 85°C

–
3.0°C (maximum) from –40°C to 125°C

- Low quiescent current:

–
7.5μA active (maximum)

–
0.35μA shutdown (maximum)

- Supply range: 1.4V to 3.6V

- Resolution: 12 bits

- Digital output: SMBus, two-wire, and I [2] C interface
compatibility

- NIST traceable **2 Applications**

- [Portable electronics](https://www.ti.com/applications/personal-electronics/portable-electronics/overview.html/overview.html)

- Power-supply temperature monitoring

- [Connected peripherals and printers](https://www.ti.com/applications/personal-electronics/connected-peripherals-printers/overview.html)

- [PC and notebooks](https://www.ti.com/applications/personal-electronics/pc-notebooks/overview.html)

- Battery management

- [Enterprise machine](https://www.ti.com/applications/enterprise-systems/enterprise-machine/overview.html)

- [Thermostat](https://www.ti.com/solution/thermostat)

- Electromechanical device temperatures

- General temperature measurements:

–
[Factory automation & control](https://www.ti.com/applications/industrial/factory-automation/overview.html)
– [Test & measurement](https://www.ti.com/applications/industrial/test-measurement/overview.html)

– [Medical and healthcare](https://www.ti.com/applications/industrial/medical-healthcare/overview.html)

Supply Voltage

1.4V to 3.6V

Supply Bypass
Capacitor

Pullup Resistors 0.01µF

5kΩ

TMP102

##### **3 Description**

The TMP102 device is a digital temperature sensor
designed for NTC/PTC thermistor replacement where
high accuracy is required. The device offers an
accuracy of ±0.5°C without requiring calibration
or external component signal conditioning. Device
temperature sensors are highly linear and do not
require complex calculations or lookup tables to
derive the temperature. The on-chip 12-bit ADC offers
resolutions down to 0.0625°C.

The 1.6mm × 1.6mm SOT563 package is 68%
smaller footprint than an SOT-23 package. The
TMP102 device features SMBus [™], two-wire and I [2] C
interface compatibility, and allows up to four devices
on one bus. The device also features an SMBus
alert function. The device is specified to operate over
supply voltages from 1.4V to 3.6V with the maximum
quiescent current of 7.5µA over the full operating

range.

The TMP102 device is designed for extended
temperature measurement in a variety of
communication, computer, consumer, environmental,
industrial, and instrumentation applications. The
device is specified for operation over a temperature
range of –40°C to 125°C.

The TMP102 production units are 100% tested
against sensors that are NIST-traceable and are
verified with equipment that are NIST-traceable
through ISO/IEC 17025 accredited calibrations.

**Packa** **g** **e Information**

(1) For more information, see Section 10.
(2) The package size (length × width) is a nominal value and
includes pins, where applicable.

Temperature

|PART NUMBER|PACKAGE(1)|PACKAGE SIZE(2)|
|---|---|---|
|TMP102|SOT563 (6)|1.60mm × 1.60mm|


Two-Wire

Host Controller


SCL

GND


6

5

4


SDA

V+


ALERT


ADD0

|Col1|Col2|Col3|
|---|---|---|
||||
|||2 3|


SCL


SDA


**Simplified Schematic**



**Block Diagram**


ADD0

|1 2 3|Diode Control Temp. Logic Sensor DS Serial A/D Interface Converter Config. OSC and Temp. Register|6 5 4|
|---|---|---|


An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


-----

**[TMP102](https://www.ti.com/product/TMP102)**
[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397) **[www.ti.com](https://www.ti.com)**
##### **Table of Contents**


**1 Features** ............................................................................1

**2 Applications** ..................................................................... 1
**3 Description** .......................................................................1
**4 Pin Configuration and Functions** ...................................3
**5 Specifications** .................................................................. 4

5.1 Absolute Maximum Ratings........................................ 4
5.2 ESD Ratings............................................................... 4
5.3 Recommended Operating Conditions.........................4
5.4 Thermal Information....................................................4

5.5 Electrical Characteristics.............................................5

5.6 Timing Requirements.................................................. 6
5.7 Typical Characteristics................................................ 7
**6 Detailed Description** ........................................................8

6.1 Overview..................................................................... 8

6.2 Functional Block Diagram........................................... 8
6.3 Feature Description.....................................................8
6.4 Device Functional Modes..........................................14


6.5 Programming............................................................ 16
**7 Application and Implementation** .................................. 20

7.1 Application Information............................................. 20
7.2 Typical Application.................................................... 20
7.3 Power Supply Recommendations.............................21
7.4 Layout....................................................................... 22
**8 Device and Documentation Support** ............................23

8.1 Documentation Support............................................ 23
8.2 Receiving Notification of Documentation Updates....23
8.3 Support Resources................................................... 23
8.4 Trademarks............................................................... 23
8.5 Electrostatic Discharge Caution................................23
8.6 Glossary....................................................................23
**9 Revision History** ............................................................ 23
**10 Mechanical, Packaging, and Orderable**

**Information** .................................................................... 25


2 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* Copyright © 2024 Texas Instruments Incorporated

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[www.ti.com](https://www.ti.com)**
##### **4 Pin Configuration and Functions**

SCL

GND

ALERT


SDA

V+

ADD0


**[TMP102](https://www.ti.com/product/TMP102)**

[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397)

|Col1|CBZ|Col3|
|---|---|---|
|1||6|
|2||5|
|3||4|
||||


**Figure 4-1. DRL Package 6-Pin SOT563 Top View**

(1) I = Input, O = Output, I/O = Input or Output

|Col1|Col2|Col3|Table 4-1. Pin Functions|
|---|---|---|---|
|PIN||TYPE(1)|DESCRIPTION|
|NO.|NAME|||
|1|SCL|I|Serial clock|
|2|GND|—|Ground|
|3|ALERT|O|Overtemperature alert. Open-drain output; requires a pullup resistor.|
|4|ADD0|I|Address select. Connect to GND or V+|
|5|V+|I|Supply voltage, 1.4 V to 3.6 V|
|6|SDA|I/O|Serial data. Open-drain output; requires a pullup resistor.|



Copyright © 2024 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* 3

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[TMP102](https://www.ti.com/product/TMP102)**
[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397) **[www.ti.com](https://www.ti.com)**
##### **5 Specifications**
###### **5.1 Absolute Maximum Ratings**

Over o p eratin g free-air tem p erature ran g e ( unless otherwise noted ) [(1)]

(1) Operation outside the *Absolute Maximum Ratings* may cause permanent device damage. *Absolute Maximum Ratings* do not imply
functional operation of the device at these or any other conditions beyond those listed under *Recommended Operating Conditions* .
If used outside the *Recommended Operating Conditions* but within the *Absolute Maximum Ratings*, the device may not be fully
functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.
(2) Input voltage rating applies to all TMP102 input voltages. **5.2 ESD Ratings**

(1) Level listed above is the passing level per ANSI, ESDA, and JEDEC JS-001. JEDEC document JEP155 states that 500-V HBM allows
safe manufacturing with a standard ESD control process.
(2) Level listed above is the passing level per EIA-JEDEC JESD22-C101. JEDEC document JEP157 states that 250-V CDM allows safe
manufacturing with a standard ESD control process **5.3 Recommended Operating Conditions**

Over o p eratin g free-air tem p erature ran g e ( unless otherwise noted )

(1) For more information about traditional and new thermal metrics, see the *[Semiconductor and IC Package Thermal Metrics application](https://www.ti.com/lit/an/spra953c/spra953c.pdf?ts=1707774760058&ref_url=https%253A%252F%252Fwww.google.com%252F)*
*note* .

|Col1|MIN MAX|UNIT|
|---|---|---|
|Supply voltage|4|V|
|Voltage at SCL, SDA and ADD0(2)|–0.5 4|V|
|Voltage at ALERT|((V+) + 0.3) and ≤ 4|V|
|Operating temperature|–55 150|°C|
|Junction temperature|150|°C|
|Storage temperature, T stg|–60 150|°C|


|Col1|Col2|Col3|VALUE|UNIT|
|---|---|---|---|---|
|V (ESD)|Electrostatic discharge|Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1)|±2000|V|
|||Charged-device model (CDM), per JEDEC specification JESD22- C101(2)|±1000||


|Col1|Col2|MIN NOM MAX|UNIT|
|---|---|---|---|
|V+|Supply voltage|1.4 3.3 3.6|V|
|T A|Operating free-air temperature|–40 125|°C|


|5.4 Thermal Information|Col2|Col3|Col4|
|---|---|---|---|
|THERMAL METRIC(1)||TMP102|UNIT|
|||DRL (SOT563)||
|||6 PINS||
|R θJA|Junction-to-ambient thermal resistance|240.2|°C/W|
|R θJC(top)|Junction-to-case (top) thermal resistance|96.4|°C/W|
|R θJB|Junction-to-board thermal resistance|124.3|°C/W|
|ψ JT|Junction-to-top characterization parameter|4.0|°C/W|
|ψ JB|Junction-to-board characterization parameter|123.1|°C/W|



4 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* Copyright © 2024 Texas Instruments Incorporated

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[www.ti.com](https://www.ti.com)**
###### **5.5 Electrical Characteristics**

At T A = 25°C and V+ = 1.4 to 3.6 V, unless otherwise noted.


**[TMP102](https://www.ti.com/product/TMP102)**

[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397)

|PARAMETER|Col2|Col3|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|---|
|TEMPERATURE SENSOR||||||
||Range|||–40 125|°C|
||Accuracy (temperature error)||-25°C to 85°C|± 0.5 ± 2|°C|
||||-40°C to 125°C|± 1 ± 3||
||vs supply|||0.2 0.5|°C/V|
||Resolution|||0.0625|°C|
|DIGITAL INPUT/OUTPUT||||||
||Input capacitance|||3|pF|
|V IH|Input logic high|||0.7 × (V+) 3.6|V|
|V IL|Input logic low|||–0.5 0.3 × (V+)|V|
|I IN|Input current||0 < V < 3.6V IN|1|µA|
|V OL|Output logic|SDA|V+ > 2 V, I = 3 mA OL|0 0.4|V|
||||V+ < 2 V, I = 3 mA OL|0 0.2 × (V+)||
|||ALERT|V+ > 2 V, I = 3 mA OL|0 0.4||
||||V+ < 2 V, I = 3 mA OL|0 0.2 × (V+)||
||Resolution|||12|Bit|
||Conversion time|||10 15|ms|
||Conversion modes||CR1 = 0, CR0 = 0|0.25|Conv/s|
||||CR1 = 0, CR0 = 1|1||
||||CR1 = 1, CR0 = 0 (default)|4||
||||CR1 = 1, CR0 = 1|8||
||Timeout time|||30 40|ms|
|POWER SUPPLY||||||
||Operating supply range|||1.4 3.6|V|
|I Q|Average quiescent current||Serial bus inactive, CR1 = 0, CR0 = 1|3.2 5|µA|
||||Serial bus inactive, CR1 = 1, CR0 = 0 (default)|4.8 7.5||
||||Serial bus active, SCL frequency = 400 kHz|10||
||||Serial bus active, SCL frequency = 2.85 MHz|40||
|I SD|Shutdown current||Serial bus inactive|0.15 0.35|µA|
||||Serial bus active, SCL frequency = 400 kHz|5.5||
||||Serial bus active, SCL frequency = 2.85 MHz|35||
|TEMPERATURE||||||
||Specified range|||–40 125|°C|
||Operating range|||–55 150|°C|


Copyright © 2024 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* 5

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[TMP102](https://www.ti.com/product/TMP102)**
[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397) **[www.ti.com](https://www.ti.com)**
###### **5.6 Timing Requirements**

See the *Timin* *g* *Dia* *g* *rams* section for additional information.

|Col1|Col2|Col3|FAST MODE|HIGH-SPEED MODE|UNIT|
|---|---|---|---|---|---|
||||MIN MAX|MIN MAX||
|f(SCL)|SCL operating frequency|V+|0.001 0.4|0.001 2.85|MHz|
|t(BUF)|Bus-free time between STOP and START condition|See Figure 6-1|600|160|ns|
|t(HDSTA)|Hold time after repeated START condition. After this period, the first clock is generated.||600|160|ns|
|t(SUSTA)|Repeated START condition setup time||600|160|ns|
|t(SUSTO)|STOP condition setup time||600|160|ns|
|t(HDDAT)|Data hold time||100 900|25 105|ns|
|t(SUDAT)|Data setup time||100|25|ns|
|t(LOW)|SCL clock low period|V+, See Figure 6-1|1300|210|ns|
|t(HIGH)|SCL clock high period|See Figure 6-1|600|60|ns|
|tFD|Data fall time|See Figure 6-1|300|80|ns|
|tRD|Data rise time|See Figure 6-1|300||ns|
|||SCLK ≤ 100 kHz, See Figure 6-1|1000||ns|
|tFC|Clock fall time|See Figure 6-1|300|40|ns|
|tRC|Clock rise time|See Figure 6-1|300|40|ns|



6 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* Copyright © 2024 Texas Instruments Incorporated

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[www.ti.com](https://www.ti.com)**
###### **5.7 Typical Characteristics**

At T A = 25°C and V+ = 3.3 V, unless otherwise noted.


**[TMP102](https://www.ti.com/product/TMP102)**

[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397)

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
||1.4V|Sup|ply|||||||
||3.6V|Sup|ply|||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||

|Col1|1.4V S 3.6V S|upp upp|ly ly|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||

|Col1|1.4V|Supp|ly|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
||3.6V|Supp|ly|||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||

|Col1|Col2|Col3||Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
||-|5|5|C ||||||||
|||+2|5|C||||||||
|||+1|2|5C||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||M M|ean ean + 3 V|
||||||||||||||M|ean  3 V|
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||

|8.5 1.4V Supply 8 3.6V Supply 7.5 7 6.5 (A) 6 IQ 5.5 5 4.5 4 -60 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (C) Four conversions per second Figure 5-1. Average Quiescent Current vs Temperature|3,000 1.4V Supply 3.6V Supply 2,500 2,000 (nA) 1,500 ISD 1,000 500 0 -60 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (C) Figure 5-2. Shutdown Current vs Temperature|
|---|---|
|15 1.4V Supply 14 3.6V Supply 13 (ms) 12 11 Time 10 Conversion 9 8 7 6 5 -60 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (C) Figure 5-3. Conversion Time vs Temperature|50.0 -55C 45.0 +25C +125C 40.0 35.0 30.0 (A) 25.0 IQ 20.0 15.0 10.0 5.0 0.0 1x103 1x104 1x105 1x106 1x107 Bus Frequency (Hz) Figure 5-4. Quiescent Current vs Bus Frequency (Temperature at 3.3-V Supply)|
|1 Mean 0.8 Mean + 3 V 0.6 Mean  3 V (qC) 0.4 Error 0.2 0 Temperature -0.2 -0.4 -0.6 -0.8 -1 -60 -40 -20 0 20 40 60 80 100 120 140 Temperature (qC) D002 Figure 5-5. Temperature Error vs Temperature|70 60 50 Population 40 30 20 10 0 -0.35 -0.3 -0.25 -0.2 -0.15 -0.1 -0.05 0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 D001 Temperature Error (qC) Figure 5-6. Temperature Error at 25°C|


Copyright © 2024 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* 7

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[TMP102](https://www.ti.com/product/TMP102)**
[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397) **[www.ti.com](https://www.ti.com)**
##### **6 Detailed Description**
###### **6.1 Overview**

The TMP102 device is a digital temperature sensor that is designed for thermal-management and thermalprotection applications. The TMP102 device is two-wire, SMBus and I [2] C interface-compatible. The device is
specified over an operating temperature range of –40°C to 125°C. See *Functional Block Diagram* for a block
diagram of the TMP102 device.

The TMP102 device is a temperature sensor. Thermal paths run through the package leads as well as the plastic
package. The package leads provide the primary thermal path because of the lower thermal resistance of the
metal.

An alternative version of the TMP102 device is available. The TMP112 device has highest accuracy, the same
micro-package, and is pin-to-pin compatible.

**Table 6-1. Advanta** **g** **es of TMP112 versus TMP102** **6.2 Functional Block Diagram**

Temperature

|DEVICE|COMPATIBLE INTERFACES|PACKAGE|SUPPLY CURRENT|SUPPLY VOLTAGE (MIN)|SUPPLY VOLTAGE (MAX)|RESOLUTION|LOCAL SENSOR ACCURACY (MAX)|SPECIFIED CALIBRATION DRIFT SLOPE|
|---|---|---|---|---|---|---|---|---|
|TMP112|I2C SMBus|SOT563 1.2 × 1.6 × 0.6|7.5 µA|1.4 V|3.6 V|12 bit 0.0625°C|0.5°C: (0°C to 65°C) 1°C: (-40°C to 125°C)|Yes|
|TMP102|I2C SMBus|SOT563 1.2 × 1.6 × 0.6|7.5 µA|1.4 V|3.6 V|12 bit 0.0625°C|2°C: (25°C to 85°C) 3°C: (-40°C to 125°C)|No|


SCL


SDA




ADD0

|1 2 3|Diode Control Temp. Logic Sensor DS Serial A/D Interface Converter Config. OSC and Temp. Register|6 5 4|
|---|---|---|

###### **6.3 Feature Description**

***6.3.1 Digital Temperature Output***

The digital output from each temperature measurement is stored in the read-only temperature register. The
temperature register of the TMP102 device is configured as a 12-bit, read-only register (configuration register
EM bit = 0, see the *Extended Mode (EM)* section), or as a 13-bit, read-only register (configuration register
EM bit = 1) that stores the output of the most recent conversion. Two bytes must be read to obtain data and
are listed in Table 6-8 and Table 6-9. Byte 1 is the most significant byte (MSB), followed by byte 2, the least
significant byte (LSB). The first 12 bits (13 bits in extended mode) are used to indicate temperature. The least
significant byte does not have to be read if that information is not needed. The data format for temperature
is summarized in Table 6-2 and Table 6-3. One LSB equals 0.0625°C. Negative numbers are represented in
binary twos-complement format. Following power-up or reset, the temperature register reads 0°C until the first
conversion is complete. Bit D0 of byte 2 indicates normal mode (EM bit = 0) or extended mode (EM bit = 1),
and can be used to distinguish between the two temperature register data formats. The unused bits in the
temperature register always read 0.

8 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* Copyright © 2024 Texas Instruments Incorporated

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[www.ti.com](https://www.ti.com)**


**[TMP102](https://www.ti.com/product/TMP102)**

[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397)

**Table 6-2. 12-Bit Tem** **p** **erature Data Format** [(1) ]

|TEMPERATURE (°C)|DIGITAL OUTPUT (BINARY)|HEX|
|---|---|---|
|128|0111 1111 1111|7FF|
|127.9375|0111 1111 1111|7FF|
|100|0110 0100 0000|640|
|80|0101 0000 0000|500|
|75|0100 1011 0000|4B0|
|50|0011 0010 0000|320|
|25|0001 1001 0000|190|
|0.25|0000 0000 0100|004|
|0|0000 0000 0000|000|
|–0.25|1111 1111 1100|FFC|
|–25|1110 0111 0000|E70|
|–55|1100 1001 0000|C90|


(1) The resolution for the Temp ADC in Internal Temperature mode is 0.0625°C/count.

Table 6-2 does not list all temperatures. Use the following rules to obtain the digital data format for a given
temperature or the temperature for a given digital data format.

To convert positive temperatures to a digital data format:
1. Divide the temperature by the resolution
2. Convert the result to binary code with a 12-bit, left-justified format, and MSB = 0 to denote a positive sign.

Example: (50°C) / (0.0625°C / LSB) = 800 = 320h = 0011 0010 0000

To convert a positive digital data format to temperature:
1. Convert the 12-bit, left-justified binary temperature result, with the MSB = 0 to denote a positive sign, to a
decimal number.

2. Multiply the decimal number by the resolution to obtain the positive temperature.

Example: 0011 0010 0000 = 320h = 800 × (0.0625°C / LSB) = 50°C

To convert negative temperatures to a digital data format:
1. Divide the absolute value of the temperature by the resolution, and convert the result to binary code with a
12-bit, left-justified format.
2. Generate the twos complement of the result by complementing the binary number and adding one. Denote a
negative number with MSB = 1.

Example: (|–25°C|) / (0.0625°C / LSB) = 400 = 190h = 0001 1001 0000

Two's complement format: 1110 0110 1111 + 1 = 1110 0111 0000

To convert a negative digital data format to temperature:
1. Generate the twos compliment of the 12-bit, left-justified binary number of the temperature result (with
MSB = 1, denoting negative temperature result) by complementing the binary number and adding one. This
represents the binary number of the absolute value of the temperature.
2. Convert to decimal number and multiply by the resolution to get the absolute temperature, then multiply by
–1 for the negative sign.

Example: 1110 0111 0000 has twos compliment of 0001 1001 0000 = 0001 1000 1111 + 1

Convert to temperature: 0001 1001 0000 = 190h = 400; 400 × (0.0625°C / LSB) = 25°C = (|–25°C|); (|–
25°C|) × (–1) = –25°C

**Table 6-3. 13-Bit Tem** **p** **erature Data Format**

|TEMPERATURE (°C)|DIGITAL OUTPUT (BINARY)|HEX|
|---|---|---|
|150|0 1001 0110 0000|0960|



Copyright © 2024 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* 9

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[TMP102](https://www.ti.com/product/TMP102)**
[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397) **[www.ti.com](https://www.ti.com)**

**Table 6-3. 13-Bit Tem** **p** **erature Data Format** **(** **continued** **)**

***6.3.2 Serial Interface***

|TEMPERATURE (°C)|DIGITAL OUTPUT (BINARY)|HEX|
|---|---|---|
|128|0 1000 0000 0000|0800|
|127.9375|0 0111 1111 1111|07FF|
|100|0 0110 0100 0000|0640|
|80|0 0101 0000 0000|0500|
|75|0 0100 1011 0000|04B0|
|50|0 0011 0010 0000|0320|
|25|0 0001 1001 0000|0190|
|0.25|0 0000 0000 0100|0004|
|0|0 0000 0000 0000|0000|
|–0.25|1 1111 1111 1100|1FFC|
|–25|1 1110 0111 0000|1E70|
|–55|1 1100 1001 0000|1C90|



The TMP102 device operates as a target device only on the two-wire bus and SMBus. Connections to the bus
are made through the open-drain I/O lines, SDA and SCL. The SDA and SCL pins feature integrated spike
suppression filters and Schmitt triggers to minimize the effects of input spikes and bus noise. The TMP102
device supports the transmission protocol for both fast (1 kHz to 400 kHz) and high-speed (1 kHz to 2.85 MHz)
modes. All data bytes are transmitted MSB first.

***6.3.3 Bus Overview***

The device that initiates the transfer is called a *controller*, and the devices controlled by the controller are called
*targets* . The bus must be controlled by a controller device that generates the serial clock (SCL), controls the bus
access, and generates the START and STOP conditions.

To address a specific device, a START condition is initiated, indicated by pulling the data-line (SDA) from a high
to low logic level when SCL is high. All targets on the bus shift in the target address byte on the rising edge of
the clock, with the last bit indicating whether a read or write operation is intended. During the ninth clock pulse,
the target being addressed responds to the controller by generating an acknowledge and by pulling SDA pin low.

A data transfer is then initiated and sent over eight clock pulses followed by an acknowledge bit. During the data
transfer the SDA pin must remain stable when SCL is high, because any change in SDA pin when SCL pin is
high is interpreted as a START signal or STOP signal.

When all data have been transferred, the controller generates a STOP condition indicated by pulling SDA pin
from low to high, when the SCL pin is high.

***6.3.4 Serial Bus Address***

To communicate with the TMP102, the controller must first address target devices via a target address byte. The
target address byte consists of seven address bits, and a direction bit indicating the intent of executing a read or
write operation.

The TMP102 features an address pin to allow up to four devices to be addressed on a single bus. Table 6-4
describes the pin logic levels used to properly connect up to four devices.

10 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* Copyright © 2024 Texas Instruments Incorporated

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[TMP102](https://www.ti.com/product/TMP102)**

**[www.ti.com](https://www.ti.com)** [SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397)

|Table 6-4. Address Pin|and Target Addresses|
|---|---|
|DEVICE TWO-WIRE ADDRESS|A0 PIN CONNECTION|
|1001000|Ground|
|1001001|V+|
|1001010|SDA|
|1001011|SCL|



***6.3.5 Writing and Reading Operation***

Accessing a particular register on the TMP102 device is accomplished by writing the appropriate value to the
pointer register. The value for the pointer register is the first byte transferred after the target address byte with
the R/W bit low. Every write operation to the TMP102 device requires a value for the pointer register (see Figure
6-2).

When reading from the TMP102 device, the last value stored in the pointer register by a write operation
determines which register is read by a read operation. To change the register pointer for a read operation,
a new value must be written to the pointer register. This action is accomplished by issuing a target address
byte with the R/W bit low, followed by the pointer register byte. No additional data are required. The controller
then generates a START condition and sends the target address byte with the R/W bit high to initiate the read
command. See Figure 6-1 for details of this sequence. If repeated reads from the same register are desired,
continually sending the Pointer Register bytes is not necessary because the TMP102 remembers the Pointer
Register value until the device is changed by the next write operation.

Register bytes are sent with the most significant byte first, followed by the least significant byte.

***6.3.6 Target Mode Operations***

The TMP102 can operate as a target receiver or target transmitter. As a target device, the TMP102 never drives
the SCL line.

**6.3.6.1 Target Receiver Mode**

The first byte transmitted by the controller is the target address, with the R/W bit low. The TMP102 then
acknowledges reception of a valid address. The next byte transmitted by the controller is the pointer register.
The TMP102 then acknowledges reception of the pointer register byte. The next byte or bytes are written to
the register addressed by the pointer register. The TMP102 acknowledges reception of each data byte. The
controller can terminate data transfer by generating a START or STOP condition..

**6.3.6.2 Target Transmitter Mode**

The first byte transmitted by the controller is the target address, with the R/ W bit high. The target acknowledges
reception of a valid target address. The next byte is transmitted by the target and is the most significant byte of
the register indicated by the pointer register. The controller acknowledges reception of the data byte. The next
byte transmitted by the target is the least significant byte. The controller acknowledges reception of the data
byte. The controller terminates data transfer by generating a *Not-Acknowledge* on reception of any data byte, or
generating a START or STOP condition.

***6.3.7 SMBus Alert Function***

The TMP102 device supports the SMBus alert function. When the TMP102 device operates in Interrupt Mode
(TM = 1), the ALERT pin can be connected as an SMBus alert signal. When a controller senses that an ALERT
condition is present on the ALERT line, the controller sends an SMBus alert command (0001 1001) to the bus.
If the ALERT pin is active, the device acknowledges the SMBus alert command and responds by returning the
target address on the SDA line. The eighth bit (LSB) of the target address byte indicates if the ALERT condition
was caused by the temperature exceeding T HIGH or falling below T LOW . For POL = 0, the LSB is low if the
temperature is greater than or equal to T HIGH ; this bit is high if the temperature is less than T LOW . The polarity of
this bit is inverted if POL = 1. See Figure 6-4 for details of this sequence.

If multiple devices on the bus respond to the SMBus alert command, arbitration during the target address portion
of the SMBus alert command determines which device clears the ALERT status. The device with the lowest

Copyright © 2024 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* 11

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[TMP102](https://www.ti.com/product/TMP102)**
[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397) **[www.ti.com](https://www.ti.com)**

two-wire address wins the arbitration. If the TMP102 device wins the arbitration, the ALERT pin inactivates at
the completion of the SMBus alert command. If the TMP102 device loses the arbitration, the ALERT pin remains
active.

***6.3.8 General Call***

The TMP102 device responds to a two-wire general call address (000 0000) if the eighth bit is 0. The device
acknowledges the general call address and responds to commands in the second byte. If the second byte is
0000 0110, the TMP102 device internal registers are reset to power-up values. The TMP102 device does not
support the general address acquire command.

***6.3.9 High-Speed (HS) Mode***

For the two-wire bus to operate at frequencies above 400 kHz, the controller device must issue an HS-Mode
controller code (0000 1xxx) as the first byte after a START condition to switch the bus to high-speed operation.
The TMP102 device does not acknowledge this byte, but switches the input filters on SDA and SCL and the
output filters on SDA to operate in HS-mode, allowing transfers of up to 2.85 MHz. After sending the HS-Mode
controller code and NACK bit, user must send a repeated start before sending the target address. The bus
continues to operate in HS-Mode until a STOP condition occurs on the bus. Upon receiving the STOP condition,
the TMP102 device switches the input and output filters back to fast-mode operation.

***6.3.10 Timeout Function***

The TMP102 device resets the serial interface if SCL is held low for 30 ms (typ) between a start and stop
condition. The TMP102 device releases the SDA line if the SCL pin is pulled low and waits for a start condition
from the host controller. To avoid activating the time-out function, maintaining a communication speed of at least
1 kHz for SCL operating frequency is necessary..

***6.3.11 Timing Diagrams***

The TMP102 device is two-wire, SMBus, and I [2] C-interface compatible. Figure 6-1, Figure 6-2, Figure 6-3, and
Figure 6-4 list the various operations on the TMP102 device. Parameters for Figure 6-1 are defined in the *Timing*
*Requirements* table. The bus definitions are defined as follows:

**Acknowledge** Each receiving device, when addressed, is obliged to generate an acknowledge bit. A
device that acknowledges must pull down the SDA line during the acknowledge clock pulse
in such a way that the SDA line is stable low during the high period of the Acknowledge
clock pulse. Setup and hold times must be taken into account. On a controller receive,
the termination of the data transfer can be signaled by the controller generating a *not-*
*acknowledge* (1) on the last byte that has been transmitted by the target.

**Bus Idle** Both SDA and SCL lines remain high.

**Data Transfer** The number of data bytes transferred between a START and a STOP condition is not
limited and is determined by the controller device. The TMP102 device can also be used for
single byte updates. To update only the MS byte, terminate the communication by issuing a
START or STOP communication on the bus.

**Start Data** A change in the state of the SDA line, from high to low, when the SCL line is high, defines a
**Transfer** START condition. Each data transfer is initiated with a START condition.

**Stop Data** A change in the state of the SDA line from low to high when the SCL line is high defines
**Transfer** a STOP condition. Each data transfer is terminated with a repeated START or STOP

condition.

12 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* Copyright © 2024 Texas Instruments Incorporated

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[www.ti.com](https://www.ti.com)**


SCL

SDA

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||tFC tRC t(HDSTA) t(HIGH) t(SUSTA) t(HDDAT) t(SUDAT) tRD|||t(HDSTA) tFD|||
||||)||||||t (|
|||t(BUF||||||||
|||||||||||
||P||S|||||P||



SCL

SDA

SCL

(Continued)


**[TMP102](https://www.ti.com/product/TMP102)**

[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397)

**Figure 6-1. Two-Wire Timing Diagram**


1 9 1


9


…


SDA 1 0 0 1 0 A1 (1) A0 (1) R/W 0 0 0 0 0 0 P1 P0 …

Start By ACK By ACK By
Host Device Device

Frame 1 Two Wire Device Address Byte Frame 2 Pointer Register Byte

1 9 1 9

SCL

(Continued)

SDA
D7 D6 D5 D4 D3 D2 D1 D0 D7 D6 D5 D4 D3 D2 D1 D0
(Continued)

ACK By ACK By Stop By
Device Device Host

NOTE: (1) The value of A0 and A1 are determined by the ADD0 pin.

**Figure 6-2. Two-Wire Timing Diagram for Write Word Format**

Copyright © 2024 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* 13

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[TMP102](https://www.ti.com/product/TMP102)**
[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397) **[www.ti.com](https://www.ti.com)**

1 9 1 9

SCL …

SDA 1 0 0 1 0 A1 (1) A0 (1) R/W 0 0 0 0 0 0 P1 P0 …

Start By ACK By ACK By Stop By
Host Device Device Host

Frame 1 Two-Wire Device Address Byte Frame 2 Pointer Register Byte

1 9 1 9

(Continued)SCL …

SDA 1 0 0 1 0 A1 (1) A0 (1) R/W D7 D6 D5 D4 D3 D2 D1 D0 …
(Continued)

Start By ACK By From ACK By
Host Device Device Host (2)

~~F~~ rame 3 Two-Wire Device Address Byt ~~e~~ Frame 4 Data Byte 1 Read Register

1 9

SCL

(Continued)

SDA

(Continued)

From ACK By Stop By
Device Host (3) Host

Frame 5 Data Byte 2 Read Register

NOTE: (1) The value of A0 and A1 are determined by the ADD0 pin.
(2) Host should leave SDA high to terminate a single-byte read operation.
(3) Host should leave SDA high to terminate a two-byte read operation.

**Figure 6-3. Two-Wire Timing Diagram for Read Word Format**

ALERT

1 9 1 9

SCL

SDA 0 0 0 1 1 0 0 R/W 1 0 0 1 A1 (1) A0 (1) Status

Start By ACK By From NACK By Stop By
Host Device Device Host Host

Frame 1 SMBus ALERT Response Address Byte ~~F~~ rame 2 Device Address Byt ~~e~~

NOTE: (1) The value of A0 and A1 are determined by the ADD0 pin.

**Figure 6-4. Timing Diagram for SMBus Alert**
###### **6.4 Device Functional Modes**

***6.4.1 Continuous-Conversion Mode***

The default mode of the TMP102 device is continuous conversion mode. During continuous-conversion mode,
the ADC performs continuous temperature conversions and stores each results to the temperature register,
overwriting the result from the previous conversion. The conversion rate bits, CR1 and CR0, configure the
TMP102 device for conversion rates of 0.25 Hz, 1 Hz, 4 Hz, or 8 Hz. The default rate is 4 Hz. The TMP102
device has a typical conversion time of 10 ms. To achieve different conversion rates, the TMP102 device makes
a conversion and then powers down to wait for the appropriate delay set by CR1 and CR0. Table 6-5 lists the
settings for CR1 and CR0.

14 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* Copyright © 2024 Texas Instruments Incorporated

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[www.ti.com](https://www.ti.com)**


**[TMP102](https://www.ti.com/product/TMP102)**

[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397)


**Table 6-5. Conversion Rate Settin** **g** **s**

|CR1|CR0|CONVERSION RATE|
|---|---|---|
|0|0|0.25 Hz|
|0|1|1 Hz|
|1|0|4 Hz (default)|
|1|1|8 Hz|



After power-up or general-call reset, the TMP102 immediately starts a conversion, as shown in Figure 6-5. The
first result is available after 10 ms (typical). The active quiescent current during conversion is 55 μA (typical at
+27°C). The quiescent current during delay is 2.6 μA (typical at +27°C).

10ms

|Col1|Col2|Delay(1)|Col4|
|---|---|---|---|
|||||
|||10ms||



Startup Start of
Conversion

A. Delay is set by CR1 and CR0.

**Figure 6-5. Conversion Start**

***6.4.2 Extended Mode (EM)***

The Extended-Mode bit configures the device for Normal mode operation (EM = 0) or Extended mode operation
(EM = 1). In Normal mode, the Temperature Register and high- and low-limit registers use a 12-bit data format.
[Normal mode is used to make the TMP102 device compatible with the TMP75 device.](http://focus.ti.com/docs/prod/folders/print/tmp75.html)

Extended mode (EM = 1) allows measurement of temperatures above 128°C by configuring the Temperature
Register, and high- and low-limit registers for 13-bit data format.

***6.4.3 Shutdown Mode (SD)***

The Shutdown-mode bit saves maximum power by shutting down all device circuitry other than the serial
interface, reducing current consumption to typically less than 0.15 μA. Shutdown mode enables when the SD bit
is 1; the device shuts down when current conversion is completed. When SD is equal to 0, the device maintains
a continuous conversion state.

***6.4.4 One-Shot/Conversion Ready (OS)***

The TMP102 device features a one-shot temperature measurement mode. When the device is in Shutdown
Mode, writing a 1 to the OS bit starts a single temperature conversion. During the conversion, the OS bit reads
'0'. The device returns to the shutdown state at the completion of the single conversion. After the conversion, the
OS bit reads 1. This feature reduces power consumption in the TMP102 device when continuous temperature
monitoring is not required.

As a result of the short conversion time, the TMP102 device achieves a higher conversion rate. A single
conversion typically takes 10 ms and a read can take place in less than 20 μs. When using One-Shot Mode, 80
or more conversions per second are possible.

***6.4.5 Thermostat Mode (TM)***

The thermostat-mode bit indicates to the device whether to operate in comparator mode (TM = 0) or Interrupt
mode (TM = 1).

**6.4.5.1 Comparator Mode (TM = 0)**

In Comparator mode (TM = 0), the Alert pin is activated when the temperature equals or exceeds the value in
the T (HIGH) register and remains active until the temperature falls below the value in the T (LOW) register. For more
information on the comparator mode, see the *High- and Low-Limit Registers* .

Copyright © 2024 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* 15

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[TMP102](https://www.ti.com/product/TMP102)**
[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397) **[www.ti.com](https://www.ti.com)**

**6.4.5.2 Interrupt Mode (TM = 1)**

In Interrupt mode (TM = 1), the Alert pin is activated with the conditions described in *High- and Low-Limit*
*Registers* . The Alert pin is cleared when the host controller reads the temperature register. For more information
on the interrupt mode, see the *High- and Low-Limit Registers* .
###### **6.5 Programming**

***6.5.1 Pointer Register***

Figure 6-6 illustrates the internal register structure of the TMP102 device. The 8-bit Pointer Register of the
device is used to address a given data register. The Pointer Register uses the two least-significant bytes (LSBs)
(see Table 6-15 and Table 6-16) to identify which of the data registers must respond to a read or write command.
Table 6-6 identifies the bits of the Pointer Register byte. During a write command, P2 through P7 must always be
'0'. Table 6-7 describes the pointer address of the registers available in the TMP102 device. The power-up reset
value of P1 and P0 is 00. By default, the TMP102 device reads the temperature on power up.

SCL

SDA

|Col1|Pointer Register|
|---|---|


|Col1|T HIGH Register|
|---|---|
|||


|I/O Control Interface|Col2|
|---|---|
|||
|||



**Figure 6-6. Internal Register Structure**

**Table 6-6. Pointer Re** **g** **ister B** **y** **te**

***6.5.2 Temperature Register***

|P7|P6|P5|P4|P3|P2|P1|P0|
|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|Register Bits||


|Col1|Col2|Table 6-7. Pointer Addresses|
|---|---|---|
|P1|P0|REGISTER|
|0|0|Temperature Register (Read Only)|
|0|1|Configuration Register (Read/Write)|
|1|0|T Register (Read/Write) LOW|
|1|1|T Register (Read/Write) HIGH|



The Temperature Register of the TMP102 is configured as a 12-bit, read-only register (Configuration Register
EM bit = 0, see the *Extended Mode* section), or as a 13-bit, read-only register (Configuration Register EM bit = 1)
that stores the output of the most recent conversion. Two bytes must be read to obtain data, and are described
in Table 6-8 and Table 6-9. Note that byte 1 is the most significant byte, followed by byte 2, the least significant
byte. The first 12 bits (13 bits in Extended mode) are used to indicate temperature. The least significant byte
does not have to be read if that information is not needed.

16 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* Copyright © 2024 Texas Instruments Incorporated

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[www.ti.com](https://www.ti.com)**


**[TMP102](https://www.ti.com/product/TMP102)**

[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397)

**Table 6-8. B** **y** **te 1 of Tem** **p** **erature Re** **g** **ister** [(1) ]

|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|
|T11 (T12)|T10 (T11)|T9 (T10)|T8 (T9)|T7 (T8)|T6 (T7)|T5 (T6)|T4 (T5)|


(1) Extended mode 13-bit configuration shown in parenthesis.

**Table 6-9. B** **y** **te 2 of Tem** **p** **erature Re** **g** **ister** [(1) ]

(1) Extended mode 13-bit configuration shown in parenthesis.

***6.5.3 Configuration Register***

|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|
|T3 (T4)|T2 (T3)|T1 (T2)|T0 (T1)|0 (T0)|0 (0)|0 (0)|0 (1)|



The Configuration Register is a 16-bit read/write register used to store bits that control the operational modes
of the temperature sensor. Read/write operations are performed MSB first. Table 6-10 and Table 6-11 list the
format and the power-up or reset value of the configuration register. For compatibility, Table 6-10 and Table 6-11
correspond to the configuration register in the TMP75 device and TMP275 device (for more information see the
[device data sheets, SBOS288 and SBOS363, respectively). All registers are updated byte by byte.](https://www.ti.com/lit/pdf/SBOS288)

**Table 6-10. B** **y** **te 1 of Confi** **g** **uration and Power-U** **p** **or Reset Format**

**Table 6-11. B** **y** **te 2 of Confi** **g** **uration and Power-U** **p** **or Reset Format**

**6.5.3.1 Shutdown Mode (SD)**

|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|
|OS 0|R1 1|R0 1|F1 0|F0 0|POL 0|TM 0|SD 0|


|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|
|CR1 1|CR0 0|AL 1|EM 0|0 0|0 0|0 0|0 0|



The Shutdown-mode bit saves maximum power by shutting down all device circuitry other than the serial
interface, reducing current consumption to typically less than 0.5 μA. Shutdown mode enables when the SD bit
is 1; the device shuts down when current conversion is completed. When SD is equal to 0, the device maintains
a continuous conversion state

**6.5.3.2 Thermostat Mode (TM)**

The Thermostat mode bit indicates to the device whether to operate in Comparator mode (TM = 0) or Interrupt
mode (TM = 1). For more information on comparator and interrupt modes, see the *High- and Low-Limit Registers*
section.

**6.5.3.3 Polarity (POL)**

The polarity bit allows the user to adjust the polarity of the ALERT pin output. If the POL bit is set to 0 (default),
the ALERT pin becomes active low. When the POL bit is set to 1, the ALERT pin becomes active high and the
state of the ALERT pin is inverted. The operation of the ALERT pin in various modes is illustrated in Figure 6-7.

Copyright © 2024 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* 17

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[TMP102](https://www.ti.com/product/TMP102)**
[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397) **[www.ti.com](https://www.ti.com)**

Measured

Temperature

**Device** ALERT�PIN

(Comparator�Mode)
POL�=�0

**Device** ALERT�PIN

(Interrupt�Mode)
POL�=�0

**Device** ALERT�PIN

(Comparator�Mode)
POL�=�1

**Device** ALERT�PIN

(Interrupt�Mode)
POL�=�1

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||T HIGH||
||||||T LOW||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||


Read Read

Time


Read


**Figure 6-7. Output Transfer Function Diagrams**

**6.5.3.4 Fault Queue (F1/F0)**

A fault condition exists when the measured temperature exceeds the user-defined limits set in the T HIGH and
T LOW registers. Additionally, the number of fault conditions required to generate an alert can be programmed
using the fault queue. The fault queue is provided to prevent a false alert as a result of environmental noise.
The fault queue requires consecutive fault measurements to trigger the alert function. Table 6-12 defines the
number of measured faults that can be programmed to trigger an alert condition in the device. For T HIGH and
T LOW register format and byte order, see the *High- and Low-Limit Registers* section.

**Table 6-12. TMP102 Fault Settin** **g** **s**

|F1|F0|CONSECUTIVE FAULTS|
|---|---|---|
|0|0|1|
|0|1|2|
|1|0|4|
|1|1|6|



**6.5.3.5 Converter Resolution (R1/R0)**

The converter resolution bits, R1 and R0, are read-only bits. The TMP102 converter resolution is set at device
start-up to 11 which sets the temperature register to a 12 bit-resolution.

**6.5.3.6 One-Shot (OS)**

When the device is in Shutdown Mode, writing a 1 to the OS bit starts a single temperature conversion. During
the conversion, the OS bit reads '0'. The device returns to the shutdown state at the completion of the single
conversion. For more information on the one-shot conversion mode, see the *One-Shot/Conversion Ready (OS)*
section.

**6.5.3.7 EM Bit**

The Extended-Mode bit configures the device for Normal Mode operation (EM = 0) or Extended Mode operation
(EM = 1). In normal mode, the temperature register, high-limit register, and low-limit register use a 12-bit data
format. For more information on the extended mode, see the *Extended Mode (EM)* section.

18 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* Copyright © 2024 Texas Instruments Incorporated

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[TMP102](https://www.ti.com/product/TMP102)**

**[www.ti.com](https://www.ti.com)** [SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397)

**6.5.3.8 Alert (AL Bit)**

The AL bit is a read-only function. Reading the AL bit provides information about the comparator mode status.
The state of the POL bit inverts the polarity of data returned from the AL bit. When the POL bit equals 0, the AL
bit reads as 1 until the temperature equals or exceeds T (HIGH) for the programmed number of consecutive faults,
causing the AL bit to read as 0. The AL bit continues to read as 0 until the temperature falls below T (LOW) for the
programmed number of consecutive faults, when the AL bit again reads as 1. The status of the TM bit does not
affect the status of the AL bit.

**6.5.3.9 Conversion Rate (CR)**

The conversion rate bits, CR1 and CR0, configure the TMP102 device for conversion rates of 0.25 Hz, 1 Hz, 4
Hz, or 8 Hz. The default rate is 4 Hz. For more information on the conversion rate bits, see Table 6-5.

***6.5.4 High- and Low-Limit Registers***

The temperature limits are stored in the T (LOW) and T (HIGH) registers in the same format as the temperature
result, and the values are compared to the temperature result on every conversion. The outcome of the
comparison drives the behavior of the ALERT pin, which operates as a comparator output or an interrupt, and is
set by the TM bit in the configuration register.

In Comparator mode (TM = 0), the ALERT pin becomes active when the temperature equals or exceeds the
value in T HIGH and generates a consecutive number of faults according to fault bits F1 and F0. The ALERT pin
remains active until the temperature falls below the indicated T LOW value for the same number of faults.

In Interrupt mode (TM = 1), the ALERT pin becomes active when the temperature equals or exceeds the value
in T (HIGH) for a consecutive number of fault conditions (as shown in Table 6-5). The ALERT pin remains active
until a read operation of any register occurs, or the device successfully responds to the SMBus Alert Response
address. The ALERT pin will also be cleared if the device is placed in Shutdown mode. When the ALERT pin
is cleared, it becomes active again only when temperature falls below T (LOW), and remains active until cleared
by a read operation of any register or a successful response to the SMBus Alert Response address. When
the ALERT pin is cleared, the above cycle repeats, with the ALERT pin becoming active when the temperature
equals or exceeds T (HIGH) . The ALERT pin can also be cleared by resetting the device with the General Call
Reset command. This action also clears the state of the internal registers in the device, returning the device to
Comparator mode (TM = 0).

Both operational modes are represented in Figure 6-7. Table 6-13 through Table 6-16 describe the format for the
T HIGH and T LOW registers. Note that the most significant byte is sent first, followed by the least significant byte.
Power-up reset values for T HIGH and T LOW are: T HIGH = 80°C and T LOW = 75°C. The format of the data for T HIGH
and T LOW is the same as for the Temperature Register.

**Table 6-13. B** **y** **te 1 Tem** **p** **erature Re** **g** **ister** **HIGH** [(1) ]

(1) Extended mode 13-bit configuration shown in parenthesis.

**Table 6-14. B** **y** **te 2 Tem** **p** **erature Re** **g** **ister** **HIGH**

**Table 6-15. B** **y** **te 1 Tem** **p** **erature Re** **g** **ister** **LOW** [(1) ]

(1) Extended mode 13-bit configuration shown in parenthesis.

|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|
|H11 (H12)|H10 (H11)|H9 (H10)|H8 (H9)|H7 (H8)|H6 (H7)|H5 (H6)|H4 (H5)|


|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|
|H3 (H4)|H2 (H3)|H1 (H2)|H0 (H1)|0 (H0)|0 (0)|0 (0)|0 (0)|


|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|
|L11 (L12)|L10 (L11)|L9 (L10)|L8 (L9)|L7 (L8)|L6 (L7)|L5 (L6)|L4 (L5)|



Copyright © 2024 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* 19

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[TMP102](https://www.ti.com/product/TMP102)**
[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397) **[www.ti.com](https://www.ti.com)**

**Table 6-16. B** **y** **te 2 Tem** **p** **erature Re** **g** **ister** **LOW**
##### **7 Application and Implementation**

**Note**

Information in the following applications sections is not part of the TI component specification,
and TI does not warrant its accuracy or completeness. TI’s customers are responsible for
determining suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.
###### **7.1 Application Information**

|D7|D6|D5|D4|D3|D2|D1|D0|
|---|---|---|---|---|---|---|---|
|L3 (L4)|L2 (L3)|L1 (L2)|L0 (L1)|0 (L0)|0 (0)|0 (0)|0 (0)|



The TMP102 device is used to measure the PCB temperature of the board location where the device is
mounted. The programmable address options allow up to four locations on the board to be monitored on a single
serial bus. **7.2 Typical Application**

Supply Voltage

1.4V to 3.6V

Supply Bypass
Capacitor

Pullup Resistors 0.01µF

5kΩ


TMP102


Two-Wire

Host Controller


SCL

GND

ALERT


6

5

4


ADD0


SDA

V+

|Col1|Col2|Col3|
|---|---|---|
|||2 3|


**Figure 7-1. Typical Connections**

***7.2.1 Design Requirements***

The TMP102 device requires pullup resistors on the SCL, SDA, and ALERT pins. The recommended value for
the pullup resistors is 5-kΩ. In some applications the pullup resistor can be lower or higher than 5 kΩ but must
not exceed 3 mA of current on any of those pins. A 0.01-μF bypass capacitor on the supply is recommended
as shown in Figure 7-1. The SCL and SDA lines can be pulled up to a supply that is equal to or higher than V+
through the pullup resistors. To configure one of four different addresses on the bus, connect the ADD0 pin to
either the GND, V+, SDA, or SCL pin.

***7.2.2 Detailed Design Procedure***

Place the TMP102 device in close proximity to the heat source that must be monitored, with a proper layout
for good thermal coupling. This placement verifies that temperature changes are captured within the shortest

20 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* Copyright © 2024 Texas Instruments Incorporated

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[www.ti.com](https://www.ti.com)**


**[TMP102](https://www.ti.com/product/TMP102)**

[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397)


possible time interval. To maintain accuracy in applications that require air or surface temperature measurement,
care must be taken to isolate the package and leads from ambient air temperature. A thermally-conductive
adhesive is helpful in achieving accurate surface temperature measurement.

The TMP102 device is a very low-power device and generates very low noise on the supply bus. Applying an RC
filter to the V+ pin of the TMP102 device can further reduce any noise that the TMP102 device can propagate to
other components. R (F) in Figure 7-2 must be less than 5 kΩ and C (F) must be greater than 10 nF.

Supply Voltage


Device


R ≤ 5 kΩ
(F)


C ≥ 10 nF
(F)

**Figure 7-2. Noise Reduction Techniques**

***7.2.3 Application Curve***

Figure 7-3 shows the step response of the TMP102 device to a submersion in an oil bath of 100°C from room
temperature (27°C). The time-constant, or the time for the output to reach 63% of the input step, is 0.8 s. The
time-constant result depends on the printed circuit board (PCB) that the TMP102 device is mounted. For this
test, the TMP102 device was soldered to a two-layer PCB that measured 0.375 inch × 0.437 inch.

space

100

95

90

85

80

75

70

65

60

55

50

45

40

35

30

25

-1 1 3 5 7 9 11 13 15 17 19

Time (s)

**Figure 7-3. Temperature Step Response**
###### **7.3 Power Supply Recommendations**

The TMP102 device operates with power supply in the range of 1.4 to 3.6 V. The device is optimized for
operation at 3.3-V supply but can measure temperature accurately in the full supply range.

A power-supply bypass capacitor is required for proper operation. Place this capacitor as close as possible to
the supply and ground pins of the device. A typical value for this supply bypass capacitor is 0.01 μF. Applications

Copyright © 2024 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* 21

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[TMP102](https://www.ti.com/product/TMP102)**
[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397) **[www.ti.com](https://www.ti.com)**

with noisy or high-impedance power supplies can require additional decoupling capacitors to reject power-supply
noise.
###### **7.4 Layout**

***7.4.1 Layout Guidelines***

Place the power-supply bypass capacitor as close as possible to the supply and ground pins. The recommended
value of this bypass capacitor is 0.01 μF. Additional decoupling capacitance can be added to compensate for
noisy or high-impedance power supplies. Pull up the open-drain output pins (SDA, SCL and ALERT) through
5-kΩ pullup resistors.

***7.4.2 Layout Example***

Via to Power or

Ground Plane


Via to Internal Layer


Supply Voltage


Supply Bypass
Capacitor


Serial Bus Traces


Pullup Resistors

|Col1|Col2|Col3|SCL SDA GND V+ ALERT ADD0|Col5|
|---|---|---|---|---|
|||||RT A|
||||||
||||ALE||
|||||round Plane fo ermal Couplin o Heat Source|
|||||Heat Source|



**Figure 7-4. TMP102 Layout Example**


22 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* Copyright © 2024 Texas Instruments Incorporated

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[www.ti.com](https://www.ti.com)**
##### **8 Device and Documentation Support**
###### **8.1 Documentation Support**

***8.1.1 Related Documentation***


**[TMP102](https://www.ti.com/product/TMP102)**

[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397)


For related documentation see the following:

 - Texas Instruments, *[TMPx75 Temperature Sensor With I2C and SMBus Interface in Industry Standard LM75](https://www.ti.com/lit/pdf/SBOS288)*
*[Form Factor and Pinout](https://www.ti.com/lit/pdf/SBOS288)*, data sheet

 - Texas Instruments, *[TMP275 ±0.5°C Temperature Sensor With I 2C and SMBus Interface in Industry Standard](https://www.ti.com/lit/pdf/SBOS363)*
*[LM75 Form Factor and Pinout](https://www.ti.com/lit/pdf/SBOS363)*, data sheet

 - [Texas Instruments, Capacitive Touch Operated Automotive LED Dome Light with Haptics Feedback, Design](http://www.ti.com/tool/TIDA-00156)
Guide
###### **8.2 Receiving Notification of Documentation Updates**

To receive notification of documentation updates, navigate to the device product folder on [ti.com. Click on](https://www.ti.com)
*Notifications* to register and receive a weekly digest of any product information that has changed. For change
details, review the revision history included in any revised document. **8.3 Support Resources**

TI E2E [™] [support forums are an engineer's go-to source for fast, verified answers and design help — straight](https://e2e.ti.com)
from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
[not necessarily reflect TI's views; see TI's Terms of Use.](https://www.ti.com/corp/docs/legal/termsofuse.shtml) **8.4 Trademarks**

SMBus [™] is a trademark of Intel, Inc.
TI E2E [™] is a trademark of Texas Instruments.
All trademarks are the property of their respective owners. **8.5 Electrostatic Discharge Caution**

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications. **8.6 Glossary**

[TI Glossary](https://www.ti.com/lit/pdf/SLYZ022) This glossary lists and explains terms, acronyms, and definitions.
##### **9 Revision History**

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

**Changes from Revision H** **(** **December 2018) to Revision I (June 2024)** **Page**

 - Updated the numbering format for tables, figures, and cross-references throughout the document ................ 1

 - Changed all instances of legacy terminology to controller and target where I [2] C is mentioned .........................1

 - Changed the "Conversion time" throughout the document................................................................................ 1

 - Changed the active, shutdown, average, and delay quiescent current throughout the document..................... 1

 - Changed the SCL pin description in *Pin Functions* table................................................................................... 3

 - Removed machine model (MM) from *ESD Ratings* section............................................................................... 4

 - Changed DRL package Thermal Information section.........................................................................................4

 - Changed "Conversion time" in Electrical Characteristics table.......................................................................... 5

 - Added Average quiescent current at 1Hz conversion mode in Electrical Characteristics table......................... 5

 - Changed Average quiescent current at 4Hz conversion mode in Electrical Characteristics table..................... 5

Copyright © 2024 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* 23

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[TMP102](https://www.ti.com/product/TMP102)**
[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397) **[www.ti.com](https://www.ti.com)**

 - Changed Average quiescent current when serial bus active, SCL frequency = 400 kHz in Electrical
Characteristics table........................................................................................................................................... 5

 - Changed Average quiescent current when serial bus active, SCL frequency = 2.85MHz in Electrical
Characteristics table........................................................................................................................................... 5

 - Changed the frequency from 3.4 to 2.85 MHz in the POWER SUPPLY section of the *Electrical Characteristics*
table.................................................................................................................................................................... 5

 - Changed shutdown current for both serial bus inactive and active, SCL frequency = 400 kHz in Electrical
Characteristics table........................................................................................................................................... 5

 - Changed shutdown current when serial bus active, SCL frequency = 2.85 MHz in Electrical Characteristics
table.................................................................................................................................................................... 5

 - Changed Average Quiescent Current vs Temperature, Shutdown Current vs Temperature, Conversion Time
vs Temperature, and Quiescent Current vs Bus Frequency graphs in the *Typical Characteristics* section........7

 - Changed the *Interrupt Mode (TM=1)* section....................................................................................................16

**Changes from Revision G** **(** **September 2018) to Revision H (December 2018)** **Page**

 - Changed *Absolute Maximum Ratings* for voltage at SCL, SDA and ADD0 pin..................................................4

 - Changed *Absolute Maximum Ratings* for voltage at ALERT pin........................................................................ 4

**Chan** **g** **es from Revision F (September 2018) to Revision G (November 2018)** **Page**

 - Changed input voltage maximum value from: 3.6V to: 4V..................................................................................4

 - Changed output voltage maximum value from: 3.6V to: ((V+) + 0.5) and ≤ 4V.................................................. 4

 - Changed Junction-to-ambient thermal resistance from 200 °C/W to 210.3 °C/W.............................................. 4

 - Changed Junction-to-case (top) thermal resistance from 73.7 °C/W to 105.0 °C/W.......................................... 4

 - Changed Junction-to-board thermal resistance from 34.4 °C/W to 87.5 °C/W...................................................4

 - Changed Junction-to-top characterization parameter from 3.1 °C/W to 6.1 °C/W..............................................4

 - Changed Junction-to-board characterization parameter from 34.2 °C/W to 87.0 °C/W..................................... 4

 - Added the *Receiving Notification of Documentation Updates* section..............................................................23

**Chan** **g** **es from Revision E (April 2015) to Revision F (December 2015)** **Page**

 - Added TI Design ................................................................................................................................................1

 - Added NIST Features bullet .............................................................................................................................. 1

 - Added last paragraph of *Description* section .....................................................................................................1

**Chan** **g** **es from Revision D** **(** **September 2014) to Revision E (December 2014)** **Page**

 - Changed the Temperature Error vs Temperature graph in the *Typical Characteristics* section..........................7

 - Changed the Temperature Error at 25°C graph in the *Typical Characteristics* section...................................... 7

**Chan** **g** **es from Revision C** **(** **October 2012) to Revision D (September 2014)** **Page**

 - Added *Handling Rating* table, *Feature Description* section, *Device Functional Modes*, *Application and*
*Implementation* section, *Power Supply Recommendations* section, *Layout* section, *Device and*
*Documentation Support* section, and *Mechanical, Packaging, and Orderable Information* section................... 4

 - Changed parameters in *Timing Requirements.* .................................................................................................6

24 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* Copyright © 2024 Texas Instruments Incorporated

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

**[www.ti.com](https://www.ti.com)**


**[TMP102](https://www.ti.com/product/TMP102)**

[SBOS397I – AUGUST 2007 – REVISED JUNE 2024](https://www.ti.com/lit/pdf/SBOS397)


**Changes from Revision B** **(** **October 2008** **)** **to Revision C (October 2012)** **Page**

 - Changed DRL package Thermal Information section.........................................................................................4

 - Changed "Conversion time" in Electrical Characteristics table.......................................................................... 5

 - Changed values for *Data Hold Time parameter* in *Timing Requirements* ....................................................... 12
##### **10 Mechanical, Packaging, and Orderable Information**

The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

Copyright © 2024 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOS397I&partnum=TMP102)* 25

Product Folder Links: *[TMP102](https://www.ti.com/product/tmp102?qgpn=tmp102)*


-----

### **PACKAGE OPTION ADDENDUM**

www.ti.com 30-Jul-2024
###### **PACKAGING INFORMATION**


**Orderable Device** **Status**


**Package Type Package**


**Op Temp (°C)** **Device Marking**

(4/5)



**Eco Plan**

(2)


**MSL Peak Temp**

(3)


TMP102AIDRLR ACTIVE SOT-5X3 DRL 6 4000 RoHS & Green NIPDAU | NIPDAUAG Level-1-260C-UNLIM -40 to 125 CBZ

TMP102AIDRLT OBSOLETE SOT-5X3 DRL 6 TBD Call TI Call TI -40 to 125 CBZ

**(1)** The marketing status values are defined as follows:
**ACTIVE:** Product device recommended for new designs.
**LIFEBUY:** TI has announced that the device will be discontinued, and a lifetime-buy period is in effect.
**NRND:** Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using this part in a new design.
**PREVIEW:** Device has been announced but is not in production. Samples may or may not be available.
**OBSOLETE:** TI has discontinued the production of the device.

**(2)** **RoHS:** TI defines "RoHS" to mean semiconductor products that are compliant with the current EU RoHS requirements for all 10 RoHS substances, including the requirement that RoHS substance
do not exceed 0.1% by weight in homogeneous materials. Where designed to be soldered at high temperatures, "RoHS" products are suitable for use in specified lead-free processes. TI may
reference these types of products as "Pb-Free".
**RoHS Exempt:** TI defines "RoHS Exempt" to mean products that contain lead but are compliant with EU RoHS pursuant to a specific EU RoHS exemption.
**Green:** TI defines "Green" to mean the content of Chlorine (Cl) and Bromine (Br) based flame retardants meet JS709B low halogen requirements of <=1000ppm threshold. Antimony trioxide based
flame retardants must also meet the <=1000ppm threshold requirement.

**(3)** MSL, Peak Temp. - The Moisture Sensitivity Level rating according to the JEDEC industry standard classifications, and peak solder temperature.

**(4)** There may be additional marking, which relates to the logo, the lot trace code information, or the environmental category on the device.

**(5)** Multiple Device Markings will be inside parentheses. Only one Device Marking contained in parentheses and separated by a "~" will appear on a device. If a line is indented then it is a continuation
of the previous line and the two combined represent the entire Device Marking for that device.

**(6)** Lead finish/Ball material - Orderable Devices may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two
lines if the finish value exceeds the maximum column width.

**Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information
provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and
continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals.
TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

Addendum-Page 1


-----

### **PACKAGE OPTION ADDENDUM**

www.ti.com 30-Jul-2024

**[OTHER QUALIFIED VERSIONS OF TMP102 :]**
##### • [Automotive : ][TMP102-Q1]

[NOTE: Qualified Version Definitions:] • [Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects]

Addendum-Page 2


-----

### **PACKAGE MATERIALS INFORMATION**

www.ti.com 7-Nov-2024
###### **TAPE AND REEL INFORMATION**


**REEL DIMENSIONS**

*All dimensions are nominal


**TAPE DIMENSIONS**

Reel Width (W1)

|K0|Col2|P1|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|||||||W B0|
||||||||
||||||||
|vity|||A0||||


|A0|Dimension designed to accommodate the component width A0 Cavity|
|---|---|
|A0|Dimension designed to accommodate the component width|
|B0|Dimension designed to accommodate the component length|
|K0|Dimension designed to accommodate the component thickness|
|W|Overall width of the carrier tape|
|P1|Pitch between successive cavity centers|



**QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE**

Sprocket Holes

|Q1|Q2|
|---|---|
|Q3|Q4|


|Q1|Q2|
|---|---|
|Q3|Q4|



Pocket Quadrants

Pack Materials-Page 1

|Device|Package Type|Package Drawing|Pins|SPQ|Reel Diameter (mm)|Reel Width W1 (mm)|A0 (mm)|B0 (mm)|K0 (mm)|P1 (mm)|W (mm)|Pin1 Quadrant|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TMP102AIDRLR|SOT-5X3|DRL|6|4000|180.0|8.4|2.0|1.8|0.75|4.0|8.0|Q3|
|TMP102AIDRLR|SOT-5X3|DRL|6|4000|180.0|8.4|1.98|1.78|0.69|4.0|8.0|Q3|


-----

### **PACKAGE MATERIALS INFORMATION**

www.ti.com 7-Nov-2024

*All dimensions are nominal

Pack Materials-Page 2

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|TMP102AIDRLR|SOT-5X3|DRL|6|4000|210.0|185.0|35.0|
|TMP102AIDRLR|SOT-5X3|DRL|6|4000|202.0|201.0|28.0|


-----

## **PACKAGE OUTLINE**
# DRL0006A SCALE 8.000 SOT - 0.6 mm max hei g ht

PLASTIC SMALL OUTLINE

NOTES:

|0.0|5 C|
|---|---|


|C|A|B|
|---|---|---|


1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
exceed 0.15 mm per side.
4. Reference JEDEC re g istration MO-293 Variation UAAD

www.ti.com


-----

## **EXAMPLE BOARD LAYOUT**
# **DRL0006A SOT - 0.6 mm max hei g ht**

PLASTIC SMALL OUTLINE

NOTES: (continued)

5. Publication IPC-7351 may have alternate designs.
6. Solder mask tolerances between and around signal pads can vary based on board fabrication site.
7. Land pattern design aligns to IPC-610, Bottom Termination Component (BTC) solder joint inspection criteria.

www.ti.com


-----

## **EXAMPLE STENCIL DESIGN**
# **DRL0006A SOT - 0.6 mm max hei g ht**

PLASTIC SMALL OUTLINE

NOTES: (continued)

8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
9. Board assembly site may have different recommendations for stencil design.

www.ti.com


-----

##### **IMPORTANT NOTICE AND DISCLAIMER**

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE
DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES “AS IS”
AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY
IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD
PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate
TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable
standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an
application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license
is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you
will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these

resources.

[TI’s products are provided subject to TI’s Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with](https://www.ti.com/legal/terms-conditions/terms-of-sale.html)
such TI products. TI’s provision of these resources does not expand or otherwise alter TI’s applicable warranties or warranty disclaimers for
TI products.

TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265

Copyright © 2025, Texas Instruments Incorporated


-----

