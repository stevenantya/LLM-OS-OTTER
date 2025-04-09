|BMP280: Data sheet|Col2|
|---|---|
|Document revision 1.14||
|Document release date May 5th, 2015||
|Document number BST-BMP280-DS001-11||
|Technical reference code(s) 0273 300 416||
|Notes|Data in this document are subject to change without notice. Product photos and pictures are for illustration purposes only and may differ from the real product’s appearance.|


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 2|
|---|---|---|

### BMP280 D IGITAL P RESSURE S ENSOR

**Key parameters**

 - Pressure range 300 … 1100 hPa
(equiv. to +9000…-500 m above/below sea level)

 Package 8-pin LGA metal-lid
Footprint : 2.0 × 2.5 mm², height: 0.95 mm

 Relative accuracy ±0.12 hPa, equiv. to ±1 m
(950 … 1050hPa @25°C)

 Absolute accuracy typ. ±1 hPa
(950 ...1050 hPa, 0 ...+40 °C)

 Temperature coefficient offset 1.5 Pa/K, equiv. to 12.6 cm/K
(25 ... 40°C @900hPa)

 Digital interfaces I²C (up to 3.4 MHz)
SPI (3 and 4 wire, up to 10 MHz)

 Current consumption 2.7µA @ 1 Hz sampling rate

 - Temperature range -40 … +85 °C

 RoHS compliant, halogen-free

 - MSL 1

**Typical applications**

 Enhancement of GPS navigation
(e.g. time-to-first-fix improvement, dead-reckoning, slope detection)

 Indoor navigation (floor detection, elevator detection)

 Outdoor navigation, leisure and sports applications

 - Weather forecast

 Health care applications (e.g. spirometry)

 Vertical velocity indication (e.g. rise/sink speed)

**Target devices**

 Handsets such as mobile phones, tablet PCs, GPS devices

 Navigation systems

 - Portable health care devices

 - Home weather stations

 Flying toys

 - Watches

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 3|
|---|---|---|

|BMP180|BMP280|
|---|---|
|3.6 × 3.8 mm|2.0 × 2.5 mm|
|1.80 V|1.71 V|
|1.62 V|1.20 V|
|12 µA|2.7 µA|
|3 Pa|1.3 Pa|
|1 Pa|0.16 Pa|
|0.1°C|0.01°C|
|I²C|I²C & SPI (3 and 4 wire, mode ‘00’ and ‘11’)|
|Only P or T, forced|P&T, forced or periodic|
|up to 120 Hz|up to 157 Hz|
|None|Five bandwidths|


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 4|
|---|---|---|

### Index of Contents

**1. SPECIFICATION ........................................................................................................................ 7**

**2. ABSOLUTE MAXIMUM RATINGS ............................................................................................ 9**

**3. FUNCTIONAL DESCRIPTION ................................................................................................. 10**

3.1 B LOCK DIAGRAM ............................................................................................................... 11

3.2 P OWER MANAGEMENT ....................................................................................................... 11

3.3 M EASUREMENT FLOW ....................................................................................................... 11

3.3.1 P RESSURE MEASUREMENT ........................................................................................................... 12

3.3.2 T EMPERATURE MEASUREMENT ..................................................................................................... 13

3.3.3 IIR FILTER .................................................................................................................................... 13

3.4 F ILTER SELECTION ............................................................................................................ 14

3.5 N OISE .............................................................................................................................. 15

3.6 P OWER MODES ................................................................................................................. 15

3.6.1 S LEEP MODE ................................................................................................................................ 16

3.6.2 F ORCED MODE ............................................................................................................................. 16

3.6.3 N ORMAL MODE ............................................................................................................................. 16

3.6.4 M ODE TRANSITION DIAGRAM ......................................................................................................... 17

3.7 C URRENT CONSUMPTION ................................................................................................... 18

3.8 M EASUREMENT TIMINGS .................................................................................................... 18

3.8.1 M EASUREMENT TIME .................................................................................................................... 18

3.8.2 M EASUREMENT RATE IN NORMAL MODE ......................................................................................... 19

3.9 D ATA READOUT ................................................................................................................ 19

3.10 D ATA REGISTER SHADOWING ........................................................................................... 20

3.11 O UTPUT COMPENSATION ................................................................................................. 20

3.11.1 C OMPUTATIONAL REQUIREMENTS ............................................................................................... 20

3.11.2 T RIMMING PARAMETER READOUT ................................................................................................ 21

3.11.3 C OMPENSATION FORMULA .......................................................................................................... 21

3.12 C ALCULATING PRESSURE AND TEMPERATURE ................................................................... 22

**4. GLOBAL MEMORY MAP AND REGISTER DESCRIPTION .................................................. 24**

4.1 G ENERAL REMARKS .......................................................................................................... 24

4.2 M EMORY MAP ................................................................................................................... 24

4.3 R EGISTER DESCRIPTION .................................................................................................... 24

4.3.1 R EGISTER 0 X D0 *“* *ID* *”* .................................................................................................................... 24
4.3.2 R EGISTER 0 X E0 *“* *RESET* *”* .............................................................................................................. 24
4.3.3 R EGISTER 0 X F3 *“* *STATUS* *”* ............................................................................................................ 25
4.3.44.3.5 RR EGISTER EGISTER 00 XX F4F5 *““* *CTRLCONFIG* *_* *MEAS* *”* ............................................................................................................ 26 *”* ...................................................................................................... 25
4.3.64.3.7 RR EGISTER EGISTER 00 XX F7…0FA…0 XX F9FC *““* *PRESSTEMP* *””(_(_* *MSBMSB* *,,__* *LSBLSB* *,,__* *XLSBXLSB* *))* ................................................................... 27 .................................................................. 26

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 5|
|---|---|---|


**5. DIGITAL INTERFACES ............................................................................................................ 28**

5.1 I NTERFACE SELECTION ...................................................................................................... 28

5.2 I²C I NTERFACE .................................................................................................................. 28

5.2.1 I²C WRITE .................................................................................................................................... 29

5.2.2 I²C READ ..................................................................................................................................... 29

5.3 SPI INTERFACE ................................................................................................................. 30

5.3.1 SPI WRITE ................................................................................................................................... 31

5.3.2 SPI READ .................................................................................................................................... 31

5.4 I NTERFACE PARAMETER SPECIFICATION ............................................................................. 32

5.4.1 G ENERAL INTERFACE PARAMETERS ............................................................................................... 32

5.4.2 I²C TIMINGS ................................................................................................................................. 32

5.4.3 SPI TIMINGS ................................................................................................................................ 33

**6. PIN-OUT AND CONNECTION DIAGRAM ............................................................................... 35**

      6.1 P IN OUT ........................................................................................................................... 35

6.2 C ONNECTION DIAGRAM 4- WIRE SPI ................................................................................... 36

6.3 C ONNECTION DIAGRAM 3- WIRE SPI ................................................................................... 37

6.4 C ONNECTION DIAGRAM I [2] C ................................................................................................ 38

**7. PACKAGE, REEL AND ENVIRONMENT ................................................................................ 39**

7.1 O UTLINE DIMENSIONS ....................................................................................................... 39

7.2 L ANDING PATTERN RECOMMENDATION ............................................................................... 40

7.3 M ARKING .......................................................................................................................... 41

7.3.1 M ASS PRODUCTION DEVICES ........................................................................................................ 41

7.3.2 E NGINEERING SAMPLES ................................................................................................................ 41

7.4 S OLDERING GUIDELINES .................................................................................................... 42

7.5 T APE AND REEL SPECIFICATION ......................................................................................... 43

7.5.1 D IMENSIONS ................................................................................................................................ 43

7.5.2 O RIENTATION WITHIN THE REEL ..................................................................................................... 43

7.6 M OUNTING AND ASSEMBLY RECOMMENDATIONS ................................................................. 44

7.7 E NVIRONMENTAL SAFETY .................................................................................................. 44

7.7.1 R O HS ......................................................................................................................................... 44

7.7.2 H ALOGEN CONTENT ..................................................................................................................... 44

7.7.3 I NTERNAL PACKAGE STRUCTURE ................................................................................................... 44

**8. APPENDIX 1: COMPUTATION FORMULAE FOR 32 BIT SYSTEMS .................................. 44**

8.1 C OMPENSATION FORMULA IN FLOATING POINT .................................................................... 44

8.2 C OMPENSATION FORMULA IN 32 BIT FIXED POINT ................................................................ 45

**9. LEGAL DISCLAIMER ............................................................................................................... 47**

9.1 E NGINEERING SAMPLES .................................................................................................... 47

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 6|
|---|---|---|


9.2 P RODUCT USE .................................................................................................................. 47

9.3 A PPLICATION EXAMPLES AND HINTS ................................................................................... 47

**10. DOCUMENT HISTORY AND MODIFICATION ..................................................................... 48**

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 7|
|---|---|---|

#### **1. Specification **

If not stated otherwise,

  All values are valid over the full voltage range

  All minimum/maximum values are given for the full accuracy temperature range

  - Minimum/maximum values of drifts, offsets and temperature coefficients are ±3 values
