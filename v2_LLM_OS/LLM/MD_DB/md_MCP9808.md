# **M C P 9808**
### **±0.5°C Maximum Accuracy Digital Temperature Sensor**

##### **Features**

- Accuracy:

 - ±0.25 (typical) from -40°C to +125°C

 - ±0.5°C (maximum) from -20°C to 100°C

 - ±1°C (maximum) from -40°C to +125°C

- User-Selectable Measurement Resolution:

 - +0.5°C, +0.25°C, +0.125°C, +0.0625°C

- User-Programmable Temperature Limits:

 - Temperature Window Limit

 - Critical Temperature Limit

- User-Programmable Temperature Alert Output

- Operating Voltage Range: 2.7V to 5.5V

- Operating Current: 200 µA (typical)

- Shutdown Current: 0.1 µA (typical)

- 2-wire Interface: I [2] C™/SMBus Compatible

- Available Packages: 2x3 DFN-8, MSOP-8 **Typical Applications**

- General Purpose

- Industrial Applications

- Industrial Freezers and Refrigerators

- Food Processing

- Personal Computers and Servers

- PC Peripherals

- Consumer Electronics

- Handheld/Portable Devices **Tem p erature Accurac y**

##### **Description**

Microchip Technology Inc.’s MCP9808 digital
temperature sensor converts temperatures between
-20°C and +100°C to a digital word with
±0.25°C/±0.5°C (typical/maximum) accuracy.

The MCP9808 comes with user-programmable registers
that provide flexibility for temperature sensing
applications. The registers allow user-selectable
settings such as Shutdown or Low-Power modes and
the specification of temperature Alert window limits and
critical output limits. When the temperature changes
beyond the specified boundary limits, the MCP9808
outputs an Alert signal. The user has the option of setting
the Alert output signal polarity as an active-low or activehigh comparator output for thermostat operation, or as a
temperature Alert interrupt output for microprocessorbased systems. The Alert output can also be configured
as a critical temperature output only.

This sensor has an industry standard 400 kHz, 2-wire,
SMBus/I [2] C compatible serial interface, allowing up to
eight or sixteen sensors to be controlled with a single
serial bus (see Table 3-2 for available Address codes).
These features make the MCP9808 ideal for

sophisticated, multi-zone, temperature-monitoring
applications. **Packa g e T yp es**


**8-Pin 2x3 DFN***

SDA 1 8 V DD

SCL 2 EP 7 A0

9

Alert 3 6 A1

GND 4 5 A2


**8-Pin MSOP**


V DD

A0

A1

A2


**40%**

**30%**

|1|Col2|8|
|---|---|---|
|4||5|



- Includes Exposed Thermal Pad (EP); see Table 3-1.


**20%**

**10%**


**0%**


**Temperature Accuracy (°C)**


© 2011 Microchip Technology Inc. DS25095A-page 1


-----

## **MCP9808**
##### **Functional Block Dia g ram**

Register
Pointer


Hysteresis

Shutdown

Critical Trip Lock

Alarm Window Lock

Clear Alert

Alert Status

Output Control

Critical Alert only

Alert Polarity

Alert Comp./Int.

Configuration

Tem p erature

T UPPER Limit

T LOWER Limit

T CRITICAL Limit

Manufacturer ID

Device ID/Rev

Resolution

SMBus/Standard I [2] C™
Interface


Band Gap
Temperature
Sensor

ΔΣ ADC

+0.5°C
+0.25°C
+0.125°C
+0.0625°C


A0 A1 A2 Alert SDA SCL V DD GND

DS25095A-page 2 © 2011 Microchip Technology Inc.


-----

#### **1.0 ELECTRICAL ** **CHARACTERISTICS**
##### **Absolute Maximum Ratings †**

V DD .................................................................................. 6.0V

Voltage at All Input/Output Pins .............. GND – 0.3V to 6.0V

Storage Temperature ....................................-65°C to +150°C

Ambient Temperature with Power Applied ....-40°C to +125°C

Junction Temperature (T J ) ..........................................+150°C

ESD Protection on All Pins (HBM:MM) ................ (4 kV:400V)

Latch-up Current at Each Pin (+25°C) ..................... ±200 mA

## **MCP9808**

**†Notice:** Stresses above those listed under “Maximum
ratings” may cause permanent damage to the device.
This is a stress rating only and functional operation of
the device at those or any other conditions above those
indicated in the operational listings of this specification
is not implied. Exposure to maximum rating conditions
for extended periods may affect device reliability.

|TEMPERATURE SENSOR DC CHARACTERISTICS|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Electrical Specifications: Unless otherwise indicated, V = 2.7V to 5.5V, GND = Ground and DD T = -40°C to +125°C. A|||||||
|Parameters|Sym|Min|Typ|Max|Unit|Conditions|
|Temperature Sensor Accuracy|||||||
|-20°C < T ≤ +100°C A|T ACY T ACY|-0.5|±0.25|+0.5|°C|V = 3.3V DD|
|-40°C < T ≤ +125°C A||-1.0|±0.25|+1.0|°C|V = 3.3V DD|
|Temperature Conversion Time|||||||
|0.5°C/bit|t CONV|—|30|—|ms|33s/sec (typical)|
|0.25°C/bit||—|65|—|ms|15s/sec (typical)|
|0.125°C/bit||—|130|—|ms|7s/sec (typical)|
|0.0625°C/bit||—|250|—|ms|4s/sec (typical)|
|Power Supply|||||||
|Operating Voltage Range|V DD|2.7|—|5.5|V||
|Operating Current|I DD|—|200|400|µA||
|Shutdown Current|I SHDN|—|0.1|2|µA||
|Power-on Reset (POR)|V POR|—|2.2|—|V|Threshold for falling V DD|
|Power Supply Rejection|Δ°C/ΔV DD|—|-0.1|—|°C/V|V = 2.7V to 5.5V, T = +25°C DD A|
|Alert Output (open-drain output, external pull-up resistor required), see Section 5.2.3 “Alert Output Configuration”|||||||
|High-Level Current (leakage)|I OH|—|—|1|µA|V = V (Active-Low, Pull-up Resistor) OH DD|
|Low-Level Voltage|V OL|—|—|0.4|V|I = 3 mA (Active-Low, Pull-up Resistor) OL|
|Thermal Response, from +25°C (air) to +125°C (oil bath)|||||||
|8L-DFN|t RES|—|0.7|—|s|Time to 63% (+89°C)|
|8L-MSOP||—|1.4|—|s||


© 2011 Microchip Technology Inc. DS25095A-page 3


-----

## **MCP9808**
#### **GRAPHICAL SYMBOL DESCRIPTION**

|DIGITAL INPUT/OUTPUT PIN CHARACTERISTICS|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Electrical Specifications: Unless otherwise indicated, V = 2.7V to 5.5V, GND = Ground and DD T = -40°C to +125°C. A|||||||
|Parameters|Sym|Min|Typ|Max|Units|Conditions|
|Serial Input/Output (SCL, SDA, A0, A1, A2)|||||||
|Input|||||||
|High-Level Voltage|V IH|0.7 V DD|—|V DD|V||
|Low-Level Voltage|V IL|GND|—|0.3 V DD|V||
|Input Current|I IN|—|—|±5|µA||
|Output (SDA)|||||||
|Low-Level Voltage|V OL|—|—|0.4|V|I = 3 mA OL|
|High-Level Current (leakage)|I OH|—|—|1|µA|V = 5.5V OH|
|Low-Level Current|I OL|6|—|—|mA|V = 0.6V OL|
|SDA and SCL Inputs|||||||
|Hysteresis|V HYST|—|0.05 V DD|—|V||
|Spike Suppression|t SP|—|—|50|ns||
|Capacitance|C IN|—|5|—|pF||


**Voltage**

**Current**


V DD V IH

I IN

**time**


**OUTPUT**
**INPUT** **Voltage** V DD

V IL V OL

I OL

**Current**

I OH

**time**

|TEMPERATURE CHARACTERISTICS|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Electrical Specifications: Unless otherwise indicated, V = 2.7V to 5.5V and GND = Ground. DD|||||||
|Parameters|Sym|Min|Typ|Max|Units|Conditions|
|Temperature Ranges|||||||
|Specified Temperature Range|T A|-40|—|+125|°C|(Note 1)|
|Operating Temperature Range|T A|-40|—|+125|°C||
|Storage Temperature Range|T A|-65|—|+150|°C||
|Thermal Package Resistances|||||||
|Thermal Resistance, 8L-DFN|θ JA|—|68|—|°C/W||
|Thermal Resistance, 8L-MSOP|θ JA|—|211|—|°C/W||


**Note 1:** Operation in this range must not cause T J to exceed Maximum Junction Temperature (+150°C).

DS25095A-page 4 © 2011 Microchip Technology Inc.


-----

## **MCP9808**

**Note 1:** All values referred to V IL MAX and V IH MIN levels.
**2:** If t LOW    - t OUT or t HIGH    - t OUT, the temperature sensor I [2] C interface will time-out. A Repeat Start command
is required for communication.
**3:** This device can be used in a Standard mode I [2] C bus system, but the requirement, t SU-DI ≥ 100 ns, must
be met. This device does not stretch the SCL Low time.

**4:** As a transmitter, the device provides internal minimum delay time, t HD-DO MIN, to bridge the undefined
region (min. 200 ns) of the falling edge of SCL, t F MAX, to avoid unintended generation of Start or Stop
conditions.

**5:** As a receiver, SDA should not be sampled at the falling edge of SCL. SDA can transition t HD-DI 0 ns after
SCL toggles Low.
#### **TIMING DIAGRAM**

|SENSOR SERIAL INTERFACE TIMING SPECIFICATIONS|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Electrical Specifications: Unless otherwise indicated, V = 2.7V to 5.5V, T = -40°C to +125°C, GND = Ground DD A and C = 80 pF. (Note 1) L||||||
|Parameters|Sym|Min|Max|Units|Conditions|
|2-Wire SMBus/Standard Mode I2C™ Compatible Interface (Note 1)||||||
|Serial Port Clock Frequency|f SC|0|400|kHz|(Note 2, 4)|
|Low Clock|t LOW|1300|—|ns|(Note 2)|
|High Clock|t HIGH|600|—|ns|(Note 2)|
|Rise Time|t R|20|300|ns||
|Fall Time|t F|20|300|ns||
|Data in Setup Time|t SU-DI|100|—|ns|(Note 3)|
|Data In Hold Time|t HD-DI|0|—|ns|(Note 5)|
|Data Out Hold Time|t HD-DO|200|900|ns|(Note 4)|
|Start Condition Setup Time|t SU-START|600|—|ns||
|Start Condition Hold Time|t HD-START|600|—|ns||
|Stop Condition Setup Time|t SU-STOP|600|—|ns||
|Bus Free|t B-FREE|1300|—|ns||
|Time-out|t OUT|25|35|ms||
|Bus Capacitive Load|C b|—|400|pf||


t HD-START

