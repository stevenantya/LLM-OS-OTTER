**Product status link**

# **VL53L0X**
### Datasheet
## Time-of-Flight ranging sensor
### **Features**

**Fully integrated miniature module**

- 940 nm laser VCSEL (vertical-cavity surface-emitting laser)

- VCSEL driver

- Ranging sensor with advanced embedded microcontroller

- 4.4 x 2.4 x 1.0 mm

**Fast, accurate distance ranging**

- Measures absolute range up to 2 m

- The reported range is independent of the target reflectance

- Advanced embedded optical crosstalk compensation to simplify cover glass
selection

**Eye safety**

- Class 1 laser device compliant with latest standard IEC 60825-1:2014 - 3rd
edition

**Easy integration**

- Single reflowable component

- No additional optics

- Single power supply

- I²C interface for device control and data transfer

- Xshutdown (reset) and interrupt GPIO

- Programmable I²C address **Application**

- Access control (system activation and presence detection)

- Robotics (collision avoidance, wall tracking, and cliff detection)

- Home appliance and home automation

- Inventory management and liquid level monitoring **Description**

The VL53L0X is a Time-of-Flight (ToF) laser-ranging module housed in the smallest
package on the market today, providing accurate distance measurement whatever
the target reflectance, unlike conventional technologies. It can measure absolute
distances up to 2 m, setting a new benchmark in ranging performance levels,
opening the door to various new applications.

The VL53L0X integrates a leading-edge SPAD array (single photon avalanche
diodes) and embeds ST’s second generation FlightSense patented technology.

The VL53L0X’s 940 nm VCSEL emitter (vertical cavity surface-emitting laser), is
totally invisible to the human eye, coupled with internal physical infrared filters, it
enables longer ranging distances, higher immunity to ambient light, and better
robustness to cover glass optical crosstalk.