over lifetime

  Typical values of currents and state machine timings are determined at 25 °C

  Minimum/maximum values of currents are determined using corner lots over complete
temperature range

  Minimum/maximum values of state machine timings are determined using corner lots
over 0…+65 °C temperature range

The specification tables are split into pressure and temperature part of BMP280

Table 2: Parameter specification

|Parameter|Symbol|Condition|Min|Typ|Max|Units|
|---|---|---|---|---|---|---|
|Operating temperature range|T A|operational|-40|25|+85|°C|
|||full accuracy|0||+65||
|Operating pressure range|P|full accuracy|300||1100|hPa|
|Sensor supply voltage|V DD|ripple max. 50mVpp|1.71|1.8|3.6|V|
|Interface supply voltage|V DDIO||1.2|1.8|3.6|V|
|Supply current|I DD,LP|1 Hz forced mode, pressure and temperature, lowest power||2.8|4.2|µA|
|Peak current|I peak|during pressure measurement||720|1120|µA|
|Current at temperature measurement|I DDT|||325||µA|
|Sleep current1|I DDSL|25 °C||0.1|0.3|µA|
|Standby current (inactive period of normal mode) 2|I DDSB|25 °C||0.2|0.5|µA|
|Relative accuracy pressure V = 3.3V DD|A rel|700 … 900hPa 25 . . . 40 °C||±0.12||hPa|
|||||±1.0||m|



1
Typical value at VDD = VDDIO = 1.8 V, maximal value at VDD = VDDIO = 3.6 V.
2
Typical value at VDD = VDDIO = 1.8 V, maximal value at VDD = VDDIO = 3.6 V.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 8|
|---|---|---|

|Offset temperature coefficient|TCO|900hPa 25 . . . 40 °C|Col4|±1.5|Col6|Pa/K|
|---|---|---|---|---|---|---|
|||||12.6||cm/K|
|Absolute accuracy pressure|AP ext|300 . . . 1100 hPa -20 . . . 0 °C||±1.7||hPa|
||AP full|300 . . . 1100 hPa 0 . . . 65 °C||±1.0||hPa|
|Resolution of output data in ultra high resolution mode|RP|Pressure||0.0016||hPa|
||RT|Temperature||0.01||°C|
|Noise in pressure|V p,full|Full bandwidth, ultra high resolution See chapter 3.5||1.3||Pa|
|||||11||cm|
||V p,filtered|Lowest bandwidth, ultra high resolution See chapter 3.5||0.2||Pa|
|||||1.7||cm|
|Absolute accuracy temperature3|AT|@ 25 °C||±0.5||°C|
|||0 . . . +65 °C||±1.0||°C|
|PSRR (DC)|PSRR|full V range DD|||±0.005|Pa/ mV|
|Long term stability4|P stab|12 months||±1.0||hPa|
|Solder drifts||Minimum solder height 50 µm|-0.5||+2|hPa|
|Start-up time|t startup|Time to first communication after both V > 1.58V and DD V > 0.65V DDIO|||2|ms|
|Possible sampling rate|f sample|osrs_t = osrs_p = 1; See chapter 3.8|157|182|tbd5|Hz|
|Standby time accuracy|t standby|||±5|±25|%|


3 Temperature measured by the internal temperature sensor. This temperature value depends on the PCB temperature, sensor
element self-heating and ambient temperature and is typically above ambient temperature.
4 Long term stability is specified in the full accuracy operating pressure range 0 … 65°C
5 Depends on application case, please contact Application Engineer for further questions

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 9|
|---|---|---|

#### **2. Absolute maximum ratings **

The absolute maximum ratings are provided in Table 3.

Table 3: Absolute maximum ratings

|Parameter|Condition|Min|Max|Unit|
|---|---|---|---|---|
|Voltage at any supply pin|V and V Pin DD DDIO|-0.3|4.25|V|
|Voltage at any interface pin||-0.3|V + 0.3 DDIO|V|
|Storage Temperature|≤ 65% rel. H.|-45|+85|°C|
|Pressure||0|20 000|hPa|
|ESD|HBM, at any Pin||±2|kV|
||CDM||±500|V|
||Machine model||±200|V|



BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 10|
|---|---|---|

#### **3. Functional description **

The BMP280 consists of a Piezo-resistive pressure sensing element and a mixed-signal ASIC.
The ASIC performs A/D conversions and provides the conversion results and sensor specific
compensation data through a digital interface.

BMP280 provides highest flexibility to the designer and can be adapted to the requirements
regarding accuracy, measurement time and power consumption by selecting from a high
number of possible combinations of the sensor settings.

BMP280 can be operated in three power modes (see chapter 3.6):

  sleep mode

  - normal mode

  - forced mode

In sleep mode, no measurements are performed. Normal mode comprises an automated
perpetual cycling between an active measurement period and an inactive standby period. In
forced mode, a single measurement is performed. When the measurement is finished, the
sensor returns to sleep mode.

A set of oversampling settings is available ranging from ultra low power to ultra high resolution
setting in order to adapt the sensor to the target application. The settings are predefined
combinations of pressure measurement oversampling and temperature measurement
oversampling. Pressure and temperature measurement oversampling can be selected
independently from 0 to 16 times oversampling (see chapter 3.3.1 and 3.3.2):

  - Temperature measurement

  Ultra low power

  - Low power

  - Standard resolution

  High resolution

  Ultra high resolution

BMP280 is equipped with a built-in IIR filter in order to minimize short-term disturbances in the
output data caused by the slamming of a door or window. The filter coefficient ranges from 0
(off) to 16.

In order to simplify the device usage and reduce the high number of possible combinations of
power modes, oversampling rates and filter settings, Bosch Sensortec provides a proven set of
recommendations for common use-cases in smart-phones, mobile weather stations or flying
toys (see chapter 3.4):

  Handheld device low-power (e.g. smart phones running Android)

  Handheld device dynamic (e.g. smart phones running Android)

  Weather monitoring (setting with lowest power consumption)

  Elevator / floor change detection

  Drop detection

  Indoor navigation

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 11|
|---|---|---|

###### **3.1 Block diagram **

Figure 1 shows a simplified block diagram of the BMP280:

SCK

GND

|Col1|VDDIO|Col3|
|---|---|---|
||||
||||


|OSC|POR|NVM|
|---|---|---|



Figure 1: Block diagram of BMP280

|VDDIO VDD|Col2|Col3|
|---|---|---|
|Voltage Voltage reference regulator (analog & digital) I n Pressure/ t temperature Analog ADC e sensing front-end Logic r element f a c e OSCPORNVM|||
||Voltage Voltage reference regulator (analog & digital) I n t Analog ADC e front-end Logic r f a c e OSCPORNVM||
||||
||||
||||
||||
||||
||||
||||
|||| **3.2 Power management **

The BMP280 has two separate power supply pins

  - V DD is the main power supply for all internal analog and digital functional blocks

  - V DDIO is a separate power supply pin, used for the supply of the digital interface

A power-on reset generator is built in which resets the logic circuitry and the register values
after the power-on sequence. There are no limitations on slope and sequence of raising the V DD
and V DDIO levels. After powering up, the sensor settles in sleep mode (see 3.6.1).

Warning. Holding any interface pin (SDI, SDO, SCK or CSB) at a logical high level when V DDIO is
switched off can permanently damage the device due caused by excessive current flow through
the ESD protection diodes.

If V DDIO is supplied, but V DD is not, the interface pins are kept at a high-Z level. The bus can
therefore already be used freely before the BMP280 V DD supply is established. **3.3 Measurement flow **

The BMP280 measurement period consists of a temperature and pressure measurement with
selectable oversampling. After the measurement period, the data are passed through an
optional IIR filter, which removes short-term fluctuations in pressure (e.g. caused by slamming a
door). The flow is depicted in the diagram below.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 12|
|---|---|---|

|Oversampling setting|Pressure oversampling|Typical pressure resolution|Recommended temperature oversampling|
|---|---|---|---|
|Pressure measurement skipped|Skipped (output set to 0x80000)|–|As needed|
|Ultra low power|×1|16 bit / 2.62 Pa|×1|
|Low power|×2|17 bit / 1.31 Pa|×1|
|Standard resolution|×4|18 bit / 0.66 Pa|×1|
|High resolution|×8|19 bit / 0.33 Pa|×1|
|Ultra high resolution|×16|20 bit / 0.16 Pa|×2|


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 13|
|---|---|---|


**3.3.2** **Temperature measurement**

Temperature measurement can be enabled or skipped. Skipping the measurement could be
useful to measure pressure extremely rapidly. When enabled, several oversampling options
exist. Each oversampling step reduces noise and increases the output resolution by one bit,
which is stored in the XLSB data register 0xFC. Enabling/disabling the temperature
measurement and oversampling setting are selected through the osrs_t[2:0] bits in control
register 0xF4.

Table 5: *osrs_t* settings

