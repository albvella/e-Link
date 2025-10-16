
## Page 1
SIM7000 Series
Hardware Design
SIMCom Wireless Solutions Limited
Building B, SIM Technology Building, No.633, Jinzhong Road
Changning District, Shanghai P.R.China
Tel: 86-21-31575100
support@simcom.com
www.simcom.com
LPWA Module

---

## Page 2
SIM7000 Series Hardware Design V1.09
www.simcom.com
2/69
Document Title:
SIM7000 _Hardware Design
Version:
V1.09
Date:
2021-04-19
Status:
Released
GENERAL NOTES
SIMCOM OFFERS THIS INFORMATION AS A SERVICE TO ITS CUSTOMERS, TO SUPPORT
APPLICATION AND ENGINEERING EFFORTS THAT USE THE PRODUCTS DESIGNED BY SIMCOM.
THE INFORMATION PROVIDED IS BASED UPON REQUIREMENTS SPECIFICALLY PROVIDED TO
SIMCOM BY THE CUSTOMERS. SIMCOM HAS NOT UNDERTAKEN ANY INDEPENDENT SEARCH
FOR ADDITIONAL RELEVANT INFORMATION, INCLUDING ANY INFORMATION THAT MAY BE IN THE
CUSTOMER’S
POSSESSION.
FURTHERMORE,
SYSTEM
VALIDATION
OF
THIS
PRODUCT
DESIGNED BY SIMCOM WITHIN A LARGER ELECTRONIC SYSTEM REMAINS THE RESPONSIBILITY
OF
THE CUSTOMER
OR THE
CUSTOMER’S SYSTEM
INTEGRATOR.
ALL SPECIFICATIONS
SUPPLIED HEREIN ARE SUBJECT TO CHANGE.
COPYRIGHT
THIS DOCUMENT CONTAINS PROPRIETARY TECHNICAL INFORMATION WHICH IS THE PROPERTY
OF SIMCOM WIRELESS SOLUTIONS LIMITED COPYING, TO OTHERS AND USING THIS DOCUMENT,
ARE FORBIDDEN WITHOUT EXPRESS AUTHORITY BY SIMCOM. OFFENDERS ARE LIABLE TO THE
PAYMENT OF INDEMNIFICATIONS. ALL RIGHTS RESERVED
BY SIMCOM IN THE PROPRIETARY
TECHNICAL INFORMATION ，INCLUDING BUT NOT LIMITED TO REGISTRATION GRANTING OF A
PATENT , A UTILITY MODEL OR DESIGN. ALL SPECIFICATION SUPPLIED HEREIN ARE SUBJECT TO
CHANGE WITHOUT NOTICE AT ANY TIME.
SIMCom Wireless Solutions Limited
Building B, SIM Technology Building, No.633 Jinzhong Road, Changning District, Shanghai P.R.China
Tel: +86 21 31575100
Email: simcom@simcom.com
For more information, please visit:
https://www.simcom.com/download/list-863-en.html
For technical support, or to report documentation errors, please visit:
https://www.simcom.com/ask/or email to: support@simcom.com
Copyright © 2020 SIMCom Wireless Solutions Limited All Rights Reserved.

---

## Page 3
SIM7000 Series Hardware Design V1.09
www.simcom.com
3/69
Version History
Date
Version
Description of change
Author
2017-05-23
1.00
Original
TuHongjun
Li Ya
2017-07-13
1.01
1. Update the data of Table 1, Table 23 and Table
24
2. Update figure 3 and figure 4
Li Ya
2017-08-29
V1.02
1. Update the description of RI and DTR.
2. Update the description of voltage monitor.
3. Update the description of power off function.
4. Update the description of the remarks of some
nonsupport function in existingsoftware, such as
PCM, I2C,SIM_DET.
5. Update the mechanical information.
6. Update the data of Table 1.
7. Update the data of Table 32.
8. Add ESD testing condition.
TuHongjun
2017-09-18
V1.03
Update the data of Table 32.
TuHongjun
2018-1-31
V1.04
1.
Change the description GSM to GPRS and
EDGE.
2.
Update the table related documents.
3.
Update thepictureblock diagram.
4.
Update the picturePin assignment overview.
5.
Add comment for Galileo.
6.
Deletetherecommendedtype
of
SIM
card
socket.
7.
Update the baking information.
8.
Add the PSM and e-DRX information.
9.
Add the design check list information.
10. Add the table 41and table 42Add recommend
SMT stencil;
TuHongjun
Li ya
2018-12-24
V1.05
e-DRX Update
TuHongjun
2020-04-23
V1.06
Update document format
PanQiMing
2020-05-15
V1.07
Update format, Chinese and English corresponding
problem modification
ZhangShuai
2021-04-02
V1.08
Update sensitivity
LiMeihao
2021-04-19
V1.09
Update supporting band
LiMeihao

---

## Page 4
SIM7000 Series Hardware Design V1.09
www.simcom.com
4/69
Contents
1
Introduction...................................................................................................................................................9
1.1
Product Outline........................................................................................................................................... 9
1.2
Hardware Interface Overview.................................................................................................................10
1.3
Hardware Block Diagram........................................................................................................................10
1.4
Functional Overview.................................................................................................................................11
2
Package Information................................................................................................................................ 13
2.1
Pin Assignment Overview.......................................................................................................................13
2.2
Pin Description..........................................................................................................................................15
2.3
Mechanical Information........................................................................................................................... 18
2.4
Footprint Recommendation.................................................................................................................... 19
3
Interface Application................................................................................................................................20
3.1
Power Supply............................................................................................................................................20
3.1.1
Power Supply Design Guide..........................................................................................................21
3.1.2
Recommended Power Supply Circuit.......................................................................................... 22
3.1.3
Voltage Monitor................................................................................................................................ 22
3.2
Power on/Power off/Reset Function..................................................................................................... 23
3.2.1
Power on........................................................................................................................................... 23
3.2.2
Power off............................................................................................................................................24
3.2.3
Reset Function................................................................................................................................. 26
3.3
UART Interface......................................................................................................................................... 27
3.3.1
UART Design Guide........................................................................................................................27
3.3.2
RI and DTR Behavior......................................................................................................................28
3.4
USB Interface............................................................................................................................................29
3.5
SIM Interface.............................................................................................................................................30
3.5.1
SIM Application Guide.....................................................................................................................30
3.6
PCM Interface........................................................................................................................................... 32
3.6.1
PCM timing........................................................................................................................................32
3.6.2
PCM Application Guide...................................................................................................................33
3.7
I2C Interface..............................................................................................................................................34
3.8
Network status.......................................................................................................................................... 34
3.9
Other interface.......................................................................................................................................... 36
3.9.1
ADC....................................................................................................................................................36
3.9.2
LDO.................................................................................................................................................... 36
4
RF Specifications...................................................................................................................................... 38
4.1
GSM/LTE RF Specifications...................................................................................................................38
4.2
GSM/LTE Antenna Design Guide..........................................................................................................41
4.3
GNSS......................................................................................................................................................... 42
4.3.1
GNSS Technical specification........................................................................................................42
4.3.2
GNSS Application Guide................................................................................................................ 42
4.4
RF traces note.......................................................................................................................................... 44

---

## Page 5
SIM7000 Series Hardware Design V1.09
www.simcom.com
5/69
4.4.1
RF traces layout...............................................................................................................................44
4.4.2
LTE ANT and other system ANT decoupling...............................................................................45
5
Electrical Specifications..........................................................................................................................46
5.1
Absolute maximum ratings..................................................................................................................... 46
5.2
Operating conditions................................................................................................................................46
5.3
Operating Mode........................................................................................................................................48
5.3.1
Operating Mode Definition..............................................................................................................48
5.3.2
Sleep mode.......................................................................................................................................49
5.3.3
Minimum functionality mode and Flight mode............................................................................ 49
5.3.4
Power Saving Mode (PSM)............................................................................................................49
5.4
Current Consumption...............................................................................................................................50
5.5
ESD Notes.................................................................................................................................................52
6
Electrical Specifications..........................................................................................................................53
6.1
Top and Bottom View of SIM7000.........................................................................................................53
6.2
Label Information......................................................................................................................................54
6.3
Typical SMT Reflow Profile.....................................................................................................................55
6.4
Moisture Sensitivity Level (MSL)........................................................................................................... 56
6.5
Baking.........................................................................................................................................................56
6.6
Stencil Foil Design Recommendation...................................................................................................57
7
Electrical Specifications..........................................................................................................................58
7.1
Tray packaging......................................................................................................................................... 58
8
Appendix..................................................................................................................................................... 61
8.1
Reference Design.....................................................................................................................................61
8.2
Design check list.......................................................................................................................................62
8.3
Coding Schemes and Maximum Net Data Rates over Air Interface............................................... 64
8.4
Related Documents................................................................................................................................. 65
8.5
Terms and Abbreviations.........................................................................................................................67
8.6
Safety Caution.......................................................................................................................................... 69

---

## Page 6
SIM7000 Series Hardware Design V1.09
www.simcom.com
6/69
Table Index
Table 1: SIM7000 frequency bands and air interface............................................................................................... 9
Table 2: General features.............................................................................................................................................11
Table 3: Pin definition................................................................................................................................................... 13
Table 4: IO parameters definition............................................................................................................................... 15
Table 5: Pin description................................................................................................................................................15
Table 6: VBAT pins electronic characteristic............................................................................................................ 20
Table 7: Recommended TVS diode list.....................................................................................................................21
Table 8: Power on timing and electronic characteristic.......................................................................................... 24
Table 9: Power off timing and electronic characteristic.......................................................................................... 25
Table 10: RESET pin electronic characteristic.........................................................................................................26
Table 11: UART electronic characteristic.................................................................................................................. 28
Table 12: SIM TVS recommended model list...........................................................................................................30
Table 13: SIM electronic characteristic in 1.8V mode (SIM_VDD=1.8V)............................................................ 30
Table 14: SIM electronic characteristic 3.0V mode (SIM_VDD=2.95V).............................................................. 30
Table 15: PCM format...................................................................................................................................................32
Table 16: PCM timing parameters..............................................................................................................................33
Table 17: NETLIGHT pin status..................................................................................................................................35
Table 18: ADC electronic characteristics...................................................................................................................36
Table 19: Electronic characteristic..............................................................................................................................36
Table 20: Conducted transmission power.................................................................................................................38
Table 21: Maximum Power Reduction (MPR) for UE category NB1 Power Class 3.........................................38
Table 22: Operating frequencies................................................................................................................................ 39
Table 23: E-UTRA operating bands........................................................................................................................... 39
Table 24: Conducted receive sensitivity....................................................................................................................39
Table 25: CAT-M1 Reference sensitivity (QPSK).................................................................................................... 40
Table 26: CAT-NB1 Reference sensitivity (QPSK)..................................................................................................40
Table 27: Trace loss......................................................................................................................................................41
Table 28: Recommended TVS....................................................................................................................................41
Table 29: Absolute maximum ratings.........................................................................................................................46
Table 30: Recommended operating ratings..............................................................................................................46
Table 31: 1.8V Digital I/O characteristics*................................................................................................................ 46
Table 32: Operating temperature................................................................................................................................47
Table 33: Operating mode Definition......................................................................................................................... 48
Table 34: Current consumption on VBAT Pins (VBAT=3.8V)................................................................................50
Table 35: The ESD performance measurement table (Temperature: 25℃, Humidity: 45%.)..........................52
Table 35: The description of label information......................................................................................................... 54
Table 37: Moisture Sensitivity Level and Floor Life.................................................................................................56
Table 38: Baking conditions........................................................................................................................................ 56
Table 39: Tray size........................................................................................................................................................59
Table 40: Small Carton size.........................................................................................................................................59
Table 41: Big Carton size.............................................................................................................................................60
Table 42: SchematicCheck List.................................................................................................................................. 62