t SU-START


t HIGH t LOW

t OUT
t R, t F

t SU-DI t HD-DI/ t HD-DO


t B-F R EE
t S U-ST O P


SCL

SDA


START Condition Data Transmission STOP Condition

© 2011 Microchip Technology Inc. DS25095A-page 5


-----

## **MCP9808**
###### **NOTES:**

DS25095A-page 6 © 2011 Microchip Technology Inc.


-----

## **MCP9808**
#### **2.0 TYPICAL PERFORMANCE CURVES**

**Note:** The graphs and tables provided following this note are a statistical summary based on a limited number of
samples and are provided for informational purposes only. The performance characteristics listed herein
are not tested or guaranteed. In some graphs or tables, the data presented may be outside the specified
operating range (e.g., outside specified power supply range) and therefore outside the warranted range.

**Note:** Unless otherwise indicated, V DD = 2.7V to 5.5V, GND = Ground, SDA/SCL pulled-up to V DD and
T A = -40°C to +125°C.


**1.0**

**0.5**


**40%**

**30%**


**0.0**

**-0.5**


**-1.0**


**20%**

**10%**

**0%**

|Col1|VDD 854 240|= 3.3V units a units a|t -20 t -40° °|C, 25C, C, 125° C °|85C, 1 °|00C °|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||+Std Av -Std|. Dev. erage . Dev.||+3 * Std -3 * Std|. Dev. . Dev.||||


**-40** **-20** **0** **20** **40** **60** **80** **100** **120**

**T** **A** **(°C)**


**Temperature Accuracy (°C)**

###### *FIGURE 2-1: Temperature Accuracy.*

###### *FIGURE 2-4: Temperature Accuracy * *Histogram.*


**40%**

**30%**


**40%**

**30%**


**20%**

**10%**

**0%**


**20%**

**10%**

**0%**


**Temperature Accuracy (°C)**


**Temperature Accuracy (°C)**

###### *FIGURE 2-2: Temperature Accuracy * *Histogram, T A = -20°C.*

###### *FIGURE 2-5: Temperature Accuracy * *Histogram, T A = +85°C.*


**40%**

**30%**


**40%**

**30%**


**20%**

**10%**

**0%**


**20%**

**10%**

**0%**


**Temperature Accuracy (°C)**


**Temperature Accuracy (°C)**

###### *FIGURE 2-3: Temperature Accuracy * *Histogram, T A = +25°C.*

###### *FIGURE 2-6: Temperature Accuracy * *Histogram, T A = +100°C.*


© 2011 Microchip Technology Inc. DS25095A-page 7


-----

## **MCP9808**

**Note:** Unless otherwise indicated, V DD = 2.7V to 5.5V, GND = Ground, SDA/SCL pulled-up to V DD and
T A = -40°C to +125°C.


**40%**

**30%**


**20%**

**10%**

**0%**


**40%**

**30%**

**20%**

**10%**


**0%**


**Temperature Accuracy (°C)**


**Temperature Accuracy (°C)**

###### *FIGURE 2-7: Temperature Accuracy * *Histogram, T A = -40°C.*

###### *FIGURE 2-10: Temperature Accuracy * *Histogram, T A = +125°C.*


**400**

**350**

**300**

**250**

**200**

**150**

**100**


**1.00**

**0.50**

**0.00**


**-0.50**

**-1.00**

|VDD = VDD =|2.7V 3.3V|Col3|∆°C/|∆VDD = 0|.1°C/V|Col7|
|---|---|---|---|---|---|---|
|VDD =|5.5V||||||
||||||||
||||||||


**-40** **-20** **0** **20** **40** **60** **80** **100** **120**

**Temperature (°C)**


**-40** **-20** **0** **20** **40** **60** **80** **100** **120**

**Temperature (°C)**

###### *FIGURE 2-8: Supply Current vs. * *Temperature.*

###### *FIGURE 2-11: Temperature Accuracy vs * *Supply Voltage.*


**3**

**2.5**

**2**


**1000**

**100**


**1.5**

**1**


**10**

|0.06 0.12 0.25|25°C 5°C °C|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|0.5°|C||||||


**-40** **-20** **0** **20** **40** **60** **80** **100** **120**

**Temperature (°C)**


**-40** **-20** **0** **20** **40** **60** **80** **100** **120**

**Temperature (°C)**

###### *FIGURE 2-9: Power-on Reset Threshold * *Voltage vs. Temperature.*

###### *FIGURE 2-12: Temperature Conversion * *Time vs. Temperature.*


DS25095A-page 8 © 2011 Microchip Technology Inc.


-----

## **MCP9808**

**Note:** Unless otherwise indicated, V DD = 2.7V to 5.5V, GND = Ground, SDA/SCL pulled-up to V DD and
T A = -40°C to +125°C.


**0.4**

**0.3**


**0.2**

**0.1**


**35**

**30**

**25**


**0**

|IOL = 3|mA|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
|SDA|VOL||||A|lert VOL|||
||||||||||



**-40** **-20** **0** **20** **40** **60** **80** **100** **120**

**Temperature (°C)**


**20**


**-40** **-20** **0** **20** **40** **60** **80** **100** **120**

**Temperature (°C)**

###### *FIGURE 2-13: SDA and Alert Output V OL* *vs. Temperature.*

###### *FIGURE 2-16: SMBus Time-out vs. * *Temperature.*


**48**

**42**

**36**

**30**

**24**

**18**

**12**

**6**

**-40** **-20** **0** **20** **40** **60** **80** **100** **120**

**Temperature (°C)**


**2.00**

**1.50**

**1.00**


**0.50**

**0.00**

**-40** **-20** **0** **20** **40** **60** **80** **100** **120**

**Temperature (°C )**

###### *FIGURE 2-14: SDA I OL vs. Temperature.*

###### *FIGURE 2-17: Shutdown Current vs * *Temperature.*


**120%**

**100%**


**1.0**

**0.5**


**80%**

**60%**

**40%**

**20%**


**0.0**

**-0.5**


**-1.0**

|∆°C/∆VDD, V|DD = 3.3V + 1|50 mVPP (AC)|TTAA == +252°5C°C|
|---|---|---|---|
|||||
|||||
|No decoupli|ng capacitor|||


**0%**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||MS|OP-8|||||
||||DF|N-8|||||
|||||Roo|m to|+125°C|(Oil bat|h)|


**-2** **0** **2** **4** **6** **8** **10** **12** **14** **16**

**Time (s)**


**100** **100** ~~**1k**~~ **1k** **1,000** ~~**10k**~~ **10k** **10,000** ~~**100k**~~ **100k** **100,000** **1,000,000** ~~**1M**~~ **1M**

**Frequency (Hz)**

###### *FIGURE 2-15: Package Thermal * *Response.*

###### *FIGURE 2-18: Power Supply Rejection vs. * *Frequency.*


© 2011 Microchip Technology Inc. DS25095A-page 9


-----

## **MCP9808**
###### **NOTES:**

DS25095A-page 10 © 2011 Microchip Technology Inc.


-----

#### **3.0 PIN DESCRIPTION**

The descriptions of the pins are listed in Table 3-1.
###### **TABLE 3-1: PIN FUNCTION TABLE**
##### **3.1 Serial Data Line (SDA) **

SDA is a bidirectional input/output pin, used to serially
transmit data to/from the host controller. This pin
requires a pull-up resistor. (See **Section 4.0 “Serial**
**Communication”** .) **3.2 Serial Clock Line (SCL)**

The SCL is a clock input pin. All communication and
timing is relative to the signal on this pin. The clock is
generated by the host or master controller on the bus.
(See **Section 4.0 “Serial Communication”** .) **3.3 Temperature Alert, Open-Drain ** **Output (Alert)**

The MCP9808 temperature Alert output pin is an
open-drain output. The device outputs a signal when the
ambient temperature goes beyond the user-programmed
temperature limit. (See **Section 5.2.3 “Alert Output**
**Configuration”** ). **3.4 Ground Pin (GND)**

The GND pin is the system ground pin.

## **MCP9808**
##### **3.5 Address Pins (A0, A1, A2)**

These pins are device address input pins.

|DFN|MSOP|Symbol|Pin Function|
|---|---|---|---|
|1|1|SDA|Serial Data Line|
|2|2|SCL|Serial Clock Line|
|3|3|Alert|Temperature Alert Output|
|4|4|GND|Ground|
|5|5|A2|Slave Address|
|6|6|A1|Slave Address|
|7|7|A0|Slave Address|
|8|8|V DD|Power Pin|
|9|—|EP|Exposed Thermal Pad (EP); must be connected to GND|



The address pins correspond to the Least Significant
bits (LSbs) of the address bits and the Most Significant
bits (MSbs): A6, A5, A4, A3. This is illustrated in
Table 3-2.
###### **TABLE 3-2: MCP9808 ADDRESS BYTE**

**Note 1:** User-selectable address is shown by ‘ `x` ’.
A2, A1 and A0 must match the
corresponding device pin configuration.

**2:** Contact factory for this address code.
##### **3.6 Power Pin (V DD )**

|Device|Address Code|Col3|Col4|Col5|Slave Address|Col7|Col8|
|---|---|---|---|---|---|---|---|
||A6|A5|A4|A3|A2|A1|A0|
|MCP9808|0|0|1|1|x(1)|x|x|
|MCP9808(2)|1|0|0|1|x|x|x|



V DD is the power pin. The operating voltage range, as
specified in the DC electrical specification table, is
applied on this pin. **3.7 Exposed Thermal Pad (EP)**

There is an internal electrical connection between the
Exposed Thermal Pad (EP) and the GND pin. The EP
may be connected to the system ground on the Printed
Circuit Board (PCB).


© 2011 Microchip Technology Inc. DS25095A-page 11


-----

## **MCP9808**
###### **NOTES:**

DS25095A-page 12 © 2011 Microchip Technology Inc.


-----

#### **4.0 SERIAL COMMUNICATION**
##### **4.1 2-Wire Standard Mode I [2] C™ ** **Protocol Compatible Interface**

The MCP9808 Serial Clock (SCL) input and the
bidirectional Serial Data (SDA) line form a 2-wire
bidirectional, Standard mode, I [2] C compatible
communication port (refer to the **Digital Input/Output**
**Pin Characteristics** and **Sensor Serial Interface**

**Timing Specifications** tables).

The following bus protocol has been defined:

## **MCP9808**
###### 4.1.1 DATA TRANSFER

Data transfers are initiated by a Start condition
(START), followed by a 7-bit device address and a
read/write bit. An Acknowledge (ACK) from the slave
confirms the reception of each byte. Each access must
be terminated by a Stop condition (STOP).

Repeated communication is initiated after t B-FREE .

This device does not support sequential register
read/write. Each register needs to be addressed using
the Register Pointer.

This device supports the receive protocol. The register
can be specified using the pointer for the initial read.
Each repeated read or receive begins with a Start
condition and address byte. The MCP9808 retains the
previously selected register. Therefore, it outputs data
from the previously specified register (repeated pointer
specification is not necessary). 4.1.2 MASTER/SLAVE