|osrs_t[2:0]|Temperature oversampling|Typical temperature resolution|
|---|---|---|
|000|Skipped (output set to 0x80000)|–|
|001|×1|16 bit / 0.0050 °C|
|010|×2|17 bit / 0.0025 °C|
|011|×4|18 bit / 0.0012 °C|
|100|×8|19 bit / 0.0006 °C|
|101, 110, 111|×16|20 bit / 0.0003 °C|



It is recommended to base the value of *osrs_t* on the selected value of *osrs_p* as per Table 4.
Temperature oversampling above ×2 is possible, but will not significantly improve the accuracy
of the pressure output any further. The reason for this is that the noise of the compensated
pressure value depends more on the raw pressure than on the raw temperature noise.
Following the recommended setting will result in an optimal noise-to-power ratio.

**3.3.3** **IIR filter**

The environmental pressure is subject to many short-term changes, caused e.g. by slamming of
a door or window, or wind blowing into the sensor. To suppress these disturbances in the output
data without causing additional interface traffic and processor work load, the BMP280 features
an internal IIR filter. It effectively reduces the bandwidth of the output signals [6] . The output of a
next measurement step is filter using the following formula:

*data* _ *filtered* _ *old*  ( *filter* _ *coefficien* *t*  )1  *data* _ *ADC*
*data* _ *filtered* 

*filter* _ *coefficien* *t*

,

where data_filtered_old is the data coming from the previous acquisition, and data_ADC is the
data coming from the ADC before IIR filtering.

The IIR filter can be configured using the filter[2:0] bits in control register 0xF5 with the following
options:

6 Since most pressure sensors do not sample continuously, filtering can suffer from signals with a frequency higher than the
sampling rate of the sensor. E.g. environmental fluctuations caused by windows being opened and closed might have a frequency
<5 Hz. Consequently, a sampling rate of ODR = 10 Hz is sufficient to obey the Nyquist theorem.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 14|
|---|---|---|


Table 6: *filter* settings

|Filter coefficient|Samples to reach ≥75 % of step response|
|---|---|
|Filter off|1|
|2|2|
|4|5|
|8|11|
|16|22|



In order to find a suitable setting for *filter*, please consult chapter 3.4.

When writing to the register *filter*, the filter is reset. The next value will pass through the filter
and be the initial memory value for the filter. If temperature or pressure measurement is
skipped, the corresponding filter memory will be kept unchanged even though the output
registers are set to 0x80000. When the previously skipped measurement is re-enabled, the
output will be filtered using the filter memory from the last time when the measurement was not
skipped.
###### **3.4 Filter selection **

In order to select optimal settings, the following use cases are suggested:

Table 7: Recommended filter settings based on use cases

|Use case|Mode|Over- sampling setting|osrs_p|osrs_t|IIR filter coeff. (see 3.3.3)|I DD [µA] (see 3.7)|ODR [Hz] (see 3.8.2)|RMS Noise [cm] (see 3.5)|
|---|---|---|---|---|---|---|---|---|
|handheld device low-power (e.g. Android)|Normal|Ultra high resolution|×16|×2|4|247|10.0|4.0|
|handheld device dynamic (e.g. Android)|Normal|Standard resolution|×4|×1|16|577|83.3|2.4|
|Weather monitoring (lowest power)|Forced|Ultra low power|×1|×1|Off|0.14|1/60|26.4|
|Elevator / floor change detection|Normal|Standard resolution|×4|×1|4|50.9|7.3|6.4|
|Drop detection|Normal|Low power|×2|×1|Off|509|125|20.8|
|Indoor navigation|Normal|Ultra high resolution|×16|×2|16|650|26.3|1.6|



BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 15|
|---|---|---|

###### **3.5 Noise **

Noise depends on the oversampling and filter settings selected. The stated values were
determined in a controlled pressure environment and are based on the average standard
deviation of 32 consecutive measurement points taken at highest sampling speed. This is
needed in order to exclude long term drifts from the noise measurement.

Table 8: Noise in pressure

Table 9: Noise in temperature

|Oversampling setting|IIR filter coefficient|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||off|2|4|8|16|
|Ultra low power|3.3|1.9|1.2|0.9|0.4|
|Low power|2.6|1.5|1.0|0.6|0.4|
|Standard resolution|2.1|1.2|0.8|0.5|0.3|
|High resolution|1.6|1.0|0.6|0.4|0.2|
|Ultra high resolution|1.3|0.8|0.5|0.4|0.2| **3.6 Power modes **

|Temperature oversampling|IIR filter off|
|---|---|
|oversampling ×1|0.005|
|oversampling ×2|0.004|
|oversampling ×4|0.003|
|oversampling ×8|0.003|
|oversampling ×16|0.002|



The BMP280 offers three power modes: sleep mode, forced mode and normal mode. These
can be selected using the mode[1:0] bits in control register 0xF4.

Table 10: *mode* settings

|mode[1:0]|Mode|
|---|---|
|00|Sleep mode|
|01 and 10|Forced mode|
|11|Normal mode|



BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 16|
|---|---|---|


**3.6.1** **Sleep mode**
Sleep mode is set by default after power on reset. In sleep mode, no measurements are
performed and power consumption (I DDSM ) is at a minimum. All registers are accessible; Chip-ID
and compensation coefficients can be read.

**3.6.2** **Forced mode**

In forced mode, a single measurement is performed according to selected measurement and
filter options. When the measurement is finished, the sensor returns to sleep mode and the
measurement results can be obtained from the data registers. For a next measurement, forced
mode needs to be selected again. This is similar to BMP180 operation. Forced mode is
recommended for applications which require low sampling rate or host-based synchronization.

I DDP

I DDT

I DDSB

I DDSL


Write

|rrent|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|cur osrs_t osrs_p P T T T P P P P T T P P P P Measurement Measurement Measurement Measurement Measurement Measurement Measurement Measurement Measurement Measurement Measurement Measurement B SL time|osrs_t osrs_p|||||||||||||||
|||||||||||||||||
|||surement T|surement T|surement P|surement P|surement P|surement P||surement T|surement T|surement P|surement P|surement P|surement P||
|||Mea|Mea|Mea|Mea|Mea|Mea||Mea|Mea|Mea|Mea|Mea|Mea||
|||||||||||||||||


POR Mode[1:0] = 01 Data readout Mode[1:0] = 01

settings
Figure 3: Forced mode timing diagram

**3.6.3** **Normal mode**



Normal mode continuosly cycles between an (active) measurement period and an (inactive)
standby period, whose time is defined by t standby . The current in the standby period (I DDSB ) is
slightly higher than in sleep mode. After setting the mode,measurement and filter options, the
last measurement results can be obtained from the data registers without the need of further
write accesses. Normal mode is recommended when using the IIR filter, and useful for
applications in which short-term disturbances (e.g. blowing into the sensor) should be filtered.

I DDP

I DDT

I DDSB

I DDSL


POR Write Mode[1:0] = 11 Data readout

settings

when needed

Figure 4: Normal mode timing diagram


|rrent|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|cur osrs_t osrs_p t standby P T T T P P P P T T P P P P Measurement Measurement Measurement Measurement Measurement Measurement Measurement Measurement Measurement Measurement Measurement Measurement B SL time|osrs_t osrs_p t standby|||||||||||||||
|||||||||||||||||
|||surement T|surement T|surement P|surement P|surement P|surement P||surement T|surement T|surement P|surement P|surement P|surement P||
|||Mea|Mea|Mea|Mea|Mea|Mea||Mea|Mea|Mea|Mea|Mea|Mea||
|||||||||||||||||


BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 17|
|---|---|---|

|t_sb[1:0]|t [ms] standby|
|---|---|
|000|0.5|
|001|62.5|
|010|125|
|011|250|
|100|500|
|101|1000|
|110|2000|
|111|4000|


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 18|
|---|---|---|

###### **3.7 Current consumption **

The current consumption depends on ODR and oversampling setting. The values given below
are normalized to an ODR of 1 Hz. The actual consumption at a given ODR can be calculated
by multiplying the consumption in Table 12 with the ODR used. The actual ODR is defined
either by the frequency at which the user sets forced measurements or by oversampling and
t standby settings in normal mode in Table 14.

Table 12: Current consumption

|Oversampling setting|Pressure oversampling|Temperature oversampling|I [µA] @ 1 Hz forced mode DD|Col5|
|---|---|---|---|---|
||||Typ|Max|
|Ultra low power|×1|×1|2.74|4.16|
|Low power|×2|×1|4.17|6.27|
|Standard resolution|×4|×1|7.02|10.50|
|High resolution|×8|×1|12.7|18.95|
|Ultra high resolution|×16|×2|24.8|36.85| **3.8 Measurement timings **

The rate at which measurements can be performed in forced mode depends on the
oversampling settings *osrs_t* and *osrs_p* . The rate at which they are performed in normal mode
depends on the oversampling setting settings *osrs_t* and *osrs_p* and the standby time t standby . In
the following table the resulting ODRs are given only for the suggested osrs combinations.

**3.8.1** **Measurement time**

The following table explains the typical and maximum measurement time based on selected
oversampling setting. The minimum achievable frequency is determined by the maximum
measurement time.