---

## Page 7
SIM7000 Series Hardware Design V1.09
www.simcom.com
7/69
Table 43: PCB LayoutCheck List................................................................................................................................62
Table 44: Coding Schemes and Maximum Net Data Rates over Air Interface...................................................64
Table 45: Related Documents.....................................................................................................................................65
Table 46: Terms and Abbreviations............................................................................................................................67
Table 47: Safety Caution..............................................................................................................................................69

---

## Page 8
SIM7000 Series Hardware Design V1.09
www.simcom.com
8/69
Figure Index
Figure 1: SIM7000 block diagram.............................................................................................................................. 11
Figure 2: Pin assignment overview............................................................................................................................13
Figure 3: Dimensions (Unit: mm)................................................................................................................................18
Figure 4: Footprint recommendation (Unit: mm)..................................................................................................... 19
Figure 5: VBAT voltage drop during burst emission (EDGE/GPRS)................................................................... 20
Figure 6: Power supply application circuit................................................................................................................ 21
Figure 7: Linear regulator reference circuit.............................................................................................................. 22
Figure 8: power supply reference circuit (NB only).................................................................................................22
Figure 9: Reference power on/off circuit...................................................................................................................23
Figure 10: Power on timing sequence.......................................................................................................................24
Figure 11: Power off timing sequence.......................................................................................................................25
Figure 12: Reference reset circuit..............................................................................................................................26
Figure 13: UART full modem...................................................................................................................................... 27
Figure 14: UART null modem..................................................................................................................................... 27
Figure 15: Reference circuit of level shift..................................................................................................................28
Figure 16: RI behaviour（SMS and URC report）................................................................................................. 29
Figure 17: USB reference circuit................................................................................................................................ 29
Figure 18: SIM interface reference circuit.................................................................................................................31
Figure 19: PCM_SYNC timing....................................................................................................................................32
Figure 20: External codec to module timing.............................................................................................................32
Figure 21: Module to external codec timing............................................................................................................. 33
Figure 22: Audio codec reference circuit.................................................................................................................. 34
Figure 23: I2C reference circuit.................................................................................................................................. 34
Figure 24: NETLIGHT reference circuit.....................................................................................................................35
Figure 25：Power on sequence of the VDD_EXT..................................................................................................36
Figure 26: Antenna matching circuit (MAIN_ANT)..................................................................................................41
Figure 27: Active antenna circuit................................................................................................................................43
Figure 28: Passive antenna circuit (Default)............................................................................................................ 43
Figure 29: RF trace should be far away from other high speed signal lines...................................................... 44
Figure 30: The distance between GND to the inner conductor of SMA.............................................................. 45
Figure 31: Top and bottom view of SIM700............................................................................................................. 53
Figure 32: Label information....................................................................................................................................... 54
Figure 33: The ramp-soak-spike reflow profile of SIM7000...................................................................................55
Figure 34: stencil recommendation (Unit: mm)........................................................................................................57
Figure 35: packaging diagram.................................................................................................................................... 58
Figure 36: Tray drawing...............................................................................................................................................58
Figure 37: Small carton drawing.................................................................................................................................59
Figure 38: Big carton drawing.....................................................................................................................................59
Figure 39: Reference design.......................................................................................................................................61

---

## Page 9
SIM7000 Series Hardware Design V1.09
www.simcom.com
9/69
1 Introduction
This document describes the electronic specifications, RF specifications, interfaces, mechanical
characteristics and testing results of the SIMCom SIM7000 series module. With the help of this document
and other SIM7000 series software application notes/user guides, users can understand and use
SIM7000 series module to design and develop applications quickly.
Product Outline
The SIM7000 series modules support LTE CAT-M1、LTE CAT-NB1、GPRS and EDGE.
The physical dimension of SIM7000 is 24×24×2.6mm mm. And the physical dimension is compatible with
the packaging of SIM900, SIM800 and SIM800F.
Table 1: SIM7000 frequency bands and air interface
Standard
Frequency
Variants
SIM7000A
SIM7000C
SIM7000E
SIM7000JC
SIM7000C-
N
SIM7000E-
N
SIM7000G
GPRS
GSM850MHz

EGSM900MHz



DCS1800MHz



PCS1900MHz

LTE-FDD
HD-FDD
LTE-FDD B1




LTE-FDD B2


LTE-FDD B3






LTE-FDD B4


LTE-FDD B5




LTE-FDD B8






LTE-FDD B12


LTE-FDD B13


LTE-FDD B18


LTE-FDD B19


LTE-FDD B20



LTE-FDD B25
LTE-FDD B26


LTE-FDD B28



LTE-FDD B39


---

## Page 10
SIM7000 Series Hardware Design V1.09
www.simcom.com
10/69
Category
LTE-M1





Category
LTE-NB1






GNSS
GPS





GLONASS





BeiDou




Galileo
*
Galileo is default closed in software. But users can open it via AT command “AT+CGNSMOD”.For more
information about these AT commands, please refer to Document [1]
Hardware Interface Overview
The interfaces are described in detail in the next chapters include:
●
Power Supply
●
USB Interface
●
UART Interface
●
SIM Interface
●
ADC
●
LDO Power Output
●
PCM Interface
●
I2C Interface
●
GPIOs
●
Antenna Interface
Hardware Block Diagram
The block diagram of the SIM7000 module is shown in the figure below.
NOTE

---

## Page 11
SIM7000 Series Hardware Design V1.09
www.simcom.com
11/69
Figure 1: SIM7000 block diagram
Functional Overview
Table 2: General features
Feature
Implementation
Power supply
Power supply voltage 3.0～4.3V.
Power saving
Current in sleep mode: 1.2mA (@DRX=2.56s).
Current in PSM mode: 9uA.
Radio frequency bands
Please refer to the table 1
Transmitting power
GPRS power class:

---

## Page 12
SIM7000 Series Hardware Design V1.09
www.simcom.com
12/69
--EGSM900: 4 (2W).
--DCS1800: 1 (1W).
EDGE power class:
--EGSM900: E2 (0.5W).
--DCS1800: E1 (0.4W).
LTE power class:3 (0.25W).
Data Transmission
Throughput
GPRS multi-slot class 12.
EDGE multi-slot class 12.
LTE CAT M1: 300Kbps (DL).
LTE CAT M1: 375Kbps (UL).
LTE CAT NB1: 34Kbps (DL).
LTE CAT NB1: 66Kbps (UL).
Antenna
GPRS/EDGE/LTE main antenna.
GNSS antenna.
GNSS
GNSS engine (GPS,GLONASS, BD and Galileo).
Protocol: NMEA.
SMS
MT, MO, CB, Text and PDU mode.
SMS storage: SIM card or ME(default).
SIM interface
Support identity card: 1.8V/ 3V.
SIM application toolkit
Support SAT class 3, GSM 11.14 Release 98.
Support USAT.
Audio feature
Support PCM interface.
Only support PCM master mode and short frame sync, 16-bit linear data
formats.
UART interface
A full modem serial port by default.
Baud rate: 300bps to 3686400bps. Default rate is 0bps (auto baud rate).
Support auto baud rate, but only limited to 9600, 19200, 38400, 57600
and115200 bps.
Can be used as the AT commands or data stream channel.
Support RTS/CTS hardware handshake.
USB
USB 2.0 high speed interface.
Firmware upgrade
Firmware upgrade over USB interface
Physical characteristics
Size:24×24×2.6mm
Weight:3g
Temperature range
Normal operation temperature: -30°C to +80°C
Extended operation temperature: -40°C to +85°C*
Storage temperature -45°C to +90°C
Module is able to make and receive voice calls, data calls, SMS and make GPRS/EDGE/LTE traffic in
-40 ℃
~ +85 ℃. The performance will be reduced slightly from the 3GPP specifications if the
temperature is outside the normal operating temperature range and still within the extreme operating
temperature range.
NOTE

---

## Page 13
SIM7000 Series Hardware Design V1.09
www.simcom.com
13/69
2 Package Information
Pin Assignment Overview
All functions of the SIM7000 will be provided through 68 pads that will be connected to the customers’
platform. The following Figure is the pin assignment of the SIM7000.
Figure 2: Pin assignment overview
Table 3: Pin definition
Pin No.
Pin Name
Pin No.
Pin Name
1
PWRKEY
2
GND
3
DTR
4
RI
5
DCD
6
BOOT_CFG

---

## Page 14
SIM7000 Series Hardware Design V1.09
www.simcom.com
14/69
7
CTS
8
RTS
9
TXD
10
RXD
11
PCM_CLK
12
PCM_SYNC
13
PCM_DIN
14
PCM_DOUT
15
VDD_EXT
16
NRESET
17
GND
18
GND
19
NC
20
NC
21
NC
22
NC
23
MDM_LOG_TX
24
USB_VBUS
25
ADC
26
NC
27
USB_DP
28
USB_DM
29
GND
30
SIM_VDD
31
SIM_DATA
32
SIM_CLK
33
SIM_RST
34
SIM_DET
35
NC
36
NC
37
I2C_SDA
38
I2C_SCL
39
GND
40
NC
41
NC
42
NC
43
NC
44
NC
45
GND
46
GND
47
NC
48
GPIO4
49
GPIO1/UART3_RXD
50
GPIO0/UART3_TXD
51
NC
52
NETLIGHT
53
GNSS_ANT
54
GND
55
VBAT
56
VBAT
57
VBAT
58
GND
59
GND
60
RF_ANT
61
GND
62
GND
63
GND
64
GND
65
GND
66
STATUS
67
GPIO2
68
GPIO3
Before the normal power up, BOOT_CFG cannot be pulled up.
NOTE

---

## Page 15
SIM7000 Series Hardware Design V1.09
www.simcom.com
15/69
Pin Description
Table 4: IO parameters definition
Pintype
Description
PI
Power input
PO
Power output
AI
Analog input
AIO
Analog input/output
I/O
Bidirectional input /output
DI
Digital input
DO
Digital output
DOH
Digital output with high level
DOL
Digital output with low level
PU
Pull up
PD
Pull down
Table 5: Pin description
Pin name
Pin No.
Default
status
Description
Comment
Power supply
VBAT
55、56、
57
PI
Power supply, voltage range:
3.0～4.3V.
VDD_EXT
15
PO
LDO power output 1.8V for other
external circuits with Max 50mA
current output.
This power supple only
use for external GPIO
pulling up or level shift
circuit.
If unused, keep it open.
GND
2、17、18、
29、39、
45、46、
54、58、
59、61、
62、63、
64、65
Ground
System Control
PWRKEY
1
DI,PU
System power on/off control input,
active low. The efficient input level
must be below 0.5V.
The level is 0.8V when
this PIN is floating;
NRESET
16
DI, PU
System reset control input, active
low.
NRESET has been
pulled up to 1.8V via
40Kohmresistor
internally.
SIM interface
SIM_DATA
31
I/O,PU
SIM Card data I/O, which has
been pulled up via a 10KR resistor
to SIM_VDD internally. Do not pull
it up or down externally.
All lines of SIM interface
should be protected
against ESD.

