Features
Triple-channel architecture for UI, EIS, and OIS data processing
"Always-on" experience with low power consumption for both accelerometer
and gyroscope
Smart FIFO up to 4.5 KB
Android compliant
±2/±4/±8/±16 g full scale
±125/±250/±500/±1000/±2000/±4000 dps full scale
SPI / I²C & MIPI I3C® v1.1 serial interface with main processor data
synchronization
Auxiliary SPI for OIS data output for gyroscope and accelerometer
OIS configurable from aux. SPI, primary interface (SPI / I²C & MIPI I3C® v1.1)
EIS dedicated channel on primary interface with dedicated filtering
Advanced pedometer, step detector, and step counter
Significant motion detection, tilt detection
Standard interrupts: free-fall, wake-up, 6D/4D orientation, click and double
click
Programmable finite state machine for accelerometer, gyroscope, and external
sensor data processing with high rate @ 960 Hz
Machine learning core with exportable features and filters for AI applications
Embedded adaptive self-configuration (ASC)
Embedded Qvar (electrostatic sensor) for user interface functions (tap, double
tap, triple tap, long press, L/R – R/L swipe)
Embedded analog hub for ADC and processing analog input data
Embedded sensor fusion low-power algorithm
Embedded temperature sensor
Analog supply voltage: 1.71 V to 3.6 V
Independent IO supply (extended range: 1.08 V to 3.6 V)
Power consumption: 0.65 mA in combo high-performance mode
Compact footprint: 2.5 mm x 3 mm x 0.83 mm
ECOPACK and RoHS compliant
Applications
Motion tracking and gesture detection, augmented reality (AR) / virtual reality
(VR) / mixed reality (MR) applications & metaverse applications
Wearables
Indoor navigation
IoT and connected devices
Smartphones and handheld devices
EIS and OIS for camera applications
Vibration monitoring and compensation
LSM6DSV16X
LGA-14L
(2.5 x 3.0 x 0.83 mm) typ.
Product status link
LSM6DSV16X
Product summary
Order code LSM6DSV16X LSM6DSV16XTR
Temp. range
[°C] -40 to +
Package (2.5 x 3.0 x 0.83 mm)LGA-14L
Packing Tray Tape and reel
Product resources
AN5763 (device application note)
AN5882 (finite state machine)
AN5804 (machine learning core)
AN5755 (Qvar sensing)
TN0018 (design and soldering)
Product label
6-axis inertial measurement unit (IMU) and AI sensor
with embedded sensor fusion, Qvar for high-end applications
Datasheet
DS13510 - Rev 4 - May 2023
For further information contact your local STMicroelectronics sales office.

http://www.st.com
Description
The LSM6DSV16X is a high-performance, low-power 6-axis small IMU, featuring a 3-axis digital accelerometer
and a 3-axis digital gyroscope, that offers the best IMU sensor with a triple-channel architecture for processing
acceleration and angular rate data on three separate channels (user interface, OIS, and EIS) with dedicated
configuration, processing, and filtering.

The LSM6DSV16X enables processes in edge computing, leveraging embedded advanced dedicated features
such as a finite state machine (FSM) for configurable motion tracking and a machine learning core (MLC) for
context awareness with exportable AI features for IoT applications.

The LSM6DSV16X supports the adaptive self-configuration (ASC) feature, which allows the FSM to automatically
reconfigure the device in real time based on the detection of a specific motion pattern or based on the output of a
specific decision tree configured in the MLC, without any intervention from the host processor.

The LSM6DSV16X embeds Qvar (electric charge variation detection) for user interface functions like tap, double
tap, triple tap, long press, or L/R – R/L swipe.

The LSM6DSV16X embeds an analog hub able to connect an external analog input and convert it to a digital
signal for processing.

1 Overview
The LSM6DSV16X is a system-in-package featuring a high-performance 3-axis digital accelerometer and 3-axis
digital gyroscope.
The LSM6DSV16X delivers best-in-class motion sensing that can detect orientation and gestures in order to
empower application developers and consumers with features and capabilities that are more sophisticated than
simply orienting their devices to portrait and landscape mode.
The event-detection interrupts enable efficient and reliable motion tracking and context awareness, implementing
hardware recognition of free-fall events, 6D orientation, click and double-click sensing, activity or inactivity,
stationary/motion detection and wake-up events. Machine learning and finite state machine processing allow
moving some algorithms from the application processor to the LSM6DSV16X sensor, enabling consistent
reduction of power consumption.
The LSM6DSV16X supports the main OS requirements, offering real, virtual, and batch mode sensors. In
addition, the LSM6DSV16X can efficiently run the sensor-related features specified in Android, saving power
and enabling faster reaction time. In particular, the LSM6DSV16X has been designed to implement hardware
features such as significant motion detection, stationary/motion detection, tilt, pedometer functions, timestamping
and to support the data acquisition of external sensors.
The LSM6DSV16X offers hardware flexibility to connect the pins with different mode connections to external
sensors to expand functionalities such as adding a sensor hub, auxiliary SPI, and so forth.
The LSM6DSV16X offers advanced design flexibility for OIS and EIS applications. Both channels have a
dedicated processing path with independent filtering and enhanced EIS channel gyroscope data are read over the
primary interfaces I²C/ MIPI I3C® v1.1 / SPI.
Channel 1 has been designed for user interface data processing for motion tracking. Data are available on the
primary output of I²C / SPI / I3C® for the accelerometer and gyroscope with independent ODR and FS.
Channel 2 has been designed for OIS applications. Data are available on the aux SPI at 7.68 kHz with
accelerometer/gyroscope processing with independent FS at ±2 g - ±16 g (accelerometer) / ±125 dps - ±
dps (gyroscope). The accelerometer is also available as standalone with dedicated filtering.
Channel 3 has been design for enhanced EIS. Data are available in freerun mode in the output registers or in
FIFO with dedicated tag and timestamp.
Up to 4.5 KB of FIFO with compression and dynamic allocation of significant data (that is, external sensors,
timestamp, and so forth) allows overall power saving of the system.
The LSM6DSV16X embeds a sensor fusion low-power (SFLP) algorithm able to provide a 6-axis (accelerometer
+ gyroscope) game rotation vector represented as a quaternion. The X, Y, Z quaternion components are stored in
FIFO.
Like the entire portfolio of MEMS sensor modules, the LSM6DSV16X leverages the robust and mature in-house
manufacturing processes already used for the production of micromachined accelerometers and gyroscopes. The
various sensing elements are manufactured using specialized micromachining processes, while the IC interfaces
are developed using CMOS technology that allows the design of a dedicated circuit, which is trimmed to better
match the characteristics of the sensing element.
The LSM6DSV16X embeds an analog hub, which is able to connect an external analog input and convert it to a
digital signal for processing as well as advanced dedicated features like a finite state machine and data filtering
for OIS, EIS, and motion processing.
The LSM6DSV16X embeds Qvar functionality, which is an electrostatic sensor able to measure the variation of
the quasi-electrostatic potential. The Qvar sensing channel can be used for user interface applications like tap,
double tap, triple tap, long press, and L/R – R/L swipe.
The LSM6DSV16X is available in a small plastic land grid array (LGA) package of 2.5 x 3.0 x 0.83 mm to address
ultracompact solutions.
Overview
2 Embedded low-power features
The LSM6DSV16X has been designed to be fully compliant with Android, featuring the following on-chip
functions:
4.5 KB FIFO data buffering, data can be compressed two or three times
100% efficiency with flexible configurations and partitioning
Possibility to store timestamp
Event-detection interrupts (fully configurable)
Free-fall
Wake-up
6D orientation
Click and double-click sensing
Activity/inactivity recognition
Stationary/motion detection
Specific IP blocks (called "embedded functions") with negligible power consumption and high performance
Pedometer functions: step detector and step counters
Tilt
Significant motion detection
Finite state machine (FSM)
Machine learning core (MLC) with exportable features and filters for AI applications
Adaptive self-configuration (ASC)
Embedded sensor fusion low-power (SFLP) algorithm
Sensor hub
Up to six total sensors: two internal (accelerometer and gyroscope) and four external sensors
Analog hub for processing external analog input data
Qvar: electric charge variation detection
2.1 Pedometer functions: step detector and step counters
The LSM6DSV16X embeds an advanced pedometer with an algorithm running in an ultralow-power domain in
order to ensure extensive battery life in battery-constrained applications.
Leveraging enhanced configurability, the advanced embedded pedometer is suitable for a large range of
applications from mobile to wearable devices.
The algorithm processes and analyzes the accelerometer waveform in order to count the user's steps during
walking and running activities.
The pedometer works at 30 Hz and it is not affected by the selected device power mode (ultralow-power, low-
power, high-performance), thus guaranteeing an ultralow-power experience and extreme flexibility in conjunction
with other device functionalities.
The pedometer output can be batched in the device's FIFO buffer, in order to decrease overall system current
consumption.
ST freely provides the support and the tools for easily configuring the device and tuning the algorithm
configuration for a best-in-class user experience.
Embedded low-power features
2.2 Pedometer algorithm
The pedometer algorithm is composed of a cascade of four stages:
Computation of the acceleration magnitude signal in order to detect the signal independently from device
orientation;
FIR filter to extract relevant frequency components and to smooth the signal by cutting off high frequencies;
Peak detector to find the maximum and minimum of the waveform and compute the peak-to-peak value;
Step count: if the peak-to-peak value is greater than the settled threshold, a step is counted.
Figure 1. Four-stage pedometer algorithm
The LSM6DSV16X embeds a dynamic internal threshold for step detection that is updated after each peak-to-
peak evaluation: the internal threshold is increased with a configurable speed if a step is detected or decreased
with a configurable speed if a step is not detected.
This approach ensures high accuracy when the user starts to walk and a false peak rejection when the user is
walking or running.
An internal configurable debounce algorithm can be also set to filter false walks: indeed, an accelerometer pattern
is recognized as a walk or run only if a minimum number of steps are counted.
The LSM6DSV16X has been designed to reject a false-positive signal inside the algorithm core.
On top of the mechanisms detailed above, the LSM6DSV16X allows enabling and configuring a dedicated
false-positive rejection block to further boost pedometer accuracy.
2.3 Tilt detection
The tilt function helps to detect activity change and has been implemented in hardware using only the
accelerometer to achieve targets of both ultralow power consumption and robustness during the short duration of
dynamic accelerations.
The tilt function is based on a trigger of an event each time the device's tilt changes and can be used with
different scenarios, for example:
Triggers when a phone is in a front pants pocket and the user goes from sitting to standing or standing to
sitting;
Does not trigger when a phone is in a front pants pocket and the user is walking, running, or going upstairs.
2.4 Significant motion detection
The significant motion detection (SMD) function generates an interrupt when a ‘significant motion’, that could be
due to a change in user location, is detected. In the LSM6DSV16X device this function has been implemented in
hardware using only the accelerometer.
SMD functionality can be used in location-based applications in order to receive a notification indicating when the
user is changing location.
Pedometer algorithm
2.5 Finite state machine
The LSM6DSV16X can be configured to generate interrupt signals activated by user-defined motion patterns. To
do this, up to 8 embedded finite state machines can be programmed independently for motion detection such as
glance gestures, absolute wrist tilt, shake and double-shake detection.
Definition of finite state machine
A state machine is a mathematical abstraction used to design logic connections. It is a behavioral model
composed of a finite number of states and transitions between states, similar to a flow chart in which one can
inspect the way logic runs when certain conditions are met. The state machine begins with a start state, goes to
different states through transitions dependent on the inputs, and can finally end in a specific state (called stop
state). The current state is determined by the past states of the system. The following figure shows a generic
state machine.
Figure 2. Generic state machine
Finite state machine in the LSM6DSV16X
The LSM6DSV16X works as a combo accelerometer-gyroscope sensor, generating acceleration and angular rate
output data. It is also possible to connect an external sensor like a magnetometer or pressure sensor by using the
sensor hub feature (mode 2). These data can be used as input of up to 8 programs in the embedded finite state
machine (Figure 3. State machine in the LSM6DSV16X).
All 8 finite state machines are independent: each one has its dedicated memory area and it is independently
executed. An interrupt is generated when the end state is reached or when some specific command is performed.
Figure 3. State machine in the LSM6DSV16X
Finite state machine
2.6 Machine learning core
The LSM6DSV16X embeds a dedicated core for machine learning processing that provides system flexibility,
allowing some algorithms run in the application processor to be moved to the MEMS sensor with the advantage of
consistent reduction in power consumption.
Machine learning core logic allows identifying if a data pattern (for example motion, pressure, temperature,
magnetic data, and so forth) matches a user-defined set of classes. Typical examples of applications could be
activity detection like running, walking, driving, and so forth.
The LSM6DSV16X machine learning core works on data patterns coming from the accelerometer and gyro
sensors, but it is also possible to connect and process external sensor data (like magnetometer or pressure
sensor) by using the sensor hub feature (mode 2).
The input data can be filtered using a dedicated configurable computation block containing filters and features
computed in a fixed time window defined by the user. Computed feature values and filtered data values can also
be read through the FIFO buffer.
Machine learning processing is based on logical processing composed of a series of configurable nodes
characterized by "if-then-else" conditions where the "feature" values are evaluated against defined thresholds.
Figure 4. Machine learning core in the LSM6DSV16X
Machine
learning core
logical processing
Sensor
data
Computation
block
Decision
tree
Accelerometer
Gyroscope Results
External sensor
Features
Filters Meta-classifier
The LSM6DSV16X can be configured to run up to 4 decision trees simultaneously and independently and every
decision tree can generate up to 16 results. The total number of nodes can be up to 128.
The results of the machine learning processing are available in dedicated output registers readable from the
application processor at any time.
The LSM6DSV16X machine learning core can be configured to generate an interrupt when a change in the result
occurs.
2.7 Adaptive self-configuration (ASC)
The LSM6DSV16X supports the adaptive self-configuration (ASC) feature, which allows the FSM to automatically
reconfigure the device in real time based on the detection of a specific motion pattern or based on the output of a
specific decision tree configured in the MLC, without any intervention from the host processor. The FSM can write
a subset of the device registers using the SETR command, which allows indicating the register address and the
new value to be written in such a register. The access to these device registers is mutually exclusive to the host.
Machine learning core
2.8 Sensor fusion low power
A sensor fusion low-power (SFLP) block is available in the LSM6DSV16X for generating the following data based
on the accelerometer and gyroscope data processing:
Game rotation vector, which provides a quaternion representing the attitude of the device
Gravity vector, which provides a three-dimensional vector representing the direction of gravity
Gyroscope bias, which provides a three-dimensional vector representing the gyroscope bias
The SFLP block is enabled by setting the SFLP_GAME_EN bit to 1 of the EMB_FUNC_EN_A (04h) embedded
functions register.
The SFLP block can be reinitialized by setting the SFLP_GAME_INIT bit to 1 of the EMB_FUNC_INIT_A (66h)
embedded functions register.
Table 1. Sensor fusion performance
Parameter Value
Static accuracy
heading / yaw 0.5 deg. / 5 minutes
pitch 1.5 deg.
roll 1.5 deg.
Low dynamic accuracy
heading / yaw 0.7 deg. / 5 minutes
pitch 0.5 deg.
roll 0.5 deg.
High dynamic accuracy
heading / yaw 5.9 deg. / 5 minutes
pitch 1.6 deg.
roll 1.2 deg.
Calibration time 0.8 seconds(1)
Orientation stabilization time 0.7 seconds
1. Time required to reach steady state

Sensor fusion low power
3 Pin description
Figure 5. Pin connections
Ω Y
Ω R
Ω P
Z
Y
X
SDO/SA
BOTTOM
VIEW
SDx/AH1/Qvar
SCx/AH2/Qvar
INT
1
4
11
8
7 5
Vdd_IO
GNDGND
Vdd
INT
OCS_Aux
SDO_Aux
CSSCLSDA
Direction of detectable
acceleration (top view)
Direction of detectable
angular rate (top view)
Pin description
3.1 Pin connections
The LSM6DSV16X offers flexibility to connect the pins in order to have three different mode connections and
functionalities. In detail:
Mode 1 : I²C / MIPI I3C® slave interface or SPI (3- and 4-wire) serial interface is available. The analog hub
and Qvar functionalities are available in mode 1 with I²C interface only.
Mode 2 : I²C / MIPI I3C® slave interface or SPI (3- and 4-wire) serial interface and I²C interface master for
external sensor connections are available.
Mode 3: I²C / MIPI I3C® slave interface or SPI (3- and 4-wire) serial interface is available for the application
processor interface while an auxiliary SPI (3- and 4-wire) serial interface for external sensor connections is
available for the accelerometer and gyroscope.
Note: Refer to the product application note for the details regarding operating/power mode configurations, settings,
turn-on/off time and on-the-fly changes.

Figure 6. LSM6DSV16X connection modes
HOST
LSM6DSV16X
HOST
LSM6DSM
LESMxte6DrnaSMl^
sensors
I^2 C/
SPI ( 3 / 4 - w)
I^2 C/
SPI ( 3 / 4 - w)
Master I^2 C
Mode 1 Mode 2 Mode 3
HOST
I^2 C/
SPI ( 3 / 4 - w)
Aux SPI ( 3 / 4 - w) For XL and/or
gyro data
Camera
module
MIPI I3C/ MIPI I3C / (^) MIPI I3C /

LSM6DSV16X LSM6DSV16X
® ® ®
Pin connections
In the following table, each mode is described for the pin connections and function.
Table 2. Pin description
Pin# Name Mode 1 function Mode 2 function Mode 3 function
(^1) SDO/SA0(1)
SPI 4-wire interface serial data output
(SDO)
I²C least significant bit of the device
address (SA0)
SPI 4-wire interface serial data
output (SDO)
I²C least significant bit of the device
address (SA0)
SPI 4-wire interface serial data output
(SDO)
I²C least significant bit of the device
address (SA0)
2
SDx/AH1/
Qvar
Connect to Vdd_IO or GND if the analog
hub and Qvar are disabled.
AH input 1 (or Qvar electrode 1) is
connected if the analog hub (or Qvar
functionality) is enabled.
I²C serial data master (MSDA)
Auxiliary SPI 3/4-wire interface serial
data input (SDI_Aux)
and SPI 3-wire serial data output
(SDO_Aux)
3
SCx/AH2/
Qvar
Connect to Vdd_IO or GND if the analog
hub and Qvar are disabled.
AH input 2 (or Qvar electrode 2) is
connected if the analog hub (or Qvar
functionality) is enabled.
I²C serial clock master (MSCL)
Auxiliary SPI 3/4-wire interface serial
port clock (SPC_Aux)
4 INT1 Programmable interrupt in I²C and SPI
5 Vdd_IO(2) Power supply for I/O pins
6 GND 0 V supply
7 GND 0 V supply
8 Vdd(2) Power supply
9 INT
Programmable interrupt 2
(INT2) / Data enable (DEN)
Programmable interrupt 2 (INT2) /
Data enable (DEN) /
I²C master external synchronization
signal (MDRDY)
Programmable interrupt 2 (INT2) /
Data enable (DEN)
10 OCS_Aux
Connect to Vdd_IO or
leave unconnected(3)
Connect to Vdd_IO or
leave unconnected(3)
Enable auxiliary SPI 3/4-wire interface
11 SDO_Aux
Connect to Vdd_IO or
leave unconnected(3)
Connect to Vdd_IO or
leave unconnected(3)
Auxiliary SPI 3-wire interface: leave
unconnected(3)
Auxiliary SPI 4-wire interface: serial
data output (SDO_Aux)
12 CS(1)
I²C / MIPI I3C® / SPI mode selection
(1: SPI idle mode / I²C / MIPI I3C®
communication enabled;
0: SPI communication mode / I²C / MIPI
I3C® disabled)
I²C / MIPI I3C® / SPI mode
selection
(1: SPI idle mode / I²C / MIPI I3C®
communication enabled;
0: SPI communication mode / I²C /
MIPI I3C® disabled)
I²C / MIPI I3C® / SPI mode selection
(1: SPI idle mode / I²C / MIPI I3C®
communication enabled;
0: SPI communication mode / I²C /
MIPI I3C® disabled)
13 SCL(1)
I²C / MIPI I3C® serial clock (SCL)
SPI serial port clock (SPC)
I²C / MIPI I3C® serial clock (SCL)
SPI serial port clock (SPC)
I²C / MIPI I3C® serial clock (SCL)
SPI serial port clock (SPC)
(^14) SDA(1)
I²C / MIPI I3C® serial data (SDA)
SPI serial data input (SDI)
3-wire interface serial data output (SDO)
I²C / MIPI I3C® serial data (SDA)
SPI serial data input (SDI)
3-wire interface serial data output
(SDO)
I²C / MIPI I3C® serial data (SDA)
SPI serial data input (SDI)
3-wire interface serial data
output (SDO)

_1. SPI 3/4-wire interface not available with the analog hub / Qvar functionality enabled.

Recommended 100 nF filter capacitor.
Leave pin electrically unconnected and soldered to PCB._
Pin connections
4 Module specifications
4.1 Mechanical characteristics
@ Vdd = 1.8 V, T = 25 °C, unless otherwise noted.
Table 3. Mechanical characteristics
Symbol Parameter Test conditions Min. Typ.(1) Max. Unit
LA_FS Linear acceleration measurement range
±
g
±
±
±
G_FS Angular rate measurement range
±
dps
±
±
±
±
±
LA_So Linear acceleration sensitivity
FS = ±2 g 0.
m g /LSB
FS = ±4 g 0.
FS = ±8 g 0.
FS = ±16 g 0.
G_So Angular rate sensitivity(2)
FS = ±125 dps 4.
mdps/LSB
FS = ±250 dps 8.
FS = ±500 dps 17.
FS = ±1000 dps 35
FS = ±2000 dps 70
FS = ±4000 dps 140
G_So% Sensitivity tolerance(2) at component level ±0.3 %
LA_SoDr Linear acceleration sensitivity change vs. temperature(3) from -40° to +85° ±0.01 %/°C
G_SoDr Angular rate sensitivity change vs. temperature(3) from -40° to +85° ±0.007 %/°C
LA_TyOff Linear acceleration zero- g level offset accuracy(4) ±12 m g
G_TyOff Angular rate zero-rate level(4) ±1 dps
LA_OffDr Linear acceleration zero- g level change vs. temperature(3) ±0.07 m g /°C
G_OffDr Angular rate typical zero-rate level change vs. temperature(3) ±0.006 dps/°C
Rn Rate noise density in high-performance mode(5) 2.8 mdps/√Hz
RnRMS Gyroscope RMS noise in low-power mode(6) 60 mdps RMS
An
Acceleration noise density in high-performance mode(7) FS = ±2 g - ±16 g 60
μ g /√Hz
Acceleration noise density in normal mode(8)(9) FS = ±2 g - ±16 g^100
RMS Accelerometer RMS noise in low-power mode
LPM1 2.
LPM2 1.8 m g RMS
LPM3 1.
Module specifications
Symbol Parameter Test conditions Min. Typ.(1) Max. Unit
LA_ODR Linear acceleration output data rate
1.875(10)
7.
15
30
60
120
240
480
960
1.92 k
3.84 k
7.68 k Hz
G_ODR Angular rate output data rate
7.
15
30
60
120
240
480
960
1.92 k
3.84 k
7.68 k
HAODR
ODR variation over temperature and supply range in high-accuracy
mode(11)
Gyro on ±
%
Gyro off ±
Vst
Linear acceleration self-test output change(12)(13)(14)^501700 m g
Angular rate self-test output change(15)(16)
FS = ±250 dps 20 80 dps
FS = ±2000 dps 150 700 dps
Top Operating temperature range -40 +85 °C
_1. Typical specifications are not guaranteed.

Sensitivity tolerance for FS up to ±2000 dps.
Measurements are performed in a uniform temperature setup and they are based on characterization data in a limited number of samples._
_Not measured during final test for production.
Value after calibration.
Gyroscope rate noise density in high-performance mode is independent of the ODR and FS setting up to ±2000 dps.
Gyroscope RMS noise in low-power mode is independent of the ODR and FS setting up to ±2000 dps.
Accelerometer noise density in high-performance mode is independent of the selected ODR and FS. Valid when XL_DualC_EN = 0 in_
_register CTRL8 (17h).
Accelerometer noise density in normal mode is independent of the ODR and FS setting. Valid when XL_DualC_EN = 0 in register CTRL_
_(17h).
Noise RMS related to BW = ODR/2.
This ODR is available when the accelerometer is in low-power mode.
Values specified by design.
The sign of the linear acceleration self-test output change is defined by the ST_XL_[1:0] bits in a dedicated register for all axes.
The linear acceleration self-test output change is defined with the device in stationary condition as the absolute value of: OUTPUT[LSb]_
_(self-test enabled) - OUTPUT[LSb] (self-test disabled). 1LSb = 0.061 mg at ±2 g full scale.
Accelerometer self-test limits are full-scale independent._
Mechanical characteristics
15. The sign of the angular rate self-test output change is defined by the ST_G[1:0] bits in a dedicated register for all axes.

The angular rate self-test output change is defined with the device in stationary condition as the absolute value of: OUTPUT[LSb] (self-test_
enabled) - OUTPUT[LSb] (self-test disabled). 1LSb = 70 mdps at ±2000 dps full scale.

4.2 Electrical characteristics
@ Vdd = 1.8 V, T = 25 °C, unless otherwise noted.
Table 4. Electrical characteristics
Symbol Parameter Test conditions Min. Typ.(1) Max. Unit
Vdd Supply voltage 1.71 1.8 3.6 V
Vdd_IO Power supply for I/O 1.08 3.6 V
IddHP
Gyroscope and accelerometer current consumption in high-performance
mode
0.65 mA
LA_IddHP Accelerometer current consumption in high-performance mode 190 μA
LA_IddNM Accelerometer current consumption in normal mode 100 μA
LA_IddLPM2 Accelerometer current consumption in low-power mode (LPM2)
ODR = 60 Hz
ODR = 1.875 Hz
20
4.
μA
LA_IddLPM1 Accelerometer current consumption in low-power mode (LPM1)
ODR = 60 Hz
ODR = 1.875 Hz
17
4.
μA
IddPD Gyroscope and accelerometer current consumption during power-down 2.6 μA
Ton Turn-on time - gyroscope 30 ms
VIH Digital high-level input voltage
0.7 *
Vdd_IO
V
VIL Digital low-level input voltage 0.3 *
Vdd_IO V
VOH High-level output voltage IOH = 4 mA(2) Vdd_IO
V
VOL Low-level output voltage IOL = 4 mA(2) 0.2 V
Top Operating temperature range -40 +85 °C
_1. Typical specifications are not guaranteed.

4 mA is the maximum driving capability, that is, the maximum DC current that can be sourced/sunk by the digital pin in order to guarantee_
the correct digital output voltage levels VOH and VOL.

Table 5. Electrical parameters of Qvar (@Vdd = 1.8 V, T = 25 °C)
Parameter Typ.(1) Unit
Power consumption 15 (2) μA
Offset (shorted inputs) 3 mV
Noise (shorted inputs) 54 μV
Qvar gain 78 LSB/mV
CMRR 54 dB
Input impedance Configurable (from 235 M to 2.4 G) Ω
Input range ±460 mV
_1. Vdd_IO = 1.8 V, Zin = 235 MOhm. Typical values are based on characterization and are not guaranteed.

Extra power consumption when only the analog hub / Qvar function is enabled. In this condition the accelerometer must be set to_
high-performance mode or normal mode.

Electrical characteristics
4.3 Temperature sensor characteristics
@ Vdd = 1.8 V, T = 25 °C unless otherwise noted.
Table 6. Temperature sensor characteristics
Symbol Parameter Test condition Min. Typ. (1) Max. Unit
TODR(2) Temperature refresh rate^60 Hz
Toff Temperature offset(3) -15 +15 °C
TSen Temperature sensitivity 256 LSB/°C
TST Temperature stabilization time(4) 500 μs
T_ADC_res Temperature ADC resolution 16 bit
Top Operating temperature range -40 +85 °C
_1. Typical specifications are not guaranteed

When the accelerometer is in low-power mode and the gyroscope part is turned off, the TODR value is equal to the accelerometer ODR.
The output of the temperature sensor is 0 LSB (typ.) at 25 °C.
Time from power ON to valid data based on characterization data._
Temperature sensor characteristics
4.4 Communication interface characteristics
4.4.1 SPI - serial peripheral interface
Subject to general operating conditions for Vdd and Top. @ Vdd_IO = 1.8 V, T = 25 °C unless otherwise noted.
Table 7. SPI slave timing values
Symbol Parameter
Value(1)
Unit
Min Typ Max
fc(SPC) SPI clock frequency 10 MHz
tc(SPC) SPI clock period 100
ns
thigh(SPC) SPI clock high 45
tlow(SPC) SPI clock low 45
tsu(CS)
CS setup time (mode 3) 5
CS setup time (mode 0) 20
th(CS)
CS hold time (mode 3) 20
CS hold time (mode 0) 20
tsu(SI) SDI input setup time 5
th(SI) SDI input hold time 15
tv(SO) SDO valid output time 15 25
tdis(SO) SDO output disable time 50
Cload Bus capacitance 100 pF
1. Values are evaluated at 10 MHz clock frequency for SPI with both 4 and 3 wires, based on characterization results, not
tested in production

Figure 7. SPI slave timing in mode 0
CS
SPC
SDI
SDO MSB OUT
MSB IN
LSB OUT
LSB IN
t
t
t
tlow(SPC)
v(SO)
tsu(CS) thigh(SPC) tc(SPC)
tsu(SI) th(SI)
dis(SO)
h(CS)
Communication interface characteristics
Figure 8. SPI slave timing in mode 3
CS
SPC
SDI
SDO MSB OUT
MSB IN LSB IN
LSB OUT
tv(SO) tdis(SO)
tsu(SI) th(SI) tlow(SPC)
tsu(CS) thigh(SPC) tc(SPC)
Note: Measurement points are done at 0.3·Vdd_IO and 0.7·Vdd_IO for both input and output ports.

Communication interface characteristics
4.4.2 I²C - inter-IC control interface
Subject to general operating conditions for Vdd and Top.
Table 8. I²C slave timing values
Symbol Parameter
I²C fast mode(1)(2) I²C fast mode plus(1)(2)
Unit
Min Max Min Max
f(SCL) SCL clock frequency 0 400 0 1000 kHz
tw(SCLL) SCL clock low time 1.3 0.
μs
tw(SCLH) SCL clock high time 0.6 0.
tsu(SDA) SDA setup time 100 50 ns
th(SDA) SDA data hold time 0 0.9 0
μs
th(ST) START/REPEATED START condition hold time 0.6 0.
tsu(SR) REPEATED START condition setup time 0.6 0.
tsu(SP) STOP condition setup time 0.6 0.
tw(SP:SR) Bus free time between STOP and START condition 1.3 0.
Data valid time 0.9 0.
Data valid acknowledge time 0.9 0.
CB Capacitive load for each bus line 400 550 pF
_1. Data based on standard I²C protocol requirement, not tested in production.

Data for I²C fast mode and I²C fast mode plus have been validated by characterization, not tested in production._
Figure 9. I²C slave timing diagram
tsu(SP)
tw(SCLL)
tsu(SDA)
tsu(SR)
th(ST) tw(SCLH)
th(SDA)
tw(SP:SR)
START
REPEATED
START
START
STOP
SDA
SCL
Note: Measurement points are done at 0.3·Vdd_IO and 0.7·Vdd_IO for both ports.

Communication interface characteristics
4.5 Absolute maximum ratings
Stresses above those listed as “absolute maximum ratings” may cause permanent damage to the device. This
is a stress rating only and functional operation of the device under these conditions is not implied. Exposure to
maximum rating conditions for extended periods may affect device reliability.
Table 9. Absolute maximum ratings
Symbol Ratings Maximum value Unit
Vdd Supply voltage -0.3 to 4.8 V
TSTG Storage temperature range -40 to +125 °C
Sg Acceleration g for 0.2 ms 20,000 g
ESD Electrostatic discharge protection (HBM) 2 kV
Vin
Input voltage on any control pin
(including CS, SCL/SPC, SDA/SDI/SDO, SDO/SA0)
-0.3 to Vdd_IO +0.3 V
Note: Supply voltage on any pin should never exceed 4.8 V.

This device is sensitive to mechanical shock, improper handling can cause permanent damage to the part.
This device is sensitive to electrostatic discharge (ESD), improper handling can cause permanent damage to the part.
Absolute maximum ratings
4.6 Terminology
4.6.1 Sensitivity
Linear acceleration sensitivity can be determined, for example, by applying 1 g acceleration to the device.
Because the sensor can measure DC accelerations, this can be done easily by pointing the selected axis towards
the ground, noting the output value, rotating the sensor 180 degrees (pointing towards the sky) and noting the
output value again. By doing so, ±1 g acceleration is applied to the sensor. Subtracting the larger output value
from the smaller one, and dividing the result by 2, leads to the actual sensitivity of the sensor. This value changes
very little over temperature and over time. The sensitivity tolerance describes the range of sensitivities of a large
number of sensors (see Table 3).
An angular rate gyroscope is a device that produces a positive-going digital output for counterclockwise rotation
around the axis considered. Sensitivity describes the gain of the sensor and can be determined by applying a
defined angular velocity to it. This value changes very little over temperature and time (see Table 3).
4.6.2 Zero- g and zero-rate level
Linear acceleration zero- g level offset (TyOff) describes the deviation of an actual output signal from the ideal
output signal if no acceleration is present. A sensor in a steady state on a horizontal surface measures 0 g on
both the X-axis and Y-axis, whereas the Z-axis measures 1 g. Ideally, the output is in the middle of the dynamic
range of the sensor (content of OUT registers 00h, data expressed as two's complement number). A deviation
from the ideal value in this case is called zero- g offset.
Offset is to some extent a result of stress to the MEMS sensor and therefore the offset can slightly change after
mounting the sensor onto a printed circuit board or exposing it to extensive mechanical stress. Offset changes
little over temperature, see “Linear acceleration zero- g level change vs. temperature” in Table 3. The zero- g level
tolerance (TyOff) describes the standard deviation of the range of zero- g levels of a group of sensors.
Zero-rate level describes the actual output signal if there is no angular rate present. The zero-rate level of precise
MEMS sensors is, to some extent, a result of stress to the sensor and therefore the zero-rate level can slightly
change after mounting the sensor onto a printed circuit board or after exposing it to extensive mechanical stress.
This value changes very little over temperature and time (see Table 3).
Terminology
5 Digital interfaces
5.1 I²C/SPI interface
The registers embedded inside the LSM6DSV16X may be accessed through both the I²C and SPI serial
interfaces. The latter may be software configured to operate either in 3-wire or 4-wire interface mode. The device
is compatible with SPI modes 0 and 3.
The serial interfaces are mapped to the same pins. To select/exploit the I²C interface, the CS line must be tied
high (that is, connected to Vdd_IO).
Table 10. Serial interface pin description
Pin name Pin description
CS
Enables SPI
I²C/SPI mode selection
(1: SPI idle mode / I²C communication enabled;
0: SPI communication mode / I²C disabled)
SCL/SPC
I²C serial clock (SCL)
SPI serial port clock (SPC)
SDA/SDI/SDO
I²C serial data (SDA)
SPI serial data input (SDI)
3-wire interface serial data output (SDO)
SDO/SA0
SPI serial data output (SDO)
I²C less significant bit of the device address
5.1.1 I²C serial interface
The LSM6DSV16X I²C is a bus slave. The I²C is employed to write the data to the registers, whose content can
also be read back.
The relevant I²C terminology is provided in the table below.
Table 11. I²C terminology
Term Description
Transmitter The device that sends data to the bus
Receiver The device that receives data from the bus
Master The device that initiates a transfer, generates clock signals, and terminates a transfer
Slave The device addressed by the master
There are two signals associated with the I²C bus: the serial clock line (SCL) and the serial data line (SDA). The
latter is a bidirectional line used for sending and receiving the data to/from the interface. Both the lines must be
connected to Vdd_IO through external pull-up resistors. When the bus is free, both the lines are high.
The I²C interface is implemented with fast mode (400 kHz) I²C standards as well as with fast mode plus
(1000 kHz).
In order to disable the I²C block, I2C_I3C_disable = 1 must be written in IF_CFG (03h).
Digital interfaces
5.1.2 I²C operation
The transaction on the bus is started through a start (ST) signal. A start condition is defined as a high to low
transition on the data line while the SCL line is held high. After this has been transmitted by the master, the bus
is considered busy. The next byte of data transmitted after the start condition contains the address of the slave in
the first 7 bits and the eighth bit tells whether the master is receiving data from the slave or transmitting data to
the slave. When an address is sent, each device in the system compares the first seven bits after a start condition
with its address. If they match, the device considers itself addressed by the master.
The slave address (SAD) associated to the LSM6DSV16X is 110101xb. The SDO/SA0 pin can be used to modify
the less significant bit of the device address. If the SDO/SA0 pin is connected to the supply voltage, LSb is 1
(address 1101011b); else if the SDO/SA0 pin is connected to ground, the LSb value is 0 (address 1101010b). This
solution permits to connect and address two different inertial modules to the same I²C bus.
Data transfer with acknowledge is mandatory. The transmitter must release the SDA line during the acknowledge
pulse. The receiver must then pull the data line low so that it remains stable low during the high period of the
acknowledge clock pulse. A receiver that has been addressed is obliged to generate an acknowledge after each
byte of data received.
The I²C embedded inside the LSM6DSV16X behaves like a slave device and the following protocol must be
adhered to. After the start condition (ST) a slave address is sent, once a slave acknowledge (SAK) has been
returned, an 8-bit subaddress (SUB) is transmitted. The increment of the address is configured by the CTRL3
(12h) (IF_INC).
The slave address is completed with a read/write bit. If the bit is 1 (read), a repeated start (SR) condition
must be issued after the two subaddress bytes; if the bit is 0 (write) the master transmits to the slave with
direction unchanged. Table 12 explains how the SAD+read/write bit pattern is composed, listing all the possible
configurations.
Table 12. SAD+read/write patterns
Command SAD[6:1] SAD[0] = SA0 R/W SAD+R/W
Read 110101 0 1 11010101 (D5h)
Write 110101 0 0 11010100 (D4h)
Read 110101 1 1 11010111 (D7h)
Write 110101 1 0 11010110 (D6h)
Table 13. Transfer when master is writing one byte to slave
Master ST SAD + W SUB DATA SP
Slave SAK SAK SAK
Table 14. Transfer when master is writing multiple bytes to slave
Master ST SAD + W SUB DATA DATA SP
Slave SAK SAK SAK SAK
Table 15. Transfer when master is receiving (reading) one byte of data from slave
Master ST SAD + W SUB SR SAD + R NMAK SP
Slave SAK SAK SAK DATA
Table 16. Transfer when master is receiving (reading) multiple bytes of data from slave
Master ST
SAD+
W
SUB SR
SAD+
R
MAK MAK NMAK SP
Slave SAK SAK SAK DATA DATA DATA
I²C/SPI interface
Data are transmitted in byte format (DATA). Each data transfer contains 8 bits. The number of bytes transferred
per transfer is unlimited. Data is transferred with the most significant bit (MSb) first. If a slave receiver does not
acknowledge the slave address (that is, it is not able to receive because it is performing some real-time function)
the data line must be left high by the slave. The master can then abort the transfer. A low to high transition on the
SDA line while the SCL line is high is defined as a stop condition. Each data transfer must be terminated by the
generation of a stop (SP) condition.

In the presented communication format, MAK is master acknowledge and NMAK is no master acknowledge.

I²C/SPI interface
5.1.3 SPI bus interface
The SPI on the LSM6DSV16X is a bus slave which allows writing and reading the registers of the device.
Figure 10. Read and write protocol (in mode 3)
CS
SPC
SDI
SDO
RW
AD5 AD4 AD3 AD2 AD1 AD0
DI7 DI6 DI5 DI4 DI3 DI2 DI1 DI0
DO7 DO6 DO5 DO4 DO3 DO2 DO1 DO0
AD6
CS enables the serial port and it is controlled by the SPI master. It goes low at the start of the transmission and
goes back high at the end. SPC is the serial port clock and it is controlled by the SPI master. It is stopped high
when CS is high (no transmission). SDI and SDO are, respectively, the serial port data input and output. Those
lines are driven at the falling edge of SPC and should be captured at the rising edge of SPC.
Both the read register and write register commands are completed in 16 clock pulses or in multiples of 8 in case
of multiple read/write bytes. Bit duration is the time between two falling edges of SPC. The first bit (bit 0) starts at
the first falling edge of SPC after the falling edge of CS while the last bit (bit 15, bit 23, ...) starts at the last falling
edge of SPC just before the rising edge of CS.
bit 0 : RW bit. When 0, the data DI(7:0) is written into the device. When 1, the data DO(7:0) from the device is
read. In latter case, the chip drives SDO at the start of bit 8.
bit 1-7 : address AD(6:0). This is the address field of the indexed register.
bit 8-15 : data DI(7:0) (write mode). This is the data that is written into the device (MSb first).
bit 8-15 : data DO(7:0) (read mode). This is the data that is read from the device (MSb first).
In multiple read/write commands further blocks of 8 clock periods are added. When the CTRL3 (12h) (IF_INC) bit
is 0, the address used to read/write data remains the same for every block. When the CTRL3 (12h) (IF_INC) bit is
1, the address used to read/write data is increased at every block.
The function and the behavior of SDI and SDO remain unchanged.
I²C/SPI interface
5.1.3.1 SPI read

Figure 11. SPI read protocol (in mode 3)
CS
SPC
SDI
SDO
RW
DO7DO6DO5DO4DO3DO2DO1DO0
AD6AD5 AD4 AD3 AD2 AD1 AD0
The SPI read command is performed with 16 clock pulses. A multiple byte read command is performed by adding
blocks of 8 clock pulses to the previous one.
bit 0 : READ bit. The value is 1.
bit 1-7 : address AD(6:0). This is the address field of the indexed register.
bit 8-15 : data DO(7:0) (read mode). This is the data that is read from the device (MSb first).
bit 16-... : data DO(...-8). Further data in multiple byte reads.
Figure 12. Multiple byte SPI read protocol (2-byte example) (in mode 3)
CS
SPC
SDI
SDO
RW
DO7DO6DO5DO4DO3DO2DO1DO0
AD 5 AD 4 AD 3 AD 2 AD 1 AD0
DO15 DO14 DO13 DO12 DO11DO10 DO9DO8
AD6
I²C/SPI interface
5.1.3.2 SPI write

Figure 13. SPI write protocol (in mode 3)
CS
SPC
SDI
RW DI7 DI6 DI5 DI4 DI3 DI2 DI1 DI0
AD6AD5 AD4 AD3 AD2 AD1 AD0
The SPI write command is performed with 16 clock pulses. A multiple byte write command is performed by adding
blocks of 8 clock pulses to the previous one.
bit 0 : WRITE bit. The value is 0.
bit 1 -7 : address AD(6:0). This is the address field of the indexed register.
bit 8-15 : data DI(7:0) (write mode). This is the data that is written inside the device (MSb first).
bit 16-... : data DI(...-8). Further data in multiple byte writes.
Figure 14. Multiple byte SPI write protocol (2-byte example) (in mode 3)
CS
SPC
SDI
RW
AD 5 AD 4 AD 3 AD 2 AD 1 AD0
DI 7 DI 6 DI 5 DI 4 DI 3 DI 2 DI 1 DI 0 DI15 DI14 DI13 DI12 DI 11 DI10 DI 9 DI8
AD6
5.1.3.3 SPI read in 3-wire mode

3-wire mode is entered by setting the IF_CFG (03h) (SIM) bit equal to 1 (SPI serial interface mode selection).
Figure 15. SPI read protocol in 3-wire mode (in mode 3)
CS
SPC
SDI/O
RW DO7 DO6 DO5 DO4 DO3 DO2 DO1 DO0
AD6AD5 AD4 AD3 AD2 AD1 AD0
The SPI read command is performed with 16 clock pulses:
bit 0 : READ bit. The value is 1.
bit 1-7 : address AD(6:0). This is the address field of the indexed register.
bit 8-15 : data DO(7:0) (read mode). This is the data that is read from the device (MSb first).
A multiple read command is also available in 3-wire mode.
I²C/SPI interface
5.2 MIPI I3C® interface
5.2.1 MIPI I3C® slave interface
The LSM6DSV16X interface includes an MIPI I3C® SDR only slave interface (compliant with release 1.1 of the
specification) with MIPI I3C® SDR embedded features:
CCC command
Direct CCC communication (SET and GET)
Broadcast CCC communication
Private communications
Private read and write for single byte
Multiple read and write
In-band interrupt request
Slave reset pattern
Group address
Full range Vdd_IO support
Asynchronous modes 0 and 1
Synchronous mode
Error detection and recovery methods (S0-S6)
In order to disable the MIPI I3C® block, I2C_I3C_disable = 1 must be written in IF_CFG (03h).
MIPI I3C® interface
5.2.2 MIPI I3C® CCC supported commands
The list of MIPI I3C® CCC commands supported by the device is detailed in the following table.
Table 17. MIPI I3C® CCC commands
Command Command code Default Description
ENTDAA 0x07 DAA procedure
SETDASA 0x87 Assign dynamic address using static address 0x6B/0x6A depending on SDO pin
ENEC 0x80 / 0x00 Slave activity control (direct and broadcast)
DISEC 0x81/ 0x01 Slave activity control (direct and broadcast)
ENTAS0 0x82 / 0x02 Enter activity state (direct and broadcast)
SETXTIME 0x98 / 0x28 Timing information exchange
GETXTIME 0x99
0x07
0x00
0x05
0x92
Timing information exchange
RSTDAA 0x06 Reset the assigned dynamic address (broadcast only)
SETMWL 0x89 / 0x08 Define maximum write length during private write (direct and broadcast)
SETMRL 0x8A / 0x09 Define maximum read length during private read (direct and broadcast)
SETNEWDA 0x88 Change dynamic address
GETMWL 0x8B
0x00
0x08
(2 byte)
Get maximum write length during private write
GETMRL 0x8C
0x00
0x10
0x09
(3 byte)
Get maximum read length during private read
GETPID 0x8D
0x02
0x08
0x00
0x70
0x92
0x0B
SDO = 1
0x02
0x08
0x00
0x70
0x12
0x0B
SDO = 0
GETBCR 0x8E
0x07
(1 byte)
Bus characteristics register
GETDCR 0x8F 0x44 default MIPI I3C® device characteristics register
GETSTATUS 0x90
0x00
0x00
(2 byte)
Status register
MIPI I3C® interface
Command Command code Default Description
GETMXDS 0x94
0x08
0x60
Return max write and read speed
GETCAPS 0x95
0x00
0x11
0x18
0x00
Provide information about device capabilities and supported extended features
SETGRPA 0x9B Group address assignment command
RSTGRPA 0x2C / 0x9C Reset the group address
RSTACT 0x9A / 0x2A Configure slave reset action
5.2.3 Overview of anti-spike filter management
The device acts as a standard I²C target as long as it has an I²C static address. The device is capable of
detecting and disabling the I²C anti-spike filter after detecting the broadcast address (7'h7E/W). In order to
guarantee proper behavior of the device, the I3C master must emit the first START, 7'h7E/W at open-drain speed
using I²C fast mode plus reference timing.
After detecting the broadcast address, the device can receive the I3C dynamic address following the I3C push-
pull timing. If the device is not assigned a dynamic address, then the device continues to operate as an I²C device
with no anti-spike filter. For the case in which the host decides to keep the device as I²C with anti-spike filter, there
is a configuration required to keep the anti-spike filter active. This configuration is done by writing the ASF_CTRL
bit to 1 in the IF_CFG (03h) register. This configuration forces the anti-spike filter to always be turned on instead
of being managed by the communication on the bus.
MIPI I3C® interface
5.3 Master I²C interface
If the LSM6DSV16X is configured in mode 2, a master I²C line is available. The master serial interface is mapped
to the following dedicated pins.
Table 18. Master I²C pin details
Pin name Pin description
MSCL I²C serial clock master
MSDA I²C serial data master
MDRDY I²C master external synchronization signal
5.4 Auxiliary SPI interface
If the LSM6DSV16X is configured in mode 3, the auxiliary SPI is available. The auxiliary SPI interface is mapped
to the following dedicated pins.
Table 19. Auxiliary SPI pin details
Pin name Pin description
OCS_Aux Enables auxiliary SPI 3/4-wire
SDx/AH1/Qvar1 Auxiliary SPI 3/4-wire data input (SDI_Aux) and SPI 3-wire data output (SDO_Aux)
SCx/AH2/Qvar2 Auxiliary SPI 3/4-wire interface serial port clock
SDO_Aux Auxiliary SPI 4-wire data output (SDO_Aux)
When the LSM6DSV16X is configured in mode 3, the auxiliary SPI can be connected to a camera module for OIS
support.
Master I²C interface
6 Functionality
This section describes all the operating modes and power modes of the LSM6DSV16X.
Note: Refer to the product application note for the details regarding operating/power mode configurations, settings,
turn-on/off time and on-the-fly changes.

6.1 Operating modes
In the LSM6DSV16X, the accelerometer and the gyroscope can be turned on/off independently of each other and
are allowed to have different ODRs and power modes.
The LSM6DSV16X has three operating modes available:
Only accelerometer active and gyroscope in power-down
Only gyroscope active and accelerometer in power-down
Both accelerometer and gyroscope sensors active with independent ODR and power mode
The accelerometer is activated from power-down by writing ODR_XL_[3:0] in CTRL1 (10h) while the gyroscope
is activated from power-down by writing ODR_G_[3:0] in CTRL2 (11h). For combo mode, the ODRs are totally
independent.
6.2 Accelerometer power modes
In the LSM6DSV16X, the accelerometer can be configured in five different operating modes: power-down mode,
low-power mode (1, 2, 3), normal mode, high-performance mode and high-accuracy ODR mode.
The operating mode selected depends on the value of the OP_MODE_XL_[2:0] bits in CTRL1 (10h).
If the value of the OP_MODE_XL_[2:0] bits is 000 (default), high-performance mode is valid for all ODRs (from
7.5 Hz up to 7.68 kHz).
Normal mode is available for ODR values from 7.5 Hz to 1.92 kHz and it is enabled by setting the
OP_MODE_XL_[2:0] bits to 111. Normal mode cannot be used in mode 3 connection mode.
In high-performance mode and in normal mode the analog anti-aliasing filter is active.
Low-power mode is available for lower ODRs (1.875 Hz, 15 Hz, 30 Hz, 60 Hz, 120 Hz, 240 Hz). The three
low-power modes are enabled by setting OP_MODE_XL_[2:0] to 100 (LPM1), 101 (LPM2), 110 (LPM3).
High-accuracy ODR mode is available for ODR values from 15 Hz up to 7.68 kHz and it is enabled by setting the
OP_MODE_XL_[2:0] bits to 001. Refer to Section 6.5 High-accuracy ODR mode for more details.
The embedded functions based on accelerometer data (free-fall, 6D/4D, tap/double-tap, wake-up, activity/
inactivity, stationary/motion, step counter, step detection, significant motion, tilt) and the FIFO batching
functionality are supported in all modes.
Functionality
6.3 Accelerometer dual-channel mode
The LSM6DSV16X accelerometer block has a dual-channel architecture able to work with two different full scales
simultaneously. By default, the device operates in single-channel mode supporting FS scale values from ±2 g
through ±16 g and different power modes, as described in Section 6.2 Accelerometer power modes. The block
diagrams in the following figures show the configuration of acceleration data processing in the two different
modes.
Figure 16. Single-channel mode (XL_DualC_EN = 0)
ADC
Digital
LP Filter
OP_MODE_XL_[2:0]
ODR_XL_[3:0]
LPF1
SPI / I^2 C /
MIPI I^3 C
FIFO
Composite
Filter
Channel 1
±2/±4/±8/± 16 g
®
Figure 17. Dual-channel mode (XL_DualC_EN = 1)
ADC
Digital
LP Filter
OP_MODE_XL_[2:0]
ODR_XL_[3:0]
LPF1
SPI / I^2 C /
MIPI I^3 C
FIFO
Composite
Filter
Channel 1
±2/±4/±8/± 16 g
DualC
XL_DualC_EN
Channel 2
± 16 g
®
The dual-channel functionality can be enabled/disabled by configuring the bit XL_DualC_EN to 1 (enable) or to 0
(disable) in CTRL8 (17h).
Referring to Figure 17. Dual-channel mode (XL_DualC_EN = 1), when the dual-channel mode has been
activated:
Channel 1 supports user-selectable full-scale acceleration range of ±2/±4/±8/±16 g based on the value of the
FS_XL_[1:0] bits in the CTRL8 (17h) register.
Channel 2 full scale is set to ±16 g. Acceleration data are available in the output
registers from UI_OUTX_L_A_OIS_DualC (34h) and UI_OUTX_H_A_OIS_DualC (35h) through
UI_OUTZ_L_A_OIS_DualC (38h) and UI_OUTZ_H_A_OIS_DualC (39h)).
Accelerometer dual-channel mode
6.4 Gyroscope power modes
In the LSM6DSV16X, the gyroscope can be configured in five different operating modes: power-down mode,
sleep mode, low-power mode, high-performance mode and high-accuracy ODR mode.
The operating mode selected depends on the value of the OP_MODE_G_[2:0] bits in CTRL2 (11h).
If the value of the OP_MODE_G_[2:0] bits is 000 (default), high-performance mode is valid for all ODRs (from 7.5
Hz up to 7.68 kHz).
Low-power mode is available for lower ODRs (7.5 Hz, 15 Hz, 30 Hz, 60 Hz, 120 Hz, 240 Hz) and it is enabled by
setting the the OP_MODE_G_[2:0] bits to 101.
High-accuracy ODR mode is available for ODR values from 15 Hz up to 7.68 kHz and it is enabled by setting the
OP_MODE_G_[2:0] bits to 001. Refer to Section 6.5 High-accuracy ODR mode for more details.
6.5 High-accuracy ODR mode
High-accuracy ODR (HAODR) mode can be enabled to reduce the part-to-part output data rate variation. It
supports accelerometer only, gyroscope only, and combo (accelerometer and gyroscope) modes. When this mode
is used for one sensor (accelerometer or gyroscope), the other sensor also has to be configured in high-accuracy
ODR (HAODR) mode.
The main high-accuracy ODR features are:
Noise level is aligned with high-performance mode
Power consumption increase of 20 μA (typical) vs. the corresponding high-performance mode configuration
selected
The UI channel bandwidth can be selected through the gyroscope LPF1 and accelerometer HPF/LPF2
filters.
When HAODR mode is enabled, it is applied to the UI accelerometer, UI gyroscope, EIS gyroscope, and
temperature. It is not applied to OIS accelerometer/gyroscope channels.
Note: HAODR mode has to be enabled / disabled when the device is in power-down mode.

When HAODR mode is enabled, two different sets of ODRs are supported based on the configuration of the
HAODR_SEL_[1:0] bitfield in the HAODR_CFG (62h) register, as shown in the table below.
Note: High-accuracy ODR mode is not compatible with the analog hub / Qvar functionality and the activity/inactivity
functionality (motion/stationary can be used).

Table 20. Accelerometer and gyroscope ODR selection in high-accuracy ODR mode
ODR_XL_[3:0]
ODR_G_[3:0]
ODR [Hz]
HAODR_SEL_[1:0] = 00
ODR [Hz]
HAODR_SEL_[1:0] = 01
ODR [Hz]
HAODR_SEL_[1:0] = 10
0000 Power-down Power-down Power-down
0001 Reserved Reserved Reserved
0010 Reserved Reserved Reserved
0011 15 15.625 12.5
0100 30 31.25 25
0101 60 62.5 50
0110 120 125 100
0111 240 250 200
1000 480 500 400
1001 960 1000 800
1010 1920 2000 1600
1011 3840 4000 3200
1100 7680 8000 6400
Others Reserved Reserved Reserved
Gyroscope power modes
6.6 ODR-triggered mode
When ODR-triggered mode is enabled, a reference signal must be provided to the INT2 pin, and the device then
automatically aligns (in frequency and phase) the data generation to the edges of the reference signal.
It supports accelerometer only, gyroscope only, and combo (accelerometer and gyroscope) modes. When both
the accelerometer and gyroscope are enabled, the user must configure the same ODR on both the accelerometer
and gyroscope. It is not possible to select different ODRs for the accelerometer and gyroscope; if different output
data rate values are set, the ODR configured for the gyroscope data is also applied to the accelerometer data.
The full-scale configurations are totally independent between the accelerometer and gyroscope and they can be
set in any combination.
Note: ODR-triggered mode has to be enabled / disabled when the device is in power-down mode.

Note: When ODR-triggered mode is enabled, the 1100 configuration of the ODR_XL[3:0] bits in register CTRL1 (10h)
and the 1100 configuration of the ODR_G_[3:0] bits in register CTRL2 (11h) cannot be used._

Note: ODR-triggered mode is not compatible with the analog hub / Qvar functionality nor the EIS functionality.

6.7 Analog hub functionality
The LSM6DSV16X embeds an analog hub sensing functionality which is able to connect an analog input and
convert it to a digital signal for embedded processing.
In the LSM6DSV16X, the analog hub has a dedicated channel that can be activated by setting the AH_QVAR_EN
bit to 1 in the CTRL7 (16h) register.
The accelerometer sensor must be set in high-performance mode or in normal mode when the analog hub
channel is enabled.
The analog hub data-ready signal is represented by the AH_QVARDA bit of the STATUS_REG (1Eh) register.
This signal can be driven to the INT2 pin by setting the INT2_DRDY_AH_QVAR bit to 1 in the CTRL7 (16h)
register.
Analog hub data are available as a 16-bit word in two’s complement in the AH_QVAR_OUT_L (3Ah) and
AH_QVAR_OUT_H (3Bh) registers at a fixed rate of 240 Hz (typical).
Analog signal data can be also processed by MLC/FSM logic.
The analog hub functionality is available in mode 1 connection mode for the I²C interface only. The external
analog lines have to be connected to pin 2 (SDx/AH1/Qvar1) and/or pin 3 (SCx/AH2/Qvar2), so the I²C-master
interface (mode 2) and the auxiliary SPI (mode 3) are not available when the analog hub is used.
The equivalent input impedance of the analog hub buffers can be selected by properly setting the
AH_QVAR_C_ZIN_[1:0] bits in the CTRL7 (16h) register.
6.8 Qvar functionality
The LSM6DSV16X embeds a Qvar sensor which is able to detect electric charge variations in the proximity of the
external electrodes connected to the device.
In the LSM6DSV16X, Qvar has a dedicated channel that can be activated by setting the AH_QVAR_EN bit to 1 in
the CTRL7 (16h) register.
The accelerometer sensor must be set in high-performance mode or in normal mode when the Qvar channel is
enabled.
The Qvar data-ready signal is represented by the AH_QVARDA bit of the STATUS_REG (1Eh) register. This
signal can be driven to the INT2 pin by setting the INT2_DRDY_AH_QVAR bit to 1 in the CTRL7 (16h) register.
Qvar data are available as a 16-bit word in two’s complement in the AH_QVAR_OUT_L (3Ah) and
AH_QVAR_OUT_H (3Bh) registers at a fixed rate of 240 Hz (typical).
Qvar data can also be processed by MLC/FSM logic.
The Qvar functionality is available in mode 1 connection mode for the I²C interface only. The external electrodes
have to be connected to pin 2 (SDx/AH1/Qvar1) and/or pin 3 (SCx/AH2/Qvar2), so the I²C-master interface (mode
2) and the auxiliary SPI (mode 3) are not available when Qvar is used.
The equivalent input impedance of the Qvar buffers can be selected by properly setting the
AH_QVAR_C_ZIN_[1:0] bits in the CTRL7 (16h) register.
ODR-triggered mode
6.9 Block diagram of filters
Figure 18. Block diagram of filters
ADC 1
ADC 2
Low-Pass
UI/EIS Gyro
Low-Pass
OIS Gyro
Low-Pass
OIS XL
Regs
array,
FIFO
interface
Interrupt
mng
Auxiliary
SPI
Voltage and current
references
Trimming circuit
and Test interface
Clock and phase
generator
Power
management FTP
CS
SCL/SPC
SDA/SDI/SDO
SDO/SA0
CS
SPC_Aux
SDI_Aux
SDO_Aux
INT 1
INT 2
M
E
M
S
S E N S O R
Low-Pass
UI XL
Gyro
UI/EIS/OIS
front-end
XL UI/OIS
front-end
Temperature
sensor
Regs
array
Interrupt
mng
I^2 C/
/SPI^
MIPI I3C®
Block diagram of filters
6.9.1 Block diagrams of the accelerometer filters
In the LSM6DSV16X, the filtering chain for the accelerometer part is composed of the following:
Digital filter (LPF1)
Composite filter
Details of the block diagram appear in the following figure.
Figure 19. Accelerometer UI chain
Digital
LP Filter
OP_MODE_XL_[2:0]
ODR_XL_[3:0]
LPF1
Composite
Filter
ADC
Figure 20. Accelerometer composite filter
SLOPE
FILTER
000
001
010
...
111
SPI /
I^2 C /
MIPI I3C
1
0
HP_SLOPE_XL_EN
LPF2_XL_EN
0
1
Digital
HP Filter
HP_LPF2_XL_BW_[2:0]
Digital
LP Filter
LPF 2
S/D Tap
6 D / 4 D
0
1
LOW_PASS_ON_6D
1
0
SLOPE_FDS
Wake-up
Activity /
Inactivity
Free-fall
Embedded
functions
FIFO
USER
OFFSET
0
1
USR_OFF_ON_OUT
USR_OFF_W
OFS_USR_[7: 0 ]
1
0
USR_OFF_ON_WU
LPF 1
Output (^1 )
®
HP_LPF2_XL_BW_[2:0]
HP_LPF2_XL_BW_[2:0]
The cutoff value of the LPF1 output is ODR/2 when the accelerometer is in high-performance mode,
high-accuracy ODR mode, or normal mode. This value is equal to 2300 Hz when the accelerometer is in
low-power mode 1 (2 mean), 912 Hz in low-power mode 2 (4 mean) or 431 Hz in low-power mode 3 (8
mean).
Note: Embedded functions include finite state machine, machine learning core, pedometer, step detector and step
counter, significant motion detection, and tilt functions.

Block diagram of filters
The accelerometer filtering chain when mode 3 is enabled is illustrated in the following figure.
Figure 21. Accelerometer chain with mode 3 enabled
Digital
LP Filter
LPF_OIS
LPF_XL_OIS_BW_[2:0]
ADC Aux_SPI
ODR XL
@7.68 kHz
UI chain
SPI /
I^2 C /
MIPI I 3 C
ODR XL
@7.68 kHz
®
Note: The accelerometer OIS chain is enabled by setting the OIS_XL_EN bit to 1 in the UI_CTRL1_OIS (70h) /
SPI2_CTRL1_OIS (70h) register.
The configuration of the accelerometer UI chain is not affected by enabling/disabling the accelerometer OIS
chain, with one exception: accelerometer normal operating mode (OP_MODE_XL[2:0] = 111 in the CTRL1
(10h) register) cannot be used when the accelerometer OIS chain is enabled._
Accelerometer output values are available in the following registers with ODR at 7.68 kHz:

UI_OUTX_L_A_OIS_DualC (34h) and UI_OUTX_H_A_OIS_DualC (35h) through
UI_OUTZ_L_A_OIS_DualC (38h) and UI_OUTZ_H_A_OIS_DualC (39h)
SPI2_OUTX_L_A_OIS (28h) and SPI2_OUTX_H_A_OIS (29h) through SPI2_OUTZ_L_A_OIS (2Ch) and
SPI2_OUTZ_H_A_OIS (2Dh)
Note: When the accelerometer OIS is used, refer to the product application note for the power mode configuration and
settings.

Block diagram of filters
6.9.2 Block diagrams of the gyroscope filters
In the LSM6DSV16X, the gyroscope filtering chain depends on the mode configuration:
Mode 1 (for user interface (UI) and electronic image stabilization (EIS) functionality through the primary
interface) and mode 2
Figure 22. Gyroscope digital chain - mode 1 (UI/EIS) and mode 2
ADC
LPF1_G_EN
Digital
LP filter
LPF1_G_BW_[2:0]
LPF1
0
1
SPI / I^2 C /
MIPI I3C
Digital FIFO
LP filter
ODR_G_[ 3 : 0 ]
LPF2
( 1 )( 2 )
FSM / MLC
®
When the gyroscope OIS or EIS chain is enabled, the LPF1 filter is not available in the gyroscope UI chain.
It is recommended to avoid using the LPF1 filter in the gyroscope UI chain when the gyroscope OIS or EIS is
used.
The LPF1 filter is available in high-performance mode only. If the gyroscope is configured in low-power
mode, the LPF1 filter is bypassed.
In this configuration, the gyroscope ODR is selectable from 7.5 Hz up to 7.68 kHz. A low-pass filter (LPF1)
is available, for more details about the filter characteristics see Table 64. Gyroscope LPF1 + LPF2 bandwidth
selection.
The digital LPF2 filter's cutoff frequency depends on the selected gyroscope ODR, as indicated in the following
table.
Table 21. Gyroscope LPF2 bandwidth selection
Gyroscope ODR [Hz] LPF2 cutoff [Hz]
7.5 3.4
15 6.6
30 13.0
60 24.6
120 49.4
240 96
480 187
960 342
1.92 kHz 491
3.84 kHz 528
7.68 kHz 537
Note: Data can be acquired from the output registers and FIFO over the primary I²C/MIPI I3C®/SPI interface.

Block diagram of filters
Mode 3 (for OIS functionality)
Figure 23. Gyroscope digital chain - mode 3 (OIS)
ADC
Digital
LP filter
LPF1_G_OIS_BW_[1:0]
LPF1
SPI / I^2 C /
MIPI I3C
Digital FIFO
LP filter
ODR_G_[ 3 : 0 ]
LPF2
Aux_SPI
ODR gyro
@7.68 kHz
( 1 )( 2 )
®
(3)
When the gyroscope OIS or EIS chain is enabled, the LPF1 filter is not available in the gyroscope UI chain.
It is recommended to avoid using the LPF1 filter in mode1/2 when the gyroscope OIS or EIS chain is used.
When the gyroscope OIS is used, refer to the product application note for the power mode configuration and
settings.
The auxiliary interface needs to be enabled in UI_CTRL1_OIS (70h) / SPI2_CTRL1_OIS (70h).

In mode 3 configuration, there are two paths:

The chain for user interface (UI) where the ODR is selectable from 7.5 Hz up to 7.68 kHz
The chain for OIS where the ODR is at 7.68 kHz and the LPF1 is available. The LPF1 configuration
depends on the setting of the LPF1_G_OIS_BW_[1:0] bits in register UI_CTRL2_OIS (71h) /
SPI2_CTRL2_OIS (71h); for more details about the filter characteristics see UI_CTRL2_OIS (71h).
Gyroscope output values are in registers 22h to 27h if read from the Auxi_SPI or in registers 2Eh to
33h if read from the primary interface with the selected full scale FS_G_OIS_[1:0] bits in UI_CTRL2_OIS
(71h) / SPI2_CTRL2_OIS (71h)).
Block diagram of filters
6.10 Enhanced EIS
The LSM6DSV16X offers advanced design flexibility for EIS applications: enhanced EIS functionality has a
dedicated channel and processing with independent filtering.
Enhanced EIS main features:
Enhanced EIS channel gyroscope data can be read over the primary interfaces through I²C / MIPI I3C® /
SPI.
EIS data are available in free-run mode in the output registers (UI_OUTX_L_G_OIS_EIS (2Eh) and
UI_OUTX_H_G_OIS_EIS (2Fh) through UI_OUTZ_L_G_OIS_EIS (32h) and UI_OUTZ_H_G_OIS_EIS
(33h)) by setting the G_EIS_ON_G_OIS_OUT_REG bit to 1 in the CTRL_EIS (6Bh) register or in FIFO (by
setting the G_EIS_FIFO_EN bit to 1 in the FIFO_CTRL4 (0Ah) register) with dedicated TAG and timestamp
configurable using FIFO_CTRL4 (0Ah).
Enhanced EIS option is compatible with mode 3 selection. When EIS data-out are read from the output
registers (setting G_EIS_ON_G_OIS_OUT_REG bit), data from the gyroscope OIS chain can be only read
from the auxiliary SPI interface.
Figure 24. LSM6DSV16X supports UI, enhanced EIS, and OIS processing simultaneously
UI UI / EIS
EIS Block^
Camera
module
AP
Auxiliary
SPI
Primary
output
I^2 C/MIPI I 3 C^ /SPI
®
Figure 25. Gyroscope enhanced EIS and UI block diagram
ADC
LPF EIS
LPF UI
FS UI
FIFO
SPI / I^2 C/
MIPI I3C
UI Channel
EIS Channel
FS EIS
®
When enhanced EIS mode is activated through the ODR_EIS_[1:0] bits in the CTRL_EIS (6Bh) register:
Gyroscope UI can be configured only in power-down mode, high-performance mode, or high-accuracy
ODR mode.
Gyroscope EIS full scale can be selected by using the FS_G_EIS_[2:0] bits in the CTRL_EIS (6Bh)
register.
Gyroscope EIS data rate selectable at 1.92 kHz or 960 Hz configurable through the ODR_G_EIS_[1:0] bits
in the CTRL_EIS (6Bh) register.
LPF_EIS low-pass filter (refer to Figure 25) bandwidth selection can be configured through the
LPF_G_EIS_BW bit in the CTRL_EIS (6Bh) register.
Enhanced EIS
6.11 OIS
This section describes OIS functionality. There is a dedicated gyroscope and accelerometer DSP for OIS.
The device also supports self-test functionality on the OIS side.
6.11.1 Enabling OIS functionality and connection schemes
There are two different ways in order to enable and configure OIS functionality:
Auxiliary SPI full control : Enabling and configuration done from the auxiliary SPI
Primary interface full control : Enabling and configuration done from the primary interface
The configurations that allow selecting these two different options are done using the OIS_CTRL_FROM_UI bit in
the FUNC_CFG_ACCESS (01h) register as described in the following table.
Table 22. OIS configurations
OIS_CTRL_FROM_UI OIS configuration option
0 Auxiliary SPI full control
1 Primary interface full control
OIS
6.11.1.1 Auxiliary SPI full control

This is the default condition of the device. The camera module is completely independent from the application
processor as shown in Figure 26.
The auxiliary SPI can configure OIS functionality through SPI2_INT_OIS (6Fh), SPI2_CTRL1_OIS (70h),
SPI2_CTRL2_OIS (71h), SPI2_CTRL3_OIS (72h).
Reading from the auxiliary SPI is enabled only when the SPI2_READ_EN bit in the SPI2_CTRL1_OIS (70h)
register is set to 1.
The primary interface can access the OIS control registers (UI_INT_OIS (6Fh), UI_CTRL1_OIS (70h),
UI_CTRL2_OIS (71h), UI_CTRL3_OIS (72h)) in read mode.
Figure 26. Auxiliary SPI full control
6x
UI/OIS
AP
I 3 C/SPI/I^2 C
Camera Module
OIS Driver
Image
Sensor
Actuator
SPI_Aux
OIS
6.11.1.2 Primary interface full control

This option allows the application processor to configure all OIS functionalities from the primary interface. This
option allows using embedded OIS data for both the main and front camera, connecting them to the application
processor (eventually adding a context hub) as shown in Figure 27: the AP can also do some processing on the
data before sending them to the cameras.
In order to place the device in this mode, the OIS_CTRL_FROM_UI bit in the FUNC_CFG_ACCESS (01h)
register must be set to 1 from the primary interface.
Figure 27. OIS Primary interface full control
Context
Hub
Front camera
6x
UI/OIS
AP
I 3 C/SPI/I^2 C
2 ndcamera Main camera
OIS Driver
Image
Sensor
Actuator
Context
Hub
Front camera
6x
UI/OIS
AP
I3C/SPI/I^2 C
2 ndcamera Main camera
OIS Driver
Image
Sensor
Actuator
SPI_Aux
(a) (b)
Then, the AP can configure OIS functionalities through UI_INT_OIS (6Fh), UI_CTRL1_OIS (70h), UI_CTRL2_OIS
(71h), UI_CTRL3_OIS (72h).
Reading from the auxiliary SPI can be enabled by setting the SPI2_ READ_EN bit in the UI_CTRL1_OIS (70h)
register to 1 in order to directly read OIS data (as shown in Figure 27 (b)). The auxiliary SPI can access the
SPI2_INT_OIS (6Fh), SPI2_CTRL1_OIS (70h), SPI2_CTRL2_OIS (71h), and SPI2_CTRL3_OIS (72h) registers
in read-only mode.
Note: The OIS_CTRL_FROM_UI bit is reset by the software reset procedure.

OIS
6.12 FIFO
The presence of a FIFO allows consistent power saving for the system since the host processor does not need
continuously poll data from the sensor, but It can wake up only when needed and burst the significant data out
from the FIFO.
The LSM6DSV16X embeds 1.5 KB of data in FIFO (up to 4.5 KB with the compression feature enabled) to store
the following data:
Gyroscope
Accelerometer
External sensors (up to 4)
Step counter
Timestamp
Temperature
MLC features and filters
SFLP output data (quaternion, gyroscope bias, gravity vector)
Writing data in the FIFO can be configured to be triggered by the:
Accelerometer / gyroscope data-ready signal
Sensor hub data-ready signal
Step detection signal
The applications have maximum flexibility in choosing the rate of batching for physical sensors with FIFO-
dedicated configurations: accelerometer, gyroscope and temperature sensor batch rates can be selected by the
user. External sensor writing in FIFO can be triggered by the accelerometer data-ready signal or by an external
sensor interrupt. The step counter can be stored in FIFO with associated timestamp each time a step is detected.
It is possible to select decimation for timestamp batching in FIFO with a factor of 1, 8, or 32.
The reconstruction of a FIFO stream is a simple task thanks to the FIFO_DATA_OUT_TAG byte that allows
recognizing the meaning of a word in FIFO.
FIFO allows correct reconstruction of the timestamp information for each sensor stored in FIFO. If a change in the
ODR or BDR (batch data rate) configuration is performed, the application can correctly reconstruct the timestamp
and know exactly when the change was applied without disabling FIFO batching. FIFO stores information of the
new configuration and timestamp in which the change was applied in the device.
Finally, FIFO embeds a compression algorithm that the user can enable in order to have up to 4.5 KB data
stored in FIFO and take advantage of interface communication length for FIFO flushing and communication power
consumption.
The programmable FIFO watermark threshold can be set using the WTM[7:0] bits in the FIFO_CTRL1 (07h)
register. To monitor the FIFO status, dedicated registers (FIFO_STATUS1 (1Bh), FIFO_STATUS2 (1Ch)) can be
read to detect FIFO overrun events, FIFO full status, FIFO empty status, FIFO watermark status and the number
of unread samples stored in the FIFO. To generate dedicated interrupts on the INT1 and INT2 pins of these status
events, the configuration can be set in INT1_CTRL (0Dh) and INT2_CTRL (0Eh).
The FIFO buffer can be configured according to seven different modes:
Bypass mode
FIFO mode
Continuous mode
Continuous-to-FIFO mode
ContinuousWTM-to-full mode
Bypass-to-continuous mode
Bypass-to-FIFO mode
Each mode is selected by the FIFO_MODE_[2:0] bits in the FIFO_CTRL4 (0Ah) register.
6.12.1 Bypass mode
In bypass mode (FIFO_CTRL4 (0Ah)(FIFO_MODE_[2:0] = 000), the FIFO is not operational and it remains empty.
Bypass mode is also used to reset the FIFO when in FIFO mode.
FIFO
6.12.2 FIFO mode
In FIFO mode (FIFO_CTRL4 (0Ah)(FIFO_MODE_[2:0] = 001) data from the output channels are stored in the
FIFO until it is full.
To reset FIFO content, bypass mode should be selected by writing FIFO_CTRL4 (0Ah)(FIFO_MODE_[2:0])
to 000. After this reset command, it is possible to restart FIFO mode by writing FIFO_CTRL4 (0Ah)
(FIFO_MODE_[2:0]) to 001.
The FIFO buffer memorizes up to 4.5 KB of data (with compression enabled) but the depth of the FIFO can be
resized by setting the WTM[7:0] bits in FIFO_CTRL1 (07h). If the STOP_ON_WTM bit in FIFO_CTRL2 (08h) is
set to 1, FIFO depth is limited up to the WTM[7:0] bits in the FIFO_CTRL1 (07h) register.
6.12.3 Continuous mode
Continuous mode (FIFO_CTRL4 (0Ah)(FIFO_MODE_[2:0] = 110) provides a continuous FIFO update: as new
data arrives, the older data is discarded.
A FIFO threshold flag FIFO_STATUS2 (1Ch)(FIFO_WTM_IA) is asserted when the number of unread samples in
FIFO is greater than or equal to FIFO_CTRL1 (07h) (WTM[7:0]).
It is possible to route the FIFO_WTM_IA flag to the INT1 pin by writing in register INT1_CTRL (0Dh)
(INT1_FIFO_TH) = 1 or to the INT2 pin by writing in register INT2_CTRL (0Eh)(INT2_FIFO_TH) = 1.
A full-flag interrupt can be enabled, INT1_CTRL (0Dh)(INT1_FIFO_FULL) = 1 or INT2_CTRL (0Eh)
(INT2_FIFO_FULL) = 1, in order to indicate FIFO saturation and eventually read its content all at once.
If an overrun occurs, at least one of the oldest samples in FIFO has been overwritten and the FIFO_OVR_IA flag
in FIFO_STATUS2 (1Ch) is asserted.
In order to empty the FIFO before it is full, it is also possible to pull from FIFO the number of unread samples
available in FIFO_STATUS1 (1Bh) and FIFO_STATUS2 (1Ch)(DIFF_FIFO_[8:0]).
6.12.4 Continuous-to-FIFO mode
In continuous-to-FIFO mode (FIFO_CTRL4 (0Ah)(FIFO_MODE_[2:0] = 011), FIFO behavior changes according to
the trigger event detected in one of the following interrupt events:
Single tap
Double tap
Wake-up
Free-fall
D6D
When the selected trigger bit is equal to 1, FIFO operates in FIFO mode.
When the selected trigger bit is equal to 0, FIFO operates in continuous mode.
6.12.5 ContinuousWTM-to-full mode
In continuousWTM-to-full mode (FIFO_CTRL4 (0Ah)(FIFO_MODE_[2:0] = 010), FIFO behavior changes
according to the trigger event detected in one of the following interrupt events:
Single tap
Double tap
Wake-up
Free-fall
D6D
When the selected trigger bit is equal to 0, FIFO operates in continuous mode with the FIFO size limited to the
FIFO watermark level (defined by the WTM[7:0] bits in the FIFO_CTRL1 (07h) register).
When the selected trigger bit is equal to 1, FIFO continues to store data until it is full.
FIFO
6.12.6 Bypass-to-continuous mode
In bypass-to-continuous mode (FIFO_CTRL4 (0Ah)(FIFO_MODE_[2:0] = 100), data measurement storage inside
FIFO operates in Continuous mode when selected triggers are equal to 1, otherwise FIFO content is reset
(bypass mode).
FIFO behavior changes according to the trigger event detected in one of the following interrupt events:
Single tap
Double tap
Wake-up
Free-fall
D6D
6.12.7 Bypass-to-FIFO mode
In bypass-to-FIFO mode (FIFO_CTRL4 (0Ah)(FIFO_MODE_[2:0] = 111), data measurement storage inside FIFO
operates in FIFO mode when selected triggers are equal to 1, otherwise FIFO content is reset (bypass mode).
FIFO behavior changes according to the trigger event detected in one of the following interrupt events:
Single tap
Double tap
Wake-up
Free-fall
D6D
6.12.8 FIFO reading procedure
The data stored in FIFO are accessible from dedicated registers and each FIFO word is composed of 7
bytes: one tag byte (FIFO_DATA_OUT_TAG (78h), in order to identify the sensor, and 6 bytes of fixed data
(FIFO_DATA_OUT registers from (79h) to (7Eh)).
The DIFF_FIFO_[8:0] field in the FIFO_STATUS1 (1Bh) and FIFO_STATUS2 (1Ch) registers contains the number
of words (1 byte TAG + 6 bytes DATA) collected in FIFO.
In addition, it is possible to configure a counter of the batch events of accelerometer or gyroscope sensors.
The flag COUNTER_BDR_IA in FIFO_STATUS2 (1Ch) alerts that the counter reaches a selectable threshold
(CNT_BDR_TH_[9:0] field in COUNTER_BDR_REG1 (0Bh) and COUNTER_BDR_REG2 (0Ch)). This allows
triggering the reading of FIFO with the desired latency of one single sensor. The sensor is selectable using
the TRIG_COUNTER_BDR_[1:0] bits in COUNTER_BDR_REG1 (0Bh). As for the other FIFO status events,
the flag COUNTER_BDR_IA can be routed on the INT1 or INT2 pins by asserting the corresponding bits
(INT1_CNT_BDR of INT1_CTRL (0Dh) and INT2_CNT_BDR of INT2_CTRL (0Eh)).
In order to maximize the amount of accelerometer and gyroscope data in FIFO, the user can enable
the compression algorithm by setting to 1 both the FIFO_COMPR_EN bit in EMB_FUNC_EN_B (05h)
(embedded functions registers bank) and the FIFO_COMPR_RT_EN bit in FIFO_CTRL2 (08h). When
compression is enabled, it is also possible to force writing noncompressed data at a selectable rate using the
UNCOMPR_RATE_[1:0] field in FIFO_CTRL2 (08h).
Meta information about accelerometer and gyroscope sensor configuration changes can be managed by enabling
the ODR_CHG_EN bit in FIFO_CTRL2 (08h).
FIFO
7 Application hints
7.1 LSM6DSV16X electrical connections in mode 1
Figure 28. LSM6DSV16X electrical connections in mode 1
GND
or
Vdd_IO
Vdd_IO
GND
100 nF
C2
SDO/SA0
SDx/AH1/Qvar1
SCx/AH2/Qvar2
INT1
GND
Vdd_IO
SDASCLCS
11
5 7
12
TOP
VIEW
Vdd
INT2
NC
NC
14
4 8 Vdd
GND
100 nF
C1
GND
1
SCL
SDA
Vdd_IO
Rpu Rpu
Pull-up to be added
Rpu= 10 kOhm
I^2 C configuration
HOST
LSM6DSV16X
Mode 1
(1)
(1)
I^2 C
SPI ( 3 / 4 - w)
/
MIPI I3C®/
Leave pin electrically unconnected and soldered to PCB.
The device core is supplied through the Vdd line. Power supply decoupling capacitors (C1, C2 = 100 nF ceramic)
should be placed as near as possible to the supply pin of the device (common design practice).
The functionality of the device and the measured acceleration/angular rate data is selectable and accessible
through the SPI/I²C/MIPI I3C® interface.
The functions, the threshold, and the timing of the two interrupt pins for each sensor can be completely
programmed by the user through the SPI/I²C/MIPI I3C® interface.
Figure 29. Qvar external connections to pin 2, 3 (Qvar input)
LSM6DSV16X
SDx/AH1/Qvar1
SCx/AH2/Qvar2
500 Ω
500 Ω
110 pF
110 pF
Electrode 1
Electrode 2
D1(1)
D2(1)
(1) ST ESDALCL5-1BM2 is referenced as an ST catalog product but similar features of other ESD diodes also can be used.
Note: Figure 29 provides an example of a test circuit. For a specific application, refer to the related application note.

Application hints
7.2 LSM6DSV16X electrical connections in mode 2
Figure 30. LSM6DSV16X electrical connections in mode 2
Vdd_IO
GND
100 nF
C2
SDO/SA0
MSDA
MSCL
INT1
GND
Vdd_IO
SDASCLCS
11
5 7
12
TOP
VIEW
Vdd
NC
NC
14
(^48) Vdd
GND
100 nF
C1
MDRDY/INT2
GND
1
HOST
LELSMxSMte6Dr6DnaSMlSM^
sensors
Master I^2 C
Mode 2
SCL
SDA
Vdd_IO
Rpu Rpu
Pull-up to be added
Rpu= 10 kOhm
I^2 C configuration
(1)
(1)
I^2 C
SPI ( 3 / 4 - w)
/
MIPI I3C /
LSM6DSV16X
®

Leave pin electrically unconnected and soldered to PCB.
The device core is supplied through the Vdd line. Power supply decoupling capacitors (C1, C2 = 100 nF ceramic)
should be placed as near as possible to the supply pin of the device (common design practice).
The functionality of the device and the measured acceleration/angular rate data is selectable and accessible
through the SPI/I²C/MIPI I3C® primary interface.
The functions, the threshold, and the timing of the two interrupt pins for each sensor can be completely
programmed by the user through the SPI/I²C/MIPI I3C® primary interface.
LSM6DSV16X electrical connections in mode 2
7.3 LSM6DSV16X electrical connections in mode 3
Figure 31. LSM6DSV16X electrical connections in mode 3 (auxiliary 3/4-wire SPI)
Vdd_IO
GND
100 nF
C2
SDO/SA0
INT1
GND
Vdd_IO
SDA
11
5 7
12
TOP
VIEW
Vdd
INT2
SDO_Aux
14
4 8 Vdd
GND
100 nF
C1
SDI_Aux
SPC_Aux
OCS_Aux
1
SCLCS
GND
SCL
SDA
Vdd_IO
Rpu Rpu
Pull-up to be added
Rpu= 10 kOhm
I^2 C configuration
HOST
Camera
module
Mode 3
For XL and/or
gyro data
I^2 C
SPI ( 3 / 4 - w)
/
MIPI I3C /
Aux SPI ( 3 /4-wire)
LSM6DSV16X
®
Note: When mode 3 is used, the pull-up on pins 10 and 11 can be enabled or disabled (refer to Table 23. Internal pin
status). To avoid leakage current, it is not recommended to leave the SPI lines floating (or when the OIS system
is off).
The device core is supplied through the Vdd line. Power supply decoupling capacitors (C1, C2 = 100 nF ceramic)
should be placed as near as possible to the supply pin of the device (common design practice).
The functionality of the device is selectable and accessible through the SPI/I²C/MIPI I3C® primary interface.
Measured acceleration/angular rate data is selectable and accessible through the SPI/I²C/MIPI I3C® primary
interface and auxiliary SPI.
The functions, the threshold, and the timing of the two interrupt pins for each sensor can be completely
programmed by the user through the SPI/I²C/MIPI I3C® interface.

Note: When mode 3 is used, refer to the product application note for the power mode configuration and settings.

LSM6DSV16X electrical connections in mode 3
Table 23. Internal pin status
pin# Name Mode 1 function Mode 2 function Mode 3 function Pin status mode 1 Pin status mode 2 Pin status mode 3 (1)
1
SDO SPI 4-wire interface serialdata output (SDO) SPI 4-wire interface serialdata output (SDO) SPI 4-wire interface serialdata output (SDO)
Default: input without pull-up
Pull-up is enabled if bit
SDO_PU_EN = 1 in register
PIN_CTRL (02h).
Default: input without pull-up
Pull-up is enabled if bit
SDO_PU_EN = 1 in register
PIN_CTRL (02h).
Default: input without pull-up
Pull-up is enabled if bit
SDO_PU_EN = 1 in register
SA0 PIN_CTRL (02h).
I²C least significant bit of
the device address (SA0)
MIPI I3C® least significant
bit of the static address
(SA0)
I²C least significant bit of
the device address (SA0)
MIPI I3C® least significant
bit of the static address
(SA0)
I²C least significant bit of
the device address (SA0)
MIPI I3C® least significant
bit of the static address
(SA0)
2 SDx/AH1/Qvar1
Connect to Vdd_IO or GND
if the analog hub and/or
Qvar are disabled.
Connect to the analog input
or Qvar electrode 1 if the
Qvar function is enabled.(2)
I²C serial data master
(MSDA)
Auxiliary SPI 3/4-wire
interface serial data input
(SDI_Aux) and SPI 3-
wire serial data output
(SDO_Aux)
Default: input without pull-up
Pull-up is enabled if bit
SHUB_PU_EN = 1 in register
IF_CFG (03h).
Default: input without pull-up
Pull-up is enabled if bit
SHUB_PU_EN = 1 in register
IF_CFG (03h).
Default: input without pull-up
Pull-up is enabled if bit
SHUB_PU_EN = 1 in register
IF_CFG (03h).
3 SCx/AH2/Qvar2
Connect to Vdd_IO or GND
if the analog hub and/or
Qvar are disabled.
Connect to the analog input
or Qvar electrode 2 if the
Qvar function is enabled.(2)
I²C serial clock master
(MSCL)
Auxiliary SPI 3/4-wire
interface serial port clock
(SPC_Aux)
Default: input without pull-up
Pull-up is enabled if bit
SHUB_PU_EN = 1 in register
IF_CFG (03h).
Default: input without pull-up
Pull-up is enabled if bit
SHUB_PU_EN = 1 in register
IF_CFG (03h).
Default: input without pull-up
Pull-up is enabled if bit
SHUB_PU_EN = 1 in register
IF_CFG (03h)
4 INT1 Programmable interrupt 1 Programmable interrupt 1 Programmable interrupt 1 Default: output forced to ground Default: output forced to ground Default: output forced to ground
5 Vdd_IO Power supply for I/O pins Power supply for I/O pins Power supply for I/O pins
6 GND 0 V supply 0 V supply 0 V supply
7 GND 0 V supply 0 V supply 0 V supply
8 Vdd Power supply Power supply Power supply
9 INT2
Programmable interrupt 2
(INT2) / Data enabled
(DEN)
Programmable interrupt 2
(INT2) / Data enabled
(DEN) / I²C master external
synchronization signal
(MDRDY)
Programmable interrupt 2
(INT2) / Data enabled
(DEN)
Default: output forced to ground Default: output forced to ground Default: output forced to ground
10 OCS_Aux Connect to Vdd_IO orleave unconnected Connect to Vdd_IO orleave unconnected Auxiliary SPI 3/4-wireinterface enabled
Default: input with pull-up
Pull-up is disabled if bit
OIS_PU_DIS = 1 in register
PIN_CTRL (02h).
Default: input with pull-up
Pull-up is disabled if bit
OIS_PU_DIS = 1 in register
PIN_CTRL (02h).
Default: input without pull-up
(regardless of the value of bit
OIS_PU_DIS in register PIN_CTRL
(02h))
11 SDO_Aux Connect to Vdd_IO orleave unconnected Connect to Vdd_IO orleave unconnected
Auxiliary SPI 3-
wire interface: leave
unconnected / Auxiliary SPI
4-wire interface: serial data
output (SDO_Aux)
Default: input with pull-up
Pull-up is disabled if bit
OIS_PU_DIS = 1 in register
PIN_CTRL (02h).
Default: input with pull-up
Pull-up is disabled if bit
OIS_PU_DIS = 1 in register
PIN_CTRL (02h).
Default: input without pull-up
Pull-up is enabled if bit SIM_OIS = 1
(Aux_SPI 3-wire) in reg 70h and
bit OIS_PU_DIS = 0 in register
PIN_CTRL (02h).
12 CS
I²C/SPI mode selection
(1: SPI idle mode / I²C
communication enabled;
0: SPI communication
mode / I²C disabled)
I²C/SPI mode selection
(1: SPI idle mode / I²C
communication enabled;
0: SPI communication
mode / I²C disabled)
I²C/SPI mode selection
(1: SPI idle mode / I²C
communication enabled;
0: SPI communication
mode / I²C disabled)
Default: input with pull-up
Pull-up is disabled if bit
I2C_I3C_disable = 1 in register
IF_CFG (03h).
Default: input with pull-up
Pull-up is disabled if bit
I2C_I3C_disable = 1 in register
IF_CFG (03h).
Default: input with pull-up
Pull-up is disabled if bit
I2C_I3C_disable = 1 in register
IF_CFG (03h).
DS13510
Rev 4

page 50/198

LSM6DSV16X
LSM6DSV16X
(^) electrical connections in mode 3

pin# Name Mode 1 function Mode 2 function Mode 3 function Pin status mode 1 Pin status mode 2 Pin status mode 3 (1)
13 SCL
I²C/MIPI I3C® serial clock
(SCL) / SPI serial port clock
(SPC)
I²C/MIPI I3C® serial clock
(SCL) / SPI serial port clock
(SPC)
I²C/MIPI I3C® serial clock
(SCL) / SPI serial port clock
(SPC)
Default: input without pull-up Default: input without pull-up Default: input without pull-up
14 SDA
I²C/MIPI I3C® serial
data (SDA) / SPI serial
data input (SDI) / 3-wire
interface serial data output
(SDO)
I²C/MIPI I3C® serial
data (SDA) / SPI serial
data input (SDI) / 3-wire
interface serial data output
(SDO)
I²C/MIPI I3C® serial
data (SDA) / SPI serial
data input (SDI) / 3-wire
interface serial data output
(SDO)
Default: input without pull-up
Pull-up is enabled if bit
SDA_PU_EN = 1 in register IF_CFG
(03h).
Default: input without pull-up
Pull-up is enabled if bit
SDA_PU_EN = 1 in register IF_CFG
(03h).
Default: input without pull-up
Pull-up is enabled if bit
SDA_PU_EN = 1 in register IF_CFG
(03h).
_1. Mode 3 is enabled when the OIS_XL_EN bit or the OIS_G_EN bit in the UI_CTRL1_OIS (70h) / SPI2_CTRL1_OIS (70h) registers is set to 1.

The analog hub and Qvar functions are enabled by setting the AH_QVAR_EN bit to 1 in CTRL7 (16h)._
Internal pull-up value is from 30 kΩ to 50 kΩ, depending on Vdd_IO.
DS13510
Rev 4

page 51/198
LSM6DSV16X
LSM6DSV16X
(^) electrical connections in mode 3

8 Register mapping
The table given below provides a list of the 8/16-bit registers embedded in the device and the corresponding
addresses.
All these registers are accessible from the primary SPI/I²C/MIPI I3C® interface only.
Table 24. Registers address map
Name Type
Register address
Default Comment
Hex Binary
FUNC_CFG_ACCESS R/W 01 00000001 00000000
PIN_CTRL R/W 02 00000010 00100011
IF_CFG R/W 03 00000011 00000000
RESERVED - 04-05
ODR_TRIG_CFG R/W 06 00000110 00000000
FIFO_CTRL1 R/W 07 00000111 00000000
FIFO_CTRL2 R/W 08 00001000 00000000
FIFO_CTRL3 R/W 09 00001001 00000000
FIFO_CTRL4 R/W 0A 00001010 00000000
COUNTER_BDR_REG1 R/W 0B 00001011 00000000
COUNTER_BDR_REG2 R/W 0C 00001100 00000000
INT1_CTRL R/W 0D 00001101 00000000
INT2_CTRL R/W 0E 00001110 00000000
WHO_AM_I R 0F 00001111 01110000 R (SPI2)
CTRL1 R/W 10 00010000 00000000 R (SPI2)
CTRL2 R/W 11 00010001 00000000 R (SPI2)
CTRL3 R/W 12 00010010 01000100 R (SPI2)
CTRL4 R/W 13 00010011 00000000 R (SPI2)
CTRL5 R/W 14 00010100 00000000 R (SPI2)
CTRL6 R/W 15 00010101 00000000 R (SPI2)
CTRL7 R/W 16 00010110 00000000 R (SPI2)
CTRL8 R/W 17 0001 0111 00000000 R (SPI2)
CTRL9 R/W 18 00011000 00000000 R (SPI2)
CTRL10 R/W 19 00011001 00000000 R (SPI2)
CTRL_STATUS R 1A 00011010 output
FIFO_STATUS1 R 1B 00011011 output
FIFO_STATUS2 R 1C 00011100 output
ALL_INT_SRC R 1D 00011101 output
STATUS_REG R 1E 00011110 output
RESERVED - 1F
OUT_TEMP_L R 20 00100000 output
OUT_TEMP_H R 21 00100001 output
OUTX_L_G R 22 00100010 output
OUTX_H_G R 23 00100011 output
Register mapping
Name Type
Register address
Default Comment
Hex Binary
OUTY_L_G R 24 00100100 output

OUTY_H_G R 25 00100101 output

OUTZ_L_G R 26 00100110 output

OUTZ_H_G R 27 00100111 output

OUTX_L_A R 28 00101000 output

OUTX_H_A R 29 00101001 output

OUTY_L_A R 2A 00101010 output

OUTY_H_A R 2B 00101011 output

OUTZ_L_A R 2C 00101100 output

OUTZ_H_A R 2D 00101101 output

UI_OUTX_L_G_OIS_EIS R 2E 00101110 output

UI_OUTX_H_G_OIS_EIS R 2F 00101111 output

UI_OUTY_L_G_OIS_EIS R 30 00110000 output

UI_OUTY_H_G_OIS_EIS R 31 00110001 output

UI_OUTZ_L_G_OIS_EIS R 32 00110010 output

UI_OUTZ_H_G_OIS_EIS R 33 00110011 output

UI_OUTX_L_A_OIS_DualC R 34 00110100 output

UI_OUTX_H_A_OIS_DualC R 35 00110101 output

UI_OUTY_L_A_OIS_DualC R 36 00110110 output

UI_OUTY_H_A_OIS_DualC R 37 00110111 output

UI_OUTZ_L_A_OIS_DualC R 38 00111000 output

UI_OUTZ_H_A_OIS_DualC R 39 00111001 output

AH_QVAR_OUT_L R 3A 00111010 output

AH_QVAR_OUT_H R 3B 00111011 output

RESERVED - 3C-3F

TIMESTAMP0 R 40 01000000 output R (SPI2)

TIMESTAMP1 R 41 01000001 output R (SPI2)

TIMESTAMP2 R 42 01000010 output R (SPI2)

TIMESTAMP3 R 43 01000011 output R (SPI2)

UI_STATUS_REG_OIS R 44 01000100 output

WAKE_UP_SRC R 45 01000101 output

TAP_SRC R 46 01000110 output

D6D_SRC R 47 01000111 output

STATUS_MASTER_
MAINPAGE
R 48 01001000 output

EMB_FUNC_STATUS_
MAINPAGE
R 49 01001001 output

FSM_STATUS_MAINPAGE R 4A 01001010 output

MLC_STATUS_MAINPAGE R 4B 01001011 output

RESERVED - 4C-4E

INTERNAL_FREQ_FINE R 4F 01001111 output

Register mapping
Name Type
Register address
Default Comment
Hex Binary
FUNCTIONS_ENABLE RW 50 01010000 00000000

DEN R/W 51 01010001 00001110

INACTIVITY_DUR R/W 54 01010100 00000100

INACTIVITY_THS R/W 55 01010101 00000000

TAP_CFG0 R/W 56 01010110 00000000

TAP_CFG1 R/W 57 01010111 00000000

TAP_CFG2 R/W 58 01011000 00000000

TAP_THS_6D R/W 59 01011001 00000000

TAP_DUR R/W 5A 01011010 00000000

WAKE_UP_THS R/W 5B 01011011 00000000

WAKE_UP_DUR R/W 5C 01011100 00000000

FREE_FALL R/W 5D 01011101 00000000

MD1_CFG R/W 5E 01011110 00000000

MD2_CFG R/W 5F 01011111 00000000

RESERVED - 60-61

HAODR_CFG R/W 62 01100010 00000000

EMB_FUNC_CFG R/W 63 01100011 00000000

UI_HANDSHAKE_CTRL R/W 64 01100100 00000000

UI_SPI2_SHARED_0 R/W 65 01100101 00000000

UI_SPI2_SHARED_1 R/W 66 01100110 00000000

UI_SPI2_SHARED_2 R/W 67 01100111 00000000

UI_SPI2_SHARED_3 R/W 68 01101000 00000000

UI_SPI2_SHARED_4 R/W 69 01101001 00000000

UI_SPI2_SHARED_5 R/W 6A 01101010 00000000

CTRL_EIS R/W 6B 01101011 00000000

RESERVED - 6C - 6E

UI_INT_OIS

R (SPI2 full-control mode)
R/W (primary IF full-control mode)
6F 01101111 00000000
UI_CTRL1_OIS

R (SPI2 full-control mode)
R/W (primary IF full-control mode)
70 01110000 00000000
UI_CTRL2_OIS

R (SPI2 full-control mode)
R/W (primary IF full-control mode)
71 01110001 00000000
UI_CTRL3_OIS

R (SPI2 full-control mode)
R/W (primary IF full-control mode)
72 01110010 00000000
X_OFS_USR R/W 73 01110011 00000000

Y_OFS_USR R/W 74 01110100 00000000

Z_OFS_USR R/W 75 01110101 00000000

RESERVED - 76-77

FIFO_DATA_OUT_TAG R 78 01111000 output

FIFO_DATA_OUT_X_L R 79 01111001 output

Register mapping
Name Type
Register address
Default Comment
Hex Binary
FIFO_DATA_OUT_X_H R 7A 01111010 output

FIFO_DATA_OUT_Y_L R 7B 01111011 output

FIFO_DATA_OUT_Y_H R 7C 01111100 output

FIFO_DATA_OUT_Z_L R 7D 01111101 output

FIFO_DATA_OUT_Z_H R 7E 01111110 output

Reserved registers must not be changed. Writing to those registers may cause permanent damage to the device.
The content of the registers that are loaded at boot should not be changed. They contain the factory calibration
values. Their content is automatically restored when the device is powered up.
Register mapping
9 Register description
The device contains a set of registers which are used to control its behavior and to retrieve linear acceleration,
angular rate, temperature, analog hub and Qvar data. The register addresses, made up of 7 bits, are used to
identify them and to write the data through the serial interface.
9.1 FUNC_CFG_ACCESS (01h)
Enable embedded functions register (R/W)
Table 25. FUNC_CFG_ACCESS register
EMB_FUNC_
REG_ACCESS
SHUB_REG
_ACCESS^0
(1) 0 (1) FSM_WR_
CTRL_EN
SW_POR SPI2_RESET OIS_CTRL
_FROM_UI
1. This bit must be set to 0 for the correct operation of the device.

Table 26. FUNC_CFG_ACCESS register description
EMB_FUNC_REG_ACCESS
Enables access to the embedded functions configuration registers. (1)
Default value: 0
SHUB_REG_ACCESS
Enables access to the sensor hub (I²C master) configuration registers. (2)
Default value: 0
FSM_WR_CTRL_EN
Enables the control of the CTRL registers to FSM (FSM can change some configurations of the
device autonomously). Default value: 0
(0: disabled; 1: enabled)
SW_POR Global reset of the device. Default value: 0
SPI2_RESET Resets the control registers of SPI2 from the primary interface. This bit must be set to 1 and
then back to 0 (this bit is not automatically cleared). Default value: 0
OIS_CTRL_FROM_UI
Enables the full control of OIS configurations from the primary interface. Default value: 0
(0: OIS chain full control from primary interface disabled;
1: OIS chain full control from primary interface enabled)
1. Details concerning the embedded functions configuration registers are available in Section 12 Embedded functions register
_mapping and Section 13 Embedded functions register description.

Details concerning the sensor hub registers are available in Section 16 Sensor hub register mapping and Section 17 Sensor
hub register description._
Register description
9.2 PIN_CTRL (02h)
SDO, OCS_Aux, SDO_Aux pins pull-up register (R/W). This register is not reset during the software reset
procedure (see bit 0 of the CTRL3 (12h) register).
Table 27. PIN_CTRL register
OIS_
PU_DIS
SDO_
PU_EN
IBHR_
POR_EN^0
(1) 0 (1) 0 (1) 1 (2) 1 (2)
_1. This bit must be set to 0 for the correct operation of the device.

This bit must be set to 1 for the correct operation of the device._
Table 28. PIN_CTRL register description
OIS_PU_DIS
Disables pull-up on both OCS_Aux and SDO_Aux pins (for mode 1 and mode 2). For further details about
the configuration of the pull-up resistors in mode 3, refer to Table 23. Default value: 0
(0: OCS_Aux and SDO_Aux pins with pull-up;
1: OCS_Aux and SDO_Aux pins pull-up disconnected)
SDO_PU_EN
Enables pull-up on SDO pin. For details, refer to Table 23. Default value: 0
(0: SDO pin pull-up disconnected; 1: SDO pin with pull-up)
IBHR_POR_EN
Selects the action the device performs after "reset whole chip" I3C pattern. Default value: 1
(0: configuration reset (SW reset + dynamic address reset);
(1: global reset (POR reset))
PIN_CTRL (02h)
9.3 IF_CFG (03h)
Interface configuration register (R/W). This register is not reset during the software reset procedure (see bit 0 of
the CTRL3 (12h) register).
Table 29. IF_CFG register
SDA_PU_EN
SHUB_
PU_EN ASF_CTRL H_LACTIVE PP_OD SIM^0
(1) I2C_I3C_
disable
1. This bit must be set to 0 for the correct operation of the device.

Table 30. IF_CFG register description
SDA_PU_EN
Enables pull-up on SDA pin. Default value: 0
(0: SDA pin pull-up disconnected;
1: SDA pin with pull-up)
SHUB_PU_EN
Enables master I²C pull-up. Default value: 0
(0: internal pull-up on auxiliary I²C line disabled;
1: internal pull-up on auxiliary I²C line enabled)
ASF_CTRL
Enables anti-spike filters. Default value: 0
(0: anti-spike filters are managed by the protocol and turned off after the broadcast address;
1: anti-spike filters on SCL and SDA lines are always enabled)
H_LACTIVE
Interrupt activation level. Default value: 0
(0: interrupt output pins active high;
1: interrupt output pins active low)
PP_OD
Push-pull/open-drain selection on INT1 and INT2 pins. Default value: 0
(0: push-pull mode;
1: open-drain mode)
SIM
SPI serial interface mode selection. Default value: 0
(0: 4-wire interface;
1: 3-wire interface)
I2C_I3C_disable
Disables I²C and MIPI I3C® interfaces. Default value: 0
(0: SPI, I²C and MIPI I3C® interfaces enabled;
1: I²C and MIPI I3C® interfaces disabled)
9.4 ODR_TRIG_CFG (06h)
ODR-triggered mode configuration register (R/W)
Table 31. ODR_TRIG_CFG register
ODR_TRIG_
NODR_7
ODR_TRIG_
NODR_6
ODR_TRIG_
NODR_5
ODR_TRIG_
NODR_4
ODR_TRIG_
NODR_3
ODR_TRIG_
NODR_2
ODR_TRIG_
NODR_1
ODR_TRIG_
NODR_0
Table 32. ODR_TRIG_CFG register description
ODR_TRIG_NODR_[7:0]
When ODR-triggered mode is set, these bits are used to define the number of data generated in
the reference period.
Allowed values for ODR_TRIG_NODR_[7:0] are 0 (default) and values in the range from 4 to 255.
IF_CFG (03h)
9.5 FIFO_CTRL1 (07h)
FIFO control register 1 (R/W)
Table 33. FIFO_CTRL1 register
WTM_7 WTM_6 WTM_5 WTM_4 WTM_3 WTM_2 WTM_1 WTM_0
Table 34. FIFO_CTRL1 register description
WTM_[7:0]
FIFO watermark threshold: 1 LSB = TAG (1 byte) + 1 sensor (6 bytes) written in FIFO.
Watermark flag rises when the number of bytes written in the FIFO is greater than or equal to the threshold level.
9.6 FIFO_CTRL2 (08h)
FIFO control register 2 (R/W)
Table 35. FIFO_CTRL2 register
STOP_ON
_WTM
FIFO_COMPR
_RT_EN^0
(1) ODR_CHG
_EN^0
(1) UNCOMPR
_RATE_1
UNCOMPR
_RATE_0
XL_DualC_BATCH
_FROM_FSM
1. This bit must be set to 0 for the correct operation of the device.

Table 36. FIFO_CTRL2 register description
STOP_ON_WTM
Sensing chain FIFO stop values memorization at threshold level. Default value: 0
(0: FIFO depth is not limited;
1: FIFO depth is limited to threshold level, defined in FIFO_CTRL1 (07h))
FIFO_COMPR_RT_EN(1)
Enables/disables compression algorithm runtime. Default value: 0
(0: FIFO compression algorithm disabled;
1: FIFO compression algorithm enabled)
ODR_CHG_EN
Enables ODR CHANGE virtual sensor to be batched in FIFO. Default value: 0
(0: ODR CHANGE virtual sensor not batched in FIFO;
1: ODR CHANGE virtual sensor batched in FIFO)
Note: Refer to the product application note for the details regarding operating/power mode
configurations, settings, turn-on/off time and on-the-fly changes.
UNCOMPR_RATE_[1:0]
This field configures the compression algorithm to write uncompressed data at each rate.
(0: uncompressed data writing is not forced (default);
1: uncompressed data every 8 batch data rate;
2: uncompressed data every 16 batch data rate;
3: uncompressed data every 32 batch data rate)
XL_DualC_BATCH_FROM_FSM
When dual-channel mode is enabled, this bit enables FSM-triggered batching in FIFO of
accelerometer channel 2. Default value: 0
(0: disabled; 1: enabled)
1. This bit is activated if the FIFO_COMPR_EN bit of EMB_FUNC_EN_B (05h) is set to 1.

FIFO_CTRL1 (07h)
9.7 FIFO_CTRL3 (09h)
FIFO control register 3 (R/W)
Table 37. FIFO_CTRL3 register
BDR_GY_3 BDR_GY_2 BDR_GY_1 BDR_GY_0 BDR_XL_3 BDR_XL_2 BDR_XL_1 BDR_XL_0
Table 38. FIFO_CTRL3 register description
BDR_GY_[3:0]
Selects batch data rate (write frequency in FIFO) for gyroscope data.
(0000: gyroscope not batched in FIFO (default);
0001: 1.875 Hz;
0010: 7.5 Hz;
0011: 15 Hz;
0100: 30 Hz;
0101: 60 Hz;
0110: 120 Hz;
0111: 240 Hz;
1000: 480 Hz;
1001: 960 Hz;
1010: 1.92 kHz;
1011: 3.84 kHz;
1100: 7.68 kHz
1101-1111: reserved)
BDR_XL_[3:0]
Selects batch data rate (write frequency in FIFO) for accelerometer data.
(0000: accelerometer not batched in FIFO (default);
0001: 1.875 Hz;
0010: 7.5 Hz;
0011: 15 Hz;
0100: 30 Hz;
0101: 60 Hz;
0110: 120 Hz;
0111: 240 Hz;
1000: 480 Hz;
1001: 960 Hz;
1010: 1.92 kHz;
1011: 3.84 kHz;
1100: 7.68 kHz
1101-1111: reserved)
FIFO_CTRL3 (09h)
9.8 FIFO_CTRL4 (0Ah)
FIFO control register 4 (R/W)
Table 39. FIFO_CTRL4 register
DEC_TS_
BATCH_1
DEC_TS_
BATCH_0
ODR_T_
BATCH_1
ODR_T_
BATCH_0
G_EIS_
FIFO_EN
FIFO_
MODE_2
FIFO_
MODE_1
FIFO_
MODE_0
Table 40. FIFO_CTRL4 register description
DEC_TS_BATCH_[1:0]
Selects decimation for timestamp batching in FIFO. Write rate is the maximum rate between the
accelerometer and gyroscope BDR divided by decimation decoder.
(00: timestamp not batched in FIFO (default);
01: decimation 1: max(BDR_XL[Hz],BDR_GY[Hz]) [Hz];
10: decimation 8: max(BDR_XL[Hz],BDR_GY[Hz])/8 [Hz];
11: decimation 32: max(BDR_XL[Hz],BDR_GY[Hz])/32 [Hz])
ODR_T_BATCH_[1:0]
Selects batch data rate (write frequency in FIFO) for temperature data
(00: temperature not batched in FIFO (default);
01: 1.875 Hz;
10: 15 Hz;
11: 60 Hz)
G_EIS_FIFO_EN
Enables FIFO batching of enhanced EIS gyroscope output values. Default value: 0
(0: disabled; 1: enabled)
FIFO_MODE_[2:0]
FIFO mode selection
(000: bypass mode: FIFO disabled (default);
001: FIFO mode: stops collecting data when FIFO is full;
010: continuousWTM-to-full mode: continuous mode with FIFO watermark size until trigger is
deasserted, then data are stored in FIFO until the buffer is full;
011: continuous-to-FIFO mode: continuous mode until trigger is deasserted, then FIFO mode;
100: bypass-to-continuous mode: bypass mode until trigger is deasserted, then continuous mode;
101: reserved;
110: continuous mode: if the FIFO is full, the new sample overwrites the older one;
111: bypass-to-FIFO mode: bypass mode until trigger is deasserted, then FIFO mode.)
FIFO_CTRL4 (0Ah)
9.9 COUNTER_BDR_REG1 (0Bh)
Counter batch data rate register 1 (R/W)
Table 41. COUNTER_BDR_REG1 register
0 (1)
TRIG_COUN
TER_BDR_1
TRIG_COUN
TER_BDR_0
0 (1) 0 (1) 0 (1)
CNT_
BDR_TH_9
CNT_
BDR_TH_8
1. This bit must be set to 0 for the correct operation of the device.

Table 42. COUNTER_BDR_REG1 register description
TRIG_COUNTER_BDR_[1:0]
Selects the trigger for the internal counter of batch events between the accelerometer,
gyroscope and EIS gyroscope.
(00: accelerometer batch event;
01: gyroscope batch event;
10 – 11: gyroscope EIS batch event)
CNT_BDR_TH_[9:8]
In conjunction with CNT_BDR_TH_[7:0] in COUNTER_BDR_REG2 (0Ch), sets the threshold
for the internal counter of batch events. When this counter reaches the threshold, the counter
is reset and the COUNTER_BDR_IA flag in FIFO_STATUS2 (1Ch) is set to 1.
9.10 COUNTER_BDR_REG2 (0Ch)
Counter batch data rate register 2 (R/W)
Table 43. COUNTER_BDR_REG2 register
CNT_
BDR_TH_7
CNT_
BDR_TH_6
CNT_
BDR_TH_5
CNT_
BDR_TH_4
CNT_
BDR_TH_3
CNT_
BDR_TH_2
CNT_
BDR_TH_1
CNT_
BDR_TH_0
Table 44. COUNTER_BDR_REG2 register description
CNT_BDR_TH_[7:0]
In conjunction with CNT_BDR_TH_[9:8] in COUNTER_BDR_REG1 (0Bh), sets the threshold for the
internal counter of batch events. When this counter reaches the threshold, the counter is reset and the
COUNTER_BDR_IA flag in FIFO_STATUS2 (1Ch) is set to 1.
COUNTER_BDR_REG1 (0Bh)
9.11 INT1_CTRL (0Dh)
INT1 pin control register (R/W)
Each bit in this register enables a signal to be carried over INT1 when the MIPI I3C® dynamic address is not
assigned (I²C or SPI is used). Some bits can be also used to trigger an IBI (in-band interrupt) when the MIPI
I3C® interface is used. The output of the pin is the OR combination of the signals selected here and in MD1_CFG
(5Eh).
Table 45. INT1_CTRL register
0 (1)
INT1_
CNT_BDR
INT1_
FIFO_FULL
INT1_
FIFO_OVR
INT1_
FIFO_TH^0
(1) INT1_
DRDY_G
INT1_
DRDY_XL
1. This bit must be set to 0 for the correct operation of the device.

Table 46. INT1_CTRL register description
INT1_CNT_BDR Enables COUNTER_BDR_IA interrupt on INT1 pin. Default value: 0
INT1_FIFO_FULL Enables FIFO full flag interrupt on INT1 pin. It can be also used to trigger an IBI when the MIPI I3C
®
interface is used. Default value: 0
INT1_FIFO_OVR
Enables FIFO overrun interrupt on INT1 pin. It can be also used to trigger an IBI when the MIPI
I3C® interface is used. Default value: 0
INT1_FIFO_TH
Enables FIFO threshold interrupt on INT1 pin. It can be also used to trigger an IBI when the MIPI
I3C® interface is used. Default value: 0
INT1_DRDY_G
Enables gyroscope data-ready interrupt on INT1 pin. It can be also used to trigger an IBI when the MIPI
I3C® interface is used. Default value: 0
INT1_DRDY_XL
Enables accelerometer data-ready interrupt on INT1 pin. It can be also used to trigger an IBI when the
MIPI I3C® interface is used. Default value: 0
INT1_CTRL (0Dh)
9.12 INT2_CTRL (0Eh)
INT2 pin control register (R/W)
Each bit in this register enables a signal to be carried over INT2 when the MIPI I3C® dynamic address is not
assigned (I²C or SPI is used). Some bits can be also used to trigger an IBI when the MIPI I3C® interface is used.
The output of the pin is the OR combination of the signals selected here and in MD2_CFG (5Fh).
Table 47. INT2_CTRL register
INT2_EMB_
FUNC_ENDOP
INT2_
CNT_BDR
INT2_
FIFO_FULL
INT2_
FIFO_OVR
INT2_
FIFO_TH
INT2_
DRDY_G_EIS
INT2_
DRDY_G
INT2_
DRDY_XL
Table 48. INT2_CTRL register description
INT2_EMB_FUNC_ENDOP
Enables routing the embedded functions end of operations signal to the INT2 pin.
Default value: 0
INT2_CNT_BDR Enables COUNTER_BDR_IA interrupt on INT2. Default value: 0
INT2_FIFO_FULL Enables FIFO full flag interrupt on INT2 pin.Default value: 0
INT2_FIFO_OVR Enables FIFO overrun interrupt on INT2 pin. Default value: 0
INT2_FIFO_TH Enables FIFO threshold interrupt on INT2 pin. Default value: 0
INT2_DRDY_G_EIS Enables gyroscope EIS data-ready interrupt on INT2 pin. Default value: 0
INT2_DRDY_G Gyroscope data-ready interrupt on INT2 pin. Default value: 0
INT2_DRDY_XL Accelerometer data-ready interrupt on INT2 pin. Default value: 0
9.13 WHO_AM_I (0Fh)
WHO_AM_I register (R). This is a read-only register. Its value is fixed at 70h.
Table 49. WhoAmI register
0 1 1 1 0 0 0 0
INT2_CTRL (0Eh)
9.14 CTRL1 (10h)
Accelerometer control register 1 (R/W)
Table 50. CTRL1 register
0 (1)
OP_MODE_
XL_2
OP_MODE_
XL_1
OP_MODE_
XL_0
ODR_XL_3 ODR_XL_2 ODR_XL_1 ODR_XL_0
1. This bit must be set to 0 for the correct operation of the device.

Table 51. CTRL1 register description
OP_MODE_XL_[2:0]
Accelerometer operating mode selection.
(000: high-performance mode (default);
001: high-accuracy ODR mode;
010: reserved;
011: ODR-triggered mode;
100: low-power mode 1 (2 mean);
101: low-power mode 2 (4 mean);
110: low-power mode 3 (8 mean);
111: normal mode)
ODR_XL_[3:0] Accelerometer ODR selection (see Table 52)
Table 52. Accelerometer ODR selection
ODR_XL_3 ODR_XL_2 ODR_XL_1 ODR_XL_0 ODR selection [Hz]
0 0 0 0 Power-down (default)
0 0 0 1 1.875 Hz (low-power mode)
0 0 1 0 7.5 Hz (high-performance, normal mode)
0 0 1 1 15 Hz (low-power, high-performance, normal mode)
0 1 0 0 30 Hz (low-power, high-performance, normal mode)
0 1 0 1 60 Hz (low-power, high-performance, normal mode)
0 1 1 0 120 Hz (low-power, high-performance, normal mode)
0 1 1 1 240 Hz (low-power, high-performance, normal mode)
1 0 0 0 480 Hz (high-performance, normal mode)
1 0 0 1 960 Hz (high-performance, normal mode)
1 0 1 0 1.92 kHz (high-performance, normal mode)
1 0 1 1 3.84 kHz (high-performance mode)
1 1 0 0 7.68 kHz (high-performance mode)
Others Reserved
CTRL1 (10h)
9.15 CTRL2 (11h)
Gyroscope control register 2 (R/W)
Table 53. CTRL2 register
0 (1)
OP_MODE_
G_2
OP_MODE_
G_1
OP_MODE_
G_0
ODR_G_3 ODR_G_2 ODR_G_1 ODR_G_0
1. This bit must be set to 0 for the correct operation of the device.

Table 54. CTRL2 register description
OP_MODE_G_[2:0]
Gyroscope operating mode selection.
(000: high-performance mode (default);
001: high-accuracy ODR mode;
010: reserved;
011: ODR-triggered mode;
100: sleep mode;
101: low-power mode;
110-111: reserved)
ODR_G_[3:0]
Gyroscope output data rate selection.
(See Table 55)
Table 55. Gyroscope ODR selection
ODR_G_3 ODR_G_2 ODR_G_1 ODR_G_0 ODR [Hz]
0 0 0 0 Power-down (default)
0 0 1 0 7.5 Hz (low-power, high-performance mode)
0 0 1 1 15 Hz (low-power, high-performance mode)
0 1 0 0 30 Hz (low-power, high-performance mode)
0 1 0 1 60 Hz (low-power, high-performance mode)
0 1 1 0 120 Hz (low-power, high-performance mode)
0 1 1 1 240 Hz (low-power, high-performance mode)
1 0 0 0 480 Hz (high-performance mode)
1 0 0 1 960 Hz (high-performance mode)
1 0 1 0 1.92 kHz (high-performance mode)
1 0 1 1 3.84 kHz (high-performance mode)
1 1 0 0 7.68 kHz (high-performance mode)
Others Reserved
CTRL2 (11h)
9.16 CTRL3 (12h)
Control register 3 (R/W)
Table 56. CTRL3 register
BOOT BDU 0 (1) 0 (1) 0 (1) IF_INC 0 (1) SW_RESET
1. This bit must be set to 0 for the correct operation of the device.

Table 57. CTRL3 register description
BOOT
Reboots memory content. This bit is automatically cleared. Default value: 0
(0: normal mode; 1: reboot memory content)
BDU
Block data update. Default value: 1
(0: continuous update;
1: output registers are not updated until LSB and MSB have been read)
IF_INC
Register address automatically incremented during a multiple byte access with a serial interface (I²C, MIPI I3C,
or SPI). Default value: 1
(0: disabled; 1: enabled)
SW_RESET
Software reset, resets all control registers to their default value. This bit is automatically cleared. Default
value: 0
(0: normal mode; 1: reset device)
CTRL3 (12h)
9.17 CTRL4 (13h)
Control register 4 (R/W)
Table 58. CTRL4 register
0 (1) 0 (1) 0 (1)
INT2_on
_INT1
DRDY_
MASK
INT2_
DRDY_TEMP
DRDY_
PULSED
INT2_
IN_LH
1. This bit must be set to 0 for the correct operation of the device.

Table 59. CTRL4 register description
INT2_on_INT1
Enables routing the embedded functions interrupt signals to the INT1 pin. Default value: 0
The corresponding bits in the INT2 control registers need to be enabled.
These interrupts are in OR with those enabled on the INT1 pin.
They are not fed to the INT2 pin.
The movable interrupts are:
INT2_DRDY_G_EIS and INT2_EMB_FUNC_ENDOP, enabled through INT2_CTRL (0Eh)
INT2_TIMESTAMP enabled through MD2_CFG (5Fh)
INT2_DRDY_TEMP enabled through CTRL4 (13h)
INT2_DRDY_AH_QVAR enabled through Section 9.20
DRDY_MASK
Enables / masks data-ready signal. Default value: 0
(0: disabled;
1: masks DRDY signals (both accelerometer and gyroscope) until filter settling ends (accelerometer and
gyroscope independently masked))
Note: Refer to the product application note for the details regarding operating/power mode
configurations, settings, turn-on/off time and on-the-fly changes.
INT2_DRDY_TEMP
Enables temperature sensor data-ready interrupt on the INT2 pin. It can be also used to trigger an IBI
when the MIPI I3C® interface is used and INT2_ON_INT1 = 1 in CTRL4_C (13h). Default value: 0
(0: disabled; 1: enabled)
DRDY_PULSED
Enables pulsed data-ready mode. Default value: 0
(0: data-ready latched mode (returns to 0 only after the higher part of the associated output register has
been read);
1: data-ready pulsed mode (the data-ready pulses are 65 μs long))
INT2_IN_LH
Set to 1 in order to change the polarity of the INT2 pin input trigger for DEN or embedded functions.
Default value: 0
(0: trigger for DEN and embedded functions pin is active low;
1: trigger for DEN and embedded functions pin is active high)
CTRL4 (13h)
9.18 CTRL5 (14h)
Control register 5 (R/W)
Table 60. CTRL5 register
0 (1) 0 (1) 0 (1) 0 (1) 0 (1)
BUS_ACT_
SEL_1
BUS_ACT_
SEL_0
INT_EN_I3C
1. This bit must be set to 0 for the correct operation of the device.

Table 61. CTRL5 register description
BUS_ACT_SEL_[1:0]
Bus available time selection for IBI (in-band interrupt):
00: 2 μs;
01: 50 μs (default);
10: 1 ms;
11: 25 ms)
INT_EN_I3C
Enables INT pin when I3C is enabled. Default value: 0
(0: disabled; 1: enabled)
9.19 CTRL6 (15h)
Control register 6 (R/W)
Table 62. CTRL6 register
0 (1)
LPF1_G_
BW_2
LPF1_G_
BW_1
LPF1_G_
BW_0
FS_G_3 FS_G_2 FS_G_1 FS_G_0
1. This bit must be set to 0 for the correct operation of the device.

Table 63. CTRL6 register description
LPF1_G_BW_[2:0]
Gyroscope low-pass filter (LPF1) bandwidth selection
Table 64 shows the selectable bandwidth values (available if OIS and/or EIS are disabled).
FS_G_[3:0]
Gyroscope UI chain full-scale selection:
(0000: ±125 dps (default);
0001: ±250 dps;
0010: ±500 dps;
0011: ±1000 dps;
0100: ±2000 dps;
1100: ±4000 dps(1)
Others: reserved)
1. When FS = ±4000 dps is selected, the gyroscope OIS chain must be disabled (OIS_G_EN bit of UI_CTRL1_OIS (70h) /
SPI2_CTRL1_OIS (70h) must be set to 0).

CTRL5 (14h)
Table 64. Gyroscope LPF1 + LPF2 bandwidth selection
LPF1_G_
BW_[2:0] 60 Hz 120 Hz 240 Hz 480 Hz 960 Hz 1.92 kHz 3.84 kHz 7.68 kHz
000 24.6 49.4 96 175 241 273 280 281
001 24.6 49.4 96 157 195 210 213 213
010 24.6 49.4 96 131 149 155 156 156
011 24.6 49.4 96 188 310 387 403 407
100 24.6 49.4 78.4 94 100 101 102 102
101 24.6 42.6 53 56.7 57.9 58.2 58.3 58
110 18.0 24.2 27.3 28.4 28.7 28.8 28.8 28.8
111 12.1 13.6 14.2 14.3 14.4 14.4 14.4 14.4
9.20 CTRL7 (16h)
Control register 7 (R/W)
Table 65. CTRL7 register
AH_QVAR_
EN
INT2_DRDY_
AH_QVAR
AH_QVAR_
C_ZIN_1
AH_QVAR_
C_ZIN_0^0
(1) 0 (1) 0 (1) LPF1_G_EN
1. This bit must be set to 0 for the correct operation of the device.

Table 66. CTRL7 register description
AH_QVAR_EN
Enables the analog hub and Qvar chain. When this bit is set to 1, the analog hub and Qvar buffers
are connected to the SDx/AH1/Qvar1 and SCx/AH2/Qvar2 pins. Before setting this bit to 1, the
accelerometer and gyroscope sensors have to be configured in power-down mode. Default value: 0
(0: disabled; 1: enabled)
INT2_DRDY_AH_QVAR
Analog hub and Qvar data-ready interrupt on the INT2 pin. Default value: 0
(0: disabled; 1: enabled)
AH_QVAR_C_ZIN_[1:0]
Configures the equivalent input impedance of the analog hub and Qvar buffers.
(00: 2.4 GΩ (default);
01: 730 MΩ;
10: 300 MΩ;
11: 235 MΩ)
LPF1_G_EN
Enables the gyroscope digital LPF1 filter. If the OIS chain is disabled, the bandwidth can be
selected through LPF1_G_BW_[2:0] in CTRL6 (15h)
CTRL7 (16h)
9.21 CTRL8 (17h)
Control register 8 (R/W)
Table 67. CTRL8 register
HP_LPF2_
XL_BW_2
HP_LPF2_
XL_BW_1
HP_LPF2_
XL_BW_0^0
(1) XL_DualC_EN 0 (1) FS_XL_1 FS_XL_0
1. This bit must be set to 0 for the correct operation of the device.

Table 68. CTRL8 register description
HP_LPF2_XL_BW_[2:0] Accelerometer LPF2 and HP filter configuration and cutoff setting. Refer to Table 69.
XL_DualC_EN
Enables dual-channel mode. When this bit is set to 1, data with the maximum full scale are sent to the output
registers at addresses 34h to 39h. The UI processing chain is used. Default value: 0
(0: disabled; 1: enabled)
FS_XL_[1:0]
Accelerometer full-scale selection:
(00: ±2 g ;
01: ±4 g ;
10: ±8 g ;
11: ±16 g )
Table 69. Accelerometer bandwidth configurations
Filter type HP_SLOPE_
XL_EN
LPF2_XL_EN HP_LPF2_XL_BW_[2:0] Bandwidth
Low pass 0
0 - ODR/2(1)
1
000 ODR/4
001 ODR/10
010 ODR/20
011 ODR/45
100 ODR/100
101 ODR/200
110 ODR/400
111 ODR/800
High pass 1 -
000 SLOPE (ODR/4)
001 ODR/10
010 ODR/20
011 ODR/45
100 ODR/100
101 ODR/200
110 ODR/400
111 ODR/800
1. This value is ODR/2 when the accelerometer is in high-performance mode, high-accuracy ODR mode and normal mode. It
is equal to 2300 Hz when the accelerometer is in low-power mode 1 (2 mean), 912 Hz in low-power mode 2 (4 mean) and
431 Hz in low-power mode 3 (8 mean).

CTRL8 (17h)
9.22 CTRL9 (18h)
Control register 9 (R/W)
Table 70. CTRL9 register
0 (1)
HP_REF_
MODE_XL
XL_FASTSET
TL_MODE
HP_SLOPE_
XL_EN
LPF2_XL_EN 0 (1) USR_OFF_W
USR_OFF_
ON_OUT
1. This bit must be set to 0 for the correct operation of the device.

Table 71. CTRL9 register description
HP_REF_MODE_XL
Enables accelerometer high-pass filter reference mode (valid for high-pass path -
HP_SLOPE_XL_EN bit must be 1). Default value: 0
(0: disabled, 1: enabled)(1)
XL_FASTSETTL_MODE
Enables accelerometer LPF2 and HPF fast-settling mode. The filter sets the first sample after
writing this bit. Active only during device exit from power-down mode. Default value: 0
(0: disabled, 1: enabled)
HP_SLOPE_XL_EN
Accelerometer slope filter / high-pass filter selection. Refer to Figure 32. Default value: 0
(0: low-pass filter path selected;
1: high-pass filter path selected)
LPF2_XL_EN
Accelerometer high-resolution selection. Refer to Figure 32. Default value: 0
(0: output from first stage digital filtering selected;
1: output from LPF2 second filtering stage selected)
USR_OFF_W
Weight of XL user offset bits of registers X_OFS_USR (73h), Y_OFS_USR (74h), Z_OFS_USR
(75h). Default value: 0
(0: 2-10 g /LSB;
1: 2-6 g /LSB)
USR_OFF_ON_OUT
Enables accelerometer user offset correction block; it is valid for the low-pass path. Refer to
Figure 32. Default value: 0
(0: accelerometer user offset correction block bypassed;
1: accelerometer user offset correction block enabled)
1. When enabled, the first output data has to be discarded.

CTRL9 (18h)
Figure 32. Accelerometer block diagram
SLOPE
FILTER
000
001
010
...
111
SPI /
I^2 C /
MIPI I3C
1
0
HP_SLOPE_XL_EN
LPF2_XL_EN
0
1
Digital
HP Filter
HP_LPF2_XL_BW_[2:0]
Digital
LP Filter
LPF 2
S/D Tap
6 D / 4 D
0
1
LOW_PASS_ON_6D
1
0
SLOPE_FDS
Wake-up
Activity /
Inactivity
Free-fall
Embedded
functions
FIFO
USER
OFFSET
0
1
USR_OFF_ON_OUT
USR_OFF_W
OFS_USR_[7: 0 ]
1
0
USR_OFF_ON_WU
LPF 1
Output (^1 )
®
HP_LPF2_XL_BW_[2:0]
HP_LPF2_XL_BW_[2:0]
The cutoff value of the LPF1 output is ODR/2 when the accelerometer is in high-performance mode,
high-accuracy ODR mode or normal mode. This value is equal to 2300 Hz when the accelerometer is in
low-power mode 1 (2 mean), 912 Hz in low-power mode 2 (4 mean) or 431 Hz in low-power mode 3 (8
mean).
CTRL9 (18h)
9.23 CTRL10 (19h)
Control register 10 (R/W)
Table 72. CTRL10 register
0 (1)
EMB_FUNC_
DEBUG
0 (1) 0 (1) ST_G_1 ST_G_0 ST_XL_1 ST_XL_0
1. This bit must be set to 0 for the correct operation of the device.

Table 73. CTRL10 register description
EMB_FUNC_DEBUG
Enables debug mode for the embedded functions.
(0: disabled; 1: enabled)
ST_G_[1:0]
Gyroscope self-test selection
(00: normal mode (default);
01: positive sign self-test;
10: negative sign self-test;
11: reserved)
ST_XL_[1:0]
Accelerometer self-test selection
(00: normal mode (default);
01: positive sign self-test;
10: negative sign self-test;
11: reserved)
9.24 CTRL_STATUS (1Ah)
(R)
Table 74. CTRL_STATUS register
(^00000) CTRL_STATUSFSM_WR_ - 0
Table 75. CTRL_STATUS register description
FSM_WR_CTRL_STATUS
This flag indicates the current controller of the device configuration registers. This flag must
be used as an acknowledge flag when the value of the FSM_WR_CTRL_EN bit in the
FUNC_CFG_ACCESS (01h) register is changed. Default value: 0
(0: all registers and configurations are writable from the standard interface;
1: some registers and configurations are under FSM control and are in read-only mode from the
standard interface).
CTRL10 (19h)

9.25 FIFO_STATUS1 (1Bh)
FIFO status register 1 (R)
Table 76. FIFO_STATUS1 register
DIFF_
FIFO_7
DIFF_
FIFO_6
DIFF_
FIFO_5
DIFF_
FIFO_4
DIFF_
FIFO_3
DIFF_
FIFO_2
DIFF_
FIFO_1
DIFF_
FIFO_0
Table 77. FIFO_STATUS1 register description
DIFF_FIFO_[7:0]
Number of unread sensor data (TAG + 6 bytes) stored in FIFO
In conjunction with DIFF_FIFO_8 in FIFO_STATUS2 (1Ch).
9.26 FIFO_STATUS2 (1Ch)
FIFO status register 2 (R)
Table 78. FIFO_STATUS2 register
FIFO_
WTM_IA
FIFO_
OVR_IA
FIFO_
FULL_IA
COUNTER_
BDR_IA
FIFO_OVR_
LATCHED
0 0
DIFF_
FIFO_8
Table 79. FIFO_STATUS2 register description
FIFO_WTM_IA
FIFO watermark status. Default value: 0
(0: FIFO filling is lower than WTM;
1: FIFO filling is equal to or greater than WTM)
Watermark is set through bits WTM[7:0] in FIFO_CTRL2 (08h) and FIFO_CTRL1 (07h).
FIFO_OVR_IA
FIFO overrun status. Default value: 0
(0: FIFO is not completely filled; 1: FIFO is completely filled)
FIFO_FULL_IA
Smart FIFO full status. Default value: 0
(0: FIFO is not full; 1: FIFO will be full at the next ODR)
COUNTER_BDR_IA
Counter BDR reaches the CNT_BDR_TH_[10:0] threshold set in COUNTER_BDR_REG1 (0Bh) and
COUNTER_BDR_REG2 (0Ch). Default value: 0
This bit is reset when these registers are read.
FIFO_OVR_LATCHED
Latched FIFO overrun status. Default value: 0
This bit is reset when this register is read.
DIFF_FIFO_8
Number of unread sensor data (TAG + 6 bytes) stored in FIFO. Default value: 00
In conjunction with DIFF_FIFO[7:0] in FIFO_STATUS1 (1Bh)
FIFO_STATUS1 (1Bh)
9.27 ALL_INT_SRC (1Dh)
Source register for all interrupts (R)
Table 80. ALL_INT_SRC register
EMB_
FUNC_IA
SHUB_IA
SLEEP_
CHANGE_IA
D6D_IA 0 TAP_IA WU_IA FF_IA
Table 81. ALL_INT_SRC register description
EMB_FUNC_IA
Embedded functions interrupt status. Default value: 0
(0: embedded functions event not detected;
1: embedded functions event detected)
SHUB_IA
Sensor hub (I²C master) interrupt status. Default value: 0
(0: sensor hub interrupt not generated;
1: sensor hub interrupt generated)
SLEEP_CHANGE_IA
Detects change event in activity/inactivity status. Default value: 0
(0: change status not detected; 1: change status detected)
D6D_IA
Interrupt active for change in position of portrait, landscape, face-up, face-down. Default value: 0
(0: change in position not detected; 1: change in position detected)
TAP_IA
Single or double-tap event detection status depending on SINGLE_DOUBLE_TAP_bit value (see
WAKE_UP_THS (5Bh) register). Default value: 0
(0: tap event not detected; 1: tap event detected)
WU_IA
Wake-up event status. Default value: 0
(0: event not detected, 1: event detected)
FF_IA
Free-fall event status. Default value: 0
(0: event not detected, 1: event detected)
ALL_INT_SRC (1Dh)
9.28 STATUS_REG (1Eh)
The STATUS_REG register is read by the primary interface SPI/I²C & MIPI I3C® (R).
Table 82. STATUS_REG register
TIMESTAMP_
ENDCOUNT^0 OIS_DRDY GDA_EIS AH_QVARDA TDA GDA XLDA
Table 83. STATUS_REG register description
TIMESTAMP_ENDCOUNT Alerts timestamp overflow within 5.6 ms
OIS_DRDY
Accelerometer OIS or gyroscope OIS new output data available. Default value: 0
(0: no set of data (accelerometer or gyroscope) available on OIS chain;
1: a new set of data (accelerometer or gyroscope) is available on OIS chain)
GDA_EIS
Enhanced EIS gyroscope new data available. Default value: 0
(0: no set of data available at gyroscope output;
1: a new set of data is available at gyroscope output)
AH_QVARDA
Analog hub or Qvar new data available. Default value: 0
(0: no set of data available at the analog hub or Qvar data output;
1: a new set of data is available at the analog hub or Qvar data output)
TDA
Temperature new data available. Default: 0
(0: no set of data is available at temperature sensor output;
1: a new set of data is available at temperature sensor output)
GDA
Gyroscope new data available. Default value: 0
(0: no set of data available at gyroscope output;
1: a new set of data is available at gyroscope output)
XLDA
Accelerometer new data available. Default value: 0
(0: no set of data available at accelerometer output;
1: a new set of data is available at accelerometer output)
STATUS_REG (1Eh)
9.29 OUT_TEMP_L (20h), OUT_TEMP_H (21h)
Temperature data output register (R). L and H registers together express a 16-bit word in two’s complement.
Table 84. OUT_TEMP_L register
Temp7 Temp6 Temp5 Temp4 Temp3 Temp2 Temp1 Temp0
Table 85. OUT_TEMP_H register
Temp15 Temp14 Temp13 Temp12 Temp11 Temp10 Temp9 Temp8
Table 86. OUT_TEMP register description
Temp[15:0]
Temperature sensor output data
The value is expressed in two's complement.
9.30 OUTX_L_G (22h) and OUTX_H_G (23h)
Angular rate sensor pitch axis (X) angular rate output register (R). The value is expressed as a 16-bit word in
two’s complement.
Data are according to the full-scale (CTRL6 (15h)) and ODR settings (CTRL2 (11h)) of the gyroscope user
interface.
Table 87. OUTX_L_G register
D7 D6 D5 D4 D3 D2 D1 D0
Table 88. OUTX_H_G register
D15 D14 D13 D12 D11 D10 D9 D8
Table 89. OUTX_G register description
D[15:0] Gyroscope UI chain pitch axis (X) angular rate output value
OUT_TEMP_L (20h), OUT_TEMP_H (21h)
9.31 OUTY_L_G (24h) and OUTY_H_G (25h)
Angular rate sensor roll axis (Y) angular rate output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the full-scale (CTRL6 (15h)) and ODR settings (CTRL2 (11h)) of the gyroscope user
interface.
Table 90. OUTY_L_G register
D7 D6 D5 D4 D3 D2 D1 D0
Table 91. OUTY_H_G register
D15 D14 D13 D12 D11 D10 D9 D8
Table 92. OUTY_G register description
D[15:0] Gyroscope UI chain roll axis (Y) angular rate output value
9.32 OUTZ_L_G (26h) and OUTZ_H_G (27h)
Angular rate sensor yaw axis (Z) angular rate output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the full-scale (CTRL6 (15h)) and ODR settings (CTRL2 (11h)) of the gyroscope user
interface.
Table 93. OUTZ_L_G register
D7 D6 D5 D4 D3 D2 D1 D0
Table 94. OUTZ_H_G register
D15 D14 D13 D12 D11 D10 D9 D8
Table 95. OUTZ_H_G register description
D[15:0] Gyroscope UI chain yaw axis (Z) angular rate output value
OUTY_L_G (24h) and OUTY_H_G (25h)
9.33 OUTX_L_A (28h) and OUTX_H_A (29h)
Linear acceleration sensor X-axis output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the full-scale (CTRL8 (17h)) and ODR settings (CTRL1 (10h)) of the accelerometer user
interface.
Table 96. OUTX_L_A register
D7 D6 D5 D4 D3 D2 D1 D0
Table 97. OUTX_H_A register
D15 D14 D13 D12 D11 D10 D9 D8
Table 98. OUTX_A register description
D[15:0] Accelerometer UI chain X-axis linear acceleration output value
9.34 OUTY_L_A (2Ah) and OUTY_H_A (2Bh)
Linear acceleration sensor Y-axis output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the full-scale (CTRL8 (17h)) and ODR settings (CTRL1 (10h)) of the accelerometer user
interface.
Table 99. OUTY_L_A register
D7 D6 D5 D4 D3 D2 D1 D0
Table 100. OUTY_H_A register
D15 D14 D13 D12 D11 D10 D9 D8
Table 101. OUTY_A register description
D[15:0] Accelerometer UI chain Y-axis linear acceleration output value
OUTX_L_A (28h) and OUTX_H_A (29h)
9.35 OUTZ_L_A (2Ch) and OUTZ_H_A (2Dh)
Linear acceleration sensor Z-axis output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the full-scale (CTRL8 (17h)) and ODR settings (CTRL1 (10h)) of the accelerometer user
interface.
Table 102. OUTZ_L_A register
D7 D6 D5 D4 D3 D2 D1 D0
Table 103. OUTZ_H_A register
D15 D14 D13 D12 D11 D10 D9 D8
Table 104. OUTZ_A register description
D[15:0] Accelerometer UI chain Z-axis linear acceleration output value
9.36 UI_OUTX_L_G_OIS_EIS (2Eh) and UI_OUTX_H_G_OIS_EIS (2Fh)
Angular rate sensor pitch axis (X) angular rate output register (R). The value is expressed as a 16-bit word in
two’s complement.
Data are according to the gyroscope full-scale and ODR settings of the OIS gyroscope or the EIS gyroscope
channel.
Table 105. UI_OUTX_L_G_OIS_EIS register
D7 D6 D5 D4 D3 D2 D1 D0
Table 106. UI_OUTX_H_G_OIS_EIS register
D15 D14 D13 D12 D11 D10 D9 D8
Table 107. UI_OUTX_G_OIS_EIS register description
D[15:0] Gyroscope pitch axis OIS/EIS output expressed in two's complement
OUTZ_L_A (2Ch) and OUTZ_H_A (2Dh)
9.37 UI_OUTY_L_G_OIS_EIS (30h) and UI_OUTY_H_G_OIS_EIS (31h)
Angular rate sensor roll axis (Y) angular rate output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the gyroscope full-scale and ODR settings of the OIS gyroscope or the EIS gyroscope
channel.
Table 108. UI_OUTY_L_G_OIS_EIS register
D7 D6 D5 D4 D3 D2 D1 D0
Table 109. UI_OUTY_H_G_OIS_EIS register
D15 D14 D13 D12 D11 D10 D9 D8
Table 110. UI_OUTY_G_OIS_EIS register description
D[15:0] Gyroscope roll axis OIS/EIS output expressed in two's complement
9.38 UI_OUTZ_L_G_OIS_EIS (32h) and UI_OUTZ_H_G_OIS_EIS (33h)
Angular rate sensor yaw axis (Z) angular rate output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the gyroscope full-scale and ODR settings of the OIS gyroscope or the EIS gyroscope
channel.
Table 111. UI_OUTZ_L_G_OIS_EIS register
D7 D6 D5 D4 D3 D2 D1 D0
Table 112. UI_OUTZ_H_G_OIS_EIS register
D15 D14 D13 D12 D11 D10 D9 D8
Table 113. UI_OUTZ_G_OIS_EIS register description
D[15:0] Gyroscope yaw axis OIS/EIS output expressed in two's complement
UI_OUTY_L_G_OIS_EIS (30h) and UI_OUTY_H_G_OIS_EIS (31h)
9.39 UI_OUTX_L_A_OIS_DualC (34h) and UI_OUTX_H_A_OIS_DualC (35h)
Linear acceleration sensor X-axis output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the accelerometer full-scale and ODR settings of the OIS accelerometer or according to the
accelerometer dual-channel mode configuration.
Table 114. UI_OUTX_L_A_OIS_DualC register
D7 D6 D5 D4 D3 D2 D1 D0
Table 115. UI_OUTX_H_A_OIS_DualC register
D15 D14 D13 D12 D11 D10 D9 D8
Table 116. UI_OUTX_A_OIS_DualC register description
D[15:0] Accelerometer X-axis OIS/DualC output expressed in two's complement
9.40 UI_OUTY_L_A_OIS_DualC (36h) and UI_OUTY_H_A_OIS_DualC (37h)
Linear acceleration sensor Y-axis output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the accelerometer full-scale and ODR settings of the OIS accelerometer or according to the
accelerometer dual-channel mode configuration.
Table 117. UI_OUTY_L_A_OIS_DualC register
D7 D6 D5 D4 D3 D2 D1 D0
Table 118. UI_OUTY_H_A_OIS_DualC register
D15 D14 D13 D12 D11 D10 D9 D8
Table 119. UI_OUTY_A_OIS_DualC register description
D[15:0] Accelerometer Y-axis OIS/DualC output expressed in two's complement
UI_OUTX_L_A_OIS_DualC (34h) and UI_OUTX_H_A_OIS_DualC (35h)
9.41 UI_OUTZ_L_A_OIS_DualC (38h) and UI_OUTZ_H_A_OIS_DualC (39h)
Linear acceleration sensor Z-axis output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the accelerometer full-scale and ODR settings of the OIS accelerometer or according to the
accelerometer dual-channel mode configuration.
Table 120. UI_OUTZ_L_A_OIS_DualC register
D7 D6 D5 D4 D3 D2 D1 D0
Table 121. UI_OUTZ_H_A_OIS_DualC register
D15 D14 D13 D12 D11 D10 D9 D8
Table 122. UI_OUTZ_A_OIS_DualC register description
D[15:0] Accelerometer Z-axis OIS/DualC output expressed in two's complement
9.42 AH_QVAR_OUT_L (3Ah) and AH_QVAR_OUT_H (3Bh)
Analog hub and Qvar data output register (R). L and H registers together express a 16-bit word in two’s
complement.
Table 123. AH_QVAR_OUT_L register
AH_Qvar_7 AH_Qvar_6 AH_Qvar_5 AH_Qvar_4 AH_Qvar_3 AH_Qvar_2 AH_Qvar_1 AH_Qvar_0
Table 124. AH_QVAR_OUT_H register
AH_Qvar_15 AH_Qvar_14 AH_Qvar_13 AH_Qvar_12 AH_Qvar_11 AH_Qvar_10 AH_Qvar_9 AH_Qvar_8
Table 125. AH_QVAR_OUT register description
AH_Qvar_[15:0]
When the analog hub or Qvar is enabled (by setting the AH_QVAR_EN bit to 1 in CTRL7 (16h)), these
registers contain the analog hub or the Qvar sensor ouput data.
Data are expressed in two's complement.
UI_OUTZ_L_A_OIS_DualC (38h) and UI_OUTZ_H_A_OIS_DualC (39h)
9.43 TIMESTAMP0 (40h), TIMESTAMP1 (41h), TIMESTAMP2 (42h), and TIMESTAMP3
(43h)
Timestamp first data output register (R). The value is expressed as a 32-bit word and the bit resolution is 21.75 μs
(typical).
Table 126. TIMESTAMP output registers
D31 D30 D29 D28 D27 D26 D25 D24
D23 D22 D21 D20 D19 D18 D17 D16
D15 D14 D13 D12 D11 D10 D9 D8
D7 D6 D5 D4 D3 D2 D1 D0
Table 127. TIMESTAMP output register description
D[31:0] Timestamp output registers: 1LSB = 21.75 μs (typical)
9.44 UI_STATUS_REG_OIS (44h)
Table 128. UI_STATUS_REG_OIS register
0 0 0 0 0
GYRO_
SETTLING
GDA_OIS XLDA_OIS
Table 129. UI_STATUS_REG_OIS register description
GYRO_SETTLING High when the gyroscope output is in the settling phase
GDA_OIS
Gyroscope OIS data available (reset when one of the high parts of the output data is read).
Default value: 0
(0: no set of data available at gyroscope OIS output;
1: a new set of data is available at gyroscope output)
XLDA_OIS
Accelerometer OIS data available (reset when one of the high parts of the output data is read).
Default value: 0
(0: no set of data available at gyroscope OIS output;
1: a new set of data is available at gyroscope output)
TIMESTAMP0 (40h), TIMESTAMP1 (41h), TIMESTAMP2 (42h),and TIMESTAMP3 (43h)
9.45 WAKE_UP_SRC (45h)
Wake-up interrupt source register (R)
Table 130. WAKE_UP_SRC register
0
SLEEP_
CHANGE_IA
FF_IA
SLEEP_
STATE
WU_IA X_WU Y_WU Z_WU
Table 131. WAKE_UP_SRC register description
SLEEP_CHANGE_IA
Detects change event in activity/inactivity status. Default value: 0
(0: change status not detected; 1: change status detected)
FF_IA
Free-fall event detection status. Default: 0
(0: free-fall event not detected; 1: free-fall event detected)
SLEEP_STATE
Sleep status bit. Default value: 0
(0: Activity status; 1: Inactivity status)
WU_IA
Wake-up event detection status. Default value: 0
(0: wake-up event not detected; 1: wake-up event detected.)
X_WU
Wake-up event detection status on X-axis. Default value: 0
(0: wake-up event on X-axis not detected; 1: wake-up event on X-axis detected)
Y_WU
Wake-up event detection status on Y-axis. Default value: 0
(0: wake-up event on Y-axis not detected; 1: wake-up event on Y-axis detected)
Z_WU
Wake-up event detection status on Z-axis. Default value: 0
(0: wake-up event on Z-axis not detected; 1: wake-up event on Z-axis detected)
WAKE_UP_SRC (45h)
9.46 TAP_SRC (46h)
Tap source register (R)
Table 132. TAP_SRC register
0 TAP_IA
SINGLE_
TAP
DOUBLE_
TAP
TAP_SIGN X_TAP Y_TAP Z_TAP
Table 133. TAP_SRC register description
TAP_IA
Tap event detection status. Default: 0
(0: tap event not detected; 1: tap event detected)
SINGLE_TAP
Single-tap event status. Default value: 0
(0: single tap event not detected; 1: single tap event detected)
DOUBLE_TAP
Double-tap event detection status. Default value: 0
(0: double-tap event not detected; 1: double-tap event detected.)
TAP_SIGN
Sign of acceleration detected by tap event. Default: 0
(0: positive sign of acceleration detected by tap event;
1: negative sign of acceleration detected by tap event)
X_TAP
Tap event detection status on X-axis. Default value: 0
(0: tap event on X-axis not detected; 1: tap event on X-axis detected)
Y_TAP
Tap event detection status on Y-axis. Default value: 0
(0: tap event on Y-axis not detected; 1: tap event on Y-axis detected)
Z_TAP
Tap event detection status on Z-axis. Default value: 0
(0: tap event on Z-axis not detected; 1: tap event on Z-axis detected)
TAP_SRC (46h)
9.47 D6D_SRC (47h)
Portrait, landscape, face-up and face-down source register (R)
Table 134. D6D_SRC register
0 D6D_IA ZH ZL YH YL XH XL
Table 135. D6D_SRC register description
D6D_IA
Interrupt active for change position portrait, landscape, face-up, face-down. Default value: 0
(0: change position not detected; 1: change position detected)
ZH
Z-axis high event (over threshold). Default value: 0
(0: event not detected; 1: event (over threshold) detected)
ZL
Z-axis low event (under threshold). Default value: 0
(0: event not detected; 1: event (under threshold) detected)
YH
Y-axis high event (over threshold). Default value: 0
(0: event not detected; 1: event (over-threshold) detected)
YL
Y-axis low event (under threshold). Default value: 0
(0: event not detected; 1: event (under threshold) detected)
XH
X-axis high event (over threshold). Default value: 0
(0: event not detected; 1: event (over threshold) detected)
XL
X-axis low event (under threshold). Default value: 0
(0: event not detected; 1: event (under threshold) detected)
9.48 STATUS_MASTER_MAINPAGE (48h)
Sensor hub source register (R)
Table 136. STATUS_MASTER_MAINPAGE register
WR_ONCE_
DONE
SLAVE3_
NACK
SLAVE2_
NACK
SLAVE1_
NACK
SLAVE0_
NACK
0 0
SENS_HUB
_ENDOP
Table 137. STATUS_MASTER_MAINPAGE register description
WR_ONCE_DONE
When the bit WRITE_ONCE in MASTER_CONFIG (14h) is configured as 1, this bit is set to 1 when the
write operation on slave 0 has been performed and completed. Default value: 0
SLAVE3_NACK This bit is set to 1 if Not acknowledge occurs on slave 3 communication. Default value: 0
SLAVE2_NACK This bit is set to 1 if Not acknowledge occurs on slave 2 communication. Default value: 0
SLAVE1_NACK This bit is set to 1 if Not acknowledge occurs on slave 1 communication. Default value: 0
SLAVE0_NACK This bit is set to 1 if Not acknowledge occurs on slave 0 communication. Default value: 0
SENS_HUB_ENDOP
Sensor hub communication status. Default value: 0
(0: sensor hub communication not concluded;
1: sensor hub communication concluded)
D6D_SRC (47h)
9.49 EMB_FUNC_STATUS_MAINPAGE (49h)
Embedded function status register (R)
Table 138. EMB_FUNC_STATUS_MAINPAGE register
IS_FSM_LC 0
IS_
SIGMOT
IS_TILT
IS_
STEP_DET
0 0 0
Table 139. EMB_FUNC_STATUS_MAINPAGE register description
IS_FSM_LC
Interrupt status bit for FSM long counter timeout interrupt event.
(1: interrupt detected; 0: no interrupt)
IS_SIGMOT
Interrupt status bit for significant motion detection
(1: interrupt detected; 0: no interrupt)
IS_TILT
Interrupt status bit for tilt detection
(1: interrupt detected; 0: no interrupt)
IS_STEP_DET
Interrupt status bit for step detection
(1: interrupt detected; 0: no interrupt)
9.50 FSM_STATUS_MAINPAGE (4Ah)
Finite state machine status register (R)
Table 140. FSM_STATUS_MAINPAGE register
IS_FSM8 IS_FSM7 IS_FSM6 IS_FSM5 IS_FSM4 IS_FSM3 IS_FSM2 IS_FSM1
Table 141. FSM_STATUS_MAINPAGE register description
IS_FSM8 Interrupt status bit for FSM8 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM7 Interrupt status bit for FSM7 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM6 Interrupt status bit for FSM6 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM5 Interrupt status bit for FSM5 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM4 Interrupt status bit for FSM4 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM3 Interrupt status bit for FSM3 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM2 Interrupt status bit for FSM2 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM1 Interrupt status bit for FSM1 interrupt event. (1: interrupt detected; 0: no interrupt)
EMB_FUNC_STATUS_MAINPAGE (49h)
9.51 MLC_STATUS_MAINPAGE (4Bh)
Machine learning core status register (R)
Table 142. MLC_STATUS _MAINPAGE register
0 0 0 0 IS_MLC4 IS_MLC3 IS_MLC2 IS_MLC1
Table 143. MLC_STATUS_MAINPAGE register description
IS_MLC4 Interrupt status bit for MLC4 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_MLC3 Interrupt status bit for MLC3 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_MLC2 Interrupt status bit for MLC2 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_MLC1 Interrupt status bit for MLC1 interrupt event. (1: interrupt detected; 0: no interrupt)
9.52 INTERNAL_FREQ_FINE (4Fh)
Internal frequency register (R)
Table 144. INTERNAL_FREQ_FINE register
FREQ_
FINE_7
FREQ_
FINE_6
FREQ_
FINE_5
FREQ_
FINE_4
FREQ_
FINE_3
FREQ_
FINE_2
FREQ_
FINE_1
FREQ_
FINE_0
Table 145. INTERNAL_FREQ_FINE register description
FREQ_FINE_[7:0] Difference in percentage of the effective ODR (and timestamp rate) with respect to the typical.
Step: 0.13%. 8-bit format, two's complement.
The actual timestamp resolution and the actual output data rate can be calculated using the following formulas:
tactuals=^1
46080 ⋅1+0.0013⋅FREQ_FINE
ODRactualHz=^7680 ⋅ 1+0.0013ODR ⋅FREQ_FINE
coeff
Table 146. ODRcoeff values
Selected ODR [Hz] ODRcoeff
7.5 1024
15 512
30 256
60 128
120 64
240 32
480 16
960 8
1.92 kHz 4
3.84 kHz 2
7.68 kHz 1
MLC_STATUS_MAINPAGE (4Bh)
9.53 FUNCTIONS_ENABLE (50h)
Enable interrupt functions register (R/W)
Table 147. FUNCTIONS_ENABLE register
INTERRUPTS
_ENABLE
TIMESTAMP
_EN^0
(1) 0 (1) DIS_RST_LIR
_ALL_INT^0
(1) INACT_EN_1 INACT_EN_0
1. This bit must be set to 0 for the correct operation of the device.

Table 148. FUNCTIONS_ENABLE register description
INTERRUPTS_ENABLE
Enables basic interrupts (6D/4D, free-fall, wake-up, tap, activity/inactivity). Default value: 0
(0: interrupt disabled; 1: interrupt enabled)
TIMESTAMP_EN
Enables timestamp counter. The counter is readable in TIMESTAMP0 (40h), TIMESTAMP1 (41h),
TIMESTAMP2 (42h), and TIMESTAMP3 (43h). Default value: 0
(0: disabled; 1: enabled)
DIS_RST_LIR_ALL_INT
When this bit is set to 1, reading the ALL_INT_SRC (1Dh) register does not reset the latched
interrupt signals. This can be useful in order to not reset some status flags before reading the
corresponding status register. Default value: 0
(0: disabled; 1: enabled)
INACT_EN_[1:0]
Enables activity/inactivity (sleep) function. Default value: 00
(00: stationary/motion-only interrupts generated, accelerometer and gyroscope configuration do not
change;
01: sets accelerometer to low-power mode 1 with accelerometer ODR selected through the
XL_INACT_ODR_[1:0] bits of the INACTIVITY_DUR (54h) register, gyroscope configuration does
not change;
10: sets accelerometer to low-power mode 1 with accelerometer ODR selected through the
XL_INACT_ODR_[1:0] bits of the INACTIVITY_DUR (54h) register, gyroscope in sleep mode;
11: sets accelerometer to low-power mode 1 with accelerometer ODR selected through the
XL_INACT_ODR_[1:0] bits of the INACTIVITY_DUR (54h) register, gyroscope in power-down
mode)
FUNCTIONS_ENABLE (50h)
9.54 DEN (51h)
DEN configuration register (R/W)
Table 149. DEN register
0 (1) LVL1_EN LVL2_EN DEN_XL_EN DEN_X DEN_Y DEN_Z DEN_XL_G
1. This bit must be set to 0 for the correct operation of the device.

Table 150. DEN register description
LVL1_EN Enables DEN data level-sensitive trigger. Refer to Table 151.
LVL2_EN Enables DEN level-sensitive latched. Refer to Table 151.
DEN_XL_EN
Extends DEN functionality to accelerometer sensor. Default value: 0
(0: disabled; 1: enabled)
DEN_X
DEN value stored in LSB of X-axis. Default value: 1
(0: DEN not stored in X-axis LSB; 1: DEN stored in X-axis LSB)
DEN_Y
DEN value stored in LSB of Y-axis. Default value: 1
(0: DEN not stored in Y-axis LSB; 1: DEN stored in Y-axis LSB)
DEN_Z
DEN value stored in LSB of Z-axis. Default value: 1
(0: DEN not stored in Z-axis LSB; 1: DEN stored in Z-axis LSB)
DEN_XL_G
DEN stamping sensor selection. Default value: 0
(0: DEN pin info stamped in the gyroscope axis selected by bits DEN_X, DEN_Y, DEN_Z;
1: DEN pin info stamped in the accelerometer axis selected by bits DEN_X, DEN_Y, DEN_Z)
Table 151. Trigger mode selection
LVL1_EN, LVL2_EN Trigger mode
10 Level-sensitive trigger mode is selected
11 Level-sensitive latched mode is selected
DEN (51h)
9.55 INACTIVITY_DUR (54h)
Activity/inactivity configuration register (R/W)
Table 152. INACTIVITY_DUR register
SLEEP_STATUS
_ON_INT
WU_INACT_
THS_W_2
WU_INACT_
THS_W_1
WU_INACT_
THS_W_0
XL_INACT
_ODR_1
XL_INACT
_ODR_0
INACT
_DUR_1
INACT
_DUR_0
Table 153. INACTIVITY_DUR register description
SLEEP_STATUS_ON_INT
Activity/inactivity interrupt mode configuration.
If the INT1_SLEEP_CHANGE or INT2_SLEEP_CHANGE bit is enabled, drives the sleep status
or sleep change on the INT pin. Default value: 0
(0: sleep change notification on INT pin;
1: sleep status reported on INT pin)
WU_INACT_THS_W_[2:0]
Weight of 1 LSB of wake-up (WU_THS) and activity/inactivity (INACT_THS) threshold.
(000: 7.8125 m g /LSB (default);
001: 15.625 m g /LSB;
010: 31.25 m g /LSB;
011: 62.5 m g /LSB;
100: 125 m g /LSB;
101 - 110 - 111: 250 m g /LSB)
XL_INACT_ODR_[1:0]
Selects the ODR_XL target during inactivity.
(00: 1.875 Hz;
01: 15 Hz (default);
10: 30 Hz;
11: 60 Hz)
INACT_DUR_[1:0]
Duration in the transition from stationary to motion (from inactivity to activity).
(00: transition to motion (activity) immediately at first overthreshold event (default);
01: transition to motion (activity) after two consecutive overthreshold events;
10: transition to motion (activity) after three consecutive overthreshold events;
11: transition to motion (activity) after four consecutive overthreshold events)
9.56 INACTIVITY_THS (55h)
Activity/inactivity threshold setting register (R/W)
Table 154. INACTIVITY_THS register
0 (1) 0 (1)
INACT_
THS_5
INACT_
THS_4
INACT_
THS_3
INACT_
THS_2
INACT_
THS_1
INACT_
THS_0
1. This bit must be set to 0 for the correct operation of the device.

Table 155. INACTIVITY_THS register description
INACT_THS_[5:0] Activity/inactivity threshold. The resolution of the threshold depends on the value of
WU_INACT_THS_W_[2:0] in the INACTIVITY_DUR (54h) register. Default value: 000000
INACTIVITY_DUR (54h)
9.57 TAP_CFG0 (56h)
Tap configuration register 0 (R/W)
Table 156. TAP_CFG0 register
0 (1) LOW_PASS_ON_6D HW_FUNC_MASK_XL_SETTL SLOPE_FDS TAP_X_EN TAP_Y_EN TAP_Z_EN LIR
1. This bit must be set to 0 for the correct operation of the device.

Table 157. TAP_CFG0 register description
LOW_PASS_ON_6D
LPF2 filter on 6D function selection. Refer to Figure 32. Default value: 0
(0: ODR/2 low-pass filtered data sent to 6D interrupt function;
1: LPF2 output data sent to 6D interrupt function)
HW_FUNC_MASK_XL_SETTL
Enables masking the execution trigger of the basic interrupt functions (6D/4D, free-fall, wake-
up, tap, activity/inactivity) when accelerometer data are settling. Default value: 0
(0: disabled; 1: enabled)
Note: Refer to the product application note for the details regarding operating/power mode
configurations, settings, turn-on/off time and on-the-fly changes.
SLOPE_FDS
HPF or slope filter selection on wake-up and activity/inactivity functions. Refer to Figure 32.
Default value: 0
(0: slope filter applied; 1: HPF applied)
TAP_X_EN
Enables X direction in tap recognition. Default value: 0
(0: X direction disabled; 1: X direction enabled)
TAP_Y_EN
Enables Y direction in tap recognition. Default value: 0
(0: Y direction disabled; 1: Y direction enabled)
TAP_Z_EN
Enables Z direction in tap recognition. Default value: 0
(0: Z direction disabled; 1: Z direction enabled)
LIR
Latched interrupt. Default value: 0
(0: interrupt request not latched; 1: interrupt request latched)
TAP_CFG0 (56h)
9.58 TAP_CFG1 (57h)
Tap configuration register 1 (R/W)
Table 158. TAP_CFG1 register
TAP_
PRIORITY_2
TAP_
PRIORITY_1
TAP_
PRIORITY_0
TAP_
THS_X_4
TAP_
THS_X_3
TAP_
THS_X_2
TAP_
THS_X_1
TAP_
THS_X_0
Table 159. TAP_CFG1 register description
TAP_PRIORITY_[2:0] Selection of axis priority for tap detection (see Table 160)
TAP_THS_X_[4:0]
X-axis tap recognition threshold. Default value: 0
1 LSB = FS_XL / (2^5 )
Table 160. TAP priority decoding
TAP_PRIORITY_[2:0] Max. priority Mid. priority Min. priority
000 X Y Z
001 Y X Z
010 X Z Y
011 Z Y X
100 X Y Z
101 Y Z X
110 Z X Y
111 Z Y X
9.59 TAP_CFG2 (58h)
Tap configuration register 2 (R/W)
Table 161. TAP_CFG2 register
0 (1) 0 (1) 0 (1)
TAP_
THS_Y_4
TAP_
THS_Y_3
TAP_
THS_Y_2
TAP_
THS_Y_1
TAP_
THS_Y_0
1. This bit must be set to 0 for the correct operation of the device.

Table 162. TAP_CFG2 register description
TAP_THS_Y_[4:0]
Y-axis tap recognition threshold. Default value: 0
1 LSB = FS_XL / (2^5 )
TAP_CFG1 (57h)
9.60 TAP_THS_6D (59h)
Portrait/landscape position and tap function threshold register (R/W)
Table 163. TAP_THS_6D register
D4D_EN SIXD_THS_1 SIXD_THS_0
TAP_
THS_Z_4
TAP_
THS_Z_3
TAP_
THS_Z_2
TAP_
THS_Z_1
TAP_
THS_Z_0
Table 164. TAP_THS_6D register description
D4D_EN
Enables 4D orientation detection. Z-axis position detection is disabled. Default value: 0
(0: disabled; 1: enabled)
SIXD_THS_[1:0]
Threshold for 4D/6D function. Default value: 00
For details, refer to Table 165.
TAP_THS_Z_[4:0]
Z-axis recognition threshold. Default value: 0
1 LSB = FS_XL / (2^5 )
Table 165. Threshold for D4D/D6D function
SIXD_THS_[1:0] Threshold value
00 80 degrees
01 70 degrees
10 60 degrees
11 50 degrees
TAP_THS_6D (59h)
9.61 TAP_DUR (5Ah)
Tap recognition function setting register (R/W)
Table 166. TAP_DUR register
DUR_3 DUR_2 DUR_1 DUR_0 QUIET_1 QUIET_0 SHOCK_1 SHOCK_0
Table 167. TAP_DUR register description
DUR_[3:0]
Duration of maximum time gap for double-tap recognition. Default: 0000
When double-tap recognition is enabled, this register expresses the maximum time between two consecutive
detected taps to determine a double-tap event. The default value of these bits is 0000b which corresponds to
16/ODR_XL time. If the DUR_[3:0] bits are set to a different value, 1LSB corresponds to 32/ODR_XL time.
QUIET_[1:0]
Expected quiet time after a tap detection. Default value: 00
Quiet time is the time after the first detected tap in which there must not be any overthreshold event. The
default value of these bits is 00b which corresponds to 2/ODR_XL time. If the QUIET_[1:0] bits are set to a
different value, 1LSB corresponds to 4/ODR_XL time.
SHOCK_[1:0]
Maximum duration of overthreshold event. Default value: 00
Maximum duration is the maximum time of an overthreshold signal detection to be recognized as a tap event.
The default value of these bits is 00b which corresponds to 4/ODR_XL time. If the SHOCK_[1:0] bits are set to
a different value, 1LSB corresponds to 8/ODR_XL time.
9.62 WAKE_UP_THS (5Bh)
Single/double-tap selection and wake-up configuration (R/W)
Table 168. WAKE_UP_THS register
SINGLE_
DOUBLE_TAP
USR_OFF
_ON_WU
WK_THS_5 WK_THS_4 WK_THS_3 WK_THS_2 WK_THS_1 WK_THS_0
Table 169. WAKE_UP_THS register description
SINGLE_DOUBLE_TAP
Enables single/double-tap event. Default value: 0
(0: only single-tap event enabled;
1: both single and double-tap events enabled)
USR_OFF_ON_WU
Drives the low-pass filtered data with user offset correction (instead of high-pass filtered data) to the
wake-up and the activity/inactivity functions. Refer to Figure 32. Default value: 0
WK_THS_[5:0] Wake-up threshold. The resolution of the threshold depends on the value of
WU_INACT_THS_W_[2:0] in the INACTIVITY_DUR (54h) register. Default value: 000000
TAP_DUR (5Ah)
9.63 WAKE_UP_DUR (5Ch)
Free-fall, wake-up, and sleep mode functions duration setting register (R/W)
Table 170. WAKE_UP_DUR register
FF_DUR_5 WAKE_DUR_1 WAKE_DUR_0 0 (1) SLEEP_DUR_3 SLEEP_DUR_2 SLEEP_DUR_1 SLEEP_DUR_0
1. This bit must be set to 0 for the correct operation of the device.

Table 171. WAKE_UP_DUR register description
FF_DUR_5
Free-fall duration event. Default: 0
For the complete configuration of the free-fall duration, refer to FF_DUR_[4:0] in the FREE_FALL (5Dh)
configuration.
1 LSB = 1/ODR_XL time
WAKE_DUR_[1:0]
Wake-up duration event. Default: 00
1 LSB = 1/ODR_XL time
SLEEP_DUR_[3:0]
Duration to go in sleep mode. Default value: 0000 (this corresponds to 16 ODR)
1 LSB = 512/ODR_XL time
9.64 FREE_FALL (5Dh)
Free-fall function duration setting register (R/W)
Table 172. FREE_FALL register
FF_DUR_4 FF_DUR_3 FF_DUR_2 FF_DUR_1 FF_DUR_0 FF_THS_2 FF_THS_1 FF_THS_0
Table 173. FREE_FALL register description
FF_DUR_[4:0]
Free-fall duration event. Default: 00000
For the complete configuration of the free-fall duration, refer to FF_DUR_5 in the WAKE_UP_DUR (5Ch)
configuration.
FF_THS_[2:0]
Free-fall threshold setting. Default: 000
For details refer to Table 174.
Table 174. Threshold for free-fall function
FF_THS_[2:0] Threshold value
000 156 m g
001 219 m g
010 250 m g
011 312 m g
100 344 m g
101 406 m g
110 469 m g
111 500 m g
WAKE_UP_DUR (5Ch)
9.65 MD1_CFG (5Eh)
Functions routing to INT1 pin register (R/W). Each bit in this register enables a signal to be carried over the
INT1 pin. The output of the pin is the OR combination of the signals selected here and in the INT1_CTRL (0Dh)
register.
Table 175. MD1_CFG register
INT1_SLEEP_
CHANGE
INT1_
SINGLE_TAP
INT1_WU INT1_FF INT1_
DOUBLE_TAP
INT1_6D INT1_
EMB_FUNC
INT1_SHUB
Table 176. MD1_CFG register description
INT1_SLEEP_CHANGE(1)
Routing activity/inactivity recognition event to INT1. Default: 0
(0: routing activity/inactivity event to INT1 disabled;
1: routing activity/inactivity event to INT1 enabled)
INT1_SINGLE_TAP
Routing single-tap recognition event to INT1. Default: 0
(0: routing single-tap event to INT1 disabled;
1: routing single-tap event to INT1 enabled)
INT1_WU
Routing wake-up event to INT1. Default value: 0
(0: routing wake-up event to INT1 disabled;
1: routing wake-up event to INT1 enabled)
INT1_FF
Routing free-fall event to INT1. Default value: 0
(0: routing free-fall event to INT1 disabled;
1: routing free-fall event to INT1 enabled)
INT1_DOUBLE_TAP
Routing tap event to INT1. Default value: 0
(0: routing double-tap event to INT1 disabled;
1: routing double-tap event to INT1 enabled)
INT1_6D
Routing 6D event to INT1. Default value: 0
(0: routing 6D event to INT1 disabled;
1: routing 6D event to INT1 enabled)
INT1_EMB_FUNC
Routing embedded functions event to INT1. Default value: 0
(0: routing embedded functions event to INT1 disabled;
1: routing embedded functions event to INT1 enabled)
INT1_SHUB
Routing sensor hub communication concluded event to INT1. Default value: 0
(0: routing sensor hub communication concluded event to INT1 disabled;
1: routing sensor hub communication concluded event to INT1 enabled)
1. Activity/inactivity interrupt mode (sleep change or sleep status) depends on the SLEEP_STATUS_ON_INT bit in the
INACTIVITY_DUR (54h) register.

MD1_CFG (5Eh)
9.66 MD2_CFG (5Fh)
Functions routing to INT2 pin register (R/W). Each bit in this register enables a signal to be carried over the
INT2 pin. The output of the pin is the OR combination of the signals selected here and in the INT2_CTRL (0Eh)
register.
Table 177. MD2_CFG register
INT2_SLEEP
_CHANGE
INT2_
SINGLE_TAP
INT2_WU INT2_FF INT2_
DOUBLE_TAP
INT2_6D INT2_
EMB_FUNC
INT2_
TIMESTAMP
Table 178. MD2_CFG register description
INT2_SLEEP_CHANGE(1)
Routing activity/inactivity recognition event to INT2. Default: 0
(0: routing activity/inactivity event to INT2 disabled;
1: routing activity/inactivity event to INT2 enabled)
INT2_SINGLE_TAP
Single-tap recognition routing to INT2. Default: 0
(0: routing single-tap event to INT2 disabled;
1: routing single-tap event to INT2 enabled)
INT2_WU
Routing wake-up event to INT2. Default value: 0
(0: routing wake-up event to INT2 disabled;
1: routing wake-up event to INT2 enabled)
INT2_FF
Routing free-fall event to INT2. Default value: 0
(0: routing free-fall event to INT2 disabled;
1: routing free-fall event to INT2 enabled)
INT2_DOUBLE_TAP
Routing tap event to INT2. Default value: 0
(0: routing double-tap event to INT2 disabled;
1: routing double-tap event to INT2 enabled)
INT2_6D
Routing 6D event to INT2. Default value: 0
(0: routing 6D event to INT2 disabled;
1: routing 6D event to INT2 enabled)
INT2_EMB_FUNC
Routing embedded functions event to INT2. Default value: 0
(0: routing embedded functions event to INT2 disabled;
1: routing embedded functions event to INT2 enabled)
INT2_TIMESTAMP Enables routing the alert for timestamp overflow within 5.6 ms to the INT2 pin.
1. Activity/inactivity interrupt mode (sleep change or sleep status) depends on the SLEEP_STATUS_ON_INT bit in the
INACTIVITY_DUR (54h) register.

9.67 HAODR_CFG (62h)
HAODR data rate configuration register (R/W)
Table 179. HAODR_CFG register
0 (1) 0 (1) 0 (1) 0 (1) 0 (1) 0 (1)
HAODR_
SEL_1
HAODR_
SEL _0
1. This bit must be set to 0 for the correct operation of the device.

Table 180. HAODR_CFG register description
HAODR_SEL_[1:0]
Selects the ODR set supported when high-accuracy ODR (HAODR) mode is enabled (see Table 20).
Default: 00
MD2_CFG (5Fh)
9.68 EMB_FUNC_CFG (63h)
Embedded functions configuration register (R/W)
Table 181. EMB_FUNC_CFG register
XL_DualC_BATCH
_FROM_IF^0
(1) EMB_FUNC_IRQ_
MASK_G_SETTL
EMB_FUNC_IRQ_
MASK_XL_SETTL
EMB_FUNC_
DISABLE^0
(1) 0 (1) 0 (1)
1. This bit must be set to 0 for the correct operation of the device.

Table 182. EMB_FUNC_CFG register description
XL_DualC_BATCH_FROM_IF
When dual-channel mode is enabled, this bit enables batching the accelerometer
channel 2 in FIFO. Default value: 0
(0: disabled; 1: enabled)
EMB_FUNC_IRQ_MASK_G_SETTL
Enables / masks execution trigger of the embedded functions when gyroscope data
are settling. Default value: 0
(0: disabled;
1: masks execution trigger of the embedded functions until gyroscope filter settling
ends)
Note: Refer to the product application note for the details regarding operating/power
mode configurations, settings, turn-on/off time and on-the-fly changes.
EMB_FUNC_IRQ_MASK_XL_SETTL
Enables / masks execution trigger of the embedded functions when accelerometer
data are settling. Default value: 0
(0: disabled;
1: masks execution trigger of the embedded functions until accelerometer filter settling
ends)
Note: Refer to the product application note for the details regarding operating/power
mode configurations, settings, turn-on/off time and on-the-fly changes.
EMB_FUNC_DISABLE
Disables execution of the embedded functions. Default value: 0
(0: disabled;
1: embedded functions execution trigger is not generated anymore and all initialization
procedures are forced when this bit is set back to 0).
9.69 UI_HANDSHAKE_CTRL (64h)
Control register (UI side) for UI / SPI2 shared registers (R/W)
Table 183. UI_HANDSHAKE_CTRL register
0 (1) 0 (1) 0 (1) 0 (1) 0 (1) 0 (1)
UI_SHARED
_ACK
UI_SHARED
_REQ
1. This bit must be set to 0 for the correct operation of the device.

Table 184. UI_HANDSHAKE_CTRL register description
UI_SHARED_ACK
Primary interface side. This bit acknowledges the handshake. If the secondary interface is not accessing
the shared registers, this bit is set to 1 by the device and the R/W operation on the UI_SPI2_SHARED_0
(65h) through UI_SPI2_SHARED_5 (6Ah) registers is allowed on the primary interface.
UI_SHARED_REQ
This bit is used by the primary interface master to request access to the UI_SPI2_SHARED_0 (65h)
through UI_SPI2_SHARED_5 (6Ah) registers. When the R/W operation is finished, the master must reset
this bit.
EMB_FUNC_CFG (63h)
9.70 UI_SPI2_SHARED_0 (65h)
UI / SPI2 shared register 0 (R/W)
Table 185. UI_SPI2_SHARED_0 register
D7 D6 D5 D4 D3 D2 D1 D0
Table 186. UI_SPI2_SHARED_0 register description
D[7:0]
Volatile byte is used as a contact point between the primary and secondary interface host. These shared
registers are accessible only by one interface at a time and access is managed through the UI_SHARED_ACK
and UI_SHARED_REQ bits of register UI_HANDSHAKE_CTRL (64h) and the SPI2_SHARED_ACK and
SPI2_SHARED_REQ bits of register SPI2_HANDSHAKE_CTRL (6Eh).
9.71 UI_SPI2_SHARED_1 (66h)
UI / SPI2 shared register 1 (R/W)
Table 187. UI_SPI2_SHARED_1 register
D7 D6 D5 D4 D3 D2 D1 D0
Table 188. UI_SPI2_SHARED_1 register description
D[7:0]
Volatile byte is used as a contact point between the primary and secondary interface host. These shared
registers are accessible only by one interface at a time and access is managed through the UI_SHARED_ACK
and UI_SHARED_REQ bits of register UI_HANDSHAKE_CTRL (64h) and the SPI2_SHARED_ACK and
SPI2_SHARED_REQ bits of register SPI2_HANDSHAKE_CTRL (6Eh).
9.72 UI_SPI2_SHARED_2 (67h)
UI / SPI2 shared register 2 (R/W)
Table 189. UI_SPI2_SHARED_2 register
D7 D6 D5 D4 D3 D2 D1 D0
Table 190. UI_SPI2_SHARED_2 register description
D[7:0]
Volatile byte is used as a contact point between the primary and secondary interface host. These shared
registers are accessible only by one interface at a time and access is managed through the UI_SHARED_ACK
and UI_SHARED_REQ bits of register UI_HANDSHAKE_CTRL (64h) and the SPI2_SHARED_ACK and
SPI2_SHARED_REQ bits of register SPI2_HANDSHAKE_CTRL (6Eh).
UI_SPI2_SHARED_0 (65h)
9.73 UI_SPI2_SHARED_3 (68h)
UI / SPI2 shared register 3 (R/W)
Table 191. UI_SPI2_SHARED_3 register
D7 D6 D5 D4 D3 D2 D1 D0
Table 192. UI_SPI2_SHARED_3 register description
D[7:0]
Volatile byte is used as a contact point between the primary and secondary interface host. These shared
registers are accessible only by one interface at a time and access is managed through the UI_SHARED_ACK
and UI_SHARED_REQ bits of register UI_HANDSHAKE_CTRL (64h) and the SPI2_SHARED_ACK and
SPI2_SHARED_REQ bits of register SPI2_HANDSHAKE_CTRL (6Eh).
9.74 UI_SPI2_SHARED_4 (69h)
UI / SPI2 shared register 4 (R/W)
Table 193. UI_SPI2_SHARED_4 register
D7 D6 D5 D4 D3 D2 D1 D0
Table 194. UI_SPI2_SHARED_4 register description
D[7:0]
Volatile byte is used as a contact point between the primary and secondary interface host. These shared
registers are accessible only by one interface at a time and access is managed through the UI_SHARED_ACK
and UI_SHARED_REQ bits of register UI_HANDSHAKE_CTRL (64h) and the SPI2_SHARED_ACK and
SPI2_SHARED_REQ bits of register SPI2_HANDSHAKE_CTRL (6Eh).
9.75 UI_SPI2_SHARED_5 (6Ah)
UI / SPI2 shared register 5 (R/W)
Table 195. UI_SPI2_SHARED_5 register
D7 D6 D5 D4 D3 D2 D1 D0
Table 196. UI_SPI2_SHARED_5 register description
D[7:0]
Volatile byte is used as a contact point between the primary and secondary interface host. These shared
registers are accessible only by one interface at a time and access is managed through the UI_SHARED_ACK
and UI_SHARED_REQ bits of register UI_HANDSHAKE_CTRL (64h) and the SPI2_SHARED_ACK and
SPI2_SHARED_REQ bits of register SPI2_HANDSHAKE_CTRL (6Eh).
UI_SPI2_SHARED_3 (68h)
9.76 CTRL_EIS (6Bh)
Gyroscope EIS channel control register (R/W)
Table 197. CTRL_EIS register
ODR_G_EIS_1 ODR_G_EIS_0 0 (1) LPF_G_EIS_BW G_EIS_ON_G_OIS_OUT_REG FS_G_EIS_2 FS_G_EIS_1 FS_G_EIS_0
1. This bit must be set to 0 for the correct operation of the device.

Table 198. CTRL_EIS register description
ODR_G_EIS_[1:0]
Enables and selects the ODR of the gyroscope EIS channel.
(00: EIS channel is off (default);
01: 1.92 kHz;
10: 960 Hz;
11: reserved)
LPF_G_EIS_BW Gyroscope digital LPF_EIS filter bandwidth selection. Refer to Table 199.
G_EIS_ON_G_OIS_OUT_REG
Enables routing gyroscope EIS output to OIS from UI output addresses (2Eh – 33h). When
this bit is set to 1, the gyroscope OIS data cannot be read from primary interface. Default
value: 0
(0: disabled; 1: enabled)
FS_G_EIS_[2:0]
Gyroscope full-scale selection for EIS channel. If the FS_G_[3:0] bits in CTRL6 (15h) are
equal to 1100 (±4000 dps), FS_G_EIS_[2:0] must be set to “100” in order to have ±4000 dps
full scale on both UI and EIS channels. If the FS_G_3 bit in register CTRL6 (15h) is equal to
0, the EIS channel full scale can be selected as follows:
(000: ±125 dps (default);
001: ±250 dps;
010: ±500 dps;
011: ±1000 dps;
100: ±2000 dps;
101: reserved;
110: reserved;
111: reserved)
Table 199. Gyroscope EIS chain digital LPF_EIS filter bandwidth selection
ODR_G_EIS_[1:0] Gyroscope EIS ODR [Hz] LPF_G_EIS_BW Cutoff [Hz] Phase @ 20 Hz [°]
01 1.92 kHz
0 153 Hz -13.5°
1 203 Hz -10.8°
10 960
0 148 Hz -15.4°
1 193 Hz -12.7°
CTRL_EIS (6Bh)
9.77 UI_INT_OIS (6Fh)
OIS interrupt configuration register
The primary interface can write to this register when the OIS_CTRL_FROM_UI bit in the FUNC_CFG_ACCESS
(01h) register is equal to 1 (primary IF full-control mode); this register is read-only when the
OIS_CTRL_FROM_UI bit is equal to 0 (SPI2 full-control mode) and shows the content of the SPI2_INT_OIS
(6Fh) register.
Table 200. UI_INT_OIS register
INT2_
DRDY_OIS
DRDY_
MASK_OIS^0
(1) ST_OIS_
CLAMPDIS^0
(1) 0 (1) 0 (1) 0 (1)
1. This bit must be set to 0 for the correct operation of the device.

Table 201. UI_INT_OIS register description
INT2_DRDY_OIS
Enables OIS chain DRDY on INT2 pin from the UI interface. This setting has priority over all other INT2
settings.
DRDY_MASK_OIS
Enables / masks OIS data available. Default value: 0
(0: disabled;
1: masks OIS DRDY signals (both accelerometer and gyroscope) until filter settling ends
(accelerometer and gyroscope independently masked))
ST_OIS_CLAMPDIS
Disables OIS chain clamp during self-test. Default value: 0
(0: All OIS chain outputs = 8000h during self-test;
1: OIS chain self-test outputs)
UI_INT_OIS (6Fh)
9.78 UI_CTRL1_OIS (70h)
OIS configuration register
The primary interface can write this register when the OIS_CTRL_FROM_UI bit in the FUNC_CFG_ACCESS
(01h) register is equal to 1 (primary IF full-control mode); this register is read-only when the
OIS_CTRL_FROM_UI bit is equal to 0 (SPI2 full-control mode) and shows the content of the SPI2_CTRL1_OIS
(70h) register.
Table 202. UI_CTRL1_OIS register
0 (1) 0 (1) SIM_OIS 0 (1) 0 (1)
OIS_
XL_EN
OIS_
G_EN
SPI2_READ
_EN
1. This bit must be set to 0 for the correct operation of the device.

Table 203. UI_CTRL1_OIS register description
SIM_OIS
SPI2 3- or 4-wire interface. Default value: 0
(0: 4-wire SPI2;
1: 3-wire SPI2)
OIS_XL_EN
Enables accelerometer OIS chain. Default value: 0
(0: accelerometer OIS chain disabled;
1: accelerometer OIS chain enabled)
OIS_G_EN
Enables gyroscope OIS chain. Default value: 0
(0: gyroscope OIS chain disabled;
1: gyroscope OIS chain enabled)
SPI2_READ_EN
In primary IF full-control mode, enables auxiliary SPI for reading OIS data
in registers SPI2_OUTX_L_G_OIS (22h) and SPI2_OUTX_H_G_OIS (23h) through
Section 11.9 SPI2_OUTZ_L_A_OIS (2Ch) and SPI2_OUTZ_H_A_OIS (2Dh). Default value: 0
(0: OIS data read from auxiliary SPI disabled;
1: OIS data read from auxiliary SPI enabled)
UI_CTRL1_OIS (70h)
9.79 UI_CTRL2_OIS (71h)
OIS configuration register
The primary interface can write this register when the OIS_CTRL_FROM_UI bit in the FUNC_CFG_ACCESS
(01h) register is equal to 1 (primary IF full-control mode); this register is read-only when the
OIS_CTRL_FROM_UI bit is equal to 0 (SPI2 full-control mode) and shows the content of the SPI2_CTRL2_OIS
(71h) register.
Table 204. UI_CTRL2_OIS register
0 (1) 0 (1) 0 (1)
LPF1_G_
OIS_BW_1
LPF1_G_
OIS_BW_0
FS_G
_OIS_2
FS_G
_OIS_1
FS_G
_OIS_0
1. This bit must be set to 0 for the correct operation of the device.

Table 205. UI_CTRL2_OIS register description
LPF1_G_OIS_BW_[1:0] Gyroscope OIS digital LPF1 filter bandwidth selection. Refer to Table 206.
FS_G_OIS_[2:0]
Gyroscope OIS full-scale selection:
(000: ±125 dps;
001: ±250 dps;
010: ±500 dps;
011: ±1000 dps;
100: ±2000 dps;
101: reserved;
110: reserved;
111: reserved)
Table 206. Gyroscope OIS chain digital LPF1 filter bandwidth selection
LPF1_G_OIS_BW_[1:0] Cutoff [Hz] Phase @ 20 Hz [°]
00 293 Hz -7.1°
01 217 Hz -9.1°
10 158 Hz -11.9°
11 476 Hz -5.1°
UI_CTRL2_OIS (71h)
9.80 UI_CTRL3_OIS (72h)
OIS configuration register
The primary interface can write this register when the OIS_CTRL_FROM_UI bit in the FUNC_CFG_ACCESS
(01h) register is equal to 1 (primary IF full-control mode); this register is read-only when the
OIS_CTRL_FROM_UI bit is equal to 0 (SPI2 full-control mode) and shows the content of the SPI2_CTRL3_OIS
(72h) register.
Table 207. UI_CTRL3_OIS register
0 (1) 0 (1)
LPF_XL_
OIS_BW_2
LPF_XL_
OIS_BW_1
LPF_XL_
OIS_BW_0^0
(1) FS_XL
_OIS_1
FS_XL
_OIS_0
1. This bit must be set to 0 for the correct operation of the device.

Table 208. UI_CTRL3_OIS register description
LPF_XL_OIS_BW_[2:0] Selects accelerometer OIS channel bandwidth, see Table 209. Default value: 0
FS_XL_OIS_[1:0]
Selects accelerometer OIS channel full-scale:
(00: ±2 g (default);
01: ±4 g ;
10: ±8 g ;
11: ±16 g )
Note: When the accelerometer full-scale value is selected only from the UI side it is readable also from the OIS side.

Table 209. Accelerometer OIS channel bandwidth and phase
LPF_XL_OIS_BW_[2:0] Typ. overall bandwidth [Hz] Typ. overall phase [°]
000 749 Hz -3.41 deg @ 20 Hz
001 539 Hz -4.04 deg@ 20 Hz
010 342 Hz -5.31 deg@ 20 Hz
011 162 Hz -9.08 deg@ 20 Hz
100 78.5 Hz -16.4 deg @ 20 Hz
101 38.6 Hz -29.6 deg@ 20 Hz
110 19.3 Hz -28.8 deg @ 10 Hz
111 9.8 Hz -29.1 deg @ 5 Hz
UI_CTRL3_OIS (72h)
9.81 X_OFS_USR (73h)
Accelerometer X-axis user offset correction (R/W). The offset value set in the X_OFS_USR offset register is
internally subtracted from the acceleration value measured on the X-axis.
Table 210. X_OFS_USR register
X_OFS_
USR_7
X_OFS_
USR_6
X_OFS_
USR_5
X_OFS_
USR_4
X_OFS_
USR_3
X_OFS_
USR_2
X_OFS_
USR_1
X_OFS_
USR_0
Table 211. X_OFS_USR register description
X_OFS_USR_[7:0]
Accelerometer X-axis user offset correction expressed in two’s complement, weight depends
on USR_OFF_W in CTRL9 (18h). The offset can be applied to the output registers (see
USR_OFF_ON_OUT bit in the CTRL9 (18h) register) or to the wake-up function input data (see
USR_OFF_ON_WU bit in the WAKE_UP_THS (5Bh) register).
The value must be in the range [-127 127].
9.82 Y_OFS_USR (74h)
Accelerometer Y-axis user offset correction (R/W). The offset value set in the Y_OFS_USR offset register is
internally subtracted from the acceleration value measured on the Y-axis.
Table 212. Y_OFS_USR register
Y_OFS_
USR_7
Y_OFS_
USR_6
Y_OFS_
USR_5
Y_OFS_
USR_4
Y_OFS_
USR_3
Y_OFS_
USR_2
Y_OFS_
USR_1
Y_OFS_
USR_0
Table 213. Y_OFS_USR register description
Y_OFS_USR_[7:0]
Accelerometer Y-axis user offset correction expressed in two’s complement, weight depends
on USR_OFF_W in CTRL9 (18h). The offset can be applied to the output registers (see
USR_OFF_ON_OUT bit in the CTRL9 (18h) register) or to the wake-up function input data (see
USR_OFF_ON_WU bit in the WAKE_UP_THS (5Bh) register).
The value must be in the range [-127 127].
9.83 Z_OFS_USR (75h)
Accelerometer Z-axis user offset correction (R/W). The offset value set in the Z_OFS_USR offset register is
internally subtracted from the acceleration value measured on the Z-axis.
Table 214. Z_OFS_USR register
Z_OFS_
USR_7
Z_OFS_
USR_6
Z_OFS_
USR_5
Z_OFS_
USR_4
Z_OFS_
USR_3
Z_OFS_
USR_2
Z_OFS_
USR_1
Z_OFS_
USR_0
Table 215. Z_OFS_USR register description
Z_OFS_USR_[7:0]
Accelerometer Z-axis user offset correction expressed in two’s complement, weight depends
on USR_OFF_W in CTRL9 (18h). The offset can be applied to the output registers (see
USR_OFF_ON_OUT bit in the CTRL9 (18h) register) or to the wake-up function input data (see
USR_OFF_ON_WU bit in the WAKE_UP_THS (5Bh) register).
The value must be in the range [-127 127].
X_OFS_USR (73h)
9.84 FIFO_DATA_OUT_TAG (78h)
FIFO tag register (R)
Table 216. FIFO_DATA_OUT_TAG register
TAG_
SENSOR_4
TAG_
SENSOR_3
TAG_
SENSOR_2
TAG_
SENSOR_1
TAG_
SENSOR_0
TAG_CNT_1 TAG_CNT_0 -
Table 217. FIFO_DATA_OUT_TAG register description
TAG_SENSOR_[4:0]
FIFO tag. Identifies the sensor in:
FIFO_DATA_OUT_X_L (79h) and FIFO_DATA_OUT_X_H (7Ah), FIFO_DATA_OUT_Y_L (7Bh) and
FIFO_DATA_OUT_Y_H (7Ch), and FIFO_DATA_OUT_Z_L (7Dh) and FIFO_DATA_OUT_Z_H (7Eh)
For details, refer to Table 218.
TAG_CNT_[1:0] 2-bit counter which identifies sensor time slot
Table 218. FIFO tag
TAG_SENSOR_[4:0] Sensor name
0x00 FIFO empty
0x01 Gyroscope NC
0x02 Accelerometer NC
0x03 Temperature
0x04 Timestamp
0x05 CFG_Change
0x06 Accelerometer NC_T_2
0x07 Accelerometer NC_T_1
0x08 Accelerometer 2xC
0x09 Accelerometer 3xC
0x0A Gyroscope NC_T_2
0x0B Gyroscope NC_T_1
0x0C Gyroscope 2xC
0x0D Gyroscope 3xC
0x0E Sensor hub slave 0
0x0F Sensor hub slave 1
0x10 Sensor hub slave 2
0x11 Sensor hub slave 3
0x12 Step counter
0x13 SFLP game rotation vector
0x16 SFLP gyroscope bias
0x17 SFLP gravity vector
0x19 Sensor hub nack
0x1A MLC result
0x1B MLC filter
0x1C MLC feature
0x1D Accelerometer dualC
0x1E Enhanced EIS gyroscope
FIFO_DATA_OUT_TAG (78h)
9.85 FIFO_DATA_OUT_X_L (79h) and FIFO_DATA_OUT_X_H (7Ah)
FIFO data output X (R)
Table 219. FIFO_DATA_OUT_X_H and FIFO_DATA_OUT_X_L registers
D15 D14 D13 D12 D11 D10 D9 D8
D7 D6 D5 D4 D3 D2 D1 D0
Table 220. FIFO_DATA_OUT_X_H and FIFO_DATA_OUT_X_L register description
D[15:0] FIFO X-axis output
9.86 FIFO_DATA_OUT_Y_L (7Bh) and FIFO_DATA_OUT_Y_H (7Ch)
FIFO data output Y (R)
Table 221. FIFO_DATA_OUT_Y_H and FIFO_DATA_OUT_Y_L registers
D15 D14 D13 D12 D11 D10 D9 D8
D7 D6 D5 D4 D3 D2 D1 D0
Table 222. FIFO_DATA_OUT_Y_H and FIFO_DATA_OUT_Y_L register description
D[15:0] FIFO Y-axis output
9.87 FIFO_DATA_OUT_Z_L (7Dh) and FIFO_DATA_OUT_Z_H (7Eh)
FIFO data output Z (R)
Table 223. FIFO_DATA_OUT_Z_H and FIFO_DATA_OUT_Z_L registers
D15 D14 D13 D12 D11 D10 D9 D8
D7 D6 D5 D4 D3 D2 D1 D0
Table 224. FIFO_DATA_OUT_Z_H and FIFO_DATA_OUT_Z_L register description
D[15:0] FIFO Z-axis output
FIFO_DATA_OUT_X_L (79h) and FIFO_DATA_OUT_X_H (7Ah)
10 SPI2 register mapping
The table given below provides a list of the 8/16-bit registers embedded in the device and the corresponding
addresses.
All these registers are accessible from auxiliary SPI interface only.
Table 225. SPI2 register address map
Name Type
Register address
Default Comment
Hex Binary
SPI2_WHO_AM_I R 0F 00001111 01110000
SPI2_STATUS_REG_OIS R 1E 00011110 output
SPI2_OUT_TEMP_L R 20 00100000 output
SPI2_OUT_TEMP_H R 21 00100001 output
SPI2_OUTX_L_G_OIS R 22 00100010 output
SPI2_OUTX_H_G_OIS R 23 00100011 output
SPI2_OUTY_L_G_OIS R 24 00100100 output
SPI2_OUTY_H_G_OIS R 25 00100101 output
SPI2_OUTZ_L_G_OIS R 26 00100110 output
SPI2_OUTZ_H_G_OIS R 27 00100111 output
SPI2_OUTX_L_A_OIS R 28 00101000 output
SPI2_OUTX_H_A_OIS R 29 00101001 output
SPI2_OUTY_L_A_OIS R 2A 00101010 output
SPI2_OUTY_H_A_OIS R 2B 00101011 output
SPI2_OUTZ_L_A_OIS R 2C 00101100 output
SPI2_OUTZ_H_A_OIS R 2D 00101101 output
SPI2_HANDSHAKE_CTRL R/W 6E 01101110 00000000
SPI2_INT_OIS
R/W (SPI2 full-control mode)
R (primary IF full-control mode)
6F 01101111 00000000
SPI2_CTRL1_OIS
R/W (SPI2 full-control mode)
R (primary IF full-control mode)
70 01110000 00000000
SPI2_CTRL2_OIS
R/W (SPI2 full-control mode)
R (primary IF full-control mode)
71 01110001 00000000
SPI2_CTRL3_OIS
R/W (SPI2 full-control mode)
R (primary IF full-control mode)
72 01110010 00000000
Reserved registers must not be changed. Writing to those registers may cause permanent damage to the device.
The content of the registers that are loaded at boot should not be changed. They contain the factory calibration
values. Their content is automatically restored when the device is powered up.
SPI2 register mapping
11 SPI2 register description
11.1 SPI2_WHO_AM_I (0Fh)
WHO_AM_I register (R). This is a read-only register. Its value is fixed at 70h.
Table 226. SPI2_WhoAmI register
0 1 1 1 0 0 0 0
11.2 SPI2_STATUS_REG_OIS (1Eh)
The SPI2_STATUS_REG_OIS register is read by the auxiliary SPI (R).
Table 227. SPI2_STATUS_REG_OIS register
0 0 0 0 0
GYRO_
SETTLING
GDA XLDA
Table 228. SPI2_STATUS_REG_OIS description
GYRO_SETTLING High when the gyroscope output is in the settling phase
GDA Gyroscope data available (reset when one of the high parts of the output data is read)
XLDA Accelerometer data available (reset when one of the high parts of the output data is read)
11.3 SPI2_OUT_TEMP_L (20h) and SPI2_OUT_TEMP_H (21h)
Temperature data output register (R). L and H registers together express a 16-bit word in two’s complement.
Table 229. SPI2_OUT_TEMP_L register
Temp7 Temp6 Temp5 Temp4 Temp3 Temp2 Temp1 Temp0
Table 230. SPI2_OUT_TEMP_H register
Temp15 Temp14 Temp13 Temp12 Temp11 Temp10 Temp9 Temp8
Table 231. SPI2_OUT_TEMP register description
Temp[15:0]
Temperature sensor output data
The value is expressed as two’s complement sign extended on the MSB.
SPI2 register description
11.4 SPI2_OUTX_L_G_OIS (22h) and SPI2_OUTX_H_G_OIS (23h)
Angular rate sensor pitch axis (X) angular rate output register (R). The value is expressed as a 16-bit word in
two’s complement.
Data are according to the gyroscope full-scale and ODR (7.68 kHz) settings of the OIS gyroscope.
Table 232. SPI2_OUTX_L_G_OIS register
D7 D6 D5 D4 D3 D2 D1 D0
Table 233. SPI2_OUTX_H_G_OIS register
D15 D14 D13 D12 D11 D10 D9 D8
Table 234. SPI2_OUTX_H_G_OIS register description
D[15:0] Gyroscope OIS chain pitch axis (X) angular rate output value
11.5 SPI2_OUTY_L_G_OIS (24h) and SPI2_OUTY_H_G_OIS (25h)
Angular rate sensor roll axis (Y) angular rate output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the gyroscope full-scale and ODR (7.68 kHz) settings of the OIS gyroscope.
Table 235. SPI2_OUTY_L_G_OIS register
D7 D6 D5 D4 D3 D2 D1 D0
Table 236. SPI2_OUTY_H_G_OIS register
D15 D14 D13 D12 D11 D10 D9 D8
Table 237. SPI2_OUTY_H_G_OIS register description
D[15:0] Gyroscope OIS chain roll axis (Y) angular rate output value
SPI2_OUTX_L_G_OIS (22h) and SPI2_OUTX_H_G_OIS (23h)
11.6 SPI2_OUTZ_L_G_OIS (26h) and SPI2_OUTZ_H_G_OIS (27h)
Angular rate sensor yaw axis (Z) angular rate output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the gyroscope full-scale and ODR (7.68 kHz) settings of the OIS gyroscope.
Table 238. SPI2_OUTZ_L_G_OIS register
D7 D6 D5 D4 D3 D2 D1 D0
Table 239. SPI2_OUTZ_H_G_OIS register
D15 D14 D13 D12 D11 D10 D9 D8
Table 240. SPI2_OUTZ_H_G_OIS register description
D[15:0] Gyroscope OIS chain yaw axis (Z) angular rate output value
11.7 SPI2_OUTX_L_A_OIS (28h) and SPI2_OUTX_H_A_OIS (29h)
Linear acceleration sensor X-axis output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the accelerometer full scale and ODR (7.68 kHz) settings of the OIS accelerometer.
Table 241. SPI2_OUTX_L_A_OIS register
D7 D6 D5 D4 D3 D2 D1 D0
Table 242. SPI2_OUTX_H_A_OIS register
D15 D14 D13 D12 D11 D10 D9 D8
Table 243. SPI2_OUTX_H_A_OIS register description
D[15:0] Accelerometer OIS chain X-axis linear acceleration output value
SPI2_OUTZ_L_G_OIS (26h) and SPI2_OUTZ_H_G_OIS (27h)
11.8 SPI2_OUTY_L_A_OIS (2Ah) and SPI2_OUTY_H_A_OIS (2Bh)
Linear acceleration sensor Y-axis output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the accelerometer full scale and ODR (7.68 kHz) settings of the OIS accelerometer.
Table 244. SPI2_OUTY_L_A_OIS register
D7 D6 D5 D4 D3 D2 D1 D0
Table 245. SPI2_OUTY_H_A_OIS register
D15 D14 D13 D12 D11 D10 D9 D8
Table 246. SPI2_OUTY_H_A_OIS register description
D[15:0] Accelerometer OIS chain Y-axis linear acceleration output value
11.9 SPI2_OUTZ_L_A_OIS (2Ch) and SPI2_OUTZ_H_A_OIS (2Dh)
Linear acceleration sensor Z-axis output register (R). The value is expressed as a 16-bit word in two’s
complement.
Data are according to the accelerometer full scale and ODR (7.68 kHz) settings of the OIS accelerometer.
Table 247. SPI2_OUTZ_L_A_OIS register
D7 D6 D5 D4 D3 D2 D1 D0
Table 248. SPI2_OUTZ_H_A_OIS register
D15 D14 D13 D12 D11 D10 D9 D8
Table 249. SPI2_OUTZ_H_A_OIS register description
D[15:0] Accelerometer OIS chain Z-axis linear acceleration output value
11.10 SPI2_HANDSHAKE_CTRL (6Eh)
Control register (SPI2 side) for UI / SPI2 shared registers (R/W)
Table 250. SPI2_HANDSHAKE_CTRL register
0 (1) 0 (1) 0 (1) 0 (1) 0 (1) 0 (1)
SPI2_
SHARED_REQ
SPI2_
SHARED_ACK
1. This bit must be set to 0 for the correct operation of the device.

Table 251. SPI2_HANDSHAKE_CTRL register description
SPI2_SHARED_REQ
This bit is used by the auxiliary SPI (SPI2) interface master to request access to the
UI_SPI2_SHARED_0 (65h) through UI_SPI2_SHARED_5 (6Ah) registers. When the R/W operation
is finished, the master must reset this bit.
SPI2_SHARED_ACK
Auxiliary SPI (SPI2) interface side. This bit acknowledges the handshake. If the primary interface is
not accessing the shared registers, this bit is set to 1 by the device and the R/W operation on the
UI_SPI2_SHARED_0 (65h) through UI_SPI2_SHARED_5 (6Ah) registers is allowed on the auxiliary
SPI interface.
SPI2_OUTY_L_A_OIS (2Ah) and SPI2_OUTY_H_A_OIS (2Bh)
11.11 SPI2_INT_OIS (6Fh)
OIS interrupt configuration register and self-test setting
The auxiliary SPI interface can write this register when the OIS_CTRL_FROM_UI bit in the
FUNC_CFG_ACCESS (01h) register is equal to 0 (SPI2 full-control mode); this register is read-only when the
OIS_CTRL_FROM_UI bit is equal to 1 (primary IF full-control mode) and shows the content of the UI_INT_OIS
(6Fh) register.
Table 252. SPI2_INT_OIS register
INT2_
DRDY_OIS
DRDY_MASK
_OIS^0
(1) ST_OIS_
CLAMPDIS
ST_G_
OIS_1
ST_G_
OIS_0
ST_XL_
OIS_1
ST_XL_
OIS_0
1. This bit must be set to 0 for the correct operation of the device.

Table 253. SPI2_INT_OIS register description
INT2_DRDY_OIS Enables OIS chain DRDY on INT2 pin. This setting has priority over all other INT2 settings.
DRDY_MASK_OIS
Enables / masks OIS data available. Default value: 0
(0: disabled;
1: masks OIS DRDY on pin (both accelerometer and gyroscope) until filter settling ends (accelerometer
and gyroscope independently masked))
ST_OIS_CLAMPDIS
Disables OIS chain clamp during self-test. Default value: 0
(0: All OIS chain outputs = 8000h during self-test;
1: OIS chain self-test outputs)
ST_G_OIS_[1:0]
Gyroscope OIS chain self-test selection when the self-test is enabled and ST_OIS_CLAMPDIS = 0.
(00: normal mode (default);
01: positive sign self-test;
10: normal mode;
11: negative sign self-test)
ST_XL_OIS_[1:0]
Accelerometer OIS chain self-test selection; activated only if the accelerometer OIS chain is enabled.
(00: normal mode (default);
01: positive sign self-test;
10: negative sign self-test;
11: reserved)
SPI2_INT_OIS (6Fh)
11.12 SPI2_CTRL1_OIS (70h)
OIS configuration register
The auxiliary SPI interface can write this register when the OIS_CTRL_FROM_UI bit in the
FUNC_CFG_ACCESS (01h) register is equal to 0 (SPI2 full-control mode); this register is read-only when
the OIS_CTRL_FROM_UI bit is equal to 1 (primary IF full-control mode) and shows the content of the
UI_CTRL1_OIS (70h) register.
Table 254. SPI2_CTRL1_OIS register
0 (1) 0 (1) SIM_OIS 0 (1) 0 (1)
OIS_
XL_EN
OIS_
G_EN
SPI2_READ
_EN
1. This bit must be set to 0 for the correct operation of the device.

Table 255. SPI2_CTRL1_OIS register description
SIM_OIS
SPI2 3- or 4-wire interface. Default value: 0
(0: 4-wire SPI2;
1: 3-wire SPI2)
OIS_XL_EN
Enables accelerometer OIS chain. Default value: 0
(0: accelerometer OIS chain disabled;
1: accelerometer OIS chain enabled)
OIS_G_EN
Enables gyroscope OIS chain. Default value: 0
(0: gyroscope OIS chain disabled;
1: gyroscope OIS chain enabled)
SPI2_READ_EN
In auxiliary SPI full-control mode, enables auxiliary SPI for reading OIS data
in registers SPI2_OUTX_L_G_OIS (22h) and SPI2_OUTX_H_G_OIS (23h) through
Section 11.9 SPI2_OUTZ_L_A_OIS (2Ch) and SPI2_OUTZ_H_A_OIS (2Dh). Default value: 0
(0: OIS data read from auxiliary SPI disabled;
1: OIS data read from auxiliary SPI enabled)
SPI2_CTRL1_OIS (70h)
11.13 SPI2_CTRL2_OIS (71h)
OIS configuration register
The auxiliary SPI interface can write this register when the OIS_CTRL_FROM_UI bit in the
FUNC_CFG_ACCESS (01h) register is equal to 0 (SPI2 full-control mode); this register is read-only when
the OIS_CTRL_FROM_UI bit is equal to 1 (primary IF full-control mode) and shows the content of the
UI_CTRL2_OIS (71h) register.
Table 256. SPI2_CTRL2_OIS register
0 (1) 0 (1) 0 (1)
LPF1_G_
OIS_BW_1
LPF1_G_
OIS_BW_0
FS_G
_OIS_2
FS_G
_OIS_1
FS_G
_OIS_0
1. This bit must be set to 0 for the correct operation of the device.

Table 257. SPI2_CTRL2_OIS register description
LPF1_G_OIS_BW_[1:0] Gyroscope OIS digital LPF1 filter bandwidth selection. Refer to Table 258.
FS_G_OIS_[2:0]
Gyroscope OIS full-scale selection:
(000: ±125 dps;
001: ±250 dps;
010: ±500 dps;
011: ±1000 dps;
100: ±2000 dps;
101: reserved;
110: reserved;
111: reserved)
Table 258. Gyroscope OIS chain digital LPF1 filter bandwidth selection
LPF1_G_OIS_BW_[1:0] Cutoff [Hz] Phase @ 20 Hz [°]
00 293 Hz -7.1°
01 217 Hz -9.1°
10 158 Hz -11.9°
11 476 Hz -5.1°
SPI2_CTRL2_OIS (71h)
11.14 SPI2_CTRL3_OIS (72h)
OIS configuration register
The auxiliary SPI interface can write this register when the OIS_CTRL_FROM_UI bit in the
FUNC_CFG_ACCESS (01h) register is equal to 0 (SPI2 full-control mode); this register is read-only when
the OIS_CTRL_FROM_UI bit is equal to 1 (primary IF full-control mode) and shows the content of the
UI_CTRL3_OIS (72h) register.
Table 259. SPI2_CTRL3_OIS register
0 (1) 0 (1)
LPF_XL_
OIS_BW_2
LPF_XL_
OIS_BW_1
LPF_XL_
OIS_BW_0^0
(1) FS_XL
_OIS_1
FS_XL
_OIS_0
1. This bit must be set to 0 for the correct operation of the device.

Table 260. SPI2_CTRL3_OIS register description
LPF_XL_OIS_BW_[2:0] Selects accelerometer OIS channel bandwidth, see Table 261. Default value: 0
FS_XL_OIS_[1:0]
Selects accelerometer OIS channel full-scale:
(00: ±2 g (default);
01: ±4 g ;
10: ±8 g ;
11: ±16 g )
Note: When the accelerometer full-scale value is selected only from the UI side it is readable also from the OIS side.

Table 261. Accelerometer OIS channel bandwidth and phase
LPF_XL_OIS_BW_[2:0] Typ. overall bandwidth [Hz] Typ. overall phase [°]
000 749 Hz -3.41 deg @ 20 Hz
001 539 Hz -4.04 deg@ 20 Hz
010 342 Hz -5.31 deg@ 20 Hz
011 162 Hz -9.08 deg@ 20 Hz
100 78.5 Hz -16.4 deg @ 20 Hz
101 38.6 Hz -29.6 deg@ 20 Hz
110 19.3 Hz -28.8 deg @ 10 Hz
111 9.8 Hz -29.1 deg @ 5 Hz
SPI2_CTRL3_OIS (72h)
12 Embedded functions register mapping
The table given below provides a list of the registers for the embedded functions available in the device and the
corresponding addresses. Embedded functions registers are accessible when EMB_FUNC_REG_ACCESS is set
to 1 in FUNC_CFG_ACCESS (01h).
Table 262. Register address map - embedded functions
Name Type
Register address
Default Comment
Hex Binary
PAGE_SEL R/W 02 00000010 00000001
EMB_FUNC_EN_A R/W 04 00000100 00000000
EMB_FUNC_EN_B R/W 05 00000101 00000000
EMB_FUNC_EXEC_STATUS R 07 00000111 output
PAGE_ADDRESS R/W 08 00001000 00000000
PAGE_VALUE R/W 09 00001001 00000000
EMB_FUNC_INT1 R/W 0A 00001010 00000000
FSM_INT1 R/W 0B 00001011 00000000
RESERVED - 0C
MLC_INT1 R/W 0D 00001101 00000000
EMB_FUNC_INT2 R/W 0E 00001110 00000000
FSM_INT2 R/W 0F 00001111 00000000
RESERVED - 10
MLC_INT2 R/W 11 00010001 00000000
EMB_FUNC_STATUS R 12 00010010 output
FSM_STATUS R 13 00010011 output
RESERVED - 14
MLC_STATUS R 15 00010101 output
PAGE_RW R/W 17 00010111 00000000
RESERVED - 18-43
EMB_FUNC_FIFO_EN_A R/W 44 01000100 00000000
EMB_FUNC_FIFO_EN_B R/W 45 01000101
FSM_ENABLE R/W 46 01000110 00000000
RESERVED - 47
FSM_LONG_COUNTER_L R/W 48 01001000 00000000
FSM_LONG_COUNTER_H R/W 49 01001001 00000000
RESERVED - 4A
INT_ACK_MASK R/W 4B 01001011 00000000
FSM_OUTS1 R 4C 01001100 output
FSM_OUTS2 R 4D 01001101 output
FSM_OUTS3 R 4E 01001110 output
FSM_OUTS4 R 4F 01001111 output
FSM_OUTS5 R 50 01010000 output
FSM_OUTS6 R 51 01010001 output
Embedded functions register mapping
Name Type
Register address
Default Comment
Hex Binary
FSM_OUTS7 R 52 01010010 output
FSM_OUTS8 R 53 01010011 output
RESERVED - 54- 5D
SFLP_ODR R/W 5E 01011110 01011011
FSM_ODR R/W 5F 01011111 01001011
MLC_ODR R/W 60 01100000 00010101
STEP_COUNTER_L R 62 01100010 output
STEP_COUNTER_H R 63 01100011 output
EMB_FUNC_SRC R/W 64 01100100 output
EMB_FUNC_INIT_A R/W 66 01100110 00000000
EMB_FUNC_INIT_B R/W 67 01100111 00000000
MLC1_SRC R 70 01110000 output
MLC2_SRC R 71 01110001 output
MLC3_SRC R 72 01110010 output
MLC4_SRC R 73 01110011 output
Reserved registers must not be changed. Writing to those registers may cause permanent damage to the device.

The content of the registers that are loaded at boot should not be changed. They contain the factory calibration
values. Their content is automatically restored when the device is powered up.

Embedded functions register mapping
13 Embedded functions register description
13.1 PAGE_SEL (02h)
Enable advanced features dedicated page (R/W)
Table 263. PAGE_SEL register
PAGE_SEL3 PAGE_SEL2 PAGE_SEL1 PAGE_SEL0 0 (1) 0 (1) 0 (1) 1 (2)
_1. This bit must be set to 0 for the correct operation of the device.

This bit must be set to 1 for the correct operation of the device._
Table 264. PAGE_SEL register description
PAGE_SEL[3:0] Selects the advanced features dedicated page. Default value: 0000
13.2 EMB_FUNC_EN_A (04h)
Enable embedded functions register (R/W)
Table 265. EMB_FUNC_EN_A register
MLC_BEFORE
_FSM_EN^0
(1) SIGN_
MOTION_EN TILT_EN PEDO_EN^0
(1) SFLP_GAME_
EN^0
(1)
1. This bit must be set to 0 for the correct operation of the device.

Table 266. EMB_FUNC_EN_A register description
MLC_BEFORE_FSM_EN(1)
Enables machine learning core function. When the machine learning core is enabled by setting
this bit to 1, the MLC algorithms are executed before the FSM programs. Default value: 0
(0: machine learning core function disabled;
1: machine learning core function enabled and executed before FSM programs)
SIGN_MOTION_EN
Enables significant motion detection function. Default value: 0
(0: significant motion detection function disabled;
1: significant motion detection function enabled)
TILT_EN
Enables tilt calculation. Default value: 0
(0: tilt algorithm disabled;
1: tilt algorithm enabled)
PEDO_EN
Enables pedometer algorithm. Default value: 0
(0: pedometer algorithm disabled;
1: pedometer algorithm enabled)
SFLP_GAME_EN
Enables sensor fusion low-power algorithm for 6-axis (accelerometer + gyroscope) game rotation
vector. Default value: 0
(0: sensor fusion algorithm for 6-axis accelerometer + gyroscope disabled;
1: sensor fusion algorithm for 6-axis accelerometer + gyroscope enabled)
1. MLC_EN bit in the EMB_FUNC_EN_B (05h) register must be set to 0 when using this bit.

Embedded functions register description
13.3 EMB_FUNC_EN_B (05h)
Enable embedded functions register (R/W)
Table 267. EMB_FUNC_EN_B register
0 (1) 0 (1) 0 (1) MLC_EN
FIFO_
COMPR_EN
0 (1) 0 (1) FSM_EN
1. This bit must be set to 0 for the correct operation of the device.

Table 268. EMB_FUNC_EN_B register description
MLC_EN(1)
Enables machine learning core function. When the machine learning core is enabled by setting this bit
to 1, the MLC algorithms are executed after executing the FSM programs. Default value: 0
(0: machine learning core function disabled;
1: machine learning core function enabled and executed after FSM programs)
FIFO_COMPR_EN(2)
Enables FIFO compression function. Default value: 0
(0: FIFO compression function disabled;
1: FIFO compression function enabled)
FSM_EN
Enables finite state machine (FSM) function. Default value: 0
(0: FSM function disabled; 1: FSM function enabled)
_1. MLC_BEFORE_FSM_EN bit in the EMB_FUNC_EN_A (04h) register must be set to 0 when using this bit.

This bit is activated if the FIFO_COMPR_RT_EN bit of FIFO_CTRL2 (08h) is set to 1._
13.4 EMB_FUNC_EXEC_STATUS (07h)
Embedded functions execution status register (R)
Table 269. EMB_FUNC_EXEC_STATUS register
0 0 0 0 0 0
EMB_FUNC_
EXEC_OVR
EMB_FUNC
_ENDOP
Table 270. EMB_FUNC_EXEC_STATUS register description
EMB_FUNC_EXEC_OVR
This bit is set to 1 when the execution of the embedded functions program exceeds maximum time
(new data are generated before the end of the algorithms). Default value: 0
EMB_FUNC_ENDOP When this bit is set to 1, no embedded function is running. Default value: 0
EMB_FUNC_EN_B (05h)
13.5 PAGE_ADDRESS (08h)
Page address register (R/W)
Table 271. PAGE_ADDRESS register
PAGE_
ADDR7
PAGE_
ADDR6
PAGE_
ADDR5
PAGE_
ADDR4
PAGE_
ADDR3
PAGE_
ADDR2
PAGE_
ADDR1
PAGE_
ADDR0
Table 272. PAGE_ADDRESS register description
PAGE_ADDR[7:0]
After setting the bit PAGE_WRITE / PAGE_READ in register PAGE_RW (17h), this register is used to set
the address of the register to be written/read in the advanced features page selected through the bits
PAGE_SEL[3:0] in register PAGE_SEL (02h).
13.6 PAGE_VALUE (09h)
Page value register (R/W)
Table 273. PAGE_VALUE register
PAGE_
VALUE7
PAGE_
VALUE6
PAGE_
VALUE5
PAGE_
VALUE4
PAGE_
VALUE3
PAGE_
VALUE2
PAGE_
VALUE1
PAGE_
VALUE0
Table 274. PAGE_VALUE register description
PAGE_VALUE[7:0]
These bits are used to write (if the bit PAGE_WRITE = 1 in register PAGE_RW (17h)) or read (if the bit
PAGE_READ = 1 in register PAGE_RW (17h)) the data at the address PAGE_ADDR[7:0] of the selected
advanced features page.
13.7 EMB_FUNC_INT1 (0Ah)
INT1 pin control register (R/W)
Each bit in this register enables a signal to be carried over INT1. The pin's output supplies the OR combination of
the selected signals.
Table 275. EMB_FUNC_INT1 register
INT1_
FSM_LC
0 (1)
INT1_
SIG_MOT
INT1_TILT
INT1_STEP
_DETECTOR
0 (1) 0 (1) 0 (1)
1. This bit must be set to 0 for the correct operation of the device.

Table 276. EMB_FUNC_INT1 register description
INT1_FSM_LC(1)
Routing FSM long counter timeout interrupt event to INT1. Default value: 0 (0: routing to INT1
disabled; 1: routing to INT1 enabled)
INT1_SIG_MOT(1)
Routing significant motion event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
INT1_TILT(1)
Routing tilt event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
INT1_STEP_DETECTOR(1)
Routing pedometer step recognition event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
1. This bit is activated if the INT1_EMB_FUNC bit of MD1_CFG (5Eh) is set to 1.

PAGE_ADDRESS (08h)
13.8 FSM_INT1 (0Bh)
INT1 pin control register (R/W)
Each bit in this register enables a signal to be carried over INT1. The pin's output supplies the OR combination of
the selected signals.
Table 277. FSM_INT1 register
INT1_FSM8 INT1_FSM7 INT1_FSM6 INT1_FSM5 INT1_FSM4 INT1_FSM3 INT1_FSM2 INT1_FSM1
Table 278. FSM_INT1 register description
INT1_FSM8(1)
Routing FSM8 interrupt event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
INT1_FSM7(1)
Routing FSM7 interrupt event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
INT1_FSM6(1)
Routing FSM6 interrupt event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
INT1_FSM5(1)
Routing FSM5 interrupt event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
INT1_FSM4(1)
Routing FSM4 interrupt event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
INT1_FSM3(1)
Routing FSM3 interrupt event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
INT1_FSM2(1)
Routing FSM2 interrupt event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
INT1_FSM1(1)
Routing FSM1 interrupt event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
1. This bit is activated if the INT1_EMB_FUNC bit of MD1_CFG (5Eh) is set to 1.

FSM_INT1 (0Bh)
13.9 MLC_INT1 (0Dh)
INT1 pin control register (R/W)
Each bit in this register enables a signal to be carried over INT1. The pin's output supplies the OR combination of
the selected signals.
Table 279. MLC_INT1 register
0 (1) 0 (1) 0 (1) 0 (1) INT1_MLC4 INT1_MLC3 INT1_MLC2 INT1_MLC1
1. This bit must be set to 0 for the correct operation of the device.

Table 280. MLC_INT1 register description
INT1_MLC4
Routing MLC4 interrupt event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
INT1_MLC3
Routing MLC3 interrupt event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
INT1_MLC2
Routing MLC2 interrupt event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
INT1_MLC1
Routing MLC1 interrupt event to INT1. Default value: 0
(0: routing to INT1 disabled; 1: routing to INT1 enabled)
13.10 EMB_FUNC_INT2 (0Eh)
INT2 pin control register (R/W)
Each bit in this register enables a signal to be carried over INT2. The pin's output supplies the OR combination of
the selected signals.
Table 281. EMB_FUNC_INT2 register
INT2_
FSM_LC
0 (1)
INT2_
SIG_MOT
INT2_TILT
INT2_STEP
_DETECTOR
0 (1) 0 (1) 0 (1)
1. This bit must be set to 0 for the correct operation of the device.

Table 282. EMB_FUNC_INT2 register description
INT2_FSM_LC(1)
Routing FSM long counter timeout interrupt event to INT2. Default value: 0 (0: routing to INT2
disabled; 1: routing to INT2 enabled)
INT2_SIG_MOT(1)
Routing significant motion event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
INT2_TILT(1)
Routing tilt event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
INT2_STEP_DETECTOR(1)
Routing pedometer step recognition event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
1. This bit is activated if the INT2_EMB_FUNC bit of MD2_CFG (5Fh) is set to 1.

MLC_INT1 (0Dh)
13.11 FSM_INT2 (0Fh)
INT2 pin control register (R/W)
Each bit in this register enables a signal to be carried over INT2. The pin's output supplies the OR combination of
the selected signals.
Table 283. FSM_INT2 register
INT2_FSM8 INT2_FSM7 INT2_FSM6 INT2_FSM5 INT2_FSM4 INT2_FSM3 INT2_FSM2 INT2_FSM1
Table 284. FSM_INT2 register description
INT2_FSM8(1)
Routing FSM8 interrupt event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
INT2_FSM7(1)
Routing FSM7 interrupt event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
INT2_FSM6(1)
Routing FSM6 interrupt event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
INT2_FSM5(1)
Routing FSM5 interrupt event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
INT2_FSM4(1)
Routing FSM4 interrupt event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
INT2_FSM3(1)
Routing FSM3 interrupt event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
INT2_FSM2(1)
Routing FSM2 interrupt event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
INT2_FSM1(1)
Routing FSM1 interrupt event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
1. This bit is activated if the INT2_EMB_FUNC bit of MD2_CFG (5Fh) is set to 1.

FSM_INT2 (0Fh)
13.12 MLC_INT2 (11h)
INT2 pin control register (R/W)
Each bit in this register enables a signal to be carried over INT2. The pin's output supplies the OR combination of
the selected signals.
Table 285. MLC_INT2 register
0 (1) 0 (1) 0 (1) 0 (1) INT2_MLC4 INT2_MLC3 INT2_MLC2 INT2_MLC1
1. This bit must be set to 0 for the correct operation of the device.

Table 286. MLC_INT2 register description
INT2_MLC4
Routing MLC4 interrupt event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
INT2_MLC3
Routing MLC3 interrupt event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
INT2_MLC2
Routing MLC2 interrupt event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
INT2_MLC1
Routing MLC1 interrupt event to INT2. Default value: 0
(0: routing to INT2 disabled; 1: routing to INT2 enabled)
13.13 EMB_FUNC_STATUS (12h)
Embedded function status register (R)
Table 287. EMB_FUNC_STATUS register
IS_FSM_LC 0 IS_SIGMOT IS_TILT IS_STEP_DET 0 0 0
Table 288. EMB_FUNC_STATUS register description
IS_FSM_LC
Interrupt status bit for FSM long counter timeout interrupt event.
(1: interrupt detected; 0: no interrupt)
IS_SIGMOT
Interrupt status bit for significant motion detection
(1: interrupt detected; 0: no interrupt)
IS_TILT
Interrupt status bit for tilt detection
(1: interrupt detected; 0: no interrupt)
IS_STEP_DET
Interrupt status bit for step detection
(1: interrupt detected; 0: no interrupt)
MLC_INT2 (11h)
13.14 FSM_STATUS (13h)
Finite state machine status register (R)
Table 289. FSM_STATUS register
IS_FSM8 IS_FSM7 IS_FSM6 IS_FSM5 IS_FSM4 IS_FSM3 IS_FSM2 IS_FSM1
Table 290. FSM_STATUS register description
IS_FSM8 Interrupt status bit for FSM8 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM7 Interrupt status bit for FSM7 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM6 Interrupt status bit for FSM6 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM5 Interrupt status bit for FSM5 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM4 Interrupt status bit for FSM4 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM3 Interrupt status bit for FSM3 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM2 Interrupt status bit for FSM2 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_FSM1 Interrupt status bit for FSM1 interrupt event. (1: interrupt detected; 0: no interrupt)
13.15 MLC_STATUS (15h)
Machine learning core status register (R)
Table 291. MLC_STATUS register
0 0 0 0 IS_MLC4 IS_MLC3 IS_MLC2 IS_MLC1
Table 292. MLC_STATUS register description
IS_MLC4 Interrupt status bit for MLC4 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_MLC3 Interrupt status bit for MLC3 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_MLC2 Interrupt status bit for MLC2 interrupt event. (1: interrupt detected; 0: no interrupt)
IS_MLC1 Interrupt status bit for MLC1 interrupt event. (1: interrupt detected; 0: no interrupt)
FSM_STATUS (13h)
13.16 PAGE_RW (17h)
Enable read and write mode of advanced features dedicated page (R/W)
Table 293. PAGE_RW register
EMB_
FUNC_LIR
PAGE_
WRITE
PAGE_
READ
0 (1) 0 (1) 0 (1) 0 (1) 0 (1)
1. This bit must be set to 0 for the correct operation of the device.

Table 294. PAGE_RW register description
EMB_FUNC_LIR
Latched interrupt mode for embedded functions. Default value: 0
(0: embedded functions interrupt request not latched;
1: embedded functions interrupt request latched)
PAGE_WRITE
Enables writes to the selected advanced features dedicated page.(1) Default value: 0
(1: enable; 0: disable)
PAGE_READ
Enables reads from the selected advanced features dedicated page.(1) Default value: 0
(1: enable; 0: disable)
1. Page selected by PAGE_SEL[3:0] in PAGE_SEL (02h) register.

13.17 EMB_FUNC_FIFO_EN_A (44h)
Embedded functions FIFO configuration register A (R/W)
Table 295. EMB_FUNC_FIFO_EN_A register
MLC_
FIFO_EN
STEP_COUNTER
_FIFO_EN
SFLP_GBIAS
_FIFO_EN
SFLP_GRAVITY
_FIFO_EN^0
(1) 0 (1) SFLP_GAME
_FIFO_EN^0
(1)
1. This bit must be set to 0 for the correct operation of the device.

Table 296. EMB_FUNC_FIFO_EN_A register description
MLC_FIFO_EN
Enables batching the machine learning core results in the FIFO buffer. Default value: 0
(0: disabled; 1: enabled)
STEP_COUNTER_FIFO_EN
Enables batching the step counter values in the FIFO buffer. Default value: 0
(0: disabled; 1: enabled)
SFLP_GBIAS_FIFO_EN
Enables batching the gyroscope bias values computed by the SFLP algorithm in the FIFO
buffer. Default value: 0
(0: disabled; 1: enabled)
SFLP_GRAVITY_FIFO_EN
Enables batching the gravity values computed by the SFLP algorithm in the FIFO buffer.
Default value: 0
(0: disabled; 1: enabled)
SFLP_GAME_FIFO_EN
Enables batching the game rotation vector (quaternion) values computed by the SFLP
algorithm in the FIFO buffer. Default value: 0
(0: disabled; 1: enabled)
PAGE_RW (17h)
13.18 EMB_FUNC_FIFO_EN_B (45h)
Embedded functions FIFO configuration register B (R/W)
Table 297. EMB_FUNC_FIFO_EN_B register
0 (1) 0 (1) 0 (1) 0 (1) 0 (1) 0 (1)
MLC_FILTER_
FEATURE_FIFO_
EN
0 (1)
1. This bit must be set to 0 for the correct operation of the device.

Table 298. EMB_FUNC_FIFO_EN_B register description
MLC_FILTER_FEATURE_FIFO_EN
Enables batching the machine learning core filters and features in the FIFO buffer.
Default value: 0
(0: disabled; 1: enabled)
13.19 FSM_ENABLE (46h)
Enable FSM register (R/W)
Table 299. FSM_ENABLE register
FSM8_EN FSM7_EN FSM6_EN FSM5_EN FSM4_EN FSM3_EN FSM2_EN FSM1_EN
Table 300. FSM_ENABLE register description
FSM8_EN Enables FSM8. Default value: 0 (0: FSM8 disabled; 1: FSM8 enabled)
FSM7_EN Enables FSM7. Default value: 0 (0: FSM7 disabled; 1: FSM7 enabled)
FSM6_EN Enables FSM6. Default value: 0 (0: FSM6 disabled; 1: FSM6 enabled)
FSM5_EN Enables FSM5. Default value: 0 (0: FSM5 disabled; 1: FSM5 enabled)
FSM4_EN Enables FSM4. Default value: 0 (0: FSM4 disabled; 1: FSM4 enabled)
FSM3_EN Enables FSM3. Default value: 0 (0: FSM3 disabled; 1: FSM3 enabled)
FSM2_EN Enables FSM2. Default value: 0 (0: FSM2 disabled; 1: FSM2 enabled)
FSM1_EN Enables FSM1. Default value: 0 (0: FSM1 disabled; 1: FSM1 enabled)
EMB_FUNC_FIFO_EN_B (45h)
13.20 FSM_LONG_COUNTER_L (48h) and FSM_LONG_COUNTER_H (49h)
FSM long counter status register (R/W)
The long counter value is an unsigned integer value (16-bit format).
Table 301. FSM_LONG_COUNTER_L register
FSM_LC_7 FSM_LC_6 FSM_LC_5 FSM_LC_4 FSM_LC_3 FSM_LC_2 FSM_LC_1 FSM_LC_0
Table 302. FSM_LONG_COUNTER_L register description
FSM_LC_[7:0] Long counter current value (LSbyte). Default value: 00000000
Table 303. FSM_LONG_COUNTER_H register
FSM_LC_15 FSM_LC_14 FSM_LC_13 FSM_LC_12 FSM_LC_11 FSM_LC_10 FSM_LC_9 FSM_LC_8
Table 304. FSM_LONG_COUNTER_H register description
FSM_LC_[15:8] Long counter current value (MSbyte). Default value: 00000000
FSM_LONG_COUNTER_L (48h) and FSM_LONG_COUNTER_H (49h)
13.21 INT_ACK_MASK (4Bh)
Reset status register (R/W)
Table 305. INT_ACK_MASK register
IACK_
MASK7
IACK_
MASK6
IACK_
MASK5
IACK_
MASK4
IACK_
MASK3
IACK_
MASK2
IACK_
MASK1
IACK_
MASK0
Table 306. INT_ACK_MASK register description
IACK_MASK7
If set to 1, when reading the EMB_FUNC_STATUS (12h) / EMB_FUNC_STATUS_MAINPAGE
(49h), FSM_STATUS (13h) / FSM_STATUS_MAINPAGE (4Ah) and MLC_STATUS (15h) /
MLC_STATUS_MAINPAGE (4Bh) registers in latched mode (when the EMB_FUNC_LIR bit is set to 1 in
the PAGE_RW (17h) register), bit 7 of the status register is not reset. When this bit is set to 0, bit 7 of the
status register is reset. Default value: 0
IACK_MASK6
If set to 1, when reading the EMB_FUNC_STATUS (12h) / EMB_FUNC_STATUS_MAINPAGE
(49h), FSM_STATUS (13h) / FSM_STATUS_MAINPAGE (4Ah) and MLC_STATUS (15h) /
MLC_STATUS_MAINPAGE (4Bh) registers in latched mode (when the EMB_FUNC_LIR bit is set to 1 in
the PAGE_RW (17h) register), bit 6 of the status register is not reset. When this bit is set to 0, bit 6 of the
status register is reset. Default value: 0
IACK_MASK5
If set to 1, when reading the EMB_FUNC_STATUS (12h) / EMB_FUNC_STATUS_MAINPAGE
(49h), FSM_STATUS (13h) / FSM_STATUS_MAINPAGE (4Ah) and MLC_STATUS (15h) /
MLC_STATUS_MAINPAGE (4Bh) registers in latched mode (when the EMB_FUNC_LIR bit is set to 1 in
the PAGE_RW (17h) register), bit 5 of the status register is not reset. When this bit is set to 0, bit 5 of the
status register is reset. Default value: 0
IACK_MASK4
If set to 1, when reading the EMB_FUNC_STATUS (12h) / EMB_FUNC_STATUS_MAINPAGE
(49h), FSM_STATUS (13h) / FSM_STATUS_MAINPAGE (4Ah) and MLC_STATUS (15h) /
MLC_STATUS_MAINPAGE (4Bh) registers in latched mode (when the EMB_FUNC_LIR bit is set to 1 in
the PAGE_RW (17h) register), bit 4 of the status register is not reset. When this bit is set to 0, bit 4 of the
status register is reset. Default value: 0
IACK_MASK3
If set to 1, when reading the EMB_FUNC_STATUS (12h) / EMB_FUNC_STATUS_MAINPAGE
(49h), FSM_STATUS (13h) / FSM_STATUS_MAINPAGE (4Ah) and MLC_STATUS (15h) /
MLC_STATUS_MAINPAGE (4Bh) registers in latched mode (when the EMB_FUNC_LIR bit is set to 1 in
the PAGE_RW (17h) register), bit 3 of the status register is not reset. When this bit is set to 0, bit 3 of the
status register is reset. Default value: 0
IACK_MASK2
If set to 1, when reading the EMB_FUNC_STATUS (12h) / EMB_FUNC_STATUS_MAINPAGE
(49h), FSM_STATUS (13h) / FSM_STATUS_MAINPAGE (4Ah) and MLC_STATUS (15h) /
MLC_STATUS_MAINPAGE (4Bh) registers in latched mode (when the EMB_FUNC_LIR bit is set to 1 in
the PAGE_RW (17h) register), bit 2 of the status register is not reset. When this bit is set to 0, bit 2 of the
status register is reset. Default value: 0
IACK_MASK1
If set to 1, when reading the EMB_FUNC_STATUS (12h) / EMB_FUNC_STATUS_MAINPAGE
(49h), FSM_STATUS (13h) / FSM_STATUS_MAINPAGE (4Ah) and MLC_STATUS (15h) /
MLC_STATUS_MAINPAGE (4Bh) registers in latched mode (when the EMB_FUNC_LIR bit is set to 1 in
the PAGE_RW (17h) register), bit 1 of the status register is not reset. When this bit is set to 0, bit 1 of the
status register is reset. Default value: 0
IACK_MASK0
If set to 1, when reading the EMB_FUNC_STATUS (12h) / EMB_FUNC_STATUS_MAINPAGE
(49h), FSM_STATUS (13h) / FSM_STATUS_MAINPAGE (4Ah) and MLC_STATUS (15h) /
MLC_STATUS_MAINPAGE (4Bh) registers in latched mode (when the EMB_FUNC_LIR bit is set to 1 in
the PAGE_RW (17h) register), bit 0 of the status register is not reset. When this bit is set to 0, bit 0 of the
status register is reset. Default value: 0
INT_ACK_MASK (4Bh)
13.22 FSM_OUTS1 (4Ch)
FSM1 output register (R)
Table 307. FSM_OUTS1 register
P_X N_X P_Y N_Y P_Z N_Z P_V N_V
Table 308. FSM_OUTS1 register description
P_X FSM1 output: positive event detected on the X-axis. (0: event not detected; 1: event detected)
N_X FSM1 output: negative event detected on the X-axis. (0: event not detected; 1: event detected)
P_Y FSM1 output: positive event detected on the Y-axis. (0: event not detected; 1: event detected)
N_Y FSM1 output: negative event detected on the Y-axis. (0: event not detected; 1: event detected)
P_Z FSM1 output: positive event detected on the Z-axis. (0: event not detected; 1: event detected)
N_Z FSM1 output: negative event detected on the Z-axis. (0: event not detected; 1: event detected)
P_V FSM1 output: positive event detected on the vector. (0: event not detected; 1: event detected)
N_V FSM1 output: negative event detected on the vector. (0: event not detected; 1: event detected)
13.23 FSM_OUTS2 (4Dh)
FSM2 output register (R)
Table 309. FSM_OUTS2 register
P_X N_X P_Y N_Y P_Z N_Z P_V N_V
Table 310. FSM_OUTS2 register description
P_X FSM2 output: positive event detected on the X-axis. (0: event not detected; 1: event detected)
N_X FSM2 output: negative event detected on the X-axis. (0: event not detected; 1: event detected)
P_Y FSM2 output: positive event detected on the Y-axis. (0: event not detected; 1: event detected)
N_Y FSM2 output: negative event detected on the Y-axis. (0: event not detected; 1: event detected)
P_Z FSM2 output: positive event detected on the Z-axis. (0: event not detected; 1: event detected)
N_Z FSM2 output: negative event detected on the Z-axis. (0: event not detected; 1: event detected)
P_V FSM2 output: positive event detected on the vector. (0: event not detected; 1: event detected)
N_V FSM2 output: negative event detected on the vector. (0: event not detected; 1: event detected)
FSM_OUTS1 (4Ch)
13.24 FSM_OUTS3 (4Eh)
FSM3 output register (R)
Table 311. FSM_OUTS3 register
P_X N_X P_Y N_Y P_Z N_Z P_V N_V
Table 312. FSM_OUTS3 register description
P_X FSM3 output: positive event detected on the X-axis. (0: event not detected; 1: event detected)
N_X FSM3 output: negative event detected on the X-axis. (0: event not detected; 1: event detected)
P_Y FSM3 output: positive event detected on the Y-axis. (0: event not detected; 1: event detected)
N_Y FSM3 output: negative event detected on the Y-axis. (0: event not detected; 1: event detected)
P_Z FSM3 output: positive event detected on the Z-axis. (0: event not detected; 1: event detected)
N_Z FSM3 output: negative event detected on the Z-axis. (0: event not detected; 1: event detected)
P_V FSM3 output: positive event detected on the vector. (0: event not detected; 1: event detected)
N_V FSM3 output: negative event detected on the vector. (0: event not detected; 1: event detected)
13.25 FSM_OUTS4 (4Fh)
FSM4 output register (R)
Table 313. FSM_OUTS4 register
P_X N_X P_Y N_Y P_Z N_Z P_V N_V
Table 314. FSM_OUTS4 register description
P_X FSM4 output: positive event detected on the X-axis. (0: event not detected; 1: event detected)
N_X FSM4 output: negative event detected on the X-axis. (0: event not detected; 1: event detected)
P_Y FSM4 output: positive event detected on the Y-axis. (0: event not detected; 1: event detected)
N_Y FSM4 output: negative event detected on the Y-axis. (0: event not detected; 1: event detected)
P_Z FSM4 output: positive event detected on the Z-axis. (0: event not detected; 1: event detected)
N_Z FSM4 output: negative event detected on the Z-axis. (0: event not detected; 1: event detected)
P_V FSM4 output: positive event detected on the vector. (0: event not detected; 1: event detected)
N_V FSM4 output: negative event detected on the vector. (0: event not detected; 1: event detected)
FSM_OUTS3 (4Eh)
13.26 FSM_OUTS5 (50h)
FSM5 output register (R)
Table 315. FSM_OUTS5 register
P_X N_X P_Y N_Y P_Z N_Z P_V N_V
Table 316. FSM_OUTS5 register description
P_X FSM5 output: positive event detected on the X-axis. (0: event not detected; 1: event detected)
N_X FSM5 output: negative event detected on the X-axis. (0: event not detected; 1: event detected)
P_Y FSM5 output: positive event detected on the Y-axis. (0: event not detected; 1: event detected)
N_Y FSM5 output: negative event detected on the Y-axis. (0: event not detected; 1: event detected)
P_Z FSM5 output: positive event detected on the Z-axis. (0: event not detected; 1: event detected)
N_Z FSM5 output: negative event detected on the Z-axis. (0: event not detected; 1: event detected)
P_V FSM5 output: positive event detected on the vector. (0: event not detected; 1: event detected)
N_V FSM5 output: negative event detected on the vector. (0: event not detected; 1: event detected)
13.27 FSM_OUTS6 (51h)
FSM6 output register (R)
Table 317. FSM_OUTS6 register
P_X N_X P_Y N_Y P_Z N_Z P_V N_V
Table 318. FSM_OUTS6 register description
P_X FSM6 output: positive event detected on the X-axis. (0: event not detected; 1: event detected)
N_X FSM6 output: negative event detected on the X-axis. (0: event not detected; 1: event detected)
P_Y FSM6 output: positive event detected on the Y-axis. (0: event not detected; 1: event detected)
N_Y FSM6 output: negative event detected on the Y-axis. (0: event not detected; 1: event detected)
P_Z FSM6 output: positive event detected on the Z-axis. (0: event not detected; 1: event detected)
N_Z FSM6 output: negative event detected on the Z-axis. (0: event not detected; 1: event detected)
P_V FSM6 output: positive event detected on the vector. (0: event not detected; 1: event detected)
N_V FSM6 output: negative event detected on the vector. (0: event not detected; 1: event detected)
FSM_OUTS5 (50h)
13.28 FSM_OUTS7 (52h)
FSM7 output register (R)
Table 319. FSM_OUTS7 register
P_X N_X P_Y N_Y P_Z N_Z P_V N_V
Table 320. FSM_OUTS7 register description
P_X FSM7 output: positive event detected on the X-axis. (0: event not detected; 1: event detected)
N_X FSM7 output: negative event detected on the X-axis. (0: event not detected; 1: event detected)
P_Y FSM7 output: positive event detected on the Y-axis. (0: event not detected; 1: event detected)
N_Y FSM7 output: negative event detected on the Y-axis. (0: event not detected; 1: event detected)
P_Z FSM7 output: positive event detected on the Z-axis. (0: event not detected; 1: event detected)
N_Z FSM7 output: negative event detected on the Z-axis. (0: event not detected; 1: event detected)
P_V FSM7 output: positive event detected on the vector. (0: event not detected; 1: event detected)
N_V FSM7 output: negative event detected on the vector. (0: event not detected; 1: event detected)
13.29 FSM_OUTS8 (53h)
FSM8 output register (R)
Table 321. FSM_OUTS8 register
P_X N_X P_Y N_Y P_Z N_Z P_V N_V
Table 322. FSM_OUTS8 register description
P_X FSM8 output: positive event detected on the X-axis. (0: event not detected; 1: event detected)
N_X FSM8 output: negative event detected on the X-axis. (0: event not detected; 1: event detected)
P_Y FSM8 output: positive event detected on the Y-axis. (0: event not detected; 1: event detected)
N_Y FSM8 output: negative event detected on the Y-axis. (0: event not detected; 1: event detected)
P_Z FSM8 output: positive event detected on the Z-axis. (0: event not detected; 1: event detected)
N_Z FSM8 output: negative event detected on the Z-axis. (0: event not detected; 1: event detected)
P_V FSM8 output: positive event detected on the vector. (0: event not detected; 1: event detected)
N_V FSM8 output: negative event detected on the vector. (0: event not detected; 1: event detected)
FSM_OUTS7 (52h)
13.30 SFLP_ODR (5Eh)
Sensor fusion low-power output data rate configuration register (R/W)
Table 323. SFLP_ODR register
0 (1) 1 (2)
SFLP_GAME
_ODR_2
SFLP_GAME
_ODR_1
SFLP_GAME
_ODR_0
0 (1) 1 (2) 1 (2)
_1. This bit must be set to 0 for the correct operation of the device.

This bit must be set to 1 for the correct operation of the device._
Table 324. SFLP_ODR register description
SFLP_GAME_ODR_[2:0]
ODR configuration of the SFLP game algorithm:
(000: 15 Hz;
001: 30 Hz;
010: 60 Hz;
011: 120 Hz (default);
100: 240 Hz;
101: 480 Hz)
13.31 FSM_ODR (5Fh)
Finite state machine output data rate configuration register (R/W)
Table 325. FSM_ODR register
0 (1) 1 (2) FSM_ODR_2 FSM_ODR_1 FSM_ODR_0 0 (1) 1 (2) 1 (2)
_1. This bit must be set to 0 for the correct operation of the device.

This bit must be set to 1 for the correct operation of the device._
Table 326. FSM_ODR register description
FSM_ODR_[2:0]
Finite state machine ODR configuration:
(000: 15 Hz;
001: 30 Hz (default);
010: 60 Hz;
011: 120 Hz;
100: 240 Hz;
101: 480 Hz;
110: 960 Hz)
SFLP_ODR (5Eh)
13.32 MLC_ODR (60h)
Machine learning core output data rate configuration register (R/W)
Table 327. MLC_ODR register
0 (1) MLC_ODR_2 MLC_ODR_1 MLC_ODR_0 0 (1) 1 (2) 0 (1) 1 (2)
_1. This bit must be set to 0 for the correct operation of the device.

This bit must be set to 1 for the correct operation of the device._
Table 328. MLC_ODR register description
MLC_ODR_[2:0]
Machine learning core ODR configuration:
(000: 15 Hz;
001: 30 Hz (default);
010: 60 Hz;
011: 120 Hz;
100: 240 Hz)
13.33 STEP_COUNTER_L (62h) and STEP_COUNTER_H (63h)
Step counter output register (R)
Table 329. STEP_COUNTER_L register
STEP_7 STEP_6 STEP_5 STEP_4 STEP_3 STEP_2 STEP_1 STEP_0
Table 330. STEP_COUNTER_L register description
STEP_[7:0] Step counter output (LSbyte)
Table 331. STEP_COUNTER_H register
STEP_15 STEP_14 STEP_13 STEP_12 STEP_11 STEP_10 STEP_9 STEP_8
Table 332. STEP_COUNTER_H register description
STEP_[15:8] Step counter output (MSbyte)
MLC_ODR (60h)
13.34 EMB_FUNC_SRC (64h)
Embedded function source register (R/W)
Table 333. EMB_FUNC_SRC register
PEDO_
RST_STEP^0
(1) STEP_
DETECTED
STEP_COUNT
_DELTA_IA
STEP_
OVERFLOW
STEPCOUNTER
_BIT_SET^0
(1) 0 (1)
1. This bit must be set to 0 for the correct operation of the device.

Table 334. EMB_FUNC_SRC register description
PEDO_RST_STEP
Reset pedometer step counter. Read/write bit.
(0: disabled; 1: enabled)
STEP_DETECTED
Step detector event detection status. Read-only bit.
(0: step detection event not detected; 1: step detection event detected)
STEP_COUNT_DELTA_IA
Pedometer step recognition on delta time status. Read-only bit.
(0: no step recognized during delta time;
1: at least one step recognized during delta time)
STEP_OVERFLOW
Step counter overflow status. Read-only bit.
(0: step counter value < 2^16 ; 1: step counter value reached 2^16 )
STEPCOUNTER_BIT_SET
This bit is equal to 1 when the step count is increased. If a timer period is programmed in
PEDO_SC_DELTAT_L (D0h) and PEDO_SC_DELTAT_H (D1h) embedded advanced features
(page 1) registers, this bit is kept at 0.
Read-only bit.
EMB_FUNC_SRC (64h)
13.35 EMB_FUNC_INIT_A (66h)
Embedded functions initialization register (R/W)
Table 335. EMB_FUNC_INIT_A register
MLC_BEFORE
_FSM_INIT^0
(1) SIG_MOT
_INIT TILT_INIT
STEP_DET
_INIT^0
(1) SFLP_GAME
_INIT^0
(1)
1. This bit must be set to 0 for the correct operation of the device.

Table 336. EMB_FUNC_INIT_A register description
MLC_BEFORE_FSM_INIT Machine learning core initialization request (MLC executed before FSM). Default value: 0
SIG_MOT_INIT Significant motion detection algorithm initialization request. Default value: 0
TILT_INIT Tilt algorithm initialization request. Default value: 0
STEP_DET_INIT Pedometer step counter/detector algorithm initialization request. Default value: 0
SFLP_GAME_INIT SFLP game algorithm initialization request. Default value: 0
13.36 EMB_FUNC_INIT_B (67h)
Embedded functions initialization register (R/W)
Table 337. EMB_FUNC_INIT_B register
0 (1) 0 (1) 0 (1) MLC_INIT
FIFO_
COMPR_INIT
0 (1) 0 (1) FSM_INIT
1. This bit must be set to 0 for the correct operation of the device.

Table 338. EMB_FUNC_INIT_B register description
MLC_INIT Machine learning core initialization request (MLC executed after FSM). Default value: 0
FIFO_COMPR_INIT FIFO compression feature initialization request. Default value: 0
FSM_INIT FSM initialization request. Default value: 0
EMB_FUNC_INIT_A (66h)
13.37 MLC1_SRC (70h)
Machine learning core source register (R)
Table 339. MLC1_SRC register
MLC1_
SRC_7
MLC1_
SRC_6
MLC1_
SRC_5
MLC1_
SRC_4
MLC1_
SRC_3
MLC1_
SRC_2
MLC1_
SRC_1
MLC1_
SRC_0
Table 340. MLC1_SRC register description
MLC1_SRC_[7:0] Output value of MLC1 decision tree
13.38 MLC2_SRC (71h)
Machine learning core source register (R)
Table 341. MLC2_SRC register
MLC2_
SRC_7
MLC2_
SRC_6
MLC2_
SRC_5
MLC2_
SRC_4
MLC2_
SRC_3
MLCS2_
SRC_2
MLC2_
SRC_1
MLC2_
SRC_0
Table 342. MLC2_SRC register description
MLC2_SRC_[7:0] Output value of MLC2 decision tree
13.39 MLC3_SRC (72h)
Machine learning core source register (R)
Table 343. MLC3_SRC register
MLC3_
SRC_7
MLC3_
SRC_6
MLC3_
SRC_5
MLC3_
SRC_4
MLC3_
SRC_3
MLC3_
SRC_2
MLC3_
SRC_1
MLC3_
SRC_0
Table 344. MLC3_SRC register description
MLC3_SRC_[7:0] Output value of MLC3 decision tree
13.40 MLC4_SRC (73h)
Machine learning core source register (R)
Table 345. MLC4_SRC register
MLC4_
SRC_7
MLC4_
SRC_6
MLC4_
SRC_5
MLC4_
SRC_4
MLC4_
SRC_3
MLC4_
SRC_2
MLC4_
SRC_1
MLC4_
SRC_0
Table 346. MLC4_SRC register description
MLC4_SRC_[7:0] Output value of MLC4 decision tree
MLC1_SRC (70h)
14 Embedded advanced features pages
The table given below provides a list of the registers for the embedded advanced features page 0. These
registers are accessible when PAGE_SEL[3:0] are set to 0000 in PAGE_SEL (02h).
Note: External sensor offset compensation registers and transformation matrix correction registers affect FSM data
only. When these registers are set with their default values, no compensation is applied.

Table 347. Register address map - embedded advanced features page 0
Name Type
Register address
Default Comment
Hex Binary
SFLP_GAME_GBIASX_L R/W 6E 01101110 00000000
SFLP_GAME_GBIASX_H R/W 6F 01101111 00000000
SFLP_GAME_GBIASY_L R/W 70 01110000 00000000
SFLP_GAME_GBIASY_H R/W 71 01110001 00000000
SFLP_GAME_GBIASZ_L R/W 72 01110010 00000000
SFLP_GAME_GBIASZ_H R/W 73 01110011 00000000
FSM_EXT_SENSITIVITY_L R/W BA 10111010 00100100
FSM_EXT_SENSITIVITY_H R/W BB 10111011 00010110
FSM_EXT_OFFX_L R/W C0 11000000 00000000
FSM_EXT_OFFX_H R/W C1 11000001 00000000
FSM_EXT_OFFY_L R/W C2 11000010 00000000
FSM_EXT_OFFY_H R/W C3 11000011 00000000
FSM_EXT_OFFZ_L R/W C4 11000100 00000000
FSM_EXT_OFFZ_H R/W C5 11000101 00000000
FSM_EXT_MATRIX_XX_L R/W C6 11000110 00000000
FSM_EXT_MATRIX_XX_H R/W C7 11000111 00111100
FSM_EXT_MATRIX_XY_L R/W C8 11001000 00000000
FSM_EXT_MATRIX_XY_H R/W C9 11001001 00000000
FSM_EXT_MATRIX_XZ_L R/W CA 11001010 00000000
FSM_EXT_MATRIX_XZ_H R/W CB 11001011 00000000
FSM_EXT_MATRIX_YY_L R/W CC 11001100 00000000
FSM_EXT_MATRIX_YY_H R/W CD 11001101 00111100
FSM_EXT_MATRIX_YZ_L R/W CE 11001110 00000000
FSM_EXT_MATRIX_YZ_H R/W CF 11001111 00000000
FSM_EXT_MATRIX_ZZ_L R/W D0 11010000 00000000
FSM_EXT_MATRIX_ZZ_H R/W D1 11010001 00111100
EXT_CFG_A R/W D4 11010100 00000101
EXT_CFG_B R/W D5 11010101 00000010
Embedded advanced features pages
The following table provides a list of the registers for the embedded advanced features page 1. These registers
are accessible when PAGE_SEL[3:0] are set to 0001 in PAGE_SEL (02h).

Table 348. Register address map - embedded advanced features page 1
Name Type
Register address
Default Comment
Hex Binary
FSM_LC_TIMEOUT_L R/W 7A 01111010 00000000
FSM_LC_TIMEOUT_H R/W 7B 01111011 00000000
FSM_PROGRAMS R/W 7C 01111100 00000000
FSM_START_ADD_L R/W 7E 01111110 00000000
FSM_START_ADD_H R/W 7F 01111111 00000000
PEDO_CMD_REG R/W 83 10000011 00000000
PEDO_DEB_STEPS_CONF R/W 84 10000100 00001010
PEDO_SC_DELTAT_L R/W D0 11010000 00000000
PEDO_SC_DELTAT_H R/W D1 11010001 00000000
MLC_EXT_SENSITIVITY_L R/W E8 11101000 00000000
MLC_EXT_SENSITIVITY_H R/W E9 11101001 00111100
The following table provides a list of the registers for the embedded advanced features page 2. These registers
are accessible when PAGE_SEL[3:0] are set to 0010 in PAGE_SEL (02h).

Table 349. Register address map - embedded advanced features page 2
Name Type
Register address
Default Comment
Hex Binary
EXT_FORMAT R/W 00 00000000 00000000
EXT_3BYTE_SENSITIVITY_L R/W 02 00000010 00000000
EXT_3BYTE_SENSITIVITY_H R/W 03 00000011 00001100
EXT_3BYTE_OFFSET_XL R/W 06 00000110 00000000
EXT_3BYTE_OFFSET_L R/W 07 00000111 01010100
EXT_3BYTE_OFFSET_H R/W 08 00001000 00111111
Reserved registers must not be changed. Writing to those registers may cause permanent damage to the device.

The content of the registers that are loaded at boot should not be changed. They contain the factory calibration
values. Their content is automatically restored when the device is powered up.

Write procedure example: write value 06h in register at address 84h (PEDO_DEB_STEPS_CONF) in Page 1

Write bit EMB_FUNC_REG_ACCESS = 1 in FUNC_CFG_ACCESS (01h) // Enable access to embedded functions
registers
Write bit PAGE_WRITE = 1 in PAGE_RW (17h) register // Select write operation mode
Write 0001 in PAGE_SEL[3:0] field of register PAGE_SEL (02h) // Select page 1
Write 84h in PAGE_ADDR register (08h) // Set address
Write 06h in PAGE_DATA register (09h) // Set value to be written
Write bit PAGE_WRITE = 0 in PAGE_RW (17h) register // Write operation disabled
Write bit EMB_FUNC_REG_ACCESS = 0 in FUNC_CFG_ACCESS (01h) // Disable access to embedded functions
registers
Embedded advanced features pages
Read procedure example : read value of register at address 84h (PEDO_DEB_STEPS_CONF) in Page 1
Write bit EMB_FUNC_REG_ACCESS = 1 in FUNC_CFG_ACCESS (01h) // Enable access to embedded functions
registers
Write bit PAGE_READ = 1 in PAGE_RW (17h) register // Select read operation mode
Write 0001 in PAGE_SEL[3:0] field of register PAGE_SEL (02h) // Select page 1
Write 84h in PAGE_ADDR register (08h) // Set address
Read value of PAGE_DATA register (09h) // Get register value
Write bit PAGE_READ = 0 in PAGE_RW (17h) register // Read operation disabled
Write bit EMB_FUNC_REG_ACCESS = 0 in FUNC_CFG_ACCESS (01h) // Disable access to embedded functions
registers
Note: Steps 1 and 2 of both procedures are intended to be performed at the beginning of the procedure. Steps 6 and 7
of both procedures are intended to be performed at the end of the procedure. If the procedure involves multiple
operations, only steps 3, 4 and 5 must be repeated for each operation. If, in particular, the multiple operations
involve consecutive registers, only step 5 can be performed.

Embedded advanced features pages
15 Embedded advanced features register description
15.1 Page 0 - embedded advanced features registers
15.1.1 SFLP_GAME_GBIASX_L (6Eh) and SFLP_GAME_GBIASX_H (6Fh)
SFLP game algorithm X-axis gyroscope bias register (R/W)
The value is expressed as half-precision floating-point format: SEEEEEFFFFFFFFFF (S: 1 sign bit; E: 5 exponent
bits; F: 10 fraction bits).
Table 350. SFLP_GAME_GBIASX_L register
GAME_
GBIASX_7
GAME_
GBIASX_6
GAME_
GBIASX_5
GAME_
GBIASX_4
GAME_
GBIASX_3
GAME_
GBIASX_2
GAME_
GBIASX_1
GAME_
GBIASX_0
Table 351. SFLP_GAME_GBIASX_L register description
GAME_GBIASX_[7:0]
SFLP game algorithm X-axis gbias: temporary register for gbias setting procedure (LSbyte).
Default value: 00000000
Table 352. SFLP_GAME_GBIASX_H register
GAME_
GBIASX_15
GAME_
GBIASX_14
GAME_
GBIASX_13
GAME_
GBIASX_12
GAME_
GBIASX_11
GAME_
GBIASX_10
GAME_
GBIASX_9
GAME_
GBIASX_8
Table 353. SFLP_GAME_GBIASX_H register description
GAME_GBIASX_[15:8]
SFLP game algorithm X-axis gbias: temporary register for gbias setting procedure (MSbyte).
Default value: 00000000
15.1.2 SFLP_GAME_GBIASY_L (70h) and SFLP_GAME_GBIASY_H (71h)
SFLP game algorithm Y-axis gyroscope bias register (R/W)
The value is expressed as half-precision floating-point format: SEEEEEFFFFFFFFFF (S: 1 sign bit; E: 5 exponent
bits; F: 10 fraction bits).
Table 354. SFLP_GAME_GBIASY_L register
GAME_
GBIASY_7
GAME_
GBIASY_6
GAME_
GBIASY_5
GAME_
GBIASY_4
GAME_
GBIASY_3
GAME_
GBIASY_2
GAME_
GBIASY_1
GAME_
GBIASY_0
Table 355. SFLP_GAME_GBIASY_L register description
GAME_GBIASY_[7:0]
SFLP game algorithm Y-axis gbias: temporary register for gbias setting procedure (LSbyte).
Default value: 00000000
Table 356. SFLP_GAME_GBIASY_H register
GAME_
GBIASY_15
GAME_
GBIASY_14
GAME_
GBIASY_13
GAME_
GBIASY_12
GAME_
GBIASY_11
GAME_
GBIASY_10
GAME_
GBIASY_9
GAME_
GBIASY_8
Table 357. SFLP_GAME_GBIASY_H register description
GAME_GBIASY_[15:8] SFLP game algorithm Y-axis gbias: temporary register for gbias setting procedure (MSbyte).
Default value: 00000000
Embedded advanced features register description
15.1.3 SFLP_GAME_GBIASZ_L (72h) and SFLP_GAME_GBIASZ_H (73h)
SFLP game algorithm Z-axis gyroscope bias register (R/W)
The value is expressed as half-precision floating-point format: SEEEEEFFFFFFFFFF (S: 1 sign bit; E: 5 exponent
bits; F: 10 fraction bits).
Table 358. SFLP_GAME_GBIASZ_L register
GAME_
GBIASZ_7
GAME_
GBIASZ_6
GAME_
GBIASZ_5
GAME_
GBIASZ_4
GAME_
GBIASZ_3
GAME_
GBIASZ_2
GAME_
GBIASZ_1
GAME_
GBIASZ_0
Table 359. SFLP_GAME_GBIASZ_L register description
GAME_GBIASZ_[7:0]
SFLP game algorithm Z-axis gbias: temporary register for gbias setting procedure (LSbyte).
Default value: 00000000
Table 360. SFLP_GAME_GBIASZ_H register
GAME_
GBIASZ_15
GAME_
GBIASZ_14
GAME_
GBIASZ_13
GAME_
GBIASZ_12
GAME_
GBIASZ_11
GAME_
GBIASZ_10
GAME_
GBIASZ_9
GAME_
GBIASZ_8
Table 361. SFLP_GAME_GBIASZ_H register description
GAME_GBIASZ_[15:8] SFLP game algorithm Z-axis gbias: temporary register for gbias setting procedure (MSbyte).
Default value: 00000000
15.1.4 FSM_EXT_SENSITIVITY_L (BAh) and FSM_EXT_SENSITIVITY_H (BBh)
External sensor sensitivity value register for the finite state machine (R/W)
This register corresponds to the conversion value of the external sensor. The register value is expressed as
half-precision floating-point format: SEEEEEFFFFFFFFFF (S: 1 sign bit; E: 5 exponent bits; F: 10 fraction bits).
Default value of FSM_EXT_S_[15:0] bits is 0x1624 (when using an external magnetometer this value
corresponds to 0.0015 gauss/LSB).
Table 362. FSM_EXT_SENSITIVITY_L register
FSM_EXT_
S_7
FSM_EXT_
S_6
FSM_EXT_
S_5
FSM_EXT_
S_4
FSM_EXT_
S_3
FSM_EXT_
S_2
FSM_EXT_
S_1
FSM_EXT_
S_0
Table 363. FSM_EXT_SENSITIVITY_L register description
FSM_EXT_S_[7:0] External sensor sensitivity (LSbyte). Default value: 00100100
Table 364. FSM_EXT_SENSITIVITY_H register
FSM_EXT_
S_15
FSM_EXT_
S_14
FSM_EXT_
S_13
FSM_EXT_
S_12
FSM_EXT_
S_11
FSM_EXT_
S_10
FSM_EXT_
S_9
FSM_EXT_
S_8
Table 365. FSM_EXT_SENSITIVITY_H register description
FSM_EXT_S_[15:8] External sensor (MSbyte). Default value: 00010110
Page 0 - embedded advanced features registers
15.1.5 FSM_EXT_OFFX_L (C0h) and FSM_EXT_OFFX_H (C1h)
External sensor X-axis offset
The value is expressed as half-precision floating-point format: SEEEEEFFFFFFFFFF
(S: 1 sign bit; E: 5 exponent bits; F: 10 fraction bits).
Table 366. FSM_EXT_OFFX_L register
FSM_EXT_
OFFX_7
FSM_EXT_
OFFX_6
FSM_EXT_
OFFX_5
FSM_EXT_
OFFX_4
FSM_EXT_
OFFX_3
FSM_EXT_
OFFX_2
FSM_EXT_
OFFX_1
FSM_EXT_
OFFX_0
Table 367. FSM_EXT_OFFX_L register description
FSM_EXT_OFFX_[7:0] External sensor X-axis offset (LSbyte). Default value: 00000000
Table 368. FSM_EXT_OFFX_H register
FSM_EXT_
OFFX_15
FSM_EXT_
OFFX_14
FSM_EXT_
OFFX_13
FSM_EXT_
OFFX_12
FSM_EXT_
OFFX_11
FSM_EXT_
OFFX_10
FSM_EXT_
OFFX_9
FSM_EXT_
OFFX_8
Table 369. FSM_EXT_OFFX_H register description
FSM_EXT_OFFX_[15:8] External sensor X-axis offset (MSbyte). Default value: 00000000
15.1.6 FSM_EXT_OFFY_L (C2h) and FSM_EXT_OFFY_H (C3h)
External sensor Y-axis offset
The value is expressed as half-precision floating-point format: SEEEEEFFFFFFFFFF
(S: 1 sign bit; E: 5 exponent bits; F: 10 fraction bits).
Table 370. FSM_EXT_OFFY_L register
FSM_EXT_
OFFY_7
FSM_EXT_
OFFY_6
FSM_EXT_
OFFY_5
FSM_EXT_
OFFY_4
FSM_EXT_
OFFY_3
FSM_EXT_
OFFY_2
FSM_EXT_
OFFY_1
FSM_EXT_
OFFY_0
Table 371. FSM_EXT_OFFY_L register description
FSM_EXT_OFFY_[7:0] External sensor Y-axis offset (LSbyte). Default value: 00000000
Table 372. FSM_EXT_OFFY_H register
FSM_EXT_
OFFY_15
FSM_EXT_
OFFY_14
FSM_EXT_
OFFY_13
FSM_EXT_
OFFY_12
FSM_EXT_
OFFY_11
FSM_EXT_
OFFY_10
FSM_EXT_
OFFY_9
FSM_EXT_
OFFY_8
Table 373. FSM_EXT_OFFY_H register description
FSM_EXT_OFFY_[15:8] External sensor Y-axis offset (MSbyte). Default value: 00000000
Page 0 - embedded advanced features registers
15.1.7 FSM_EXT_OFFZ_L (C4h) and FSM_EXT_OFFZ_H (C5h)
External sensor Z-axis offset register (R/W)
The value is expressed as half-precision floating-point format: SEEEEEFFFFFFFFFF
(S: 1 sign bit; E: 5 exponent bits; F: 10 fraction bits).
Table 374. FSM_EXT_OFFZ_L register
FSM_EXT_
OFFZ_7
FSM_EXT_
OFFZ_6
FSM_EXT_
OFFZ_5
FSM_EXT_
OFFZ_4
FSM_EXT_
OFFZ_3
FSM_EXT_
OFFZ_2
FSM_EXT_
OFFZ_1
FSM_EXT_
OFFZ_0
Table 375. FSM_EXT_OFFZ_L register description
FSM_EXT_OFFZ_[7:0] External sensor Z-axis offset (LSbyte). Default value: 00000000
Table 376. FSM_EXT_OFFZ_H register
FSM_EXT_
OFFZ_15
FSM_EXT_
OFFZ_14
FSM_EXT_
OFFZ_13
FSM_EXT_
OFFZ_12
FSM_EXT_
OFFZ_11
FSM_EXT_
OFFZ_10
FSM_EXT_
OFFZ_9
FSM_EXT_
OFFZ_8
Table 377. FSM_EXT_OFFZ_H register description
FSM_EXT_OFFZ_[15:8] External sensor Z-axis offset (MSbyte). Default value: 00000000
15.1.8 FSM_EXT_MATRIX_XX_L (C6h) and FSM_EXT_MATRIX_XX_H (C7h)
External sensor transformation matrix register (R/W)
The value is expressed as half-precision floating-point format: SEEEEEFFFFFFFFFF
(S: 1 sign bit; E: 5 exponent bits; F: 10 fraction bits).
Table 378. FSM_EXT_MATRIX_XX_L register
FSM_EXT_
MAT_XX_7
FSM_EXT_
MAT_XX_6
FSM_EXT_
MAT_XX_5
FSM_EXT_
MAT_XX_4
FSM_EXT_
MAT_XX_3
FSM_EXT_
MAT_XX_2
FSM_EXT_
MAT_XX_1
FSM_EXT_
XX_0
Table 379. FSM_EXT_MATRIX_XX_L register description
FSM_EXT_MAT_XX_[7:0] Transformation matrix row1 col1 coefficient (LSbyte). Default value: 00000000
Table 380. FSM_EXT_MATRIX_XX_H register
FSM_EXT_
MAT_XX_15
FSM_EXT_
MAT_XX_14
FSM_EXT_
MAT_XX_13
FSM_EXT_
MAT_XX_12
FSM_EXT_
MAT_XX_11
FSM_EXT_
MAT_XX_10
FSM_EXT_
XX_9
FSM_EXT_
XX_8
Table 381. FSM_EXT_MATRIX_XX_H register description
FSM_EXT_MAT_[15:8] Transformation matrix row1 col1 coefficient (MSbyte). Default value: 00111100
Page 0 - embedded advanced features registers
15.1.9 FSM_EXT_MATRIX_XY_L (C8h) and FSM_EXT_MATRIX_XY_H (C9h)
External sensor transformation matrix register (R/W)
The value is expressed as half-precision floating-point format: SEEEEEFFFFFFFFFF
(S: 1 sign bit; E: 5 exponent bits; F: 10 fraction bits).
Table 382. FSM_EXT_MATRIX_XY_L register
FSM_EXT_
MAT_XY_7
FSM_EXT_
MAT_XY_6
FSM_EXT_
MAT_XY_5
FSM_EXT_
MAT_XY_4
FSM_EXT_
MAT_XY_3
FSM_EXT_
MAT_XY_2
FSM_EXT_
MAT_XY_1
FSM_EXT_
MAT_XY_0
Table 383. FSM_EXT_MATRIX_XY_L register description
FSM_EXT_MAT_XY_[7:0] Transformation matrix row1 col2 (and row2 col1) coefficient (LSbyte). Default value: 00000000
Table 384. FSM_EXT_MATRIX_XY_H register
FSM_EXT_
XY_15
FSM_EXT_
XY_14
FSM_EXT_
XY_13
FSM_EXT_
XY_12
FSM_EXT_
XY_11
FSM_EXT_
XY_10
FSM_EXT_
XY_9
FSM_EXT_
XY_8
Table 385. FSM_EXT_MATRIX_XY_H register description
FSM_EXT_MAT_XY_[15:8] Transformation matrix row1 col2 (and row2 col1) coefficient (MSbyte). Default value: 00000000
15.1.10 FSM_EXT_MATRIX_XZ_L (CAh) and FSM_EXT_MATRIX_XZ_H (CBh)
External sensor transformation matrix register (R/W)
The value is expressed as half-precision floating-point format: SEEEEEFFFFFFFFFF
(S: 1 sign bit; E: 5 exponent bits; F: 10 fraction bits).
Table 386. FSM_EXT_MATRIX_XZ_L register
FSM_EXT_
MAT_XZ_7
FSM_EXT_
MAT_XZ_6
FSM_EXT_
MAT_XZ_5
FSM_EXT_
MAT_XZ_4
FSM_EXT_
MAT_XZ_3
FSM_EXT_
MAT_XZ_2
FSM_EXT_
MAT_XZ_1
FSM_EXT_
MAT_XZ_0
Table 387. FSM_EXT_MATRIX_XZ_L register description
FSM_EXT_MAT_XZ_[7:0] Transformation matrix row1 col3 (and row3 col1) coefficient (LSbyte). Default value: 00000000
Table 388. FSM_EXT_MATRIX_XZ_H register
FSM_EXT_
MAT_XZ_15
FSM_EXT_
MAT_XZ_14
FSM_EXT_
MAT_XZ_13
FSM_EXT_
MAT_XZ_12
FSM_EXT_
MAT_XZ_11
FSM_EXT_
MAT_XZ_10
FSM_EXT_
MAT_XZ_9
FSM_EXT_
MAT_XZ_8
Table 389. FSM_EXT_MATRIX_XZ_H register description
FSM_EXT_MAT_XZ_[15:8] Transformation matrix row1 col3 (and row3 col1) coefficient (MSbyte). Default value: 00000000
Page 0 - embedded advanced features registers
15.1.11 FSM_EXT_MATRIX_YY_L (CCh) and FSM_EXT_MATRIX_YY_H (CDh)
External sensor transformation matrix register (R/W)
The value is expressed as half-precision floating-point format: SEEEEEFFFFFFFFFF
(S: 1 sign bit; E: 5 exponent bits; F: 10 fraction bits).
Table 390. FSM_EXT_MATRIX_YY_L register
FSM_EXT_
MAT_YY_7
FSM_EXT_
MAT_YY_6
FSM_EXT_
MAT_YY_5
FSM_EXT_
MAT_YY_4
FSM_EXT_
MAT_YY_3
FSM_EXT_
MAT_YY_2
FSM_EXT_
MAT_YY_1
FSM_EXT_
MAT_YY_0
Table 391. FSM_EXT_MATRIX_YY_L register description
FSM_EXT_MAT_YY_[7:0] Transformation matrix row2 col2 coefficient (LSbyte). Default value: 00000000
Table 392. FSM_EXT_MATRIX_YY_H register
FSM_EXT_
MAT_YY_15
FSM_EXT_
MAT_YY_14
FSM_EXT_
MAT_YY_13
FSM_EXT_
MAT_YY_12
FSM_EXT_
MAT_YY_11
FSM_EXT_
MAT_YY_10
FSM_EXT_
MAT_YY_9
FSM_EXT_
MAT_YY_8
Table 393. FSM_EXT_MATRIX_YY_H register description
FSM_EXT_MAT_YY_[15:8] Transformation matrix row2 col2 coefficient (MSbyte). Default value: 00111100
15.1.12 FSM_EXT_MATRIX_YZ_L (CEh) and FSM_EXT_MATRIX_YZ_H (CFh)
External sensor transformation matrix register (R/W)
The value is expressed as half-precision floating-point format: SEEEEEFFFFFFFFFF
(S: 1 sign bit; E: 5 exponent bits; F: 10 fraction bits).
Table 394. FSM_EXT_MATRIX_YZ_L register
FSM_EXT_
MAT_YZ_7
FSM_EXT_
MAT_YZ_6
FSM_EXT_
MAT_YZ_5
FSM_EXT_
MAT_YZ_4
FSM_EXT_
MAT_YZ_3
FSM_EXT_
MAT_YZ_2
FSM_EXT_
MAT_YZ_1
FSM_EXT_
MAT_YZ_0
Table 395. FSM_EXT_MATRIX_YZ_L register description
FSM_EXT_MAT_YZ_[7:0]
Transformation matrix row2 col3 (and row3 col2) coefficient (LSbyte).
Default value: 00000000
Table 396. FSM_EXT_MATRIX_YZ_H register
FSM_EXT_
MAT_YZ_15
FSM_EXT_
MAT_YZ_14
FSM_EXT_
MAT_YZ_13
FSM_EXT_
MAT_YZ_12
FSM_EXT_
MAT_YZ_11
FSM_EXT_
MAT_YZ_10
FSM_EXT_
MAT_YZ_9
FSM_EXT_
MAT_YZ_8
Table 397. FSM_EXT_MATRIX_YZ_H register description
FSM_EXT_MAT_YZ_[15:8]
Transformation matrix row2 col3 (and row3 col2) coefficient (MSbyte).
Default value: 00000000
Page 0 - embedded advanced features registers
15.1.13 FSM_EXT_MATRIX_ZZ_L (D0h) and FSM_EXT_MATRIX_ZZ_H (D1h)
External sensor transformation matrix register (R/W)
The value is expressed as half-precision floating-point format: SEEEEEFFFFFFFFFF
(S: 1 sign bit; E: 5 exponent bits; F: 10 fraction bits).
Table 398. FSM_EXT_MATRIX_ZZ_L register
FSM_EXT_
MAT_ZZ_7
FSM_EXT_
MAT_ZZ_6
FSM_EXT_
MAT_ZZ_5
FSM_EXT_
MAT_ZZ_4
FSM_EXT_
MAT_ZZ_3
FSM_EXT_
MAT_ZZ_2
FSM_EXT_
MAT_ZZ_1
FSM_EXT_
MAT_ZZ_0
Table 399. FSM_EXT_MATRIX_ZZ_L register description
FSM_EXT_MAT_ZZ_[7:0] Transformation matrix row3 col3 coefficient (LSbyte). Default value: 00000000
Table 400. FSM_EXT_MATRIX_ZZ_H register
FSM_EXT_
MAT_ZZ_15
FSM_EXT_
MAT_ZZ_14
FSM_EXT_
MAT_ZZ_13
FSM_EXT_
MAT_ZZ_12
FSM_EXT_
MAT_ZZ_11
FSM_EXT_
MAT_ZZ_10
FSM_EXT_
MAT_ZZ_9
FSM_EXT_
MAT_ZZ_8
Table 401. FSM_EXT_MATRIX_ZZ_H register description
FSM_EXT_MAT_ZZ_[15:8] Transformation matrix row3 col3 coefficient (MSbyte). Default value: 00111100
Page 0 - embedded advanced features registers
15.1.14 EXT_CFG_A (D4h)
External sensor coordinates (Z and Y axes) rotation register (r/w).
Table 402. EXT_CFG_A register
0 (1)
EXT_Y_
AXIS2
EXT_Y_
AXIS1
EXT_Y_
AXIS0^0
(1) EXT_Z_
AXIS2
EXT_Z_
AXIS1
EXT_Z_
AXIS0
1. This bit must be set to 0 for the correct operation of the device.

Table 403. EXT_CFG_A description
EXT_Y_AXIS[2:0]
External sensor Y-axis coordinates rotation (to be aligned to accelerometer/gyroscope axes orientation)
(000: Y = Y; (default)
001: Y = -Y;
010: Y = X;
011: Y = -X;
100: Y = -Z;
101: Y = Z;
Others: Y = Y)
EXT_Z_AXIS[2:0]
External sensor Z-axis coordinates rotation (to be aligned to accelerometer/gyroscope axes orientation)
(000: Z = Y;
001: Z = -Y;
010: Z = X;
011: Z = -X;
100: Z = -Z;
101: Z = Z; (default)
Others: Z = Y)
15.1.15 EXT_CFG_B (D5h)
External sensor coordinates (X-axis) rotation register (r/w).
Table 404. EXT_CFG_B register
0 (1) 0 (1) 0 (1) 0 (1) 0 (1)
EXT_X_
AXIS2
EXT_X_
AXIS1
EXT_X_
AXIS0
1. This bit must be set to 0 for the correct operation of the device.

Table 405. EXT_CFG_B description
EXT_X_AXIS[2:0]
External sensor X-axis coordinates rotation (to be aligned to accelerometer/gyroscope axes orientation)
(000: X = Y;
001: X = -Y;
010: X = X; (default)
011: X = -X;
100: X = -Z;
101: X = Z;
Others: X = Y)
Page 0 - embedded advanced features registers
15.2 Page 1 - embedded advanced features registers
15.2.1 FSM_LC_TIMEOUT_L (7Ah) and FSM_LC_TIMEOUT_H (7Bh)
FSM long counter timeout register (R/W)
The long counter timeout value is an unsigned integer value (16-bit format). When the long counter value reached
this value, the FSM generates an interrupt.
Table 406. FSM_LC_TIMEOUT_L register
FSM_LC_
TIMEOUT7
FSM_LC_
TIMEOUT6
FSM_LC_
TIMEOUT5
FSM_LC_
TIMEOUT4
FSM_LC_
TIMEOUT3
FSM_LC_
TIMEOUT2
FSM_LC_
TIMEOUT1
FSM_LC_
TIMEOUT0
Table 407. FSM_LC_TIMEOUT_L register description
FSM_LC_TIMEOUT[7:0] FSM long counter timeout value (LSbyte). Default value: 00000000
Table 408. FSM_LC_TIMEOUT_H register
FSM_LC_
TIMEOUT15
FSM_LC_
TIMEOUT14
FSM_LC_
TIMEOUT13
FSM_LC_
TIMEOUT12
FSM_LC_
TIMEOUT11
FSM_LC_
TIMEOUT10
FSM_LC_
TIMEOUT9
FSM_LC_
TIMEOUT8
Table 409. FSM_LC_TIMEOUT_H register description
FSM_LC_TIMEOUT[15:8] FSM long counter timeout value (MSbyte). Default value: 00000000
15.2.2 FSM_PROGRAMS (7Ch)
FSM number of programs register (R/W)
Table 410. FSM_PROGRAMS register
FSM_N_
PROG7
FSM_N_
PROG6
FSM_N_
PROG5
FSM_N_
PROG4
FSM_N_
PROG3
FSM_N_
PROG2
FSM_N_
PROG1
FSM_N_
PROG0
Table 411. FSM_PROGRAMS register description
FSM_N_PROG[7:0]
Number of FSM programs; must be less than or equal to 8.
Default value: 00000000
Page 1 - embedded advanced features registers
15.2.3 FSM_START_ADD_L (7Eh) and FSM_START_ADD_H (7Fh)
FSM start address register (R/W). First available address is 0x35C.
Table 412. FSM_START_ADD_L register
FSM_
START7
FSM_
START6
FSM_
START5
FSM_
START4
FSM_
START3
FSM_
START2
FSM_
START1
FSM_
START0
Table 413. FSM_START_ADD_L register description
FSM_START[7:0] FSM start address value (LSbyte). Default value: 00000000
Table 414. FSM_START_ADD_H register
FSM_
START15
FSM_
START14
FSM_
START13
FSM_
START12
FSM_
START11
FSM_
START10
FSM_
START9
FSM_
START8
Table 415. FSM_START_ADD_H register description
FSM_START[15:8] FSM start address value (MSbyte). Default value: 00000000
15.2.4 PEDO_CMD_REG (83h)
Pedometer configuration register (R/W)
Table 416. PEDO_CMD_REG register
0 (1) 0 (1) 0 (1) 0 (1) COUNT_ENCARRY_ REJECTION_ENFP_ 0 (1) 0 (1)
1. This bit must be set to 0 for the correct operation of the device.

Table 417. PEDO_CMD_REG register description
CARRY_COUNT_EN Set when user wants to generate interrupt only on count overflow event.
FP_REJECTION_EN(1) Enables the false-positive rejection feature
1. This bit is activated if the MLC_EN bit of EMB_FUNC_EN_B (05h) or the MLC_BEFORE_FSM_EN bit in the
EMB_FUNC_EN_A (04h) register is set to 1.

Page 1 - embedded advanced features registers
15.2.5 PEDO_DEB_STEPS_CONF (84h)
Pedometer debounce configuration register (R/W)
Table 418. PEDO_DEB_STEPS_CONF register
DEB_
STEP7
DEB_
STEP6
DEB_
STEP5
DEB_
STEP4
DEB_
STEP3
DEB_
STEP2
DEB_
STEP1
DEB_
STEP0
Table 419. PEDO_DEB_STEPS_CONF register description
DEB_STEP[7:0]
Debounce threshold. Minimum number of steps to increment the step counter (debounce).
Default value: 00001010
15.2.6 PEDO_SC_DELTAT_L (D0h) and PEDO_SC_DELTAT_H (D1h)
Time period register for step detection on delta time (R/W)
Table 420. PEDO_SC_DELTAT_L register
PD_SC_7 PD_SC_6 PD_SC_5 PD_SC_4 PD_SC_3 PD_SC_2 PD_SC_1 PD_SC_0
Table 421. PEDO_SC_DELTAT_H register
PD_SC_15 PD_SC_14 PD_SC_13 PD_SC_12 PD_SC_11 PD_SC_10 PD_SC_9 PD_SC_8
Table 422. PEDO_SC_DELTAT_H/L register description
PD_SC_[15:0] Time period value (1LSB = 6.4 ms)
Page 1 - embedded advanced features registers
15.2.7 MLC_EXT_SENSITIVITY_L (E8h) and MLC_EXT_SENSITIVITY_H (E9h)
External sensor sensitivity value register for the machine learning core (R/W)
This register corresponds to the conversion value of the external sensor. The register value is expressed as
half-precision floating-point format: SEEEEEFFFFFFFFFF (S: 1 sign bit; E: 5 exponent bits; F: 10 fraction bits).
Default value of MLC_EXT_S_[15:0] is 0x3C00 (when using an external magnetometer this value corresponds to
1 gauss/LSB).
Table 423. MLC_EXT_SENSITIVITY_L register
MLC_
EXT_S_7
MLC_
EXT_S_6
MLC_
EXT_S_5
MLC_
EXT_S_4
MLC_
EXT_S_3
MLC_
EXT_S_2
MLC_
EXT_S_1
MLC_
EXT_S_0
Table 424. MLC_ EXT_SENSITIVITY_L register description
MLC_EXT_S_[7:0] External sensor sensitivity (LSbyte). Default value: 00000000
Table 425. MLC_EXT_SENSITIVITY_H register
MLC_
EXT_S_15
MLC_
EXT_S_14
MLC_
EXT_S_13
MLC_
EXT_S_12
MLC_
EXT_S_11
MLC_
EXT_S_10
MLC_
EXT_S_9
MLC_
EXT_S_8
Table 426. MLC_EXT_SENSITIVITY_H register description
MLC_EXT_S_[15:8] External sensor sensitivity (MSbyte). Default value: 00111100
Page 1 - embedded advanced features registers
15.3 Page 2 - embedded advanced features registers
15.3.1 EXT_FORMAT (00h)
AH / Qvar / external sensor data format (2-byte or 3-byte) for the finite state machine and machine learning core
(R/W)
Table 427. EXT_FORMAT register
0 (1) 0 (1) 0 (1) 0 (1) 0 (1)
EXT_FORMAT
_SEL^0
(1) 0 (1)
1. This bit must be set to 0 for the correct operation of the device.

Table 428. EXT_FORMAT register description
EXT_FORMAT_SEL
Selects the format of AH / Qvar / external sensor data for FSM and MLC processing. Default value: 0
(0: 2-byte format; 1: 3-byte format)
15.3.2 EXT_3BYTE_SENSITIVITY_L (02h) and EXT_3BYTE_SENSITIVITY_H (03h)
External sensor (3-byte output data) sensitivity value register for the finite state machine and machine learning
core (R/W)
This register corresponds to the conversion value of the external sensor having 3-byte output data. The register
value is expressed as half-precision floating-point format: SEEEEEFFFFFFFFFF (S: 1 sign bit; E: 5 exponent bits;
F: 10 fraction bits).
The default value of EXT_3BYTE_S_[15:0] is 0x0C00 (when using an external pressure sensor this value
corresponds to 2.441e-04 hPa/LSB).
Table 429. EXT_3BYTE_SENSITIVITY_L register
EXT_3BYTE_
S_7
EXT_3BYTE_
S_6
EXT_3BYTE_
S_5
EXT_3BYTE_
S_4
EXT_3BYTE_
S_3
EXT_3BYTE_
S_2
EXT_3BYTE_
S_1
EXT_3BYTE_
S_0
Table 430. EXT_3BYTE_SENSITIVITY_L register description
EXT_3BYTE_S_[7:0] External sensor (3-byte output data) sensitivity (LSbyte). Default value: 00000000
Table 431. EXT_3BYTE_SENSITIVITY_H register
EXT_3BYTE_
S_15
EXT_3BYTE_
S_14
EXT_3BYTE_
S_13
EXT_3BYTE_
S_12
EXT_3BYTE_
S_11
EXT_3BYTE_
S_10
EXT_3BYTE_
S_9
EXT_3BYTE_
S_8
Table 432. EXT_3BYTE_SENSITIVITY_H register description
EXT_3BYTE_S_[15:8] External sensor (3-byte output data) sensitivity (MSbyte). Default value: 00001100
Page 2 - embedded advanced features registers
15.3.3 EXT_3BYTE_OFFSET_XL (06h), EXT_3BYTE_OFFSET_L (07h) and EXT_3BYTE_OFFSET_H
(08h)
External sensor (3-byte output data) offset value register for the finite state machine and machine learning core
(R/W)
This register corresponds to the offset value applied to external sensor output data (3-byte) before being
processed in FSM and MLC. The value is expressed as a 24-bit word in two’s complement.
The default value of EXT_3BYTE_OFF_[23:0] is 0x3F5400, which corresponds to 4150272 LSB. This
offset is subtracted from the external output data (in LSB) before the sensitivity (configured in the
EXT_3BYTE_SENSITIVITY_L (02h) and EXT_3BYTE_SENSITIVITY_H (03h) registers) is internally applied.
Table 433. EXT_3BYTE_OFFSET_XL register
EXT_3BYTE_
OFF_7
EXT_3BYTE_
OFF_6
EXT_3BYTE_
OFF_5
EXT_3BYTE_
OFF_4
EXT_3BYTE_
OFF_3
EXT_3BYTE_
OFF_2
EXT_3BYTE_
OFF_1
EXT_3BYTE_
OFF_0
Table 434. EXT_3BYTE_OFFSET_XL register description
EXT_3BYTE_OFF_[7:0] External sensor (3-byte output data) offset (low byte). Default value: 00000000
Table 435. EXT_3BYTE_OFFSET_L register
EXT_3BYTE_
OFF_15
EXT_3BYTE_
OFF_14
EXT_3BYTE_
OFF_13
EXT_3BYTE_
OFF_12
EXT_3BYTE_
OFF_11
EXT_3BYTE_
OFF_10
EXT_3BYTE_
OFF_9
EXT_3BYTE_
OFF_8
Table 436. EXT_3BYTE_OFFSET_L register description
EXT_3BYTE_OFF_[15:8] External sensor (3-byte output data) offset (mid byte). Default value: 01010100
Table 437. EXT_3BYTE_OFFSET_H register
EXT_3BYTE_
OFF_23
EXT_3BYTE_
OFF_22
EXT_3BYTE_
OFF_21
EXT_3BYTE_
OFF_20
EXT_3BYTE_
OFF_19
EXT_3BYTE_
OFF_18
EXT_3BYTE_
OFF_17
EXT_3BYTE_
OFF_16
Table 438. EXT_3BYTE_OFFSET_H register description
EXT_3BYTE_OFF_[23:16] External sensor (3-byte output data) offset (high byte). Default value: 00111111
Page 2 - embedded advanced features registers
16 Sensor hub register mapping
The table given below provides a list of the registers for the sensor hub functions available in the device and the
corresponding addresses. The sensor hub registers are accessible when bit SHUB_REG_ACCESS is set to 1 in
FUNC_CFG_ACCESS (01h).
Table 439. Register address map - sensor hub registers
Name Type
Register address
Default Comment
Hex Binary
SENSOR_HUB_1 R 02 00000010 output
SENSOR_HUB_2 R 03 00000011 output
SENSOR_HUB_3 R 04 00000100 output
SENSOR_HUB_4 R 05 00000101 output
SENSOR_HUB_5 R 06 00000110 output
SENSOR_HUB_6 R 07 00000111 output
SENSOR_HUB_7 R 08 00001000 output
SENSOR_HUB_8 R 09 00001001 output
SENSOR_HUB_9 R 0A 00001010 output
SENSOR_HUB_10 R 0B 00001011 output
SENSOR_HUB_11 R 0C 00001100 output
SENSOR_HUB_12 R 0D 00001101 output
SENSOR_HUB_13 R 0E 00001110 output
SENSOR_HUB_14 R 0F 00001111 output
SENSOR_HUB_15 R 10 00010000 output
SENSOR_HUB_16 R 11 00010001 output
SENSOR_HUB_17 R 12 00010010 output
SENSOR_HUB_18 R 13 00010011 output
MASTER_CONFIG R/W 14 00010100 00000000
SLV0_ADD R/W 15 00010101 00000000
SLV0_SUBADD R/W 16 00010110 00000000
SLV0_CONFIG R/W 17 00010111 10000000
SLV1_ADD R/W 18 00011000 00000000
SLV1_SUBADD R/W 19 00011001 00000000
SLV1_CONFIG R/W 1A 00011010 00010000
SLV2_ADD R/W 1B 00011011 00000000
SLV2_SUBADD R/W 1C 00011100 00000000
SLV2_CONFIG R/W 1D 00011101 00000000
SLV3_ADD R/W 1E 00011110 00000000
SLV3_SUBADD R/W 1F 00011111 00000000
SLV3_CONFIG R/W 20 00100000 00000000
DATAWRITE_SLV0 R/W 21 00100001 00000000
STATUS_MASTER R 22 00100010 output
Reserved registers must not be changed. Writing to those registers may cause permanent damage to the device.
The content of the registers that are loaded at boot should not be changed. They contain the factory calibration
values. Their content is automatically restored when the device is powered up.
Sensor hub register mapping
17 Sensor hub register description
17.1 SENSOR_HUB_1 (02h)
Sensor hub output register (R)
First byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG number
of read operation configurations (for external sensors from x = 0 to x = 3).
Table 440. SENSOR_HUB_1 register
Sensor
Hub1_7
Sensor
Hub1_6
Sensor
Hub1_5
Sensor
Hub1_4
Sensor
Hub1_3
Sensor
Hub1_2
Sensor
Hub1_1
Sensor
Hub1_0
Table 441. SENSOR_HUB_1 register description
SensorHub1_[7:0] First byte associated to external sensors
17.2 SENSOR_HUB_2 (03h)
Sensor hub output register (R)
Second byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 442. SENSOR_HUB_2 register
Sensor
Hub2_7
Sensor
Hub2_6
Sensor
Hub2_5
Sensor
Hub2_4
Sensor
Hub2_3
Sensor
Hub2_2
Sensor
Hub2_1
Sensor
Hub2_0
Table 443. SENSOR_HUB_2 register description
SensorHub2_[7:0] Second byte associated to external sensors
17.3 SENSOR_HUB_3 (04h)
Sensor hub output register (R)
Third byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 444. SENSOR_HUB_3 register
Sensor
Hub3_7
Sensor
Hub3_6
Sensor
Hub3_5
Sensor
Hub3_4
Sensor
Hub3_3
Sensor
Hub3_2
Sensor
Hub3_1
Sensor
Hub3_0
Table 445. SENSOR_HUB_3 register description
SensorHub3_[7:0] Third byte associated to external sensors
Sensor hub register description
17.4 SENSOR_HUB_4 (05h)
Sensor hub output register (R)
Fourth byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 446. SENSOR_HUB_4 register
Sensor
Hub4_7
Sensor
Hub4_6
Sensor
Hub4_5
Sensor
Hub4_4
Sensor
Hub4_3
Sensor
Hub4_2
Sensor
Hub4_1
Sensor
Hub4_0
Table 447. SENSOR_HUB_4 register description
SensorHub4_[7:0] Fourth byte associated to external sensors
17.5 SENSOR_HUB_5 (06h)
Sensor hub output register (R)
Fifth byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG number
of read operation configurations (for external sensors from x = 0 to x = 3).
Table 448. SENSOR_HUB_5 register
Sensor
Hub5_7
Sensor
Hub5_6
Sensor
Hub5_5
Sensor
Hub5_4
Sensor
Hub5_3
Sensor
Hub5_2
Sensor
Hub5_1
Sensor
Hub5_0
Table 449. SENSOR_HUB_5 register description
SensorHub5_[7:0] Fifth byte associated to external sensors
17.6 SENSOR_HUB_6 (07h)
Sensor hub output register (R)
Sixth byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 450. SENSOR_HUB_6 register
Sensor
Hub6_7
Sensor
Hub6_6
Sensor
Hub6_5
Sensor
Hub6_4
Sensor
Hub6_3
Sensor
Hub6_2
Sensor
Hub6_1
Sensor
Hub6_0
Table 451. SENSOR_HUB_6 register description
SensorHub6_[7:0] Sixth byte associated to external sensors
SENSOR_HUB_4 (05h)
17.7 SENSOR_HUB_7 (08h)
Sensor hub output register (R)
Seventh byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 452. SENSOR_HUB_7 register
Sensor
Hub7_7
Sensor
Hub7_6
Sensor
Hub7_5
Sensor
Hub7_4
Sensor
Hub7_3
Sensor
Hub7_2
Sensor
Hub7_1
Sensor
Hub7_0
Table 453. SENSOR_HUB_7 register description
SensorHub7_[7:0] Seventh byte associated to external sensors
17.8 SENSOR_HUB_8 (09h)
Sensor hub output register (R)
Eighth byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 454. SENSOR_HUB_8 register
Sensor
Hub8_7
Sensor
Hub8_6
Sensor
Hub8_5
Sensor
Hub8_4
Sensor
Hub8_3
Sensor
Hub8_2
Sensor
Hub8_1
Sensor
Hub8_0
Table 455. SENSOR_HUB_8 register description
SensorHub8_[7:0] Eighth byte associated to external sensors
17.9 SENSOR_HUB_9 (0Ah)
Sensor hub output register (R)
Ninth byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 456. SENSOR_HUB_9 register
Sensor
Hub9_7
Sensor
Hub9_6
Sensor
Hub9_5
Sensor
Hub9_4
Sensor
Hub9_3
Sensor
Hub9_2
Sensor
Hub9_1
Sensor
Hub9_0
Table 457. SENSOR_HUB_9 register description
SensorHub9_[7:0] Ninth byte associated to external sensors
SENSOR_HUB_7 (08h)
17.10 SENSOR_HUB_10 (0Bh)
Sensor hub output register (R)
Tenth byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 458. SENSOR_HUB_10 register
Sensor
Hub10_7
Sensor
Hub10_6
Sensor
Hub10_5
Sensor
Hub10_4
Sensor
Hub10_3
Sensor
Hub10_2
Sensor
Hub10_1
Sensor
Hub10_0
Table 459. SENSOR_HUB_10 register description
SensorHub10_[7:0] Tenth byte associated to external sensors
17.11 SENSOR_HUB_11 (0Ch)
Sensor hub output register (R)
Eleventh byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 460. SENSOR_HUB_11 register
Sensor
Hub11_7
Sensor
Hub11_6
Sensor
Hub11_5
Sensor
Hub11_4
Sensor
Hub11_3
Sensor
Hub11_2
Sensor
Hub11_1
Sensor
Hub11_0
Table 461. SENSOR_HUB_11 register description
SensorHub11_[7:0] Eleventh byte associated to external sensors
17.12 SENSOR_HUB_12 (0Dh)
Sensor hub output register (R)
Twelfth byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 462. SENSOR_HUB_12 register
Sensor
Hub12_7
Sensor
Hub12_6
Sensor
Hub12_5
Sensor
Hub12_4
Sensor
Hub12_3
Sensor
Hub12_2
Sensor
Hub12_1
Sensor
Hub12_0
Table 463. SENSOR_HUB_12 register description
SensorHub12_[7:0] Twelfth byte associated to external sensors
SENSOR_HUB_10 (0Bh)
17.13 SENSOR_HUB_13 (0Eh)
Sensor hub output register (R)
Thirteenth byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 464. SENSOR_HUB_13 register
Sensor
Hub13_7
Sensor
Hub13_6
Sensor
Hub13_5
Sensor
Hub13_4
Sensor
Hub13_3
Sensor
Hub13_2
Sensor
Hub13_1
Sensor
Hub13_0
Table 465. SENSOR_HUB_13 register description
SensorHub13_[7:0] Thirteenth byte associated to external sensors
17.14 SENSOR_HUB_14 (0Fh)
Sensor hub output register (R)
Fourteenth byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 466. SENSOR_HUB_14 register
Sensor
Hub14_7
Sensor
Hub14_6
Sensor
Hub14_5
Sensor
Hub14_4
Sensor
Hub14_3
Sensor
Hub14_2
Sensor
Hub14_1
Sensor
Hub14_0
Table 467. SENSOR_HUB_14 register description
SensorHub14_[7:0] Fourteenth byte associated to external sensors
17.15 SENSOR_HUB_15 (10h)
Sensor hub output register (R)
Fifteenth byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 468. SENSOR_HUB_15 register
Sensor
Hub15_7
Sensor
Hub15_6
Sensor
Hub15_5
Sensor
Hub15_4
Sensor
Hub15_3
Sensor
Hub15_2
Sensor
Hub15_1
Sensor
Hub15_0
Table 469. SENSOR_HUB_15 register description
SensorHub15_[7:0] Fifteenth byte associated to external sensors
SENSOR_HUB_13 (0Eh)
17.16 SENSOR_HUB_16 (11h)
Sensor hub output register (R)
Sixteenth byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 470. SENSOR_HUB_16 register
Sensor
Hub16_7
Sensor
Hub16_6
Sensor
Hub16_5
Sensor
Hub16_4
Sensor
Hub16_3
Sensor
Hub16_2
Sensor
Hub16_1
Sensor
Hub16_0
Table 471. SENSOR_HUB_16 register description
SensorHub16_[7:0] Sixteenth byte associated to external sensors
17.17 SENSOR_HUB_17 (12h)
Sensor hub output register (R)
Seventeenth byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 472. SENSOR_HUB_17 register
Sensor
Hub17_7
Sensor
Hub17_6
Sensor
Hub17_5
Sensor
Hub17_4
Sensor
Hub17_3
Sensor
Hub17_2
Sensor
Hub17_1
Sensor
Hub17_0
Table 473. SENSOR_HUB_17 register description
SensorHub17_[7:0] Seventeenth byte associated to external sensors
17.18 SENSOR_HUB_18 (13h)
Sensor hub output register (R)
Eighteenth byte associated to external sensors. The content of the register is consistent with the SLVx_CONFIG
number of read operation configurations (for external sensors from x = 0 to x = 3).
Table 474. SENSOR_HUB_17 register
Sensor
Hub18_7
Sensor
Hub18_6
Sensor
Hub18_5
Sensor
Hub18_4
Sensor
Hub18_3
Sensor
Hub18_2
Sensor
Hub18_1
Sensor
Hub18_0
Table 475. SENSOR_HUB_17 register description
SensorHub18_[7:0] Eighteenth byte associated to external sensors
SENSOR_HUB_16 (11h)
17.19 MASTER_CONFIG (14h)
Master configuration register (R/W)
Table 476. MASTER_CONFIG register
RST_MASTER
_REGS
WRITE_
ONCE
START_
CONFIG
PASS_
THROUGH_
MODE
0 (1) MASTER_ON
AUX_
SENS_ON1
AUX_
SENS_ON0
1. This bit must be set to 0 for the correct operation of the device.

Table 477. MASTER_CONFIG register description
RST_MASTER_REGS Resets master logic and output registers. Must be set to 1 and then set to 0. Default value: 0
WRITE_ONCE
Slave 0 write operation is performed only at the first sensor hub cycle.
Default value: 0
(0: write operation for each sensor hub cycle;
1: write operation only for the first sensor hub cycle)
START_CONFIG
Sensor hub trigger signal selection. Default value: 0
(0: sensor hub trigger signal is the accelerometer/gyro data-ready;
1: sensor hub trigger signal external from INT2 pin)
PASS_THROUGH_MODE
I²C interface pass-through. Default value: 0
(0: pass-through disabled;
1: pass-through enabled, primary I²C line is short-circuited with the sensor hub line)
MASTER_ON
Enables sensor hub I²C master. Default: 0
(0: master I²C of sensor hub disabled; 1: master I²C of sensor hub enabled)
AUX_SENS_ON[1:0]
Number of external sensors to be read by the sensor hub.
(00: one sensor (default);
01: two sensors;
10: three sensors;
11: four sensors)
MASTER_CONFIG (14h)
17.20 SLV0_ADD (15h)
I²C slave address of the first external sensor (sensor 0) register (R/W)
Table 478. SLV0_ADD register
slave0_add6 slave0_add5 slave0_add4 slave0_add3 slave0_add2 slave0_add1 slave0_add0 rw_0
Table 479. SLV_ADD register description
slave0_add[6:0]
I²C slave address of sensor 0 that can be read by the sensor hub.
Default value: 0000000
rw_0
Read/write operation on sensor 0. Default value: 0
(0: write operation; 1: read operation)
17.21 SLV0_SUBADD (16h)
Address of register on the first external sensor (sensor 0) register (R/W)
Table 480. SLV0_SUBADD register
slave0_reg7 slave0_reg6 slave0_reg5 slave0_reg4 slave0_reg3 slave0_reg2 slave0_reg1 slave0_reg0
Table 481. SLV0_SUBADD register description
slave0_reg[7:0]
Address of register on sensor 0 that has to be read/written according to the rw_0 bit value in SLV0_ADD
(15h). Default value: 00000000
17.22 SLV0_CONFIG (17h)
First external sensor (sensor 0) configuration and sensor hub settings register (R/W)
Table 482. SLV0_CONFIG register
SHUB_
ODR_2
SHUB_
ODR_1
SHUB_
ODR_0^0
(1) BATCH_EXT_
SENS_0_EN
Slave0_
numop2
Slave0_
numop1
Slave0_
numop0
1. This bit must be set to 0 for the correct operation of the device.

Table 483. SLV0_CONFIG register description
SHUB_ODR_[2:0]
Rate at which the master communicates.
(000: 1.875 Hz;
001: 15 Hz;
010: 30 Hz;
011: 60 Hz;
100: 120 Hz (default);
101: 240 Hz;
110: 480 Hz;
111: reserved
BATCH_EXT_SENS_0_EN Enables FIFO data batching of first slave. Default value: 0
Slave0_numop[2:0] Number of read operations on sensor 0. Default value: 000
SLV0_ADD (15h)
17.23 SLV1_ADD (18h)
I²C slave address of the second external sensor (sensor 1) register (R/W)
Table 484. SLV1_ADD register
Slave1_add6 Slave1_add5 Slave1_add4 Slave1_add3 Slave1_add2 Slave1_add1 Slave1_add0 r_1
Table 485. SLV1_ADD register description
Slave1_add[6:0]
I²C slave address of sensor 1 that can be read by the sensor hub.
Default value: 0000000
r_1
Enables read operation on sensor 1. Default value: 0
(0: read operation disabled; 1: read operation enabled)
17.24 SLV1_SUBADD (19h)
Address of register on the second external sensor (sensor 1) register (R/W)
Table 486. SLV1_SUBADD register
Slave1_reg7 Slave1_reg6 Slave1_reg5 Slave1_reg4 Slave1_reg3 Slave1_reg2 Slave1_reg1 Slave1_reg0
Table 487. SLV1_SUBADD register description
Slave1_reg[7:0] Address of register on sensor 1 that has to be read/written according to the r_1 bit value in SLV1_ADD (18h).
17.25 SLV1_CONFIG (1Ah)
Second external sensor (sensor 2) configuration register (R/W)
Table 488. SLV1_CONFIG register
0 (1) 0 (1) 0 (1) 1 (2) BATCH_EXT_SENS_1_EN Slave1_numop2 Slave1_numop1 Slave1_numop0
_1. This bit must be set to 0 for the correct operation of the device.

This bit must be set to 1 for the correct operation of the device._
Table 489. SLV1_CONFIG register description
BATCH_EXT_SENS_1_EN Enables FIFO data batching of second slave. Default value: 0
Slave1_numop[2:0] Number of read operations on sensor 2. Default value: 000
SLV1_ADD (18h)
17.26 SLV2_ADD (1Bh)
I²C slave address of the third external sensor (sensor 2) register (R/W)
Table 490. SLV2_ADD register
Slave2_add6 Slave2_add5 Slave2_add4 Slave2_add3 Slave2_add2 Slave2_add1 Slave2_add0 r_2
Table 491. SLV2_ADD register description
Slave2_add[6:0] I²C slave address of sensor 2 that can be read by the sensor hub.
r_2
Enables read operation on sensor 2. Default value: 0
(0: read operation disabled; 1: read operation enabled)
17.27 SLV2_SUBADD (1Ch)
Address of register on the third external sensor (sensor 2) register (R/W)
Table 492. SLV2_SUBADD register
Slave2_reg7 Slave2_reg6 Slave2_reg5 Slave2_reg4 Slave2_reg3 Slave2_reg2 Slave2_reg1 Slave2_reg0
Table 493. SLV2_SUBADD register description
Slave2_reg[7:0]
Address of register on sensor 2 that has to be read/written according to the r_2 bit value in SLV2_ADD
(1Bh).
17.28 SLV2_CONFIG (1Dh)
Third external sensor (sensor 2) configuration register (R/W)
Table 494. SLV2_CONFIG register
0 (1) 0 (1) 0 (1) 0 (1) BATCH_EXT_SENS_2_EN Slave2_numop2 Slave2_numop1 Slave2_numop0
1. This bit must be set to 0 for the correct operation of the device.

Table 495. SLV2_CONFIG register description
BATCH_EXT_SENS_2_EN Enables FIFO data batching of third slave. Default value: 0
Slave2_numop[2:0] Number of read operations on sensor 2. Default value: 000
SLV2_ADD (1Bh)
17.29 SLV3_ADD (1Eh)
I²C slave address of the fourth external sensor (sensor 3) register (R/W)
Table 496. SLV3_ADD register
Slave3_add6 Slave3_add5 Slave3_add4 Slave3_add3 Slave3_add2 Slave3_add1 Slave3_add0 r_3
Table 497. SLV3_ADD register description
Slave3_add[6:0] I²C slave address of sensor 3 that can be read by the sensor hub.
r_3
Enables read operation on sensor 3. Default value: 0
(0: read operation disabled; 1: read operation enabled)
17.30 SLV3_SUBADD (1Fh)
Address of register on the fourth external sensor (sensor 3) register (R/W)
Table 498. SLV3_SUBADD register
Slave3_reg7 Slave3_reg6 Slave3_reg5 Slave3_reg4 Slave3_reg3 Slave3_reg2 Slave3_reg1 Slave3_reg0
Table 499. SLV3_SUBADD register description
Slave3_reg[7:0] Address of register on sensor 3 that has to be read according to the r_3 bit value in SLV3_ADD (1Eh).
17.31 SLV3_CONFIG (20h)
Fourth external sensor (sensor 3) configuration register (R/W)
Table 500. SLV3_CONFIG register
0 (1) 0 (1) 0 (1) 0 (1)
BATCH_EXT
_SENS_3_EN
Slave3_
numop2
Slave3_
numop1
Slave3_
numop0
1. This bit must be set to 0 for the correct operation of the device.

Table 501. SLV3_CONFIG register description
BATCH_EXT_SENS_3_EN Enables FIFO data batching of fourth slave. Default value: 0
Slave3_numop[2:0] Number of read operations on sensor 3. Default value: 000
SLV3_ADD (1Eh)
17.32 DATAWRITE_SLV0 (21h)
Data to be written into the slave device register (R/W)
Table 502. DATAWRITE_SLV0 register
Slave0_
dataw7
Slave0_
dataw6
Slave0_
dataw5
Slave0_
dataw4
Slave0_
dataw3
Slave0_
dataw2
Slave0_
dataw1
Slave0_
dataw0
Table 503. DATAWRITE_SLV0 register description
Slave0_dataw[7:0]
Data to be written into the slave 0 device according to the rw_0 bit in register SLV0_ADD (15h).
Default value: 00000000
17.33 STATUS_MASTER (22h)
Sensor hub source register (R)
Table 504. STATUS_MASTER register
WR_ONCE
_DONE
SLAVE3_
NACK
SLAVE2_
NACK
SLAVE1_
NACK
SLAVE0_
NACK
0 0
SENS_HUB
_ENDOP
Table 505. STATUS_MASTER register description
WR_ONCE_DONE
When the bit WRITE_ONCE in MASTER_CONFIG (14h) is configured as 1, this bit is set to 1 when the
write operation on slave 0 has been performed and completed. Default value: 0
SLAVE3_NACK This bit is set to 1 if Not acknowledge occurs on slave 3 communication. Default value: 0
SLAVE2_NACK This bit is set to 1 if Not acknowledge occurs on slave 2 communication. Default value: 0
SLAVE1_NACK This bit is set to 1 if Not acknowledge occurs on slave 1 communication. Default value: 0
SLAVE0_NACK This bit is set to 1 if Not acknowledge occurs on slave 0 communication. Default value: 0
SENS_HUB_ENDOP
Sensor hub communication status. Default value: 0
(0: sensor hub communication not concluded;
1: sensor hub communication concluded)
DATAWRITE_SLV0 (21h)
18 Soldering information
The LGA package is compliant with the ECOPACK and RoHS standard.
It is qualified for soldering heat resistance according to JEDEC J-STD-020.
For land pattern and soldering recommendations, consult technical note TN0018 available on http://www.st.com.
Soldering information
19 Package information
In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK packages,
depending on their level of environmental compliance. ECOPACK specifications, grade definitions and product
status are available at: http://www.st.com. ECOPACK is an ST trademark.
19.1 LGA-14L package information
Figure 33. LGA-14L 2.5 x 3.0 x 0.86 mm package outline and mechanical data
W
L
H 4x (0.1)
14x 0.475±0.05
14x 0.25±0.05
0.5
0.5
Pin1 indicator
TOP VIEW BOTTOM VIEW
1.5
1
C
0.05 C
Pin 1 indicator
Dimensions are in millimeter unless otherwise specified
General tolerance is +/-0.1mm unless otherwise specified
OUTER DIMENSIONS
ITEM DIMENSION [mm] TOLERANCE [mm]
Length [L] 2. 50 ± 0. 1
Width [W] 3. 00 ± 0. 1
Height [H] 0. 86 MAX
DM00249496_5
Package information
19.2 LGA-14 packing information
Figure 34. Carrier tape information for LGA-14 package
Figure 35. LGA-14 package orientation in carrier tape
USER DIRECTION OF FEED
LGA-14 packing information
Figure 36. Reel information for carrier tape of LGA-14 package
A

D
B
Full radius
Tape slot
in core for
tape start
2.5mm min. width
G measured at hub
C
N
40mm min.
Access hole at
slot location
T
Table 506. Reel dimensions for carrier tape of LGA-14 package
Reel dimensions (mm)
A (max) 330
B (min) 1.5
C 13 ±0.25
D (min) 20.2
N (min) 60
G 12.4 +2/-0
T (max) 18.4
LGA-14 packing information
Revision history
Table 507. Document revision history
Date Revision Changes
15-Jul-2022 1 Initial release
18-Nov-2022 2
Minor textual updates
Added Section 2.8 Sensor fusion low power
Updated Section 6.5 High-accuracy ODR mode and added HAODR_CFG
(62h)
Added Section 6.6 ODR-triggered mode and ODR_TRIG_CFG (06h)
Minor update of registers in Section 9 Register description
01-Mar-2023 3 Added Note to Section 3.1 Pin connections
25-May-2023 4
Updated Section 2.1 Pedometer functions: step detector and step counters
Updated Note in Section 3.1 Pin connections
Updated footnotes of Table 3. Mechanical characteristics
Updated Section 6 Functionality
Updated Section 6.5 High-accuracy ODR mode
Updated registers in Section 9 Register description
Contents
1 Overview.......................................................................... 3
2 Embedded low-power features..................................................... 4
2.1 Pedometer functions: step detector and step counters............................... 4
2.2 Pedometer algorithm ........................................................... 5
2.3 Tilt detection................................................................... 5
2.4 Significant motion detection...................................................... 5
2.5 Finite state machine............................................................ 6
2.6 Machine learning core.......................................................... 7
2.7 Adaptive self-configuration (ASC)................................................. 7
2.8 Sensor fusion low power........................................................ 8
3 Pin description.................................................................... 9
3.1 Pin connections............................................................... 10
4 Module specifications............................................................ 12
4.1 Mechanical characteristics...................................................... 12
4.2 Electrical characteristics........................................................ 14
4.3 Temperature sensor characteristics.............................................. 15
4.4 Communication interface characteristics.......................................... 16
4.4.1 SPI - serial peripheral interface............................................. 16
4.4.2 I²C - inter-IC control interface.............................................. 18
4.5 Absolute maximum ratings...................................................... 19
4.6 Terminology.................................................................. 20
4.6.1 Sensitivity............................................................. 20
4.6.2 Zero- g and zero-rate level................................................. 20
5 Digital interfaces................................................................. 21
5.1 I²C/SPI interface.............................................................. 21
5.1.1 I²C serial interface....................................................... 21
5.1.2 I²C operation........................................................... 22
5.1.3 SPI bus interface........................................................ 24
5.2 MIPI I3C® interface............................................................ 27
5.2.1 MIPI I3C® slave interface................................................. 27
5.2.2 MIPI I3C® CCC supported commands....................................... 28
5.2.3 Overview of anti-spike filter management..................................... 29
5.3 Master I²C interface........................................................... 30
5.4 Auxiliary SPI interface.......................................................... 30
Contents
6 Functionality..................................................................... 31
6.1 Operating modes.............................................................. 31
6.2 Accelerometer power modes.................................................... 31
6.3 Accelerometer dual-channel mode............................................... 32
6.4 Gyroscope power modes....................................................... 33
6.5 High-accuracy ODR mode...................................................... 33
6.6 ODR-triggered mode .......................................................... 34
6.7 Analog hub functionality........................................................ 34
6.8 Qvar functionality.............................................................. 34
6.9 Block diagram of filters......................................................... 35
6.9.1 Block diagrams of the accelerometer filters.................................... 36
6.9.2 Block diagrams of the gyroscope filters....................................... 38
6.10 Enhanced EIS................................................................ 40
6.11 OIS ......................................................................... 41
6.11.1 Enabling OIS functionality and connection schemes............................. 41
6.12 FIFO........................................................................ 44
6.12.1 Bypass mode.......................................................... 44
6.12.2 FIFO mode............................................................ 45
6.12.3 Continuous mode....................................................... 45
6.12.4 Continuous-to-FIFO mode................................................. 45
6.12.5 ContinuousWTM-to-full mode.............................................. 45
6.12.6 Bypass-to-continuous mode............................................... 46
6.12.7 Bypass-to-FIFO mode.................................................... 46
6.12.8 FIFO reading procedure.................................................. 46
7 Application hints................................................................. 47
7.1 LSM6DSV16X electrical connections in mode 1.................................... 47
7.2 LSM6DSV16X electrical connections in mode 2.................................... 48
7.3 LSM6DSV16X electrical connections in mode 3.................................... 49
8 Register mapping................................................................. 52
9 Register description.............................................................. 56
9.1 FUNC_CFG_ACCESS (01h).................................................... 56
9.2 PIN_CTRL (02h).............................................................. 57
9.3 IF_CFG (03h)................................................................. 58
9.4 ODR_TRIG_CFG (06h)........................................................ 58
9.5 FIFO_CTRL1 (07h)............................................................ 59
9.6 FIFO_CTRL2 (08h)............................................................ 59
Contents
9.7 FIFO_CTRL3 (09h)............................................................ 60
9.8 FIFO_CTRL4 (0Ah)............................................................ 61
9.9 COUNTER_BDR_REG1 (0Bh).................................................. 62
9.10 COUNTER_BDR_REG2 (0Ch).................................................. 62
9.11 INT1_CTRL (0Dh)............................................................. 63
9.12 INT2_CTRL (0Eh)............................................................. 64
9.13 WHO_AM_I (0Fh)............................................................. 64
9.14 CTRL1 (10h)................................................................. 65
9.15 CTRL2 (11h)................................................................. 66
9.16 CTRL3 (12h)................................................................. 67
9.17 CTRL4 (13h)................................................................. 68
9.18 CTRL5 (14h)................................................................. 69
9.19 CTRL6 (15h)................................................................. 69
9.20 CTRL7 (16h)................................................................. 70
9.21 CTRL8 (17h)................................................................. 71
9.22 CTRL9 (18h)................................................................. 72
9.23 CTRL10 (19h)................................................................ 74
9.24 CTRL_STATUS (1Ah).......................................................... 74
9.25 FIFO_STATUS1 (1Bh)......................................................... 75
9.26 FIFO_STATUS2 (1Ch)......................................................... 75
9.27 ALL_INT_SRC (1Dh).......................................................... 76
9.28 STATUS_REG (1Eh)........................................................... 77
9.29 OUT_TEMP_L (20h), OUT_TEMP_H (21h)........................................ 78
9.30 OUTX_L_G (22h) and OUTX_H_G (23h)......................................... 78
9.31 OUTY_L_G (24h) and OUTY_H_G (25h)......................................... 79
9.32 OUTZ_L_G (26h) and OUTZ_H_G (27h).......................................... 79
9.33 OUTX_L_A (28h) and OUTX_H_A (29h).......................................... 80
9.34 OUTY_L_A (2Ah) and OUTY_H_A (2Bh)......................................... 80
9.35 OUTZ_L_A (2Ch) and OUTZ_H_A (2Dh)......................................... 81
9.36 UI_OUTX_L_G_OIS_EIS (2Eh) and UI_OUTX_H_G_OIS_EIS (2Fh).................. 81
9.37 UI_OUTY_L_G_OIS_EIS (30h) and UI_OUTY_H_G_OIS_EIS (31h).................. 82
9.38 UI_OUTZ_L_G_OIS_EIS (32h) and UI_OUTZ_H_G_OIS_EIS (33h).................. 82
9.39 UI_OUTX_L_A_OIS_DualC (34h) and UI_OUTX_H_A_OIS_DualC (35h).............. 83
9.40 UI_OUTY_L_A_OIS_DualC (36h) and UI_OUTY_H_A_OIS_DualC (37h).............. 83
9.41 UI_OUTZ_L_A_OIS_DualC (38h) and UI_OUTZ_H_A_OIS_DualC (39h).............. 84
9.42 AH_QVAR_OUT_L (3Ah) and AH_QVAR_OUT_H (3Bh)............................ 84
Contents
9.43 TIMESTAMP0 (40h), TIMESTAMP1 (41h), TIMESTAMP2 (42h), and TIMESTAMP3 (43h) 85
9.44 UI_STATUS_REG_OIS (44h)................................................... 85
9.45 WAKE_UP_SRC (45h)......................................................... 86
9.46 TAP_SRC (46h)............................................................... 87
9.47 D6D_SRC (47h).............................................................. 88
9.48 STATUS_MASTER_MAINPAGE (48h)............................................ 88
9.49 EMB_FUNC_STATUS_MAINPAGE (49h)......................................... 89
9.50 FSM_STATUS_MAINPAGE (4Ah) ............................................... 89
9.51 MLC_STATUS_MAINPAGE (4Bh) ............................................... 90
9.52 INTERNAL_FREQ_FINE (4Fh).................................................. 90
9.53 FUNCTIONS_ENABLE (50h)................................................... 91
9.54 DEN (51h)................................................................... 92
9.55 INACTIVITY_DUR (54h) ....................................................... 93
9.56 INACTIVITY_THS (55h)........................................................ 93
9.57 TAP_CFG0 (56h).............................................................. 94
9.58 TAP_CFG1 (57h).............................................................. 95
9.59 TAP_CFG2 (58h).............................................................. 95
9.60 TAP_THS_6D (59h)........................................................... 96
9.61 TAP_DUR (5Ah).............................................................. 97
9.62 WAKE_UP_THS (5Bh)......................................................... 97
9.63 WAKE_UP_DUR (5Ch)........................................................ 98
9.64 FREE_FALL (5Dh)............................................................ 98
9.65 MD1_CFG (5Eh).............................................................. 99
9.66 MD2_CFG (5Fh)............................................................. 100
9.67 HAODR_CFG (62h).......................................................... 100
9.68 EMB_FUNC_CFG (63h)....................................................... 101
9.69 UI_HANDSHAKE_CTRL (64h)................................................. 101
9.70 UI_SPI2_SHARED_0 (65h).................................................... 102
9.71 UI_SPI2_SHARED_1 (66h).................................................... 102
9.72 UI_SPI2_SHARED_2 (67h).................................................... 102
9.73 UI_SPI2_SHARED_3 (68h).................................................... 103
9.74 UI_SPI2_SHARED_4 (69h).................................................... 103
9.75 UI_SPI2_SHARED_5 (6Ah).................................................... 103
9.76 CTRL_EIS (6Bh)............................................................. 104
9.77 UI_INT_OIS (6Fh)............................................................ 105
9.78 UI_CTRL1_OIS (70h)......................................................... 106
Contents
9.79 UI_CTRL2_OIS (71h)......................................................... 107
9.80 UI_CTRL3_OIS (72h)......................................................... 108
9.81 X_OFS_USR (73h)........................................................... 109
9.82 Y_OFS_USR (74h)........................................................... 109
9.83 Z_OFS_USR (75h)........................................................... 109
9.84 FIFO_DATA_OUT_TAG (78h).................................................. 110
9.85 FIFO_DATA_OUT_X_L (79h) and FIFO_DATA_OUT_X_H (7Ah).................... 111
9.86 FIFO_DATA_OUT_Y_L (7Bh) and FIFO_DATA_OUT_Y_H (7Ch).................... 111
9.87 FIFO_DATA_OUT_Z_L (7Dh) and FIFO_DATA_OUT_Z_H (7Eh).................... 111
10 SPI2 register mapping.......................................................... 112
11 SPI2 register description........................................................ 113
11.1 SPI2_WHO_AM_I (0Fh)....................................................... 113
11.2 SPI2_STATUS_REG_OIS (1Eh)................................................ 113
11.3 SPI2_OUT_TEMP_L (20h) and SPI2_OUT_TEMP_H (21h)......................... 113
11.4 SPI2_OUTX_L_G_OIS (22h) and SPI2_OUTX_H_G_OIS (23h)..................... 114
11.5 SPI2_OUTY_L_G_OIS (24h) and SPI2_OUTY_H_G_OIS (25h)..................... 114
11.6 SPI2_OUTZ_L_G_OIS (26h) and SPI2_OUTZ_H_G_OIS (27h)..................... 115
11.7 SPI2_OUTX_L_A_OIS (28h) and SPI2_OUTX_H_A_OIS (29h) ..................... 115
11.8 SPI2_OUTY_L_A_OIS (2Ah) and SPI2_OUTY_H_A_OIS (2Bh)..................... 116
11.9 SPI2_OUTZ_L_A_OIS (2Ch) and SPI2_OUTZ_H_A_OIS (2Dh)..................... 116
11.10 SPI2_HANDSHAKE_CTRL (6Eh)............................................... 116
11.11 SPI2_INT_OIS (6Fh) ......................................................... 117
11.12 SPI2_CTRL1_OIS (70h)....................................................... 118
11.13 SPI2_CTRL2_OIS (71h)....................................................... 119
11.14 SPI2_CTRL3_OIS (72h)....................................................... 120
12 Embedded functions register mapping.......................................... 121
13 Embedded functions register description....................................... 123
13.1 PAGE_SEL (02h) ............................................................ 123
13.2 EMB_FUNC_EN_A (04h)...................................................... 123
13.3 EMB_FUNC_EN_B (05h)...................................................... 124
13.4 EMB_FUNC_EXEC_STATUS (07h)............................................. 124
13.5 PAGE_ADDRESS (08h)....................................................... 125
13.6 PAGE_VALUE (09h).......................................................... 125
13.7 EMB_FUNC_INT1 (0Ah)...................................................... 125
13.8 FSM_INT1 (0Bh)............................................................. 126
Contents
13.9 MLC_INT1 (0Dh)............................................................. 127
13.10 EMB_FUNC_INT2 (0Eh)...................................................... 127
13.11 FSM_INT2 (0Fh)............................................................. 128
13.12 MLC_INT2 (11h)............................................................. 129
13.13 EMB_FUNC_STATUS (12h)................................................... 129
13.14 FSM_STATUS (13h).......................................................... 130
13.15 MLC_STATUS (15h).......................................................... 130
13.16 PAGE_RW (17h)............................................................. 131
13.17 EMB_FUNC_FIFO_EN_A (44h)................................................ 131
13.18 EMB_FUNC_FIFO_EN_B (45h)................................................ 132
13.19 FSM_ENABLE (46h).......................................................... 132
13.20 FSM_LONG_COUNTER_L (48h) and FSM_LONG_COUNTER_H (49h).............. 133
13.21 INT_ACK_MASK (4Bh)....................................................... 134
13.22 FSM_OUTS1 (4Ch).......................................................... 135
13.23 FSM_OUTS2 (4Dh).......................................................... 135
13.24 FSM_OUTS3 (4Eh)........................................................... 136
13.25 FSM_OUTS4 (4Fh)........................................................... 136
13.26 FSM_OUTS5 (50h)........................................................... 137
13.27 FSM_OUTS6 (51h)........................................................... 137
13.28 FSM_OUTS7 (52h)........................................................... 138
13.29 FSM_OUTS8 (53h)........................................................... 138
13.30 SFLP_ODR (5Eh)............................................................ 139
13.31 FSM_ODR (5Fh)............................................................. 139
13.32 MLC_ODR (60h)............................................................. 140
13.33 STEP_COUNTER_L (62h) and STEP_COUNTER_H (63h)......................... 140
13.34 EMB_FUNC_SRC (64h)....................................................... 141
13.35 EMB_FUNC_INIT_A (66h)..................................................... 142
13.36 EMB_FUNC_INIT_B (67h)..................................................... 142
13.37 MLC1_SRC (70h)............................................................ 143
13.38 MLC2_SRC (71h)............................................................ 143
13.39 MLC3_SRC (72h)............................................................ 143
13.40 MLC4_SRC (73h)............................................................ 143
14 Embedded advanced features pages............................................ 144
15 Embedded advanced features register description.............................. 147
15.1 Page 0 - embedded advanced features registers.................................. 147
15.1.1 SFLP_GAME_GBIASX_L (6Eh) and SFLP_GAME_GBIASX_H (6Fh).............. 147
Contents
15.1.2 SFLP_GAME_GBIASY_L (70h) and SFLP_GAME_GBIASY_H (71h).............. 147
15.1.3 SFLP_GAME_GBIASZ_L (72h) and SFLP_GAME_GBIASZ_H (73h)............... 148
15.1.4 FSM_EXT_SENSITIVITY_L (BAh) and FSM_EXT_SENSITIVITY_H (BBh).......... 148
15.1.5 FSM_EXT_OFFX_L (C0h) and FSM_EXT_OFFX_H (C1h) ...................... 149
15.1.6 FSM_EXT_OFFY_L (C2h) and FSM_EXT_OFFY_H (C3h) ...................... 149
15.1.7 FSM_EXT_OFFZ_L (C4h) and FSM_EXT_OFFZ_H (C5h)....................... 150
15.1.8 FSM_EXT_MATRIX_XX_L (C6h) and FSM_EXT_MATRIX_XX_H (C7h)............ 150
15.1.9 FSM_EXT_MATRIX_XY_L (C8h) and FSM_EXT_MATRIX_XY_H (C9h)............ 151
15.1.10 FSM_EXT_MATRIX_XZ_L (CAh) and FSM_EXT_MATRIX_XZ_H (CBh)............ 151
15.1.11 FSM_EXT_MATRIX_YY_L (CCh) and FSM_EXT_MATRIX_YY_H (CDh)............ 152
15.1.12 FSM_EXT_MATRIX_YZ_L (CEh) and FSM_EXT_MATRIX_YZ_H (CFh)............ 152
15.1.13 FSM_EXT_MATRIX_ZZ_L (D0h) and FSM_EXT_MATRIX_ZZ_H (D1h) ............ 153
15.1.14 EXT_CFG_A (D4h)..................................................... 154
15.1.15 EXT_CFG_B (D5h)..................................................... 154
15.2 Page 1 - embedded advanced features registers.................................. 155
15.2.1 FSM_LC_TIMEOUT_L (7Ah) and FSM_LC_TIMEOUT_H (7Bh)................... 155
15.2.2 FSM_PROGRAMS (7Ch)................................................ 155
15.2.3 FSM_START_ADD_L (7Eh) and FSM_START_ADD_H (7Fh).................... 156
15.2.4 PEDO_CMD_REG (83h)................................................. 156
15.2.5 PEDO_DEB_STEPS_CONF (84h)......................................... 157
15.2.6 PEDO_SC_DELTAT_L (D0h) and PEDO_SC_DELTAT_H (D1h) .................. 157
15.2.7 MLC_EXT_SENSITIVITY_L (E8h) and MLC_EXT_SENSITIVITY_H (E9h) .......... 158
15.3 Page 2 - embedded advanced features registers.................................. 159
15.3.1 EXT_FORMAT (00h).................................................... 159
15.3.2 EXT_3BYTE_SENSITIVITY_L (02h) and EXT_3BYTE_SENSITIVITY_H (03h)....... 159
15.3.3 EXT_3BYTE_OFFSET_XL (06h), EXT_3BYTE_OFFSET_L (07h) and
EXT_3BYTE_OFFSET_H (08h)........................................... 160
16 Sensor hub register mapping................................................... 161
17 Sensor hub register description................................................. 162
17.1 SENSOR_HUB_1 (02h)....................................................... 162
17.2 SENSOR_HUB_2 (03h)....................................................... 162
17.3 SENSOR_HUB_3 (04h)....................................................... 162
17.4 SENSOR_HUB_4 (05h)....................................................... 163
17.5 SENSOR_HUB_5 (06h)....................................................... 163
17.6 SENSOR_HUB_6 (07h)....................................................... 163
17.7 SENSOR_HUB_7 (08h)....................................................... 164
17.8 SENSOR_HUB_8 (09h)....................................................... 164
Contents
17.9 SENSOR_HUB_9 (0Ah)....................................................... 164
17.10 SENSOR_HUB_10 (0Bh)...................................................... 165
17.11 SENSOR_HUB_11 (0Ch)...................................................... 165
17.12 SENSOR_HUB_12 (0Dh)...................................................... 165
17.13 SENSOR_HUB_13 (0Eh)...................................................... 166
17.14 SENSOR_HUB_14 (0Fh)...................................................... 166
17.15 SENSOR_HUB_15 (10h)...................................................... 166
17.16 SENSOR_HUB_16 (11h)...................................................... 167
17.17 SENSOR_HUB_17 (12h)...................................................... 167
17.18 SENSOR_HUB_18 (13h)...................................................... 167
17.19 MASTER_CONFIG (14h)...................................................... 168
17.20 SLV0_ADD (15h)............................................................. 169
17.21 SLV0_SUBADD (16h)......................................................... 169
17.22 SLV0_CONFIG (17h)......................................................... 169
17.23 SLV1_ADD (18h)............................................................. 170
17.24 SLV1_SUBADD (19h)......................................................... 170
17.25 SLV1_CONFIG (1Ah)......................................................... 170
17.26 SLV2_ADD (1Bh) ............................................................ 171
17.27 SLV2_SUBADD (1Ch)........................................................ 171
17.28 SLV2_CONFIG (1Dh)......................................................... 171
17.29 SLV3_ADD (1Eh) ............................................................ 172
17.30 SLV3_SUBADD (1Fh)......................................................... 172
17.31 SLV3_CONFIG (20h)......................................................... 172
17.32 DATAWRITE_SLV0 (21h)...................................................... 173
17.33 STATUS_MASTER (22h)...................................................... 173
18 Soldering information........................................................... 174
19 Package information............................................................ 175
19.1 LGA-14L package information.................................................. 175
19.2 LGA-14 packing information ................................................... 176
Revision history..................................................................... 178
List of tables........................................................................ 187
List of figures........................................................................ 197
Contents
List of tables
Table 1. Sensor fusion performance ............................................................ 8

Table 2. Pin description .................................................................... 11

Table 3. Mechanical characteristics ............................................................ 12

Table 4. Electrical characteristics.............................................................. 14

Table 5. Electrical parameters of Qvar (@Vdd = 1.8 V, T = 25 °C)....................................... 14

Table 6. Temperature sensor characteristics...................................................... 15

Table 7. SPI slave timing values............................................................... 16

Table 8. I²C slave timing values............................................................... 18

Table 9. Absolute maximum ratings............................................................ 19

Table 10. Serial interface pin description.......................................................... 21

Table 11. I²C terminology.................................................................... 21

Table 12. SAD+read/write patterns.............................................................. 22

Table 13. Transfer when master is writing one byte to slave............................................. 22

Table 14. Transfer when master is writing multiple bytes to slave......................................... 22

Table 15. Transfer when master is receiving (reading) one byte of data from slave............................. 22

Table 16. Transfer when master is receiving (reading) multiple bytes of data from slave......................... 22

Table 17. MIPI I3C® CCC commands............................................................ 28

Table 18. Master I²C pin details................................................................ 30

Table 19. Auxiliary SPI pin details.............................................................. 30

Table 20. Accelerometer and gyroscope ODR selection in high-accuracy ODR mode........................... 33

Table 21. Gyroscope LPF2 bandwidth selection..................................................... 38

Table 22. OIS configurations.................................................................. 41

Table 23. Internal pin status.................................................................. 50

Table 24. Registers address map............................................................... 52

Table 25. FUNC_CFG_ACCESS register......................................................... 56

Table 26. FUNC_CFG_ACCESS register description................................................. 56

Table 27. PIN_CTRL register.................................................................. 57

Table 28. PIN_CTRL register description......................................................... 57

Table 29. IF_CFG register.................................................................... 58

Table 30. IF_CFG register description............................................................ 58

Table 31. ODR_TRIG_CFG register............................................................. 58

Table 32. ODR_TRIG_CFG register description..................................................... 58

Table 33. FIFO_CTRL1 register................................................................ 59

Table 34. FIFO_CTRL1 register description........................................................ 59

Table 35. FIFO_CTRL2 register................................................................ 59

Table 36. FIFO_CTRL2 register description........................................................ 59

Table 37. FIFO_CTRL3 register................................................................ 60

Table 38. FIFO_CTRL3 register description........................................................ 60

Table 39. FIFO_CTRL4 register................................................................ 61

Table 40. FIFO_CTRL4 register description........................................................ 61

Table 41. COUNTER_BDR_REG1 register........................................................ 62

Table 42. COUNTER_BDR_REG1 register description................................................ 62

Table 43. COUNTER_BDR_REG2 register........................................................ 62

Table 44. COUNTER_BDR_REG2 register description................................................ 62

Table 45. INT1_CTRL register................................................................. 63

Table 46. INT1_CTRL register description......................................................... 63

Table 47. INT2_CTRL register................................................................. 64

Table 48. INT2_CTRL register description......................................................... 64

Table 49. WhoAmI register................................................................... 64

Table 50. CTRL1 register.................................................................... 65

Table 51. CTRL1 register description............................................................ 65

Table 52. Accelerometer ODR selection.......................................................... 65

Table 53. CTRL2 register.................................................................... 66

List of tables
Table 54. CTRL2 register description............................................................ 66

Table 55. Gyroscope ODR selection............................................................. 66

Table 56. CTRL3 register.................................................................... 67

Table 57. CTRL3 register description............................................................ 67

Table 58. CTRL4 register.................................................................... 68

Table 59. CTRL4 register description............................................................ 68

Table 60. CTRL5 register.................................................................... 69

Table 61. CTRL5 register description............................................................ 69

Table 62. CTRL6 register.................................................................... 69

Table 63. CTRL6 register description............................................................ 69

Table 64. Gyroscope LPF1 + LPF2 bandwidth selection............................................... 70

Table 65. CTRL7 register.................................................................... 70

Table 66. CTRL7 register description............................................................ 70

Table 67. CTRL8 register.................................................................... 71

Table 68. CTRL8 register description............................................................ 71

Table 69. Accelerometer bandwidth configurations................................................... 71

Table 70. CTRL9 register.................................................................... 72

Table 71. CTRL9 register description............................................................ 72

Table 72. CTRL10 register................................................................... 74

Table 73. CTRL10 register description........................................................... 74

Table 74. CTRL_STATUS register.............................................................. 74

Table 75. CTRL_STATUS register description...................................................... 74

Table 76. FIFO_STATUS1 register.............................................................. 75

Table 77. FIFO_STATUS1 register description...................................................... 75

Table 78. FIFO_STATUS2 register.............................................................. 75

Table 79. FIFO_STATUS2 register description...................................................... 75

Table 80. ALL_INT_SRC register............................................................... 76

Table 81. ALL_INT_SRC register description....................................................... 76

Table 82. STATUS_REG register............................................................... 77

Table 83. STATUS_REG register description....................................................... 77

Table 84. OUT_TEMP_L register............................................................... 78

Table 85. OUT_TEMP_H register............................................................... 78

Table 86. OUT_TEMP register description......................................................... 78

Table 87. OUTX_L_G register................................................................. 78

Table 88. OUTX_H_G register................................................................. 78

Table 89. OUTX_G register description........................................................... 78

Table 90. OUTY_L_G register................................................................. 79

Table 91. OUTY_H_G register................................................................. 79

Table 92. OUTY_G register description........................................................... 79

Table 93. OUTZ_L_G register................................................................. 79

Table 94. OUTZ_H_G register................................................................. 79

Table 95. OUTZ_H_G register description......................................................... 79

Table 96. OUTX_L_A register................................................................. 80

Table 97. OUTX_H_A register................................................................. 80

Table 98. OUTX_A register description........................................................... 80

Table 99. OUTY_L_A register................................................................. 80

Table 100. OUTY_H_A register................................................................. 80

Table 101. OUTY_A register description........................................................... 80

Table 102. OUTZ_L_A register................................................................. 81

Table 103. OUTZ_H_A register................................................................. 81

Table 104. OUTZ_A register description........................................................... 81

Table 105. UI_OUTX_L_G_OIS_EIS register....................................................... 81

Table 106. UI_OUTX_H_G_OIS_EIS register....................................................... 81

Table 107. UI_OUTX_G_OIS_EIS register description................................................. 81

Table 108. UI_OUTY_L_G_OIS_EIS register....................................................... 82

List of tables
Table 109. UI_OUTY_H_G_OIS_EIS register....................................................... 82

Table 110. UI_OUTY_G_OIS_EIS register description................................................. 82

Table 111. UI_OUTZ_L_G_OIS_EIS register........................................................ 82

Table 112. UI_OUTZ_H_G_OIS_EIS register....................................................... 82

Table 113. UI_OUTZ_G_OIS_EIS register description................................................. 82

Table 114. UI_OUTX_L_A_OIS_DualC register...................................................... 83

Table 115. UI_OUTX_H_A_OIS_DualC register...................................................... 83

Table 116. UI_OUTX_A_OIS_DualC register description............................................... 83

Table 117. UI_OUTY_L_A_OIS_DualC register...................................................... 83

Table 118. UI_OUTY_H_A_OIS_DualC register...................................................... 83

Table 119. UI_OUTY_A_OIS_DualC register description............................................... 83

Table 120. UI_OUTZ_L_A_OIS_DualC register...................................................... 84

Table 121. UI_OUTZ_H_A_OIS_DualC register...................................................... 84

Table 122. UI_OUTZ_A_OIS_DualC register description................................................ 84

Table 123. AH_QVAR_OUT_L register............................................................ 84

Table 124. AH_QVAR_OUT_H register............................................................ 84

Table 125. AH_QVAR_OUT register description..................................................... 84

Table 126. TIMESTAMP output registers .......................................................... 85

Table 127. TIMESTAMP output register description................................................... 85

Table 128. UI_STATUS_REG_OIS register......................................................... 85

Table 129. UI_STATUS_REG_OIS register description................................................. 85

Table 130. WAKE_UP_SRC register............................................................. 86

Table 131. WAKE_UP_SRC register description..................................................... 86

Table 132. TAP_SRC register.................................................................. 87

Table 133. TAP_SRC register description.......................................................... 87

Table 134. D6D_SRC register.................................................................. 88

Table 135. D6D_SRC register description.......................................................... 88

Table 136. STATUS_MASTER_MAINPAGE register................................................... 88

Table 137. STATUS_MASTER_MAINPAGE register description.......................................... 88

Table 138. EMB_FUNC_STATUS_MAINPAGE register................................................ 89

Table 139. EMB_FUNC_STATUS_MAINPAGE register description........................................ 89

Table 140. FSM_STATUS_MAINPAGE register...................................................... 89

Table 141. FSM_STATUS_MAINPAGE register description.............................................. 89

Table 142. MLC_STATUS _MAINPAGE register..................................................... 90

Table 143. MLC_STATUS_MAINPAGE register description.............................................. 90

Table 144. INTERNAL_FREQ_FINE register........................................................ 90

Table 145. INTERNAL_FREQ_FINE register description................................................ 90

Table 146. ODRcoeff values.................................................................... 90

Table 147. FUNCTIONS_ENABLE register......................................................... 91

Table 148. FUNCTIONS_ENABLE register description................................................. 91

Table 149. DEN register...................................................................... 92

Table 150. DEN register description.............................................................. 92

Table 151. Trigger mode selection............................................................... 92

Table 152. INACTIVITY_DUR register............................................................ 93

Table 153. INACTIVITY_DUR register description.................................................... 93

Table 154. INACTIVITY_THS register............................................................ 93

Table 155. INACTIVITY_THS register description.................................................... 93

Table 156. TAP_CFG0 register................................................................. 94

Table 157. TAP_CFG0 register description......................................................... 94

Table 158. TAP_CFG1 register................................................................. 95

Table 159. TAP_CFG1 register description......................................................... 95

Table 160. TAP priority decoding................................................................ 95

Table 161. TAP_CFG2 register................................................................. 95

Table 162. TAP_CFG2 register description......................................................... 95

Table 163. TAP_THS_6D register............................................................... 96

List of tables
Table 164. TAP_THS_6D register description....................................................... 96

Table 165. Threshold for D4D/D6D function........................................................ 96

Table 166. TAP_DUR register.................................................................. 97

Table 167. TAP_DUR register description.......................................................... 97

Table 168. WAKE_UP_THS register.............................................................. 97

Table 169. WAKE_UP_THS register description..................................................... 97

Table 170. WAKE_UP_DUR register............................................................. 98

Table 171. WAKE_UP_DUR register description..................................................... 98

Table 172. FREE_FALL register................................................................ 98

Table 173. FREE_FALL register description........................................................ 98

Table 174. Threshold for free-fall function.......................................................... 98

Table 175. MD1_CFG register.................................................................. 99

Table 176. MD1_CFG register description.......................................................... 99

Table 177. MD2_CFG register................................................................. 100

Table 178. MD2_CFG register description......................................................... 100

Table 179. HAODR_CFG register.............................................................. 100

Table 180. HAODR_CFG register description...................................................... 100

Table 181. EMB_FUNC_CFG register........................................................... 101

Table 182. EMB_FUNC_CFG register description................................................... 101

Table 183. UI_HANDSHAKE_CTRL register....................................................... 101

Table 184. UI_HANDSHAKE_CTRL register description............................................... 101

Table 185. UI_SPI2_SHARED_0 register......................................................... 102

Table 186. UI_SPI2_SHARED_0 register description................................................. 102

Table 187. UI_SPI2_SHARED_1 register......................................................... 102

Table 188. UI_SPI2_SHARED_1 register description................................................. 102

Table 189. UI_SPI2_SHARED_2 register......................................................... 102

Table 190. UI_SPI2_SHARED_2 register description................................................. 102

Table 191. UI_SPI2_SHARED_3 register......................................................... 103

Table 192. UI_SPI2_SHARED_3 register description................................................. 103

Table 193. UI_SPI2_SHARED_4 register......................................................... 103

Table 194. UI_SPI2_SHARED_4 register description................................................. 103

Table 195. UI_SPI2_SHARED_5 register......................................................... 103

Table 196. UI_SPI2_SHARED_5 register description................................................. 103

Table 197. CTRL_EIS register................................................................. 104

Table 198. CTRL_EIS register description......................................................... 104

Table 199. Gyroscope EIS chain digital LPF_EIS filter bandwidth selection.................................. 104

Table 200. UI_INT_OIS register................................................................ 105

Table 201. UI_INT_OIS register description........................................................ 105

Table 202. UI_CTRL1_OIS register............................................................. 106

Table 203. UI_CTRL1_OIS register description..................................................... 106

Table 204. UI_CTRL2_OIS register............................................................. 107

Table 205. UI_CTRL2_OIS register description..................................................... 107

Table 206. Gyroscope OIS chain digital LPF1 filter bandwidth selection.................................... 107

Table 207. UI_CTRL3_OIS register............................................................. 108

Table 208. UI_CTRL3_OIS register description..................................................... 108

Table 209. Accelerometer OIS channel bandwidth and phase........................................... 108

Table 210. X_OFS_USR register............................................................... 109

Table 211. X_OFS_USR register description....................................................... 109

Table 212. Y_OFS_USR register............................................................... 109

Table 213. Y_OFS_USR register description....................................................... 109

Table 214. Z_OFS_USR register............................................................... 109

Table 215. Z_OFS_USR register description....................................................... 109

Table 216. FIFO_DATA_OUT_TAG register......................................................... 110

Table 217. FIFO_DATA_OUT_TAG register description................................................ 110

Table 218. FIFO tag......................................................................... 110

List of tables
Table 219. FIFO_DATA_OUT_X_H and FIFO_DATA_OUT_X_L registers.................................... 111

Table 220. FIFO_DATA_OUT_X_H and FIFO_DATA_OUT_X_L register description ............................ 111

Table 221. FIFO_DATA_OUT_Y_H and FIFO_DATA_OUT_Y_L registers.................................... 111

Table 222. FIFO_DATA_OUT_Y_H and FIFO_DATA_OUT_Y_L register description ............................ 111

Table 223. FIFO_DATA_OUT_Z_H and FIFO_DATA_OUT_Z_L registers.................................... 111

Table 224. FIFO_DATA_OUT_Z_H and FIFO_DATA_OUT_Z_L register description............................. 111

Table 225. SPI2 register address map............................................................ 112

Table 226. SPI2_WhoAmI register............................................................... 113

Table 227. SPI2_STATUS_REG_OIS register....................................................... 113

Table 228. SPI2_STATUS_REG_OIS description..................................................... 113

Table 229. SPI2_OUT_TEMP_L register........................................................... 113

Table 230. SPI2_OUT_TEMP_H register.......................................................... 113

Table 231. SPI2_OUT_TEMP register description.................................................... 113

Table 232. SPI2_OUTX_L_G_OIS register......................................................... 114

Table 233. SPI2_OUTX_H_G_OIS register......................................................... 114

Table 234. SPI2_OUTX_H_G_OIS register description................................................. 114

Table 235. SPI2_OUTY_L_G_OIS register......................................................... 114

Table 236. SPI2_OUTY_H_G_OIS register......................................................... 114

Table 237. SPI2_OUTY_H_G_OIS register description................................................. 114

Table 238. SPI2_OUTZ_L_G_OIS register......................................................... 115

Table 239. SPI2_OUTZ_H_G_OIS register......................................................... 115

Table 240. SPI2_OUTZ_H_G_OIS register description................................................. 115

Table 241. SPI2_OUTX_L_A_OIS register......................................................... 115

Table 242. SPI2_OUTX_H_A_OIS register......................................................... 115

Table 243. SPI2_OUTX_H_A_OIS register description................................................. 115

Table 244. SPI2_OUTY_L_A_OIS register......................................................... 116

Table 245. SPI2_OUTY_H_A_OIS register......................................................... 116

Table 246. SPI2_OUTY_H_A_OIS register description................................................. 116

Table 247. SPI2_OUTZ_L_A_OIS register......................................................... 116

Table 248. SPI2_OUTZ_H_A_OIS register......................................................... 116

Table 249. SPI2_OUTZ_H_A_OIS register description................................................. 116

Table 250. SPI2_HANDSHAKE_CTRL register...................................................... 116

Table 251. SPI2_HANDSHAKE_CTRL register description.............................................. 116

Table 252. SPI2_INT_OIS register............................................................... 117

Table 253. SPI2_INT_OIS register description....................................................... 117

Table 254. SPI2_CTRL1_OIS register............................................................ 118

Table 255. SPI2_CTRL1_OIS register description.................................................... 118

Table 256. SPI2_CTRL2_OIS register............................................................ 119

Table 257. SPI2_CTRL2_OIS register description.................................................... 119

Table 258. Gyroscope OIS chain digital LPF1 filter bandwidth selection..................................... 119

Table 259. SPI2_CTRL3_OIS register........................................................... 120

Table 260. SPI2_CTRL3_OIS register description................................................... 120

Table 261. Accelerometer OIS channel bandwidth and phase........................................... 120

Table 262. Register address map - embedded functions............................................... 121

Table 263. PAGE_SEL register................................................................ 123

Table 264. PAGE_SEL register description........................................................ 123

Table 265. EMB_FUNC_EN_A register........................................................... 123

Table 266. EMB_FUNC_EN_A register description.................................................. 123

Table 267. EMB_FUNC_EN_B register........................................................... 124

Table 268. EMB_FUNC_EN_B register description.................................................. 124

Table 269. EMB_FUNC_EXEC_STATUS register................................................... 124

Table 270. EMB_FUNC_EXEC_STATUS register description........................................... 124

Table 271. PAGE_ADDRESS register........................................................... 125

Table 272. PAGE_ADDRESS register description................................................... 125

Table 273. PAGE_VALUE register.............................................................. 125

List of tables
Table 274. PAGE_VALUE register description...................................................... 125

Table 275. EMB_FUNC_INT1 register........................................................... 125

Table 276. EMB_FUNC_INT1 register description................................................... 125

Table 277. FSM_INT1 register................................................................. 126

Table 278. FSM_INT1 register description........................................................ 126

Table 279. MLC_INT1 register................................................................. 127

Table 280. MLC_INT1 register description........................................................ 127

Table 281. EMB_FUNC_INT2 register........................................................... 127

Table 282. EMB_FUNC_INT2 register description................................................... 127

Table 283. FSM_INT2 register................................................................. 128

Table 284. FSM_INT2 register description........................................................ 128

Table 285. MLC_INT2 register................................................................. 129

Table 286. MLC_INT2 register description........................................................ 129

Table 287. EMB_FUNC_STATUS register......................................................... 129

Table 288. EMB_FUNC_STATUS register description................................................. 129

Table 289. FSM_STATUS register.............................................................. 130

Table 290. FSM_STATUS register description...................................................... 130

Table 291. MLC_STATUS register.............................................................. 130

Table 292. MLC_STATUS register description...................................................... 130

Table 293. PAGE_RW register................................................................ 131

Table 294. PAGE_RW register description........................................................ 131

Table 295. EMB_FUNC_FIFO_EN_A register...................................................... 131

Table 296. EMB_FUNC_FIFO_EN_A register description.............................................. 131

Table 297. EMB_FUNC_FIFO_EN_B register...................................................... 132

Table 298. EMB_FUNC_FIFO_EN_B register description.............................................. 132

Table 299. FSM_ENABLE register.............................................................. 132

Table 300. FSM_ENABLE register description...................................................... 132

Table 301. FSM_LONG_COUNTER_L register..................................................... 133

Table 302. FSM_LONG_COUNTER_L register description............................................. 133

Table 303. FSM_LONG_COUNTER_H register..................................................... 133

Table 304. FSM_LONG_COUNTER_H register description............................................. 133

Table 305. INT_ACK_MASK register............................................................ 134

Table 306. INT_ACK_MASK register description.................................................... 134

Table 307. FSM_OUTS1 register............................................................... 135

Table 308. FSM_OUTS1 register description....................................................... 135

Table 309. FSM_OUTS2 register............................................................... 135

Table 310. FSM_OUTS2 register description....................................................... 135

Table 311. FSM_OUTS3 register............................................................... 136

Table 312. FSM_OUTS3 register description....................................................... 136

Table 313. FSM_OUTS4 register............................................................... 136

Table 314. FSM_OUTS4 register description....................................................... 136

Table 315. FSM_OUTS5 register............................................................... 137

Table 316. FSM_OUTS5 register description....................................................... 137

Table 317. FSM_OUTS6 register............................................................... 137

Table 318. FSM_OUTS6 register description....................................................... 137

Table 319. FSM_OUTS7 register............................................................... 138

Table 320. FSM_OUTS7 register description....................................................... 138

Table 321. FSM_OUTS8 register............................................................... 138

Table 322. FSM_OUTS8 register description....................................................... 138

Table 323. SFLP_ODR register................................................................ 139

Table 324. SFLP_ODR register description........................................................ 139

Table 325. FSM_ODR register................................................................. 139

Table 326. FSM_ODR register description........................................................ 139

Table 327. MLC_ODR register................................................................. 140

Table 328. MLC_ODR register description........................................................ 140

List of tables
Table 329. STEP_COUNTER_L register.......................................................... 140

Table 330. STEP_COUNTER_L register description.................................................. 140

Table 331. STEP_COUNTER_H register......................................................... 140

Table 332. STEP_COUNTER_H register description................................................. 140

Table 333. EMB_FUNC_SRC register........................................................... 141

Table 334. EMB_FUNC_SRC register description................................................... 141

Table 335. EMB_FUNC_INIT_A register.......................................................... 142

Table 336. EMB_FUNC_INIT_A register description.................................................. 142

Table 337. EMB_FUNC_INIT_B register.......................................................... 142

Table 338. EMB_FUNC_INIT_B register description.................................................. 142

Table 339. MLC1_SRC register................................................................ 143

Table 340. MLC1_SRC register description........................................................ 143

Table 341. MLC2_SRC register................................................................ 143

Table 342. MLC2_SRC register description........................................................ 143

Table 343. MLC3_SRC register................................................................ 143

Table 344. MLC3_SRC register description........................................................ 143

Table 345. MLC4_SRC register................................................................ 143

Table 346. MLC4_SRC register description........................................................ 143

Table 347. Register address map - embedded advanced features page 0................................... 144

Table 348. Register address map - embedded advanced features page 1................................... 145

Table 349. Register address map - embedded advanced features page 2................................... 145

Table 350. SFLP_GAME_GBIASX_L register...................................................... 147

Table 351. SFLP_GAME_GBIASX_L register description.............................................. 147

Table 352. SFLP_GAME_GBIASX_H register...................................................... 147

Table 353. SFLP_GAME_GBIASX_H register description.............................................. 147

Table 354. SFLP_GAME_GBIASY_L register...................................................... 147

Table 355. SFLP_GAME_GBIASY_L register description.............................................. 147

Table 356. SFLP_GAME_GBIASY_H register...................................................... 147

Table 357. SFLP_GAME_GBIASY_H register description.............................................. 147

Table 358. SFLP_GAME_GBIASZ_L register...................................................... 148

Table 359. SFLP_GAME_GBIASZ_L register description.............................................. 148

Table 360. SFLP_GAME_GBIASZ_H register...................................................... 148

Table 361. SFLP_GAME_GBIASZ_H register description.............................................. 148

Table 362. FSM_EXT_SENSITIVITY_L register..................................................... 148

Table 363. FSM_EXT_SENSITIVITY_L register description............................................ 148

Table 364. FSM_EXT_SENSITIVITY_H register.................................................... 148

Table 365. FSM_EXT_SENSITIVITY_H register description............................................ 148

Table 366. FSM_EXT_OFFX_L register.......................................................... 149

Table 367. FSM_EXT_OFFX_L register description.................................................. 149

Table 368. FSM_EXT_OFFX_H register.......................................................... 149

Table 369. FSM_EXT_OFFX_H register description.................................................. 149

Table 370. FSM_EXT_OFFY_L register.......................................................... 149

Table 371. FSM_EXT_OFFY_L register description.................................................. 149

Table 372. FSM_EXT_OFFY_H register.......................................................... 149

Table 373. FSM_EXT_OFFY_H register description.................................................. 149

Table 374. FSM_EXT_OFFZ_L register.......................................................... 150

Table 375. FSM_EXT_OFFZ_L register description.................................................. 150

Table 376. FSM_EXT_OFFZ_H register.......................................................... 150

Table 377. FSM_EXT_OFFZ_H register description.................................................. 150

Table 378. FSM_EXT_MATRIX_XX_L register..................................................... 150

Table 379. FSM_EXT_MATRIX_XX_L register description............................................. 150

Table 380. FSM_EXT_MATRIX_XX_H register..................................................... 150

Table 381. FSM_EXT_MATRIX_XX_H register description............................................. 150

Table 382. FSM_EXT_MATRIX_XY_L register..................................................... 151

Table 383. FSM_EXT_MATRIX_XY_L register description............................................. 151

List of tables
Table 384. FSM_EXT_MATRIX_XY_H register..................................................... 151

Table 385. FSM_EXT_MATRIX_XY_H register description............................................. 151

Table 386. FSM_EXT_MATRIX_XZ_L register...................................................... 151

Table 387. FSM_EXT_MATRIX_XZ_L register description............................................. 151

Table 388. FSM_EXT_MATRIX_XZ_H register..................................................... 151

Table 389. FSM_EXT_MATRIX_XZ_H register description............................................. 151

Table 390. FSM_EXT_MATRIX_YY_L register..................................................... 152

Table 391. FSM_EXT_MATRIX_YY_L register description............................................. 152

Table 392. FSM_EXT_MATRIX_YY_H register..................................................... 152

Table 393. FSM_EXT_MATRIX_YY_H register description............................................. 152

Table 394. FSM_EXT_MATRIX_YZ_L register...................................................... 152

Table 395. FSM_EXT_MATRIX_YZ_L register description............................................. 152

Table 396. FSM_EXT_MATRIX_YZ_H register..................................................... 152

Table 397. FSM_EXT_MATRIX_YZ_H register description............................................. 152

Table 398. FSM_EXT_MATRIX_ZZ_L register...................................................... 153

Table 399. FSM_EXT_MATRIX_ZZ_L register description ............................................. 153

Table 400. FSM_EXT_MATRIX_ZZ_H register..................................................... 153

Table 401. FSM_EXT_MATRIX_ZZ_H register description............................................. 153

Table 402. EXT_CFG_A register............................................................... 154

Table 403. EXT_CFG_A description............................................................. 154

Table 404. EXT_CFG_B register............................................................... 154

Table 405. EXT_CFG_B description............................................................. 154

Table 406. FSM_LC_TIMEOUT_L register........................................................ 155

Table 407. FSM_LC_TIMEOUT_L register description................................................ 155

Table 408. FSM_LC_TIMEOUT_H register........................................................ 155

Table 409. FSM_LC_TIMEOUT_H register description................................................ 155

Table 410. FSM_PROGRAMS register........................................................... 155

Table 411. FSM_PROGRAMS register description................................................... 155

Table 412. FSM_START_ADD_L register......................................................... 156

Table 413. FSM_START_ADD_L register description................................................. 156

Table 414. FSM_START_ADD_H register......................................................... 156

Table 415. FSM_START_ADD_H register description................................................. 156

Table 416. PEDO_CMD_REG register........................................................... 156

Table 417. PEDO_CMD_REG register description................................................... 156

Table 418. PEDO_DEB_STEPS_CONF register.................................................... 157

Table 419. PEDO_DEB_STEPS_CONF register description............................................ 157

Table 420. PEDO_SC_DELTAT_L register........................................................ 157

Table 421. PEDO_SC_DELTAT_H register........................................................ 157

Table 422. PEDO_SC_DELTAT_H/L register description............................................... 157

Table 423. MLC_EXT_SENSITIVITY_L register..................................................... 158

Table 424. MLC_ EXT_SENSITIVITY_L register description............................................ 158

Table 425. MLC_EXT_SENSITIVITY_H register.................................................... 158

Table 426. MLC_EXT_SENSITIVITY_H register description............................................ 158

Table 427. EXT_FORMAT register.............................................................. 159

Table 428. EXT_FORMAT register description...................................................... 159

Table 429. EXT_3BYTE_SENSITIVITY_L register................................................... 159

Table 430. EXT_3BYTE_SENSITIVITY_L register description........................................... 159

Table 431. EXT_3BYTE_SENSITIVITY_H register................................................... 159

Table 432. EXT_3BYTE_SENSITIVITY_H register description........................................... 159

Table 433. EXT_3BYTE_OFFSET_XL register..................................................... 160

Table 434. EXT_3BYTE_OFFSET_XL register description............................................. 160

Table 435. EXT_3BYTE_OFFSET_L register...................................................... 160

Table 436. EXT_3BYTE_OFFSET_L register description.............................................. 160

Table 437. EXT_3BYTE_OFFSET_H register...................................................... 160

Table 438. EXT_3BYTE_OFFSET_H register description.............................................. 160

List of tables
Table 439. Register address map - sensor hub registers............................................... 161

Table 440. SENSOR_HUB_1 register............................................................ 162

Table 441. SENSOR_HUB_1 register description................................................... 162

Table 442. SENSOR_HUB_2 register............................................................ 162

Table 443. SENSOR_HUB_2 register description................................................... 162

Table 444. SENSOR_HUB_3 register............................................................ 162

Table 445. SENSOR_HUB_3 register description................................................... 162

Table 446. SENSOR_HUB_4 register............................................................ 163

Table 447. SENSOR_HUB_4 register description................................................... 163

Table 448. SENSOR_HUB_5 register............................................................ 163

Table 449. SENSOR_HUB_5 register description................................................... 163

Table 450. SENSOR_HUB_6 register............................................................ 163

Table 451. SENSOR_HUB_6 register description................................................... 163

Table 452. SENSOR_HUB_7 register............................................................ 164

Table 453. SENSOR_HUB_7 register description................................................... 164

Table 454. SENSOR_HUB_8 register............................................................ 164

Table 455. SENSOR_HUB_8 register description................................................... 164

Table 456. SENSOR_HUB_9 register............................................................ 164

Table 457. SENSOR_HUB_9 register description................................................... 164

Table 458. SENSOR_HUB_10 register........................................................... 165

Table 459. SENSOR_HUB_10 register description................................................... 165

Table 460. SENSOR_HUB_11 register........................................................... 165

Table 461. SENSOR_HUB_11 register description................................................... 165

Table 462. SENSOR_HUB_12 register........................................................... 165

Table 463. SENSOR_HUB_12 register description................................................... 165

Table 464. SENSOR_HUB_13 register........................................................... 166

Table 465. SENSOR_HUB_13 register description................................................... 166

Table 466. SENSOR_HUB_14 register........................................................... 166

Table 467. SENSOR_HUB_14 register description................................................... 166

Table 468. SENSOR_HUB_15 register........................................................... 166

Table 469. SENSOR_HUB_15 register description................................................... 166

Table 470. SENSOR_HUB_16 register........................................................... 167

Table 471. SENSOR_HUB_16 register description................................................... 167

Table 472. SENSOR_HUB_17 register........................................................... 167

Table 473. SENSOR_HUB_17 register description................................................... 167

Table 474. SENSOR_HUB_17 register........................................................... 167

Table 475. SENSOR_HUB_17 register description................................................... 167

Table 476. MASTER_CONFIG register........................................................... 168

Table 477. MASTER_CONFIG register description.................................................. 168

Table 478. SLV0_ADD register................................................................ 169

Table 479. SLV_ADD register description......................................................... 169

Table 480. SLV0_SUBADD register............................................................. 169

Table 481. SLV0_SUBADD register description..................................................... 169

Table 482. SLV0_CONFIG register............................................................. 169

Table 483. SLV0_CONFIG register description..................................................... 169

Table 484. SLV1_ADD register................................................................ 170

Table 485. SLV1_ADD register description........................................................ 170

Table 486. SLV1_SUBADD register............................................................. 170

Table 487. SLV1_SUBADD register description..................................................... 170

Table 488. SLV1_CONFIG register............................................................. 170

Table 489. SLV1_CONFIG register description..................................................... 170

Table 490. SLV2_ADD register................................................................ 171

Table 491. SLV2_ADD register description........................................................ 171

Table 492. SLV2_SUBADD register............................................................. 171

Table 493. SLV2_SUBADD register description..................................................... 171

List of tables
Table 494. SLV2_CONFIG register............................................................. 171

Table 495. SLV2_CONFIG register description..................................................... 171

Table 496. SLV3_ADD register................................................................ 172

Table 497. SLV3_ADD register description........................................................ 172

Table 498. SLV3_SUBADD register............................................................. 172

Table 499. SLV3_SUBADD register description..................................................... 172

Table 500. SLV3_CONFIG register............................................................. 172

Table 501. SLV3_CONFIG register description..................................................... 172

Table 502. DATAWRITE_SLV0 register........................................................... 173

Table 503. DATAWRITE_SLV0 register description.................................................. 173

Table 504. STATUS_MASTER register........................................................... 173

Table 505. STATUS_MASTER register description................................................... 173

Table 506. Reel dimensions for carrier tape of LGA-14 package......................................... 177

Table 507. Document revision history............................................................ 178

List of tables
List of figures
Figure 1. Four-stage pedometer algorithm........................................................ 5

Figure 2. Generic state machine............................................................... 6

Figure 3. State machine in the LSM6DSV16X..................................................... 6

Figure 4. Machine learning core in the LSM6DSV16X................................................ 7

Figure 5. Pin connections................................................................... 9

Figure 6. LSM6DSV16X connection modes...................................................... 10

Figure 7. SPI slave timing in mode 0........................................................... 16

Figure 8. SPI slave timing in mode 3........................................................... 17

Figure 9. I²C slave timing diagram............................................................ 18

Figure 10. Read and write protocol (in mode 3).................................................... 24

Figure 11. SPI read protocol (in mode 3)......................................................... 25

Figure 12. Multiple byte SPI read protocol (2-byte example) (in mode 3)................................... 25

Figure 13. SPI write protocol (in mode 3)......................................................... 26

Figure 14. Multiple byte SPI write protocol (2-byte example) (in mode 3)................................... 26

Figure 15. SPI read protocol in 3-wire mode (in mode 3).............................................. 26

Figure 16. Single-channel mode (XL_DualC_EN = 0)................................................ 32

Figure 17. Dual-channel mode (XL_DualC_EN = 1)................................................. 32

Figure 18. Block diagram of filters ............................................................. 35

Figure 19. Accelerometer UI chain............................................................. 36

Figure 20. Accelerometer composite filter........................................................ 36

Figure 21. Accelerometer chain with mode 3 enabled................................................ 37

Figure 22. Gyroscope digital chain - mode 1 (UI/EIS) and mode 2....................................... 38

Figure 23. Gyroscope digital chain - mode 3 (OIS).................................................. 39

Figure 24. LSM6DSV16X supports UI, enhanced EIS, and OIS processing simultaneously...................... 40

Figure 25. Gyroscope enhanced EIS and UI block diagram............................................ 40

Figure 26. Auxiliary SPI full control............................................................. 42

Figure 27. OIS Primary interface full control....................................................... 43

Figure 28. LSM6DSV16X electrical connections in mode 1............................................ 47

Figure 29. Qvar external connections to pin 2, 3 (Qvar input)........................................... 47

Figure 30. LSM6DSV16X electrical connections in mode 2............................................ 48

Figure 31. LSM6DSV16X electrical connections in mode 3 (auxiliary 3/4-wire SPI)............................ 49

Figure 32. Accelerometer block diagram......................................................... 73

Figure 33. LGA-14L 2.5 x 3.0 x 0.86 mm package outline and mechanical data............................. 175

Figure 34. Carrier tape information for LGA-14 package............................................. 176

Figure 35. LGA-14 package orientation in carrier tape............................................... 176

Figure 36. Reel information for carrier tape of LGA-14 package........................................ 177

List of figures
IMPORTANT NOTICE – READ CAREFULLY
STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and improvements to ST
products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on ST products before placing orders. ST
products are sold pursuant to ST’s terms and conditions of sale in place at the time of order acknowledgment.

Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or the design of
purchasers’ products.

No license, express or implied, to any intellectual property right is granted by ST herein.

Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.

ST and the ST logo are trademarks of ST. For additional information about ST trademarks, refer to http://www.st.com/trademarks. All other product or service names
are the property of their respective owners.

Information in this document supersedes and replaces information previously supplied in any prior versions of this document.

© 2023 STMicroelectronics – All rights reserved
This is a offline tool, your data stays locally and is not send to any server!
Feedback & Bug Reports