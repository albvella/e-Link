1
64Mbit Serial SRAM
Vilsion Technology Inc.
Document Title
64Mbit Serial SRAM Specification

Revision History
Revision No. History Date Remark
0.1 Initial Draft March. 31 2017 Preliminary

2
64Mbit Serial SRAM
Vilsion Technology Inc.
1.General Description
This document defines “64Mbit Serial SRAM”, which support 1.8v & 3.0V 64Mbit of SPI/QPI (Serial Peripheral
Interface/Quad Peripheral Interface) SRAM device. This RAM is configurable as 1 bit Input and Output separate or 4
bit I/O common interface. All of necessary Refresh operation is taken care by device itself.

Features
-SPI Bus Interface:
SPI compatible
SQI(qual) compatible
20 MHz Clock rate for all mode
-Low-Power CMOS Technology:
Read Current: Max.25mA
Standby Current: Typical 50uA
-Unlimited Read and Write Cycles
-8M x 8-bit Organization & 1Kbytes page size
-High Reliability
-RoHS Compliant
-8 Lead SOIC Package
-Temperature Ranges Supported:
Extended(E): -25°C to +85°C
Industrial(I): -40°C to +85°C

Product Family
Part Number Temperature Ranges Power Supply Packages
VTI7064LSME E 1.6V~2.0V 8pin SOIC
VTI7064LSMI I 1.6V~2.0V 8pin SOIC
VTI7064MSME E 2.7V~3.3V 8pin SOIC
VTI7064MSMI I 2.7V~3.3V 8pin SOIC
2.Pin Description
8pin SOIC 150mil

#CE
SO/SIO1
SIO2
VSS
SIO
VDD
SCLK
SI/SIO
3
64Mbit Serial SRAM
Vilsion Technology Inc.
Symbol Signal Type SPI Mode QPI Mode
VDD Power Core Power Supply
VSS Ground Core Supply Ground
CE# Input
Chip select signal, Active Low. When CE# input isHigh, memory will be in
Standby state
CLK Input Clock Signal
SI/SIO[0] I/O Serial Input I/O[0]
SO/SIO[1] I/O Serial Output I/O[1]
SIO[3:2] I/O I/O[3:2]^1 I/O[3:2]
Note:1,Fast read Quad access and Quad Write access in SPI Mode use SIO[3:2].Recommend to pull down to GND if no use of SIO[3:2] in SPI
mode.

3. Power up initialization
All products include an on−chip voltage sensor used to start the self−initialization process. When VDD reaches a
stable level at or above minimum VDD, the device will require 150μs to complete its self−initialization process. From
the beginning of power ramp to the end of the 150μs period, CLK should remain LOW, CE# should remain HIGH
(track VDD within 200mV) and SI/SO/SIO[3:0] should remain LOW.
After the 150us period the device requires initialization command sequence as it’s shown in Figure 2, and then the
device is ready for normal operation.

Figure 1. Power-Up Initialization Timing
Figure 2. Reset command sequence for Device Initialization
4
64Mbit Serial SRAM
Vilsion Technology Inc.
4.Interface Description
4.1 Address Space
All devices are byte−addressable. 64M device is addressed with A[22:0].
4.2 Page Length
Read and write operations are always linear address space. The Linear Burst can cross page boundary as long as
tCEM(max.) is met.
4.3 Drive Strength
The device powers up in 50Ω.
4.4 Power-on Status
The device powers up in SPI Mode.
It is required to have CE# high before beginning any operations.
4.5 Command/Address Latching Truth
The device recognizes the following commands specified by the various input methods