[VL53L0X](https://www.st.com/en/imaging-and-photonics-solutions/vl53l0x)


**DS11555** - **Rev 6** - **June 2024**
For further information contact your local STMicroelectronics sales office.


www.st.com


-----

### **VL53L0X**

**Acronyms and abbreviations**
## **1 Acronyms and abbreviations**

**Table 1. Acronymas and abbreviations**

|Acronym/abbreviation|Definition|
|---|---|
|API|application programming interface|
|cal|calibration|
|ESD|electrostatic discharge|
|FoV|field of view|
|FW BOOT|firmware boot|
|HW STANDBY|hardware standby|
|I²C|inter-integrated circuit (serial bus)|
|MSB|most significant bit|
|NVM|non-volatile memory|
|PCB|printed circuit board|
|PVT|power, voltage, and temperature|
|RIT|return ignore threshold|
|SCL|serial clock line|
|SDA|serial data line|
|SW STANDBY|software standby|
|SPAD|single photon avalanche diode|
|ToF|Time-of-Flight|
|VCSEL|vertical-cavity surface-emitting laser|
|VHV|very high voltage|



**DS11555** - **Rev 6** **page 2/38**


-----

### **VL53L0X**

**Overview**

## **2 Overview**
### **2.1 Technical specification**

|Feature|Detail|
|---|---|
|Package|Optical LGA12|
|Size|4.4 x 2.4 x 1 mm|
|Operating voltage|2.6 to 3.5 V|
|Operating temperature|-20 to 70°C|
|Infrared emitter|940 nm|
|I²C|Up to 400 kHz (fast mode) serial bus Address: 0x52| **2.2 System block diagram**
##### GND SDA

##### AVDD XSHUT


**Table 2. Technical specification**

**Figure 1. VL53L0X block diagram**


|Col1|VL53L0X module VL53L0X silicon Detection array Single Photon Avalanche Diode (SPAD) ROM Non Volatile Memory RAM Microcontroller Advanced Ranging Core VCSEL Driver IR+ IR- 940nm|Col3|
|---|---|---|


**DS11555** - **Rev 6** **page 3/38**


-----

### **VL53L0X**

**Overview**

### **2.3 Device pinout**

The following figure shows the pinout of the VL53L0X (see also Section 7: Outline drawings).

**Figure 2. VL53L0X pinout (bottom view)**
##### GND3

##### DNC 8 SDA 9 GND4

##### 5 XSHUT 4 GND2 3 GND 2 AVSSVCSEL 1 AVDDVCSEL


**Table 3. VL53L0X pin description**

|Pin number|Signal name|Signal type|Signal description|
|---|---|---|---|
|1|AVDDVCSEL|Supply|VCSEL supply, to be connected to main supply|
|2|AVSSVCSEL|Ground|VCSEL ground, to be connected to main ground|
|3|GND||To be connected to the main ground|
|4|GND2|||
|5|XSHUT|Digital input|Xshutdown pin, active low|
|6|GND3|Ground|To be connected to the main ground|
|7|GPIO1|Digital output|Interrupt output. Open drain output|
|8|DNC|Digital input|Do not connect, must be left floating|
|9|SDA|Digital input/output|I²C serial data|
|10|SCL|Digital input|I²C serial clock input|
|11|AVDD|Supply|Supply, to be connected to the main supply|
|12|GND4|Ground|To be connected to the main ground|



*Note:* *AVSSVCSEL and GND are ground pins that can be connected in the application schematics.*

*Note:* *GND2, GND3, and GND4 are standard pins that are forced to the ground domain in the application schematics.*
*This is to avoid possible instabilities, which might arise if set in other states.*

**DS11555** - **Rev 6** **page 4/38**


-----

### **2.4 Application schematic**

The following figure shows the application schematic of the VL53L0X.

**Figure 3. VL53L0X schematic**
##### IOVDD 5 7 HOST 9 10 8

### **VL53L0X**

**Overview**


*Note:* *Capacitors on the external supply AVDD should be placed as close as possible to the AVDDVCSEL and*
*AVSSVCSEL module pins.*

*Note:* *The external pull-up resistor values can be found in the I²C-bus specification. Pull-ups are typically fitted only*
*once per bus, near the host. Recommended values for pull-up resistors for an AVDD of 2.8 V and a 400 kHz I²C*
*clock are 1.5 k to 2 kOhms*

*Note:* *The XSHUT pin must always be driven to avoid leakage current. A pull-up is needed if the host state is not*
*known. XSHUT is needed to use hardware standby mode (there is no I²C communication).*

*Note:* *The recommended value of the XSHUT and GPIO1 pull-ups is 10 kOhms.*

*Note:* *The GPIO1 should be left unconnected if not used.*


**DS11555** - **Rev 6** **page 5/38**


-----

### **VL53L0X**

**Functional description**
## **3 Functional description**
### **3.1 System functional description**

Figure 4. VL53L0X system functional description shows the system level functional description. The host
customer application controls the VL53L0X device using an API (application programming interface).

The API exposes to the customer application a set of high level functions that allow control of the VL53L0X
firmware (FW). Functions include initialization/calibration, ranging start/stop, choice of accuracy, and choice of
ranging mode.

The API is a turnkey solution. It consists of a set of C functions which enables fast development of end user
applications, without the complication of direct multiple register access. The API is structured in a way that it can
be compiled on any kind of platform through a well isolated platform layer.

The API package allows the user to fully benefit from the VL53L0X capabilities.

A detailed description of the API is available in the VL53L0X API user manual (UM2039).

VL53L0X FW fully manages the hardware (HW) register accesses.

Section 3.2: Firmware state machine description details the firmware state machine.

**Figure 4. VL53L0X system functional description**


**DS11555** - **Rev 6** **page 6/38**


-----

### **VL53L0X**

**Functional description** **3.2 Firmware state machine description**

The following figure shows the device state machine.

**Figure 5. Firmware state machine**


**DS11555** - **Rev 6** **page 7/38**


-----

### **VL53L0X**

**Functional description** **3.3 Customer manufacturing calibration flow**

Figure 6. Customer manufacturing calibration flow shows the recommended calibration flow that should be
applied at customer and factory level, once only. This flow takes into account all parameters (cover glass,
temperature, and voltage) from the application.

**Figure 6. Customer manufacturing calibration flow**


**DS11555** - **Rev 6** **page 8/38**


-----

### **VL53L0X**

**Functional description**
##### **3.3.1 SPAD and temperature calibration**

To optimize the dynamics of the system, the reference SPADs have to be calibrated. Reference SPAD calibration
needs to be done only once during the initial manufacturing calibration. The calibration data should then be stored
on the host.

Temperature calibration is the calibration of two parameters (VHV and phase cal) which are temperature
dependent. These two parameters are used to set the device sensitivity. Calibration should be performed during
initial manufacturing calibration. It must be performed again when the temperature varies more than 8°C
compared to the initial calibration temperature.

For more details on SPAD and temperature calibration, refer to the VL53L0X API user manual (UM2039). **3.3.2 Ranging offset calibration**

Ranging offset is characterized by the mean offset, which is the centering of the measurement versus the real
distance.

Offset calibration should be performed at the factory for optimal performance. It is recommended at 10 cm. The
offset calibration should consider:

         - The supply voltage and temperature.

         - The protective cover glass above the VL53L0X module.

**Figure 7. Range offset** **3.3.3 Crosstalk calibration**

Crosstalk is defined as the signal return from the cover glass. The magnitude of the crosstalk depends on the type
of glass and air gap. Crosstalk results in a range error. This is proportional to the ratio of the crosstalk to the
signal return from the target.

**Figure 8. Crosstalk compensation**

The full offset and crosstalk calibration procedures are described in the VL53L0X API user manual (UM2039).


**DS11555** - **Rev 6** **page 9/38**


-----

### **VL53L0X**

**Functional description** **3.4 Ranging operating modes**

There are three ranging modes available in the API:

1. Single ranging

Ranging is performed only once after the API function is called. The system returns to SW standby
automatically.

2. Continuous ranging.

Ranging is performed in a continuous way after the API function is called. As soon as the measurement is
finished, another one is started without delay. The user has to stop the ranging to return to SW standby. The
last measurement is completed before stopping.

3. Timed ranging.

Ranging is performed in a continuous way after the API function is called. When a measurement is finished,
another one is started after a user-defined delay. This delay (intermeasurement period) can be defined
through the API.

The user has to stop the ranging to return to SW standby.

If the stop request comes during a range measurement, the measurement is completed before stopping. If it
happens during an intermeasurement period, the range measurement stops immediately. **3.5 Ranging profiles**

There are four different ranging profiles available via the API example code. Customers can create their own
ranging profile dependent on their use case and performance requirements. For more details, refer to the
VL53L0X API user manual (UM2039).

         - Default mode

         - High speed

         - High accuracy

         - Long range **3.6 Ranging profile phases**

Each range profile consists of three consecutive phases:

         - Initialization and load calibration data

         - Ranging

         - Digital housekeeping

**DS11555** - **Rev 6** **page 10/38**


-----

### **VL53L0X**

**Functional description**

**Figure 9. Typical initialization/ranging/housekeeping phases**
##### **3.6.1 Initialization and load calibration data phase**

The initialization and calibration phase is performed before the first ranging, or after a device reset (see
Figure 9. Typical initialization/ranging/housekeeping phases). The user may then have to repeat the temperature
calibration phase in a periodic way, depending on the use case.

For more details on the calibration functions, refer to the VL53L0X API user manual (UM2039). **3.6.2 Ranging phase**

The ranging phase consists of a range setup, and then a range measurement.

During the ranging operation, several VCSEL infrared pulses are emitted. They are hen reflected back by the
target object, and detected by the receiving array. The photo detector used inside VL53L0X uses advanced
ultrafast SPAD technology, which is protected by several patents.

The typical timing budget for a range is 33 ms using init/ranging/housekeeping (see Figure 12. Ranging
sequence). The actual range measurement takes 23 ms (see Figure 9. Typical initialization/ranging/housekeeping
phases). The minimum range measurement period is 8 ms.

**DS11555** - **Rev 6** **page 11/38**


-----

### **VL53L0X**

**Functional description**
##### **3.6.3 Digital housekeeping**

Digital processing (housekeeping) is the last operation inside the ranging sequence that computes, validates, or
rejects a ranging measurement. Part of this processing is performed internally while the other part is executed on
the host by the API.

At the end of the digital processing, the ranging distance is computed by VL53L0X itself. If the distance cannot be
measured (for example, a weak signal, or no target), a corresponding error code is provided.

The following functions are performed on the device itself:

         - Signal value check (weak signal)

         - Offset correction

         - Crosstalk correction (in case of cover glass)

         - Final ranging value computation

The above functions are performed while the API performs the following:

         - RIT check (signal check versus crosstalk)

         - Sigma check (accuracy condition)

         - Final ranging state computation

If the user wants to enhance the ranging accuracy, some extra processing (which is not part of the API) can be
carried out by the host. For example, rolling average, hysteresis or any kind of filtering.
### **3.7 Getting the data: Interrupt or polling**

The user can get the final data using a polling or an interrupt mechanism.

**Polling mode**

The user has to check the status of the ongoing measurement by polling an API function.

**Interrupt mode**

An interrupt pin (GPIO1) sends an interrupt to the host when a new measurement is available.

The description of these two modes is available in the VL53L0X API user manual (UM2039). **3.8 Device programming and control**

The I²C is the physical control interface of the device. It is described in Section 4: Control interface.

A software layer (API) is also provided to control the device. The API is described in the VL53L0X API user
manual (UM2039).

**DS11555** - **Rev 6** **page 12/38**


-----

### **VL53L0X**

**Functional description** **3.9 Power sequence**

There are two options available for device power-up and boot sequence.

*Note:* *In all cases, XSHUT is raised only when AVDD is tied on.*

**Option 1**

The XSHUT pin is connected and controlled from the host.

This option optimizes power consumption. The device can be completely powered off when not used, and then
woken up through the host (using the XSHUT pin).

Hardware standby mode is the period when the AVDD is present and the XSHUT is low.

**Figure 10. Power-up and boot sequence**

*Note:* *t* *BOOT* *is 1.2 ms maximum.*

**Option 2**

The host does not control the XSHUT pin. This pin is tied to AVDD through a pull-up resistor.

When the XSHUT pin is not controlled, the power-up sequence is as shown in the following figure. In this case,
the device goes automatically to software standby after a firmware boot, without entering hardware standby.

**Figure 11. Power-up and boot sequence with XSHUT not controlled**

*Note:* *t* *BOOT* *is 1.2 ms maximum.*


**DS11555** - **Rev 6** **page 13/38**


-----

### **VL53L0X**

**Functional description** **3.10 Ranging sequence**

**Figure 12. Ranging sequence**

*Note:* *The t* *timing_budget* *is a parameter set by the user, using a dedicated driver function. The default value is 33 ms.*


**DS11555** - **Rev 6** **page 14/38**


-----

### **VL53L0X**

**Control interface**
## **4 Control interface**

This section specifies the control interface. The I²C interface uses two signals: serial data line (SDA) and serial
clock line (SCL). Each device connected to the bus uses a unique address and a simple controller/target
relationship exists.

Both SDA and SCL lines are connected to a positive supply voltage using pull-up resistors located on the host.
Lines are only actively driven low. A high condition occurs when lines are floating and the pull-up resistors pull
lines up. When no data is transmitted both lines are high.

Clock signal generation is performed by the controller device. The controller device initiates data transfer. The I²C
bus has a maximum speed of 400 kbits/s and uses a default device address of 0x52.

**Figure 13. Data transfer protocol**


Start condition


Acknowledge


SDA

SCL


Address or data byte

|Col1|Col2|
|---|---|
|||
|P||


|MSB LSB 1 2 3 4 5 6 7 8|Col2|Col3|Col4|
|---|---|---|---|
|||c/Am||
||A|||


Stop condition

|Col1|Col2|
|---|---|
|||
||S|


Information is packed in 8-bit packets (bytes) and is always followed by an acknowledge bit, Ac for the VL53L0X
acknowledge and Am for the controller acknowledge (host bus controller). The internal data are produced by
sampling SDA at a rising edge of SCL. The external data must be stable during the high period of SCL. The
exceptions to this are start (S) or stop (P) conditions when SDA falls or rises respectively, while SCL is high.

A message contains a series of bytes preceded by a start condition, and followed by either a stop or repeated
start (another start condition but without a preceding stop condition), followed by another message. The first byte
contains the device address (0x52) and also specifies the data direction. If the least significant bit is low (that is,
0x52) the message is a controller write-to-the-target. If the LSB is set (that is, 0x53) then the message is a
controller read-from-the-target.

**Figure 14. I²C device address: 0x52**

MSBit LSBit

|0|1|0|1|0|0|1|R/W|
|---|---|---|---|---|---|---|---|



All serial interface communications with the Time-of-Flight sensor must begin with a start condition. The VL53L0X
module acknowledges the receipt of a valid address by driving the SDA wire low. The state of the read/write bit
(LSB of the address byte) is stored and the next byte of data, sampled from SDA, can be interpreted. During a
write sequence, the second byte received provides an 8-bit index, which points to one of the internal 8-bit
registers.


**DS11555** - **Rev 6** **page 15/38**


-----

### **VL53L0X**

**Control interface**

**Figure 15. Data format (write)**

As data are received by the target, they are written bit by bit to a serial/parallel register. After each data byte has
been received by the target, an acknowledge is generated, the data are then stored in the internal register
addressed by the current index.

During a read message, the contents of the register addressed by the current index is read out in the byte
following the device address byte. The contents of this register are parallel loaded into the serial/parallel register
and clocked out of the device by the falling edge of SCL.

**Figure 16. Data format (read)**

At the end of each byte, in both read and write message sequences, an acknowledge is issued by the receiving
device (that is, the VL53L0X for a write, and the host for a read).

A message can only be terminated by the bus controller, either by issuing a stop condition or by a negative
acknowledge (that is, not pulling the SDA line low) after reading a complete byte during a read operation.

The interface also supports auto increment indexing. After the first data byte has been transferred, the index is
automatically incremented by 1. The controller can therefore send data bytes continuously to the target until the
target fails to provide an acknowledge, or the controller terminates the write communication with a stop condition.
If the auto increment feature is used, the controller does not have to send address indexes to accompany the data
bytes.

**Figure 17. Data format (sequential write)**

**DS11555** - **Rev 6** **page 16/38**


-----

### **VL53L0X**

**Control interface**

**Figure 18. Data format (sequential read)** **4.1 I²C interface - timing characteristics**

Timing characteristics are shown in the following table. Refer to Figure 19. I²C timing characteristics for an
explanation of the parameters used.

Timings are given for all PVT conditions.

**Table 4. I²C interface - timing characteristics**

|Symbol|Parameter|Minimum|Typical|Maximum|Unit|
|---|---|---|---|---|---|
|F I2C|Operating frequency (standard and fast mode)|0|—|400 (1)|kHz|
|t LOW|Clock pulse width low|1.6|—|—|μs|
|t HIGH|Clock pulse width high|0.6|—|—||
|t SP|Pulse width of spikes that are suppressed by the input filter|—|—|50|ns|
|t BUF|Bus free time between transmissions|1.3|—|—|ms|
|t HD.STA|Start hold time|0.26|—|—|μs|
|t SU.STA|Start setup time|0.26|—|—||
|t HD.DAT|Data in hold time|0|—|0.9||
|t SU.DAT|Data in setup time|50|—|—|ns|
|t R|SCL/SDA rise time|—|—|120||
|t F|SCL/SDA fall time|—|—|120||
|t SU.STO|Stop setup time|0.6|—|—|μs|
|Ci/o|Input/output capacitance (SDA)|—|—|10|pF|
|Cin|Input capacitance (SCL)|—|—|4||
|C L|Load capacitance|—|125|400||



*1.* *The maximum bus speed is also limited by the combination of a 400 pF load capacitance and a pull-up resistor. Refer to the*
*I²C specification for further information*

**DS11555** - **Rev 6** **page 17/38**


-----

### **VL53L0X**

**Control interface**


**Figure 19. I²C timing characteristics**

***stop*** ***start*** ***start*** ***stop***


**SDA**

**SCL**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|VIH ... VIL|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|tBUF||tLOW tR|||tF|||||tHD.STA|||
|VIH VIL||||||||...|||||
||||||||||||||


t HD.STA


t HD.DAT t HIGH t SU.DAT t SU.STA t SU.STO

IL [ or V] IH [.]


All timings are measured from either V IL or V IH .
### **4.2 I²C interface - reference registers**

The registers shown in the table below can be used to validate the user I²C interface.

**Table 5. Reference registers**

|Address|After fresh reset, without the API loaded|
|---|---|
|0xC0|0xEE|
|0xC1|0xAA|
|0xC2|0x10|
|0X51|0x0099|
|0x61|0x0000|



*Note:* *The I²C read/writes can be 8, 16, or 32-bit. Multibyte read/writes are always addressed in ascending order with*
*the MSB first as shown in the following table.*

**Table 6. 32-bit register example**

|Register address|Byte|
|---|---|
|Address|MSB|
|Address + 1|...|
|Address + 2|...|
|Address + 3|LSB|



**DS11555** - **Rev 6** **page 18/38**


-----

### **VL53L0X**

**Electrical characteristics**
## **5 Electrical characteristics**
### **5.1 Absolute maximum ratings**

**Warning:** *Stresses above those listed in the following table may cause permanent damage to the*
*device. These are stress ratings only. Functional operation of the device is not implied at*
*these or any other conditions above those indicated in the operational sections of the*
*specification. Exposure to absolute maximum rating conditions for extended periods may*
*affect device reliability.*

|Col1|Table 7. Absolute|maximum ratings|Col4|Col5|
|---|---|---|---|---|
|Parameter|Min.|Typ.|Max.|Unit|
|AVDD|-0.5|—|3.6|V|
|SCL, SDA, XSHUT, and GPIO1||||| **5.2 Recommended operating conditions**

There are no power supply sequencing requirements. The I/Os may be high, low, or floating when AVDD is
applied. The I/Os are internally failsafe with no diode connecting them to AVDD.

**Table 8. Recommended operating conditions**

*1.* *XSHUT should be high only when AVDD is on.*

*2.* *SDA, SCL, XSHUT, and GPIO1 high levels have to be equal to AVDD in 2V8 mode.*

*3.* *The default API mode is 1V8. 2V8 mode is programmable using the device settings loaded by the API. For more details*
*refer to the VL53L0X API user manual (UM2039).*

|Parameter|Col2|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|
|Voltage (AVDD)||2.6|2.8|3.5|V|
|IO (IOVDD) (1)|Standard mode|1.6|1.8|1.9||
||2V8 mode (2) (3)|2.6|2.8|3.5||
|Normal operating temperature||-20|—|70|°C| **5.3 Electrostatic discharge**

The VL53L0X is compliant with the ESD values presented in the following table.

|Col1|Table 9. ESD performances|Col3|
|---|---|---|
|Parameter|Specification|Conditions|
|Human body model|JS-001-2012|± 2 kV, 1500 ohms, 100 pF|
|Charged device model|JESD22-C101|± 500 V|



**DS11555** - **Rev 6** **page 19/38**


-----

### **VL53L0X**

**Electrical characteristics** **5.4 Current consumption**

**Table 10. Consumption at ambient temperature**

All current consumption values include silicon process variations. Temperature and voltage are nominal conditions (23°C and
2.8 V ) . All values include AVDD and AVDDVCSEL.

*1.* *In standard mode (1V8), pull-ups have to be modified. Then the SW STANDBY consumption is increased by 0.6 µA.*

*2.* *Active ranging is an average value, measured using the default API settings (33 ms timing budget).*

*3.* *Peak current (including VCSEL) can reach 40 mA.*

|Parameter|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|
|HW STANDBY|3|5|7|μA|
|SW STANDBY (2V8 mode) (1)|4|6|9||
|Timed ranging intermeasurement|—|16|—||
|Active ranging average consumption (including VCSEL) (2) (3)|—|19|—|mA|
|Average power consumption at 10 Hz with 33 ms ranging sequence|—|—|20|| **5.5 Digital input and output**

**Table 11. Digital I/O electrical characteristics**

*1.* *AVDD = 0 V*

*2.* *AVDD = 2.85 V, and I/O voltage = 1.8 V*

|Symbol|Parameter|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|
|Interrupt pin (GPIO1)||||||
|VIL|Low level input voltage|—|—|0.3 IOVDD|V|
|VIH|High level input voltage|0.7 IOVDD||—||
|VOL|Low level output voltage (IOUT = 4 mA)|—||0.4||
|VOH|High level output voltage (IOUT = 4 mA)|IOVDD-0.4||—||
|FGPIO|Operating frequency (CLOAD = 20 pF)|0||108|MHz|
|I²C interface (SDA/SCL)||||||
|VIL|Low level input voltage|-0.5|—|0.6|V|
|VIH|High level input voltage|1.12||3.5||
|VOL|Low level output voltage (IOUT = 4 mA in standard and fast modes)|—||0.4||
|IIL/IH|Leakage current (1)|—||10|μA|
||Leakage current (2)|—||0.15||



**DS11555** - **Rev 6** **page 20/38**


-----

### **VL53L0X**

**Performance**
## **6 Performance**
### **6.1 Measurement conditions**

In all the measurement tables of this document, it is considered that the full FoV is covered.

The VL53L0X system FoV is 25°.

Reflectance targets are standard ones (gray 17% N4.74 and White 88% N9.5 Munsell charts).

Unless mentioned, the device is controlled through the API using the default settings. Refer to the VL53L0X API
user manual (UM2039) for API setting descriptions.

**Figure 20. Typical ranging (default mode)**

**DS11555** - **Rev 6** **page 21/38**


-----

### **VL53L0X**

**Performance**

**Figure 21. Typical ranging - long range mode**

**DS11555** - **Rev 6** **page 22/38**


-----

### **VL53L0X**

**Performance** **6.2 Maximum ranging distance**

The table below shows the ranging specification for the VL53L0X bare module. This is without a cover glass, at
room temperature (23°C), and with nominal voltage (2.8 V).

**Table 12. Maximum ranging capabilities with a 33 ms timing budget**

*1.* *Indoor corresponds to no infrared. Outdoor overcast corresponds to a parasitic noise of 10 kcps/SPAD for the VL53L0X*

|Target reflectance level, full FoV|Conditions|Indoor (1)|Outdoor (1)|
|---|---|---|---|
|White target (88%)|Typical|200 cm+ (2)|80 cm|
||Minimum|120 cm|60 cm|
|Gray target (17%)|Typical|80 cm|50 cm|
||Minimum|70 cm|40 cm|

*module. For reference, this corresponds to a 1.2 W/m² at 940 nm, and is equivalent to 5 klx daylight, while ranging on a gray*
*17% chart at 40 cm.*

*2.* *Using a long range API profile.*

**Measurement conditions**

         - Target reflectance used: Gray (17%), White (88%)

         - Nominal voltage (2.8 V) and temperature (23°C)

         - All distances are for a complete FoV covered (FoV = 25°)

All distances mentioned in the above table are guaranteed for a minimum detection rate of 94% (up to 100%).
The detection rate is the worst case percentage of measurements that return a valid measurement when the
target is detected. **6.3 Ranging accuracy**
##### **6.3.1 Standard deviation**

The ranging accuracy can be characterized by the standard deviation. It includes measure-to-measure and partto-part (silicon) dispersion.

**Table 13. Ranging accuracy**

**Measurement conditions**

         - Target reflectance used: Gray (17%), White (88%)

         - Offset correction done at 10 cm from sensor

         - Indoor: No infrared

         - Outdoor: 5 klx equivalent sunlight (10 kcps/SPAD)

         - Nominal voltage (2.8 V) and temperature (23°C)

         - All distances are for a complete FoV covered (FoV = 25°)

         - Detection rate is considered at 94% minimum

|Target reflectance level, full FoV|Indoor (no infrared)|Col3|Col4|Outdoor|Col6|Col7|
|---|---|---|---|---|---|---|
||Distance|33 ms|66 ms|Distance|33 ms|66 ms|
|White target (88%)|At 120 cm|4%|3%|At 60 cm|7%|6%|
|Gray target (17%)|At 70 cm|7%|6%|At 40 cm|12%|9%|


**DS11555** - **Rev 6** **page 23/38**


-----

### **VL53L0X**

**Performance**
##### **6.3.2 Range profile examples**

The following table shows the typical performance for the four example ranging profiles, as per
Section 6.1: Measurement conditions.

**Table 14. Range profiles**

|Range profile|Range timing budget|Typical performance|Typical application|
|---|---|---|---|
|Default mode|30 ms|1.2 m, accuracy as per Table 13. Ranging accuracy|Standard|
|High accuracy|200 ms|1.2 m, accuracy < ±3%|Precise measurement|
|Long range|33 ms|1.2 m, accuracy as per Table 13. Ranging accuracy|Long ranging, only for dark conditions (no IR)|
|High speed|20 ms|1.2 m, accuracy ±5%|High speed where accuracy is not a priority| **6.3.3 Ranging offset error**

The table below shows how range offset may drift over distance, voltage, and temperature. We assumes that the
offset has been calibrated at 10 cm. See the VL53L0X API user manual (UM2039) for details on offset calibration.

**Table 15. Range profiles**

|Col1|Nominal conditions|Measure point|Typical offset from nominal|Maximum offset from nominal|
|---|---|---|---|---|
|Ranging distance|Offset calibration at 10 cm (“zero”)|White 120 cm (indoor) Gray 70 cm (indoor) White 60 cm (outdoor) Gray 40 cm (outdoor)|—|<3%|
|Voltage drift|2.8 V|2.6 V to 3.5 V|±10 mm|±15 mm|
|Temperature drift|23°C|-20°C to 70°C|±10 mm|±30 mm|



**DS11555** - **Rev 6** **page 24/38**


-----

### **VL53L0X**

**Outline drawings**

## **7 Outline drawings**


**Figure 22. Outline drawing (1/3)**

|sition   rface Fin|ameter sition|
|---|---|
|||
|||

|Col1|Col2|0.80|
|---|---|---|
|||0.50|
||||
|0.80|0.50||

|12|11|10|9|8|7|6|5|4|3|2|1|PAD No.|CONNECTION TABLE|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|GND4|AVDD|SCL|SDA|DNC|GPIO1|GND3|XSHUT|GND2|GND|AVSSVCSEL|AVDDVCSEL|FUNCTION||

|2|1|REV.|REVISION TABLE|Col5|
|---|---|---|---|---|
|DRAWING TITLE UPDATE|INITIAL RELEASE|DESCRIPTION|||
|04/05/2016|05/02/2016|DATE|||


**DS11555** - **Rev 6** **page 25/38**


-----

### **VL53L0X**

**Outline drawings**

**Figure 23. Outline drawing (2/3)**

|sition  rface Fin|ameter sition|
|---|---|
|||
|||



**DS11555** - **Rev 6** **page 26/38**


-----

### **VL53L0X**

**Outline drawings**

**Figure 24. Outline drawing - option with liner (3/3)**

|Col1|2.92|Col3|Col4|
|---|---|---|---|
|||||
|0.046 R0.20 1.05 IN 4 POS. PROTECTIVE LINER||||



**DS11555** - **Rev 6** **page 27/38**


-----

### **VL53L0X**

**Laser safety**
## **8 Laser safety**

This product contains a laser emitter and corresponding drive circuitry. The laser output is designed to meet
Class 1 laser safety limits under all reasonably foreseeable conditions including single faults in compliance with
IEC 60825-1:2014.

Do not increase the laser output power by any means. Do not use any optics to focus the laser beam.

**Caution:** Use of controls or adjustments, or performance of procedures other than those specified herein may result in
hazardous radiation exposure.

**Figure 25. Class 1 laser label**

This product complies with:

         - IEC 60825-1:2014

         - 21 CFR 1040.10 and 1040.11, except for conformance with IEC 60825-1:2014 as described in the laser
notice number 56, dated May 8, 2019.

         - EN 60825-1:2014 including EN 60825-1:2014/A11:2021

         - EN 50689:2021, however STMicroelectronics does not guarantee compliance with the requirement of
clause 5 from EN50689 regarding child appealing products. If designing a child appealing product, contact
STMicroelectronics' technical application support.


**DS11555** - **Rev 6** **page 28/38**


-----

### **VL53L0X**

**Packaging and labeling**
## **9 Packaging and labeling**
### **9.1 Product marking**

A two line product marking is applied on the backside of the module (on the substrate). The first line is the silicon
product code, and the second line, the internal tracking code. **9.2 Inner box labeling**

The labeling follows the STMicroelectronics' standard packing acceptance specification.

The following information is on the inner box label:

         - Assembly site

         - Sales type

         - Quantity

         - Trace code

         - Marking

         - Bulk ID number **9.3 Packing**

At customer/subcontractor level, it is recommended to mount the VL53L0X in a clean environment to avoid
foreign material deposition.

To help avoid any foreign material contamination at phone assembly level the modules are shipped in a tape and
reel format. The packaging is vacuum-sealed and includes a desiccant.

*Note:* *For sensors with the liner option, the liner must be removed during assembly of the customer device, just before*
*mounting the cover glass. The liner is compliant with a reflow at 260°C (as per JEDEC-STD-020E).*

**DS11555** - **Rev 6** **page 29/38**


-----

### **VL53L0X**

**Packaging and labeling**
##### **9.3.1 Tape outline drawing**

The pictures below show the tape outline drawings for modules without and with liner. The pin1 of the module is
referenced by a red star in the figures.

**Figure 26. Tape outline drawing - option modules without liner**

**Figure 27. Tape outline drawing - option modules with liner**


**DS11555** - **Rev 6** **page 30/38**


-----

### **VL53L0X**

**Packaging and labeling** **9.4 Pb-free solder reflow process**

Table 16. Recommended solder profile and Figure 28. Solder profile show the recommended and maximum
values for the solder profile.

Customers have to tune the reflow profile depending on the PCB, solder paste, and material used. We expect
customers to follow the recommended reflow profile, which is specifically tuned for the VL53L0X package.

If a customer must perform a reflow profile, which is different from the recommended one, the new profile must be
qualified by the customer at their own risk. This is especially true for peaks >240°C. In any case, the profile must
be within the “maximum” profile limit described in Table 16. Recommended solder profile.

*Note:* *Temperatures mentioned in the table below are measured at the top of the VL53L0X package.*

**Table 16. Recommended solder profile**

**Figure 28. Solder profile**

|Parameters|Recommended|Maximum|Unit|
|---|---|---|---|
|Minimum temperature (TS min)|130|150|°C|
|Maximum temperature (TS max)|200|200||
|Time ts (TS min to TS max)|90-110|60-120|s|
|Temperature (TL)|217|217|°C|
|Time (tL)|55-65|55-65|s|
|Ramp up|2|3|°C/s|
|Temperature (Tp-10)|—|250|°C|
|Time (tp-10)||10|s|
|Ramp up||3|°C/s|
|Peak temperature (Tp)|240|260 max|°C|
|Time to peak|30|300|s|
|Ramp down (peak to TL)|-4|-6|°C/s|



*Note:* *The component should be limited to a maximum of three passes through this solder profile.*

*Note:* *As the VL53L0X package is not sealed, only a dry reflow process should be used (such as convection reflow).*
*Vapor phase reflow is not suitable for this type of optical component.*

*Note:* *The VL53L0X is an optical component and should be treated carefully. This typically includes using a ‘no wash’*
*assembly process.*


**DS11555** - **Rev 6** **page 31/38**


-----

### **VL53L0X**

**Packaging and labeling** **9.5 Handling and storage precautions**
##### **9.5.1 Shock precaution**

Sensor modules house numerous internal components that are susceptible to shock damage. If a unit is subject
to excessive shock, it must be rejected even if no apparent damage is visible. For example, if it is dropped on the
floor, or if a tray/reel of units is dropped on the floor. **9.5.2 Part handling**

Handling must be done with nonmarring, ESD, safe carbon, plastic, or Teflon™ tweezers. Ranging modules are
susceptible to damage or contamination. The customer is advised to use a clean assembly process after
removing the tape from the parts, and until a protective cover glass is mounted. **9.5.3 Compression force**

A maximum compressive load of 25 N should be applied on the module. **9.5.4 Moisture sensitivity level**

Moisture sensitivity is level 3 (MSL) as described in IPC/JEDEC JSTD-020-C.
### **9.6 Storage temperature conditions**

**Table 17. Recommended storage conditions**

|Parameter|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|
|Temperature (storage)|-40|—|85|°C|



**DS11555** - **Rev 6** **page 32/38**


-----

### **VL53L0X**

**Package information**
## **10 Package information**

[In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK packages,](https://www.st.com/ecopack)
depending on their level of environmental compliance. ECOPACK specifications, grade definitions and product
[status are available at: www.st.com. ECOPACK is an ST trademark.](http://www.st.com)

**DS11555** - **Rev 6** **page 33/38**


-----

### **VL53L0X**

**Ordering information**
## **11 Ordering information**

|Col1|Table 18. Order codes|Col3|
|---|---|---|
|Order codes|Package|Packing|
|VL53L0CXV0DH/1|Optical LGA12 with liner|Tape and reel|
|VL53L0CXV9DH/1|Optical LGA12 without liner|Tape and reel|



**DS11555** - **Rev 6** **page 34/38**


-----

### **VL53L0X**

**Ordering information**

### **Revision history**


**Table 19. Document revision history**

|Date|Version|Changes|
|---|---|---|
|30-May-2016|1|Initial release|
|09-Apr-2018|2|Updated document title Updated Features Small text changes to Description. Removed note from Section 3.6.2: Ranging phase. Added text before Figure 24. Outline drawing - option with liner (3/3).|
|12-Oct-2021|3|Section 4: Control interface: Replaced “camera module” with “Time-of-Flight” sensor.|
|29-Nov-2022|4|Updated Figure 22. Outline drawing (1/3), Figure 23. Outline drawing (2/3), and Figure 24. Outline drawing - option with liner (3/3). Added a note before Figure 24. Outline drawing - option with liner (3/3). Updated Section 9.3.1: Tape outline drawing.|
|08-Dec-2022|5|Updated document title. Updated Application. Removed “new generation” from the Description.|
|03-Jun-2023|6|Updated Section 1: Acronyms and abbreviations. Updated Section 5.5: Digital input and output. Removed the note before Figure 24. Outline drawing - option with liner (3/3), and updated the title of this drawing. Updated Section 8: Laser safety. Removed Figure 26: Example of marking. Updated Section 9.3: Packing. Updated Section 9.3.1: Tape outline drawing. Updated Section 11: Ordering information. Master and slave replaced by controller and target respectively|


**DS11555** - **Rev 6** **page 35/38**


-----

### **VL53L0X**

**Contents**
## **Contents**
### **1 Acronyms and abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .2** **2 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .3**
#### 2.1 Technical specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 2.2 System block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 2.3 Device pinout. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 2.4 Application schematic. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
### **3 Functional description. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .6**
#### 3.1 System functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6 3.2 Firmware state machine description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 3.3 Customer manufacturing calibration flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
##### 3.3.1 SPAD and temperature calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 3.3.2 Ranging offset calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 3.3.3 Crosstalk calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
#### 3.4 Ranging operating modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .10 3.5 Ranging profiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .10 3.6 Ranging profile phases. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .10
##### 3.6.1 Initialization and load calibration data phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 3.6.2 Ranging phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 3.6.3 Digital housekeeping. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
#### 3.7 Getting the data: Interrupt or polling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .12 3.8 Device programming and control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .12 3.9 Power sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .13 3.10 Ranging sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .14
### **4 Control interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .15**
#### 4.1 I²C interface - timing characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .17 4.2 I²C interface - reference registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .18
### **5 Electrical characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .19**
#### 5.1 Absolute maximum ratings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .19 5.2 Recommended operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .19 5.3 Electrostatic discharge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .19 5.4 Current consumption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .20 5.5 Digital input and output. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .20
### **6 Performance. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .21**
#### 6.1 Measurement conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .21

**DS11555** - **Rev 6** **page 36/38**


-----

### **VL53L0X**

**Contents**
#### 6.2 Maximum ranging distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .23 6.3 Ranging accuracy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .23
##### 6.3.1 Standard deviation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 6.3.2 Range profile examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24 6.3.3 Ranging offset error . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
### **7 Outline drawings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .25** **8 Laser safety . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .28** **9 Packaging and labeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .29**
#### 9.1 Product marking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .29 9.2 Inner box labeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .29 9.3 Packing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .29
##### 9.3.1 Tape outline drawing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
#### 9.4 Pb-free solder reflow process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .31 9.5 Handling and storage precautions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .32
##### 9.5.1 Shock precaution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 9.5.2 Part handling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 9.5.3 Compression force . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 9.5.4 Moisture sensitivity level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
#### 9.6 Storage temperature conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .32
### **10 Package information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .33** **11 Ordering information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .34** **Revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .35**

**DS11555** - **Rev 6** **page 37/38**


-----

### **VL53L0X**

**IMPORTANT NOTICE – READ CAREFULLY**

STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and improvements to ST
products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on ST products before placing orders. ST
products are sold pursuant to ST’s terms and conditions of sale in place at the time of order acknowledgment.

Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or the design of
purchasers’ products.

No license, express or implied, to any intellectual property right is granted by ST herein.

Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.

[ST and the ST logo are trademarks of ST. For additional information about ST trademarks, refer to www.st.com/trademarks. All other product or service names](http://www.st.com/trademarks)
are the property of their respective owners.

Information in this document supersedes and replaces information previously supplied in any prior versions of this document.

© 2024 STMicroelectronics – All rights reserved

**DS11555** - **Rev 6** **page 38/38**


-----