---

## Page 16
SIM7000 Series Hardware Design V1.09
www.simcom.com
16/69
SIM_RST
33
DO
SIM Reset
SIM_CLK
32
DO
SIM clock
SIM_VDD
30
PO
Power output for SIM card, its
output Voltage depends on SIM
card type automatically. Its output
current is up to 50mA.
SIM_DET
34
DI
SIM card detecting input.
If used, keep a 10kΩ
resistor pulling up to the
VDD_EXT
USB*
USB_VBUS
24
DI,PD
Valid USB detection input with
3.5~5.25V detection voltage
Software download
interface.
USB_DP
27
I/O
Positive line of the differential,
bi-directional USB signal.
USB_DM
28
I/O
Negative line of the differential,
bi-directional USB signal.
UART interface
DTR
3
DI,PU
DTE get ready
If unused, keep them
open.
RI
4
DOH
Ring Indicator
DCD
5
DOH
Carrier detects
CTS
7
DOL
Clear to Send
RTS
8
DI,PD
Request to send
TXD
9
DOH
Transmit Data
RXD
10
DI,PD
Receive Data
I2C interface
I2C_SDA
37
DO
I2C data input/output
If unused, keep open, or
else pull them up
via2.2KΩ resistors to
the VDD_EXT.
I2C_SCL
38
I/O
I2C clock output
PCM interface
PCM_CLK
11
DOH
PCM data bit clock.
If unused, please keep
them open.
PCM_SYNC
12
DO
PCM data frame sync signal.
PCM_DIN
13
DI
PCM data input.
PCM_DOUT
14
DO
PCM data output.
GPIO
NETLIGHT
52
DO
LED control output as network
status indication.
If unused, keep them
open.
STATUS
66
DOH
Operating status output.
High level: Power on and firmware
ready
Low level: Power off
GPIO0
50
IO
Default: GPIO
Optional: UART3_TXD in DAM
application
GPIO1
49
IO
Default: GPIO
Optional: UART3_RXD in DAM
application

---

## Page 17
SIM7000 Series Hardware Design V1.09
www.simcom.com
17/69
GPIO2
67
IO
GPIO
GPIO3
68
DOH
GPIO
GPIO4
48
DOH
GPIO
RF interface
GNSS_ANT
53
AI
GNSS antenna soldering pad
RF_ANT
60
AIO
MAIN antenna soldering pad
Other interface
BOOT_CFG
6
DI,PD
If it needs to enterintoforcedUSB
download mode, it must be pulling
up this pin to VDD_EXT before
press the PWRKEY.
If it needs to boot up normally,
please keep this pin open.
Reserve a test points
for it. Keep it open.DO
NOT PULL UP DURING
NORMAL POWER UP!
MDM_LOG_TX
23
DO
Module log output for SW debug.
(only used for platform)
Reserve a test point for
it.
ADC
25
AI
Analog-digital converter input.
voltage range:0～VBAT.
If unused, keep them
open.
NC
19、20、
21、22、
26、35、
36、40、
41、42、
43、44、
47、51、
No connection.
Keep it open
Please reserve a test point for BOOT_CFG, VDD_EXT and MDM_LOG_TX. If there is no USB
connector, please also reserve a test point for USB_VBUS, USB_DP, and USB_DM for Firmware
upgrade.
NOTE

---

## Page 18
SIM7000 Series Hardware Design V1.09
www.simcom.com
18/69
Mechanical Information
The following figures howsthe package outline drawing ofSIM7000.
Figure 3: Dimensions (Unit: mm)

---

## Page 19
SIM7000 Series Hardware Design V1.09
www.simcom.com
19/69
Footprint Recommendation
Figure 4: Footprint recommendation (Unit: mm)

---

## Page 20
SIM7000 Series Hardware Design V1.09
www.simcom.com
20/69
3 Interface Application
Power Supply
Pin 55, pin 56 and pin 57 are VBAT power input.
On VBAT pads, when module works on CAT-M1 or NB-IoT mode, the ripple current is up to 0.6A typically.
For steady voltage, the power supply capability must be up to 0.6A.
On VBAT pads, when module works on EDGE or GPRS mode, he ripple current is up to 2A typically. For
steady voltage, the power supply capability must be up to 2A.
in order to avoid the voltage dropped down more than 300mV,the load capacitor on VBAT pads must be
more than 300uF.
The following figure shows the VBAT voltage ripple wave at the maximum power transmit phase in
EDGE/GPRS emission mode.
Figure 5: VBAT voltage drop during burst emission (EDGE/GPRS)
The test condition: The voltage of power supply for VBAT is 3.8V, Ca=100 µF tantalum capacitor
(ESR=0.7Ω) and Ce = 100Nf (Please refer to Figure 6—Application circuit).
Table 6: VBAT pins electronic characteristic
Symbol
Description
Min.
Typ.
Max.
Unit
VBAT
Module power voltage
3.0
3.8
4.3
V
IVBAT(peak)
Module power peak current in GSM and EDGE
emission mode.
-
2
-
A
NOTE

---

## Page 21
SIM7000 Series Hardware Design V1.09
www.simcom.com
21/69
Module power peak current in CAT-M1 and NB-IoT
emission mode.
-
0.6
-
A
IVBAT(average)
Module power average current in normal mode
Please refer to the chapter 5.4
IVBAT(sleep)
Power supply current in sleep mode
IVBAT(power-off)
Module power current in power off mode.
-
-
7
uA
3.1.1 Power Supply Design Guide
Make sure that the voltage on the VBAT pins will never drop below 3.0V, even during a transmit burstwhen
current consumption may rise up to 2A. If the voltage drops below3.0V, module will be shutdown.
If the power supply for VBAT pins can support up to 2A, using a total of more than 300uF capacitors is
recommended, or else users must using a total of 1000uF capacitors typically, in order to avoid the
voltage drop is more than 300mV.
Some multi-layer ceramic chip (MLCC) capacitors (0.1uF, 1uF) with low ESR in high frequency band can
be used for EMC.
These capacitors should be put as close as possible to VBAT pads. Also, users should keep VBAT trace
on circuit board wider than 2 mm to minimize PCB trace impedance. The following figure shows the
recommended circuit.
Figure 6: Power supply application circuit
In addition, for ESD protection, it is suggested to add a TVS diode near the VBAT PINs.
Table 7: Recommended TVS diode list
No.
Manufacturer
Part Number
Package
1
Prisemi
PESDHC2FD4V5B
DFN1006
2
Prisemi
PESDHC3D3V3U
SOD323
3
WILLsemi
ESD5651N-2/TR
DFN1006
NOTE

---

## Page 22
SIM7000 Series Hardware Design V1.09
www.simcom.com
22/69
3.1.2 Recommended Power Supply Circuit
It is recommended that a switching mode power supply or near regulator power supply is used. It is
important to make sure that all the components used in the power supply circuit can resist a peak current
up to 2A when used GPRS/EDGE.
The following figure shows the linear regulator reference circuit with 5V input and 3.8V output.
But this linear regulator has a minimum load current, and it is even bigger than 7mA. So if users care the
system power consumption very much, it is not recommended to use.
Figure 7: Linear regulator reference circuit
If users used LTE mode only and never used EDGE/GPRS mode, switching modepower supply is
recommended to use. And the maximum output current must be meeting the requirement. The following
figure shows these witching mode power supply reference circuit.
Figure 8: power supply reference circuit (NB only)
3.1.3 Voltage Monitor
To monitor the VBAT voltage, the AT command “AT+CBC” can be used.
AT command “AT+CBATCHK=1” can be used to enable the overvoltage warning function and the
under-voltage warning function. The default value of the over voltagewarning function in the software is
4.3V, and the default value of the under-voltage warning function is 3.1V. If the power supply for VBAT
pins is up 4.3V or under 3.1V, module will be warning.
The AT command “AT+CBATCHK=1”also can be used to enable the overvoltage power-off function and
the under-voltage power-off function. The default value of the overvoltage power-off function is 4.4V, and
the default value of the under-voltage power-off function is 2.9V. If the VBAT voltage is up 4.4V or

---

## Page 23
SIM7000 Series Hardware Design V1.09
www.simcom.com
23/69
under2.9V, module will be power off.
Under-voltage warning function and under-voltage power-off function are disabled by default. For more
information about these AT commands, please refer to Document [1].
Power on/Power off/Reset Function
3.2.1 Power on
SIM7000 can be powered on by pulling the PWRKEY pin to ground.
The PWRKEY pin has been pulled up with a diode to 1.8V internally, so it does not need to be pulled up
externally. It is strongly recommended to put a100nF capacitor and an ESD protection diode close to the
PWRKEY pin, as it would strongly enhance the ESD performance of PWRKEY pin. Please refer to the
following figure for the recommended reference circuit.
Figure 9: Reference power on/off circuit
The power-on scenarios are illustrated in the following figure.
NOTE

---

## Page 24
SIM7000 Series Hardware Design V1.09
www.simcom.com
24/69
Figure 10: Power on timing sequence
Table 8: Power on timing and electronic characteristic
Symbol
Parameter
Min.
Typ.
Max.
Unit
Ton
The time of active low level impulse of PWRKEY pin
to power on module
1
-
-
s
Ton(Vdd)
The time from power-on issue to VDD_EXT pin
output high level.
64
ms
Ton(status)
The time from power-on issue to STATUS pin output
high level(indicating power up ready )
4.5
-
-
s
Ton(uart)
The time from power-on issue to UART port ready
4.5
-
-
s
Ton(usb)
The time from power-on issue to USB port ready
4.5
-
-
s
VIH
Input high level voltage on PWRKEY pin
0.6
0.8
1.8
V
VIL
Input low level voltage on PWRKEY pin
-0.3
0
0.5
V
3.2.2 Power off
The following methods can be used to power off SIM7000.
●
Method 1: Power off SIM7000 by pulling the PWRKEY pin to ground.
●
Method 2: Power off SIM7000 by AT command “AT+CPOWD=1”.
●
Method 3: over-voltage or under-voltage automatic power off. The functioncan be enabled by AT
command “AT+CBATCHK=1”. Default is disabled.
NOTE

---

## Page 25
SIM7000 Series Hardware Design V1.09
www.simcom.com
25/69
For details about “AT+CPOWD” and “AT+CBATCHK”, please refer to Document [1].
These procedures will make modules disconnect from the network and allow the software to enter a safe
state, and save data before module be powered off completely.
The power off scenario by pulling down the PWRKEY pin is illustrated in the following figure.
Figure 11: Power off timing sequence
Table 9: Power off timing and electronic characteristic
Symbol
Parameter
Time value
Uni
Min.
Typ.
Max.
Toff
The active low level time pulse on PWRKEY pin to power
off module
1.2
-
-
s
Toff (vdd)
The time from power-off issue to VDD_EXT pin output low
level
1.8
-
6.9
s
Toff(status
)
The time from power-off issue to STATUS pin output low
level(indicating power off )*
1.8
-
6.9
s
Toff(uart)
The time from power-off issue to UART port off
1.8
-
6.9
s
Toff(usb)
The time from power-off issue to USB port off
1.8
-
6.9
s
Toff-on
The buffer time from power-off issue to power-on issue
2
-
-
s
NOTE

