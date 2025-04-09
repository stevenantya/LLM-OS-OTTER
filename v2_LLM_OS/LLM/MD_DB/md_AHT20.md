# **Data Sheet AHT20**
## Humidity and Temperature Sensor
### •
## Full calibration
### •
## Digital output, I [2] C interface
### •
## Excellent long-term stability
### •
## SMD package suitable for reflow soldering
### •
## Quick response and strong anti-jamming capability
### **1 Product Description**

HVAC, dehumidifier, testing and inspection equipment, consumer products, automobiles, automatic
control, data loggers, weather stations, home appliances, humidity control, medical and other related
temperature and humidity detection and control.

**Figure 1.** AHT20 Sensor Package Diagram (Unit: mm Tolerance: ±0.1 mm).

[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 1 / 16


-----

|Relative Humidity|Col2|min|typical|max|unit|
|---|---|---|---|---|---|
|Parameter|condition|min|typical|max|unit|
|resolution|Typical|-|0.024|-|%RH|
|Accuracy error1|Typical|-|±2|-|%RH|
||max|See Figure 2||-|%RH|
|repeatable|-|-|±0.1|-|%RH|
|hysteresis|-|-|±1|-|%RH|
|nonlinear|-|-|<0.1|-|%RH|
|Response time2|τ 63%|-|8|-|s|
|Scope of work|Extended3|0|-|100|%RH|
|Prolonged Drift4|-|-|<1|-|%RH /yr|

|Temperature|Col2|min|typical|max|unit|
|---|---|---|---|---|---|
|Parameter|condition|min|typical|max|unit|
|resolution|Typical|-|0.01|-|℃|
|Accuracy Error1|Typical|-|±0.3|-|℃|
||max|See Figure 3||-|℃|
|repeatable|-|-|±0.1|-|℃|
|hysteresis|-|-|±0.1|-|℃|
|Response time6|τ63%|5||30|S|
|Scope of work|Extended3|-40|-|85|℃|
|Prolonged Drift|-|-|<0.1|-|℃/yr|


.

### **2 Sensor Specifications**

**Relative Humidity**

Parameter co n d i t i o n min typical max

resolution Typical        - 0.024        
Accuracy error [1] T y pical      - ±2      max See Fi gu r e 2                  
re p eatable        -        - ±0.1        
h y steresis       -       - ±1       
                                  -                                   - <0.1                                   nonlinear

τ 63%                - 8                Response time [2]

Extended [3] 0                    - 100
Scope of work

                                  -                                   - <1                                   Prolonged Drift [4]

**Table 1** . Humidity characteristics table.

**Temperature**

Parameter condition min typical max

resolution Typical        - 0.01        
Typical                        - ±0.3                        
Accuracy

Error [1] max See Figure 3         
repeatable       -       - ±0.1       
hysteresis        -        - ±0.1        
τ63% 5 30
Response time [6]

Extended [3] -40                    - 85
Scope of work

                                  -                                   - <0.1                                   Prolonged Drift

**Table 2.** Temperature Characteristic table

**Figure 2** . Typical and maximum error in relative humidity at 25°C **Figure 3** . Typical and maximum temperature errors.


[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021


2 / 16


-----

**Electrical Specifications** **Package Information**

**Table 3.** Electrical characteristics. **Table 4.** Package
### **3 Expansion Performance**

**3.1 Operating Conditions**

The sensor has stable performance within the recommended working range, as shown in Figure 4. Long-term
exposure to conditions outside the normal range, especially when the humidity is> 80%, may cause temporary
signal drift (drift + 3% RH after 60 hours). After returning to normal working conditions, the sensor will slowly selfrecover to the calibration state. Refer to "Recovery Processing" in section 4.3 to speed up the recovery process.
Long-term use under abnormal conditions will accelerate the aging of the product.

**Figure 4** . Working conditions

1. This accuracy is based on the sensor's test accuracy at a supply voltage of 3.3Vat 25°C when tested at the factory. This value
does not include hysteresis and non-linearity and applies only to non-condensing conditions.

2. Time required to achieve 63% first-order response at 25°C and 1 m/s airflow.

3. Normal operating range: 0-80%RH, beyond this range, there will be deviation in the sensor reading (after 60hours in 90%RH
humidity, drift >3%RH).

4. If there are volatile solvents, tapes with pungent odors, adhesives, and packaging materials around the sensor, the readings may
shift. For details, please refer to the relevant documents.

5. The minimum and maximum values for supply current and power consumption are based on VCC = 3.3V and T < 60°C. The mean
value is the value of one measurement taken in every two seconds.

6. The response time depends on the thermal conductivity of the sensor substrate.

[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 3 / 16


-----

**3.2 RH Accuracy at Different Temperatures**

Figure 2 defines the RH accuracy at 25°C, and Figure 5 shows the typical humidity error for other temperature

ranges.

**Figure 5.** The typical error of humidity in the range of 0~80°C, unit: (%RH)

Please note: The above error is the typical error (excluding hysteresis) of the reference instrument test with a high-precision
dew point meter.

**3.3 Electrical Characteristics**

The power consumption given in Table 3 is related to temperature and supply voltage VDD. Refer to Figures 6 and
7 for power consumption estimation. Please note that the curves in Figures 6 and 7 are typical natural
characteristics, and there may be deviations.

**Figure 6** . Typical supply current vs. temperature curve (sleep mode) when VDD=3.3V.

Please note that there is a deviation of approximately ±25% between these data and the displayed value.

[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 4 / 16


-----

**Figure 7** The relationship between typical supply current and supply voltage at 25℃ Curve (sleep mode), please
note that the deviation of these data from the displayed value may reach ±50% of the displayed value. At 60℃, the coefficient
is about 15 (Compared with table 2)
### **4 Applications**

**4.1 Welding Instructions**

SMD I/O pads are made of copper lead frame plane substrates, except these pads are exposed and are used for
mechanical and circuit connections. For use, both I/O pads and bare pads need to be soldered to the PCB. To
prevent oxidation and optimize welding, the solder joints at the bottom of the sensor are coated with Ni/Au. On the
PCB, the length of the I/O contact surface should be 0.2-0.3mm larger than the sensor's I/O sealing pad, and the
width should be 0.1-0.2mm larger than the sealing pad. The part near the inner side should match the shape of the
I/O pad, and the ratio of the pin width to the SMD sealing pad width should be 1:1, as shown in Figure 8.
For mesh and solder layer designs, it is recommended to use copper foil defined pads (SMD) with openings in the
solder layer larger than the metal pads. For SMD pads, if the gap between the copper foil pads and the solder
resistance layer is 60μm-75μm, the size of the solder resistance layer opening should be greater than the size of
the pad 120μm-150μm.The square portion of the sealing pad shall match the corresponding square solder mask
opening to ensure that there is sufficient solder mask area (especially at the corners) to prevent solder intersecting.
Each pad shall have its own solder layer opening to form a network of solder layers around adjacent pads.

**Figure 8.** Recommended sensor PCB design size (unit:
mm), the outer dotted line is the external size of the SMD
package.

For solder printing, laser cutting stainless steel mesh with electronic polishing trapezoidal wall is recommended,
with recommended thickness of 0.125 mm. The steel mesh size of the pad should be 0.1 mm longer than PCB pad
and placed 0.1 mm away from the packaging center. Steel mesh with bare pads must cover 70% - 90% of the pad
area - that is, the central position of the heat dissipation area reaches 1.4 mm x 2.3 mm.

Due to the low SMD mounting, it is recommended to use no-cleaning type3 solders tin and to purify it with nitrogen
during reflux.

[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 5 / 16


-----

**Figure 9.** JEDEC Standard welding procedure diagram. Tp<=260°C，tp<30 sec, lead-free welding. TL<220°C，tl<150 sec,

The rate of temperature rise and fall during welding shall be < 5°C/sec

Sensor can be welded through standard reflow furnace. The sensor fully meets the IPC/JEDEC J-STD-020D
welding standard. The contact time should be less than 30 seconds at the highest 260℃ (see Fig. 9) and the
ultimate welding temperature that the sensor can withstand is 260℃，so it is recommended to use low
temperature 180℃ when reflow soldering.

Note: After reflow welding, the sensor should be stored at room temperature of 25℃ and relative humidity greater
than 75%RH for 12~72 hours, or placed at temperature of 60℃~85℃ and relative humidity greater than 85%RH
for 2~6 hours, to ensure the rehydration of the polymer, otherwise it will lead to sensor reading drift. Using low
temperature reflow (e.g.180℃) can reduce hydration time.

Don't not use the sensor in corrosive gas or condensed water.

**4..2 Storage Conditions and Operating Instructions**

The humidity sensitivity level (MSL) is 1, according to the IPC/JEDEC J-STD-020 standard. Therefore, it is
recommended to use it within one year after shipment.

The temperature and humidity sensor is not an ordinary electronic component and needs to be carefully protected.
Users must pay attention to this point. Long-term exposure to high concentrations of chemical vapor will cause the
sensor's readings to drift. Therefore, it is recommended to store the sensor in the original packaging including a
sealed ESD bag, and meet the following conditions: temperature range 10℃-50℃ (within a limited time 0-85℃);
humidity 20-60%RH (without ESD package) sensor). For those sensors that have been removed from the original
packaging, we recommend storing them in an antistatic bag made of PET/AL/CPE containing metal.

During production and transportation, the sensor should avoid contact with high concentrations of chemical
solvents and long-term exposure. Avoid contact with volatile glues, tapes, stickers or volatile packaging materials,
such as foam foils and foam materials Wait. The production area should be well ventilated.

**4.3 Recovery Processing**

As mentioned above, the readings can drift if the sensor is exposed to extreme operating conditions or chemical
vapors. It can be restored to the calibration state by the following processing. If the humidity is high, take drying
measures: keep it at 60-85℃ and <5%RH for 2-10 hours until recovery; If the humidity is low, it can be rehydrated.
Refer to Section 4.1 for reflow soldering after rehydration treatment.

**4.4 Temperature Effect**

The relative humidity of gases depends largely on temperature. Therefore, when measuring humidity, all sensors
measuring the same humidity should work at the same temperature as possible. When testing, it is necessary to
ensure that the same temperature, and then compare the humidity readings.

If the sensor and the heating-prone electronic components are placed on the same printing circuit board, measures

[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 6 / 16


-----

should be taken to minimize the effect of heat transfer as far as possible in the design of the circuit.

For example, to maintain good ventilation of the shell, the copper coating of AHT20 and other parts of the printed
circuit board should be as smallest as possible, or leave a gap between them. (See Fig. 10)

**Figure 10** The top view of AHT20 printed circuit board, the design of the milling slit is added in the figure, The heat transfer
can be reduced to a minimum.

In addition, when the measurement frequency is too high, the temperature of the sensor itself will rise and affect
the measurement accuracy. In order to ensure that its own temperature rise is low by 0.1℃, it is recommended
that the IIC frequency should be between 10K and 400KHz during measurement, and should not be too high, and
the data collection cycle should be greater than 1 second/time.

**4.5 Product application scenario design**
In product design, the sensor has following characteristics:

1) Sensor is in full contact with the outside air

**Housing**

**PCB**

**Figure 11.** Suitable windows on the enclosure provide good access to environmental measurements and allow for greater
air exchange.

2) The sensor is completely isolated from the air nside the housing

**Housing**

**PCB**

**Figure 12.** The sensor is isolated from the air inside the housing,
which minimizes the impact of the air inside the housing on the

sensor.

3) Small measurement dead zone around the sensor

**Housing**

**PCB**

**Figure 13.** Small measurement dead zone helps the sensor to
quickly and comprehensively detect environmental changes.

4) The sensor is isolated from the heat

[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 7 / 16


-----

**Figure 14.** The sensor is isolated from the internal heat source to
minimize the effect of internal heat on sensor.

5) The sensor power supply can be controlled

In order to improve the stability of the system, the following power supply controllable scheme is provided:

**Figure 15** . Typical application circuit.

Note: 1. The power supply voltage range of the host MCU to the sensor is 2.2~5.5V.
2. When the sensor is just powered on, MCU gives priority to VDD power supply, and SCL and SDA high
levels can be set after 5ms.

6) The wiring rules of the sensor on the PCB