Table 13: measurement time

|Oversampling setting|Pressure oversampling|Temperature oversampling|Measurement time [ms]|Col5|Measurement rate [Hz]|Col7|
|---|---|---|---|---|---|---|
||||Typ|Max|Typ|Min|
|Ultra low power|×1|×1|5.5|6.4|181.8|155.6|
|Low power|×2|×1|7.5|8.7|133.3|114.6|
|Standard resolution|×4|×1|11.5|13.3|87.0|75.0|
|High resolution|×8|×1|19.5|22.5|51.3|44.4|
|Ultra high resolution|×16|×2|37.5|43.2|26.7|23.1|



BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 19|
|---|---|---|


**3.8.2** **Measurement rate in normal mode**

The following table explains which measurement rates can be expected in normal mode based
on oversampling setting and t standby .

Table 14: typical output data Rate (ODR) in normal mode [Hz]

|t [ms] standby|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|0.5|62.5|125|250|500|1000|2000|4000|
|166.67|14.71|7.66|3.91|1.98|0.99|0.50|0.25|
|125.00|14.29|7.55|3.88|1.97|0.99|0.50|0.25|
|83.33|13.51|7.33|3.82|1.96|0.99|0.50|0.25|
|50.00|12.20|6.92|3.71|1.92|0.98|0.50|0.25|
|26.32|10.00|6.15|3.48|1.86|0.96|0.49|0.25|



Table 15: Sensor timing according to recommended settings (based on use cases)

|Use case|Mode|Over- sampling setting|osrs_p|osrs_t|IIR filter coeff. (see 3.3.3)|Timing|ODR [Hz] (see 3.8.2)|BW [Hz] (see 3.3.3)|
|---|---|---|---|---|---|---|---|---|
|handheld device low-power (e.g. Android)|Normal|Ultra high resolution|×16|×2|4|t = standby 62.5 ms|10.0|0.92|
|handheld device dynamic (e.g. Android)|Normal|Standard resolution|×4|×1|16|t = standby 0.5 ms|83.3|1.75|
|Weather monitoring (lowest power)|Forced|Ultra low power|×1|×1|Off|1/min|1/60|full|
|Elevator / floor change detection|Normal|Standard resolution|×4|×1|4|t = standby 125 ms|7.3|0.67|
|Drop detection|Normal|Low power|×2|×1|Off|t = standby 0.5 ms|125|full|
|Indoor navigation|Normal|Ultra high resolution|×16|×2|16|t = standby 0.5 ms|26.3|0.55|

###### **3.9 Data readout **

To read out data after a conversion, it is strongly recommended to use a burst read and not
address every register individually. This will prevent a possible mix-up of bytes belonging to
different measurements and reduce interface traffic. Data readout is done by starting a burst
read from 0xF7 to 0xFC. The data are read out in an unsigned 20-bit format both for pressure
and for temperature. It is strongly recommended to use the BMP280 API, available from Bosch
Sensortec, for readout and compensation. For details on memory map and interfaces, please
consult chapters 3.12 and 5 respectively.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 20|
|---|---|---|


The timing for data readout in forced mode should be done so that the maximum measurement
times (see chapter 3.8.1) are respected. In normal mode, readout can be done at a speed
similar to the expected data output rate (see chapter 3.8.2). After the values of ‘ut’ and ‘up’ have
been read, the actual pressure and temperature need to be calculated using the compensation
parameters stored in the device. The procedure is elaborated in chapter 3.11.
###### **3.10 Data register shadowing **

In normal mode, measurement timing is not necessarily synchronized to readout. This means
that new measurement results may become available while the user is reading the results from
the previous measurement. In this case, shadowing is performed in order to guarantee data
consistency. Shadowing will only work if all data registers are read in a single burst read.
Therefore, the user must use burst reads if he does not synchronize data readout with the
measurement cycle. Using several independent read commands may result in inconsistent data.

If a new measurement is finished and the data registers are still being read, the new
measurement results are transferred into shadow data registers. The content of shadow
registers is transferred into data registers as soon as the user ends the burst read, even if not all
data registers were read. Reading across several data registers can therefore only be
guaranteed to be consistent within one measurement cycle if a single burst read command is
used. The end of the burst read is marked by the rising edge of CSB pin in SPI case or by the
recognition of a stop condition in I2C case. After the end of the burst read, all user data
registers are updated at once. **3.11 Output compensation **

The BMP280 output consists of the ADC output values. However, each sensing element
behaves differently, and actual pressure and temperature must be calculated using a set of
calibration parameters. The recommended calculation in chapter 3.11.3 uses fixed point
arithmetic. In high-level languages like Matlab™ or LabVIEW™, fixed-point code may not be
well supported. In this case the floating-point code in appendix 8.1 can be used as an
alternative. For 8-bit micro controllers, the variable size may be limited. In this case a simplified
32 bit integer code with reduced accuracy is given in appendix 8.2.

**3.11.1** **Computational requirements**

The table below shows the number of clock cycles needed for compensation calculations on a
32 bit Cortex-M3 micro controller with GCC optimization level –O2. This controller does not
contain a floating point unit, so all floating-point calculations are emulated. Floating point is only
recommended for PC applications where an FPU is present.

Table 16: Com p utational re q uirements for com p ensation formulas

|Compensation of|Number of clock cycles (ARM Cortex-M3)|Col3|Col4|
|---|---|---|---|
||32 bit integer|64 bit integer|Double precision|
|Temperature|~46|–|~2400 7|
|Pressure|~112 8|~1400|~5400 7|



7 Use only recommended for high-level programming languages like Matlab™ or LabVIEW™
8 Use only recommended for 8-bit micro controllers

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 21|
|---|---|---|


**3.11.2** **Trimming parameter readout**
The trimming parameters are programmed into the devices’ non-volatile memory (NVM) during
production and cannot be altered by the customer. Each compensation word is a 16-bit signed
or unsigned integer value stored in two’s complement. As the memory is organized into 8-bit
words, two words must always be combined in order to represent the compensation word. The
8-bit registers are named calib00…calib25 and are stored at memory addresses 0x88…0xA1.
The corresponding compensation words are named dig_T# for temperature compensation
related values and dig_P# for pressure compensation related values. The mapping is shown in
Table 17.

Table 17: Compensation parameter storage, naming and data type

|Register Address LSB / MSB|Register content|Data type|
|---|---|---|
|0x88 / 0x89|dig_T1|unsigned short|
|0x8A / 0x8B|dig_T2|signed short|
|0x8C / 0x8D|dig_T3|signed short|
|0x8E / 0x8F|dig_P1|unsigned short|
|0x90 / 0x91|dig_P2|signed short|
|0x92 / 0x93|dig_P3|signed short|
|0x94 / 0x95|dig_P4|signed short|
|0x96 / 0x97|dig_P5|signed short|
|0x98 / 0x99|dig_P6|signed short|
|0x9A / 0x9B|dig_P7|signed short|
|0x9C / 0x9D|dig_P8|signed short|
|0x9E / 0x9F|dig_P9|signed short|
|0xA0 / 0xA1|reserved|reserved|



**3.11.3** **Compensation formula**
Please note that it is strongly advised to use the API available from Bosch Sensortec to perform
readout and compensation. If this is not wanted, the code below can be applied at the user’s
risk. Both pressure and temperature values are expected to be received in 20 bit format,
positive, stored in a 32 bit signed integer.

The variable t_fine (signed 32 bit) carries a fine resolution temperature value over to the
pressure compensation formula and could be implemented as a global variable.
The data type “BMP280_S32_t” should define a 32 bit signed integer variable type and can
usually be defined as “long signed int”.

The data type “BMP280_U32_t” should define a 32 bit unsigned integer variable type and can
usually be defined as “long unsigned int”.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 22|
|---|---|---|


For best possible calculation accuracy, 64 bit integer support is needed. If this is not possible on
your platform, please see appendix 8.2 for a 32 bit alternative.