---

## Page 26
SIM7000 Series Hardware Design V1.09
www.simcom.com
26/69
The STATUS pin can be used to detect whether module is powered on or not. When module has been
powered on and firmware goes ready, STATUS will be high level, or else STATUS will still low level.
3.2.3 Reset Function
SIM7000 can be reset by pulling the RESET pin to ground.
This function is only used as an emergency reset. The RESET pin will be ineffectiveness in the power
off mode.
The RESET pin has been pulled up to 1.8V with a 40KΩ resistor internally. So it does not need to be
pulled up externally. It is strongly recommended to put a100nF capacitor and an ESD protection diode
close to the RESET pin. Please refer to the following figure for the recommended reference circuit.
Figure 12: Reference reset circuit
Table 10: RESET pin electronic characteristic
Symbol
Description
Min.
Typ.
Max.
Unit
Treset
The active low level time impulse on RESET pin to
reset module
252
ms
VIH
Input high level voltage
1.2
1.8
2.1
V
VIL
Input low level voltage
-0.3
0
0.8
V
NOTE

---

## Page 27
SIM7000 Series Hardware Design V1.09
www.simcom.com
27/69
UART Interface
SIM7000 provides a7-wire UART (universal asynchronous serial transmission) interfaces DCE (Data
Communication Equipment).AT commands and data transmission can be performed through this UART
interface.
In DAM (Downloadable Application Module) application, SIM7000 provides a UART interface to use. This
UART multiplexed from GPIO. The GPIO0 multiplex as TXD and the GPIO1 multiplex as RXD. This UART
interface can’t use as AT port or data transmission. It is only used as UART in DAM application when
secondary development.
SIM7000 support high speed UART, the baud rate is up to 4Mbps. The communication baud rates
include:0,300,600,1200,2400,4800,9600,19200,38400,57600,115200,230400,921600,2000000,3000000,
3200000,3686400 bps. The rate 0bps mark auto baud rate. And it supports auto baud rate, but the rate
only supported on 9600, 19200, 38400, 57600, 115200. If users need to change to other baud rate, it
needs to switch via manual operation.
3.3.1 UART Design Guide
The following figures show the reference design.
Figure 13: UART full modem
Figure 14: UART null modem

---

## Page 28
SIM7000 Series Hardware Design V1.09
www.simcom.com
28/69
Table 11: UART electronic characteristic
Symbol
Description
Min.
Typ.
Max.
Unit
VIH
UART input high level voltage
1.17
1.8
2.1
V
VIL
UART input low level voltage
-0.3
0
0.63
V
VOH
UART output high level voltage
1.35
1.8
1.8
V
VOL
UART output low level voltage
0
0
0.45
V
The SIM7000 UART is 1.8V voltage interface. If user’s UART application circuit is 3.3V voltage interface,
the level shifter circuits should be used for voltage matching. The following figure shows the voltage
matching reference design.
Figure 15: Reference circuit of level shift
When it uses the level shifter IC, the pull up resistance on TXD_3.3V, RTS_3.3V, DCD_3.3V and
RI_3.3V should not be less than 47KΩ.
3.3.2 RI and DTR Behavior
The RI pin description:
The RI pin can be used to interrupt output signal to inform the host controller such as application CPU.
Before that, users must use AT command “AT+CFGRI=1” to enable this function.
Normally RI will keep high level until certain conditions such as receiving SMS, or a URC report coming,
then it will output a low level pulse 120ms, in the end, it will become high level.
NOTE

---

## Page 29
SIM7000 Series Hardware Design V1.09
www.simcom.com
29/69
Figure 16: RI behaviour（SMS and URC report）
The DTR pin description:
After setting the AT command “AT+CSCLK=1”, and then pulling up the DTR pin, SIM7000 will enter sleep
mode when module is in idle mode. In sleep mode, the UART is unavailable. When SIM7000 enters sleep
mode, pulling down DTR can wake up module.
After setting the AT command “AT+CSCLK=0”, SIM7000 will do nothing when the DTR pin is pulling up.
For more details of AT commands about UART, please refer to document [1] and [20].
USB Interface
The SIM7000 contains a USB interface compliant with the USB2.0 specification as a peripheral, but the
USB charging function is not supported.
USB_VBUS is the detecting signal for USB inserting. The input voltage range on the USB_VBUS pin is
from 3.5V to 5.25V. If the voltage is out of this range, it may cause USB port unidentifiable.
The reference circuit refers to the following figure.
Figure 17: USB reference circuit
Because of the high speed on USB bus, more attention should be paid to the influence of the junction
capacitance of the ESD component on USB data lines. Typically, the capacitance of the D1 and D2 should
be less than 1pF.
D3 is suggested to select the diode with anti-ESD and voltage surge function, or customer could add a
ZENER diode for surge clamping.
NOTE

---

## Page 30
SIM7000 Series Hardware Design V1.09
www.simcom.com
30/69
Table 12: SIM TVS recommended model list
NOI
Factory
P/N.
Load cap
Pack
1
NXP
PESD5V0X1BCA
L
0.85pF
0402
2
Willsemi
ESD5301N
0.4pF
0402
3
NXP
PESD5V0H1BSF
0.15pF
0201
4
Willsemi
ESD5311Z-2/TR
0.25pF
0201
The USB_DM and USB_DP nets must be traced by 90Ohm+/-10% differential impedance.
SIM Interface
SIM7000 supports both 1.8V and 3.0V SIM Cards.
Table 13: SIM electronic characteristic in 1.8V mode (SIM_VDD=1.8V)
Symbol
Parameter
Min.
Typ.
Max.
Unit
SIM_VDD
LDO power output voltage
1.75
1.8
1.95
V
VIH
High-level input voltage
0.65*SIM_VDD
-
SIM_VDD +0.3
V
VIL
Low-level input voltage
-0.3
0
0.35*SIM_VDD
V
VOH
High-level output voltage
SIM_VDD -0.45
-
SIM_VDD
V
VOL
Low-level output voltage
0
0
0.45
V
Table 14: SIM electronic characteristic 3.0V mode (SIM_VDD=2.95V)
Symbol
Parameter
Min.
Typ.
Max.
Unit
SIM_VDD
LDO power output voltage
2.75
2.95
3.05
V
VIH
High-level input voltage
0.65*SIM_VDD
-
SIM_VDD +0.3
V
VIL
Low-level input voltage
-0.3
0
0.25*SIM_VDD
V
VOH
High-level output voltage
SIM_VDD -0.45
-
SIM_VDD
V
VOL
Low-level output voltage
0
0
0.45
V
3.5.1 SIM Application Guide
It is recommended to use an ESD protection component such as ESDA6V1W5 produced by ST
(www.st.com ) or SMF15C produced by ON SEMI (www.onsemi.com ). Note that the SIM peripheral circuit
should be close to the SIM card socket. The following figure shows the 6-pin SIM card holder reference
circuit.
NOTE

---

## Page 31
SIM7000 Series Hardware Design V1.09
www.simcom.com
31/69
Figure 18: SIM interface reference circuit
SIM_DATA has been pulled up with a 10KΩ resistor to SIM_VDD in module, so it does not need to pulled
up resistor anymore.
SIM_VDD needs a 100nF capacitor close to SIM socket.
SIM_CLK is very important signal, the rise time and fall time of SIM_CLK should be less than 40ns. So the
junction capacity of the TVS needs to be less 50pF.
SIM_DET is the detecting signal for SIM card to insert and pull out. There is no pull up resistor in module, so
a 10KΩ resistor is necessary to pulling up to the power VDD_EXT. This function is disabled default by
software. Users can enable it by AT comment “AT+CSDT”. And the Interrupt state can be set by AT
comment “AT+CSPOL”.
For more details of AT commands about “AT+CSDT” and “AT+CSPOL”, please refer to document [1]
SIM card circuit is easy to be interfered, resulting in unrecognized card or card out of the situation, so
please follow the following principles in the design:

It is recommended to place a 100nF capacitor near the SIM card holder on the SIM_VDD signal
line

Place near SIM gets stuck, TVS, the parasitic capacitance of TVS should not greater than 50 pf, 22
Ω resistance in series between the SIM gets stuck and module can enhance ESD protection
performance

Be sure to keep the SIM card holder away from the main antenna during the PCB layout phase

The SIM card line should be far away from RF line, VBAT line and high-speed signal line, and the
SIM card line should not be too long

SIM card signal line line avoid line branch

The GND of the SIM card holder should maintain good connectivity with the GND of the module
and make the two GND equipotential

Each signal of SIM card should be protected by GND, and SIM_CLK should be protected
separately.
NOTE

---

## Page 32
SIM7000 Series Hardware Design V1.09
www.simcom.com
32/69
PCM Interface
SIM7000 provides a PCM interface for external codec, which can be used in master mode with short sync
and 16 bits linear format.
Table 15: PCM format
For more details about PCM AT commands, please refer to document [1].
3.6.1 PCM timing
SIM7000 supports 2.048 MHz PCM data and sync timing for 16 bits linear format codec.
Figure 19: PCM_SYNC timing
Figure 20: External codec to module timing
Characteristics
Specification
Line Interface Format
Linear(Fixed)
Data length
16bits(Fixed)
PCM Clock /Sync Source
Master Mode(Fixed)
PCM Clock Rate
2048 KHz (Fixed)
PCM Sync Format
Short sync(Fixed)
Data Ordering
MSB
NOTE

---

## Page 33
SIM7000 Series Hardware Design V1.09
www.simcom.com
33/69
Figure 21: Module to external codec timing
Table 16: PCM timing parameters
3.6.2 PCM Application Guide
The following figure shows the external codec reference design.
Parameter
Description
Min.
Typ.
Max.
Unit
T(sync)
PCM_SYNC cycle time
–
125
–
μs
T(synch)
PCM_SYNC high level time
–
488
–
ns
T(syncl)
PCM_SYNC low level time
–
124.5
–
μs
T(clk)
PCM_CLK cycle time
–
488
–
ns
T(clkh)
PCM_CLK high level time
–
244
–
ns
T(clkl)
PCM_CLK low level time
–
244
–
ns
T(susync)
PCM_SYNC setup time high before falling edge
of PCM_CLK
–
122
–
ns
T(hsync)
PCM_SYNC hold time after falling edge of
PCM_CLK
–
366
–
ns
T(sudin)
PCM_IN setup time before falling edge of
PCM_CLK
60
–
–
ns
T(hdin)
PCM_IN hold time after falling edge of PCM_CLK
60
–
–
ns
T(pdout)
Delay from PCM_CLK rising to PCM_OUT valid
–
–
60
ns
T(zdout)
Delay
from
PCM_CLK
falling
to
PCM_OUT
HIGH-Z
–
–
60
ns

---