Command Code
SPI Mode(QE=0) QPI Mode(QE=1)
Cmd Addr
Wait
Cycle
DIO Max Freq. Cmd Addr
Wait
Cycle
DIO Max Freq.
Read 0x03 S S 0 S 33 N.A. N.A. N.A. N.A. N.A.
Fast Read 0x0B S S 8 S 104 Q Q 4 Q 84
Fast Read Quad 0xEB S Q 6 Q 104 Q Q 6 Q 104
Write 0x02 S S 0 S 104 Q Q 0 Q 104
Quad Write 0x38 S Q 0 Q 104 same as 0x
Enter Quad Mode 0x35 S - - - 104 N.A. N.A. N.A. N.A. N.A.
Exit Quad Mode 0xF5 N.A. N.A. N.A. N.A. N.A. Q - - - 104
Reset Enable 0x66 S - - - 104 Q - - - 104
Reset 0x99 S - - - 104 Q - - - 104
Read ID 0x9F S S 0 S 104 N.A. N.A. N.A. N.A. N.A.
Remark: S = Serial IO, Q = Quad IO
4.6 Command termination
All All Reads & Writes must be completed by CE# LOW to HIGH. This CK# rising edge is the trigger to terminate
the activated wordline for the read/write and set the device into standby.Not doing so will block internal refresh
perations until the device sees the read/write wordline terminated.Command termination operation is necessary
not only for Reads & Write operation and also any command operation, such as Enter Quad mode command and
Reset commands.

Figure 3
5
64Mbit Serial SRAM
Vilsion Technology Inc.
5. SPI Mode Operations
The device powers up into SPI mode by default but can also be switched into QPI mode.
5.1 SPI Read Operations
All read operation, data will be available tACLK after the falling edge of CLK. SPI read operation can be done in three
ways:

0x03: Serial CMD, Serial IO, slow frequency
0x0B: Serial CMD, Serial IO, fast frequency
0xEB: Serial CMD, Quad IO, fast frequency
Figure 4: SPI Read 0x03 (max frequency @ 33MHz)
Figure 5: SPI Fast Read 0x0B (max frequency @ 104MHz)
6
64Mbit Serial SRAM
Vilsion Technology Inc.
Figure 6: SPI Fast Quad Read 0xEB (Max frequency 104Mhz)
5.2 SPI Write Operations

Figure 7: SPI Write 0x
Figure 8: SPI Quad Write 0x
7
64Mbit Serial SRAM
Vilsion Technology Inc.
5.3 SPI to QPI Mode Enable Operation
This command switches the device into QPI mode.

Figure 9. Quad Mode Enable 0x
5.4 SPI Read ID Operation
This command is similar to Fast Read, but without the wait cycles and the device outputs EID value instead of data.

Figure 10 : SPI Read ID 0x9F (available only in SPI mode)
6.QPI Mode Operations
6.1 QPI Read Operations
All read operation, data will be available tACLK after the falling edge of CLK. QPI read operation can be done in one of
two ways:

0x0B : Quad CMD, Quad IO, slow frequency
0xEB : Quad CMD, Quad IO, fast frequency
Figure 11 : QPI Fast Read 0x0B (max frequency 84Mhz)
8
64Mbit Serial SRAM
Vilsion Technology Inc.
Figure 12 : QPI Fast Read 0xEB (max frequency 104Mhz)
6.2 QPI Write Operations
QPI write command can be input as 0x02 or 0x38. It does not matter Clock frequency.

Figure 13 : QPI Write 0x02 or 0x
6.3 QPI Mode Exit Operation
This command will switch the device back into SPI mode.

Figure 14 : Quad Mode Exit 0xF5 (Only available in QPI mode)
9
64Mbit Serial SRAM
Vilsion Technology Inc.
7.Reset Operation
The Reset operation is used as a system (software) reset that puts the device in SPI standby mode which is also the
default mode after power up. This operation consists of two commands: Reset Enable (RSTEN) and Reset (RST).

Figure 15. SPI Reset
Figure 16 : QPI Reset
The Reset operation requires the Reset Enable command followed by the Reset command. Any command other
than the Reset command after the Reset Enable command will disable the Reset Enable procedure.