The bus is controlled by a master device (typically a
microcontroller) that controls the bus access and
generates the Start and Stop conditions. The MCP9808
is a slave device and does not control other devices in

the bus. Both master and slave devices can operate as
either transmitter or receiver. However, the master
device determines which mode is activated. 4.1.3 START/STOP CONDITION

A high-to-low transition of the SDA line (while SCL is
high) is the Start condition. All data transfers must be
preceded by a Start condition from the master. A
low-to-high transition of the SDA line (while SCL is
high) signifies a Stop condition.

If a Start or Stop condition is introduced during data
transmission, the MCP9808 releases the bus. All data
transfers are ended by a Stop condition from the
master.

|TABLE 4-1:|MCP9808 SERIAL BUS PROTOCOL DESCRIPTIONS|
|---|---|
|Term|Description|
|Master|The device that controls the serial bus, typically a microcontroller.|
|Slave|The device addressed by the master, such as the MCP9808.|
|Transmitter|Device sending data to the bus.|
|Receiver|Device receiving data from the bus.|
|START|A unique signal from the master to initiate serial interface with a slave.|
|STOP|A unique signal from the master to terminate serial interface from a slave.|
|Read/Write|A read or write to the MCP9808 registers.|
|ACK|A receiver Acknowledges (ACK) the reception of each byte by polling the bus.|
|NAK|A receiver Not-Acknowledges (NAK) or releases the bus to show End-of-Data (EOD).|
|Busy|Communication is not possible because the bus is in use.|
|Not Busy|The bus is in the Idle state; both SDA and SCL remain high.|
|Data Valid|SDA must remain stable before SCL becomes high in order for a data bit to be considered valid. During normal data transfers, SDA only changes state while SCL is low.|


© 2011 Microchip Technology Inc. DS25095A-page 13


-----

## **MCP9808**
###### 4.1.4 ADDRESS BYTE

Following the Start condition, the host must transmit an
8-bit address byte to the MCP9808. The address for the
MCP9808 temperature sensor is ‘ `0011,A2,A1,A0` ’ in
binary, where the A2, A1 and A0 bits are set externally
by connecting the corresponding pins to V DD ‘ `1` ’ or GND
‘ `0` ’. The 7-bit address, transmitted in the serial bit stream,
must match the selected address for the MCP9808 to
respond with an ACK. Bit 8 in the address byte is a
read/write bit. Setting this bit to ‘ `1` ’ commands a read
operation, while ‘ `0` ’ commands a write operation (see
Figure 4-1).

Address Byte

SCL 1 2 3 4 5 6 7 8 9

AC

SDA 0 0 1 1 A2 A1 A0 K

Start

Address Slave

Code Address R/W

**MCP9808** Response

**See** Table 3-2. *FIGURE 4-1: Device Addressing.*

###### 4.1.5 DATA VALID

After the Start condition, each bit of data in the
transmission needs to be settled for a time specified by
t SU-DATA before SCL toggles from low-to-high (see the
Sensor Serial Interface Timing Specifications section). 4.1.6 ACKNOWLEDGE (ACK/NAK)

Each receiving device, when addressed, must
generate an ACK bit after the reception of each byte.
The master device must generate an extra clock pulse
for ACK to be recognized.

The Acknowledging device pulls down the SDA line for
t SU-DATA before the low-to-high transition of SCL from
the master. SDA also needs to remain pulled down for
t H-DATA after a high-to-low transition of SCL.

During read, the master must signal an End-of-Data
(EOD) to the slave, by not generating an ACK bit
(NAK), once the last bit has been clocked out of the
slave. In this case, the slave will leave the data line
released to enable the master to generate the Stop
condition. 4.1.7 TIME-OUT

If the SCL stays low or high for the time specified by
t OUT, the MCP9808 temperature sensor resets the
serial interface. This dictates the minimum clock speed
as outlined in the specification.


DS25095A-page 14 © 2011 Microchip Technology Inc.


-----

## **MCP9808**

#### **5.0 FUNCTIONAL DESCRIPTION**

The MCP9808 temperature sensors consist of a bandgap-type temperature sensor, a Delta-Sigma Analog-toDigital Converter (ΔΣ ADC), user-programmable
registers and a 2-wire SMBus/I [2] C protocol compatible
serial interface. Figure 5-1 shows a block diagram of the
register structure.

Hysteresis

Shutdown

Critical Trip Lock

Alarm Win. Lock

Clear Alert

Alert Status

Output Control

Critical Alert Only

Alert Polarity

Alert Comp/Int

Configuration

Tem p erature

T UPPER Limit

T LOWER Limit

T CRITICAL Limit

Manufacturer ID

Device ID/Rev

Resolution

Register
Pointer

SMBus/Standard I [2] C™
Interface


Band Gap
Temperature
Sensor

ΔΣ ADC

+0.5°C
+0.25°C
+0.125°C
+0.0625°C


A0 A1 A2 Alert SDA SCL V DD GND
###### *FIGURE 5-1: Functional Block Diagram.*

© 2011 Microchip Technology Inc. DS25095A-page 15


-----

## **MCP9808**
##### 5.1 Registers Section 5.2.3 “Alert Output Configuration” ). In

addition, the Critical Temperature Limit register is used

The MCP9808 has several registers that are

to provide an additional critical temperature limit.

user-accessible. These registers include the Tempera
The Configuration register provides access to

ture register, Configuration register, Temperature Alert

configure the MCP9808 device’s various features.

Upper Boundary and Lower Boundary Limit registers,

These registers are described in further detail in the

Critical Temperature Limit register, Manufacturer

following sections.

Identification register and Device Identification register.

The registers are accessed by sending a Register

The Temperature register is read-only, used to access

Pointer to the MCP9808, using the serial interface. This

the ambient temperature data. This register is double
is an 8-bit write-only pointer. However, the four Least

buffered and it is updated every t CONV . The Temperature

Significant bits are used as pointers and all unused bits

Alert Upper Boundary and Lower Boundary Limit

(Register Pointer<7:4>) need to be cleared or set to ‘ `0` ’.

registers are read/write registers. If the ambient

Register 5-1 describes the pointer or the address of

temperature drifts beyond the user-specified limits, the

each register.