## Page 34
SIM7000 Series Hardware Design V1.09
www.simcom.com
34/69
Figure 22: Audio codec reference circuit
I2C Interface
SIM7000 provides anI2C interface compatible with I2C specification, version 5.0, with clock rate up to 400
kHz. Its operation voltage is 1.8V.
The following figure shows the I2C bus reference design.
Figure 23: I2C reference circuit
The I2C signal has no pull-up resistors in module. So the pulling up resistors 2.2KΩ to VDD_EXT are
necessary in application circuit.
Network status
The NETLIGHT pin is used to control Network Status LED, its reference circuit is shown in the following
figure.

---

## Page 35
SIM7000 Series Hardware Design V1.09
www.simcom.com
35/69
Figure 24: NETLIGHT reference circuit
The value of the resistor named “R” depends on the LED characteristic.
Table 17: NETLIGHT pin status
NETLIGHT pin status
Module status
64ms ON, 800ms OFF
No registered network
64ms ON, 3000ms OFF
Registered network (PS domain registration success)
64ms ON, 300ms OFF
Data transmit (PPP dial-up state and use of data services such as
internal TCP/FTP/HTTP)
OFF
Power off or PSM mode
NETLIGHT output low level as “OFF” and high level as “ON”.
NOTE
NOTE

---

## Page 36
SIM7000 Series Hardware Design V1.09
www.simcom.com
36/69
Other interface
3.9.1 ADC
SIM7000 has a dedicated ADC pin. It is available for digitizing analog signals such as battery voltage and so
on. Its input voltage range is from 0V to VBAT. That is the maximum measurement range of ADC cannot
exceed the input voltage of VBAT (3V~4.3V). When the voltage of the VBAT is reduced during use, the
range of ADC will also be reduced. If the input voltage of ADC PIN exceeds its range, it is necessary to
implement the resistance partial pressure on the hardware
The electronic specifications are shown in the following table.
Table 18: ADC electronic characteristics
Characteristics
Min.
Typ.
Max.
Unit
Resolution
–
–
15
Bits
Input Range
0
VBAT
V
Input serial resistance
1
–
–
MΩ
“AT+CADC” can be used to read the voltage of the ADC pin, for more details, please refer to document
[1].
3.9.2 LDO
SIM7000 has a LDO power output named VDD_EXT. The output voltage is 1.8V. This voltage can only be
pulled up for the external GPIO or power supply for the level conversion circuit.
Figure 25：Power on sequence of the VDD_EXT
Table 19: Electronic characteristic
Symbol
Description
Min.
Typ.
Max.
Unit
VDD_EXT
Output voltage
1.7
1.8
1.9
V
IO
Output current
-
-
50
mA
NOTE

---

## Page 37
SIM7000 Series Hardware Design V1.09
www.simcom.com
37/69
The VDD_EXT is used to the IO power in the module. The Output voltage is not supported to adjust.
NOTE

---

## Page 38
SIM7000 Series Hardware Design V1.09
www.simcom.com
38/69
4 RF Specifications
GSM/LTE RF Specifications
Table 20: Conducted transmission power
Frequency
Power
Min.
EGSM900
33dBm ±2dB
5dBm ± 5dB
DCS1800
30dBm ±2dB
0dBm ± 5dB
LTE-FDD B1
23dBm +/-2.7dB
<-40dBm
LTE-FDD B2
23dBm +/-2.7dB
<-40dBm
LTE-FDD B3
23dBm +/-2.7dB
<-40dBm
LTE-FDD B4
23dBm +/-2.7dB
<-40dBm
LTE-FDD B5
23dBm +/-2.7dB
<-40dBm
LTE-FDD B6
23dBm +/-2.7dB
<-40dBm
LTE-FDD B8
23dBm +/-2.7dB
<-40dBm
LTE-FDD B12
23dBm +/-2.7dB
<-40dBm
LTE-FDD B13
23dBm +/-2.7dB
<-40dBm
LTE-FDD B18
23dBm +/-2.7dB
<-40dBm
LTE-FDD B19
23dBm +/-2.7dB
<-40dBm
LTE-FDD B20
23dBm +/-2.7dB
<-40dBm
LTE-FDD B26
23dBm +/-2.7dB
<-40dBm
LTE-FDD B28
23dBm +/-2.7dB
<-40dBm
LTE-FDD B39
23dBm +/-2.7dB
<-40dBm
The max power is tested result for 1RB in CAT-M1 and single-tone in CAT-NB1. MPR for CAT-M1
please refer to 6.2.3EA.5 part for 3GPP. Multi-tone test results please refer to part 6.2.3F.3 for
CAT-NB1.
Table 21: Maximum Power Reduction (MPR) for UE category NB1 Power Class 3
Modulation
QPSK
Tone positions for 3 Tones
allocation
0-2
3-5 and 6-8
9-11
MPR
≤0.5 dB
0 dB
≤0.5 dB
NOTE

---

## Page 39
SIM7000 Series Hardware Design V1.09
www.simcom.com
39/69
Tone positions for 6 Tones
allocation
0-5 and 6-11
MPR
≤1 dB
≤1 dB
Tone
positions
for
12
Tones allocation
0-11
MPR
≤2 dB
Table 22: Operating frequencies
Frequency
Receiving
Transmission
EGSM900
925～960MHz
880～915 MHz
GSM850
869~894MHz
824~849 MHz
DCS1800
1805～1880 MHz
1710～1785 MHz
PCS1900
1844.9~1879.9MHz
1749.9~1784.9MHz
GPS L1 BAND
1574.4 ～1576.44 MHz
-
GLONASS
1598 ～1606 MHz
-
BD
1559～1563 MHz
LTE BAND
Refers to Table 22
Table 23: E-UTRA operating bands
E-UTRA
UL Freq.
DL Freq.
Duplex Mode
1
1920 ~1980 MHz
2110 ~2170 MHz
HD-FDD
3
1710 ~1785 MHz
1805 ~1880 MHz
HD-FDD
5
824 ~849 MHz
869 ~894 MHz
HD-FDD
6
830 ~840 MHz
875 ~885 MHz
HD-FDD
8
880 ~915 MHz
925 ~960 MHz
HD-FDD
12
699 ~716 MHz
729 ~746 MHz
HD-FDD
13
777 ~787 MHz
746 ~756 MHz
HD-FDD
18
815 ~830 MHz
860 ~875 MHz
HD-FDD
19
830 ~845 MHz
875 ~890 MHz
HD-FDD
20
832 ~862 MHz
791 ~821 MHz
HD-FDD
26
814 ~849 MHz
859 ~894 MHz
HD-FDD
28
703 ~748 MHz
758 ~803 MHz
HD-FDD
39
1880 ~1920 MHz
1880 ~1920 MHz
TDD
Table 24: Conducted receive sensitivity
Frequency
Receive sensitivity(Typical)
Receive sensitivity(MAX)
EGSM900
< -109dBm
3GPP
GSM850
< -109dBm
3GPP
DCS1800
< -109dBm
3GPP

---

## Page 40
SIM7000 Series Hardware Design V1.09
www.simcom.com
40/69
PCS1900
< -109dBm
3GPP
LTE FDD/TDD
Refers to Table 24
Table 25: CAT-M1 Reference sensitivity (QPSK)
E-UTRA Band
REFSENS MAX(dBm)
3GPP
REFSENS
Typical(dBm)
Duplex Mode
1
-102.2
-108.2
HD-FDD
2
-100.2
-107.5
HD-FDD
3
-99.2
-107.3
HD-FDD
4
-102.2
-108.6
HD-FDD
5
-100.7
-107.3
HD-FDD
8
-99.7
-107.7
HD-FDD
12
-99.2
-107.3
HD-FDD
13
-98.7
-107.3
HD-FDD
18
-102.2
-107.3
HD-FDD
19
-102.2
-107
HD-FDD
20
-99.7
-107.2
HD-FDD
26
-100.2
-107
HD-FDD
28
-100.7
-107.3
HD-FDD
Table 26: CAT-NB1 Reference sensitivity (QPSK)
Operating band
REFSENS
(dBm) 3GPP
Request
REFSENS
Typical
(dBm)
REFSENS Typical
Repeated 7/128
[EPREdBm/15KHz]
1, 2, 3, 4,5, 8, 12, 13, 17, 18, 19, 20, 26,
28
-108.2
-114
-145

---

## Page 41
SIM7000 Series Hardware Design V1.09
www.simcom.com
41/69
GSM/LTE Antenna Design Guide
Users should connect antennas to SIM7000’s antenna pads through micro-strip line or other types of RF
trace and the trace impedance must be controlled in 50Ω. SIMCom recommends that the total insertion loss
between the antenna pads and antennas should meet the following requirements:
Table 27: Trace loss
Frequency
Loss
700MHz-960MHz
<0.5dB
1710MHz-2170MHz
<0.9dB
2300MHz-2650MHz
<1.2dB
To facilitate the antenna tuning and certification test, a RF connector and an antenna matching circuit
should be added. The following figure is the recommended circuit.
Figure 26: Antenna matching circuit (MAIN_ANT)
In above figure, the components R1, C1, C2 and R2 are used for antenna matching, the values of
components can only be achieved after the antenna tuning and usually provided by antenna vendor. By
default, the R1, R2 are 0Ω resistors, and the C1, C2 are reserved for tuning. The component D1 is a TVS
for ESD protection, and it is optional for users according to application environment.
The RF test connector is used for the conducted RF performance test, and should be placed as close as to
the module’s MAIN_ANT pin. The traces impedance between SIM7000 and antenna must be controlled in
50Ω.
Two TVS are recommended in the table below.
Table 28: Recommended TVS
Package
Part Number
Vender
0201
LXES03AAA1-154
Murata
0402
LXES15AAA1-153
Murata

---

## Page 42
SIM7000 Series Hardware Design V1.09
www.simcom.com
42/69
GNSS
SIM7000
merges
GNSS
(GPS/GLONASS/BD)
satellite
and
network
information
to
provide
a
high-availability solution that offers industry-leading accuracy and performance. This solution performs well,
even in very challenging environmental conditions where conventional GNSS receivers fail, and provides a
platform to enable wireless operators to address both location-based services and emergency mandates.
4.3.1 GNSS Technical specification

Tracking sensitivity: -162 dBm（GPS）/-157 dBm（GLONASS）/TBD (BD)

Cold-start sensitivity: -148 dBm

Accuracy (Open Sky): 2.5m (CEP50)

TTFF (Open Sky) : Hot start <1s, Cold start<35s

Receiver Type: 16-channel, C/A Code

GPS L1 Frequency: 1575.42±1.023MHz

GLONASS: 1597.5~1605.8 MHz

BD: 1559.05~1563.14 MHz

Update rate: Default 1 Hz

GNSS data format: NMEA-0183

GNSS Current consumption :30mA (GSM/LTE Sleep, in total on VBAT pins)

GNSS antenna: Passive/Active antenna
If the antenna is active type, the power should be given by main board because there is no power
supply on the GPS antenna pad. If the antenna is passive, it is suggested that the external LNA should
be used.
4.3.2 GNSS Application Guide
Users can adopt an active antenna or a passive antenna to SIM7000. If using a passive antenna, an
external LNA is a must to get better performance. The following figures are the reference circuits.
NOTE

---