The data type “BMP280_S64_t” should define a 64 bit signed integer variable type, which on
most supporting platforms can be defined as “long long signed int”. The revision of the code is
rev.1.1.
```
// Returns temperature in DegC, resolution is 0.01 DegC. Output value of “5123” equals 51.23 DegC. 
// t_fine carries fine temperature as global value
BMP280_S32_t t_fine;
BMP280_S32_t bmp280_compensate_T_int32(BMP280_S32_t adc_T)
{
  BMP280_S32_t var1, var2, T;
  var1 = ((((adc_T>>3) – ((BMP280_S32_t)dig_T1<<1))) * ((BMP280_S32_t)dig_T2)) >> 11;
  var2 = (((((adc_T>>4) – ((BMP280_S32_t)dig_T1)) * ((adc_T>>4) – ((BMP280_S32_t)dig_T1))) >> 12) * 
    ((BMP280_S32_t)dig_T3)) >> 14;
  t_fine = var1 + var2;
  T = (t_fine * 5 + 128) >> 8;
  return T;
}
“”–
// Returns pressure in Pa as unsigned 32 bit integer in Q24.8 format (24 integer bits and 8 fractional bits).
// Output value of “24674867” represents 24674867/256 = 96386.2 Pa = 963.862 hPa
BMP280_U32_t bmp280_compensate_P_int64(BMP280_S32_t adc_P)
{
  BMP280_S64_t var1, var2, p;
  var1 = ((BMP280_S64_t)t_fine) – 128000;
  var2 = var1 * var1 * (BMP280_S64_t)dig_P6;
  var2 = var2 + ((var1*(BMP280_S64_t)dig_P5)<<17);
  var2 = var2 + (((BMP280_S64_t)dig_P4)<<35);
  var1 = ((var1 * var1 * (BMP280_S64_t)dig_P3)>>8) + ((var1 * (BMP280_S64_t)dig_P2)<<12);
  var1 = (((((BMP280_S64_t)1)<<47)+var1))*((BMP280_S64_t)dig_P1)>>33;
  if (var1 == 0)
  {
    return 0; // avoid exception caused by division by zero
  }
  p = 1048576-adc_P;
  p = (((p<<31)-var2)*3125)/var1;
  var1 = (((BMP280_S64_t)dig_P9) * (p>>13) * (p>>13)) >> 25;
  var2 = (((BMP280_S64_t)dig_P8) * p) >> 19;
  p = ((p + var1 + var2) >> 8) + (((BMP280_S64_t)dig_P7)<<4);
  return (BMP280_U32_t)p;
###### **3.12 Calculating pressure and temperature **

```
The following figure shows the detailed algorithm for pressure and temperature measurement.

This algorithm is available to customers as reference C source code (“ BMP28x_ API”) from
Bosch Sensortec and via its sales and distribution partners.

**Please contact your Bosch Sensortec representative for details.**

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 23|
|---|---|---|


BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 24|
|---|---|---|

#### **4. Global memory map and register description **
###### **4.1 General remarks **

All communication with the device is performed by reading from and writing to registers.
Registers have a width of 8 bits. There are several registers which are reserved; they should not
be written to and no specific value is guaranteed when they are read. For details on the
interface, consult chapter 5. **4.2 Memory map **

The memory map is given in Table 18 below. Reserved registers are not shown.

Table 18: Memory map

|Register Name|Address|bit7|bit6|bit5|bit4|bit3|bit2|bit1|bit0|Reset state|
|---|---|---|---|---|---|---|---|---|---|---|
|temp_xlsb|0xFC|temp_xlsb<7:4>||||0|0|0|0|0x00|
|temp_lsb|0xFB|temp_lsb<7:0>||||||||0x00|
|temp_msb|0xFA|temp_msb<7:0>||||||||0x80|
|press_xlsb|0xF9|press_xlsb<7:4>||||0|0|0|0|0x00|
|press_lsb|0xF8|press_lsb<7:0>||||||||0x00|
|press_msb|0xF7|press_msb<7:0>||||||||0x80|
|config|0xF5|t_sb[2:0]|||filter[2:0]||||spi3w_en[0]|0x00|
|ctrl_meas|0xF4|osrs_t[2:0]|||osrs_p[2:0]|||mode[1:0]||0x00|
|status|0xF3|||||measuring[0]|||im_update[0]|0x00|
|reset|0xE0|reset[7:0]||||||||0x00|
|id|0xD0|chip_id[7:0]||||||||0x58|
|calib25...calib00|0xA1…0x88|calibration data||||||||individual|


|Reserved registers|Calibration data|Control registers|Data registers|Status registers|Revision|Reset|
|---|---|---|---|---|---|---|
|do not write|read only|read / write|read only|read only|read only|write only| **4.3 Register description **

**4.3.1** **Register 0xD0** ***“id”***
The *“id”* register contains the chip identification number chip_id[7:0], which is 0x58. This number
can be read as soon as the device finished the power-on-reset.

**4.3.2** **Register 0xE0** ***“reset”***
The *“reset”* register contains the soft reset word reset[7:0]. If the value 0xB6 is written to the
register, the device is reset using the complete power-on-reset procedure. Writing other values
than 0xB6 has no effect. The readout value is always 0x00.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 25|
|---|---|---|


**4.3.3** **Register 0xF3** ***“status”***
The *“status”* register contains two bits which indicate the status of the device.

Table 19: Register 0xF3 *“status”*

**4.3.4** **Register 0xF4** ***“ctrl_meas”***
The *“ctrl_meas”* register sets the data acquisition options of the device.

Table 20: Register 0xF4 *“ctrl_meas”*

Table 21: register settings *osrs_p*

|Register 0xF3 “status”|Name|Description|
|---|---|---|
|Bit 3|measuring[0]|Automatically set to ‘1’ whenever a conversion is running and back to ‘0’ when the results have been transferred to the data registers.|
|Bit 0|im_update[0]|Automatically set to ‘1’ when the NVM data are being copied to image registers and back to ‘0’ when the copying is done. The data are copied at power-on-reset and before every conversion.|


|Register 0xF4 “ctrl_meas”|Name|Description|
|---|---|---|
|Bit 7, 6, 5|osrs_t[2:0]|Controls oversampling of temperature data. See chapter 3.3.2 for details.|
|Bit 4, 3, 2|osrs_p[2:0]|Controls oversampling of pressure data. See chapter 3.3.1 for details.|
|Bit 1, 0|mode[1:0]|Controls the power mode of the device. See chapter 3.6 for details.|


|osrs_p[2:0]|Pressure oversampling|
|---|---|
|000|Skipped (output set to 0x80000)|
|001|oversampling ×1|
|010|oversampling ×2|
|011|oversampling ×4|
|100|oversampling ×8|
|101, Others|oversampling ×16|



BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 26|
|---|---|---|


Table 22: register settings *osrs_t*

|osrs_t[2:0]|Temperature oversampling|
|---|---|
|000|Skipped (output set to 0x80000)|
|001|oversampling ×1|
|010|oversampling ×2|
|011|oversampling ×4|
|100|oversampling ×8|
|101, 110, 111|oversampling ×16|



**4.3.5** **Register 0xF5** ***“config”***
The *“config”* register sets the rate, filter and interface options of the device. Writes to the “config”
register in normal mode may be ignored. In sleep mode writes are not ignored.

Table 23: Register 0xF5 *“config”*

**4.3.6** **Register 0xF7…0xF9** ***“press” (_msb, _lsb, _xlsb)***

|Register 0xF5 “config”|Name|Description|
|---|---|---|
|Bit 7, 6, 5|t_sb[2:0]|Controls inactive duration t in normal mode. See standby chapter 3.6.3 for details.|
|Bit 4, 3, 2|filter[2:0]|Controls the time constant of the IIR filter. See chapter 3.3.3 for details.|
|Bit 0|spi3w_en[0]|Enables 3-wire SPI interface when set to ‘1’. See chapter 5.3 for details.|

The *“press”* register contains the raw pressure measurement output data up[19:0]. For details
on how to read out the pressure and temperature information from the device, please consult
chapter3.9.

Table 24: Register 0xF7 … 0xF9 *“press”*

|Register 0xF7-0xF9 “press”|Name|Description|
|---|---|---|
|0xF7|press_msb[7:0]|Contains the MSB part up[19:12] of the raw pressure measurement output data.|
|0xF8|press_lsb[7:0]|Contains the LSB part up[11:4] of the raw pressure measurement output data.|
|0xF9 (bit 7, 6, 5, 4)|press_xlsb[3:0]|Contains the XLSB part up[3:0] of the raw pressure measurement output data. Contents depend on temperature resolution, see table 5.|



BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 27|
|---|---|---|


**4.3.7** **Register 0xFA…0xFC** ***“temp” (_msb, _lsb, _xlsb)***
The *“temp”* register contains the raw temperature measurement output data ut[19:0]. For details
on how to read out the pressure and temperature information from the device, please consult
chapter 3.9.

Table 25: Register 0xFA … 0xFC *“temp”*

|Register 0xF7-0xF9 “press”|Name|Description|
|---|---|---|
|0xFA|temp_msb[7:0]|Contains the MSB part ut[19:12] of the raw temperature measurement output data.|
|0xFB|temp_lsb[7:0]|Contains the LSB part ut[11:4] of the raw temperature measurement output data.|
|0xFC (bit 7, 6, 5, 4)|temp_xlsb[3:0]|Contains the XLSB part ut[3:0] of the raw temperature measurement output data. Contents depend on pressure resolution, see Table 4.|



BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 28|
|---|---|---|


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 29|
|---|---|---|


is the same as BMP180’s I²C address. The SDO pin cannot be left floating; if left floating, the
I²C address will be undefined.

The I²C interface uses the following pins:

  - SCK: serial clock (SCL)

  - SDI: data (SDA)

  - SDO: Slave address LSB (GND = ‘0’, V DDIO = ‘1’)
CSB must be connected to V DDIO to select I²C interface. SDI is bi-directional with open drain to
GND: it must be externally connected to V DDIO via a pull up resistor. Refer to chapter 6 for
connection instructions.