MCP9808 outputs a signal using the Alert pin (refer to

**Legend:**

R = Readable bit W = Writable bit U = Unimplemented bit, read as ‘0’

-n = Value at POR ‘1’ = Bit is set ‘0’ = Bit is cleared x = Bit is unknown

bit 7-4 **W:** Writable bits

Write ‘ `0` ’.

Bits 7-4 must always be cleared or written to ‘ `0` ’. This device has additional registers that are reserved
for test and calibration. If these registers are accessed, the device may not perform according to the
specification.

bit 3-0 **Pointer bits**

`0000` = RFU, Reserved for Future Use (Read-Only register)
`0001` = Configuration register (CONFIG)
`0010` = Alert Temperature Upper Boundary Trip register (T UPPER )
`0011` = Alert Temperature Lower Boundary Trip register (T LOWER )
`0100` = Critical Temperature Trip register (T CRIT )
`0101` = Temperature register (T A )
`0110` = Manufacturer ID register
`0111` = Device ID/Revision register
`1000` = Resolution register
`1xxx` = Reserved **[(][1][)]**

**Note 1:** Some registers contain calibration codes and should not be accessed.

DS25095A-page 16 © 2011 Microchip Technology Inc.

|REGISTER 5-1: REGISTER POINTER (WRITE-ONLY)|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|W-0 W-0 W-0 W-0 W-0 W-0 W-0 W-0|||||
|—|—|—|—|Pointer bits|
|bit 7 bit 0|||||


-----

## **MCP9808**
###### **TABLE 5-1: BIT ASSIGNMENT SUMMARY FOR ALL REGISTERS **

© 2011 Microchip Technology Inc. DS25095A-page 17

|Col1|Col2|(See Section 5.3 “Summary of Power-on Default” for Power-on Defaults)|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|Register Pointer (Hex)|MSB/ LSB|Bit Assignment||||||||
|||7|6|5|4|3|2|1|0|
|0x00|MSB|0|0|0|0|0|0|0|0|
||LSB|0|0|0|1|1|1|1|1|
|0x01|MSB|0|0|0|0|0|Hysteresis||SHDN|
||LSB|Crt Loc|Win Loc|Int Clr|Alt Stat|Alt Cnt|Alt Sel|Alt Pol|Alt Mod|
|0x02|MSB|0|0|0|SIGN|27°C|26°C|25°C|24°C|
||LSB|23°C|22°C|21°C|20°C|2-1°C|2-2°C|0|0|
|0x03|MSB|0|0|0|SIGN|27°C|26°C|25°C|24°C|
||LSB|23°C|22°C|21°C|20°C|2-1°C|2-2°C|0|0|
|0x04|MSB|0|0|0|SIGN|27°C|26°C|25°C|24°C|
||LSB|23°C|22°C|21°C|20°C|2-1°C|2-2°C|0|0|
|0x05|MSB|T ≥ T A CRIT|T > T A UPPER|T < T A LOWER|SIGN|27°C|26°C|25°C|24°C|
||LSB|23°C|22°C|21°C|20°C|2-1°C|2-2°C|2-3°C|2-4°C|
|0x06|MSB|0|0|0|0|0|0|0|0|
||LSB|0|1|0|1|0|1|0|0|
|0x07|MSB|0|0|0|0|0|1|0|0|
||LSB|0|0|0|0|0|0|0|0|
|0x08|LSB|0|0|0|0|0|0|1|1|


-----

## **MCP9808**
###### 5.1.1 SENSOR CONFIGURATION user-specified temperature boundary (see REGISTER (CONFIG) Section 5.2.2 “Temperature Hysteresis (T HYST )” .

The Continuous Conversion or Shutdown mode is

The MCP9808 has a 16-bit Configuration register

selected using bit 8. In Shutdown mode, the band gap

(CONFIG) that allows the user to set various functions for

temperature sensor circuit stops converting

a robust temperature monitoring system. Bits 10 through

temperature and the Ambient Temperature register

0 are used to select the temperature alert output
hysteresis, device shutdown or Low-Power mode, (T A ) holds the previous temperature data (see

**Section 5.2.1 “Shutdown Mode”** ). Bits 7 and 6 are

temperature boundary and critical temperature lock, and
temperature Alert output enable/disable. In addition, Alert used to lock the user-specified boundaries T UPPER,
output condition (output set for T UPPER and T LOWER TThe Lock bits are cleared by resetting the power. Bits 5 LOWER and T CRIT to prevent an accidental rewrite.
temperature boundary or T CRIT only), Alert output status through 0 are used to configure the temperature Alert
and Alert output polarity and mode (Comparator Output

output pin. All functions are described in Register 5-2

or Interrupt Output mode) are user-configurable.

(see **Section 5.2.3 “Alert Output Configuration”** ).

The temperature hysteresis bits 10 and 9 can be used
to prevent output chatter when the ambient
temperature gradually changes beyond the

**Legend:**

R = Readable bit W = Writable bit U = Unimplemented bit, read as ‘0’

-n = Value at POR ‘1’ = Bit is set ‘0’ = Bit is cleared x = Bit is unknown

bit 15-11 **Unimplemented:** Read as ‘ `0` ’

bit 10-9 **T** **HYST** : T UPPER and T LOWER Limit Hysteresis bits
`00` = 0°C (power-up default)
`01` = +1.5°C

`10` = +3.0°C

`11` = +6.0°C

(Refer to **Section 5.2.3 “Alert Output Configuration”** .)

This bit can not be altered when either of the Lock bits are set (bit 6 and bit 7).

This bit can be programmed in Shutdown mode.

bit 8 **SHDN:** Shutdown Mode bit

`0` = Continuous conversion (power-up default)
`1` = Shutdown (Low-Power mode)

In shutdown, all power-consuming activities are disabled, though all registers can be written to or read.

This bit cannot be set to ‘ `1` ’ when either of the Lock bits is set (bit 6 and bit 7). However, it can be
cleared to ‘ `0` ’ for continuous conversion while locked (refer to **Section 5.2.1 “Shutdown Mode”** ).

DS25095A-page 18 © 2011 Microchip Technology Inc.

|REGISTER 5-2: CONFIG: CONFIGURATION REGISTER (→ ADDRESS ‘0000 0001’b)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|U-0 U-0 U-0 U-0 U-0 R/W-0 R/W-0 R/W-0|||||||
|—|—|—|—|—|T HYST|SHDN|
|bit 15 bit 8|||||||

|R/W-0 R/W-0 R/W-0 R-0 R/W-0 R/W-0 R/W-0 R/W-0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Crit. Lock|Win. Lock|Int. Clear|Alert Stat.|Alert Cnt.|Alert Sel.|Alert Pol.|Alert Mod.|
|bit 7 bit 0||||||||


-----

## **MCP9808**
###### REGISTER 5-2: CONFIG: CONFIGURATION REGISTER ( → ADDRESS ‘0000 0001’b ) 

bit 7 **Crit. Lock:** T CRIT Lock bit
`0` = Unlocked. T CRIT register can be written (power-up default)
`1` = Locked. T CRIT register can not be written

When enabled, this bit remains set to ‘ `1` ’ or locked until cleared by an internal Reset ( **Section 5.3**
**“Summary of Power-on Default”** ).

This bit can be programmed in Shutdown mode.

bit 6 **Win. Lock:** T UPPER and T LOWER Window Lock bit
`0` = Unlocked; T UPPER and T LOWER registers can be written (power-up default)
`1` = Locked; T UPPER and T LOWER registers can not be written

When enabled, this bit remains set to ‘ `1` ’ or locked until cleared by a Power-on Reset ( **Section 5.3**
**“Summary of Power-on Default”** ).

This bit can be programmed in Shutdown mode.

bit 5 **Int. Clear:** Interrupt Clear bit

`0` = No effect (power-up default)
`1` = Clear interrupt output; when read, this bit returns to ‘ `0` ’

This bit can not be set to ‘ `1` ’ in Shutdown mode, but it can be cleared after the device enters Shutdown
mode.

bit 4 **Alert Stat.:** Alert Output Status bit

`0` = Alert output is not asserted by the device (power-up default)
`1` = Alert output is asserted as a comparator/Interrupt or critical temperature output

This bit can not be set to ‘ `1` ’ or cleared to ‘ `0` ’ in Shutdown mode. However, if the Alert output is configured as Interrupt mode, and if the host controller clears to ‘ `0` ’, the interrupt, using bit 5 while the device
is in Shutdown mode, then this bit will also be cleared ‘ `0` ’.

bit 3 **Alert Cnt.:** Alert Output Control bit

`0` = Disabled (power-up default)
`1` = Enabled

This bit can not be altered when either of the Lock bits are set (bit 6 and bit 7).

This bit can be programmed in Shutdown mode, but the Alert output will not assert or deassert.

bit 2 **Alert Sel.:** Alert Output Select bit

`0` = Alert output for T UPPER, T LOWER and T CRIT (power-up default)
`1` = T A       - T CRIT only (T UPPER and T LOWER temperature boundaries are disabled)

When the Alarm Window Lock bit is set, this bit cannot be altered until unlocked (bit 6).

This bit can be programmed in Shutdown mode, but the Alert output will not assert or deassert.

bit 1 **Alert Pol.:** Alert Output Polarity bit

`0` = Active-low (power-up default; pull-up resistor required)
`1` = Active-high

This bit cannot be altered when either of the Lock bits are set (bit 6 and bit 7).

This bit can be programmed in Shutdown mode, but the Alert output will not assert or deassert.

bit 0 **Alert Mod.:** Alert Output Mode bit

`0` = Comparator output (power-up default)
`1` = Interrupt output

This bit cannot be altered when either of the Lock bits are set (bit 6 and bit 7).

This bit can be programmed in Shutdown mode, but the Alert output will not assert or deassert.

© 2011 Microchip Technology Inc. DS25095A-page 19


-----

## **MCP9808**

**Writing to the CONFIG Register to Enable the Event Output Pin** `<0000 0000 0000 1000>b:`

1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

SCL


A

0 0 0 0 0 0 0 0 C 0 0 0 0 1 0 0 0

K


A
C P
K


MSB Data


LSB Data

**MCP9808** **MCP9808**


**Note:** This is an example routine (see **Appendix A: “Source Code”** ).
```
     i2c_start(); // send START command

```
`i2c_write(AddressByte & 0xFE);` `//WRITE Command` (see **Section 4.1.4 “Address Byte”** )
```
                          //also, make sure bit 0 is cleared ‘0’
     i2c_write(0x01); // Write CONFIG Register
     i2c_write(0x00); // Write data
     i2c_write(0x08); // Write data
     i2c_stop(); // send STOP command
###### *FIGURE 5-2: Timing Diagram for Writing to the Configuration Register (see Section 4.0 “Serial * *Communication” ).*

```
DS25095A-page 20 © 2011 Microchip Technology Inc.


-----

**Reading the CONFIG Register:**

1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

SCL

A A
SDA S 0 0 1 1 A A A W C 0 0 0 0 0 0 0 1 C

2 1 0 K K

## **MCP9808**

**Note:** It is not necessary to
select the Register
Pointer if it was set
from the previous
read/write.


Address Byte


Configuration Pointer

**MCP9808** **MCP9808**


SCL

SDA


1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

S 0 0 1 1 A A A R AC 0 0 0 0 0 0 0 0 AC 0 0 0 0 1 0 0 0 NA P
2 1 0 K K K


Address Byte MSB Data LSB Data

Master Master
**MCP9808**

**Note:** This is an example routine (see **Appendix A: “Source Code”** ).
```
  i2c_start(); // send START command

```
`i2c_write(AddressByte & 0xFE);` `//WRITE Command` (see **Section 4.1.4 “Address Byte”** )
```
                      //also, make sure bit 0 is cleared ‘0’
  i2c_write(0x01); // Write CONFIG Register
  i2c_start(); // send Repeat START command
  i2c_write(AddressByte | 0x01); //READ Command
                      //also, make sure bit 0 is set ‘1’
  UpperByte = i2c_read(ACK); // READ 8 bits
                      //and Send ACK bit
  LowerByte = i2c_read(NAK); // READ 8 bits
                      //and Send NAK bit
  i2c_stop(); // send STOP command
###### *FIGURE 5-3: Timing Diagram for Reading from the Configuration Register (see Section 4.0 “Serial * *Communication” ).*

```
© 2011 Microchip Technology Inc. DS25095A-page 21


-----

## **MCP9808**
###### 5.1.2 UPPER/LOWER/CRITICAL TEMPERATURE LIMIT REGISTERS (T UPPER /T LOWER /T CRIT )

The MCP9808 has a 16-bit read/write Alert Output
Temperature Upper Boundary register (T UPPER ), a 16-bit
Lower Boundary register (T LOWER ) and a 16-bit Critical
Boundary register (T CRIT ) that contain 11-bit data in
two’s complement format (0.25°C). This data represents


the maximum and minimum temperature boundary or
temperature window that can be used to monitor
ambient temperature. If this feature is enabled
( **Section 5.1.1** **“Sensor** **Configuration** **Register**
**(CONFIG)”** ) and the ambient temperature exceeds the
specified boundary or window, the MCP9808 asserts an
Alert output. (Refer to **Section 5.2.3 “Alert Output**
**Configuration”** ).

###### **REGISTER 5-3: T UPPER /T LOWER /T CRIT UPPER/LOWER/CRITICAL TEMPERATURE LIMIT REGISTER**

**Legend:**

R = Readable bit W = Writable bit U = Unimplemented bit, read as ‘0’

-n = Value at POR ‘1’ = Bit is set ‘0’ = Bit is cleared x = Bit is unknown

bit 15-13 **Unimplemented:** Read as ‘ `0` ’

bit 12 **Sign:** Sign bit
`0` = T A ≥ 0°C
`1` = T A < 0°C

bit 11-2 **T** **UPPER** **/T** **LOWER** **/T** **CRIT** **:** Temperature Boundary bits
Temperature boundary trip data in two’s complement format.

bit 1-0 **Unimplemented:** Read as ‘ `0` ’

**Note 1:** This table shows two 16-bit registers for T UPPER, T LOWER and T CRIT, located at ‘ `0000 0010b` ’,
‘ `0000 0011b` ’ and ‘ `0000 0100b` ’, respectively.

DS25095A-page 22 © 2011 Microchip Technology Inc.

|UPPERLOWERCRIT (→ ADDRESS ‘0000 0010’b/‘0000 0011’b/‘0000 0100’b)(1)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|U-0 U-0 U-0 R/W-0 R/W-0 R/W-0 R/W-0 R/W-0||||||||
|—|—|—|Sign|27°C|26°C|25°C|24°C|
|bit 15 bit 8||||||||

|R/W-0 R/W-0 R/W-0 R/W-0 R/W-0 R/W-0 U-0 U-0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|23°C|22°C|21°C|20°C|2-1°C|2-2°C|—|—|
|bit 7 bit 0||||||||


-----

## **MCP9808**


**Writing +90°C to the T** **UPPER** **Register** `<0000 0101 1010 0000>b` **:**

1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

SCL

A

0 0 0 0 0 1 0 1 C 1 0 1 0 0 0 0 0

K


A
C P
K


MSB Data


LSB Data

**MCP9808** **MCP9808**


**Reading from the T** **UPPER** **Register:**

1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

SCL

A A
SDA S 0 0 1 1 A A A W C 0 0 0 0 0 0 1 0 C

2 1 0 K K


**Note:** It is not necessary to
select the Register
Pointer if it was set
from the previous
read/write.


Address Byte


T UPPER Pointer

**MCP9808** **MCP9808**


SCL

SDA


1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

S 0 0 1 1 A A A R AC 0 0 0 0 0 1 0 1 AC 1 0 1 0 0 0 0 0 NA P
2 1 0 K K K


Address Byte MSB Data LSB Data

**MCP9808** Master Master
###### *FIGURE 5-4: Timing Diagram for Writing and Reading from the T UPPER Register (see Section 4.0 * *“Serial Communication” ).*

© 2011 Microchip Technology Inc. DS25095A-page 23


-----

## **MCP9808**
###### 5.1.3 AMBIENT TEMPERATURE In addition, the T A register uses three bits (T A <15:13>) REGISTER (T A ) to reflect the Alert pin state. This allows the user to

identify the cause of the Alert output trigger (see

The MCP9808 uses a band gap temperature sensor

**Section 5.2.3 “Alert Output Configuration”** ); bit 15 is

circuit to output analog voltage proportional to absolute

set to ‘ `1` ’ if T A is greater than or equal to T CRIT, bit 14 is

temperature. An internal ΔΣ ADC is used to convert the set to ‘ `1` ’ if T A is greater than T UPPER and bit 13 is set to
analog voltage to a digital word. The digital word is ‘
loaded to a 16-bit read-only Ambient Temperature `1` ’ if T A is less than T LOWER . register (T A ) that contains 13-bit temperature data in The T A register bit assignment and boundary

two’s complement format. conditions are described in Register 5-4.

The T A register bits (T A <12:0>) are double-buffered.
Therefore, the user can access the register, while in the
background, the MCP9808 performs an Analog-toDigital conversion. The temperature data from the ΔΣ
ADC is loaded in parallel to the T A register at t CONV
refresh rate.

**Legend:**

R = Readable bit W = Writable bit U = Unimplemented bit, read as ‘0’

-n = Value at POR ‘1’ = Bit is set ‘0’ = Bit is cleared x = Bit is unknown

bit 15 **T** **A** **vs. T** **CRIT** **bit** **(1)**

`0` = T A < T CRIT
`1` = T A ≥ T CRIT
bit 14 **T** **A** **vs. T** **UPPER** **bit** **[(][1][)]**

`0` = T A ≤ T UPPER
`1` = T A       - T UPPER
bit 13 **T** **A** **vs. T** **LOWER** **bit** **[(][1][)]**

`0` = T A ≥ T LOWER
`1` = T A < T LOWER

bit 12 **SIGN bit**

`0` = T A ≥ 0°C
`1` = T A < 0°C

bit 11-0 **T** **A** **:** Ambient Temperature bits **[(][2][)]**

12-bit ambient temperature data in two’s complement format.

**Note 1:** Bits 15, 14 and 13 are not affected by the status of the Alert Output Configuration (CONFIG<5:0> bits,
Register 5-2).

**2:** Bits 2, 1 and 0 may remain clear at ‘ `0` ’ depending on the status of the Resolution register (Register 5-7).
The power-up default is 0.25°C/bit; bits 1 and 0 remain clear ‘ `0` ’.

DS25095A-page 24 © 2011 Microchip Technology Inc.

|REGISTER 5-4: TA: AMBIENT TEMPERATURE REGISTER (→ ADDRESS ‘0000 0101’b)(1)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|R-0 R-0 R-0 R-0 R-0 R-0 R-0 R-0||||||||
|T vs. T (1) A CRIT|T vs. T (1) A UPPER|T vs. T (1) A LOWER|SIGN|27 °C|26 °C|25 °C|24 °C|
|bit 15 bit 8||||||||

|R-0 R-0 R-0 R-0 R-0 R-0 R-0 R-0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|23 °C|22 °C|21 °C|20 °C|2-1 °C|2-2 °C(2)|2-3 °C(2)|2-4 °C(2)|
|bit 7 bit 0||||||||


-----

###### 5.1.3.1 T A Bits to Temperature Conversion

To convert the T A bits to decimal temperature, the
upper three boundary bits (T A <15:13>) must be
masked out. Then, determine the SIGN bit (bit 12) to
check positive or negative temperature, shift the bits
accordingly, and combine the upper and lower bytes of
the 16-bit register. The upper byte contains data for
temperatures greater than +32°C while the lower byte
contains data for temperature less than +32°C, including fractional data. When combining the upper and
lower bytes, the upper byte must be right-shifted by
4 bits (or multiply by 2 [4] ) and the lower byte must be leftshifted by 4 bits (or multiply by 2 [-4] ). Adding the results
of the shifted values provides the temperature data in
decimal format (see Equation 5-1).

The temperature bits are in two’s compliment format,
therefore, positive temperature data and negative temperature data are computed differently. Equation 5-1
shows the temperature computation. The example **EXAMPLE 5-1: SAMPLE INSTRUCTION CODE**

## **MCP9808**

instruction code, outlined in Example 5-1, shows the
communication flow; also see Figure 5-5 for the timing
diagram.
###### **EQUATION 5-1: BYTES TO ** **TEMPERATURE ** **CONVERSION**

Temperature *T* *A* ≥ 0°C –

*TA* *=* ( *UpperByte* × *2* *[4]* *+* *LowerByte* × *2* *[4]* )

Temperature < 0°C –

*TA* *=* *256* – ( *UpperByte* × *2* *[4]* *+* *LowerByte* × *2* *[4]* )

Where:

T A = Ambient Temperature (°C)

UpperByte = T A bit 15 to bit 8

LowerByte = T A bit 7 to bit 0


**This example routine assumes the variables and I** **[2]** **C™ communication subroutines are predefined**
**(see Appendix A: “Source Code”):**

i `2c_start();` `// send START command`

`i2c_write (AddressByte & 0xFE);` `//WRITE Command` (see **Section 4.1.4 “Address Byte”** )
```
                           //also, make sure bit 0 is cleared ‘0’
     i2c_write(0x05); // Write T A Register Address
     i2c_start(); //Repeat START

```
`i2c_write(AddressByte | 0x01);` `// READ Command` (see **Section 4.1.4 “Address Byte”** )
```
                           //also, make sure bit 0 is Set ‘1’
     UpperByte = i2c_read(ACK); // READ 8 bits
                           //and Send ACK bit
     LowerByte = i2c_read(NAK); // READ 8 bits
                           //and Send NAK bit
     i2c_stop(); // send STOP command
     //Convert the temperature data
     //First Check flag bits
     if ((UpperByte & 0x80) == 0x80){ //T A ³ T CRIT
     }
     if ((UpperByte & 0x40) == 0x40){ //T A > T UPPER
     }
     if ((UpperByte & 0x20) == 0x20){ //T A < T LOWER
     }
     UpperByte = UpperByte & 0x1F; //Clear flag bits
     if ((UpperByte & 0x10) == 0x10){ //T A < 0°C
        UpperByte = UpperByte & 0x0F; //Clear SIGN
        Temperature = 256 - (UpperByte x 16 + LowerByte / 16);
     }else //T A  ³ 0°C
        Temperature = (UpperByte x 16 + LowerByte / 16);
                           // Temperature = Ambient Temperature (°C)

```
© 2011 Microchip Technology Inc. DS25095A-page 25


-----

## **MCP9808**

1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

SCL

A A
SDA S 0 0 1 1 A A A W C 0 0 0 0 0 1 0 1 C

2 1 0 K K


**Note:** It is not necessary to
select the Register
Pointer if it was set from

the previous read/write.


Address Byte


T A Pointer

**MCP9808** **MCP9808**


SCL

SDA


1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

A A N

S 0 0 1 1 A A A R C 0 0 0 0 0 0 0 1 C 1 0 0 1 0 1 0 0 A P
2 1 0 K K K


Address Byte MSB Data LSB Data

**MCP9808** Master Master
###### *FIGURE 5-5: Timing Diagram for Reading +25.25°C Temperature from the T A Register * *(see Section 4.0 “Serial Communication” ).*

DS25095A-page 26 © 2011 Microchip Technology Inc.


-----

## **MCP9808**
###### 5.1.4 MANUFACTURER ID REGISTER

This register is used to identify the manufacturer of the
device in order to perform manufacturer-specific
operation. The Manufacturer ID for the MCP9808 is
0x0054 (hexadecimal). REGISTER 5-5: MANUFACTURER ID REGISTER – READ-ONLY ( → ADDRESS ‘0000 0110’b )

R-0 R-0 R-0 R-0 R-0 R-0 R-0 R-0

Manufacturer ID

bit 15 bit 8

R-0 R-1 R-0 R-1 R-0 R-1 R-0 R-0

Manufacturer ID

bit 7 bit 0

**Legend:**

R = Readable bit W = Writable bit U = Unimplemented bit, read as ‘0’

-n = Value at POR ‘1’ = Bit is set ‘0’ = Bit is cleared x = Bit is unknown

bit 15-0 **Device Manufacturer Identification bits**


1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

SCL

A A
SDA S 0 0 1 1 A A A W C 0 0 0 0 0 1 1 0 C

2 1 0 K K


**Note:** It is not necessary to
select the Register
Pointer if it was set
from the previous
read/write.


Address Byte


Manufacturer ID Pointer

**MCP9808** **MCP9808**


SCL

SDA


1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

S 0 0 1 1 A A A R AC 0 0 0 0 0 0 0 0 AC 0 1 0 1 0 1 0 0 NA P
2 1 0 K K K


Address Byte MSB Data LSB Data

**MCP9808** Master Master
###### *FIGURE 5-6: Timing Diagram for Reading the Manufacturer ID Register (see Section 4.0 “Serial * *Communication” ).*

© 2011 Microchip Technology Inc. DS25095A-page 27


-----

## **MCP9808**
###### 5.1.5 DEVICE ID AND REVISION REGISTER

The upper byte of this register is used to specify the
device identification and the lower byte is used to
specify the device revision. The Device ID for the
MCP9808 is 0x04 (hex).

The revision begins with 0x00 (hex) for the first release,
with the number being incremented as revised versions
are released. REGISTER 5-6: DEVICE ID AND DEVICE REVISION – READ-ONLY ( → ADDRESS ‘0000 0111’b)

R-0 R-0 R-0 R-0 R-0 R-1 R-0 R-0

Device ID

bit 15 bit 8

R-0 R-0 R-0 R-0 R-0 R-0 R-0 R-0

Device Revision

bit 7 bit 0

**Legend:**

R = Readable bit W = Writable bit U = Unimplemented bit, read as ‘0’

-n = Value at POR ‘1’ = Bit is set ‘0’ = Bit is cleared x = Bit is unknown

bit 15-8 **Device ID:** Bit 15 to bit 8 are used for device ID

bit 7-0 **Device Revision:** Bit 7 to bit 0 are used for device revision


1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

SCL

A A
SDA S 0 0 1 1 A A A W C 0 0 0 0 0 1 1 1 C

2 1 0 K K


**Note:** It is not necessary to
select the Register
Pointer if it was set
from the previous
read/write.


Address Byte


Device ID Pointer

**MCP9808** **MCP9808**


SCL

SDA


1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

S 0 0 1 1 A A A R AC 0 0 0 0 0 1 0 0 AC 0 0 0 0 0 0 0 0 NA P
2 1 0 K K K


Address Byte MSB Data LSB Data

Master Master
**MCP9808**
###### *FIGURE 5-7: Timing Diagram for Reading Device ID and Device Revision Register (see * *Section 4.0 “Serial Communication” ).*

DS25095A-page 28 © 2011 Microchip Technology Inc.


-----

## **MCP9808**
###### 5.1.6 RESOLUTION REGISTER

This register allows the user to change the sensor
resolution (see **Section 5.2.4** **“Temperature**
**Resolution”** ). The POR default resolution is
+0.0625°C. The selected resolution is also reflected in
the Capability register (see Register 5-2).

**Legend:**

R = Readable bit W = Writable bit U = Unimplemented bit, read as ‘0’

-n = Value at POR ‘1’ = Bit is set ‘0’ = Bit is cleared x = Bit is unknown

bit 7-2 **Unimplemented:** Read as ‘ `0` ’

bit 1-0 **Resolution bits**

`00` = +0.5°C (t CONV = 30 ms typical)
`01` = +0.25°C (t CONV = 65 ms typical)
`10` = +0.125°C (t CONV = 130 ms typical)
`11` = +0.0625°C (power-up default, t CONV = 250 ms typical)

|REGISTER 5-7: RESOLUTION REGISTER (→ ADDRESS ‘0000 1000’b)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|U-0 U-0 U-0 U-0 U-0 U-0 R/W-1 R/W-1|||||||
|—|—|—|—|—|—|Resolution|
|bit 7 bit 0|||||||


1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

SCL


1 2 3 4 5 6 7 8


A A
SDA S 0 0 1 1 A A A W C 0 0 0 0 1 0 0 0 C 0 0 0 0 0 0 1 1
2 1 0 K K


A
C P
K


Address Byte


Resolution Pointer Data

**MCP9808** **MCP9808**


**MCP9808**

###### *FIGURE 5-8: Timing Diagram for Changing T A Resolution to +0.0625°C <0000 0011>b (see * *Section 4.0 “Serial Communication” ).*

© 2011 Microchip Technology Inc. DS25095A-page 29


-----

## **MCP9808**
##### **5.2 SENSOR FEATURE DESCRIPTION**
###### 5.2.1 SHUTDOWN MODE

Shutdown mode disables all power consuming
activities (including temperature sampling operations)
while leaving the serial interface active. This mode is
selected by setting bit 8 of CONFIG to ‘ `1` ’. In this mode,
the device consumes I SHDN . It remains in this mode
until bit 8 is cleared to ‘ `0` ’ to enable Continuous
Conversion mode or until power is recycled.

The Shutdown bit (bit 8) cannot be set to ‘ `1` ’ while the
CONFIG<7:6> bits (Lock bits) are set to ‘ `1` ’. However, it
can be cleared to ‘ `0` ’ or returned to Continuous

Conversion mode while locked.

In Shutdown mode, all registers can be read or written.
However, the serial bus activity increases the shutdown
current. In addition, if the device is in shutdown while
the Alert pin is asserted, the device will retain the active
state during shutdown. This increases the shutdown
current due to the additional Alert output current. 5.2.2 TEMPERATURE HYSTERESIS (T HYST )

A hysteresis of 0°C, +1.5°C, +3°C or +6°C can be
selected for the T UPPER, T LOWER and T CRIT temperate
boundaries, using bits 10 and 9 of CONFIG. The
hysteresis applies for decreasing temperature only (hot
to cold) or as temperature drifts below the specified
limit.

The Hysteresis bits can not be changed if either of the
Lock bits (CONFIG<7:6) are set to ‘ `1` ’.

The T UPPER, T LOWER and T CRIT boundary conditions
are described graphically in Figure 5-10. 5.2.3 ALERT OUTPUT CONFIGURATION

The Alert output can be enabled by using bit 3 of the
CONFIG register (Alert Output Control bit) and can be
configured as either a comparator output or as an
Interrupt Output mode using bit 0 of CONFIG (Alert
Output Mode bit). The polarity can also be specified as
active-high or active-low using bit 1 of CONFIG (Alert
Polarity bit). This is an open-drain output and requires
a pull-up resistor.

When the ambient temperature increases above the
critical temperature limit, the Alert output is forced to a
comparator output (regardless of CONFIG<0>). When
the temperature drifts below the critical temperature
limit minus hysteresis, the Alert output automatically
returns to the state specified by CONFIG<0> bit.


V DD

Alert Output


**MCP9808**


R PU

###### *FIGURE 5-9: Active-Low Alert Output * *Configuration.*

The status of the Alert output can be read using
CONFIG<4> (Alert Output Status bit). This bit can not
be set to ‘ `1` ’ in Shutdown mode.

Bits 7 and 6 of the CONFIG register can be used to lock
the T UPPER, T LOWER and T CRIT registers. These bits
prevent false triggers at the Alert output due to an
accidental rewrite to these registers.

The Alert output can also be used as a critical temperature output using bit 2 of CONFIG (Alert Output Select
bit). When this feature is selected, the Alert output
becomes a comparator output. In this mode, the
interrupt output configuration (Alert Output Mode bit,
CONFIG<0>) is ignored. 5.2.3.1 Comparator Mode

Comparator mode is selected using bit 0 of CONFIG. In
this mode, the Alert output is asserted as active-high or
active-low, using bit 1 of CONFIG. Figure 5-10 shows
the conditions that toggle the Alert output.

If the device enters Shutdown mode with asserted Alert
output, the output remains asserted during Shutdown
mode. The device must be operating in Continuous
Conversion mode for t CONV . The T A vs. T UPPER,
T LOWER and T CRIT boundary conditions need to be
satisfied in order for the Alert output to deassert.

Comparator mode is useful for thermostat type
applications, such as turning on a cooling fan or
triggering a system shutdown when the temperature
exceeds a safe operating range.


DS25095A-page 30 © 2011 Microchip Technology Inc.


-----

###### 5.2.3.2 Interrupt Mode

In Interrupt mode, the Alert output is asserted as activehigh or active-low (depending on the polarity
configuration) when T A drifts above or below T UPPER
and T LOWER limits. The output is deasserted by setting
bit 5 (Interrupt Clear bit) of CONFIG. Shutting down the
device will not reset or deassert the Alert output. This
mode can not be selected when the Alert output is used
as a critical temperature output only, using bit 2 of
CONFIG.

This mode is designed for interrupt driven
microcontroller-based systems. The microcontroller
receiving the interrupt will have to Acknowledge the
interrupt by setting bit 5 of the CONFIG register from the
MCP9808.

## **MCP9808**
###### 5.2.4 TEMPERATURE RESOLUTION

The MCP9808 is capable of providing temperature
data with +0.5°C to +0.0625°C resolution. The resolu
tion can be selected using the Resolution register
(Register 5-7). It is located at address, ‘ `00001000’b`,
and it provides measurement flexibility. A +0.0625°C
resolution is set as a POR default by the factory. **TABLE 5-2: TEMPERATURE ** **CONVERSION TIME**

|Resolution|t CONV (ms)|Samples/sec (typical)|
|---|---|---|
|+0.5°C|30|33|
|+0.25°C|65|15|
|+0.125°C|130|7|
|+0.0625°C (Power-up Default)|250|4|


© 2011 Microchip Technology Inc. DS25095A-page 31


-----

## **MCP9808**

T CRIT

T UPPER

T A

T LOWER

Comparator

Interrupt

S/w Int. Clear

Critical Only

Comparator

Interrupt

S/w Int. Clear

Critical Only


T UPPER – T HYST

T LOWER – T HYST



**Notes:** **1** **2** **1** **3** **4** **3** **5** **6** **7** **4** **2**

|Notes|Alert Output Boundary Conditions|Comparator|Interrupt|Critical|T Bits A|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||Alert Output (Active-Low/High)|||15|14|13|
|1|T ≥ T A LOWER|High/Low|Low/High|High/Low|0|0|0|
|2|T < T – T A LOWER HYST|Low/High|Low/High|High/Low|0|0|1|
|3|T > T A UPPER|Low/High|Low/High|High/Low|0|1|0|
|4|T ≤ T – T A UPPER HYST|High/Low|Low/High|High/Low|0|0|0|
|5|T ≥ T A CRIT|Low/High|Low/High|Low/High|1|1|0|
|6|When T ≥ T, the Alert output is forced to Comparator mode and the CONFIG<0> (Alert Output A CRIT Mode bit) is ignored until T < T – T . In the Interrupt mode, if the interrupt is not cleared A CRIT HYST (bit 5 of CONFIG), as shown in the diagram at Note 6, then Alert will remain asserted at Note 7 until the interrupt is cleared by the controller.|||||||
|7|T < T – T A CRIT HYST|Low/High|High/Low|High/Low|0|1|0|

###### *FIGURE 5-10: Alert Output Conditions.*

DS25095A-page 32 © 2011 Microchip Technology Inc.


-----

## **MCP9808**
##### **5.3 Summary of Power-on Default**

The MCP9808 has an internal Power-on Reset (POR)
circuit. If the power supply voltage, V DD, glitches below
the V POR threshold, the device resets the registers to
the power-on default settings.

Table 5-3 shows the power-on default summary for the
Temperature Sensor registers.

© 2011 Microchip Technology Inc. DS25095A-page 33

|TABLE 5-3: POWER-ON RESET DEFAULTS|Col2|Col3|Col4|
|---|---|---|---|
|Registers||Default Register Data (Hexadecimal)|Power-Up Default Register Description|
|Address (Hexadecimal)|Register Name|||
|0x01|CONFIG|0x0000|Comparator Mode Active-Low Output Alert and Critical Output Output Disabled Alert Not Asserted Interrupt Cleared Alert Limits Unlocked Critical Limit Unlocked Continuous Conversion 0°C Hysteresis|
|0x02|T UPPER|0x0000|0°C|
|0x03|T LOWER|0x0000|0°C|
|0x04|T CRIT|0x0000|0°C|
|0x05|T A|0x0000|0°C|
|0x06|Manufacturer ID|0x0054|0x0054 (hex)|
|0x07|Device ID/Device Revision|0x0400|0x0400 (hex)|
|0x08|Resolution|0x03|0x03 (hex)|


-----

## **MCP9808**
###### **NOTES:**

DS25095A-page 34 © 2011 Microchip Technology Inc.


-----

#### **6.0 APPLICATIONS INFORMATION**
##### **6.1 Layout Considerations**

The MCP9808 does not require any additional
components besides the master controller in order to
measure temperature. However, it is recommended
that a decoupling capacitor of 0.1 µF to 1 µF be used
between the V DD and GND pins. A high-frequency
ceramic capacitor is recommended. It is necessary for
the capacitor to be located as close as possible to the
power and ground pins of the device in order to provide
effective noise protection.

In addition, good PCB layout is key for better thermal
conduction from the PCB temperature to the sensor
die. For good temperature sensitivity, add a ground
layer under the device pins, as shown in Figure 6-1. **6.2 Thermal Considerations**

A potential for self-heating errors can exist if the
MCP9808 SDA, SCL and Event lines are heavily
loaded with pull-ups (high current). Typically, the
self-heating error is negligible because of the relatively
small current consumption of the MCP9808. A temper###### *FIGURE 6-1: DFN Package Layout (Top View).*

## **MCP9808**

ature accuracy error of approximately +0.5°C could
result from self-heating if the communication pins
sink/source the maximum current specified.

For example, if the event output is loaded to maximum
I OL, Equation 6-1 can be used to determine the effect
of self-heating.
###### **EQUATION 6-1: EFFECT OF ** **SELF-HEATING**

*T* Δ *=* θ *JA VDD* ( - *IDD* *+* *V* *OL_Alert* - *I* *OL_Alert* *+* *VOL_SDA* - *IOL_SDA* )

Where:

T Δ = T J – T A

T J = Junction Temperature

T A = Ambient Temperature

θ JA = Package Thermal Resistance

V OL_Alert, SDA = Alert and SDA Output V OL
(0.4 V max )

I OL_Alert, SDA = Alert and SDA Output I OL
(3 mA max )

At room temperature (T A = +25°C) with maximum
I DD = 500 µA and V DD = 3.6V, the self-heating due to
power dissipation T Δ is +0.2°C for the DFN-8 package
and +0.5°C for the TSSOP-8 package.


© 2011 Microchip Technology Inc. DS25095A-page 35


-----

## **MCP9808**
###### **NOTES:**

DS25095A-page 36 © 2011 Microchip Technology Inc.


-----

## **MCP9808**
#### **7.0 PACKAGING INFORMATION**
##### **7.1 Package Marking Information**
###### 8-Lead DFN (2x3x0.9 mm) Example 8-Lead MSOP (3x3 mm) Example

**Legend:** XX...X Customer-specific information
Y Year code (last digit of calendar year)
YY Year code (last 2 digits of calendar year)
WW Week code (week of January 1 is week ‘01’)
NNN Alphanumeric traceability code e 3 Pb-free JEDEC designator for Matte Tin (Sn)

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|9808E 141256||||
||||| * This package is Pb-free. The Pb-free JEDEC designator ( e 3 )

can be found on the outer packaging for this package.

**Note** : In the event the full Microchip part number cannot be marked on one line, it will
be carried over to the next line, thus limiting the number of available
characters for customer-specific information.

© 2011 Microchip Technology Inc. DS25095A-page 37


-----

## **MCP9808**

##### **����������������������������������������������������������������������**

**�����** ���������������������������������������������������������������������������������������������������
����������������������������������

NOTE 1

**������**

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||


�����������������������������������������������������������������������������������
��������������������������������������������������������

����������������������������
�����������������������������������������������
������������������������������������������������������������������������
����������������������������������������������������������������������������������

����������������������������������


DS25095A-page 38 © 2011 Microchip Technology Inc.


-----

## **MCP9808**


**Note:** For the most current package drawings, please see the Microchip Packaging Specification located at
http://www.microchip.com/packaging


© 2011 Microchip Technology Inc. DS25095A-page 39


-----

## **MCP9808**

##### **������������������������������������������������������**

**�����** ���������������������������������������������������������������������������������������������������
����������������������������������

|D|Col2|Col3|Col4|
|---|---|---|---|
|D N||||
|||||
|||||
|||||



|D|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|D N E E1 TE 1 1 2 e b c A2 L||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||


**������**

�����������������������������������������������������������������������������������
����������������������������������������������������������������������������������������������������������������������������
�����������������������������������������������
������������������������������������������������������������������������
����������������������������������������������������������������������������������

����������������������������������


DS25095A-page 40 © 2011 Microchip Technology Inc.


-----

## **MCP9808**


**Note:** For the most current package drawings, please see the Microchip Packaging Specification located at
http://www.microchip.com/packaging


© 2011 Microchip Technology Inc. DS25095A-page 41


-----

## **MCP9808**
###### **NOTES:**

DS25095A-page 42 © 2011 Microchip Technology Inc.


-----

## **MCP9808**

***Software License Agreement***

The software supplied herewith by Microchip Technology Incorporated (the “Company”) is intended and supplied to you, the
Company’s customer, for use solely and exclusively with products manufactured by the Company.
The software is owned by the Company and/or its supplier, and is protected under applicable copyright laws. All rights are reserved.
Any use in violation of the foregoing restrictions may subject the user to criminal sanctions under applicable laws, as well as to civil
liability for the breach of the terms and conditions of this license.
THIS SOFTWARE IS PROVIDED IN AN “AS IS” CONDITION. NO WARRANTIES, WHETHER EXPRESS, IMPLIED OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE APPLY TO THIS SOFTWARE. THE COMPANY SHALL NOT, IN ANY CIRCUMSTANCES, BE LIABLE FOR
SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES, FOR ANY REASON WHATSOEVER.
#### **APPENDIX A: SOURCE CODE**
```
/********************************************************************
 FileName:   I2C.c
 Processor: PIC18 Microcontrollers
 Complier:  Microchip C18 (for PIC18) or C30 (for PIC24)
 Company: Microchip Technology, Inc.
#include <p18cxxx.h> // This code is developed for PIC18F2550
//It can be modified to be used with any PICmicro with MSSP module
/** PRIVATE PROTOTYPES *********************************************/
void i2c_init(void);
void i2c_start(void);
void i2c_repStart(void);
void i2c_stop(void);
unsigned char i2c_write( unsigned char i2cWriteData );
unsigned char i2c_read( unsigned char ack );
/********************************************************************
*  Function Name: i2c_init
*  Return Value:  void     
*  Parameters:   Enable SSP
*  Description:  This function sets up the SSP1 module on a   
*          PIC18CXXX device for use with a Microchip I2C 
********************************************************************/
void i2c_init(void) {
  TRISBbits.TRISB0 = 1;     // Digital Output (make it input only when reading data)
  TRISBbits.TRISB1 = 1;     // Digital Output
  SSPCON1 = 0x28;        // enable I2C Master mode
  SSPCON2 = 0x00;        // clear control bits
  SSPSTAT = 0x80;        // disable slew rate control; disable SMBus
  SSPADD = 19;         // set baud rate to 100 kHz (Fosc = 48 MHz)
  PIR1bits.SSPIF = 0;
  PIR2bits.BCLIF = 0;
  SSPCON2bits.SEN = 0;     // force idle condition
}

```
© 2011 Microchip Technology Inc. DS25095A-page 45


-----

## **MCP9808**
```
/********************************************************************
*   Function Name:  i2c_start
*   Return Value:   void  
*   Parameters:    void  
*   Description:   Send I2C Start Command
********************************************************************/
void i2c_start(void) {
  PIR1bits.SSPIF = 0; //clear flag
  while (SSPSTATbits.BF );  // wait for idle condition
  SSPCON2bits.SEN = 1;    // initiate START condition
  while (!PIR1bits.SSPIF) ;  // wait for a flag to be set
  PIR1bits.SSPIF = 0; // clear flag
}
/********************************************************************
*   Function Name:  i2c_repStart
*   Return Value:   void   
*   Parameters:    void   
*   Description:   Resend I2C Start Command
*
********************************************************************/
void i2c_repStart(void) {
  PIR1bits.SSPIF = 0; // clear flag
  while ( SSPSTATbits.BF ) ; // wait for idle condition
  SSPCON2bits.RSEN = 1;    // initiate Repeated START condition
  while (!PIR1bits.SSPIF) ; // wait for a flag to be set
  PIR1bits.SSPIF = 0; // clear flag
}
/********************************************************************
*   Function Name:  i2c_stop
*   Return Value:   void 
*   Parameters:    void   
*   Description:   Send I2C Stop command
*
********************************************************************/
void i2c_stop(void) {
  PIR1bits.SSPIF = 0; // clear flag
  while ( SSPSTATbits.BF ) ; // wait for idle condition
  SSPCON2bits.PEN = 1;     // Initiate STOP condition
  while (!PIR1bits.SSPIF) ; // wait for a flag to be set
  PIR1bits.SSPIF = 0; // clear flag
}

```
DS25095A-page 46 © 2011 Microchip Technology Inc.


-----

## **MCP9808**
```
/********************************************************************
*   Function Name:  i2c_write
*   Return Value:   Status byte for WCOL detection.      
*   Parameters:    Single data byte for I2C2 bus.       
*   Description:   This routine writes a single byte to the  
*            I2C2 bus.                 
********************************************************************/
unsigned char i2c_write( unsigned char i2cWriteData ) {
  PIR1bits.SSPIF = 0; // clear interrupt
  while ( SSPSTATbits.BF ) ; // wait for idle condition
  SSPBUF = i2cWriteData;    // Load SSPBUF with i2cWriteData (the value to be transmitted)
  while (!PIR1bits.SSPIF) ; // wait for a flag to be set
  PIR1bits.SSPIF = 0; // clear flag
  return ( !SSPCON2bits.ACKSTAT ); // function returns '1' if transmission is acknowledged
}
/********************************************************************
*   Function Name:  i2c_read
*   Return Value:   contents of SSP2BUF register        
*   Parameters:    ack = 1 and nak = 0            
*   Description:   Read a byte from I2C bus and ACK/NAK device
********************************************************************/
unsigned char i2c_read( unsigned char ack ) {
  unsigned char i2cReadData;
  PIR1bits.SSPIF = 0;// clear interrupt
  while ( SSPSTATbits.BF ) ; // wait for idle condition
  SSPCON2bits.RCEN = 1;    // enable receive mode
  while (!PIR1bits.SSPIF) ; // wait for a flag to be set
  PIR1bits.SSPIF = 0;// clear flag
  i2cReadData = SSPBUF;    // Read SSPBUF and put it in i2cReadData
  if ( ack ) {        // if ack=1
    SSPCON2bits.ACKDT = 0; //  then transmit an Acknowledge
  } else {
    SSPCON2bits.ACKDT = 1; //  otherwise transmit a Not Acknowledge
  }
  SSPCON2bits.ACKEN = 1;   // send acknowledge sequence
  while (!PIR1bits.SSPIF) ; // wait for a flag to be set
  PIR1bits.SSPIF = 0;// clear flag
  return( i2cReadData );   // return the value read from SSPBUF
}

```
© 2011 Microchip Technology Inc. DS25095A-page 47


-----

## **MCP9808**
###### **NOTES:**

DS25095A-page 48 © 2011 Microchip Technology Inc.


-----

## **MCP9808**
#### **APPENDIX B: REVISION HISTORY**
##### **Revision A (October 2011)**

- Original Release of this Document.

© 2011 Microchip Technology Inc. DS25095A-page 49


-----

## **MCP9808**
###### **NOTES:**

DS25095A-page 50 © 2011 Microchip Technology Inc.


-----

## **MCP9808**
#### **PRODUCT IDENTIFICATION SYSTEM**

To order or obtain information, e. g ., on p ricin g or deliver y, refer to the factor y or the listed sales office .

|PART NO. X -X /XX Device Tape and Reel Temperature Package and/or Range Alternate Pinout Device: MCP9808: Digital Temperature Sensor MCP9808T: Digital Temperature Sensor (Tape and Reel) Temperature Range: E = -40°C to +125°C Package: MC = Plastic Dual Flat No-Lead (DFN) 2x3, 8-lead MS = Plastic Micro Small Outline (MSOP), 8-lead|Examples: a) MCP9808-E/MC: Extended Temperature 8LD DFN package. b) MCP9808-E/MS: Extended Temperature 8LD MSOP package. c) MCP9808T-E/MC: Tape and Reel, Extended Temperature 8LD DFN package. d) MCP9808T-E/MS: Tape and Reel, Extended Temperature 8LD MSOP package.|
|---|---|