## Page 43
SIM7000 Series Hardware Design V1.09
www.simcom.com
43/69
Figure 27: Active antenna circuit
Figure 28: Passive antenna circuit (Default)
In above figures, the components C1, L1 and L2 are used for antenna matching. Usually, the values of the
components can only be achieved after antenna tuning and usually provided by antenna vendor.C2 is used
for DC blocking. L3 is the matching component of the external LNA, and the value of L3 is determined by
the LNA characteristic and PCB layout. Both VDD of active antenna and V_LNA need external power
supplies which should be considered according to active antenna and LNA characteristic. LDO/DCDC is
recommended to get lower current consuming by shutting down active antennas and LNA when GNSS is
not working.
GNSS can be tested by NMEA port. NMEA sentences can be obtained through UART or USB automatically.
NMEA sentences include GSV, GGA, RMC, GSA, and VTG. Before using GNSS, user should configure
SIM7000 in proper operating mode by AT command. Please refer to related documents for details. SIM7000
can also get position location information through AT directly.
1. GNSS is closed by default and can be started by “AT+CGNSPWR=1”. The AT command has two
parameters, the first is on/off, and the second is GNSS mode. Default mode is standalone mode.
AGPS mode needs more support from the mobile telecommunication network. Please refer to
NOTE

---

## Page 44
SIM7000 Series Hardware Design V1.09
www.simcom.com
44/69
document [21] for more details.
2. If the passive antenna is used, put the LNA close to the antenna.
3. Make sure there are no noise signals around GNSS antenna.
RF traces note
4.4.1 RF traces layout

Keep the RF trace from module ant pin to antenna as short as possible

RF trace should be 50 Ωeither on the top layer or in the inner layer

RF trace should be avoided right angle and sharp angle.

Put enough GND vias around RF traces.

RF trace should be far away from other high speed signal lines.
Figure 29: RF trace should be far away from other high speed signal lines

Avoiding the paroling rout of other system antennas nearly.

There should be some distance from The GND to the inner conductor of the SMA connector. It is better
to keep out all the layers from inner to the outer conductor.

---

## Page 45
SIM7000 Series Hardware Design V1.09
www.simcom.com
45/69
Figure 30: The distance between GND to the inner conductor of SMA

GND pads around the ANT pad should not be hot pad to keep the GND complete.
4.4.2 LTE ANT and other system ANT decoupling

Make sure the efficiency of LTE main ANT more than 40%

Keep the decoupling of LTE main ANT to WLAN ANT more than 15dB

Keep the decoupling of LTE main ANT to GNSS ANT more than 30dB
The decoupling value can be provided by ANT adventure. More details can refer to thedocument[22].
NOTE

---

## Page 46
SIM7000 Series Hardware Design V1.09
www.simcom.com
46/69
5 Electrical Specifications
Absolute maximum ratings
Absolute maximum rating for digital and analog pins of SIM7000 are listed in the following table:
Table 29: Absolute maximum ratings
Parameter
Min.
Typ.
Max.
Unit
Voltage on VBAT
-0.3
-
5.5
V
Voltage on USB_VBUS
-0.3
-
5.8
V
Voltage at digital pins
(RESET,GPIO,I2C,UART,PCM)
-0.3
-
2.1
V
Voltage at PWRKEY
-0.3
-
3.4
V
ADC
-0.3
-
VBAT
V
The absolute parameter is tested when VBAT has the power but the PWRKEY has no pulled down. If it is
over the range, the module will be damage. If the power supply on VBAT pin had been shut down, and the
other pin should not have the voltage. Otherwise, it may lead to abnormally boot up or damage the module.
Operating conditions
Table 30: Recommended operating ratings
Parameter
Min.
Typ.
Max.
Unit
Voltage at VBAT
3.0
3.8
4.3
V
Voltage at USB_VBUS
3.5
5.0
5.25
V
Make sure that the voltage on the VBAT pins will never drop below 3.0V, even during a transmit burstwhen
current consumption may rise up to 2A. If the voltage drops below 3.0V, module will be power down.
Table 31: 1.8V Digital I/O characteristics*
Parameter
Description
Min.
Typ.
Max.
Unit
VIH
High-level input voltage
1.17
1.8
2.1
V
VIL
Low-level input voltage
-0.3
0
0.63
V
VOH
High-level output voltage
1.35
-
1.8
V
VOL
Low-level output voltage
0
-
0.45
V
IOH
High-level output current(no pull
-
2
-
mA

---

## Page 47
SIM7000 Series Hardware Design V1.09
www.simcom.com
47/69
down resistor)
IOL
Low-level output current(no pull
up resistor)
-
-2
-
mA
IIH
Input high leakage current (no
pull down resistor)
-
-
1
uA
IIL
Input low leakage current(no pull
up resistor)
-1
-
-
uA
These parameters are for digital interface pins, such as GPIOs (including NETLIGHT,STATUS,
SIM_DET), I2C, UART, PCM, MDM_LOG_TX and BOOT_CFG.
The operating temperature of SIM7000 is listed in the following table.
Table 32: Operating temperature
Parameter
Min.
Typ.
Max.
Unit
Normal operation temperature
-30
25
80
℃
Extended operation temperature*
-40
25
85
℃
Storage temperature
-45
25
+90
℃
Module is able to make and receive voice calls, data calls, SMS and make GPRS/LTE traffic in -40℃~
+85 ℃. The performance will be reduced slightly from the 3GPP specifications if the temperature is
outside the normal operating temperature range and still within the extreme operating temperature
range.
NOTE
NOTE

---

## Page 48
SIM7000 Series Hardware Design V1.09
www.simcom.com
48/69
Operating Mode
5.3.1 Operating Mode Definition
The table below summarizes the various operating modes of SIM7000 product.
Table 33: Operating mode Definition
Mode
Function
Normal operation
GPRS/EDGE/LTE
Sleep
In this case, the current consumption of module will be reduced to the
minimal level and the module can still receive paging message and
SMS.
GPRS/EDGE /LTE Idle
Software is active. Module is registered to the network, and the module
is ready to communicate.
LTECat-M1Talk
Connection between two subscribers is in progress. In this case, the
power consumption depends on network settings such as DTX off/on,
FR/EFR/HR, hopping sequences, and antenna.
GPRS/EDGE/LTE
Standby
Module is ready for data transmission, but no data is currently sent or
received. In this case, power consumption depends on network
settings.
GPRS/EDGE/LTE
Data transmission
There
is
data
transmission
in
progress.
In
this
case,
power
consumption is related to network settings (e.g. power control level);
uplink/downlink data rates, etc.
Minimum functionality mode
AT command “AT+CFUN=0” and “AT+CSCLK=1”can be used to set
the module to a minimum functionality mode without removing the
power supply. In this mode, the RF part of the module will not work and
the SIM card will not be accessible, but the serial port and USB ports
are still accessible. The power consumption in this mode is lower than
normal mode.
Flight mode
AT command “AT+CFUN=4”can be used to set the module to flight
mode without removing the power supply. In this mode, the RF part of
the module will not work, but the serial port and USB ports are still
accessible. The power consumption in this mode is lower than normal
mode.
Power Saving Mode (PSM)
Setting AT command” AT+CPSMS=1” can be enable the PSM mode. In
this mode, The mode is similar to power-off. But the module remains
registered on the network and there is no need to re-attach or
re-establish the network connections. And all of the functions will be
unavailable except the RTC function. PWRKEY admit expires can
wake up the module.
Extended
Mode
DRX
(e-DRX)
In idle or sleep mode, module and the network may negotiate over
non-access stratum signaling the use of extended mode DRX for
reducing power consumption.

---

## Page 49
SIM7000 Series Hardware Design V1.09
www.simcom.com
49/69
5.3.2 Sleep mode
Module can enter into sleep mode for reducing its power consumption in idle module. In sleep mode, the
current consumption of module will be reduced to very small level, and module can still receive paging
message and SMS.
Several hardware and software conditions must be satisfied together in order to let SIM7000 enter sleep
mode:

USB condition: Connected USB can’t enter into sleep mode. So if module wants to enter into sleep
mode, it must disconnect the power supply for USB_VBUS first.

Software condition: If module wants to enter into sleep mode, AT comment “AT+CSCLK=1” must be set
to close some clock in the module. If the value “AT+CSCLK” is “0”, module will never enter into sleep
mode.

UART condition: If module wants to enter into sleep mode, AT comment “AT+CSCLK=1” must be set to
close some clock in the module. If the value “AT+CSCLK” is “0”, module will never enter into sleep
mode.
If it meets all the conditions at the same time, module will enter into sleep mode. In sleep mode, the UART
is unavailable. If the host need to communicate with module, it need to pull down DTR can wake upmodule.
5.3.3 Minimum functionality mode and Flight mode
There are three functionality modes, which could be set by the AT command “AT+CFUN=<fun>”. The
command provides the choice of the functionality levels <fun>=0, 1, 4.

AT+CFUN=0: Minimum functionality

AT+CFUN=1: Full functionality (Default)

AT+CFUN=4: Flight mode
If SIM7000 has been set to minimum functionality mode, the RF function and SIM card function will be
closed. In this case, the serial port and USB are still accessible, but RF function and SIM card will be
unavailable.
If SIM7000 has been set to flight mode, the RF function will be closed. In this case, the serial port and USB
are still accessible, but RF function will be unavailable.
When SIM7000 is in minimum functionality or flight mode, it can return to full functionality by the AT
command “AT+CFUN=1”.
5.3.4 Power Saving Mode (PSM)
SIM7000 module can enter into PSM for reducing its power consumption. The mode is similar to power-off,
but the module remains registered on the network and there is no need to re-attach or re-establish the

---

## Page 50
SIM7000 Series Hardware Design V1.09
www.simcom.com
50/69
network connections. So in PSM all the functions will be unavailable except the RTC function, module
cannot immediately respond users’ requests.
When the module wants to use the PSM, it can be enabled via “AT+CPSMS=1” command. The command
takes effect after module reboot. If the network supports PSM and accepts that the module uses PSM, the
network confirms usage of PSM by allocating an Active Time value to the module. Module will be into PSM
according to the command from network.
Either of the following methods will wake up the module from PSM:

Pulling PWRKEY pin to low level will wake up the module.

When the timer expires, the module will be automatically woken up.
Current Consumption
The current consumption is listed in the table below.
Table 34: Current consumption on VBAT Pins (VBAT=3.8V)
GNSS
GNSS supply current
(AT+CFUN=0,without USB connection)
Tracking, typical: 30mA
In DPO mode, typical: 6mA
GSM sleep/idle mode
GSM supply current
(GNSS off，without USB connection)
Sleep mode@BS_PA_MFRMS=2Typical: 1.7mA
Idle mode@BS_PA_MFRMS=2
Typical: 11.4mA
LTE sleep/idle mode
LTE supply current
(GNSS off，without USB connection)
Sleep modeTypical: 1.2mA
Idle mode Typical: 11mA
Power SavingMode
PSM supply current
PSM mode Typical: 9uA
LTE Cat-M1 Talk
TBD
TBD
TBD
TBD
GPRS
EGSM900( 2 Rx,4 Tx )
@power level #5 Typical:422mA
DCS1800( 2 Rx,4 Tx )
@power level #0Typical:345mA
EGSM900( 3Rx, 2 Tx )
@power level #5 Typical:321mA
DCS1800( 3Rx, 2 Tx )
@power level #0Typical:249mA
EDGE
EGSM900( 2 Rx,4 Tx )
@power level #8Typical:426mA
DCS1800( 2 Rx,4 Tx )
@power level #2Typical:327mA