In order to improve the reliability of the sensor, the layout of the circuit board should be avoided in the bottom of
the sensor wiring or copper design.

**4.6 Materials for Sealing and Encapsulation**

Many materials absorb moisture and will act as a buffer, which will increase response time and lag. Therefore, the
materials around the sensor should be carefully selected. The recommended materials are: metal materials, LCP,
POM(Delrin), PTFE(Teflon), PE, PEEK, PP, PB, PPS, PSU, PVDF, PVF.

Material used for sealing and bonding (conservative recommendation): It is recommended to use epoxy resin to
encapsulate electronic components, or silicone resin. The gases released by these materials may also contaminate
AHT20 (see 4.2). Therefore, the sensor should be assembled last, and placed in a well-ventilated place, or dried for
24 hours in an environment of >50℃, so as to release the polluted gas before packaging.

**4.7 Wiring Rules and Signal Integrity**

If the SCL and SDA signal lines are parallel and very close to each other, it may cause signal crosstalk and
communication failure. The solution is to place VDD and/or GND between the two signal lines, separate the signal
lines, and use shielded cables. In addition, reduce

SCL frequency may also improve the integrity of signal transmission. A 10uF decoupling capacitor must be added
between the power supply pins (VDD, GND) for filtering. This capacitor should be as close as possible to the sensor.
See the next chapter.