© 2011 Microchip Technology Inc. DS25095A-page 51


-----

## **MCP9808**
###### **NOTES:**

DS25095A-page 52 © 2011 Microchip Technology Inc.


-----

**Note the following details of the code protection feature on Microchip devices:**

- Microchip products meet the specification contained in their particular Microchip Data Sheet.

- Microchip believes that its family of products is one of the most secure families of its kind on the market today, when used in the
intended manner and under normal conditions.

- There are dishonest and possibly illegal methods used to breach the code protection feature. All of these methods, to our
knowledge, require using the Microchip products in a manner outside the operating specifications contained in Microchip’s Data
Sheets. Most likely, the person doing so is engaged in theft of intellectual property.



- Microchip is willing to work with the customer who is concerned about the integrity of their code.



- Neither Microchip nor any other semiconductor manufacturer can guarantee the security of their code. Code protection does not
mean that we are guaranteeing the product as “unbreakable.”

Code protection is constantly evolving. We at Microchip are committed to continuously improving the code protection features of our
products. Attempts to break Microchip’s code protection feature may be a violation of the Digital Millennium Copyright Act. If such acts
allow unauthorized access to your software or other copyrighted work, you may have a right to sue for relief under that Act.


Information contained in this publication regarding device
applications and the like is provided only for your convenience
and may be superseded by updates. It is your responsibility to
ensure that your application meets with your specifications.
MICROCHIP MAKES NO REPRESENTATIONS OR