---

## Page 51
SIM7000 Series Hardware Design V1.09
www.simcom.com
51/69
EGSM900( 3Rx, 2 Tx )
@power level #8Typical:263mA
DCS1800( 3Rx, 2 Tx )
@power level #2Typical:200mA
LTE Cat-M
LTE-FDD B1
@23dbm Typical: 161mA
@10dbm Typical: 111mA
@0dbm Typical: 98mA
LTE-FDD B2
@23dbmTypical: 160mA
@10dbm Typical: 116mA
@0dbm Typical: 102mA
LTE-FDD B3
@23dbmTypical: 150mA
@10dbm Typical: 110mA
@0dbm Typical: 102 mA
LTE-FDD B4
@23dbmTypical: 150mA
@10dbm Typica : 114mA
@0dbm Typical: 102mA
LTE-FDD B5
@23dbmTypical: 168mA
@10dbm Typical: 117mA
@0dbm Typical: 113mA
LTE-FDD B8
@23dbmTypical: 165mA
@10dbm Typical: 110mA
@0dbm Typical: 98mA
LTE-FDD B12
@23dbmTypical: 167mA
@10dbm Typical: 109mA
@0dbm Typical: 96mA
LTE-FDD B13
@23dbmTypical: 168mA
@10dbm Typical: 114mA
@0dbm Typical: 97mA
LTE-FDD B18
@23dbmTypical: 167mA
@10dbm Typical: 109mA
@0dbm Typical: 98mA
LTE-FDD B19
@23dbmTypical: 171mA
@10dbm Typical: 110mA
@0dbm Typical: 99mA
LTE-FDD B20
@23dbmTypical: 167mA
@10dbm Typical: 110mA
@0dbm Typical: 98mA
LTE-FDD B26
@23dbmTypical: 168mA
@10dbm Typical: 109mA
@0dbm Typical: 98mA
LTE-FDD B28
@23dbmTypical: 195mA
@10dbm Typical: 135mA
@0dbm Typical: 115mA
LTE Cat-NBdata transmission
B5
UL mac padding _15KHZ_1RU_1 subcarrier_0dbm
59.94 mA
UL mac padding _15KHZ_1RU_1 subcarrier_10dbm
68.48 mA
UL mac padding _15KHZ_1RU_1 subcarrier_23dbm
143.22 mA
UL mac padding _3.75KHZ_1RU_1 subcarrier_0dbm
83.60 mA
UL mac padding _3.75KHZ_1RU_1 subcarrier_10dbm
100.03 mA
UL mac padding _3.75KHZ_1RU_1 subcarrier_23dbm
244.96 mA
UL mac padding _15KHZ_12subcarrier_23dbm
92mA
DL mac padding _15KHZ_12subcarrier_23dbm
66.42mA

---

## Page 52
SIM7000 Series Hardware Design V1.09
www.simcom.com
52/69
B8
UL mac padding _15KHZ_1RU_1 subcarrier_0dbm
60.42 mA
UL mac padding _15KHZ_1RU_1 subcarrier_10dbm
69.54 mA
UL mac padding _15KHZ_1RU_1 subcarrier_23dbm
144.60 mA
UL mac padding _3.75KHZ_1RU_1 subcarrier_0dbm
83.84 mA
UL mac padding _3.75KHZ_1RU_1 subcarrier_10dbm
101.37 mA
UL mac padding _3.75KHZ_1RU_1 subcarrier_23dbm
248.67 mA
UL mac padding _15KHZ_12subcarrier_23dbm
93mA
DL mac padding _15KHZ_12subcarrier_23dbm
68.4mA
ESD Notes
SIM7000 is sensitive to ESD in the process of storage, transporting, and assembling. When SIM7000 is
mounted on the users’ mother board, the ESD components should be placed beside the connectors which
human body may touch, such as SIM card holder, audio jacks, switches, keys, etc. The following table
shows the SIM7000 ESD measurement performance without any external ESD component.
Table 35: The ESD performance measurement table (Temperature: 25℃, Humidity: 45%.)
Part
Contact discharge
Air discharge
VBAT,GND
+/-6K
+/-12K
Antenna port
+/-5K
+/-10K
Other PADs
+/-1K
+/-3K

---

## Page 53
SIM7000 Series Hardware Design V1.09
www.simcom.com
53/69
6 Electrical Specifications
Top and Bottom View of SIM7000
Figure 31: Top and bottom view of SIM700

---

## Page 54
SIM7000 Series Hardware Design V1.09
www.simcom.com
54/69
Label Information
Figure 32: Label information
Table 35: The description of label information
No.
Description
A
LOGO
B
No.1 Pin
C
Project name
D
Product code
E
Serial number
F
International mobile equipment identity
G
QR code

---

## Page 55
SIM7000 Series Hardware Design V1.09
www.simcom.com
55/69
Typical SMT Reflow Profile
SIMCom provides a typical soldering profile. Therefore the soldering profile shown below is only a generic
recommendation and should be adjusted to the specific application and manufacturing constraints.
Figure 33: The ramp-soak-spike reflow profile of SIM7000
For more details about secondary SMT, please refer to the document [19].
NOTE

---

## Page 56
SIM7000 Series Hardware Design V1.09
www.simcom.com
56/69
Moisture Sensitivity Level (MSL)
SIM7000 is qualified to Moisture Sensitivity Level (MSL) 4 in accordance with JEDEC J-STD-033.
The following table shows the features of Moisture Sensitivity Level (MSL). After seal off, storage conditions
must meet the following table. If the storage time was expired, module must be baking before SMT.
Table 37: Moisture Sensitivity Level and Floor Life
Moisture Sensitivity
Level (MSL)
Floor Life (out of bag) at factory ambient≤30°C/60% RH or
as stated
1
Unlimited at ≦30℃/85% RH
2
1 year at ≦30℃/60% RH
2a
4 weeks at ≦30℃/60% RH
3
168 hours at ≦30℃/60% RH
4
72 hours at ≦30℃/60% RH
5
48 hours at ≦30℃/60% RH
5a
24 hours at ≦30℃/60% RH
6
Mandatory bake before use. After bake, it must be reflowed within the
time limit specified on the label.
Baking
In order to get better yield, the module need to bake before SMT.

If the packaging is in perfect condition, the module which dateofproduction is within six months has
no use for baking. If the dateofproduction is more than six months, the module must be baking.

If the packaging had been opened or damaged, the module must be baking.
Table 38: Baking conditions
conditions
parameters
Baking temperature
120℃
Baking time
8 hours
IPC / JEDEC J-STD-033standard must be followed for production and storage.
NOTE

---

## Page 57
SIM7000 Series Hardware Design V1.09
www.simcom.com
57/69
Stencil Foil Design Recommendation
The recommended thickness of stencil foil is 0.15mm.
Figure 34: stencil recommendation (Unit: mm)

---

## Page 58
SIM7000 Series Hardware Design V1.09
www.simcom.com
58/69
7 Electrical Specifications
Tray packaging
SIM7000 module support tray packaging.
Figure 35: packaging diagram
Module tray drawing：
Figure 36: Tray drawing

---

## Page 59
SIM7000 Series Hardware Design V1.09
www.simcom.com
59/69
Table 39: Tray size
Length（±3mm）
Width（±3mm）
Module number
242.0
161.0
20
Small carton drawing：
Figure 37: Small carton drawing
Table 40: Small Carton size
Length（±10mm）Width（±10mm）
Height（±10mm）
Module number
270
180
120
20*20=400
Big carton drawing：
Figure 38: Big carton drawing

---

## Page 60
SIM7000 Series Hardware Design V1.09
www.simcom.com
60/69
Table 41: Big Carton size
Length（±10mm）Width（±10mm）
Height（±10mm）
Module number
380
280
280
400*4=1600

---

## Page 61
SIM7000 Series Hardware Design V1.09
www.simcom.com
61/69
8 Appendix
Reference Design
Refer to <SIM7000 Reference Design V1.01> for the details.
Figure 39: Reference design

---

## Page 62
SIM7000 Series Hardware Design V1.09
www.simcom.com
62/69
Design check list
Table 42: SchematicCheck List
NO.
Items
1
Insure the supply voltage for VBAT is withintherangeof3V~4.3V.
2
Insure the maximum supply current for VBAT is above its consumption when it is maximum
power emission. The maximum current is 2A during GPRS/EDGE emission maximum power,
and it 0.6A during LTE emission maximum power.
3
Insure the capacitor for VBAT is meet its request, in order to avoid the voltage drop exceed
300mV. And the voltage never dropped below 3V.
4
Insure the input signal for PWRKEY pin meet its electrical level match. It recommended use
BJT to shift its level.
5
Insure the input signal for NRESET pin meet its electrical level match.
6
Insure the netconnections of UART be correct ness according to signal direction. Insure the
signal for UART pins meet its electrical level match. It recommended use BJT or level shift IC
to shift its level.
7
Insure USB port had used TVS to protect signal. And the junction capacity of TVS for DP/DM
must be less than 1pf.
8
Insure SIM card signal had used TVS to protect. And the junction capacity of TVS must be
less than 50pf.
9
Insure SIM_DET had used resistor 10Kohm pull up to VDD_EXT if used this signal.
10
Insure I2C signal had used resistors 2.2Kohm pull up to VDD_EXT if used.
11
The electrical level of all GPIOs is 1.8V. Insure the signal for GPIO pins meet its electrical level
match.
12
The input range of ADC is 0V~VBAT. Insure the input signal never exceed its range.
13
User must pull up DTR when module enters into sleep mode. Insure DTR can be controlled by
host.
14
Suggesting to reserve test ports for VDD_EXT and BOOT_CFG. BOOT_CFG should keep
open before boot up.
15
The power supply of the active antenna should be controlled and closed.
16
LTE main ANT should have a PI type matching to debug antenna
17
LTE main ANT should Keep TVS to prevent ESD destroyed. And the TVS should be Low
junction capacitance.
Table 43: PCB LayoutCheck List
NO.
Items
1
Insure the capacitor placement for VBAT be near module pin.
2
Insure VBAT trace width be greater than 2mm. If NB only, insure VBAT trace width be greater
than 0.6mm. And the VIA number must be enough for getting through the current.
3
Insure the return path GND of the power supply is good. Insure the connectivity between
module GND and mother board GND is good.
4
Insure PCM trance is protected by GND, and keep it far from interference source, such as
power supply trace, USB trace, RF trace and so on.
5
Insure USB trance is protected by GND, and keep it far from interference source, such as
power supply trace, RF trace and so on. Insure DM/DP trace is differential routing, and
differential impedance is 90 ohm.
6
Insure ADC trance is protected by GND.

---