10
64Mbit Serial SRAM
Vilsion Technology Inc.
8.Input / Output Timing
Figure 17: Input Timing
Figure 18: Output Timing
9.Electrical Specifications:
9.1 Absolute Maximum Ratings

Parameter Symbol Rating Unit Notes
Voltage to any ball except VDD relative to VSS VT -0.3 to VDD+0.3 V
Voltage on VDD supply relative to VSS VDD -0.2 to +2.45 V
Storage Temperature TSTG -55 to +150 °C 1
Notes 1: Storage temperature refers to the case surface temperature on the center/top side of the SRAM.
2: Exposing the device to stress above those listed in Absolute Maximum Ratings could cause permanent damage. The device is not
meant to be operated under conditions outside the limits described in the operational section of this specification. Exposure to
Absolute Maximum Rating conditions for extended periods may affect device reliability.

9.2 Operating Conditions

Parameter Min Max Unit Notes
Operating Temperature (standard) -25 +85 °C
11
64Mbit Serial SRAM
Vilsion Technology Inc.
9.3 DC Characteristics

Symbol Parameter Min Typ. Max Unit Notes
VDD Supply Voltage
VTI7064Lxx 1.60 1.8 2.0 V
VTI7064Mxx 2.7 3.0 3.3 V
VIH Input high voltage VDD-0.4 - VDD+0.2 V
VIL Input low voltage -0.2 - 0.4 V
VOH Output high voltage (IOH=-0.2mA) 0.8 VDD - - V
VOL Output low voltage (IOL=+0.2mA) - - 0.2 VDD V
ILI Input leakage current - - 1 uA
ILO Output leakage current - - 1 uA
ICC Read/Write - - 25 mA
ISB Standby current
VTI7064Lxx - 50 - uA
VTI7064Mxx - 60 - uA
9.4 AC Characteristics

Symbol Parameter Min Max Unit Notes
tCLK
CLK period-SPI Read (0x03) @33MHz 30.3 - ns
CLK period-QPI Fast Read (0x0B) @84MHz 11.9 - ns
CLK period-all other operations @104MHz 9.6 - ns
tCH/tCL Clock high/low width 0.45 0.55 tCLK
tKHKL CLK rise or fall time - 1.5 ns
tCPH CE# HIGH between subsequent burst operations 1 - tCLK
tCEM CE# low pulse width - 4 μs
tCSP CE# setup time to CLK rising edge 3 - ns
tSP Setup time to active CLK edge 2.5 - ns
tHD Hold time from active CLK edge 2 - ns
tHZ Chip disable to DQ output high.Z - 7 ns
tACLK CLK to output delay - 7 ns
tKOH Data hold time from clock falling edge 1.5 - ns
12
64Mbit Serial SRAM
Vilsion Technology Inc.
10.Code Information:
Digit-No. Remark Code
1,2,3 Vilsion Technology Inc. Product VTI
4 Serial SRAM 7
5,6,7 Density
16Mb 016
32Mb 032
64Mb 064
8 Vcc
1.8V L
3.0V M
3.3V N
9 Package
8 SOIC S
8 TSSOP T
8 DIP D
10 Die Version
Monther Die M
2nd Generation A
3rd Generation B
11 Temperature range
-25°C to 85°C E
-40°C to 85°C I
-40°C to 125°C A
12 Packing type
Tube Blank
Tape and Reel T
13 ， 14 Special function TBD TBD
V T I X X X X X X X X X X X
1 2 3 4 5 6 7 8 9 10 11 12 13 14
13
64Mbit Serial SRAM
Vilsion Technology Inc.
11.Package Information
8pin SOIC(150mil)

Symbol Min Max
A 1.35 1.
A1 0.10 0.
b 0.33 0.
c 0.15 0.
D 4.75 5.
E1 3.80 4.
E 5.80 6.
e 1.27(TYP.)
L 0.40 0.
⊙ 0° 8°