WARRANTIES OF ANY KIND WHETHER EXPRESS OR

IMPLIED, WRITTEN OR ORAL, STATUTORY OR
OTHERWISE, RELATED TO THE INFORMATION,
INCLUDING BUT NOT LIMITED TO ITS CONDITION,
QUALITY, PERFORMANCE, MERCHANTABILITY OR
FITNESS FOR PURPOSE **.** Microchip disclaims all liability
arising from this information and its use. Use of Microchip
devices in life support and/or safety applications is entirely at
the buyer’s risk, and the buyer agrees to defend, indemnify and
hold harmless Microchip from any and all damages, claims,
suits, or expenses resulting from such use. No licenses are
conveyed, implicitly or otherwise, under any Microchip
intellectual property rights.


**Trademarks**

The Microchip name and logo, the Microchip logo, dsPIC,
K EE L OQ, K EE L OQ logo, MPLAB, PIC, PICmicro, PICSTART,
PIC [32] logo, rfPIC and UNI/O are registered trademarks of
Microchip Technology Incorporated in the U.S.A. and other
countries.

FilterLab, Hampshire, HI-TECH C, Linear Active Thermistor,
MXDEV, MXLAB, SEEVAL and The Embedded Control
Solutions Company are registered trademarks of Microchip
Technology Incorporated in the U.S.A.