## Page 63
SIM7000 Series Hardware Design V1.09
www.simcom.com
63/69
7
Insure SIM card signal trance is protected by GND. Especially SIM_CLK must be protected
alone. And avoid signal trace branched Routing.
8
Insure I2C trance is protected by GND.
9
Insure TVS avoid bypass. The trace must go through TVS pad first, and then arrived module
pad.
10
There should be enough ground around the RF line. RF lines Routing prohibit right angles and
sharp angles, trying to trace circular or obtuse angle line.
11
The RF line reference GND should be complete. And avoid high speed lines crossing below it.
12
the GND side of the RF output pin should be no hot welding disk
13
The routing which is RF output PIN to antenna should be isolated from other high-speed lines.
And the routing should be 50Ωimpedance control.

---

## Page 64
SIM7000 Series Hardware Design V1.09
www.simcom.com
64/69
Coding Schemes and Maximum Net Data Rates over Air Interface
Table 44: Coding Schemes and Maximum Net Data Rates over Air Interface
Multislot definition(GPRS/EDGE)
Slot class
DL slot number
UL slot number
Active slot
number
1
1
1
2
2
2
1
3
3
2
2
3
4
3
1
4
5
2
2
4
6
3
2
4
7
3
3
4
8
4
1
5
9
3
2
5
10
4
2
5
11
4
3
5
12
4
4
5
GPRS coding scheme
Max data rata（4 slots）
Modulation type
CS 1 = 9.05 kb/s / time slot
36.2 kb/s
GMSK
CS 2 = 13.4 kb/s / time slot
53.6 kb/s
GMSK
CS 3 = 15.6 kb/s / time slot
62.4 kb/s
GMSK
CS 4 = 21.4 kb/s / time slot
85.6 kb/s
GMSK
EDGE coding scheme
Max data rata（4 slots）
Modulation type
MCS 1 = 8.8 kb/s/ time slot
35.2 kb/s
GMSK
MCS 2 = 11.2 kb/s/ time slot
44.8 kb/s
GMSK
MCS 3 = 14.8 kb/s/ time slot
59.2 kb/s
GMSK
MCS 4 = 17.6 kb/s/ time slot
70.4 kb/s
GMSK
MCS 5 = 22.4 kb/s/ time slot
89.6 kb/s
8PSK
MCS 6 = 29.6 kb/s/ time slot
118.4 kb/s
8PSK
MCS 7 = 44.8 kb/s/ time slot
179.2 kb/s
8PSK
MCS 8 = 54.4 kb/s/ time slot
217.6 kb/s
8PSK
MCS 9 = 59.2 kb/s/ time slot
236.8 kb/s
8PSK
LTE-FDD device category
(Downlink)
Max data rate（peak）
Modulation type
Category M1
1Mbps
QPSK/16QAM
LTE-FDD device category
(Uplink)
Max data rate（peak）
Modulation type
Category M1
375kbps
QPSK/16QAM

---

## Page 65
SIM7000 Series Hardware Design V1.09
www.simcom.com
65/69
Related Documents
Table 45: Related Documents
NO.
Title
Description
[1]
SIM7000 SeriesAT Command
ManualV1.xx
AT Command Manual
[2]
GSM 07.07
Digital cellular telecommunications (Phase 2+); AT command
set for GSM Mobile Equipment (ME)
[3]
GSM 07.10
Support GSM 07.10 multiplexing protocol
[4]
GSM 07.05
Digital cellular telecommunications (Phase 2+); Use of Data
Terminal Equipment – Data Circuit terminating Equipment
(DTE – DCE) interface for Short Message Service (SMS) and
Cell Broadcast Service (CBS)
[5]
GSM 11.14
Digital cellular telecommunications system (Phase 2+);
Specification of the SIM Application Toolkit for the Subscriber
Identity Module – Mobile Equipment (SIM – ME) interface
[6]
GSM 11.11
Digital cellular telecommunications system (Phase 2+);
Specification of the Subscriber Identity Module – Mobile
Equipment (SIM – ME) interface
[7]
GSM 03.38
Digital cellular telecommunications system (Phase 2+);
Alphabets and language-specific information
[8]
GSM 11.10
Digital cellular telecommunications system (Phase 2)；
Mobile Station (MS) conformance specification；Part 1:
Conformance specification
[9]
3GPP TS 51.010-1
Digital cellular telecommunications system (Release 5);
Mobile Station (MS) conformance specification
[10]
3GPP TS 34.124
Electromagnetic Compatibility (EMC) for mobile terminals and
ancillary equipment.
[11]
3GPP TS 34.121
Electromagnetic Compatibility (EMC) for mobile terminals and
ancillary equipment.
[12]
3GPP TS 34.123-1
Technical Specification Group Radio Access Network;
Terminal conformance specification; Radio transmission and
reception (FDD)
[13]
3GPP TS 34.123-3
User Equipment (UE) conformance specification; Part 3:
Abstract Test Suites.
[14]
EN 301 908-02 V2.2.1
Electromagnetic compatibility and Radio spectrum Matters
(ERM); Base Stations (BS) and User Equipment (UE) for
IMT-2000.
Third Generation cellular networks; Part 2:
Harmonized EN for IMT-2000, CDMA Direct Spread
(UTRA FDD) (UE) covering essential requirements of article
3.2 of the R&TTE Directive
[15]
EN 301 489-24 V1.2.1
Electromagnetic compatibility and Radio Spectrum Matters
(ERM); Electromagnetic Compatibility (EMC) standard for
radio equipment and services; Part 24: Specific conditions for
IMT-2000 CDMA Direct Spread (UTRA) for Mobile and
portable (UE) radio and ancillary equipment
[16]
IEC/EN60950-1(2001)
Safety of information technology equipment (2000)
[17]
3GPP TS 51.010-1
Digital cellular telecommunications system (Release 5);
Mobile Station (MS) conformance specification
[18]
2002/95/EC
Directive of the European Parliament and of the Council of 27
January 2003 on the restriction of the use of certain
hazardous substances in electrical and electronic equipment
(RoHS)
[19]
Module
Module secondary SMT Guidelines

---

## Page 66
SIM7000 Series Hardware Design V1.09
www.simcom.com
66/69
secondary-SMT-UGDV1.xx
[20]
SIM7000 Series UART
Application Note_V1.xx
This document describes how to use UART interface of
SIMCom modules.
[21]
ETSI EN 301 908-13
(ETSI TS 136521-1 R13.4.0)
IMT
cellular
networks;
Harmonized
EN
covering
the
essential requirements of article 3.2 of the R&TTE Directive;
Part 13
[22]
ANTENNA DESIGN
GUIDELINES FOR
MULTI-ANTENNA SYSTEM V1
01
Design notice for multi-antenna.

---

## Page 67
SIM7000 Series Hardware Design V1.09
www.simcom.com
67/69
Terms and Abbreviations
Table 46: Terms and Abbreviations
Abbreviation
Description
ADC
Analog-to-Digital Converter
ARP
Antenna Reference Point
BER
Bit Error Rate
BD
BeiDou
BTS
Base Transceiver Station
CS
Coding Scheme
CSD
Circuit Switched Data
CTS
Clear to Send
DAC
Digital-to-Analog Converter
DSP
Digital Signal Processor
DTE
Data Terminal Equipment (typically computer, terminal, printer)
DTR
Data Terminal Ready
DTX
Discontinuous Transmission
DAM
Downloadable Application Module
DPO
Dynamic Power Optimization
EFR
Enhanced Full Rate
EGSM
Enhanced GSM
EMC
Electromagnetic Compatibility
ESD
Electrostatic Discharge
ETS
European Telecommunication Standard
FCC
Federal Communications Commission (U.S.)
FD
SIM fix dialing phonebook
FDMA
Frequency Division Multiple Access
FR
Full Rate
GMSK
Gaussian Minimum Shift Keying
GNSS
Global Navigation Satellite System
GPRS
General Packet Radio Service
GPS
Global Positioning System
GSM
Global Standard for Mobile Communications
HR
Half Rate
I2C
Inter-Integrated Circuit
IMEI
International Mobile Equipment Identity
LTE
Long Term Evolution
MO
Mobile Originated
MS
Mobile Station (GSM engine), also referred to as TE
MT
Mobile Terminated

---

## Page 68
SIM7000 Series Hardware Design V1.09
www.simcom.com
68/69
NMEA
National Marine Electronics Association
PAP
Password Authentication Protocol
PBCCH
Packet Switched Broadcast Control Channel
PCB
Printed Circuit Board
PCS
Personal Communication System, also referred to as GSM 1900
RF
Radio Frequency
RMS
Root Mean Square (value)
RTC
Real Time Clock
SIM
Subscriber Identification Module
SMS
Short Message Service
SMPS
Switched-mode power supply
TDMA
Time Division Multiple Access
TE
Terminal Equipment, also referred to as DTE
TX
Transmit Direction
UART
Universal Asynchronous Receiver & Transmitter
VSWR
Voltage Standing Wave Ratio
SM
SIM phonebook
NC
Not connect
EDGE
Enhanced data rates for GSM evolution
ZIF
Zero intermediate frequency
WCDMA
Wideband Code Division Multiple Access
VCTCXO
Voltage control temperature-compensated crystal oscillator
SIM
Universal subscriber identity module
UMTS
Universal mobile telecommunications system
UART
Universal asynchronous receiver transmitter
PSM
Power saving mode
FD
SIM fix dialing phonebook
LD
SIM last dialing phonebook (list of numbers most recently dialed)
MC
Mobile Equipment list of unanswered MT calls (missed calls)
ON
SIM (or ME) own numbers (MSISDNs) list
RC
Mobile Equipment list of received calls
SM
SIM phonebook
NC
Not connect

---

## Page 69
SIM7000 Series Hardware Design V1.09
www.simcom.com
69/69
Safety Caution
Table 47: Safety Caution
Marks
Requirements
When in a hospital or other health care facility, observe the restrictions about the use
of mobiles. Switch the cellular terminal or mobile off, medical equipment may be
sensitive and not operate normally due to RF energy interference.
Switch off the cellular terminal or mobile before boarding an aircraft. Make sure it is
switched off. The operation of wireless appliances in an aircraft is forbidden to prevent
interference with
communication systems. Forgetting to think much of
these
instructions may impact the flight safety, or offend local legal action, or both.
Do not operate the cellular terminal or mobile in the presence of flammable gases or
fumes. Switch off the cellular terminal when you are near petrol stations, fuel depots,
chemical plants or where blasting operations are in progress. Operation of any
electrical equipment in potentially explosive atmospheres can constitute a safety
hazard.
Your cellular terminal or mobile receives and transmits radio frequency energy while
switched on. RF interference can occur if it is used close to TV sets, radios,
computers or other electric equipment.
Road safety comes first! Do not use a hand-held cellular terminal or mobile when
driving a vehicle, unless it is securely mounted in a holder for hands free operation.
Before making a call with a hand-held terminal or mobile, park the vehicle.
GSM cellular terminals or mobiles operate over radio frequency signals and cellular
networks and cannot be guaranteed to connect in all conditions, especially with a
mobile fee or an invalid SIM card. While you are in this condition and need emergent
help, please remember to use emergency calls. In order to make or receive calls, the
cellular terminal or mobile must be switched on and in a service area with adequate
cellular signal strength.
Some networks do not allow for emergency call if certain network services or phone
features are in use (e.g. lock functions, fixed dialing etc.). You may have to deactivate
those features before you can make an emergency call.
Also, some networks require that a valid SIM card be properly inserted in the cellular
terminal or mobile.

---