The following abbreviations will be used in the I²C protocol figures:

  - S Start

  - P Stop

  - ACKS Acknowledge by slave

  - ACKM Acknowledge by master

  - NACKM Not acknowledge by master

**5.2.1** **I²C write**

Writing is done by sending the slave address in write mode (RW = ‘0’), resulting in slave
address 111011X0 (‘X’ is determined by state of SDO pin. Then the master sends pairs of
register addresses and register data. The transaction is ended by a stop condition. This is
depicted in Figure 7.

Figure 7: I²C multiple byte write (not auto-incremented)

|Col1|Col2|Col3|Control byte|Col5|Data byte|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Slave Address|RW|ACKS|Register address (A0h)|ACKS|Register data - address A0h|ACKS||
|1 1 1 0 1 1 X 0|||1 0 1 0 0 0 0 0||bit7 bit6 bit5 bit4 bit3 bit2 bit1 bit0|||
||||Control byte|||||
||||Control byte||Data byte|||
||||Register address (A1h)|ACKS|Register data - address A1h|ACKS|Stop|
||||1 0 1 0 0 0 0 1||bit7 bit6 bit5 bit4 bit3 bit2 bit1 bit0||P|



**5.2.2** **I²C read**

To be able to read registers, first the register address must be sent in write mode (slave address
111011X0). Then either a stop or a repeated start condition must be generated. After this the
slave is addressed in read mode (RW = ‘1’) at address 111011X1, after which the slave sends
out data from auto-incremented register addresses until a NOACKM and stop condition occurs.
This is depicted in Figure 8, where two bytes are read from register 0xF6 and 0xF7.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 30|
|---|---|---|

|Start Slave Address RW ACKS S 1 1 1 0 1 1 X 0 Start Slave Address RW ACKS S 1 1 1 0 1 1 X 1|Col2|Col3|Col4|Control byte|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||Slave Address|RW|ACKS|Register address (F6h)|ACKS||||
||1 1 1 0 1 1 X 0|||1 1 1 1 0 1 1 0|||||
|||||Data byte|||||
|||||Data byte||Data byte|||
||Slave Address|RW|ACKS|Register data - address F6h|ACKM|Register data - address F7h|NOACKM|Stop|
||1 1 1 0 1 1 X 1|||bit7 bit6 bit5 bit4 bit3 bit2 bit1 bit0||bit7 bit6 bit5 bit4 bit3 bit2 bit1 bit0||P|


Figure 8: I²C multiple byte read
###### **5.3 SPI interface **

The SPI interface is compatible with SPI mode ‘00’ (CPOL = CPHA = ‘0’) and mode ‘11’ (CPOL
= CPHA = ‘1’). The automatic selection between mode ‘00’ and ‘11’ is determined by the value
of SCK after the CSB falling edge.

The SPI interface has two modes: 4-wire and 3-wire. The protocol is the same for both. The 3wire mode is selected by setting ‘1’ to the register spi3w_en. The pad SDI is used as a data pad
in 3-wire mode.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 31|
|---|---|---|


The SPI interface uses the following pins:

  CSB: chip select, active low

  - SCK: serial clock

  - SDI: serial data input; data input/output in 3-wire mode

  SDO: serial data output; hi-Z in 3-wire mode
Refer to chapter 6 for connection instructions.

CSB is active low and has an integrated pull-up resistor. Data on SDI is latched by the device at
SCK rising edge and SDO is changed at SCK falling edge. Communication starts when CSB
goes to low and stops when CSB goes to high; during these transitions on CSB, SCK must be
stable. The SPI protocol is shown in Figure 9. For timing details, please review Table 28.

CSB

SCK

SDI

SDO

|RW AD6 AD5 AD4 AD3 AD2 AD1 AD0 DI7 DI6 DI5 DI4 DI3 DI2 DI1 DI0 DO7 DO6 DO5 DO4 DO3 DO2 DO1 DO0 tri-s|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||DI7||
||||||
||||||
||||DO7||



Figure 9: SPI protocol (shown for mode ‘11’ in 4-wire configuration)

In SPI mode, only 7 bits of the register addresses are used; the MSB of register address is not
used and replaced by a read/write bit (RW = ‘0’ for write and RW = ‘1’ for read).
Example: address 0xF7 is accessed by using SPI register address 0x77. For write access, the
byte 0x77 is transferred, for read access, the byte 0xF7 is transferred.

**5.3.1** **SPI write**

Writing is done by lowering CSB and sending pairs control bytes and register data. The control
bytes consist of the SPI register address (= full register address without bit 7) and the write
command (bit7 = RW = ‘0’). Several pairs can be written without raising CSB. The transaction is
ended by a raising CSB. The SPI write protocol is depicted in Figure 10.

Figure 10: SPI multiple byte write (not auto-incremented)

|Col1|Control byte|Col3|Data byte|Control byte|Col6|Data byte|Col8|
|---|---|---|---|---|---|---|---|
|Start|RW|Register address (F4h)|Data register - address F4h|RW|Register address (F5h)|Data register - adress F5h|Stop|
|CSB = 0|0|1 1 1 0 1 0 0|bit7 bit6 bit5 bit4 bit3 bit2 bit1 bit0|0|1 1 1 0 1 0 1|bit7 bit6 bit5 bit4 bit3 bit2 bit1 bit0|CSB = 1|



**5.3.2** **SPI read**

Reading is done by lowering CSB and first sending one control byte. The control bytes consist
of the SPI register address (= full register address without bit 7) and the read command (bit 7 =
RW = ‘1’). After writing the control byte, data is sent out of the SDO pin (SDI in 3-wire mode);
the register address is automatically incremented. The SPI read protocol is shown in Figure 11.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 32|
|---|---|---|

|Col1|Control byte|Col3|Data byte|Data byte|Col6|
|---|---|---|---|---|---|
|Start|RW|Register address (F6h)|Data register - address F6h|Data register - address F7h|Stop|
|CSB = 0|1|1 1 1 0 1 1 0|bit15 bit14 bit13 bit12 bit11 bit10 bit9 bit8|bit7 bit6 bit5 bit4 bit3 bit2 bit1 bit0|CSB = 1|


Figure 11: SPI multiple byte read
###### **5.4 Interface parameter specification **

**5.4.1** **General interface parameters**
The general interface parameters are given in Table 26 below.

Table 26: interface parameters

**5.4.2** **I²C timings**
For I²C timings, the following abbreviations are used:

  - “S&F mode” = standard and fast mode

  “HS mode” = high speed mode

  Cb = bus capacitance on SDA line

All other naming refers to I²C specification 2.1 (January 2000).

The I²C timing diagram is shown in
Figure 12. The corresponding values are given in Table 27.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.

|Parameter|Symbol|Condition|Min|Typ|Max|Units|
|---|---|---|---|---|---|---|
|Input – low level|Vil_si|V =1.2V to 3.6V DDIO|||0.2 * V DDIO|V|
|Input – high level|Vih_si|V =1.2V to 3.6V DDIO|0.8 * V DDIO|||V|
|Output – low level for I2C|Vol_SDI|V =1.62V, iol=3 mA DDIO|||0.2 * V DDIO|V|
|Output – low level for I2C|Vol_SDI _1.2|V =1.20V, iol=3 mA DDIO|||0.23 * V DDIO|V|
|Output – low level|Vol_SD O|V =1.62V, iol=1 mA DDIO|||0.2 * V DDIO|V|
|Output – low level|Vol_SD O_1.2|V =1.20V, iol=1 mA DDIO|||0.23 * V DDIO|V|
|Output – high level|Voh|V =1.62V, ioh=1 DDIO mA (SDO, SDI)|0.8 * V DDIO|||V|
|Output – high level|Voh_1.2|V =1.2V, ioh=1 mA DDIO (SDO, SDI)|0.6 * V DDIO|||V|
|Pull-up resistor|Rpull|Internal pull-up resistance to V DDIO|70|120|190|kΩ|
|I2C bus load capacitor|Cb|On SDI and SCK|||400|pF|


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 33|
|---|---|---|


SDI

t LOW t f

SCK

SDI

t SUSTA t SUSTO

Figure 12: I²C timing diagram

Table 27: I²C timings

The above-mentioned I2C specific timings correspond to the following internal added delays:

  Input delay between SDI and SCK inputs: SDI is more delayed than SCK by typically
100 ns in Standard and Fast Modes and by typically 20 ns in High Speed Mode.

  Output delay from SCK falling edge to SDI output propagation is typically 140 ns in
Standard and Fast Modes and typically 70 ns in High Speed Mode.

**5.4.3** **SPI timings**
The SPI timing diagram is in Figure 13, while the corresponding values are given in Table 28.
All timings apply both to 4- and 3-wire SPI.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.

|Parameter|Symbol|Condition|Min|Typ|Max|Units|
|---|---|---|---|---|---|---|
|SDI setup time|t SU;DAT|S&F Mode HS mode|160 30|||ns ns|
|SDI hold time|t HD;DAT|S&F Mode, Cb≤100 pF S&F Mode, Cb≤400 pF HS mode, Cb≤100 pF HS mode, Cb≤400 pF|80 90 18 24||115 150|ns ns ns ns|
|SCK low pulse|t LOW|HS mode, Cb≤100 pF V = 1.62 V DDIO|160|||ns|
|SCK low pulse|t LOW|HS mode, Cb≤100 pF V = 1.2 V DDIO|210|||ns|


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 34|
|---|---|---|


T_setup_csb


T_hold_csb


CSB

SCK

SDI

T_setup_sdi T_hold_sdi

SDO

T_delay_sdo

Figure 13: SPI timing diagram

Table 28: SPI timings

|Col1|Col2|Col3|Col4|
|---|---|---|---|


|Parameter|Symbol|Condition|Min|Typ|Max|Units|
|---|---|---|---|---|---|---|
|SPI clock input frequency|F_spi||0||10|MHz|
|SCK low pulse|T_low_sck||20|||ns|
|SCK high pulse|T_high_sck||20|||ns|
|SDI setup time|T_setup_sdi||20|||ns|
|SDI hold time|T_hold_sdi||20|||ns|
|SDO output delay|T_delay_sdo|25pF load, V =1.6V min DDIO|||30|ns|
|SDO output delay|T_delay_sdo|25pF load, V =1.2V min DDIO|||40|ns|
|CSB setup time|T_setup_csb||20|||ns|
|CSB hold time|T_hold_csb||20|||ns|



BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 35|
|---|---|---|

|Pin|Name|I/O Type|Description|Connect to|Col6|Col7|
|---|---|---|---|---|---|---|
|||||SPI 4W|SPI 3W|I²C|
|1|GND|Supply|Ground|GND|||
|2|CSB|In|Chip select|CSB|CSB|V DDIO|
|3|SDI|In/Out|Serial data input|SDI|SDI/SDO|SDA|
|4|SCK|In|Serial clock input|SCK|SCK|SCL|
|5|SDO|In/Out|Serial data output|SDO|DNC|GND for default address|
|6|V DDIO|Supply|Digital interface supply|V DDIO|||
|7|GND|Supply|Ground|GND|||
|8|V DD|Supply|Analog supply|V DD|||


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 36|
|---|---|---|

|Col1|V DD|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
|||||


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 37|
|---|---|---|

|Col1|V DD|Col3|
|---|---|---|
||||
||||


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 38|
|---|---|---|

###### **6.4 Connection diagram I [2] C **

I2C address bit 0
GND: '0'; V DDIO : '1'


SDA

SCL



|Col1|V DD|Col3|V DDIO|
|---|---|---|---|
|||||
|||||
|||||
|||||


Figure 17: I²C connection diagram (Pin1 marking indicated)

Notes:

  - The recommended value for C 1, C 2 is 100 nF.

  - A direct connection between CSB and V DDIO is recommended. If CSB is detected as low
during startup, the interface will be locked into SPI mode. See chapter 5.1.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 39|
|---|---|---|

#### **7. Package, reel and environment **
###### **7.1 Outline dimensions **

The sensor housing is an 8-pin metal-lid LGA 2.0 × 2.5× 0.95 mm [3] package. Its dimensions are
depicted in Figure 18.

Figure 18: Package outline dimensions for top, bottom and side view

Note: General tolerances are ±50 µm (linear) and ±1° µm (angular)

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 40|
|---|---|---|

###### **7.2 Landing pattern recommendation **

For the design of the landing pattern, the following dimensioning is recommended:

|Col1|8|
|---|---|


|Col1|7|
|---|---|


|2|Col2|
|---|---|


|Col1|6|
|---|---|


|3|Col2|
|---|---|


|4|Col2|
|---|---|


|Col1|Col2|Col3|Col4|Col5|0.5|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||0.5||||
|2.50|0.65||8 7|1 2|||||
||||||1|||0.35|
||||||||||
||||6 5|3 4||0.325||0.325|
||||5||||||
||||||||||
||||0.55 2.0||||||



Figure 19: Recommended landing pattern (top view); dimensions are in mm

Note: red areas demark exposed PCB metal pads.

- In case of a solder mask defined (SMD) PCB process, the land dimensions should be
defined by solder mask openings. The underlying metal pads are larger than these openings.

- In case of a non solder mask defined (NSMD) PCB process, the land dimensions should
be defined in the metal layer. The mask openings are larger than the these metal pads.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 41|
|---|---|---|

###### **7.3 Marking **

**7.3.1** **Mass production devices**

Table 30: Marking of mass production samples

**7.3.2** **Engineering samples**

Table 31: Marking of engineering samples

|Labeling|Name|Symbol|Remark|
|---|---|---|---|
|CCC TL |Lot counter|CCC|3 alphanumeric digits, variable to generate mass production trace-code|
||Product number|T|1 alphanumeric digit, fixed to identify product type, T = “K” “K” is associated with the product BMP280 (part number 0 273 300 354)|
||Sub-con ID|L|1 alphanumeric digit, variable to entify sub-con (L = “P”, L = “U”, L = “N”or L = “W”)|
||Orientation marker||Vent hole|


|Labeling|Name|Symbol|Remark|
|---|---|---|---|
|XXN CC |Eng. Sample ID|N|1 alphanumeric digit, fixed to identify engineering sample, N = “ * ” or “e” or “E”|
||Sample ID|XX|2 alphanumeric digits, variable to generate trace-code|
||Counter ID|CC|2 alphanumeric digits, variable to generate trace-code|
||Orientation marker||Vent hole|



BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 42|
|---|---|---|

###### **7.4 Soldering guidelines **

The moisture sensitivity level of the BMP280 sensors corresponds to JEDEC Level 1, see also:

 IPC/JEDEC J-STD-020C “Joint Industry Standard: Moisture/Reflow Sensitivity

Classification for non-hermetic Solid State Surface Mount Devices”

 IPC/JEDEC J-STD-033A “Joint Industry Standard: Handling, Packing, Shipping and Use of

Moisture/Reflow Sensitive Surface Mount Devices”.

The sensor fulfils the lead-free soldering requirements of the above-mentioned IPC/JEDEC
standard, i.e. reflow soldering with a peak temperature up to 260°C. The minimum height of the
solder after reflow shall be at least 50µm. This is required for good mechanical decoupling
between the sensor device and the printed circuit board (PCB).

Figure 20: Soldering profile

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 43|
|---|---|---|


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 44|
|---|---|---|

###### **7.6 Mounting and assembly recommendations **

In addition to “Handling, soldering & mounting instructions BMP280”, the following
recommendations should be taken into consideration when mounting a pressure sensor on a
printed-circuit board (PCB):

  - The clearance above the metal lid shall be 0.1mm at minimum.

  For the device housing appropriate venting needs to be provided in case the ambient
pressure shall be measured.

  Liquids shall not come into direct contact with the device.

  During operation the sensor chip is sensitive to light, which can influence the accuracy of
the measurement (photo-current of silicon). The position of the vent hole minimizes the
light exposure of the sensor chip. Nevertheless, BST recommends to avoid the
exposure of BMP280 to strong light sources.

  Soldering may not be done using vapor phase processes since the sensor might be
damaged. **7.7 Environmental safety **

**7.7.1** **RoHS**

The BMP280 sensor meets the requirements of the EC restriction of hazardous substances
(RoHS) directive, see also:

*Directive 2011/65/EU of the European Parliament and of the Council of 8 June 2011 on*
*the restriction of the use of certain hazardous substances in electrical and electronic*
*equipment.*

**7.7.2** **Halogen content**
The BMP280 is halogen-free. For more details on the analysis results please contact your
Bosch Sensortec representative.

**7.7.3** **Internal package structure**
Within the scope of Bosch Sensortec’s ambition to improve its products and secure the mass
product supply, Bosch Sensortec qualifies additional sources (e.g. 2 [nd] source) for the LGA
package of the BMP280.

While Bosch Sensortec took care that all of the technical packages parameters are described
above are 100% identical for all sources, there can be differences in the chemical content and
the internal structural between the different package sources.

However, as secured by the extensive product qualification process of Bosch Sensortec, this
has no impact to the usage or to the quality of the BMP280 product.
#### **8. Appendix 1: Computation formulae for 32 bit systems **
###### **8.1 Compensation formula in floating point **

Please note that it is strongly advised to use the API available from Bosch Sensortec to perform
readout and compensation. If this is not wanted, the code below can be applied at the user’s
risk. Both pressure and temperature values are expected to be received in 20 bit format,
positive, stored in a 32 bit signed integer.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 45|
|---|---|---|


The variable t_fine (signed 32 bit) carries a fine resolution temperature value over to the
pressure compensation formula and could be implemented as a global variable.

The data type “BMP280_S32_t” should define a 32 bit signed integer variable type and could
usually be defined as “long signed int”. The revision of the code is rev.1.1.
```
// Returns temperature in DegC, double precision. Output value of “51.23” equals 51.23 DegC.
// t_fine carries fine temperature as global value
BMP280_S32_t t_fine;
double bmp280_compensate_T_double(BMP280_S32_t adc_T)
{
  double var1, var2, T;
  var1 = (((double)adc_T)/16384.0 – ((double)dig_T1)/1024.0) * ((double)dig_T2);
  var2 = ((((double)adc_T)/131072.0 – ((double)dig_T1)/8192.0) *
    (((double)adc_T)/131072.0 – ((double) dig_T1)/8192.0)) * ((double)dig_T3);
  t_fine = (BMP280_S32_t)(var1 + var2);
  T = (var1 + var2) / 5120.0;
  return T;
}
// Returns pressure in Pa as double. Output value of “96386.2” equals 96386.2 Pa = 963.862 hPa
double bmp280_compensate_P_double(BMP280_S32_t adc_P)
{
  double var1, var2, p;
  var1 = ((double)t_fine/2.0) – 64000.0;
  var2 = var1 * var1 * ((double)dig_P6) / 32768.0;
  var2 = var2 + var1 * ((double)dig_P5) * 2.0;
  var2 = (var2/4.0)+(((double)dig_P4) * 65536.0);
  var1 = (((double)dig_P3) * var1 * var1 / 524288.0 + ((double)dig_P2) * var1) / 524288.0;
  var1 = (1.0 + var1 / 32768.0)*((double)dig_P1);
  if (var1 == 0.0)
  {
    return 0; // avoid exception caused by division by zero
  }
  p = 1048576.0 – (double)adc_P;
  p = (p – (var2 / 4096.0)) * 6250.0 / var1;
  var1 = ((double)dig_P9) * p * p / 2147483648.0;
  var2 = p * ((double)dig_P8) / 32768.0;
  p = p + (var1 + var2 + ((double)dig_P7)) / 16.0;
  return p;
}
###### **8.2 Compensation formula in 32 bit fixed point **

```
Please note that it is strongly advised to use the API available from Bosch Sensortec to perform
readout and compensation. If this is not wanted, the code below can be applied at the user’s
risk. Both pressure and temperature values are expected to be received in 20 bit format,
positive, stored in a 32 bit signed integer.

The variable t_fine (signed 32 bit) carries a fine resolution temperature value over to the
pressure compensation formula and could be implemented as a global variable.
The data type “BMP280_S32_t” should define a 32 bit signed integer variable type and can
usually be defined as “long signed int”.

The data type “BMP280_U32_t” should define a 32 bit unsigned integer variable type and can
usually be defined as “long unsigned int”.
Compensating the pressure value with 32 bit integer has an accuracy of typically 1 Pa (1sigma). At very high filter levels this adds a noticeable amount of noise to the output values and
reduces their resolution.
```
// Returns temperature in DegC, resolution is 0.01 DegC. Output value of “5123” equals 51.23 DegC. 
// t_fine carries fine temperature as global value
BMP280_S32_t t_fine;
BMP280_S32_t bmp280_compensate_T_int32(BMP280_S32_t adc_T)
{
  BMP280_S32_t var1, var2, T;

```
BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 46|
|---|---|---|

```
  var1 = ((((adc_T>>3) – ((BMP280_S32_t)dig_T1<<1))) * ((BMP280_S32_t)dig_T2)) >> 11;
  var2 = (((((adc_T>>4) – ((BMP280_S32_t)dig_T1)) * ((adc_T>>4) – ((BMP280_S32_t)dig_T1))) >> 12) * 
    ((BMP280_S32_t)dig_T3)) >> 14;
  t_fine = var1 + var2;
  T = (t_fine * 5 + 128) >> 8;
  return T;
}
// Returns pressure in Pa as unsigned 32 bit integer. Output value of “96386” equals 96386 Pa = 963.86 hPa
BMP280_U32_t bmp280_compensate_P_int32(BMP280_S32_t adc_P)
{
  BMP280_S32_t var1, var2;
  BMP280_U32_t p;
  var1 = (((BMP280_S32_t)t_fine)>>1) – (BMP280_S32_t)64000;
  var2 = (((var1>>2) * (var1>>2)) >> 11 ) * ((BMP280_S32_t)dig_P6);
  var2 = var2 + ((var1*((BMP280_S32_t)dig_P5))<<1);
  var2 = (var2>>2)+(((BMP280_S32_t)dig_P4)<<16);
  var1 = (((dig_P3 * (((var1>>2) * (var1>>2)) >> 13 )) >> 3) + ((((BMP280_S32_t)dig_P2) * var1)>>1))>>18;
  var1 =((((32768+var1))*((BMP280_S32_t)dig_P1))>>15);
  if (var1 == 0)
  {
    return 0; // avoid exception caused by division by zero
  }
  p = (((BMP280_U32_t)(((BMP280_S32_t)1048576)-adc_P)-(var2>>12)))*3125;
  if (p < 0x80000000) 
  {
    p = (p << 1) / ((BMP280_U32_t)var1);
  } 
  else
  {
    p = (p / (BMP280_U32_t)var1) * 2;
  }
  var1 = (((BMP280_S32_t)dig_P9) * ((BMP280_S32_t)(((p>>3) * (p>>3))>>13)))>>12;
  var2 = (((BMP280_S32_t)(p>>2)) * ((BMP280_S32_t)dig_P8))>>13;
  p = (BMP280_U32_t)((BMP280_S32_t)p + ((var1 + var2 + dig_P7) >> 4));
  return p;
}

```
BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 47|
|---|---|---|

#### **9. Legal disclaimer **
###### **9.1 Engineering samples **

Engineering Samples are marked with an asterisk (*) or (e) or (E). Samples may vary from the
valid technical specifications of the product series contained in this data sheet. They are
therefore not intended or fit for resale to third parties or for use in end products. Their sole
purpose is internal client testing. The testing of an engineering sample may in no way replace
the testing of a product series. Bosch Sensortec assumes no liability for the use of engineering
samples. The Purchaser shall indemnify Bosch Sensortec from all claims arising from the use of
engineering samples. **9.2 Product use **

Bosch Sensortec products are developed for the consumer goods industry. They are not
designed or approved for use in military applications, life-support appliances, safety-critical
automotive applications and devices or systems where malfunctions of these products can
reasonably be expected to result in personal injury. They may only be used within the
parameters of this product data sheet.
The resale and/or use of products are at the Purchaser’s own risk and the Purchaser’s own
responsibility.
The Purchaser shall indemnify Bosch Sensortec from all third party claims arising from any
product use not covered by the parameters of this product data sheet or not approved by Bosch
Sensortec and reimburse Bosch Sensortec for all costs in connection with such claims.
The Purchaser accepts the responsibility to monitor the market for the purchased products,
particularly with regard to product safety, and inform Bosch Sensortec without delay of any
security relevant incidents. **9.3 Application examples and hints **

With respect to any examples or hints given herein, any typical values stated herein and/or any
information regarding the application of the device, Bosch Sensortec hereby disclaims any and
all warranties and liabilities of any kind, including without limitation warranties of noninfringement of intellectual property rights or copyrights of any third party. The information given
in this document shall in no event be regarded as a guarantee of conditions or characteristics.
They are provided for illustrative purposes only and no evaluation regarding infringement of
intellectual property rights or copyrights or regarding functionality, performance or error has
been made.

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 48|
|---|---|---|

#### **10. Document history and modification **

Bosch Sensortec GmbH

Gerhard-Kindler-Strasse 8

72770 Reutlingen / Germany

contact@bosch-sensortec.com

[www.bosch-sensortec.com](http://www.bosch-sensortec.com/)

Modifications reserved | Printed in Germany

|Rev. No|Chapter|Description of modification/changes|Date|
|---|---|---|---|
|0.1||Document creation|2012-08-06|
|||||
|1.0|9.2|Change of product use|2013-11-26|
||Table 2|Update of min/max data (only for restricted version)||
|||Added comment on the sampling rate||
|1.1|1, 3.3.1|Changed value for resolution, values for osrs_p settings changed|2014-02-10|
||5.2|Changed sentence and added drawing|2014-02-18|
||3.7|Added max values for current consumption|2014-05-08|
|1.11|4.5.3|Modified write in normal mode|2014-06-25|
||5.2|Modified SDI/SCK ESD drawing||
|1.12|1|Changed min/max values for standby current, only valid for 25 °C|2014-07-12|
||Table 1|Pressure resolution 0.16Pa|2014-07-12|
|1.13|Page 2|New technical reference codes added|2014-11-12|
||7.3|New details about laser marking added||
|1.14|Table 6|Changed contents of table|2015-05-04|
||Page 1|Removed TRC 0 273 300 354 & 0273 300 391||
||Page 44|Updated RoHS directive to 2011/65/EU effective 8 June 2011|2015-05-07|



Specifications subject to change without notice

Document number: BST-BMP280-DS001-11

Revision_1.14_052015

BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

|Col1|Datasheet BMP280 Digital Pressure Sensor|Page 49|
|---|---|---|


BST-BMP280-DS001-11 | Revision 1.14 | May 2015 Bosch Sensortec

© Bosch Sensortec GmbH reserves all rights even in the event of industrial property rights. We reserve all rights of disposal such as copying and passing on to

third parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
Note: Specifications within this document are subject to change without notice. Not intended for publication.


-----