Analog-for-the-Digital Age, Application Maestro, chipKIT,
chipKIT logo, CodeGuard, dsPICDEM, dsPICDEM.net,
dsPICworks, dsSPEAK, ECAN, ECONOMONITOR,
FanSense, HI-TIDE, In-Circuit Serial Programming, ICSP,
Mindi, MiWi, MPASM, MPLAB Certified logo, MPLIB,
MPLINK, mTouch, Omniscient Code Generation, PICC,
PICC-18, PICDEM, PICDEM.net, PICkit, PICtail, REAL ICE,
rfLAB, Select Mode, Total Endurance, TSHARC,
UniWinDriver, WiperLock and ZENA are trademarks of
Microchip Technology Incorporated in the U.S.A. and other
countries.

SQTP is a service mark of Microchip Technology Incorporated
in the U.S.A.

All other trademarks mentioned herein are property of their
respective companies.

© 2011, Microchip Technology Incorporated, Printed in the
U.S.A., All Rights Reserved.

Printed on recycled paper.


ISBN: 978-1-61341-739-3

*Microchip received ISO/TS-16949:2009 certification for its worldwide*
*headquarters, design and wafer fabrication facilities in Chandler and*
*Tempe, Arizona; Gresham, Oregon and design centers in California*
*and India. The Company’s quality system processes and procedures*
*are for its PIC* *[®]* *MCUs and dsPIC* *[®]* *DSCs, K* *EE* *L* *OQ* *[®]* *code hopping*
*devices, Serial EEPROMs, microperipherals, nonvolatile memory and*
*analog products. In addition, Microchip’s quality system for the design*
*and manufacture of development systems is ISO 9001:2000 certified.*