[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 8 / 16


-----

### **5 Interface Definition**

**Table 5** . Sensor pin distribution (top view)

**5.1 Power Pin (VDD, GND)**

The power supply range of the sensor is 2.2-5.5V. A decoupling capacitor of 10uF must be added between VDD
and GND to play a filtering role. VDD is better than SDA and SCL power on or synchronous power on, to avoid the
signal line (SCL/SDA) leakage current into the chip, resulting in power on the chip in the non-working state.

**5.2 Serial Clock SCL**

The serial clock is used to synchronize the communication between the microprocessor and sensor. Since the
interface contains completely static logic, there is no minimum SCL frequency.

**5.3 Serial Data SDA**

SDA pins are used for data input and output of the sensor. The SDA is effective on the rising edge of the serial
clock SCL when sending commands to the sensor, and the SDA must remain stable when the SCL is at high levels.
After the SCL falling edge, the SDA value can be changed. To ensure communication security, the effective time of
SDA should be extended to TSU and THO before the rising edge of SCL, and after the falling edge of SCL - refer
to Figure 17.When reading data from the sensor, the SDA is effective after the SCL is low (TV) and remains until
the falling edge of the next SCL.

**Figure 16** . Typical application circuit

Note:
1. The pull-up voltage of SCL and SDA must be powered by VDD, and the power supply voltage range is 2.2~ 5.5V;
2. Add 10μF decoupling capacitor between VDD and GND
3. In order to ensure that the sensor is not disturbed by the circuit, please add filter circuit to the VDD, such as C1 on the
typical circuit.

To avoid conflict of signal, the microprocessor (MCU) must be driven SDA and SCL only at low level, need an
external pull-up resistors (for example: 2.0 ~ 4.7 K Ω) will lift the signals to high level, pull-up resistance may have
often included in a microprocessor I/O circuits. Refer to Tables 7 and 8 for detailed information on sensor
input/output characteristics.

[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 9 / 16


-----

### **6 Electrical Characteristics**

**6.1 Absolute Maximum Ratings**

The electric specifications of sensor are defined in Table 2.The absolute maximum ratings given in Table 6 are
only stress ratings and to provide more information. Under such conditions, it is not advisable for the device to
perform functional operation. Exposure to absolute maximum rating or a long time may affect the reliability of the

sensor.

|parameters|Min|Max|Unit|
|---|---|---|---|
|VDD to GND|-0.3|5.5|V|
|Digital I/O Pins (SDA,SCL) to GND|-0.3|VCC+0.3|V|
|Input current per pin|-10|10|mA|



**Table 6** . Absolute maximum electrical ratings

ESD electrostatic discharge conforms to JEDECJESD22-A114 standard (human body model ±4kV),
JEDECJESD22-A115 (machine model ±200V). If the test condition exceeds the nominal limit index, the sensor
needs to add an additional protection circuit.

**6.2 Input /Output Characteristics**

Electrical characteristics, such as power consumption, input and output high and low voltages, etc., depend on the
power supply voltage. In order to make the sensor communication smooth, it is very important to ensure that the
signal design is strictly limited to the range given in Table 7, 8 and Figure 9.

**Table 7.** DC characteristics of digital input and output pads, if there is no special statement VDD=2.2V to 5.5VT=-40°C to 85°C

**Figure 17** . Timing diagram of digital input/output

|parameters|conditions|Min|typical|Max|unit|
|---|---|---|---|---|---|
|Low output Voltage VOL|VDD=3.3V, -4mA<IOL<0mA|0|-|0.4|V|
|High output Voltage VOH||70% VDD|-|VDD|V|
|Output sink current IOL||-|-|-4|mA|
|Low output Voltage VIL||0|-|30%VDD|V|
|High output Voltage VIH||70% VDD|-|VDD|V|
|Input Current|VDD=5.5V,VIN=0V to 5.5V|-|-|±1|uA|



[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 10 / 16


-----

The abbreviations are explained in Table 8. The thicker SDA line is controlled by the sensor, and the ordinary SDA
line is controlled by the single-chip microcomputer. Please note that the SDA valid read time is triggered by the
falling edge of the previous conversion.

**Table 8** . Timing characteristics of I²C fast mode digital Inputs/outputs.

The meaning is shown in Figure 17 Unless otherwise noted.
### **7 Sensor Communication**

Sensor uses standard I²C protocol for communication. For information about the I²C protocol other than the
following chapters, please refer to the following website: www.aosong.com provides a sample program for
reference.

**7.1 Start the Sensor**

The first step is to power up the sensor with the selected VDD supply voltage (range between 2.2V and 5.5V).
After power-on, the sensor needs ≥100ms time (SCL is high at this time) to reach the idle state and it is ready to
receive commands sent by the host (MCU).

**7.2 Start/Stop Sequence**

Each transmission sequence starts with the Start state and ends with the Stop state, as shown in Figure 18 and
Figure 19.

**Figure 18** . Start transmission status (S)
When SCL is high, SDA is converted from high to low. The start state is a special bus state controlled by the
master, indicating the start of the slave transfer (after Start, the BUS bus is generally considered to be in a busy
state)

**Figure 19** . Stop transmission state (P)

[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 11 / 16


-----

When SCL is high, the SDA line changes from low to high. The stop state is a special bus state controlled by
the master, indicating the end of the slave transmission (after Stop, the BUS bus is generally considered to be
in an idle state).

**7.3 Send Command**

After the transmission is started, the first byte of I²C that is subsequently transmitted includes the 7-bit I²C device
address 0x38 and a SDA direction bit x (read R: ‘1’, write W: ‘0’). After the 8th falling edge of the SCL clock, pull
down the SDA pin (ACK bit) to indicate that the sensor data is received normally. After sending the measurement
command 0xAC, the MCU must wait until the measurement is completed.

**Table 9** . Status bit description

**7.4 Sensor Reading Process**

1. After power-on, wait for ≥100ms Before reading the temperature and humidity value, get a byte of status word
by sending 0x71. If the status word and 0x18 are not equal to 0x18, initialize the 0x1B, 0x1C, 0x1E registers,
details Please refer to our official website routine for the initialization process; if they are equal, proceed to the next
step.

2. Wait 10ms to send the 0xAC command (trigger measurement). This command parameter has two bytes, the first
byte is 0x33, and the second byte is 0x00.

3. Wait 80ms for the measurement to be completed, if the read status word Bit[7] is 0, it means the measurement
is completed, and then six bytes can be read continuously; otherwise, continue to wait.

4. After receiving six bytes, the next byte is CRC check data, which the user can read as needed. If the receiver
needs CRC check, it will send an ACK reply after receiving the sixth byte, otherwise it will send a NACK reply. The
initial value of CRC is 0xFF, and the CRC8 check polynomial is:

CRC [7:0] = 1+X [4] +X [5] +X [8]

5. Calculate the temperature and humidity value

Note: The calibration status check in the first step only needs to be checked when the power is turned on.No
operation is required during the acquisition process.

|Bits|Significance|Description|
|---|---|---|
|Bit [7]|Busy indication|1-Equipment is busy, in measurement mode 0- Equipment is idle, in hibernation state|
|Bit [6:5]|Retain|Retain|
|Bit [4]|Retain|Retain|
|Bit [3]|CAL Enable|1 - Calibrated 0 - Uncalibrated|
|Bit [2:0]|Retain|Retain|



[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 12 / 16


-----

Read temperature and humidity data

Note: The sensor needs time to collect. After the host sends a measurement command (0xAC), delay more than 80
milliseconds before reading the converted data and judging whether the returned status bit is normal. If the status bit [Bit7] is 0,
it means that the data can be read normally. When it is 1, the sensor is busy, and the host needs to wait for the data
processing to complete.
### **8 Signal Conversion**

**8.1 Relative Humidity Conversion**

The relative humidity RH can be calculated according to the relative humidity signal S RH output by SDA through the
following formula (the result is expressed in %RH):
#### RH[%]  (S2 RH20 ) *100%

**8.2 Temperature Conversion**

The temperature T can be calculated by substituting the temperature output signal S T into the following formula:
(The result is expressed in temperature ℃): T[℃] （ 2S 20T ）* 200 - 50

[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 13 / 16


-----

### **9 Environmental Stability**

If the sensor is used in equipment or machinery, make sure that the sensor used for measurement and the sensor
used for reference sense the same temperature and humidity. If the sensor is placed in the equipment, the
response time will be prolonged, so ensure that sufficient measurement time is reserved in the program design.
The sensor is based on Austrian Song temperature and humidity sensor corporate standards are tested. The
performance of the sensor under other test conditions is not guaranteed and cannot be used as a part of the
sensor's performance. Especially for specific occasions required by users, no promises are made.

**9.1 Tracking Information**

All sensors have laser labels on their surfaces. See Figure 20.

**Figure 20.** Sensor laser marking.

The label on the carton is shown in Figure 15, and provides other tracking information.
A label is also attached to the tape, as shown in Figure 21, and other trace information is provided.

**Figure 21.** Label on the tape.

**9.2 Transport packaging**

Sensor is packaged in tape and reel, sealed in an antistatic ESD bag. The standard packaging size is 5000 sheets
per roll. For sensor packaging, the 440mm (Approximately 55 sensor capacity) and the front 200mm
(Approximately 30 sensor capacity) part of each reel is empty.
The packaging diagram with sensor positioning is shown in Figure 22. The reel is placed in an anti-static pocket

[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 14 / 16


-----

**Figure 22** . Package tape and sensor location diagram.

[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 15 / 16


-----

### **Important Notices**

**Warning, Personal Injury**

Do not apply this product to safety protection devices or
emergency stop equipment, and any other applications
that may cause personal injury due to the product's failure.
Do not use this product unless there is a special purpose
or use authorization. Refer to the product data sheet and
application guide before installing, handling, using or
maintaining the product. Failure to follow this
recommendation may result in death and serious personal
injury.

If the buyer intends to purchase or use Aosong’s products
without obtaining any application licenses and
authorizations, the buyer will bear all the compensation for
personal injury and death arising therefrom, and exempt
Aosong’s managers and employees and affiliated
subsidiaries from this, Agents, distributors, etc. may incur
any claims, including: various costs, compensation fees,
attorney fees, etc.

**ESD Protection**

Due to the inherent design of the component, it is sensitive
to static electricity. In order to prevent the damage caused
by static electricity or reduce the performance of the
product, please take necessary anti-static measures when
using this product.


**Quality Assurance**

The company provides a 12-month (1 year) quality
guarantee (calculated from the date of shipment) to direct
purchasers of its products, based on the technical
specifications in the product data manual published by
Aosong. If the product is proved to be defective during the
warranty period, the company will provide free repair or
replacement. Users need to satisfy the following conditions:

 Notify our company in writing within 14 days after the
defect is found.

 The defect of this product will help to find out the
deficiency in design, material and technology of our
product.

 The product should be sent back to our company at
the buyer’s expense.

 The product should be within the warranty period.
The company is only responsible for products that are
defective when used in applications that meet the technical
conditions of the product. The company does not make any
guarantees, guarantees or written statements about the
application of its products in those special applications. At
the same time, the company does not make any promises
about the reliability of its products when applied to products
or circuits.
#### This manual may be changed at any time without notice.

Copyright [®] 2021, **ASAIR** **[®]**


[www.aosong.com](http://www.aosong.com/) Version:V1.0 —— May 2021 16 / 16


-----