© 2011 Microchip Technology Inc. DS25095A-page 53


-----

### **Worldwide Sales and Service**

###### **AMERICAS**

**Corporate Office**
2355 West Chandler Blvd.

Chandler, AZ 85224-6199

Tel: 480-792-7200

Fax: 480-792-7277

Technical Support:
http://www.microchip.com/
support
Web Address:

[www.microchip.com](http://www.microchip.com)

**Atlanta**
Duluth, GA

Tel: 678-957-9614

Fax: 678-957-1455

**Boston**
Westborough, MA
Tel: 774-760-0087

Fax: 774-760-0088

**Chicago**
Itasca, IL

Tel: 630-285-0071

Fax: 630-285-0075

**Cleveland**
Independence, OH
Tel: 216-447-0464

Fax: 216-447-0643

**Dallas**
Addison, TX

Tel: 972-818-7423

Fax: 972-818-2924

**Detroit**
Farmington Hills, MI
Tel: 248-538-2250

Fax: 248-538-2260

**Indianapolis**
Noblesville, IN

Tel: 317-773-8323

Fax: 317-773-5453

**Los Angeles**
Mission Viejo, CA
Tel: 949-462-9523

Fax: 949-462-9608

**Santa Clara**

Santa Clara, CA

Tel: 408-961-6444

Fax: 408-961-6445

**Toronto**
Mississauga, Ontario,
Canada

Tel: 905-673-0699

Fax: 905-673-6509

###### **ASIA/PACIFIC**

**Asia Pacific Office**

Suites 3707-14, 37th Floor
Tower 6, The Gateway
Harbour City, Kowloon
Hong Kong
Tel: 852-2401-1200

Fax: 852-2401-3431

**Australia - Sydney**
Tel: 61-2-9868-6733

Fax: 61-2-9868-6755

**China - Beijing**
Tel: 86-10-8569-7000

Fax: 86-10-8528-2104

**China - Chengdu**
Tel: 86-28-8665-5511

Fax: 86-28-8665-7889

**China - Chongqing**
Tel: 86-23-8980-9588

Fax: 86-23-8980-9500

**China - Hangzhou**
Tel: 86-571-2819-3187

Fax: 86-571-2819-3189

**China - Hong Kong SAR**
Tel: 852-2401-1200

Fax: 852-2401-3431

**China - Nanjing**
Tel: 86-25-8473-2460

Fax: 86-25-8473-2470

**China - Qingdao**
Tel: 86-532-8502-7355

Fax: 86-532-8502-7205

**China - Shanghai**
Tel: 86-21-5407-5533

Fax: 86-21-5407-5066

**China - Shenyang**
Tel: 86-24-2334-2829

Fax: 86-24-2334-2393

**China - Shenzhen**

Tel: 86-755-8203-2660

Fax: 86-755-8203-1760

**China - Wuhan**

Tel: 86-27-5980-5300

Fax: 86-27-5980-5118

**China - Xian**

Tel: 86-29-8833-7252

Fax: 86-29-8833-7256

**China - Xiamen**

Tel: 86-592-2388138

Fax: 86-592-2388130

**China - Zhuhai**

Tel: 86-756-3210040

Fax: 86-756-3210049

###### **ASIA/PACIFIC**

**India - Bangalore**
Tel: 91-80-3090-4444

Fax: 91-80-3090-4123

**India - New Delhi**

Tel: 91-11-4160-8631

Fax: 91-11-4160-8632

**India - Pune**

Tel: 91-20-2566-1512

Fax: 91-20-2566-1513

**Japan - Yokohama**
Tel: 81-45-471- 6166

Fax: 81-45-471-6122

**Korea - Daegu**
Tel: 82-53-744-4301

Fax: 82-53-744-4302

**Korea - Seoul**

Tel: 82-2-554-7200

Fax: 82-2-558-5932 or

82-2-558-5934

**Malaysia - Kuala Lumpur**
Tel: 60-3-6201-9857

Fax: 60-3-6201-9859

**Malaysia - Penang**
Tel: 60-4-227-8870

Fax: 60-4-227-4068

**Philippines - Manila**
Tel: 63-2-634-9065

Fax: 63-2-634-9069

**Singapore**
Tel: 65-6334-8870

Fax: 65-6334-8850

**Taiwan - Hsin Chu**

Tel: 886-3-5778-366

Fax: 886-3-5770-955

**Taiwan - Kaohsiung**
Tel: 886-7-536-4818

Fax: 886-7-330-9305

**Taiwan - Taipei**
Tel: 886-2-2500-6610

Fax: 886-2-2508-0102

**Thailand - Bangkok**
Tel: 66-2-694-1351

Fax: 66-2-694-1350

###### **EUROPE**

**Austria - Wels**

Tel: 43-7242-2244-39

Fax: 43-7242-2244-393

**Denmark - Copenhagen**
Tel: 45-4450-2828

Fax: 45-4485-2829

**France - Paris**

Tel: 33-1-69-53-63-20

Fax: 33-1-69-30-90-79

**Germany - Munich**
Tel: 49-89-627-144-0

Fax: 49-89-627-144-44

**Italy - Milan**
Tel: 39-0331-742611

Fax: 39-0331-466781

**Netherlands - Drunen**

Tel: 31-416-690399

Fax: 31-416-690340

**Spain - Madrid**
Tel: 34-91-708-08-90

Fax: 34-91-708-08-91

**UK - Wokingham**
Tel: 44-118-921-5869

Fax: 44-118-921-5820

08/02/11


DS25095A-page 54 © 2011 Microchip Technology Inc.


-----

