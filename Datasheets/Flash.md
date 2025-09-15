(^)
(^)
(^)
IS25 LP 128 F IS25WP 128 F
(^)
128 Mb
SERIAL FLASH MEMORY WITH 1 66 MHZ MULTI I/O SPI &
QUAD I/O QPI DTR INTERFACE
DATA SHEET

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 2
(^)
(^)
FEATURES

Ind- IS25LP128ustry Standard Serial InterfaceF: 128Mbit/16Mbyte

IS25WP1283 or 4 Byte AFddressing : 128Mbit/16MbyteMode
Supports I/O, Quad, Quad I/O, SPI DTR, Dual Standard SPI, Fast, Dual, Dual I/O
DTR, Quad I/OSoftware & Hardware Reset^ DTR, and QPI
Supports Serial Flash Discoverable Parameters (SFDP)
High Performance Serial Flash (SPI)^

80MHz Normal ReadUp to166Mhz Fast Read (^)
Up to 80MHz DTR (Dual Transfer Rate) Equivalent Throughput of 664 Mb/s
Selectable Dummy CyclesConfigurable Drive Strength (^)
Supports SPI Modes 0 and 3More than 100,000 Erase/Program Cycles (^)
More than 20 - year Data Retention

Flexible & Efficient Memory Architecture- Chip Erase with Uniform Sector/Block

EraProgse (4/32/64ram 1 to 256^ KbByte)yte^ per Page

Program/Erase Suspend & Resume

• Efficient Read and Program - Low Instruction Overhead Operationsmodes (^)

ContinuousBurst Wrap Read 8/16/32/64 Byte

Selectable QPI for RedBuurst ced LInstruengthc (^) tion Overhead
AutoBoot Operation

Low Power with Wide Temp. Ranges- Single Voltage Supply
IS25LP: 2.30V to 3.60VIS25WP: 1.65V to 1.95V (^)

10 mA Active Read Current 8 μA Standby Current
(^1) Temp Grades: μA Deep Power Down
Extended: Auto Grade-40°C to +105°C (A3) : -40°C to +125°C (^)
Advanced Security Protection

Software and Hardware Write ProtectionAdvanced Sector/Block Protection
Top/Bottom Block PPower Supply Lock rotectionProtection (^)
4x256with OTP Byte UserDedicated -lockable Security Bits Area

128 bit Unique ID for (Call Factory) Each Device

Industry Standard Pin^ - out & Packages

M =B = 8 (^16) - pin SOIC -pin SOIC 300mil208mil
K = 8L = 8--contact WSONcontact WSON 8x6mm6x5mm
G = 24H = 24--ball TFBGAball TFBGA (4x6 ball array) ( 5 x 5 ball array)
KGD (Call Factory)

128MSERIAL FLASH MEMORY b (^) WITH 166MHZ MULTI I/O SPI &
QUAD I/O QPI DTR INTERFACE (^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 3
GENERAL DESCRIPTION
The performance in a simplified pin count package. ISSI’s “IndusIS25LP128F and IS25WP128F Serial Flash memory offers a try Standard Serial Interface” Fversatile storage solution with lash ishigh for systems that flexibility and
requireInterface consisting of a Serial Data Input ( limited space, a low pin count, and low SI), Serial Data Output (SO), Serial Clock (SCK), and Chip Enable power consumption. The device is accessed through a 4-wire SPI
(CE#) pins, whi ch can also be configured to serve as multi-I/O (see pin descriptions).
Theof up to 1 device supports 66 MHz allow for equivalent clock rates of up to Dual and Quad I/O as well as standard 664 , DualMHz (1 Output, and 66 MHz x Quad 4) which equates to Output SPI. Clock frequencies 83 Mbytes/s of
data addressthroughput. The IS25xP series of Fes and read data on both edges of the clock.lash adds support for DTR These transfer rates can outperform 16 (Double Transfer Rate) commands that transfer -bit Parallel Flash
memories allowing for efficient memory access to support XIP (execute in place) operation.
Initial state of the memory array is erased (all bits are set to 1) when shipped from the factory.
QPI (Quad Peripheerased in groups of 4Kbyte sectors, 32Kbyte blocks, 64Kbyte blocks, ral Interface) supports 2-cycle instruction further reducing instruction times. Pages can be and/or the entire chip. The uniform sector
and blockapplications requiring solid data ret architecture allows for a high degree of ention. flexibility so that the device can be utilized for a broad variety of
(^)
(^)
(^)
(^)
Supply Voltage & Temperature Range vs. Maximum Speed
(^) Voltage & Temp. Speed
IS25LP (3.0V typ.) 2.30~3.6V, 1252.70~3.6V, 125°C°C^ 133MHz166MHz^
IS25WP (1.8V typ.) 1.65~1.95V, 1251.70~1.95V, 105°C°C^ 133MHz166MHz^ (1)
(^) Note:

1.^ Values are guaranteed by characterization and not 100% tested in production.^
IS25WP128F
TABLE OF CONTENTS
Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com
FEATURES TABLE OF CONTENTS
GENERAL DESCRIPTION
TABLE OF CONTENTS
PIN CONFIGURATION
PIN DESCRIPTIONS
BLOCK DIAGRAM
SPI MODES DESCRIPTION
SYSTEM CONFIGURATION
5.1 BLOCK/SECTOR ADDRESSES
5.2 Serial Flash Discoverable Parameters
REGISTERS
6.1 STATUS REGISTER
6.2 FUNCTION REGISTER
6.3 READ REGISTER AND EXTENDED REGISTER
6.3.1 READ REGISTER
6.3.2 EXTENDED READ REGISTER
6.4 AUTOBOOT REGISTER
6.5 BANK ADDRESS REGISTER
6.6 ADVANCED SECTOR/BLOCK PROTECTION (ASP) RELATED REGISTER
6.6.1 ADVANCED SECTOR/BLOCK PROTECTION REGISTER (ASPR)
6.6.2 PASSWORD REGISTER
6.6.3 PPB LOCK REGISTER
6.6.4 PPB REGISTER
6.6.5 DYB REGISTER
PROTECTION MODE...................................................................................................................................
7.1 HARDWARE WRITE PROTECTION......................................................................................................
7.2 SOFTWARE WRITE PROTECTION
7.2.1 BLOCK PROTECTION BITS
7.2.2 ADVANCED SECTOR/BLOCK PROTECTION (ASP)
DEVICE OPERATION
8.1 COMMAND OVERVIEW
8.2 COMMAND SET SUMMARY
8.3 NORMAL READ OPERATION (NORD, 03h or 4NORD, 13h)
8.4 FAST READ OPERATION (FRD, 0Bh or 4FRD, 0Ch)
8.5 HOLD OPERATION
8.6 FAST READ DUAL I/O OPERATION (FRDIO, BBh or 4FRDIO, BCh)
8.7 FAST READ DUAL OUTPUT OPERATION (FRDO, 3Bh or 4FRDO, 3Ch)...........................................
8.8 FAST READ QUAD OUTPUT OPERATION (FRQO, 6Bh or 4FRQO 6Ch)
Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com IS25WP128F
8.9 FAST READ QUAD I/O OPERATION (FRQIO, EBh or 4FRQIO, ECh)
8.10 PAGE PROGRAM OPERATION (PP, 02h or 4PP, 12h)......................................................................
8.11 QUAD INPUT PAGE PROGRAM OPERATION (PPQ, 32 h/38h or 4PPQ, 34h/3Eh)
8.12 ERASE OPERATION
8.13 SECTOR ERASE OPERATION (SER, D7h/20h or 4SER, 21h)
8.14 BLOCK ERASE OPERATION (BER32K:52h or 4BER32K:5Ch, BER64K:D8h or 4BER64K:DCh)
8.15 CHIP ERASE OPERATION (CER, C7h/60h)
8.16 WRITE ENABLE OPERATION (WREN, 06h)
8.17 WRITE DISABLE OPERATION (WRDI, 04h)
8.18 READ STATUS REGISTER OPERATION (RDSR, 05h)
8.19 WRITE STATUS REGISTER OPERATION (WRSR, 01h)
8.20 READ FUNCTION REGISTER OPERATION (RDFR, 48h)
8.21 WRITE FUNCTION REGISTER OPERATION (WRFR, 42h)...............................................................
8.22 ENTER QUAD PERIPHERAL INTERFACE (QPI) MODE OPERATION (QPIEN, 35h; QPIDI,F5h)
8.23 PROGRAM/ERASE SUSPEND & RESUME
8.24 ENTER DEEP POWER DOWN (DP, B9h)
8.25 RELEASE DEEP POWER DOWN (RDPD, ABh)
8.26 SET READ PARAMETERS OPERATION (SRPNV: 65h, SRPV: C0h/63h)
8.27 SET EXTENDED READ PARAMETERS OPERATION (SERPNV: 85h, SERPV: 83h)
8.28 READ READ PARAMETERS OPERATION (RDRP, 61h)
8.29 READ EXTENDED READ PARAMETERS OPERATION (RDERP, 81h)
8.30 CLEAR EXTENDED READ REGISTER OPERATION (CLERP, 82h)
8.31 READ PRODUCT IDENTIFICATION (RDID, ABh)
8.32 READ PRODUCT IDENTIFICATION BY JEDEC ID OPERATION (RDJDID, 9Fh; RDJDIDQ, AFh)
8.33 READ DEVICE MANUFACTURER AND DEVICE ID OPERATION (RDMDID, 90h)
8.34 READ UNIQUE ID NUMBER (RDUID, 4Bh)
8.35 READ SFDP OPERATION (RDSFDP, 5Ah)
8.36 NO OPERATION (NOP, 00h)
8.37 SOFTWARE RESET (RESETRESET ................................................................-ENABLE (RSTEN................................, 66h) AND RESET (RST................................, 99h)) AND HARDWARE
8.38 SECURITY INFORMATION ROW
8.39 INFORMATION ROW ERASE OPERATION (IRER, 64h)
8.40 INFORMATION ROW PROGRAM OPERATION (IRP, 62h)
8.41 INFORMATION ROW READ OPERATION (IRRD, 68h)
8.42 FAST READ DTR MODE OPERATION (FRDTR, 0Dh or 4FRDTR, 0Eh)
8.43 FAST READ DUAL IO DTR MODE OPERATION (FRDDTR, BDh or 4FRDDTR, BEh)
8.45 SECTOR LOCK/UNLOCK FUNCTIONS 8.44 FAST READ QUAD IO DTR MODE OPERATION IN SPI MODE (FRQDTR, ED ................................................................................................................................................................h or 4FRQDTR, EE.... 126 h)
8.46 AUTOBOOT
Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com IS25WP128F
- 8.47 READ BANK ADDRESS REGISTER OPERATION (RDBR: 16h/C8h)
- 8.48 WRITE BANK ADDRESS REGISTER OPERATION (WRBRNV: 18h, WRBRV: 17h/C5h)
- 8.49 ENTER 4-BYTE ADDRESS MODE OPERATION (EN4B, B7h)
- 8.50 EXIT 4-BYTE ADDRESS MODE OPERATION (EX4B, 29h)
- 8.51 READ DYB OPERATION (RDDYB, FAh or 4RDDYB, E0h)
- 8.52 WRITE DYB OPERATION (WRDYB, FBh or 4WRDYB, E1h)
- 8.53 READ PPB OPERATION (RDPPB, FCh or 4RDPPB, E2h)
- 8.54 PROGRAM PPB OPERATION (PGPPB, FDh or 4PGPPB, E3h)
- 8.55 ERASE PPB OPERATION (ERPPB, E4h)
- 8.56 READ ASP OPERATION (RDASP, 2Bh)
- 8.57 PROGRAM ASP OPERATION (PGASP, 2Fh)
- 8.58 READ PPB LOCK BIT OPERATION (RDPLB, A7h)
- 8.59 WRITE PPB LOCK BIT OPERATION (WRPLB, A6h)
- 8.60 SET FREEZE BIT OPERATION (SFRZ, 91h)
- 8.61 READ PASSWORD OPERATION (RDPWD, E7h)
- 8.62 PROGRAM PASSWORD OPERATION (PGPWD, E8h)
- 8.63 UNLOCK PASSWORD OPERATION (UNPWD, E9h)
- 8.64 GANG SECTOR/BLOCK LOCK OPERATION (GBLK, 7Eh)
- 8.65 GANG SECTOR/BLOCK UNLOCK OPERATION (GBUN, 98h)
ELECTRICAL CHARACTERISTICS
9.1 ABSOLUTE MAXIMUM RATINGS (1)
9.2 OPERATING RANGE
9.3 DC CHARACTERISTICS
9.4 AC MEASUREMENT CONDITIONS
9.5 PIN CAPACITANCE
9.6 AC CHARACTERISTICS
9.7 SERIAL INPUT/OUTPUT TIMING
9.8 POWER-UP AND POWER-DOWN
9.9 PROGRAM/ERASE PERFORMANCE
9.10 RELIABILITY CHARACTERISTICS
PACKAGE TYPE INFORMATION
10.1 8 - CONTACT ULTRA-THIN SMALL OUTLINE NO-LEAD (WSON) PACKAGE 8x6mm (L)
10.2 16-LEAD PLASTIC SMALL OUTLINE PACKAGE (300 MILS BODY WIDTH) (M)
10.3 24-BALL THIN PROFILE FINE PITCH BGA 6x8mm 4x6 BALL ARRAY (G)
10.4 24-BALL THIN PROFILE FINE PITCH BGA 6x8mm 5x5 BALL ARRAY (H)
10.5 8-Pin JEDEC 208mil Broad Small Outline Integrated Circuit (SOIC) PACKAGE (B)
10.6 8 Contact Ultra-Thin Small Outline No-Lead (WSON) PACKAGE 6X5MM (K)
ORDERING INFORMATION – Valid Part Numbers
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 7
1. PIN CONFIGURATION
NF^1 C
Vcc
RESET#/NC
NC
NC
NC
CE#
SO (IO 1 )
1 2 3 4 5 6 7 8
10
9
15
14
13
12
11
16 SCK
SI (IO 0 )
NC
NC
NC
NC
GND
WP# (IO 2 )
16 - pin SOIC 300 mil (Package: M)
HOLD#( (^) IoOr 3 R)ESET#( 1 )
(^)
(^)
HOLDRESET## or (IO3) (^) (1)
CE# Vcc
GND
SCK

1
2
3
4
7
6
5
SO (IO1)
SI (IO0)
8
WP# (IO2) 3 6
CE# Vcc^
SCK
SI (IO0)
7
8
4 5
1
2
GND
WP# (IO2)
SO (IO1) HOLDRESET##^ or (IO3) (1)
8 - pin SOIC 208mil 88 - -contactcontact WSON 6x5mmWSON 8 x 6 mm (^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 8
Top View, Balls Facing Down
NFC^1 NFC^2 NFC^3 NFC^4
NC NC RESET#/NC
NC SCK GND VCC
NC CE# NC WP#(IO 2 )
NC SO(IO 1 ) SI(IO 0 ) REHSOELTD## (^ IoOr^3 )
NC NC NC NC
NC A^2 AA^33 A^4
B 1 B 2 B 3 B 4
C 1 C 2 C 3 C 4
D 1 D 2 D 3 D 4
E 1 E 2 E 3 E 4
A 1
( 1 )
NC NC
NC SCK GND VCC
NC CE# NC WP#(IO 2 )
NC SO(IO 1 ) SI(IO 0 ) REHSOELTD## (^ oIOr^3 )
NC NC NC NC
NC
NC
NC
NC
Top View, Balls Facing Down
NC
A (^2) AA 33 A 4
B 1 B 2 B 3 B 4
C 1 C 2 C 3 C 4
D 1 D 2 D 3 D 4
E 1 E 2 E 3 E 4
A 5
B 5
C 5
D 5
E 5
( 1 )
RESET#/NC
(^)
Note1.: (^) The pin can be configured as Hold# or Reset# by setting P7 bit of the Read Register. Pin default is Hold# (IO3).
(^)
(^24) (Package: G)-ball TFBGA 6x8mm (4x6 ball array)
(^24) (Package: -ball TFBGA 6x8mmH) (5x5 ball array)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 9
2. PIN DESCRIPTIONS
SYMBOL TYPE DESCRIPTION

CE# INPUT
Chip Enable:operation. When CE# is high the device is deselected and output pins are in a high The Chip Enable (CE#) pin enables and disables the devices
impedance state. When deselected the devices nondown to allow minimal levels of power consumption while in a standby state.-critical internal circuitry power
When CE# is pulled low the device will be selected and brought out of standby mode. The device is considered active and instructions can be written to, data read, and
written to the device. After powernew instruction will be accepted. - up, CE# must transition from high to low before a
Keeping CE# in a high state deselects the device and switches it into its low power state. Data will not be accepted when CE# is high.
SI (IO0), SO (IO1) (^) INPUT/OUTPUT
Serial DataThis device supports standard SPI, Dual SPI, and Quad SPI operation. Standard SPI Input, Serial Output, and IOs (SI, SO, IO0, and IO1):
instructions use the unidirectional SI (Serial Input) pin to write instructions, addresses, or data to the device on the rising edge of the Serial Clock (SCK).
Standard SPI also uses the unidirectional SO (Serial Output) to read data or status from the device on the falling edge of the serial clock (SCK).
In Dual and Quad SPI mode, SI and SO become bidirectional IO pins toinstructions, addresses or data to the device on the rising edge of the Serial Clock write
(SCK) and read data or status from the device on the falling edge of SCK. Quad SPI instructions use the WP# and HOLD# pins as IO2 and IO3 respectively.
WP# (IO 2 ) INPUT/OUTPUT
Write Protect/Serial Data IO (IO2):being written in conjunction with the SRWD bit. When the SRWD is set to “1” and the The WP# pin protects the Status Register from
WP# is pulled low, the write-protected and viceStatus Register bits (SRWD, QE, BP3, BP2, BP1, BP0)-versa for WP# high. When the SRWD is set to “0”, the Status are
Register is not writeWhen the QE bit is set to “1”, the WP# pin (Write Protect) function is not available -protected regardless of WP# state.
since this pin is used for IO2.
HOLD# or (IO 3 )
RESET # (IO 3 ) INPUT/OUTPUT^
HOLD# or RESET#/Serial Data IO (IO3):to “1”, HOLD# pin or RESET# is not available since it becomes IO3. When the QE bit of Status Register is set
Most packages except for 16When QE=0, the pin acts as HOLD# or RESET#-pin SOIC and 24- ball BGA:and either one can be selected by
the P7 bit setting in Read Register. HOLD# will be selected if P7=0 (Default) and RESET# will be selected if P7=1.
(^16) - - pin SOIC and 24When QE=0 and Dedicated RESET#-ball BGA packages : (^) is Enabled (Default), the pin acts as
HOLD# regardless of the P7 bit setting in Read Register.

When QE=0 and Dedicated RESET# is DisabledRESET# and either one can be selected by the P7 bit setting in Read Register. , the pin acts as HOLD# or
HOLD# will b e selected if P7=0 (Default) and RESET# will be selected if P7=1.
The HOLD# pin allows the device to be paused while it is selected. It pcommunication by the master device without resetting the serial sequence. auses serial The
HOLD# pin is active low. will be at high impedance. Device operation can resume when HOLD# pin is brought When HOLD# is in a low state and CE# is low, the SO pin
to a high state.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 10
SYMBOL TYPE DESCRIPTION

RESET# INPUT/OUTPUT
RESET#:packages (^). This dedicated RESET# is available in 16 - pin SOIC and 24-ball BGA
The RESET# pin is a hardware RESET signal. When RESET# is driven HIGH, the memory is in the normal operating mode. When RESET# is driven LOW, the memory
enters reset mode and output is HighWRITE, PROGRAM, or ERASE operation is in progress, data may be lost.-Z. If RESET# is driven LOW while an internal
Dedicated RESET# function can be Disabled when bit 0 of Function Register = 1.It has an internal pull-up resistor and may be left floating if not used.
SCK INPUT Serial Data Clock: Synchronized Clock for input and output timing operations.
Vcc POWER Power: Device Core Power Supply
GND GROUND Ground: Connect to ground when referenced to Vcc
NC Unused NC: Pins labeled “NC” stand for “No Connect”. Not internally connected.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 11
3. BLOCK DIAGRAM
Control Logic High Voltage Generator
I/DOa Btau fLfeartcsh aensd
P^2 a^5 g^6 e^ B Byuteffser
Y-Decoder
X-De
code
r
Seri
al^ P
eriph
eral^
Inter
face
RSetgaitsutser
AddrCeossu (^) nLtaetrch &
Memory Array
CE#
SCK
(WIOP 2 #)
(IOS 0 I)
(IOS 1 O)
H O L (DIO# 3 o)r RESET#
RESET#
( 1 )
( 2 )

Note:
1: In case oRESET#f 16- pin SOIC or 24and either one can be selected by the P7 bit setting in Read Register. HOLD# will be selected if P7=0 -ball TFBFA, when QE=0 and Dedicated RESET# is Disabled, the pin acts as HOLD# or

(Default) and RESET# will be selected if P7=1.^
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 12
4. SPI MODES DESCRIPTION
Multiple controlled by a SPI Master, i.e. microIS25LP 128 F devices or multiple IS25WPcontroller, as shown in Figure 128 F devices can be connected on the SPI serial bus and 4. 1. The devices support either of two SPI
modes:
Mode 0 (0, 0)Mode 3 (1, 1) (^)
(^) The difference between these two modes is the clock polarity. When the SPI master is in stand-by mode, the serial

clock remains at “0” (SCK = 0) for Mode 0 and the clock remains at “1” (SCK = 1) for Mode 3. 4 .2 and Figure 4.3 for SPI and QPI mode. In both modes, the input data is latched on the rising edge of Serial Clock Please refer to Figure
(SCK), and the output data is available from the falling edge of SCK.
Figure 4. 1 Connection Diagram among SPI Master and SPI Slaves (Memory Devices)
SPI interface with( 0 , 0 ) or ( 1 , 1 )
(i.e. SPI MasterMicrocontroller)
MemorySPI
Device
MemorySPI
Device
MemorySPI
Device
SCK SO SI
SCK
SDI
SDO
CE#
WP#
SCK SO SI
CE#
WP#
SCK SO SI
CE#
WP#or RESETHOLD# #
CS 3 CS 2 CS 1
or RESETHOLD# # or RESETHOLD# #
Notes:
In case of 162. SI and SO pins become bidirectional IO0 and IO1 respectively during Dual I/O mode and SI, SO, WP#, and HOLD# -pin SOIC and 24-ball TFBGA, dedicated RESET# is supported.
pins become bidirectional IO0, IO1, IO2, and IO3 respectively during Quad I/O or QPI mode.^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 13
Figure 4. 2 SPI Mode Support
SCK
SO
SI
Mode 0 ( 0 , 0 )
Mode 3 ( 1 , 1 )
MSB
MSB
SCK
(^) Figure 4. 3 QPI Mode Support

20
CE#
SCK
4 0 4 0
3 - byte Address
16 12 8
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
IO 0
IO (^121171395151)
22 18 14 10 6 2 6 2
19 15 11 7 3 3
Mode Bits

IO 2
IO 3
C 4 C 0
C 5 C 1
C 6 C 2
C 71 C 3
4 0 4 0
5 1 5 1
(^6262)
3 3

4
5
6
0
1
2
3
...
...
...
...
Data 1 Data 2 Data 3
231 71 71 71 71
6
Note1: MSB^ (Most Significant Bit)^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 14
5. SYSTEM CONFIGURATION
The memory array is divided into uniform 4 Keight/sixteen adjacent sectors respectively). byte sectors or uniform 32/64 Kbyte blocks (a block consists of
(^) Table 5.1 illustrates the memory map of the device. The Status Register controls how the memory is protected.

5.1 BLOCK/SECTOR ADDRESSES
Table 5. 1 Block/Sector Addresses
(^)
Memory Density Block No.(64Kbyte)^ Block No.(32Kbyte)^ Sector No. Sector Size (Kbyte) Address Range
128Mb
Block 0 Block 0^
Sector 0 : 4 : 000000h –: 000FFFh
Block 1 (^) Sector 15:^4 :^ 00F000h :-^ 00FFFFh
Block 1 Block 2^
Sector 16: 4 : 010000h –: 010FFFh
Block 3 (^) Sector 31:^4 :^ 01F000h :-^ 01FFFFh
Block 2 Block 4^
Sector : 32 4 : 02 0000h –: 02 0FFFh
Block 5 (^) Sector :^47 4 :^02 F000h –:^02 FFFFh
: : : : :
Block 63 Block 126^
Sector : 1008 4 : 3F0000h –: 3F0FFFh
Block 127 (^) Sector :^1023 4 :^ 3FF000h –:^ 3FFFFFh
: : : : :
Block 127 Block 254^
Sector : 2032 4 : 7F0000h –: 7F0FFFh
Block 255 (^) Sector :^2047 4 :^ 7FF000h –:^ 7FFFFFh
: : : : :
Block 254 Block 508^
Sector : 4064 4 : FE0000h –: FE0FFFh
Block 509 (^) Sector :^4079 4 :^ FEF000h –:^ FEFFFFh
Block 255 Block 510^
Sector : 4080 4 : FF 0 000h –: FF0FFFh
Block 511 (^) Sector :^4095 4 :^ FFF000h –:^ FFFFFFh

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 15
5.2 Serial Flash Discoverable Parameters
The Serial Flash Discoverable Parameters (SFDP) standard memory device. SFDP is the standard of JEDEC JESD216. defines the structure of the SFDP database within the
The JEDECparameter headers and tables are optional. -defined header with Parameter ID FF00h and related Basic Parameter Table is mand atory. Additional
(^) Table 5. 2 Signature and Parameter Identification Data Values
Description Address(Byte) Address(Bit) Data
SFDP Signature (^) 00h 7:0 53h
01h 15:8 46h
02h 23:16 44h
SFDP Revision 03h^ 31:24^ 50h^
Minor 04h 7:0 06h
Major 05h 15:8 01h
Number of Parameter Headers (NPH) 06h 23:16 00 h
Unused 07h 31:24 FFh
Parameter ID LSB 08h 7:0 00h
Parameter Minor Revision 09h 15:8 06h
Parameter Major Revision 0Ah 23:16 01h
Parameter Table Length (in DWPRDs) 0Bh 31:24 10h
Basic Flash Parameter Table Pointer (PTP)
0Ch 7:0 3 0h
0Dh 15:8 00h
0Eh 23:16 00h
Parameter ID MSB^ 0Fh^ 31:24^ FFh^
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 16
(^) Table 5. 3 JEDEC Basic Flash Parameter Table
Description Address(Byte) Address(Bit) Data
Minimum Sector Erase Sizes
30h
1:0 01b
Write Granularity 2 1b
Volatile Status Register Block Protect bitsWrite Enable Instruction Select for writing to Volatile Status 3 0b
RegisterUnused 7:5^4 111b0b^
4KB Erase Instruction 31h 15:8 20h
Supports (1- 1 - 2) Fast Read
32h
16 1b
Address Bytes 18:17 01b
Supports Double Transfer Rate (DTR) Clocking 19 1b
Supports (1- 2 - 2) Fast Read 20 1b
Supports (1- 4 - 4 ) Fast Read 21 1b
Supports (1- 1 - 4 ) Fast Read 22 1b
Unused 23 1b
Reserved 33h 31:24 FFh
Flash memory Density (bits)
34h 7:0 FFh
35h 15:8 FFh
36h 23:16 FFh
37h 31:24 07h
1 - 4 - 4 Fast Read Wait Cycle Count (^) 38h 4:0 00100b
1 - 4 - 4 Fast Read Mode bit Cycle Count 7:5 010b
1 - 4 - 4 Fast Read Instruction 39h 15:8 EBh
1 - 1 - 4 Fast Read Wait Cycle Count (^) 3Ah 20:16 01000b
1 - 1 - 4 Fast Read Mode bit Cycle Count 23:21 000b
1 - 1 - 4 Fast Read Instruction 3Bh 31:24 6Bh
1 - 1 - 2 Fast Read Wait Cycle Count (^) 3Ch 4:0 01000b
1 - 1 - 2 Fast Read Mode bit Cycle Count 7:5 000b
1 - 1 - 2 Fast Read Instruction 3Dh 15:8 3Bh
1 - 2 - 2 Fast Read Wait Cycle Count (^) 3Eh 20:16 00000b
1 - 2 - 2 Fast Read Mode bit Cycle Count 23:21 100b
1 - 2 - 2 Fast Read Instruction 3Fh 31:24 BBh
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 17
Table 5. 3 JEDEC Basic Flash Parameter Table (Continued)
Description Address(Byte) Address(Bit) Data
Supports (2- 2 - 2) Fast Read
40h
0 0
Reserved 3:1 111b
Supports (4- 4 - 4) Fast Read 4 1
Reserved 7:5 111b
Reserved 43:41h 31:8 FFFFFFh
Reserved 45:44h 15:0 FFFFh
2 - 2 - 2 Fast Read Wait Cycle Count (^) 46h 20:16 00000b
2 - 2 - 2 Fast Read Mode bit Cycle Count 23 : 21 000 b
2 - 2 - 2 Fast Read Instruction 47h 31:24 FFh
Reserved 49:48h 15:0 FFFFh
4 - 4 - 4 Fast Read Wait Cycle Count (^) 4Ah 20:16 00100b
4 - 4 - 4 Fast Read Mode bit Cycle Count 23 : 21 010 b
4 - 4 - 4 Fast Read Instruction 4Bh 31:24 EBh
Erase Type 1 Size (4KB) 4Ch 7:0 0Ch
Erase Type 1 Instruction 4Dh 15:8 20h
Erase Type 2 Size (32KB) 4Eh 23:16 0Fh
Erase Type 2 Instruction 4Fh 31:24 52h
Erase Type 3 Size (64KB) 50h 7:0 10h
Erase Type 3 Instruction 51h 15:8 D8h
Erase Type 4 Size (256KB) 52h 23:16 00h
Erase Type 4 Instruction 53h 31:24 FFh
Multiplier from typical erase time to maximum erase time
57:54h
3:0 0010 b
Sector Type 1 ERASE time (typ) (^) 10:98:4^ 00110b01b
Sector Type 2 ERASE time (typ) 15:1117:16^ 01000b01b
Sector Type 3 ERASE time (typ) 22:1824:23^ 01010b01b
Sector Type 4 ERASE time (typ) 29:2531:30^ 00000b00b
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 18
(^) Table 5. 3 JEDEC Basic Flash Parameter Table (Continued)
Description Address(Byte) Address(Bit) Data
Multiplier from typical time to maximum time for page or byte PROGRAM (^) 58h 3:0 0010b
Page size 7:4 1000b
Page Program Typical time
5Ah:59h
12:8 11000b
13 0b
Byte Program Typical time, first byte 17:14 18 0111b0b
Byte Program Typical time, additional byte 22:19 23 00 0b^0 0b
Chip Erase, Typical time
5Bh
28:24 01000 b
Units 30:29 10b
Reserved 31 1b
Prohibited Operations During Program Suspend (^) 5Ch 3:0 1100b
Prohibited Operations During Erase Suspend 7:4 1110b
Reserved
5Eh:5Dh
8 1b
Program Resume to Suspend Interval 12:9 0110b
Suspend in-progress program max latency 17:1319:18^01100 10b b^
Erase Resume to Suspend Interval 23:20 0110b
Suspend in-progress erase max latency (^) 5Fh 28:2430:29^01100 10b b^
Suspend /Resume supported 31 0b
Program Resume Instruction 60h 7:0 7Ah
Program Suspend Instruction 61h 15:8 75h
Resume Instruction 62h 23:16 7Ah
Suspend Instruction 63h 31:24 75h
Reserved (^) 64h 1:0 11b
Status Register Polling Device Busy 7:2 111101b
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 19
(^) Table 5. 3 JEDEC Basic Flash Parameter Table (Continued)
Description Address(Byte) Address(Bit) Data
Exit Deep Power-down to next operation delay 3V^
67h:65h
1.8V 12:8^ 00010b00100b^
Exit Deep Power-down to next operation delay Units 14:13 01b
Exit Deep Power-down Instruction 22:15 ABh
Enter Deep Power-down Instruction 30:23 B9h
Deep Power-down Supported 31 0 b
4 - 4 - 4 mode disable sequences (QPIDI)
69h:68h
3:0 1010 b
4 - 4 - 4 mode enable sequences (QPIEN) 8:4 0 0100b
0 - 4 - 4 Mode Supported 9 1 b
0 - 4 - 4 Mode Exit Method 15:10 110000b
0 - 4 - 4 Mode Entry Method:
6Ah
19:16 1100b
Quad Enable Requirements (QER) 22:20 010 b
Hold or RESET Disable 23 0b
Reserved 6Bh 31:24 FFh
Volatile or NonInstruction for Status Register 1-Volatile Register and Write Enable (WREN) (^) 6Ch 6:0 1101000 b
Reserved 7 1 b
Soft Reset and Rescue Sequence Support (^) 6Eh:6Dh 13:8 110000 b
Exit 4-Byte Addressing 23:14 1111101000 b
Enter 4 - Byte Addressing 6Fh 31:24 10101001 b
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 20
6. REGISTERS
The device has When the register is read various sets of Registers: Status, Function, Read, continuously, the same data is output repeatedly until CE# goes HIGH.Extended Read and Autoboot. (^)

6.1 STATUS REGISTER
Status Register Format and During power up sequence, volatile register will be loaded with the value ofStatus Register Bit Definitions are described in (^) nonTable-volatile value.s 6.1 & 6.2. (^)
(^)

Table 6.1 Status Register Format
(^) SRWDBit 7 Bit 6QE Bit 5BP3 Bit 4BP2 Bit 3BP1 Bit 2BP0 Bit 1WEL Bit 0WIP

Default^0 0 0 0 0 0 0
(^) Table 6.2 Status Register Bit Definition
Bit Name Definition Read/Write-^ Type
Bit 0 WIP Write In Progress "0" indicates the device is ready "1" indicates a write cycle is in progress and the device is busyBit:^ (default) R Volatile
Bit 1 WEL Write Enable Latch:"0" indicates the device is not write enabled (default)"1" indicates the device is write enabled^ R/W^1 Volatile
Bit 2 BP0 (^) Block Protection Bit: (See Tables 6.4 for details)
Bit 3Bit 4 BP1BP2 (^) "0" indicates the specific blocks are not write"1" indicates the specific blocks are write-protected-protected (default) R/W Non-Volatile
Bit 5 BP
Bit 6 QE Quad Enable bit:“0” indicates the Quad output function disable “1” indicates the Quad output function enable^ (default) R/W Non-Volatile
Bit 7 SRWD Status Register Write Disable: (See Table "0" indicates the Status Register is"1" indicates the Status Register is write not write-protected7.1-protected (default)^ for details) R/W Non-Volatile

Note: WEL bit can be written by WREN and WRDI commands, but cannot by WRSR command.
The BP0, BP1, BP2, Status Register (WRSR) instruction. BP3, QE, and SRWD are The default value of the BPnon-volatile and volatile 0 , BP1, BPmemory cells that can be written by a Write 2 , BP3, QE, and SRWD bits were set
to “ 0 ” at factory.
The function of Status Register bits are described as follows:
WIP bitErase, Write/Set Non: Write In Progress (WIP) is read-Volatile/OTP Register, or Gang Sector/Block Lock/Unlock operation-only, and can be used to detect the progress or completion of. WIP is set to “1” (busy a Program,
state) when the device is executing for Read Status/Extended Read Register and the operationSoftware/Hardware. During this time the device will ignore further instructions except Reset instructions. In addition to the instructions,
an Erase/Program Suspend instruction also can be executedoperation has completed, WIP is cleared to “0” (ready state) whether the operation is successful or not during a Program or Erase operation. When and the an
device is ready for further instructions.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 21
(^) WEL bit: Write Enable Latch (WEL) bit indicates the status of the internal write enable latch. When WEL bit is “0”,

the bit is “1”, internal the write enable latch is disabled and Write operations are allowed. WELthe W bit is set rite operationsby a Write Enable (WREN described in Table 6.3, 06h) instruction. are inhibited. When WEL Most of Write
N on-Volatile/Volatile Register, Program and Erase instruction must be preceded by a WREN instruction.
(^) WEL bit can be reset by a Write Disable (WRDI) instruction. It will automatically reset after the completion of any

Write Non - Volatile Register, Program and Erase operation.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 22
Table 6.3 Instructions requiring WREN instruction ahead
Name Hex CodeInstruction s^ must be preceded by the WREN instructionOperation
PP4PP 02h12h Serial Serial Input Page Program (4Input Page Program (3--byte or 4byte Address)-byte Address)
PPQ4PPQ (^) 34h/3Eh32h/38h Quad Input Page Program (3Quad Input Page Program (4--byte or 4byte Address)-byte Address)
SER4SER D7h/20h21h Sector Erase 4KB (3 (^) Sector Erase 4KB (4--byte or 4byte Address)-byte Address)
BER32 (32K4BER32 (32KBB) (^) ) 52h5Ch Block Erase 32KB (3Block Erase 32KB (4--byte or 4byte Address)-byte Address)
BER64 (64KB4BER64 (64KB) (^) ) DChD8h Block Erase 64KB (3Block Erase 64KB (4--byte or 4byte Address)-byte Address)
CERWRSR C7h/60h01h Chip EraseWrite Status Register (^)
WRFRSRPNV 42h65h Write Function RegisterSet Read Parameters (Non (^) - Volatile)
SRPVSERPNV(^1 ) (^63) 85hh Set Read Parameters (Set Extended Read Parameters Volatile) (^) (Non-Volatile)
SERPIRER V (^83) 64hh SeErase Information Rowt Extended Read Parameters ( Volatile)
IRPWRABR 62h 1 5h Program Information RowWrite AutoBoot Register
WRBRNV 18 h Write Non-Volatile Bank Address Register
WRBRVWRDYB(1 ) C5hFBh Write Volatile Bank Write DYB RegisterAddress Register (4-byte Address) (^)
4WRDYBPGPPB FDE1hh Write Write PPBDYB Register(3-byte or 4 (3--byte or 4byte Address)-byte Address)
4PGPPBERPPB E3hE4h Write PPB (4Erase PPB - byte Address)
PGASPWRPLB 2FhA6h Program ASPWrite PPB Lock Bit (^)
SFRZGBLK 91h7Eh Set FREEZE bitGANG Sector/Block Lock (^)
GBUNPGPWD 98hE8h GANG Sector/Block UnlProgram Password ock
Note 1. C0h command for SRPV operation and 17h command for WRBRV operation do not require : (^) WREN command ahead.
(^) BP3, BP2, BP1, BP0 bits: The Block Protection (BP3, BP2, BP1 and BP0) bits are used to define the portion of

the memory area to be protected. Refer to Tcombination of BP3, BP2, BP1 and BP0 bits are set, the corresponding memory area is protected. Any program or able 6. 4 for the Block Write Protection (BP) bit settings. When a defined
erase operation to that area will be inhibited.
Note: A Chip Erase (CER) instruction will be ignored unless all the Block Protection Bits are “0”s.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 23
SRWDsignal to provide a Hardware Protection Mode. When the SRWD is set to “0”, the Status Register is not write bit: The Status Register Write Disable (SRWD) bit operates in conjunction with the Write Protection (WP#) -
protected. When the SRWD is set to “1” and the WP# BP3, BP2, BP1, BP0) become read-only, and a WRSR instruction will be ignored. If the SRWD is set to “1” and is pulled low (VIL), the bits of Status Register (SRWD, QE,
WP# is pulled high (V IH), the Status Register can be changed by a WRSR instruction.
QE HOLD#/RESET# are enablebit: The Quad Enable (QE) that allows d. When the QE bit is set to “1”, the IO2 and IO3 pinquad operation. When the QE bit is set to “0”s are enabled., the pin WP# and
WARNING: The QE bit must be set to “0” if WP# or HOLD#/RESET# pin (or ball) is tied directly to the power supply.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 24
Table 6.4 Block (64Kbyte) assignment by Block Write Protect (BP) Bits
Status Register Bits Protected Memory Area (128Mb, 256Blocks)
BP3 0 BP2 0 BP1 0 BP0 0 TBS(T/B selection) = 0, Top area0 (None) TBS(T/B selection) = 1, Bottom area0 (None)
00 00 01 10 1 (1 block : 255th)2 (2 blocks : 254th and 255th) 1 (1 block : 0th)2( 2 blocks : 0th and 1st) (^)
00 01 10 10 3 (4 blocks : 252nd to 255th)4 (8 blocks : 248th to 255th) 3 (4 blocks : 0th to 3rd)4 (8 blocks : 0th to 7th) (^)
00 11 01 10 5 (16 blocks : 240th to 255th)6 (32 blocks : 224th to 255th) 5 (16 blocks : 0th to 15th)6 (32 blocks : 0th to 31st)
01 10 10 10 7 (64 blocks : 192nd to 255th)8 (128 blocks : 128th to 255th) 7 (64 blocks : 0th to 63rd)8 (128 blocks : 0th to 127th) (^)
(^11 00 01) X (^1) (1) 9 (256 blocks : 0th to 255th) All blocks 10 - 11 (256 blocks : 0th to 255th) All blocks 9 (256 blocks : 0th to 255th) All blocks 10 - 11 (256 blocks : 0th to 255th) All blocks (^)

1 1 x(1)^ x(1)^12 - 15 (256 blocks : 0th to 255th) All blocks^12 - 15 (256 blocks : 0th to 255th) All blocks^
(^)
Status Register Bits Protected Memory Area (Optional BP Table (2), 128Mb, 256 Blocks)
BP3 0 BP2 0 BP1 0 BP0 0 TBS0 ( None) = 0, Top area TBS0 ( None) = 1, Bottom area
00 00 01 10 1 (1 block : 2552 (2 blocks : 254thth) (^) and 255th) 1 (1 block : 02 (2 blocks : 0th)th (^) and 1st)
0 0 1 1 3 (4 blocks : 252nd to 255th) 3 (4 blocks : 0th to 3rd)
00 11 00 01 4 (8 blocks : 2485 (16 blocks : 240th (^) thto 255 to 255th)th (^) ) 4 (8 5 (16 blocks : 0blocks : 0th (^) thto 7 to 15th) (^) th)
0 1 1 0 6 (32 blocks : 224th to 255th) 6 (32 blocks : 0th to 31st)
01 10 10 10 7 (64 blocks : 1928 (128 blocks : 128ndth to 255 to 255thth) (^) ) 7 (64 blocks : 08 (128 blocks : 0th (^) thto 63 to 127rd) (^) th)
1 0 0 1 9 (192 blocks : 64th to 255th) 9 (192 blocks : 0th to 191st)
11 00 11 01 10 (224 blocks : 3211 (240 blocks : 16ndth to 255to 255thth)) 10 (224 blocks : 011 (240 blocks : 0thth to 223to 239rdth)) (^)
1 1 0 0 12 (248 blocks : 8th to 255th) 12 (248 blocks : 0th to 247th)
11 11 01 10 13 (252 blocks : 414 (254 blocks : 2thnd to 255 to 255thth)) 13 (252 blocks : 014 (254 blocks : 0thth to 251to 253strd)) (^)
1 1 1 1 15 (256 blocks : 0th to 255th) 15 (256 blocks : 0th to 255th)
Notes:1. x is don’t care (^)

2. For Optional BP Table, see the Ordering Information (Option “B”)
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 25
6.2 FUNCTION REGISTER
Function Register Format and Bit definition are described in Table 6. 5 and Table 6.6.
Table 6.5 Function Register Format
Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0
IRL3 IRL2 IRL1 IRL0 ESUS PSUS TBS (^) RESET# DisableDedicated

Default^0 0 0 0 0 0 0 0 or 1^
Table 6.6 Function Register Bit Definition
Bit Name Definition (^) /WriteRead^ Type
Bit 0 (^) RESET# DisableDedicated Dedicated “0” indicates “1” indicates DRESET# Disable bitDedicated edicated RESET# was enabledRESET# was disabled^ R/W for 0R for 1 OTP
Bit 1 TBS Top/Bottom Selection.“0” indicates Top area.“1” indicates Bottom area.^ (See Table 6.4^ for details)^ R/W OTP
Bit 2 PSUS Program suspend bit:“0” indicates program is not suspend“1” indicates program is suspend^ R Volatile
Bit 3 ESUS Erase suspend bit"0" indicates "1" indicates Erase is not suspendErase is suspend:^ R Volatile
Bit 4 IR Lock 0^ Lock the “0” indicates the “1” indicates the Information Information RowInformation RowRow^ 0:^ can be programmedcannot be programmed R/W OTP
Bit 5 IR Lock 1 Lock the “0” indicates the “1” indicates the Information RowInformation RowInformation Row^ 1:^ can be programmedcannot be programmed R/W OTP
Bit 6 IR Lock 2 Lock the “0” indicates the “1” indicates the Information RowInformation RowInformation Row^ 2:^ can be programmedcannot be programmed R/W OTP
Bit 7 IR Lock 3 Lock the “0” indicates the “1” indicates the Information RowInformation RowInformation Row^ 3:^ can be programmedcannot be programmed R/W OTP

Note: Once OTP bits of Function Register are written to “1”, it cannot be modified to “0” any more.
Dedicated RESET# Disable bitdedicated RESET# (16-pin SOIC and 24: The default status of the bit is dependent on -ball BGA) can be programmed to “1” to disable dedicated RESET# package type. The device with
function to move RESET# function to Hold#/RESET# pin (or ball). So the device used for dedicated RESET# application and HOLD#/RESET# application. with dedicated RESET# can be
(^) TBS bit: BP0~3 area assignment can be changed from Top (default) to Bottom by setting TBS bit to “1”.

However, once Bottom is selected, it cannot be changed details. back to Top since TBS bit is OTP. See Table 6.4 for
(^) PSUS bit: The Program Suspend Status bit indicates when a Program operation has been suspended. The PSUS

changes toresumes, the PSUS bit is reset to “0”. “1” after a suspend command is issued during the program operation. Once the suspended Program
(^) ESUS bit: The Erase Suspend Status bit indicates when an Erase operation has been suspended. The ESUS bit

is “1” after a suspend command ESUS bit is reset to “0”. is issued during an Erase operation. Once the suspended Erase resumes, the
(^) IR Lock bit 0 ~ 3: The default is “0” so that the Information Row can be programmed. If the bit is set to “1”, it cannot

be changed back to “0” again since IR Lock bits are OTP.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 26
6.3 READ REGISTER AND EXTENDED REGISTER
Read Register format and of a pair of rewritable non-bvolatile registerit definitions are described below. and volatile register Read Register and Extended Read Register consist , respectively. During power up sequence, volatile
register will be loaded with the value of non - volatile value.
6.3.1 READ REGISTER
Table 6.7 and Table 6.8 define all bits that control features in SPI/QPI modes. HOLD#/RESET# pin selection (P7) bit is used to select HOLD# pin or RESET# pin in SPI mode when QE=“0” for the device with HOLD#/RESET#.
When QE=1 or in QPI mode, P7 bit setting will be ignored since the pin becomes IO3.For 16-pin SOIC or 24-ball TFBGA with dedicated RESET# device (Dedicated RESET# Disab (^) le bit in Functional

Register is “0”), HOLD# will be selected regardless of P7 bit setting when QE=“0” in SPI mode.
The SET READ PARAMETERS Operationbits, and can thereby define HOLD#/RESET# pins (SRPNV: 65h, SRPV: C0h or 63h) (or ball) selection, dummy cycles, and burst length with wrap are used to set all the Read Register
around. SRPNV is used to set the non - volatile register and SRPV is used to set the volatile register.
Table 6.7 Read Register Parameter Bit Table
P7 P6 P5 P4 P3 P2 P1 P0
(^) RESET#HOLD#/^ DummyCycles Dummy Cycles Dummy Cycles Dummy Cycles EnableWrap^ LengthBurst LengthBurst

Default^0 0 0 0 0 0 0 0
Table 6.8 Read Register Bit Definition
Bit Name Definition Read/Write-^ Type
P 0 Burst Length Burst Length R/W Nonand Volatile-Volatile
P 1 Burst Length Burst Length R/W Nonand Volatile-Volatile
P 2 Burst Set EnableLength Burst Length Set Enable"0" indicates disable "1" indicates enable (default)^ Bit:^ R/W Nonand Volatile-Volatile
P3 Dummy Cycles
Number of Dummy Cycles:Bits1 to Bit4 can be toggled to (^) select the number of dummy cycles
(1 to 15 cycles)
R/W Nonand Volatile-Volatile

P4 Dummy Cycles R/W Nonand Volatile-Volatile
P5 Dummy Cycles R/W Nonand Volatile-Volatile
P6 Dummy Cycles R/W Nonand Volatile-Volatile
P7 (^) RESET#HOLD#/^ HOLD#"0" indicates the "1" indicates the /RESET#^ HOLD#RESET#function function^ selection Bit:function is selected (default) is selected^ R/W Nonand Volatile-Volatile
(^) Table 6.9 Burst Length Data
8 bytes^ P1 0 P0 0
16 bytes32 bytes (^01 10)

64 bytes^1 1
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 27
Table 6.10 Wrap Function
Whole arrayWrap around boundary regardless of P1 and P0 value^ P2 0
Burst Length set by P1 and P0^1
Table 6.11 Read Dummy Cycles vs Max Frequency
P[6:3] (^) CyclesDummy 2,3 Fast Read0Bh/0Ch^5
Fast Read Dual
3Bh/3ChOutput^ Fast ReadBBh/BChDual IO^
Fast Read Quad
6Bh/6ChOutput^ Fast ReadEBh/EChQuad IO^ 0Dh/0EhFRDTR^ FRDDTRBDh/BEh^ FRQDTREDh/EEh^
0 Default^1 166MHzSPI^ 81MHzQPI^ 166MHzSPI^ 104MHzSPI^145 SPI MHz^ SPI, QPI 81 MHz 80/SPI/QPI 69 MHz^ 60MHzSPI^4 SPI, QPI 69 MHz
(^12 12 1198) 0MHzMHz 234 3MHzMHz (^758) 4MHzMHz (^5) 80MHz 5 MHz 6375 MHzMHz 234 3MHzMHz 5063 /11/ 23 MHzMHz (^30) 40MHzMHz 1123 MHzMHz (^)
3 3 122 MHz 46 MHz 98 MHz 95 MHz 87 MHz 46 MHz 75 / 34 MHz 50 MHz 34 MHz
45 45 133145 MHzMHz 5869 MHzMHz 133MHz140MHz 104MHz 120 MHz (^1198) 0MHzMHz 5869 MHzMHz (^80) 80// 4658 MHzMHz 60MHz 70 MHz 4658 MHzMHz (^)
(^67 67 15) 166MHz6MHz 81MHz 93 MHz 150MHz166MHz 133MHz 140 MHz 122133 MHzMHz 81MHz 93 MHz 80/80/80MHz 69 MHz 80MHz80MHz 69MHz80MHz (^)
8 8 166MHz 104 MHz 166MHz 150 MHz 145MHz 104 MHz 80 /80MHz 80MHz 80MHz
109 109 166MHz166MHz^122127 MHzMHz^ 166MHz166MHz^ 166MHz166MHz^156 166MHzMHz^122127 MHzMHz^ 80/80MHz80/80MHz^ 80MHz80MHz^ 80MHz80MHz^
1112 1112 166MHz166MHz 139151 MHzMHz 166MHz166MHz 166MHz166MHz 166MHz166MHz 139151 MHzMHz 80/80MHz80/80MHz 80MHz80MHz 80MHz80MHz (^)
13 13 166MHz 162 MHz 166MHz 166MHz 166MHz 162 MHz 80/80MHz 80MHz 80MHz
1415 1415 166MHz166MHz 166MHz166MHz 166MHz166MHz 166MHz166MHz 166MHz166MHz 166MHz166MHz 80/80MHz80/80MHz 80MHz80MHz 80MHz80MHz (^)
Notes:1. Default (^) dummy cycles are as follows.
Operation (^) Normal modeCommand DTR mode^ Normal modeDummy Cycles DTR mode^ Comment
Fast Read SPIFast Read QPI 0Bh/0Ch0Bh/0Ch 0Dh0Dh/0Eh/0Eh (^86 86) RDUID,applied. IRRD instructions are also
Fast Read Dual OutputFast Read Dual IO SPI 3Bh/3BBh/BChCh (^) BDh-/BEh 84 4 - (^)
Fast Read Quad OutputFast Read Quad IO SPI, (^) QPI 6Bh/6ChEBh/ECh (^) EDh-/EEh 86 6 - (^)
2.3. Enough number of dummy cycles must be applied to execute properly the AX read operation.Must satisfy bus I/O contention. For instance, if the number of dummy cycles and AX bits cycles are same, then X

mustQPI mode^ be Hi is not available for FRDDTR command-Z.^.
5. RDUID, IRRD instructions are also applied.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 28
6.3.2 EXTENDED READ REGISTER
Table 6.1EB6, EB5) bits provide a method to set and control driver strength. 2 and Table 6.13 define all bits that control features in SPI/QPI modes. The ODS2, ODS1, ODS0 (The four bits (EB3, EB2, EB1, EB0) are readEB7, -
only bits and may be checked or Write/Set Register operationto know. These bits are not affected by SERPNV or SERPV commands. EB4 bit remains what the WIP status is or whether there is an error during an Erase, Program,
reserved for future use.
The SET Extended EXTENDED Read Register bits, and can thereby define theREAD PARAMETERS Operation output driver strength s (SERPNV: 85h, SERPV: 83hused during READ modes.) are used to set all the SRPNV
is used to set the non - volatile register and SRPV is used to set the volatile register.
Table 6.12 Extended Read Register Bit Table
(^) ODS2EB (^7) ODS1EB (^6) ODS0EB (^5) ReservedEB (^4) E_ERREB (^3) P_ERREB (^2) PROT_EEB 1 EBWIP (^0)

Default^1 1 1 1 0 0 0 0
Table 6.13 Extended Read Register Bit Definition
Bit Name Definition Read/Write-^ Type
EB0 WIP Write In Progress Bit:Has exactly same function as the bit0 “0”: Ready, “1”: Busy (WIP) of Status Register R Volatile
EB1 PROT_E Protection Error Bit:"0" indicates no error"1" indicates protection error in an Erase or a Program operation^ R Volatile
EB2 P_ERR Program Error Bit:"0" indicates no error"1" indicates a Program^ operation failure or protection error R Volatile
EB 3 E_ERR Erase Error Bit:"0" indicates no error"1" indicates an^ Erase operation failure or protection error R Volatile
EB 4 Reserved Reserved R Reserved
EB 5 ODS0
Output Driver Output Drive Strength can be selected according to Table 6.14Strength: (^)
R/W Nonand Volatile-Volatile
EB 6 ODS1 R/W Nonand Volatile-Volatile
EB 7 ODS2 R/W Nonand Volatile-Volatile
(^) Table 6.14 Driver Strength Table
ODS2 0 ODS1 0 ODS0 0 DescriptionReserved Remark
00 01 10 12.50%25%
(^01 10 10) Reserved37.50% (^)
(^11 01 10) 100%75% (^)

1 1 1 50%^ Default^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 29
WIP bit : The definition of the WIP bit is exactly same as the one of Status Register.
PROT_E bitprotected array sector: The Protection Error bit i or block, or to access ndicates whether an a locked Information Row regionErase or Program. operation has attempted to modify When the bit is set to “1” it indicates a
that there was an error or errors in previous Erase or Program o perations. See Table 6.15 for details.
P_ERR bitProgram operation has attempted to : The Program Error bit indicates programwhether a protected array sectora Program operation/block or has succeeded or faileda locked Information Row regio, or whether a n.
When the bit is set to Register operations. See Table 6.15 for details.“ 1 ” it indicates that there was an error or errors in previous Program or Write/Set Non-Volatile
(^) E_ERR bit: The Erase Error bit indicates whether an Erase operation has succeeded or failed, or whether an Erase

operation has attempted to erase is set to “1” it indicates that there was an error or errors in previous Erasea protected array sector/block or a locked Information Row region. or Write/Set Non-Volatile When the bit Register
operations. See Table 6.15 for details.
Table 6.15 Instructions to set PROT_E, P_ERR, or E_ERR bit
Instructions Description
PP/4PP/PPQ/4PPQ4PGPPB/PGPWD /PGPPB/ The within the protected array sector/block or within an erase suspended sector/block will result in commands will set the P_ERR if there is a failure in the operation. Attempting to program
a programming error with P_ERR and PROT_E set to “1”.
IRP The commanwithin a locked Information Row region1. d will set the P_ERR if there is a failure in the operation. In attempting to program , the operation will fail with P_ERR and PROT_E set to
PGASP The command will set the P_ERR if there is a failure in the operation. Attempting to program ASPR[2:1] after the Protection Mode is selected or attempting to program ASPR[2:1] = 00b will result in a programming error with P_ERR and PROT_E set to “1”.
UNPWD If the UNPWD command supplied password does not match the hidden internal password, the UNPWD operation fails in the same manner as a programming operation on a protected sector/block and sets the P_ERR and PROT_E to “1”.
WRSR/WRABR/SRPNV/SERPNV/WRBRNV The update process for the nonon the nonrelated error bit (-volatile register bits. If either the erase or program portion of the update fails, the P_ERR or E_ERR)-volatile register bits involves an erase and a program operation will be set to “1”.
Only attempting to write the register will set PROT_E and E_ERR to “1”.for WRSR command, when Status Register is write-protected by SRWD bit and WP# pin ,
WRFR The commands will set the P_ERR if there is a failure in the operation.
SER/4SER/BER32K/4BER32K/BER64K/
4BER64K/CER/IRER/ERPPB
The commands will set the E_ERR if there is a failure in the operation. E_ERR and PROT_E will be set to “1” when the user attempts to erase a protected main memory sector/block or a
locked Information Row region. any blocks are protected by Block Protection bits (BP3~BP0). Chip Erase (CER) command will set E_ERR and PROT_E if But Chip Erase (CER) command
will not only. set E_ERR and PROT_E if sectors/blocks are protected by ASP (DYB bits or PPB bits)
Note1. OTP bits s: (^) in the Function Register and TBPARM (OTP bit) in the ASP Register may only be programmed to “1”.

Writing of the bits back to “0” is ignored and no error is set. Read only bits and partially protected bits by FREEZE bit in registers are never modified^ by a command so that the
correspondingOnce the PROT_E, P_ERR, and E_ERR^ bits in the Write/Set^ Register command data byte are ignored without setting error bits are set to “1”, they remains set to “1” until they any^ error indication.are cleared to “0”^
with the CLERPa Clear Extended Read Register command. Alternatively, H (CLERP) commandardware Reset, or. SThis means that those eoftware Reset may be used to clear the bits.rror bits must be cleared through
4. Any further command will be executed even though the e rror bits are set to “1”.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 30
6.4 AUTOBOOT REGISTER
Auto Boot Register Bit ( 32 bits) definitions are described in Table 6.1 6.
Table 6.16 AutoBoot Register Parameter Bit Table
Bits Symbols Function Type DefaultValue Description
AB[31:5] ABSA AutoBoot Start Address VolatileNon- 0000 000h (^32) access^ byte boundary address for the start of boot code
AB[4:1] ABSD AutoBoot Start Delay VolatileNon- 0h
Number of initial delay cycles between Clow and the first bit of boot code being transferredE# going ,
and it is or FRQIOthe (QE=1)same as. dummy cycles of FRD (QE=0)
Example(QE=0) or 6 (QE=1): The number of initial delay cycles when AB[4:1]= 0 h (Default is 8
setting).
AB0 ABE AutoBoot Enable VolatileNon- 0 1 = AutoBoot is enabled0 = AutoBoot is not enabled^
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 31
6.5 BANK ADDRESS REGISTER
Related Commands: (WRBRV 17h/C5h), Write NonRead Volatile -Volatile Bank Bank Address Address Register (RDRegister (WRBRNV 1BR 16h/C8h 8 ),h Write Volatile ), Enter 4-byte Address Mode (EN4B Bank Address Register
B7h), and Exit 4 - byte Address Mode (EX4B 29h).
Bank Address Register Bit (8 bits) definitions are described in Table 6.1 7 and Table 6.1 8.
Table 6.17 Bank Address Register Bit Table
(^) EXTADDBA (^7) ReservedBA (^6) ReservedBA (^5) ReservedBA (^4) ReservedBA (^3) ReservedBA (^2) ReservedBA (^1) ReservedBA (^0)

Default^0 0 0 0 0 0 0 0
Table 6.18 Bank Address Register Bit Definition
Bit Name Definition Read/Write-^ Type
BA0 Reserved Reserved R Reserved
BABA 12 ReservedReserved ReservedReserved RR ReservedReserved (^)
BABA 34 ReservedReserved ReservedReserved RR ReservedReserved (^)
BABA 56 ReservedReserved ReservedReserved RR ReservedReserved (^)
BA 7 EXTADD 3 "0" indicates "1" indicates -byte or 4-byte addressing 34 - -byte addressingbyte addressing^ selection Bit.. :^ R/W Nonand Volatile-Volatile
(^) EXTADD: Extended Address (EXTADD) controls the address field size for legacy SPI commands. When shipped

from factory4 bytes (32 bits) for the address field., it is cleared to “0” for 3 bytes (24 bits) of address. When set to “ 1 ”, the legacy commands will require
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 32
6.6 ADVANCED SECTOR/BLOCK PROTECTION (ASP) RELATED REGISTER
6.6.1 ADVANCED SECTOR/BLOCK PROTECTION REGISTER (ASPR)
Related Commands: Read ASP (RDASP 2Bh) and Program ASP (PGASP 2Fh).
Advanced Sector/Block Protection (ASP) Register Bit ( 16 bits) definitions are described in Tables 6.1 9 and 6. 20.
Table 6.19 Advanced Sector/Block Protection Register (ASPR) Bit Table
15 7 to 14 6 5 4 3 2 1 0
TBPARM Reserved Reserved Reserved Reserved Reserved PWDMLB PSTMLB Reserved
Default^1 1 1 1 1 1 1 1 1
Table 6.20 Advanced Sector/Block Protection Register (ASPR) Bit Definition
Bit Name Definition Read/Write-^ Type
0 Reserved Reserved R Reserved
1 PSTMLB Persistent Protection ““ 01 ”” = = Persistent Persistent Protection Mode permanently enabled.Protection Mode not permanently enabled.Mode Lock Bit^ R/W OTP
2 PWDMLB Password Protection Mode Lock Bit““ 01 ”” = Password Protection Mode permanently enabled.= Password Protection Mode not permanently enabled.^ R/W OTP
14 : 3 Reserved Reserved R Reserved
15 TBPARM Configures Parameter Sectors location““ 01 ”” = 4= 4KKB physical sectors at top, (high address)B physical sectors at bottom (Low address)^ R/W OTP
(^) The Advanced Sector/Block Protection Register (ASPR) is used to permanently configure the behavior of Advanced

Sector /Block Protection (ASP) features and parameter sectors location.
PWDMLB (ASPR[2]) and PSTMLB (ASPR[1]) bitsPersistent Protection Mode, with all sectors unprotected, when power is applied. The device programmer or host : When shipped from the factory, all devices default ASP to the
system must then choose which sectorLock Bits locks the part permanently in the selected /block protection method to use. Programming either of the Protection Mode mode:
(^) • ASPR[2:1] = 11 = No ASP mode selected, Persistent Protection Mode is the default.

• • ASPR[2:1] = 10 = Persistent Protection Mode permanently selectedASPR[2:1] = 01 = Password Protection Mode permanently selected..
• ASPR[2:1] = 00 = Illegal condition, and the program operation will abortattempting to program both bits to zero results in a programming failure. It will result in a programming error with P_ERR set to 1.
(^) As a result, PWDMLB and PSTMLB are mutually exclusive, only one may be programmed to zero.
(^) ASPR programming rules:

• If the corresponding bitPassword. Protection Mode is chosen, the password must be programmed prior to setting the
• Once the Protection Mode is selected, the further change to the ASPR[2:1] is allowed.ASPR Attempting to program [2:1] bits are permanently protected fromASPR[2:1] after selected will result in a programming and no
programming errorprogramming time. The system with P_ERR set to 1. can determine tThe programming time of the ASPhe status of the ASPR programming operation by reading the R is the same as the typical page
• WIP bit in the StatusTBPARM bit can be programmed even after ASPR[2:1] bits are programmed while the^ Register^ or Extended Read Register.^ FREEZE bit in the PPB
Lock Register is “0”.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 33
TBPARMtwo 4KB sectors bit: TBPARM defines the logical location of the parameter block. The parameter block consists of thirty, which replace two 64KB blocks. When TBPARM is default state (“ 1 ”), the parameter block is at -
the Bottom of the array. array address space. TBPARM is OTP and When TBPARM is default stateprogrammed to “ 1 ” when it ships from “0”, the parameter block is in the top of the memory Factory. If TBPARM is programmed
to “ 0 ”, an attempt to change it back to “ 1 ” will fail and ignore the Program.
Tmanufacture; before the first program or erase operation on the main flash array. TBPARM must not behe desired state of TBPARM must be selected during the initial configuration of the device during system (^)

programmed after programming or erasing is done in the main flash array.
TBstoreS bit in the Function Register parameter information from the bottom of the array and protect boot code starting at the top of the array, and can be programmed independent of TBPARM. Therefore, the user can select to
vice together.versa. Or the user can select to store and protect the parameter information starting from the top or bottom
6.6.2 PASSWORD REGISTER
Related Commands: (UNPWD, E9h). Read Password (RDPWD E7h), Program Password (PGPWD E8h), and Unlock Password
(^) Table 6.21 Password Register Bit Definition
Bit Name Definition Default Read/Write-^ Type
63 : 0 PSWD
64 bit The password is no longer readable after the password hidden password:
protection mode is selected by programming ASPR bit 2 to zero. FFFFFFFFFFFFFFFFh-^ R/W^ OTP^

6.6.3 PPB LOCK REGISTER
Related Commands: FREEZE Bit (SFRZ 91h)Read. PPB Lock Bit (RDPLB A7h), Write PPB Lock Bit (WRPLB A6h), UNPWD (E9h) and Set
(^) Table 6.22 PPB Lock Register Bit Definition
Bit Name Definition Default Read/Write-^ Type
0 PPBLK
PPB Lock bit: “ 0 ” = PPB array protected until next power cycleProtect PPB Array (^)
“ 1 ” or Hardware Reset= PPB array may be programmed or erased.^ Persistent:Password:^10 R/W^ Volatile^
6 : 1 Reserved Reserved Reserved R Reserved
7 FREEZE
Lock current state of BP3Function Register and TBPARM in -0 bits in Status Register, ASPR, and TBS in
Information Row (IR) regions.“1” = Locked
“0” = Un-locked
0 R/W Volatile
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 34
PPBLK bitset to “ 1 ”, it allows the PPBs to be changed. The WRPLB command is used to clear the PPB Lock bit to : The PPB Lock bit is a volatile bit for protecting all PPB bits. When cleared to 0, it locks all PPBs, when “ 0 ”. The
PPB Lock bit must be cleared to 0 only after all the PPBs are configured to the desired settings.
In Persistent Protection mode, the PPB Lock only be cleared to “ 0 ” by the Write PPB Lock Bit (WRPLB A6hbit is set to “ 1 ” during POR or Hardware Reset. ) command only. When cleared to The PPB Lock bit can “ 0 ”, no software
command sequence can set the PPB Lock bitPPB Lock bit. back to “ 1 ”, only another Hardware Reset or power-up can set the
(^) In the Password Protection mode, the PPB Lock bit is cleared to 0 during POR or Hardware Reset. The PPB Lock
bit can only be can clear the PPB Lock bit set to 1 by the Unlock Password commandback to “ 0 ”, only another Hardware Reset or power only. When set to “ (^1) - ”up can , no software command sequence clear the PPB Lock bit.
(^) FREEZE bit: FREEZE bit, when set to “1”, locks the current state of BP3-0 in Status Register, TBS in the Function

Registerwriting, programming, or erasing these areas. As long as FREEZE remains cleared to logi, TBPARM in the Advanced Sector/Block Protection Register, and the Information Row. This prevents c “0”, BP3-0 in Status
Register, TBwritable and the Information Row is programmable. Once FREEZE has been written to a logic “1” it can only be S in the Function Register, and TBPARM in the Advanced Sector/Block Protection Register are
cleared to a logic “The FREEZE is volatile and the default state of FREEZE after power0” by a power-on cycle or a Hardware Reset. Software Reset will not affect the state of FREEZE. -on is “0”. The FREEZE can be set to “1” by a
SFRZ command only.
6.6.4 PPB REGISTER
Related Commands: and Erase PPB (ERPPB E4h)Read PPB (. RDPPB FCh or 4RDPPB E2h)), Program PPB (PGPPB FDh or 4PGPPB E3h),
(^) Table 6.23 PPB Register Bit Definition
Bit Name Definition Default Read/Write-^ Type
7 : 0 PPB
Read or Program per sector00h = PPB for the sector/block/block addressed by the PPB: (^) RDPPB or
PGPPBthat sector command is programmed to /block from program or erase operations.“ 0 ”, protecting
FFh = PPB for the sectoror /block addressed by the RDPPB
PGPPB that sectcommand is erased to or/block from program or erase operations.“ 1 ”, not protecting
FFh R/W Non-Volatile

6.6.5 DYB REGISTER
Related Commands: Read DYB ( RDDYB FAh or 4RDDYB E0h) and Write DYB (WRDYB FBh or 4WRDYB E1h).
Table 6.24 DYB Register Bit Definition
Bit Name Definition Default Read/Write-^ Type
7 : 0 DYB
Read or Write per sector00h = DYB for the sector/block/block DYBaddressed by the : (^) RDDYB
orWRDYB (^) command is cleared to “ 0 ”, protecting that
FFh = DYB for the sectorsector/block^ from program or erase operations./block addressed by the RDDYB^
orWRDYB (^) command is set to “ 1 ”, not protecting that
sector/block from program or erase operations.
FFh R/W Volatile
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 35
7. PROTECTION MODE...................................................................................................................................
The device supports hardware and software write-protection mechanisms.
7.1 HARDWARE WRITE PROTECTION......................................................................................................
The Write Protection (WP#) pin provides a hardware write protection method for QE in the Status Register. Refer to the section 6.1 STATUS REGISTER. BP3, BP2, BP 1 , BP0, SRWD, and
(^) Write inhibit voltage (VWI) is specified in the section 9.7 POWER-UP AND POWER-DOWN. All write sequence will

be ignored when Vcc drop s to VWI.
Table 7.1 Hardware Write Protection on Status Register
SRWD 0 WP#Low Status RegisterWritable
(^10) HighLow ProtectedWritable
1 High Writable
Note: Before the execution of any program, erase or (WEL) bit must be enabled by executing a Write Enable (WREN) instruction. If the WEL bit is not enabled, the Write Status/Function Register instruction, the Write Enable Latch
program, erase or write register instruction will be ignored.

7.2 SOFTWARE WRITE PROTECTION
The bits (deviceBP3, (^) BP2, BP1, BP0) and another is Advanced Sector/Block Protection (ASP). Whealso provides two kinds of software write protection feature. One is Block Protection by Block Protection n Block Protection is

enabled (i.e., any BP3sectors/blocks not protected by the Block Protection scheme. In the case that both ASP and Block Protection are -0 are set to “1”), Advanced Sector/Block Protection (ASP) can still be used to protect
used on the same sector /block the logical OR of ASP and Block Protection related to the sector/block is used.
7.2.1 BLOCK PROTECTION BITS
The or the whole memory area to be writedevice provides a software write protection feature-protected. For details, see 6.1 Status Register.. The Block Protection bits (BP3, BP2, BP1, BP0) allow part
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 36
7.2.2 ADVANCED SECTOR/BLOCK PROTECTION (ASP)
There are two ways to implement software Advanced Sectormethod or Persistent Protection methods. Through these two protection methods, user can disable or enable the /Block Protection on this device: Password Protection
prograFigure mming or erasing operation to 7.1 shows an overview of these methods. any or all blocks including 32 top 4K sectors or 32 bottom 4K sectors. The
(^) Every main flash array block/top sector/bottom sector has a non-volatile (PPB) and a volatile (DYB) protection bit

associated with it. When either bit is 0, the sector is protected from program and erase operations.
The PPB bits are protected from program and erase when the PPB Lock bit is all main flash array sectors are unprotected when shipped from factory. “ 0 ”. The PPB bits are erased so that
(^) There are two methods for managing the state of the PPB Lock bit, Persistent Protection and Password Protection.
(^) The Persistent Protection Mode sets the PPB Lock bit to “ 1 ” during power up or Hardware Reset so that the PPB

bits are unprotected. There is a is no command in the Persistent Protection method to set the WRPLB command to clear the PPB Lock bit to PPB Lock bit therefore the PPB Lock bit will remain “ 0 ” to protect the PPB bits. There
at changing sector protection by programming or erasing the PPB, then protecting the PPB from further change for “ 0 ” until the next power up or Hardware Reset. The Persistent Protection method allows boot code the option of
the remainder of normal system operation bycontrolled sector protection. clearing the PPB Lock bit. This is sometimes called Boot-code
(^) The Password Protection Mode requires use of a password to control PPB protection. In the Password Protection

Modepassword may be permanently programmed and hidden for the , the PPB Lock bit is cleared to “0” during power up or PHardware Rassword Protection Modeeset to protect the PPB. The UNPWD bitscommand. A 64-bit
can be used to provide a password for comparison with the hidden password. If the password matcheLock bit is set to “1” to unprotect the PPB. The WRPLB command can be used to clear the PPB Lock bit to “0”. s the PPB
(^) After cleaning the PPB Lock bit to “0” with WRPLB command, H/W reset (or Power cycle) is required to use

UNPWD command again to unprot ect the PPB.
The selection of the PPB Lock bit management method is made by programming OTP bits in the ASP Register so as to permanently select the method used.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 37
Figure 7.1 Advanced Sector/Block Protection

DYB DYB (^01)
DYB DYB (^23)
SectorSector//Block Block (^01)
SectorSector//Block Block (^23)
PPB PPB (^01)
PPB PPB (^23)
DYB NDYB N-- (^32)
DYB NDYB N- 1
SectorSector//Block NBlock N-- (^32)
SectorSector//Block NBlock N- 1
PPB NPPB N-- (^32)
PPB NPPB N- 1
0 = Locked
(^64) (OTP-bit Password )
Password Protection Mode (ASPR[ 2 ]= 0 Persistent Protection Mode (ASPR[ 1 ]= 0
ASP Register Bits (OTP)
DYB Memory Array PPB

0 1 = = SectorSector//Block ProtectedBlock Unprotected (default)
DYBs are volatile and defaults to “after power-up 1 ”
0 1 = = SectorSector//Block ProtectedBlock Unprotected
PPB bits are programmed individuallybut erased collectively ,
The bit defaults to “or “ 0 ” (Password Protection mode 1 ” (Persistent Protection mode) upon reset. )
23.. “Password Protection mode requires a password to 0 ” locks all PPB bits to their current state.
set PPB Lock bit to “erase of PPB bits. 1 ” to enable program or
Persistent Protection mode only allows PPB Lock bit to be cleared to “ 0 ” to prevent program or erase
PPB bitsset PPB Lock bit to “. Power off or hardware reset is required to 1 ”.
1 = Unocked
PPB Lock Bit (Volatile)
Note: 128M: N = 285 = 32 (32xTop 4K sectors or 32xBottom 4K sectors) + 254 (254x64K blocks) - 1
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 38
Table 7.2 PPB/DYB and Sector/Block mapping (TBPARM = 1 )
Memory Density GroupPPB GroupDYB Block No.(64Kbyte) Sector No. (^) (Kbyte)Sector Size Address Range
128Mb
PPB 0 DYB 0
Block 0
: : Sector 0: 4 : 000000h -:^ 000FFFh^
PPB 15:^ DYB 15:^ Sector 15:^4 :^ 00F000h -:^ 00FFFFh
PPB 16 DYB 16
Block 1
: : Sector 16: 4 : 010000h -:^ 010FFFh^
PPB :^31 DYB 31:^ Sector 31:^4 :^ 01F000h -:^ 01FFFFh
PPB 32 DYB 32 Block 2
Sector 32: 4 : 020000h -: 020FFFh
Sector 47:^4 :^ 02F000h -:^ 02FFFFh
: : : : : :
PPB 284 DYB 284 Block 254
Sector : 4064 4 : FE0000h –: FE0FFFh
Sector :^4079 4 :^ FEF000h –:^ FEFFFFh
PPB 285 DYB 285 Block 255
Sector : 4080 4 : FF 0 000h –: FF0FFFh
Sector :^4095 4 :^ FFF000h –:^ FFFFFFh
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 39
Table 7.3 PPB/DYB and Sector/Block mapping (TBPARM = 0 )
Memory Density GroupPPB GroupDYB Block No.(64Kbyte) (^) Sector No. (^) (Kbyte)Sector Size Address Range
128Mb
PPB 0 DYB 0 Block 0
Sector 0: 4 : 000000h -: 000FFFh
Sector 15:^4 :^ 00F000h -: 00FFFFh
PPB 1 DYB 1 Block 1
Sector 16: 4 : 010000h -: 010FFFh
Sector 31:^4 :^ 01F000h -: 01FFFFh
PPB 2 DYB 2 Block 2
Sector 32: 4 : 020000h -: 020FFFh
Sector 47:^4 :^ 02F000h -: 02FFFFh
: : : : : :
PPB 126 DYB 126 Block 126
Sector : 2016 4 : 7 E0000h –: 7 E0FFFh
Sector :^2031 4 :^7 EF000h –:^7 EFFFFh
PPB 127 DYB 127 Block 127
Sector : 2032 4 : 7 F 0 000h –: 7 F0FFFh
Sector :^2047 4 :^7 FF000h –:^7 FFFFFh
PPB :^254 DYB :^254 :^ :^ :^ :^
Block 254
: : Sector : 4064 4 : FE0000h –:^ FE0FFFh^
PPB :^269 DYB :^269 Sector :^4079 4 :^ FEF000h –:^ FEFFFFh
PPB 270 DYB 270
Block 255
: : Sector : 4080 4 : FF^0 000h –:^ FF0FFFh^
PPB :^285 DYB :^285 Sector :^4095 4 :^ FFF000h –:^ FFFFFFh
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 40
Persistent Protection Bits (PPBs)
The Persistent Protection Bits 7.2, and Table 7. 3 ). It is programmed individually but must be erased as a group, similar to the way individual words (PPBs) are unique for each sector/block and non-volatile (refer to Figure 7.1, Table
may be programmed in the main array but an entire sectorthe same endurances as the Flash memory. Preprogramming and verification prior to erasure are handled by the /block must be erased at the same time. The PPBs have
device, and therefore do not require system monitoring. programming time. Erasing all the PPBs requires typical sector erase time. During PPB biProgramming a PPB bit requires the typical page t programming and PPB
bit erasing, status is available by reading the Status Registerrequires the initial access time of the device. or Extended Read Register. Reading of a PPB bit
(^) Notes:
1.2. Each PPB is individually programmedThe PPB Lock bit must be cleared first before changing the status of a PPB. to “0” and all are erased to “1” in parallel.
3.4. While programming PPB, array data cannot be read from any sectorsWhen reading the PPB of the desired sector/block the address should be location zero /blocks. (^) within the sector/block. The high

5. order address bits not used must be zero.There are no means for individually erasing a specific PPB and no specific sector^ /block address is required for this operation.
6.7. The state of the PPB for When the parts are first shipped, the PPBs are cleared (erased to “1”).a given sector/block can be verified by using a PPB Read command.
(^) Dynamic Protection Bits (DYBs)

Dynamic Protection Bits DYBs only control the protection for unprotected sectors(DYBs) are volatile and unique for each sector/blocks that have their PPBs cleared (erased to “1”). By /block and can be individually modified.
issuing the protected or unprotected state respectively. This feature allows software to easily protect sectorsWrite DYB command, the DYBs are cleared to “0” or set to “1”, thus placing each sector/blocks/block against in the
inadvertent changescan be set or cleared as often, yet does not prevent the easy removal of protection when changes are needed as needed as they are volatile bits.. The DYBs
(^) Persistent Protection Bit (PPB) Lock Bit

The “1”, it allows the PPBs to be changed.PPB Lock bit is a volatile bit for protecting all PPB bits. If the PPB Lock bit. When is “0”, the PPB Program or Erase command does not cleared to “0”, it locks all PPBs and when set to
execute and fails without programming or erasing the PPB.
In Persistent Protection mode, the PPB Lock “0”, no software command sequence can set the PPB Lock bit to “1”, only another Hardware Reset or powerbit is set to “1” during power up or Hardware Reset. When cleared to -up
can set the PPB Lock bit.
In the Password Protection mode, the PPB Lock bit is cleared to “0” during power up or a Hardware Reset during power up or a Hardware Reset during power up or a Hardware Reset. The PPB Lock bit can only be set to “1” by
the Password Unlock command.

The PPB Lock bit must be cleared to “0” only after all PPBs are configured to the desired settings.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 41
Sector/Block Protection States Summary
Each following protection states:sector in specific blocks and each of all other blocks except for the specific blocks can be in one of the
• Unlocked protection state defaults to– The sector/block unprotected after a power cycle, software reset, or hardware reset. is unprotected and protection can be changed by a simple command. The
• Dynamically Locked protection state is not saved across a power – A sector/block is protected and protection can be changed by a simple command. Thecycle.
• Persistently Locked to “ 1 ”. The protection state is non– A sector/block-volatile and saved across a power cycle or reset. Changing the protection is protected and protection can only be changed if the PPB Lock bit is set (^)

state requires programming and or erase of the PPB bits.^
Table 7.4 contains all possible combinations of the DYB, PPB, and sector/block. In summary, if the PPB Lock bit is locked (cleared to “0”), no changes to the PPBs are allowed. The PPB Lock bit relating to the status of the
PPB Lock bit can only be unlocked (set to “1”) through a Hardware Reset or power cycle.
Table 7.4 Sector/Block Protection States
““ 01 ”” = Locked or Protected= Unlocked or Unprotected (^)
PPBProtection Bit values DYB^ Assigned Sector/Block State^

11 10 UnprotectedProtected
00 10 ProtectedProtected (^)
PPB Lock Bit (^10) NOT changeableChangeable^ ChangeableChangeable^
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 42
Persistent Protection Mode
The Persistent Protection bits are unprotected by a device Mode sets the Hardware RPPB Lock biteset. Software to “ 1 ” (^) Rduring eset does not affect the power up or Hardware Reset so that the PPBPPB Lock bit. The WRPLB
command can clear the therefore the PPB Lock bitPPB Lock bit will remain at to “ 0 “ (^0) ” ”until the next power to protect the PPB. There is no command to set the up or Hardware Reset. PPB Lock bit
(^) Password Protection Mode

The Password Protection Mode allows an even higher level of security than the Persistent Protection Mode by requiring a 64-bit password for unlocking the device PPB Lock bit. In addition to this password requirement, after
power up Successful execution of the Unlock Password command by entering the entire password or Hardware Reset, the PPB Lock bit is cleared to “0” to maintain the password mode of operation. sets the PPB Lock bit to
“1” , allowing for sector/block PPBs modifications.
Notes:1. The password is all “1”s when shipped from Factory. It is located in its own memory space and is accessible through the use

of the Program Password and Read Password commands.Once the Password is programmed and verified, the Password^ Protection Mode Lock Bit (ASPR[2]=0) in ASP Register must
be programmed, programmedall further in order to Program and Read commands to the password region are disabled and these commands are prevent reading or modifying the password. After the Password Protection Mode Lock Bit is
ignoredPassword Protection M so that there is no means to verify what the password is. Password verification is only allowed before selode. ecting the
The “ 0 ” results in the cell left as a Program Password Command is only capable of programming “ 0 ” with no programming error. “ 0 ”s. Programming a “ 1 ” after a cell is programmed as a
4.5. All 64The Protection Mode Lock Bits-bit password combinations are valid as a password. in ASP Register are not erasable (^) because they are OTP.

The exact password must be entered in order for the unlocking function to occur. If the password Password command does not match the hidden internal password, the unlock operation fails in the same manner as a provided by Unlock
programming operation on a protected cleared to 0. In this case it is a failure to change the state of the PPB Lock bit because it is stillsector/block. The P_ERR and PROT_E are set to 1 and the PPB Lock bit remains protected by the lack of a
valid password.The Unlock Password command cannot be accepted any faster than once every 100μs ± 20μs. This^ makes it take an
unreasonably long time (58 million years) for a hacker to run through all the 64match a password. The Read Status Register command or the Read Extended Read Register -bit combinations in an attempt to corremay be used to read the WIP ctly
bit to determine when the device has completed the command. When a valid password is provided the Unlock PUnlock Password command does not insert the 100μs delay before assword command or is ready to accept a new password
returning the WIP bit to zero.If the password is lost after selecting the Password^ Protection Mode, there is no way to set the PPB Lock bit.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 43
8. DEVICE OPERATION
8.1 COMMAND OVERVIEW
The instruction codes. All instructions, addresses, and data are shifted in with the most significant bit (MSdevice utilizes an 8-bit instruction register. Refer to Table 8. 3. Instruction Set for details on instructions and B) first on
Serial Datedge of Serial Clock (SCK) for normal mode and both of rising and falling edges for DTR mode after Chip Enable a Input (SI) or Serial Data IOs (IO0, IO1, IO2, IO3). The input data on SI or IOs is latched on the rising
(CE#) is driven low (Vaddress bytes and/or dummy cyclesIL). Every instr uction sequence starts with a one(configurable) and/or data bytes, depending on the type of instruction. CE# -byte instruction code and is followed by
must be driven high (V IH) after the last bit of the instruction sequence has been shifted in to end the operation.
Commands are structured as follows:• Each command begins with a byte (^) (eight bits) instruction.

• The instruction may be stand alone or may be followed by address bits to select a location within one ofaddress spaces in the device. The address may be either a 24-bit or 32-bit byte boundary address. several
• The SPI done one, two, or four bits in parallelinterface with Multiple IO provides the option for each transfer of address and data. This enables a tradeoff between the number of signal connections (IO bus information to be
width) and the speed of information transfer. If the host system can support amemory performance can be increased by using the instructions that provide parallel two bit (dual) or parallel two or four bit wide IO bus the
• four bit (quad) transfers.The width of all transfers following the instruction are determined by the instruction sent.^
• • All Some instructions send single bit or parallel bit groups are transferred in most to Mode Bits following the address to indicate that the nextleast significant bit order. command will be of the same
type with an implied, rather than an explicit, instruction. The next commandbyte, only a new address and mode bits. This reduces the time needed to send each command when the same thus does not provide an instruction
• command type is repeated in a sequence of commands.The address or Mode Bits may be followed by Dummy Cycles^ before read data is returned to the host.
• Dummy CyclesCycles. may be zero to several SCK cycles. In fact, Mode Bits will be counted as a part of Dummy
• All instruction, address, the device with the Most Mode, and data information is transferred in byte granularity. Addresses are shiftedSignificant Byte first. All data is transferred with the lowest address byte sent first. into
• Following bytes of data are sent in lowest to highest byte address order i.e. the byte addressAll attempts to read the flash memory array during a program, erase, or a write cycle (embedded^ increments. operations)^
are ignored. The embedded operation will continue to execute without any affect. A veryare accepted during an embedded operation. These are discussed in the individual command descriptions. limited set of commands
While a program, erase, or write(WIP) bit is “ 0 ” before issuing most commands to the operation is in progress, it is device, to ensure the new command can be accepted. recommended to check that the Write In Progress
• Depending on the command, the time for execution varies. A command to executing command is available to determine when the command completes execution and whether theread status information from an (^)

• command was successful.Following are some general signal^ relationship descriptions to keep in mind.
– The host always controls twide transfers. The memory drives Serial Output (SO) for single bit read transfers. The host andhe Chip Enable (CE#), Serial Clock (SCK), and Serial Input (SI) - SI for single memory bit
– alternately drive the IO0All commands begin with the host selecting the memory by driving C-IO3 signals during Dual and Quad transfers.^ E# low before the first rising edge of
Generally, CSCK. CEE# is kept low throughout a command and when C# remains low for 8-bit transfer multiples to transfer byte granularity information. E# is returned high the command ends.All commands^
will not be accepted if CE# is returned high not at an 8-bit boundary.^

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 44
8.2 COMMAND SET SUMMARY
(^) Extended Addressing

To accommodate addressing above 128Mb (24 - bit), there are three options:
1. New instructions with 4-byte (32-bit) address. See Table 8. 1.
(^4) For backward compatibility to the 3-byte addressing with the 3-byte address instructions:-byte address instructions, the standard instructions can be used in
conjunction with the EXTADD Bit in theswitch from 3 bytes to 4 bytes of address field. Bank Address Register (BAR When EXTADD bit is set to 1 or Enter 4 [7]) or Enter 4-byte Address Mode -byte Address Mode to
command is issued, the instructions are changed to require 4-byte (32-bit) for the address field. See Table 8. 2.
(^3) For backward compatibility to the 3-byte addressing with the 3-byte address instructions:-byte addressing, the standard instructions can be used in conjunction (^) with
the Bank Address Register. 4 - byte Address Mode operationWhen EXTADD bit is set to 0 or Exi, the instructions are changed to require 3t 4 - byte Add-byte (24ress Mode command is issued after -bit) for the address field See
Table 8.2.
Table 8.1 New Instruction Set with 4 - byte address
Instruction Name Operation Code Address Mode
4NORD4FRD 4 - 4 byte Address -byte Address Fast Read ModeNormal Read Mode 13h0Ch 44 - -bytebyte Address Address (^)
4FRDIO4FRDO (^4) - (^4) byte Address Fast Read Dual Output-byte Address Fast Read Dual I/O BCh3Ch 44 - -byte Addressbyte Address (^)
4FRQIO4FRQO 4 - (^4) byte Address Fast Read Quad Output-byte Address Fast Read Quad I/O ECh6Ch 44 - -byte Addressbyte Address (^)

4FRDDTR4FRDTR^44 - byte Address Fast Read Dual I/O DTR -byte Address Fast Read DTR Mode^ BEh0Eh^44 - -byte Addressbyte Address^
4FRQDTR4PP 44 - -byte Address Serial Input Page Programbyte Address Fast Read Quad I/O DTR EEh12h 44 - -byte Addressbyte Address (^)
4PPQ4SER 4 - byte Address Quad Input Page Program 4 - byte Address Sector Erase 34h/3Eh21h 44 - -byte Addressbyte Address (^)
4BER32 4BER64 (64KB(32KB)) 44 - -byte Address Block Erase 32Kbyte Address Block Erase 64KBB (^) DCh5Ch 44 - -byte Addressbyte Address (^)
4SECUNLOCK4RDDYB 4 - 4 byte Address Sector Unlock-byte Address Read DYB 2 E0 5 h 44 - -byte Addressbyte Address (^)
4WRDYB4RDPPB 44 - -byte Addressbyte Address Read PPB Write DYB E1E2 44 - -byte Addressbyte Address (^)

4PGPPB^4 - byte Address Program PPB^ E3^4 - byte Address^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 45
Table 8.2 Instruction Set with 3 - byte or 4 - byte address according to EXTADD Bit setting
Instruction Name Operation Code (^) EXTADD (BAR[7] = 1Address ModeEXTADD (BAR[7]) = 0^
NORDFRD Normal Read ModeFast Read Mode 03h0Bh 44 - -byte byte AddressAddress 33 - -byte byte AddressAddress (^)
FRDIOFRDO Fast Read Dual OutputFast Read Dual I/O BBh3Bh 44 - -byte Addressbyte Address 33 - -byte Addressbyte Address (^)
FRQIOFRQO Fast Read Quad OutputFast Read Quad I/O EBh6Bh 44 - -byte Addressbyte Address 33 - -byte Addressbyte Address (^)
FRDDTRFRDTR^ Fast Read Dual I/O DTR Fast Read DTR Mode^ BDh0Dh^44 - -byte Addressbyte Address^33 - -byte Addressbyte Address^
FRQDTRPP Serial Input Page ProgramFast Read Quad I/O DTR EDh02h 44 - -byte Addressbyte Address 33 - -byte Addressbyte Address (^)
PPQSER Quad Input Page Program Sector Erase D7h/20h32h/38h 44 - -byte Addressbyte Address 33 - -byte Addressbyte Address (^)
BER32 (32KBER64 (64KBB)) Block Erase 32KBlock Erase 64KBB 52hD8h 44 - -byte Addressbyte Address 33 - -byte Addressbyte Address (^)
SECUNLOCKRDDYB Sector UnlockRead DYB 26hFA 44 - -byte Addressbyte Address 33 - -byte Addressbyte Address (^)
WRDYBRDPPB Write DYBRead PPB FBFC 44 - -byte Addressbyte Address 33 - -byte Addressbyte Address (^)
PGPPB Program PPB FD 4 - byte Address 3 - byte Address
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 46
Table 8.3 All Instruction Set
Instruction Name Operation Mode Byte0 Byte1 Byte2 Byte3 Byte4 Byte5 Byte6
NORD (^) (3Normal Read-byte Address)Mode SPI 03h (^) <23:16>A^ <15:8>A^ <7:0>A^ Data out
NORD (^) (4Normal Read-byte Address)Mode SPI 03h (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ Data out
4NORD 4 Normal Read-byte Address Mode SPI 13h (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ Data out
FRD (^) (3-byte Address)Fast ReadMode SPIQPI^ 0Bh (^) <23:16>A^ <15:8>A^ <7:0>A^ DummyByte (1)^ Data out
FRD (^) (4-byte Address)Fast ReadMode SPIQPI^ 0Bh (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ DummyByte (1)^ Data out
4FRD 4 - byte Fast ReadModeAddress SPIQPI^ 0Ch (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ DummyByte (1)^ Data out
FRDIO (^) (3-byte Address)Fast ReadDual I/O SPI BBh <23:16>DualA^ <15:8>DualA^ <7:0>DualA^ AXhDual(1),(2) Data outDual^
FRDIO (^) (4-byte Fast ReadDual I/OAddress) SPI BBh (^) <31::24>A^ <23:16>DualA^ <15:8>DualA^ <7:0>DualA^ AXhDual(1),(2) Data outDual^
4FRDIO 4 - byte Address Fast ReadDual I/O SPI BCh (^) <31::24>A^ <23:16>DualA^ <15:8>DualA^ <7:0>DualA^ AXhDual(1),(2) Data outDual^
FRDO (^) (3-Dual byte Address)Fast ReadOutput^ SPI 3Bh (^) <23:16>A^ <15:8>A^ <7:0>A^ DummyByte (1)^ Data outDual^
FRDO (^) (4-Dual Outputbyte Address)Fast Read^ SPI 3Bh (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ DummyByte (1)^ Data outDual^
4FRDO 4 - Dual Outputbyte Address Fast Read SPI 3Ch (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ DummyByte (1)^ Data outDual^
FRQIO (^) (3-byte Address)Fast ReadQuad I/O SPIQPI^ EBh <23:16>QuadA^ <15:8> QuadA^ <7:0>QuadA^ AXhQuad(1), (2) Data outQuad^
FRQIO (^) (4-byte Address)Fast ReadQuad I/O SPIQPI^ EBh <31::24>QuadA^ <23:16>QuadA^ <15:8> QuadA^ <7:0>QuadA^ AXhQuad(1), (2) Data outQuad^
4FRQIO 4 - byte Address Fast ReadQuad I/O SPIQPI^ ECh <31::24>QuadA^ <23:16>QuadA^ <15:8> QuadA^ <7:0>QuadA^ AXhQuad(1), (2) Data outQuad^
FRQO (^) (3Quad -byte Address)Fast ReadOutput^ SPI 6Bh (^) <23:16>A^ <15:8>A^ <7:0>A^ DummyByte (1)^ Data outQuad^
FRQO (^) (4Quad Output-byte Address)Fast Read^ SPI 6Bh (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ DummyByte (1)^ Data outQuad^
4FRQO 4 - Quad Outputbyte Address Fast Read SPI 6Ch (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ DummyByte (1)^ Data outQuad^
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 47
Instruction Name Operation Mode Byte0 Byte1 Byte2 Byte3 Byte4 Byte5 Byte6
FRDTR (^) (3-DTR Modebyte Address)Fast Read^ SPIQPI^ 0Dh (^) <23:16>A^ <15:8>A^ <7:0>A^ DummyByte (1)^ Data Dualout^
FRDTR (^) (4-DTR Modebyte Address)Fast Read^ SPIQPI^ 0Dh (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ DummyByte (1)^ Data outDual^
4FRDTR 4 - byte Address DTR ModeFast Read SPIQPI^ 0Eh (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ DummyByte (1)^ Data outDual^
FRDDTR (^) (3Dual I/O DTR-byte Address) Fast Read^ SPI BDh <23:16>DualA^ <15:8>DualA^ <7:0>DualA^ AXhDual(1), (2) Data outDual^
FRDDTR (^) (4Dual I/O DTR-byte Address) Fast Read^ SPI BDh (^) <31::24>A^ <23:16>DualA^ <15:8>DualA^ <7:0>DualA^ AXhDual(1), (2) Data outDual^
4FRDDTR (^4) Dual I/O DTR -byte Address Fast Read SPI BEh (^) <31::24>A^ <23:16>DualA^ <15:8>DualA^ <7:0>DualA^ AXhDual(1), (2) Data outDual^
FRQDTR (^) (3Quad I/O DTR-byte Address)Fast Read^ SPIQPI^ EDh (^) <23:16>A^ <15:8>A^ <7:0>A^ AXhQuad(1), (2) Data outQuad^
FRQDTR (^) (4Quad I/O DTR-byte Address)Fast Read^ SPIQPI^ EDh (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ AXhQuad(1), (2) Data outQuad^
4FRQDTR (^4) Quad I/O DTR-byte AddressFast Read SPIQPI^ EEh (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ AXhQuad(1), (2) Data outQuad^
PP (^) (3-Input Pagebyte Address)Program SPIQPI^ 02h (^) <23:16>A^ <15:8>A^ <7:0>A^ (256byte)PD^
PP (^) (4-Input Pagebyte Address)Program SPIQPI^ 02h (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ (256byte)PD^
4PP 4 - byte Address Input PageProgram SPIQPI^ 12h (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ (256byte)PD^
PPQ (^) (3Page Program -Quad Inputbyte Address)^ SPI 32h/38h (^) <23:16>A^ <15:8>A^ <7:0>A^ (256byte)Quad PD^
PPQ (^) (4Page Program-Quad Inputbyte Address)^ SPI 32h/38h (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ (256byte)Quad PD^
4PPQ (^4) Page Program -byte AddressQuad Input SPI 34h/3Eh (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ (256byte)Quad PD^
SER (^) (3Sector Erase-byte Address)^ SPIQPI^ D7h/20h (^) <23:16>A^ <15:8>A^ <7:0>A^
SER (^) (4Sector Erase-byte Address)^ SPIQPI^ D7h/20h (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^
4SER 4 - Sector Erasebyte Address SPIQPI^ 21h (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 48
Instruction Name Operation Mode Byte0 Byte1 Byte2 Byte3 Byte4 Byte5 Byte6
BER32 (32KB) (^) (3-Block Erasebyte Address)32Kbyte SPIQPI (^) 52h (^) <23:16>A (^) <15:8>A (^) <7:0>A (^)
BER32 (32KB) (^) (4-Block Erasebyte Address)32Kbyte SPIQPI (^) 52h (^) <31::24>A (^) <23:16>A (^) <15:8>A (^) <7:0>A (^)
4BER32 (32KB) 4 - Block Erasebyte Address32Kbyte SPIQPI (^) 5Ch (^) <31::24>A (^) <23:16>A (^) <15:8>A (^) <7:0>A (^)
BER64 (64KB) (^) (3-Block Erasebyte Address)64Kbyte SPIQPI (^) D8h (^) <23:16>A (^) <15:8>A (^) <7:0>A (^)
BER64 (64KB) (^) (4-Block Erasebyte Address)64Kbyte SPIQPI (^) D8h (^) <31::24>A (^) <23:16>A (^) <15:8>A (^) <7:0>A (^)
4BER64 (64KB) 4 - Block Erasebyte Address64Kbyte SPIQPI (^) DCh (^) <31::24>A (^) <23:16>A (^) <15:8>A (^) <7:0>A (^)
CER Chip Erase SPIQPI^ C7h/60h
WREN Write Enable SPIQPI^ 06h
WRDI Write Disable SPIQPI^ 04h
RDSR Read StatusRegister SPIQPI^ 05h Data out
WRSRRDFR Read FunctionWrite Status Register SPIQPI^ 01h Data in (^)
Register SPIQPI^ 48h^ Data out^
WRFR Write FunctionRegister SPIQPI^ 42h Data in
QPIEN (^) QPI modeEnter^ SPI 35h
(^)
QPIDI (^) QPI modeExit^ QPI F5h
PERSUS Suspend duringprogram/erase SPIQPI^ 75h/B0h
PERRSM (^) program/eraseResume^ SPIQPI^ 7Ah/30h
DP Deep Power Down SPIQPI^ B9h
RDID, RDPD (^) Power DownRead ID / Release SPIQPI (^) ABh XXh(3) XXh(3) XXh(3) ID7-ID0
SRPNV (^) (NonParameters Set Read-Volatile)^ SPIQPI^ 65h Data in
SRPV Parameters Set Read(Volatile) SPIQPI^ C0h/63h Data in
SERPNV Read Parameters (NonSet Extended -Volatile) SPIQPI^ 85h Data in
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 49
Instruction Name Operation Mode Byte0 Byte1 Byte2 Byte3 Byte4 Byte5 Byte6
SERPV Read Parameters Set Extended (Volatile) SPIQPI^ 83h Data in
RDRP Parameters Read Read(Volatile) SPIQPI^ 61h Data out
RDERP Read Parameters Read Extended (Volatile) SPIQPI^ 81h Data out
CLERP Clear Extended Read Register SPIQPI^ 82h
RDJDID Read JEDECID Command^ SPI 9Fh MF7-MF0 ID15-ID8 ID7-ID0
RDMDID Manufacturer& Device IDRead SPIQPI^ 90h XXh(3) XXh(3) 00h01h^ MF7ID7--MF0ID0 MF7ID7--ID0 MF0^
RDJDIDQ Read JEDEC QPI modeID QPI AFh MF7-MF0 ID15-ID8 ID7-ID0
RDUID (^) Unique IDRead^ SPIQPI^ 4Bh (^) <23:16>A(4)^ <15:8>A(4)^ <7:0>A(4)^ DummyByte Data out
RDSFDP SFDP Read SPI 5Ah (^) <23:16>A^ <15:8>A^ <7:0>A^ DummyByte Data out
NOP No Operation SPIQPI^ 00h
RSTEN Software EnableReset SPIQPI^ 66h
RST Software Reset SPIQPI^ 99h
IRER InformationErase Row SPIQPI^ 64h (^) <23:16>A^ <15:8>A^ <7:0>A^
IRP InformationProgramRow SPIQPI^ 62h (^) <23:16>A^ <15:8>A^ <7:0>A^ (256byte)PD^
IRRD InformationRead Row SPIQPI^ 68h (^) <23:16>A^ <15:8>A^ <7:0>A^ DummyByte Data out
SECUNLOCK (^) (3Sector Unlock-byte Address)^ SPIQPI^ 26h (^) <23:16>A^ <15:8>A^ <7:0>A^
SECUNLOCK (^) (4Sector Unlock-byte Address)^ SPIQPI^ 26h (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^
4SECUNLOCK (^4) Sector Unlock-byte Address SPIQPI^ 25h (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^
SECLOCK Sector Lock SPIQPI^ 24h
RDABR Read AutoBoot Register SPI 14h Data 1 out^ Data out 2 Data 3 out^ Data out 4
WRABR Write AutoBoot Register SPIQPI^ 15h Data in 1 Data in 2 Data in 3 Data in 4
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 50
Instruction Name Operation Mode Byte0 Byte1 Byte2 Byte3 Byte4 Byte5 Byte6
RDBR Address RegisterRead Bank (Volatile) SPIQPI^ 16h/C8h Data out
WRBRV Address RegisterWrite Bank (Volatile) SPIQPI^ 17h/C5h Data in
WRBRNV Address Register(NonWrite Bank -Volatile) SPIQPI^ 18h Data in
EN4B (^) Address ModeEnter 4-byte SPIQPI^ B7h (^)
EX4B (^) Address ModeExit 4-byte SPIQPI^ 29h
RDDYB (^) (3-byte Read DYBAddress)^ SPIQPI^ FAh (^) <23:16>A^ <15:8>A^ <7:0>A^ Data out
RDDYB (^) (4-byte Address)Read DYB^ SPIQPI^ FAh (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ Data out
4RDDYB 4 - byte Address Read DYB SPIQPI^ E0h (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ Data out
WRDYB (^) (3-byte Address)Write DYB^ SPIQPI^ FBh (^) <23:16>A^ <15:8>A^ <7:0>A^ Data in
WRDYB (^) (4-byte Address)Write DYB^ SPIQPI^ FBh (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ Data in
4WRDYB 4 - byte Address Write DYB SPIQPI^ E1h (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ Data in
RDPPB (^) (3-byte Address)Read PPB^ SPI FCh (^) <23:16>A^ <15:8>A^ <7:0>A^ Data out
RDPPB (^) (4-byte Address)Read PPB^ SPI FCh (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ Data out
4RDPPB 4 - byte Address Read PPB SPI E2h (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^ Data out
PGPPB (^) (3Program PPB (Individually)-byte Address) SPIQPI^ FDh (^) <23:16>A^ <15:8>A^ <7:0>A^
PGPPB (^) (4Program PPB (Individually)-byte Address) SPIQPI^ FDh (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^
4PGPPB 4 Program PPB -(Individually)byte Address SPIQPI^ E3h (^) <31::24>A^ <23:16>A^ <15:8>A^ <7:0>A^
ERPPB Erase PPB (as a group) SPIQPI^ E4h (^)
RDASP Read ASP SPIQPI^ 2Bh Data out(2 byte)
PGASP Program ASP SPIQPI^ 2Fh (^) (2 byte)PD^
RDPLB Read PPB Lock Bit SPI A7h Data out
WRPLB Write PPB Lock Bit SPIQPI^ A6h (^)
SFRZ Set FREEZE bit SPIQPI^ 91h
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 51
Instruction Name Operation Mode Byte0 Byte1 Byte2 Byte3 Byte4 Byte5 Byte6
RDPWD Read Password SPI E7h Data out(8 byte)
PGPWD (^) PasswordProgram SPIQPI^ E8h (^) (8 byte)PD^
UNPWD (^) PasswordUnlock SPIQPI^ E9h (^) (8 byte)Data in^
GBLK Set all DYB bits (Gang Sector/Block Lock) SPIQPI^ 7Eh (^)
GBUN Clear all DYB bits (Gang Sector/Block Unlock) SPIQPI^ 98h
Notes:1. The number of dummy cycles depends on the value setting in the Table 6. (^11) Read Dummy Cycles.
2.3. AXh has XX means “don’t care”.to be counted as a part of dummy cycles. X means “don’t care”.

4. A<23: 9 > are “don’t care” and A<8:4> are always “0”.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 52
8.3 NORMAL READ OPERATION (NORD, 03h or 4NORD, 13h)
The Normal Read (NORD) instruction is used to read memory contents at a maximum frequency of 80 MHz.
• • 03h (EXTADD=0) is followed by a 303h (EXTADD=1) is followed by a 4--byte address (A23byte address (A31--A0) orA0) or (^)

• 13h is followed by a 4-byte address (A31-A0)
The Normal Read instruction code is transmitted via the SI line, followed by three (A23 address bytes of the first memory location to be read as above. A total of 24 or 32 address bits are shifted in, but - A0) or four (A31 – A0)
only byte addressed can be at any memory location. Upon completion, any data on the SI will be ignored. Refer to Table AVMSB (Valid Most Significant Bit) - A 0 are decoded. The remaining bits (A31 – AVMSB+1) are ignored. The first
8. 4 for the related Address Key.
The array, can be read out in one Normal Read instruction. The address is automatically incremented by one after each first byte data (D7 - D0) is shifted out on the SO line, MSB first. A single byte of data, or up to the whole memory
byte of data is shifted odata comes out. When the highest address of the device is reached, the address counter will roll over to the ut. The read operation can be terminated at any time by driving CE# high (VIH) after the
000000h address, allowing the entire memory to be read in one continuous Read instruction.
If instruction is ignored and will not have any effects on the current operationthe Normal Read instruction is issued while an Erase, Program or Write operation is in process (WIP=1) the.
(^) Table 8.4 Address Key
3 byte addressMode^ Valid Address^ 128Mb^
4 byte address AVMSB(2)–A^0 A 23 - A0 (A31A^23 - A0-A24=X^ )(2)
Notes:

X=Don’t Care
AVMSB is a Valid MSB. In 4 byte address for 128Mb, A31 is an MSB, and A23 is a Valid MSB.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 53
Figure 8.1 Normal Read Sequence (03h [EXTADD=0], 3-byte address)
7 6
CE#
SCK
SI
SO 5 4 3 2 1 0
Data Out 1
Instruction = 03 h 23
CE#
SCK
SI 3 2
SO
1 0
3 - byte Address
High Impedance
22 21 ...
0 1 2 3 4 5 6 7 8 9 10 ... 28 29 30 31
32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
Mode 3
Mode 0
...
tV^76543210
Data Out 2
...
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 54
Figure 8.2 Normal Read Sequence (03h [EXTADD=1] or 13h, 4-byte address)
Instruction = 03 h/ 13 h
4 - byte Address
36 37 38 39
40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 ...
7 6
CE#
SCK
SI
SO 5 4 3 2 1 0
Data Out 1
31
CE#
SCK
SI 3 2
SO
1 0
High Impedance
30 29 ...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...
Mode 0
tV^76543210
Data Out 2
...
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 55
8.4 FAST READ OPERATION (FRD, 0Bh or 4FRD, 0Ch)
The Fast Read (FRD, 4FRD) instruction is used to read memory data at up to a 1 66 MHz clock.
• • 0Bh (EXTADD=0) is followed by a 30Bh (EXTADD=1) is followed by a 4--byte address (A23byte address (A31--A0) orA0) or (^)

• 0Ch is followed by a 4-byte address (A31-A0)
The Fast Read instruction code is followed by three or four address bytes as above and dummy cycles (configurable, default is 8 clocks), transmitted via the SI line, with each bit latched-in during the rising edge of SCK.
Then the first data byte frequency fCT, during the falling edge of SCK.from the address is shifted out on the SO line, with each bit shifted out at a maximum
(^) The first byte addressed can be at any memory location. The address is automatically incremented by one after

each byte of data is000000h address, allowing the entire memory to be read with a single Fast Read instruction. The Fast Read shifted out. When the highest address is reached, the address counter will roll over to the
instruction is terminated by driving CE# high (VIH).
If is ignored without affecting the current cycle.the Fast Read instruction is issued while an Erase, Program or Write cycle is in process (WIP=1) the instruction
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 56
Figure 8.3 Fast Read Sequence (0Bh [EXTADD=0], 3-byte address)
Instruction = 0 Bh
3 - byte Address
28 29 30 31
32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ...
7 6
CE#
SCK
SI
SO 5 4 3 2 1
Data Out
23
CE#
SCK
SI 3 2
SO
1 0
High Impedance
22 21 ...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...
Mode 0
tV
Dummy Cycles
0 ...
Note: Dummy cycles depends on Read Parameter setting. Detailed information in Table 6.11 Read Dummy Cycles.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 57
Figure 8.4 Fast Read Sequence (0Bh [EXTADD=1] or 0Ch, 4-byte address)
7 6
CE#
SCK
SI
SO 5 4 3 2 1
Data Out
Instruction = 0 Bh/ 0 Ch 31
CE#
SCK
SI 3 2
SO
1 0
4 - byte Address
High Impedance
30 29 ...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...
Mode 0
tV
Dummy Cycles
36 37 38 39
40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 ...
0 ...
Note: Dummy cycles depends on Read Parameter setting. Detailed information in Table 6.11 Read Dummy Cycles.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 58
FAST READ OPERATION IN QPI MODE (FRD, 0Bh or 4FRD, 0Ch)
The Fast Read (FRD) instruction in QPI mode is used to read memory data at up to a 166MHz clock.
• • 0Bh (EXTADD=0) is followed by a 30Bh (EXTADD=1) is followed by a 4--byte byte address (A31address (A23--A0) orA0) or (^)

• 0Ch is followed by a 4-byte address (A31-A0)
The Fast Readand 6 dummy cyc instruction codeles (configurable, default is 6 clocks) (2 clocks) is followed by three (6 clocks) or four (8 clocks) address bytes as above , transmitted via the IO3, IO2, IO1 and IO0 lines, with each
bit latchedand IO0 lines, with each bit shifted ou-in during the rising edge of SCK. Then the first data byte addressed is shifted out on the IO3, IO2, IO1 t at a maximum frequency fCT, during the falling edge of SCK.
(^) The first byte addressed can be at any memory location. The address is automatically incremented by one after

each byte of data is shifted out. When the highest address is reached, the address 000000h address, allowing the entire memory to be read with a single Fast Read QPI counter will roll over to the instruction. The Fast Read
QPI instruction is terminated by driving CE# high (VIH).
If the the instruction is ignored without affecting the current cycle.Fast Read instruction in QPI mode is issued while an Erase, Program or Write cycle is in process (WIP=1)
(^) The Fast Read sequence in QPI mode is also applied to the commands in the following table 8.5. However, only

3 - byte address mode QPI sequence is applied for RDUID, and IRRD commands.
Table 8.5 Instructions that Fast Read sequence in QPI Mode is applied to
Instruction NameFRQIO Fast Read Quad I/OOperation Hex CodeEBh
RDUIDIRRD Read Unique IDRead Information Row 4Bh68h
Figure 8.5 Fast Read QPI Sequence (0Bh [EXTADD=0], 3-byte address)
0 Bh
CE#
SCK
IO[ 3 : 0 ]
3 - byte Address^6 Dummy Cycles
Mode 3 0 1 2 3 4 5 6 7 8 9 ...^1314151617
Mode 0
23 : 20 7 : 4 3 : 0 7 : 4 3 : 0
Data 1 Data 2
19 : 1615 : 1211 : 8 7 : 4 3 : 0
...
tV
...
Note: Number of dummy cycles depends on Read ParameterInstruction setting. Detailed information in Table 6.11 Read Dummy^
Cycles.^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 59
Figure 8.6 Fast Read Sequence In QPI Mode (0Bh [EXTADD=1] or 0Ch, 4-byte address)
0 Bh/ 0 Ch
CE#
SCK
IO[ 3 : 0 ]
4 - byte Address^6 Dummy Cycles
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 ...^151617
Mode 0
31 : 28 7 : 4 3 : 0
Data 1
27 : 24 15 : 1211 : 8 7 : 4 3 : 0
tV
Instruction
23 : 2019 : 16
Note: Number of dummy cycles depends on Read Parameter setting. Detailed information in Table 6.11 Read Dummy^
Cycles.^
8.5 HOLD OPERATION
HOLD# is used in conjunction with CE# to select the device. When the device underway, HOLD# can be used to pause the serial communication with the master device without resetting the is selected and a serial sequence is
serial sequence. To pause, HOLD# is brought low while the SCK signal is low. To resume serial communication, HOLD# is brought high while the SCK signal is low (SCK may still toggle during HOLD). Inputs to SI will be ignored
while SO is in the high impedance state, during HOLD.
Note: HOLD is not supported in DTR mode or with QE=1 or when RESET# is selected for the HOLD# or RESET# pin.
Timing graph can be referenced in AC Parameters Figure 9.4.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 60
8.6 FAST READ DUAL I/O OPERATION (FRDIO, BBh or 4FRDIO, BCh)
The may aFast Read Dual I/Ollow for code to be executed directly from the SPI in some applications. (FRDIO, 4FRDIO) instruction allows the address bits to be input two bits at a time. This
(^) • BBh (EXTADD=0) is followed by a 3-byte address (A23-A0) or

• • BBh (EXTADD=1) is followed by a 4BCh is followed by a 4-byte address (A31-byte address (A31-A0) - A0) or
(^) The FRDIO/4FRDIO instruction code is followed by three or four address bytes as above and dummy cycles

(configurable, default is 4 clocks)rising edge of SCK. The address MSB is input on I, transmitted via the IO1 and IO0 lines, with each pair of bits latchedO1, the next bit on IO0, and this shift pattern continues to -in during the
alternate between the two lines. Depending on the usage of AX read operation mode, a mode byte may be located after address input.
(^) The first data byte addressed is shifted out on the IO1 and IO0 lines, with each pair of bits shifted out at a maximum

frequency fbit is output on IO0. Figures CT, during the falling edge of SCK. The first bit (MSB) is output on IO1, while simultaneously the second 8.7 and 8.8 illustrates the timing sequence.
(^) The first byte addressed can be at any memory location. The address is automatically incremented by one after

each byte of data is shifted out. When the highest address is reached, the address counter will roll over to the 000000h address, allowing the entire memory to be read with a single FRDIO/4FRDIO instruction. The
FRDIO/4FRDIO instruction is terminated by driving CE# high (VIH).
The device supports the AX read operation by applying mode bits during dummy period. Mode bits consist of 8 bits, such as M7 to M0. Four cycles after address input are reserved for Mode bits in FRDIO/4FRDIO execution.
M7 to M4 are important for enabling thit enables the AX read operation and subsequent FRDIO/4FRDIO execution skips command code. It saves cycles is mode. M3 to M0 become don’t care for future use. When M[7:4]=1010(Ah),
as described in Figures the AX read operation. After finishing the read operation, device becomes ready to receive a new command. SPI 8.9 and 8.10. When the code is different from AXh (where X is don’t care), the device exits
or QPI mode configuration retains the prior setting. Mode bit must be applied during dummy cycles. Numberdummy cycles in Table 6.11 includes number of mode bit cycles. If dummy cycles are configured as 4 cycles, data of
output will start right after mode bit is applied.
If the FRDIO/4FRDIO instruction is issued while an Erase, Program or Write cycle is in pinstruction is ignored and will not affect the current cycle. rocess (WIP=1) the
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 61
Figure 8.7 Fast Read Dual I/O Sequence (BBh [EXTADD=0], 3-byte address)
7 5 3 1 7 5 3 1
Data Out 1
Instruction = BBh 22
CE#
SCK
(^2064)
3 - byte Address
High Impedance

20 18 ...
0 1 2 3 4 5 6 7 8 9 10 ... 18 19 20 21
22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37
Mode 3
Mode 0
...
tV
23 21 19 ...^3175
IO 0
IO 1
3 1
2 0 6 4 2 0 6 4 2 0
4 Dummy Cycles
7 5 3 1
6 4 2 0
7 5 ...
6 4 ...
CE#
SCK
IO 0
IO 1
Data Out 2 Data Out 3
Mode Bits
Notes: Mode Bits^
If the mode bits=AXh (where X is don’t care), it can execute the AX read bits are different from AXh, the device exits the AX read operation. mode (without command). When the mode
2.3. Number of dummy cycles depends on clock speed. Detailed information in Table 6.11 Read Dummy Cycles.Sufficient dummy cycles are required to avoid I/O contention. If the number of dummy cycles and AX bits cycles
are same, then X should be Hi-Z.^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 62
Figure 8.8 Fast Read Dual I/O Sequence (BBh [EXTADD=1] or BCh, 4-byte address)
4 - byte Address
22 23 24 25
26 27 28 29 30 31 32 33 34 35 36 37 38 39 36 41 ...
Instruction = BBh/BCh
7 5 3 1 7 5 3 1
Data Out 1
30
CE#
SCK
2 0 6 4
High Impedance
28 26 ...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...
Mode 0
tV
31 29 27 ... 3 1 7 5
IO 0
IO 1
3 1
2 0 6 4 2 0 6 4 2 0
4 Dummy Cycles
7 5 3 1
6 4 2 0
7 5 ...
6 4 ...
CE#
SCK
IO 0
IO 1
Data Out 2 Data Out 3
Mode Bits
Mode Bits^
Notes:1. If the mode bits=AXh (where X is don’t care), it (^) can execute the AX read mode (without command). When the mode

Number of dummy cycles depends on clock speed. Detailed information in Table 6.11 Read Dummy Cycles.bits are different from AXh, the device exits the AX read operation.^
Sufficient dummy cycles are same, then X should be Hiare required to avoid I/O contention.-Z. If the number of dummy cycles and AX bits cycles
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 63
Figure 8.9 Fast Read Dual I/O AX Read Sequence (BBh [EXTADD=0], 3-byte address)
22
CE#
SCK
(^20)
3 - byte Address
20 18 ...
Mode 3 0 1 2 3 ...^1112131415161718192021
Mode 0

23 21 19 ...^31
IO 0
IO 1
4 Dummy Cycles
6
7
(^64)
7 5
(^20)
3 1
tV Data Out 1
(^64)
7 5
(^20)
3 1

4
5
Mode Bits
...
...
Data Out 2
...
Notes:
If the mode bits=AXh (wheremode bits are different from AXh, the device exits the AX read operation. X is don’t care), it will keep executing the AX read mode (without command). When the
2.3. Number of dummy cycles depends on clock speed. Detailed information in Table 6.11 Read Dummy CySufficient dummy cycles are required to avoid I/O contention. If the number of dummy cycles and AX bits cycles cles.
are same, then X should be Hi-Z.^
(^) Figure 8.10 Fast Read Dual I/O AX Read Sequence (BBh [EXTADD=1] or BCh, 4-byte address)

30
CE#
SCK
(^20)
4 - byte Address
28 26 ...
Mode 3 0 1 2 3 ...^1516171819202122232425
Mode 0

31 29 27 ...^31
IO 0
IO 1
4 Dummy Cycles
6
7
(^64)
7 5
(^20)
3 1
tV Data Out 1
(^64)
7 5
(^20)
3 1

4
5
Mode Bits
...
...
Data Out 2
...
Notes:
If the mode bits=AXh (where X is don’t care), it will keep executing the AX read mode (without command) mode bits are different from AXh, the device exits the AX read operation.. When the
2.3. Number of dummy cycles depends on clock speed. Detailed infSufficient dummy cycles are required to avoid I/O contention. ormation in Table 6.11 Read Dummy Cycles.If the number of dummy cycles and AX bits cycles
are same, then X should be Hi-Z.^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 64
8.7 FAST READ DUAL OUTPUT OPERATION (FRDO, 3Bh or 4FRDO, 3Ch)...........................................
T he FRDO/4FRDO instruction is used to read memory data on two output pins each at up to a 166 MHz clock.
• • 3Bh (EXTADD=0) is followed by a 33Bh (EXTADD=1) is followed by a 4--byte address (A23byte address (A31--A0) orA0) or (^)

• 3Ch is followed by a 4-byte address (A31-A0)
T(configurable, default is 8 clocks)he FRDO/4FRDO instruction c,o trdane (^) sis mifttedollo wedvia t (^) hbey IO0 thr elie or four addne, with each briet slats (^) cbhyetesd-i (^) nas above during thea rndising du edgemmy of cyclesSCK. (^)
Tmhenaxim thuem fifrsrequent datac by yfCteT (^) , aduddrirngess tedhe is falslinhgift eeddge out of oSn (^) CthKe. IO1The and firs (^) t bIO0it (liMSBnes,) wis ouith etputach on paIO1ir of. bSiits muslhtaifntedeou osulty, at a the

s econd bit is output on IO0.
Teahech f ibrsytte b yof datate addr eis sssedhif (^) tedcan o be atut. W anheny mtheem hoigry helosct addation.re (^) sTshe is addrearcehsed,s is theau toamddatreicsasl lyc (^) ounterincrem wented by one aill roll over to thefter (^)
(^0) F (^00) RDO/4FRDO 0 00h addre is terminatedss, allowing the by endritvirieng m CeEm#o hryigh to (be VIHread). with a single FRDO/4FRDO instruction. The instruction
(^) If the FRDO/4FRDO instruction is issued while an Erase, Program or Write cycle is in process (WIP=1) the

i nstruction is ignored and will not have any effects on the current cycle.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 65
Figure 8.11 Fast Read Dual Output Sequence (3Bh [EXTADD=0], 3-byte address)
CE#
SCK
7 5
Data Out 1
Instruction = 3 Bh 23
CE#
SCK
3 2 1 0
3 - byte Address
High Impedance
22 21 ...
0 1 2 3 4 5 6 7 8 9 10 ... 28 29 30 31
32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
Mode 3
Mode 0
...
tV
IO 0
IO 1
6 4
3 1 7 5
2 0 6 4
3 1 ...
2 0 ...
Data Out 2
IO 0
IO 1
8 Dummy Cycles
(^) Note: Dummy cycles depends on Read Parameter setting. Detailed information in Table 6.11 Read Dummy Cycles.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 66
Figure 8.12 Fast Read Dual Output Sequence (3Bh [EXTADD=1] or 3Ch, 4-byte address)
Instruction = 3 Bh/ 3 Ch
4 - byte Address
36 37 38 39
40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 ...
CE#
SCK
7 5
Data Out 1
31
CE#
SCK
3 2 1 0
High Impedance
30 29 ...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...
Mode 0
tV
IO 0
IO 1
6 4
3 1 7 5
2 0 6 4
3 1 ...
2 0 ...
Data Out 2
IO 0
IO 1
8 Dummy Cycles
Note: Dummy cycles depends on Read Parameter setting. Detailed information in Table 6.11 Read Dummy Cycles.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 67
8.8 FAST READ QUAD OUTPUT OPERATION (FRQO, 6Bh or 4FRQO 6Ch)
The FRQO/clock. 4FRQO instruction is used to read memory data on four output pins each at up to a 166 MHz
(^) • 6Bh (EXTADD=0) is followed by a 3-byte address (A23-A0) or

• • 6Bh (EXTADD=1) is followed by a 46Ch is followed by a 4 - byte address (A31-byte address (A31-A0) - A0) or
(^) The FRQO/4FRQO instruction code is followed by three or four address bytes as above and dummy cycles

(configurable, default is 8 clocks)edge of SCK. Then the first data byte addressed is shifted out on the IO3, IO2, IO1 and IO0 lines, with , transmitted via the IO0 line, with each bit latched-in during the rising
each group of four bits shifted out at a maximum frequency fbit (MSB) is output on IO3, while simultaneously the second bit isCT, during the falling edge of SCK. The first output on IO2, the third bit is output on
IO1, etc.
The first byte addressed can be at any memory location. The address is automatically incremented after each byte of data is shifted out. When the highest address is reached, the address counter will roll over
to the 000000h address, allowing the entire memory to be read with a single FRQO/FRQO/4FRQO instruction is terminated by driving CE# high (VIH). 4FRQO instruction.
(^) If a FRQO/4FRQO instruction is issued while an Erase, Program or Write cycle is in process (WIP=1) the

instruction is ignored and will not have any effects on the current cycle.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 68
Figure 8.13 Fast Read Quad Output Sequence (6Bh [EXTADD=0], 3-byte address)
CE#
SCK
5 1
Data Out 1
Instruction = 6 Bh 23
CE#
SCK
3 2 1 0
3 - byte Address
High Impedance
22 21 ...
0 1 2 3 4 5 6 7 8 9 10 ... 28 29 30 31
32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
Mode 3
Mode 0
...
tV
IO 0
IO 1
4 0
5 1 5 1
4 0 4 0
5 1 ...
IO 0 4 0 ...
IO 1
8 Dummy Cycles
IO 2 High Impedance
IO 3 High Impedance
7 3
6 2
7 3 7 3
6 2 6 2
7 3 ...
IO 2 6 2 ...
IO 3
Data Out 2 Data Out 3 Data Out 4
Note: Dummy cycles depends on Read Parameter setting. Detailed information in Table 6.11 Read Dummy Cycles.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 69
Figure 8.14 Fast Read Quad Output Sequence (6Bh [EXTADD=1] or 6Ch, 4-byte address)
CE#
0 1 2 3 4 5 6 7 8 9 10 ... 36 37 38 39
40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55
Mode 3
...
CE#
Instruction = 6 Bh/ 6 Ch 31
SCK
3 2 1 0
4 - byte Address
High Impedance
30 29 ...
Mode 0
IO 0
IO 1
IO 2 High Impedance
IO 3 High Impedance
SCK
5 1
Data Out 1
tV
4 0
5 1 5 1
4 0 4 0
5 1 ...
IO 0 4 0 ...
IO 1
8 Dummy Cycles
7 3
6 2
7 3 7 3
6 2 6 2
7 3 ...
IO 2 6 2 ...
IO 3
Data Out 2 Data Out 3 Data Out 4
Note: Dummy cycles depends on Read Parameter setting. Detailed information in Table 6.11 Read Dummy Cycles.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 70
8.9 FAST READ QUAD I/O OPERATION (FRQIO, EBh or 4FRQIO, ECh)
The FRQIO/4FRQIO instruction allows the address bits to be input four bits at a time.be executed directly from the SPI in some applications. This may allow for code to
(^) • EBh (EXTADD=0) is followed by a 3-byte address (A23-A0) or

• • EBh (EXTADD=1) is followed by a 4ECh is followed by a 4-byte address (A31-byte address (A31-A0) - A0) or
(^) The FRQIO/4FRQIO instruction code is followed by three or four address bytes as above and dummy cycles

(configlatchedurable, default is 6 clocks)-in during the rising edge of SCK. The address, transmitted via the IO3, IO2, IO1 and IO0 lines, with each group of four bits of MSB inputs on IO3, the next bit on IO2, the next bit on
IO1, the next bit on IO0, and contioperation mode, a mode byte may be located after address input.nue to shift in alternating on the four. Depending on the usage of AX read
(^) The first data byte addressed is shifted out on the IO3, IO2, IO1 and IO0 lines, with each group of four bits shifted

out at a maximum frequency fsimultaneously the second bit is output on IO2, the third bit is output on IO1, etc. Figures CT, during the falling edge of SCK. The first bit (MSB) is output on IO3, while 8.15 and 8.16 illustrates
the timing sequence.
The fof data is shifted out. When the highest address is reached, the address counter will roll over to the 000000h irst byte addressed can be at any memory location. The address is automatically incremented after each byte
address, allowing the entire memory tinstruction is terminated by driving CE# high (Vo be read with a single FRQIO/4FRQIO instruction. FRQIO/4FRQIO IH).
(^) The device supports the AX read operation by applying mode bits during dummy period. Mode bits consist of 8

bits, such as M7 to M0. Two cycles after address input are reserved for Mode bits in FRQIO/4FRQIO execution. M7 to M4 are important for enabling this mode. M3 to M0 become don’t care for future use. When M[7:4]=1010(Ah),
it enables the AX read operation and subsequent FRQIO/4FRQIO execution skips command code. It saves cycles as described in Figures 8.17 and 8.18. When the code is different from AXh (where X is don’t care), the device
exits the AX read operation. After finishing the read operation, device becomes ready to receive a new command. SPI or QPI mode configuration retains the prior setting. Mode bit must be applied during dummy cycles. Number
of dummy cycles in Table 6.11 includes number of mode bit cycles. If dummy cycles are configured as 6 cycles, data output will start right after mode bits and 4 additional dummy cycles are applied.
(^) If the FRQIO/4FRQIO instruction is issued while an Erase, Program or Write cycle is in process (WIP=1) the

instruction is ignored and will not have any effects on the current cycle.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 71
Figure 8.15 Fast Read Quad I/O Sequence (EBh [EXTADD=0], 3-byte address)
CE#
SCK
5 1
Data Out 1
Instruction = EBh 20
CE#
SCK
4 0 4 0
3 - byte Address
High Impedance
16 12 8
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
Mode 3
Mode 0
...
tV
IO 0
IO 1
4 0
5 1 5 1
4 0 4 0
5 1
IO (^040)
IO 1

21 17 13 9 5 1 5 1
22 18 14 10 6 2 6 2
23 19 15 11 7 3 7 3
Mode Bits
IO 2
IO 3
6 2 6 2 6 2 6 2
7 3 7 3 7 3 7 3
Data Out 2 Data Out 3 Data Out 4
IO 2
IO 3
1
0
5 1 ...
4 0 ...
2 6 2 ...
3 7 3 ...
5
4
6
7
6 Dummy Cycles Data Out 5 Data Out 6
Notes:1. If the mode bits=AXh (^) (where X is don’t care), it can execute the AX read mode (without command). When the mode

bits are different from AXh, the device exits the AX read operation.Number of dummy cycles depends on clock speed. Detailed information in Table 6.11 Read Dummy Cycl^ es.
Sufficient dummy cycles are required to avoid I/O contention.are same, then X should be Hi-Z. If the number of dummy cycles and AX bits cycles
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 72
Figure 8.16 Fast Read Quad I/O Sequence (EBh [EXTADD=1] or ECh, 4-byte address)
CE#
SCK
5 1
Data Out 1
Instruction = EBh/ECh 20
CE#
SCK
28 24 4 0
4 - byte Address
High Impedance
16 12 8
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
Mode 3
Mode 0
...
tV
IO 0
IO 1
4 0
5 1
4 0
(^51)
IO (^040)
IO 1

29 25 21 17 13 9 5 1
30 26 22 18 14 10 6 2
31 27 23 19 15 11 7 3
IO 2
IO 3
6 2 6 2 6 2
7 3 7 3 7 3
Data Out 2 Data Out 3
IO 2
IO 3
1
0
5 1 ...
4 0 ...
2 6 2 ...
3 7 3 ...
5
4
6
7
6 Dummy Cycles Data Out 4 Data Out 5
4 0
5 1
6 2
7 3
Mode Bits^
Notes:1. If the mode bits=AXh (where X is don’t care), it can execute the AX read mode (without command) (^). When the mode

bits are different from AXh, the device exits the AX read operation.Number of dummy cycles depends on clock speed. Detailed information in Tabl^ e 6.11 Read Dummy Cycles.
Sufficient dummy cycles are required to avoid I/O contention.are same, then X should be Hi-Z. If the number of dummy cycles and AX bits cycles
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 73
Figure 8.17 Fast Read Quad I/O AX Read Sequence (EBh [EXTADD=0], 3-byte address)
20
CE#
SCK
(^4040)
3 - byte Address
16 12 8
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
IO 0
IO (^121171395151)
22 18 14 10 6 2 6 2
23 19 15 11 7 3 7 3
Mode Bits

IO 2
IO 3
5 1
4 0
5 1
4 0
6 2 6 2
(^7373)

...
...
...
...
Data Out 1 Data Out 2
...
6 Dummy Cycles tV
Notes:
If the mode bits=AXh (where X is don’t care), it will keep executing the AX read mode (without command) mode bits are different from AXh, the device exits the AX read operation.. When the
2.3. Number of dummy cycles depends onSufficient dummy cycles are required to avoid I/O contention. clock speed. Detailed information in Table 6.11 Read Dummy Cycles. If the number of dummy cycles and AX bits cycles
are same, then X should be Hi-Z.^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 74
Figure 8.18 Fast Read Quad I/O AX Read Sequence (EBh [EXTADD=1] or ECh, 4-byte address)
20
CE#
SCK
(^4040)
4 - byte Address
16 12 8
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
IO 0
IO (^121171395151)
22 18 14 10 6 2 6 2
23 19 15 11 7 3 7 3

IO 2
IO 3
5 1
4 0
6 2
7 3
...
...
...
...
Data Out 1
...
28 24 6 Dummy Cycles tV
29 25
30 26
31 27
Notes: Mode Bits^
If the mode bits=AXh (where X is don’t care), it will keep executing the AX read mode (without command) mode bits are different from AXh, the device exits the AX read operation.. When the
2.3. Number of dummy cycles depends on clock speed. Detailed information in Table 6.11 Read Dummy Cycles.Sufficient dummy cycles are required to avoid I/O contention. If the number of dummy cycles and AX bits cycles
are same, then X should be Hi-Z.^
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 75
FAST READ QUAD I/O OPERATION IN QPI MODE (FRQIO, EBh or 4FRQIO, ECh)
The FRQIO/ 4FRQIO instruction in QPI mode is used to read memory data at up to a 200MHz clock.
The FRQIO/clocks are required, while the FRQIO/4FRQIO instruction in QPI mode4FRQIO utilizes all four IO lines to input the instruction code so that only two instruction requires that the byte-long instruction code is shifted into
the device only via IO0 line in eight clocks. As a result, 6 comQPI instruction. In addition, subsequent address and data out are shifted in/out via all four IO lines like the mand cycles will be reduced by the FRQIO/4FRQIO
FRQIO/4FRQIO exactly same as the FRQIO/4FRQIO operation in SPI mode.instruction. In fact, except for the command cycle, the FRQIO/4FRQIO operation in QPI mode is
(^) The device supports the AX read operation by applying mode bits during dummy period. Mode bits consist of 8

bits, such as M7 to M0. Two cycles after address input are reserved for Mode bitM7 to M4 are important for enabling this mode. M3 to M0 become don’t care for future use. When M[7:4]=1010(Ah), s in FRQIO/4FRQIO execution.
it enables the AX read operation and subsequent FRQIO/4FRQIO execution skips command code. It saves cycles as described in Figures 8.17 and 8.18. When the code is different from AXh (where X is don’t care), the device
exits the AX read operation. After finishing the read operation, device becomes ready to receive a new command. SPI or QPI mode configuration retains the prior setting. Mode bit must be applied during dummy cycles. Number
of dummy cycles in Table 6.11 includes number of mode bit cycles. If dummy cycles are configured as 6 cycles, data output will start right after mode bits and 4 additional dummy cycles are applied.
(^) If the FRQIO/4FRQIO instruction in QPI mode is issued while an Erase, Program or Write cycle is in process

(WIP=1) the instruction is ignored and will not have any effects on the current cycle.
Figure 8.19 Fast Read Quad I/O Sequence In QPI Mode (EBh [EXTADD=0], 3-byte address)
EBh
CE#
SCK
IO[ 3 : 0 ]
3 - byte Address 6 Dummy Cycles
0 1 2 3 4 5 6 7 8 9
...
Mode 3 13 14 15 16 17
Mode 0
23 : (^207) : 4 3 : 0 7 : 4 3 : 0
Data 1 Data 2

19 : 1615 : 1211 : 8 7 : 4 3 : 0
...
tV
Instruction
Mode Bits
7 : 4 3 : 0
...
Notes:
If the mode bits=AXh (where X is don’t care), it can execute the AX read mode (without command) bits are different from AXh, the device exits the AX read operation.. When the mode
Number of Cycles. dummy cycles depends on Read Parameter setting. Detailed information in Table 6.11 Read Dummy
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 76
Figure 8.20 Fast Read Quad I/O Sequence In QPI Mode (EBh [EXTADD=1] or ECh, 4-byte address)
EBh/ECh
CE#
IO[ 3 : 0 ]
4 - byte Address 6 Dummy Cycles
0 1 2 3 4 5 6 7 8 9
...
Mode 3 11 ...^151617
Mode 0
31 : 28 7 : 4 3 : 0 7 : 4 3 : 0
Data 1
27 : 2423 : 2018 : 1615 : 12 11 : 8
...
tV
Instruction
Mode Bits
7 : 4 3 : 0
10
SCK
Notes:
If the mode bits=AXh (where X is bits are different from AXh, the device exits the AX read operation. don’t care), it can execute the AX read mode (without command). When the mode
Number of dummy cycles depends on Read ParameterCycles. setting. Detailed information in Table 6.11 Read Dummy
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 77
8.10 PAGE PROGRAM OPERATION (PP, 02h or 4PP, 12h)......................................................................
The Page Program (PP/4PP) instruction allows up to 256 bytes data to be programmed into memory in a single operation. The destination of the memory to be programmed must be outside the protected memory area set by
the Block Protection bits page that is write-protected will be ignored. Before the execution of PP/4PP instruction, the Write Enable Latch (BP3, BP2, BP1, BP0) or ASP. A PP/4PP instruction which attempts to program into a
(WEL) must be enabled thro ugh a Write Enable (WREN) instruction.
• • 02h (EXTADD=0) is followed by a 302h (EXTADD=1) is followed by a 4--byte address (A23byte address (A31--A0) orA0) or (^)

• 12h is followed by a 4-byte address (A31-A0)
The PP/4PP instruction code, three or four address the SI line. Program operation will start immediately after the CE# is brought high, otherwise the PP/4PP instruction bytes as above and program data (1 to 256 bytes) are input via
will not be executed. The internal control logic automatically handles the progress or completion of the program operation can be determined by reading the WIP bit. If the WIP bit is “1”, programming voltages and timing. The
the program operation is still in progress. If WIP bit is “0”, the program operation has completed.
If molatched data are discarded, and the last 256 bytes are kept to be programmed into the page. The starting byte can re than 256 bytes data are sent to a device, the address counter rolls over within the same page, the previously
be anywhere within the page. of the same page. If the data to be programmed are less than a full page, the data of all other bytes on the same When the end of the page is reached, the address will wrap around to the beginning
page will remain unchanged.
Note: (^) once, to incrementally change A program operation can a lter “1”s into “0”“1” s to “0”s. An erase operation is required to change “0 s. The same byte location or page may be programmed more than ”s to “1” s.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 78
Figure 8.21 Page Program Sequence (02h [EXTADD=0], 3-byte address)
Instruction = 02 h 23
CE#
SCK
SI 7 6
SO
7
3 - byte Address
High Impedance
22 ...^0
Data In 1 Data In 256
Mode 3 0 1 ...^789 ...^313233 ...^39 ... 2072 ... 2079
Mode 0
... 0 ... ... 0
(^) Figure 8.22 Page Program QPI Sequence (02h [EXTADD=0], 3-byte address)
02 h

CE#
SCK
IO[ 3 : 0 ]
3 - byte Address
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
23 : 20 7 : 4 3 : 0 7 : 4 3 : 0
Data In 1 Data In 2
19 : 1615 : 1211 : 8 7 : 4 3 : 0 7 : 4 3 : 0 7 : 4 3 : 0
Data In 3 Data In 4
...
...
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 79
Figure 8.23 Page Program Sequence In SPI Mode (02h [EXTADD=1] or 12h, 4-byte address)
Instruction = 02 h/ 12 h 31
CE#
SCK
SI (^76)
SO

7
4 - byte Address
High Impedance
30 ...^0
Data In 1 Data In 256
Mode 3 0 1 ...^789 ...^394041 ...^47 ... 2080 ... 2087
Mode 0
... 0 ... ... 0
(^) Figure 8.24 Page Program Sequence In QPI Mode (02h [EXTADD=1] or 12h, 4-byte address)
02 h/ 12 h

CE#
SCK
IO[ 3 : 0 ]
4 - byte Address
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
31 : 28 7 : 4 3 : 0 7 : 4 3 : 0
Data In 1
27 : 2423 : 2019 : 1615 : 12 11 : 8 7 : 4 3 : 0 7 : 4 3 : 0
Data In 2 Data In 3
...
...
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 80
8.11 QUAD INPUT PAGE PROGRAM OPERATION (PPQ, 32 h/38h or 4PPQ, 34h/3Eh)
The operationQuad Input with four pins (IO0, IO1, IO2 and IO3)Page Program instruction allows up to 256 bytes data to be programmed into memory in a. The destination of the memory to be programmed must be outside single
the protected memory area set by the Block Protection (Program instruction which attempts to program into a page that is writeBP3, BP2, BP1, BP0) bits or ASP. A -protected will be ignored. Before the Quad Input Page
execution of Write Enable Latch (WEL) must be enabled through a Write Enable (Quad Input Page Program instruction, the QE bit in the Status Register must be set to “1” and WREN) instruction. the
(^) • 32h/38h (EXTADD=0) is followed by a 3-byte address (A23-A0) or

• • 32h/38h (EXTADD=1) is followed by a 434h/3Eh is followed by a 4-byte address (A31-byte address (A31-A0) - A0) or
(^) The Quad Input Page Program instruction code, three or four address bytes as above and program data (1 to 256

bytes) are input via the four pins (IO0, IO1, IO2 and IO3). Program operation will start immediately after the CE# is brought high, otherwise the Quad Input Page Program instruction will not be executed. The internal control logic
automatically handles the programming voltages and timing. The progress or completion of the program operation can be determined by reading the WIP bit. If the WIP bit is “1”, the program operation is still in progress. If WIP bit
is “0”, the program operation has completed.
If more than 256 bytes data are sent to a device, the address counter rolls over within the same page, the previously latched data are discarded, and the last 256 bytes data are kept to be programmed into the page. The starting byte
can be anywhere within the page. When the end of the page is reached, the address will wrap around to the beginning of the same page. If the data to be programmed are less than a full page, the data of all other bytes on
the same page will remain unchanged.
Note: (^) once, to incrementally change A program operation can alter “1”s into “0”“1” s to “0”s. An erase operation is required to change “0 s. The same byte location or page may be programmed more than ”s to “1” s.
(^) Figure 8.25 Quad Input Page Program operation (32h/38h [EXTADD=0], 3-byte address)
Instruction = 32 h/ 38 h 23

CE#
SCK
4 0 4 0
3 - byte Address
High Impedance
22 ... 0
Mode 3 0 1 2 3 4 5 6 7 8 9 31 32 33 34 35
Mode 0
IO 0
IO (^15151)
6 2 6 2
7 3 7 3
Data In 2

IO 2
IO 3
...
Data In 1
...
...
...
...
...
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 81
Figure 8.26 Quad Input Page Program operation (32h/38h [EXTADD=1] or 34h/3Eh, 4-byte address)
31
4 - byte Address
30
39 40 41 42 43
Instruction = 32 h/ 38 h/ 34 h/ 3 Eh
CE#
SCK
4 0 4 0
High Impedance
... 0
Mode 3 0 1 2 3 4 5 6 7 8 9
Mode 0
IO 0
IO (^15151)
6 2 6 2
7 3 7 3
Data In 2

IO 2
IO 3
Data In 1
8.12 ERASE OPERATION
The Erase command sets all bits in the addressed sector or block to “1”s.
(^) The memory array of the device is organized into uniform 4 Kbyte sectors or 32/64 Kbyte uniform blocks (a block

consists of eight/sixteen adjacent sectors respectively).
(^) Before a byte is reprogrammed, the sector or block that contains the byte must be erased (erasing sets bits to “1”).

In order to erase the device, there are three erase instructions available: Sector Erase (SER), Block Erase (BER), and Chip Erase (CER). A sector erase operation allows any individual sector to be erased without affecting the
data in other sectors. A block erase operation erases any individual block. A chip erase operation erases the whole memory array of a device. A sector erase, block erase, or chip erase operation can be executed prior to any
programming operation.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 82
8.13 SECTOR ERASE OPERATION (SER, D7h/20h or 4SER, 21h)
A the Write Enable Latch (WEL) mSector Erase (SER/4SER) instruction erases a 4 Kbyte sector before the execution of a ust be set via a Write Enable (WREN) instruction. The WEL bit is automatically SER/4SER instruction,
reset after the completion of Sector Erase operation.
• • D7h/20h (EXTADD=0) is followed by a 3D7h/20h (EXTADD=1) is followed by a 4--byte address (A23byte address (A31--A0) orA0) or (^)

• 21h is followed by a 4-byte address (A31-A0)
A SEinstruction sequence The SER/4SER instruction is entered, after CE# is pulled low to select the device and stays low during the entire R/4SER instruction code, and three or four address bytes as above are input via SI.
Erase operation will start immediately after CE# is pulled high. The internal control logic automatically handles the erase voltage and timing.
(^) The progress or completion of the erase operation can be determined by reading the WIP bit. If the WIP bit is “1”,

the erase operation is still in progress. If the WIP bit is “0”, the erase operation has been completed.
Figure 8.27 Sector Erase Sequence (D7h/20h [EXTADD=0], 3-byte address)
Instruction = D 7 h/ 20 h 23
CE#
SCK
SI 3 2
SO
1 0
3 - byte Address
High Impedance
22 21 ...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...^28293031
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 83
Figure 8.28 Sector Erase Sequence (D7h/20h [EXTADD=1] or 21h, 4-byte address)
31 30 29
36 37 38 39
Instruction = D 7 h/ 20 h/ 21 h
CE#
SCK
SI 3 2
SO
1 0
4 - byte Address
High Impedance
...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...
Mode 0
(^) Figure 8.29 Sector Erase Sequence In QPI Mode (D7h/20h [EXTADD=0], 3-byte address)
D 7 h/ 20 h

CE#
SCK
IO[ 3 : 0 ]
3 - byte Address
Mode 3 0 1 2 3 4 5 6 7
Mode 0
23 : 2019 : 1615 : 1211 : 8 7 : 4 3 : (^0)
(^)

Figure 8.30 Sector Erase Sequence In QPI Mode (D7h/20h [EXTADD=1] or 21h, 4-byte address)
CE#
4 - byte Address
31 : 2827 : 2423 : 2019 : 1615 : 1211 : 8 7 : 4 3 : 0
8 9
20 Dh^7 / 21 h/h
SCK
IO[ 3 : 0 ]
Mode 3 0 1 2 3 4 5 6 7
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 84
8.14 BLOCK ERASE OPERATION (BER32K:52h or 4BER32K:5Ch, BER64K:D8h or 4BER64K:DCh)
A Block Erase (BER) instruction erases a Enable Latch (WEL) must be set via a Write Enable (WREN) instruction. The WEL is reset automatically after the 32/64 Kbyte block. Before the execution of a BER instruction, the Write
completion of a block erase operation.
• • 52h/D8h (EXTADD=0) is followed by a 352h/D8h (EXTADD=1) is followed by a 4--byte address (A23byte address (A31--A0) orA0) or (^)

• 5Ch/DCh is followed by a 4-byte address (A31-A0)
The BER instruction code and three or four address bytes as above are input via SI. Erase operation will start immediately after the CE# is pulled high, otherwise the BER instruction will not be executed. The internal control
logic automatically handles the erase voltage and timing.
Figure 8.31 Block Erase (64K) Sequence (D8h [EXTADD=0], 3-byte address)
Instruction = D 8 h 23
CE#
SCK
SI 3 2
SO
1 0
3 - byte Address
High Impedance
22 21 ...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...^28293031
Mode 0
Figure 8.32 Block Erase (64K) Sequence (D8h [EXTADD=1] or DCh, 4-byte address)
31
4 - byte Address
29 28
36 37 38 39
Instruction = D 8 h/DCh
CE#
SCK
SI (^32)
SO

1 0
High Impedance
...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 85
Figure 8.33 Block Erase (64K) Sequence In QPI Mode (D8h [EXTADD=0], 3-byte address)
D 8 h
CE#
SCK
IO[ 3 : 0 ]
3 - byte Address
Mode 3 0 1 2 3 4 5 6 7
Mode 0
23 : 2019 : 1615 : 1211 : 8 7 : 4 3 : (^0)
(^)

Figure 8.34 Block Erase (64K) Sequence In QPI Mode (D8h [EXTADD=1] or DCh, 4-byte address)
D 8 h/DCh
CE#
SCK
IO[ 3 : 0 ]
4 - byte Address
Mode 3 0 1 2 3 4 5 6 7
Mode 0
31 : 2827 : 2423 : 2019 : 1615 : 1211 : 8 7 : 4 3 : 0
8 9
(^) Figure 8.35 Block Erase (32K) Sequence (52h [EXTADD=0], 3-byte address)
Instruction = 52 h 23

CE#
SCK
SI 3 2
SO
1 0
3 - byte Address
High Impedance
22 21 ...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...^28293031
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 86
Figure 8.36 Block Erase (32K) Sequence (52h [EXTADD=1] or 5Ch, 4-byte address)
Instruction = 52 h/ 5 Ch 31
CE#
SCK
SI 3 2
SO
1 0
4 - byte Address
High Impedance
29 28 ...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...^36373839
Mode 0
(^) Figure 8.37 Block Erase (32K) Sequence In QPI Mode (52h [EXTADD=0], 3-byte address)
52 h

CE#
SCK
IO[ 3 : 0 ]
3 - byte Address
Mode 3 0 1 2 3 4 5 6 7
Mode 0
23 : 2019 : 1615 : 1211 : 8 7 : 4 3 : (^0)
(^)

Figure 8.38 Block Erase (32K) Sequence In QPI Mode (52h [EXTADD=1] or 5Ch, 4-byte address)
52 h/ 5 Ch
CE#
SCK
IO[ 3 : 0 ]
4 - byte Address
Mode 3 0 1 2 3 4 5 6 7
Mode 0
31 : 2827 : 2423 : 2019 : 1615 : 1211 : 8 7 : 4 3 : 0
8 9
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 87
8.15 CHIP ERASE OPERATION (CER, C7h/60h)
A Chip Erase (CEnable Latch (WEL) must be set via a Write Enable (WREN) instruction. The WEL is automatically reset after ER) instruction erases the entire memory array. Before the execution of CER instruction, the Write
completion of a chip erase operation.
The Cotherwise the CER instruction will not be executed. The internal control logic automatically handles the erase ER instruction code is input via the SI. Erase operation will start immediately after CE# is pulled high,
voltage and timing.
Chip Erase (CER) insbits are not 0, the CER command is not executed and E_ERR and PROT_E are set.truction can be executed only when Block Protection (BP3~BP0) bits are set to 0s. If the BP
(^) Chip Erase (CER) instruction will skip sectors/blocks protected by ASP (DYB bits or PPB bits) and will not set

E_ERR and PROT_E if sectors/blocks are protected by ASP only.
(^) Figure 8.39 Chip Erase Sequence In SPI Mode
Instruction = C 7 h/ 60 h

CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High Impedance^
(^) Figure 8.40 Chip Erase Sequence In QPI Mode
C 7 h/ 60 h

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 88
8.16 WRITE ENABLE OPERATION (WREN, 06h)
The Write Enable (WREN) instruction is used to set the Write Enable Latch (WEL) bit. The WEL bit is reset to the write-protected state after power-up. The WEL bit must be write enabled before any write operation, including
Sector Erase, Block Erase, Chip EFunction Register, Set Non-Volatilerase, Page Program, Program Information Row, Write Status Register, Write Read Register, Set Non-Volatile Extended Read Register, Write Autoboot
Register operationsreset to the write-protected state automatically upon completion of a write operation. The WREN instruction is , Set Volatile Read Register and Set Volatile Extended Read Register. The WEL bit will be
required before any above operation is executed.
(^) Figure 8.41 Write Enable Sequence In SPI Mode
Instruction = 06 h

CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High Impedance^
(^) Figure 8.42 Write Enable Sequence In QPI Mode
06 h

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 89
8.17 WRITE DISABLE OPERATION (WRDI, 04h)
The Write Disable (WRDI) instruction resets the WEL bit and disables all write instructions. The WRDI instruction is not required after the execution of a write instruction, since the WEL bit is automatically reset.
(^) Figure 8.43 Write Disable Sequence In SPI Mode
Instruction = 04 h

CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High Impedance^
(^) Figure 8.44 Write Disable Sequence In QPI Mode
04 h

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 90
8.18 READ STATUS REGISTER OPERATION (RDSR, 05h)
The Read Status Register (RDSR) instruction provides access to Status Register. During the execution of a program, erase or Write Status Register operation, the RDSR instruction (^) will be executed,

which can be used to check the progress or completion of an operation by reading the WIP bit.
Figure 8.45 Read Status Register Sequence In SPI Mode
Instruction = 05 h
7
CE#
SCK
SI
SO 3 2 1 0
Data Out
6 5
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
4
tV
Figure 8.46 Read Status Register Sequence In QPI Mode
05 h
Mode 3 0 1
Mode 0
2 3
7 : 4 3 : 0
CE#
SCK
IO[ 3 : 0 ]
tV
Data Out^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 91
8.19 WRITE STATUS REGISTER OPERATION (WRSR, 01h)
The Write Status Register write protection features by writing “0”s or “1”s into Register (WRSR) instruction allows the user to enable or disable the block protection and Status BP3, BP2, BP1, BP0, and SRWD bits. Also WRSR
instruction allows the user to disable or enable qTo write Status Register bits, a standard Write Enable (06h) instruction must previously have been executeduad operation by writing “0” or “1” into QE bit. (^) for

the device to accept Write Status Register (01h) instruction (Status Register bit WEL must equal 1).
Figure 8.47 Write Status Register Sequence In SPI Mode
Instruction = 01 h
CE#
SCK
SI
SO
Data In
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
7 6 5 4 3 2 1 0
High Impedence
(^)

Figure 8.48 Write Status Register Sequence In QPI Mode
01 h
Mode 3 0 1
Mode 0
2 3
7 : 4 3 : 0
CE#
SCK
IO[ 3 : 0 ]
Data In^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 92
8.20 READ FUNCTION REGISTER OPERATION (RDFR, 48h)
The Read Function Register Bit Definition for more detail.Function Register (RDFR) instruction provides access to the Function Register. Refer to Table 6.6
(^) Figure 8.49 Read Function Register Sequence In SPI Mode
Instruction = 48 h
7

CE#
SCK
SI
SO 3 2 1 0
Data Out
6 5
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
4
tV
Figure 8.50 Read Function Register Sequence In QPI Mode
48 h
Mode 3 0 1
Mode 0
2 3
7 : 4 3 : 0
CE#
SCK
IO[ 3 : 0 ]
tV
Data Out^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 93
8.21 WRITE FUNCTION REGISTER OPERATION (WRFR, 42h)...............................................................
The Write SOIC or 24 ball TFBGA by setting Dedicated Function Register (WRFR) instruction allows the user to disable dedicated RESET# pin or ball on 16RESET# Disable bit to “1”. Also Information Row Lock bits -pin
(IRL3~IRL0) can be set to “1” individually by WRFR instruction in order to lock Information Row.Since Dedicated RESET# Disable bit and IRL bits are OTP, once they are set to “1”, they cannot be set (^) back to “0”

again
(^) Figure 8.51 Write Function Register Sequence In SPI Mode
Instruction = 42 h

CE#
SCK
SI
SO
Data In
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
7 6 5 4 3 2 1 0
High Impedence
(^)

Figure 8.52 Write Function Register Sequence In QPI Mode
42 h
Mode 3 0 1
Mode 0
2 3
7 : 4 3 : 0
CE#
SCK
IO[ 3 : 0 ]
Data In^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 94
8.22 ENTER QUAD PERIPHERAL INTERFACE (QPI) MODE OPERATION (QPIEN, 35h; QPIDI,F5h)
The Enter QPI (QPIEN) instruction, 35h, enables the Flash device for QPI bus operation. Upon completion of the instruction, all instructions thereafter will be 4-bit multiplexed input/output until a power cycle or an Exit QPI
instruction is sent to device.
The Exit QPI instruction, F5the host drives CE# low, sends the Exit QPI command cycle, then drives CE# high. The device just accepts QPI (2 h, resets the device to 1-bit SPI protocol operation. To execute an Exit QPI operation,
clocks) command cycles.
Figure 8.53 Enter Quad Peripheral Interface (QPI) Mode Sequence
Instruction = 35 h
CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High Impedance^
(^) Figure 8.54 Exit Quad Peripheral Interface (QPI) Mode Sequence
F 5 h

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 95
8.23 PROGRAM/ERASE SUSPEND & RESUME
The device allows the interruption of Sector Erase, Blockoperations. 75h/B0h command for suspend and 7Ah/30h for resume Erase, or Page Program operations to co will be used. (SPI/QPI all acceptable)nduct other Function
Register bit2 (PSUS) and bit3 (ESUS) are used to check whether or not the device is in suspend mode.
Suspend to Resume to another suspend timingread ready timing (tSUS) : (t (^10) RS0μs): 8 0μs (MAX (TYP)) (^)
(^) SUSPEND DURING SECTOR-ERASE OR BLOCK-ERASE (PERSUS 75h/B0h)

The Suspend will be ignored during Chip Erase operation. command allows the interruption of Sector Erase and Block Erase operations. After the Suspend command, other commands But Suspend command include array read
operation can be accepted.
But Write Status Register commandarray read for being erased sector/block is not allowed. (01h) and Erase instructions are not allowed during Erase Suspend. Also,
(^) To execute Erase Suspend operation, the host drives CE# low, sends the Suspend command cycle (75h/B0h),

then drives CE# highfrom “0” to “1”, but the device will not accept another command until it is ready. To determine when the device will. The Function Register indicates that the Erase has been suspended by setting the ESUS bit
accept a new command, poll the WIP bit or wait Enable Latch (WEL) bit clears to “0”. the specified time tSUS. When ESUS bit is set to “1”, the Write
(^) SUSPEND DURING PAGE PROGRAMMING (PERSUS 75h/B0h)

The Suspend other commands command also include array read operation allows the interruption of all array Program operations. After the Suspend commcan be accepted can be accepted. and,
(^) But Write Status Register instruction (01h) and Program instructions are not allowed during Program Suspend.

Also, array read for being programmed page is not allowed.
To (75h/B0h), then drives CE# high. The Function Register indicates that the programming has been suspended by execute the Program Suspend operation, the host drives CE# low, sends the Suspend command cycle
settingwhen the device will accept a new command, poll the WIP bit or wait the specified time t the PSUS bit from “0” to “1”, but the device will not accept another command until it is ready. To determine SUS. When PSUS bit is set
to “1” , the Write Enable Latch (WEL) bit clears to “0”.
(^) PROGRAM/ERASE RESUME (PERRSM 7Ah/30h)

The Program/Erase Resume restarts the Program or Erase command that was suspended, and cstatus bit in the Function Register (ESUS or PSUS bits) to “0”. To execute the Program/Erase Resume operation, lears the suspend
the host drives CE# low, sends the Program/Erase Resume command cycle (7Ah/30h), then drives CE# high. A cycle is two nibbles long, most significant nibble first. To issue another Erase Suspend operation after Erase
ResumeErase time to complete Erase operation. operation, Erase Resume to another Erase Suspend delay (tRS) is required, but it could require longer
(^) To determine if the internal, self-timed Write operation completed, poll the WIP bit.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 96
Table 8.6Operation Instructions accepted during Suspend
Suspended (^) Name Hex Code Instruction Allowed^ Operation
Program or Erase NORD 03h Normal Read Mode

Program or Erase 4NORD 13h 4 - byte Address Normal Read Mode
Program or Erase FRD 0Bh Fast Read Mode
Program or Erase 4FRD 0Ch 4 - byte Address Fast Read Mode
Program or Erase FRDIO BBh Fast Read Dual I/O
Program or Erase 4FRDIO BCh 4 - byte Address Fast Read Dual I/O
Program or Erase FRDO 3Bh Fast Read Dual Output
Program or Erase 4FRDO 3Ch 4 - byte Address Fast Read Dual Output
Program or Erase FRQIO EBh Fast Read Quad I/O
Program or Erase 4FRQIO ECh 4 - byte Address Fast Read Quad I/O
Program or Erase FRQO 6Bh Fast Read Quad Output
Program or Erase 4FRQO 6Ch 4 - byte Address Fast Read Quad Output
Program or Erase FRDTR 0Dh Fast Read DTR Mode
Program or Erase 4FRDTR 0Eh 4 - byte Address Fast Read DTR Mode
Program or Erase FRDDTR BDh Fast Read Dual I/O DTR
Program or Erase 4FRDDTR BEh 4 - byte Address Fast Read Dual I/O DTR
Program or Erase FRQDTR EDh Fast Read Quad I/O DTR
Program or Erase 4FRQDTR EEh 4 - byte Address Fast Read Quad I/O DTR
Program or Erase WREN 06h Write Enable
Program or Erase WRDI 04hh Write Disable
Program or Erase RDSR 05h Read Status Register
Program or Erase RDFR 48h Read Function Register
Program or Erase RDBR 16h/C8h Read Bank Address Register
Program or Erase RDRP 61h Read Read Parameters (Volatile)
Program or EraseProgram or Erase RDERPRDID ABh81h Read Extended Read Read Manufacturer and Product IDParameters (Volatile)
Program or Erase RDJDID 9Fh Read Manufacturer and Product ID by JEDEC ID Command
Program or Erase RDMDID 90h Read Manufacturer and Device ID
Program or Erase RDJDIDQ AFh Read JEDEC ID QPI mode
Program or Erase RDUID 4Bh Read Unique ID Number
Program or Erase RDSFDP 5Ah SFDP Read
Program or Erase CLERP 82h Clear Extended Read Register
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 97
SuspendedOperation (^) Name Hex Code Instruction Allowed^ Operation
Program or Erase PERRSM 7Ah/30h Program/Erase Resume
Program or Erase SRPV C0/63h Set Read Parameters (Volatile)
Program or Erase SERPV 83h Set Extended Read Parameters (Volatile)
Program or Erase WRBRV 17h/C5 Write Bank Address Register (Volatile)
Program or Erase EN4B B7h Enter 4-byte Address Mode
Program or Erase EX4B 29 h Exit 4-byte Address Mode
Program or Erase RDPPB FCh Read PPB
Program or Erase 4RDPPB F2h 4 - byte Address Read PPB
Program or Erase RDDYB FAh Read DYB
Program or Erase 4RDDYB E0h 4 - byte Address Read DYB
Program or Erase RDPWD E7h Read Password
Program or Erase RDPLB A7h Read PPB Lock Bit
Program or Erase RDASP 2Bh Read ASP

Erase SECLOCK 24h Sector Lock
Erase SECUNLOCK 26h Sector Unlock
Erase 4SECUNLOCK 25h 4 - byte Address Sector Unlock
Erase PERSUS 75h/B0h Program/Erase Suspend
Erase PP 02h Serial Input Page Program
Erase 4PP 12h 4 - byte Address Serial Input Page Program
Erase PPQ 32h/38h Quad Input Page Program
Erase 4PPQ 34h/3Eh 4 - byte Address Quad Input Page Program
Erase WRDYB FBh Write DYB
Erase 4WRDYB E0h 4 - byte Address Write DYB
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 98
8.24 ENTER DEEP POWER DOWN (DP, B9h)
Theinto Power Deep Power-down mode). During this mode, standby current is reduced from I-down (DP) instruction is for setting the device on the minimizing the power consumption (enter sb1 to Isb2. While in the Power-down
mode, the device is not active and alldriving the CE# pin low and shifting the instruction code into the device. The CE# pin must be driven high after the Write/Program/Erase instructions are ignored. The instruction is initiated by
instruction has been latched, or Powermode will be entered within the time duration of t-down mode will not enDP. While in the Powergage. Once CE# pin driven high, the Power-down mode only the Release from Power-down -
down/RDID instruction, which restores the device to normal operation, will be recognized. All otheignored, including the Read Status Register instruction which is always available during normal operation. Ignoring r instructions are
all but one instruction makes the Power Down state a useful condition for securing maximum write protection. It is available in both SPI and QPI mode.
(^) Figure 8.55 Enter Deep Power Down Mode Sequence
Instruction = B 9 h

CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
tDP
SO High Impedance^
(^) Figure 8.56 Enter Deep Power Down Mode QPI Sequence
B 9 h

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
tDP
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 99
8.25 RELEASE DEEP POWER DOWN (RDPD, ABh)
The Release Deep Powerfrom the deep power-down mode, the instruction is issued by driving the CE# pin low, shifting the instruction code -down/Read Device ID instruction is a multi-purpose command. To release the device
into the device and driving CE# high.
Releasing the device from Powerand other instructions are accepted. The CE# pin must remain high during the t-down mode will take the time duration of tRES1 before normal operation is restored RES1 time duration. If the Release
Deep Powerinstruction is ignored and will not have any effects on the current cycle.-down/RDID instruction is issued while an Erase, Program or Write cycle is in progress (WIP=1) the
(^) Figure 8.57 Release Power Down Mode Sequence In SPI Mode

tRES 1
Instruction = ABh
CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High Impedance^
(^) Figure 8.58 Release Power Down Mode Sequence In QPI Mode

tRES 1
ABh
CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 100
8.26 SET READ PARAMETERS OPERATION (SRPNV: 65h, SRPV: C0h/63h)
(^) Set Read Parameter Bits
(^) This device supports configurable burst length and dummy cycles in both SPI and QPI mode by setting three bits

(P2, P1, P0and SRPV operation instruction are used. Details regarding burst length and dummy cycles can be found in Table ) and four bits (P6, P5, P4, P3) within the Read Register, respectively. To set those bits the SRPNV
6.9, Table 6.10, and Table 6.11. HOLD#/the SRPNV and SRPV operation as well, RESET# in order to select function (^) HOLD#/RESET#selection (P7) bit in the Read Register can be set with pin as RESET# or HOLD#.

For independent of the P7 bit setting in Read Register.the device with dedicated RESET# pin (or ball) , RESET# pin (or ball) will be a separate pin (or ball) and it is
SRPNV is used to set the non - volatile Read Register, while SRPV is used to set the volatile Read Register.
To write nonexecuted for the device to accept SRPNV(65h) instruction (Status Register bit WEL must equal -volatile Read Parameter bits, a standard Write Enable (06h) instruction must previ“ 1 ously have been ”).
(^) To write volatile Read Parameter bits (SRPV), 63h or C0h command can be used.

When using 63h instruction, device to accept SRPV (63h) instruction (a standard Write Enable (06h) Status Register bit WEL must equal instruction must previously have been executed for the “ 1 ”).
But C0h instruction“ 0 ”). does not require a standard Write Enable (06h) operation. (Status Register bit WEL remains
Note: When SRPNV is executed, the volatile Read Register is set as well as the non - volatile Read Register.
Figure 8.59 Set Read Parameters Sequence In SPI Mode
Instruction = 65 h or C 0 h/ 63 h
CE#
SCK
SI
SO
Data In
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
7 6 5 4 3 2 1 0
High Impedence
(^) Figure 8.60 Set Read Parameters Sequence In QPI Mode
C^650 hh or / 63 h
Mode 3 0 1
Mode 0

2 3
7 : 4 3 : 0
CE#
SCK
IO[ 3 : 0 ]
Data In^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 101
Read with “8/16/32/64 - Byte Wrap Around”
The device is capable of burst read with wrap around in both SPI and QPI mode. The size of burst length is configurable by using P0, P1, and P2 bits in Read Register. P2 bit (Wrap enable) enables the burst mode feature.
P0 and P1 define the size of burst. Burst lengths of 8, 16, 32, and 64 bytes are supported. By default, address increases by one up through the entire array. By setting the burst length, the data being accessed can be limited
to the length of burst bois specified in the instruction. Following data will come out from the next address within the burst boundary. Once undary within a 256 byte page. The first output will be the data at the initial address which
the address reaches the end of boundary, it wiwill terminate the command. ll automatically move to the first address of the boundary. CE# high
(^) For example, if burst length of 8 and initial address being applied is 0h, following byte output will be from address

00h and continue to 01h,..,07h, 00h, 01hbeing applied is FEh(254d), following byte output will be from address FEh and continue to FFh, F8h, F9h, FAh, ... until CE# terminates the operation. If burst length of 8 and initial address
FBh, FCh, FDh, and repeat from FEh until CE# terminates the operat ion.
The commands, “SRPV (65h) or SRPNV (C0h or 63h)”, are used to configure the burst length. If the following data input is one of “00h”,”01h”,”02h”, and ”03h”, the device will be in default operation mode. It will be continuous burst
read of the whole burst length as 8,16,32 and 64, respectively.array. If the following data input is one of “04h”,”05h”,”06h”, and ”07h”, the device will set the
(^) To exit the burst mode, another “C0h or 63h” command is necessary to set P2 to 0. Otherwise, the burst mode will

be retained until either power down or reset operation. To change burst length, another “C0h or 63h” command should be executed to set P0 and P1 (Detailed information in Table 6.9 Burst Length Data). All read commands
will operate in burst mode once the Read Register is set to enable burst mode.
Refer to Figure 8.59 and Figure 8.60 for instruction sequence.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 102
8.27 SET EXTENDED READ PARAMETERS OPERATION (SERPNV: 85h, SERPV: 83h)
Set Read Operational Driver Strength
This device supports configurable Operational Driver Strength (ODS0, ODS1, ODS2) within the Extended Read Register. To set the ODS bits the SERPNV and SERPV operation in both SPI and QPI modes by setting three bits
instructions are required. The device’s dDetails regarding the driver strength can be found in Table 6.14.river strength can be reduced as low as 12.50% of full drive strength.
(^) SERPNV is used to set the non-volatile Extended Read register, while SERPV is used to set the volatile Extended

Read register.
Notes:1. The default driver strength is set to 50%. (^)

When SERPNV is executed, the volatile Read Extended Register is set as well as the nonRegister. - volatile Read Extended
(^) Figure 8.61 Set Extended Read Parameters Sequence In SPI Mode
Instruction = 85 h/ 83 h

CE#
SCK
SI
SO
Data In
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
7 6 5 4 3 2 1 0
High Impedence
(^)

Figure 8.62 Set Extended Read Parameters Sequence In QPI Mode
85 h/ 83 h
Mode 3 0 1
Mode 0
2 3
7 : 4 3 : 0
CE#
SCK
IO[ 3 : 0 ]
Data In^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 103
8.28 READ READ PARAMETERS OPERATION (RDRP, 61h)
Prior to, or after setting Read Register, the data of the Read Register can be confirmed by the RDRP command. The instruction is only applicable for the volatile Read Register, not for the non-volatile Read Register.
(^) Figure 8.63 Read Read Parameters Sequence In SPI Mode
Instruction = 61 h
7

CE#
SCK
SI
SO 3 2 1 0
Data Out
6 5
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
4
tV
Figure 8.64 Read Read Parameters Sequence In QPI Mode
61 h
Mode 3 0 1
Mode 0
2 3
7 : 4 3 : 0
CE#
SCK
IO[ 3 : 0 ]
tV
Data Out^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 104
8.29 READ EXTENDED READ PARAMETERS OPERATION (RDERP, 81h)
Prior to, or after setting Extended Read Register, the data of the Extended Read Register can be confirmed by the RDERP command. The instruction is only applicable for the volatile Extended Read Register, not for the non-
volatile Extended Read Register.
During the execution of a executed, which can be used to check the progress or completion of an operation by reading the Program, Erase or Write Non-Volatile Register operation, the RDERP instruction will be WIP bit.
(^) Figure 8.65 Read Extended Read Parameters Sequence In SPI Mode
Instruction = 81 h
7

CE#
SCK
SI
SO 3 2 1 0
Data Out
6 5
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
4
tV
(^) Figure 8.66 Read Extended Read Parameters Sequence In QPI Mode
81 h
Mode 3 0 1
Mode 0

2 3
7 : 4 3 : 0
CE#
SCK
IO[ 3 : 0 ]
tV
Data Out^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 105
8.30 CLEAR EXTENDED READ REGISTER OPERATION (CLERP, 82h)
A Clear Extended Read Register (CLERP) instruction clears PROT_E, P_ERR, and E_ERR error bits Extended Read Register to “0” when the error bits are set to “1”. Once the error bits are set to “1”, they remains set in the
to “1” until they are cleared to “0” with a CLERP command.
Figure 8.67 Clear Extended Read Register Sequence In SPI Mode
Instruction = 82 h
CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High Impedance^
(^) Figure 8.68 Clear Extended Read Register Sequence In QPI Mode
82 h
CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 106
8.31 READ PRODUCT IDENTIFICATION (RDID, ABh)
The Release from and QPI modes. The Read Product Identification (RDID) instruction is for reading out the old style of 8Power-down/Read Device ID instruction is a multi-purpose instruction. It can support bot-bit Electronic h SPI
Signature, whose values are shown as the ta ble of Product Identification.
The RDID instruction code is followed by three dummy bytes, each bit being latchededge. Then the Device ID is shifted out on SO with the MSB first, each bit been shifted out during the-in on SI during the rising falling edge SCK
of SCK. The RDID instruction is ended by driving CE# high. The Device ID (IDclock cycles are continuously sent to SCK while CE# is at low. 7 - ID0) outputs repeatedly if additional
(^) Table 8.7 Product Identification

Manufacturer ID (MF7-MF0)
ISSI Serial Flash 9Dh
Instruction ABh 90h 9Fh
Part Number Device ID (ID7-ID0) Memory Type + Capacity(ID15-ID0)
IS25LP128F 17 h 6018 h
IS25WP128F 17 h 7018 h
(^)

Figure 8.69 Read Product Identification Sequence
Device ID(Data OutID 7 - ID 0 )
32 33 ... 39
Instruction = ABh
CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^31
Mode 0
3 Dummy Bytes
tV
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 107
Figure 8.70 Read Product Identification Sequence In QPI Mode
ABh
CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
2 3 4 5 6 7 8 9
6 Dummy Cycles Device ID(ID 7 - ID 0 )
tV
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 108
8.32 READ PRODUCT IDENTIFICATION BY JEDEC ID OPERATION (RDJDID, 9Fh; RDJDIDQ, AFh)
The JEDEC ID READ instruction allows the user to read the manufacturer and product ID of devices. Refer to Table 8. 7 Product Identification for Manufacturer ID and Device ID. After the JEDEC ID READ command (9Fh in SPI
mode, AFh in QPI mode)(ID15-ID0) that indicates Memory Type is input, the Manufacturer ID is shifted out MSB first followed by the 2and Capacity, one bit at a time. Each bit is shifted out during the falling -byte electronic ID
edge of SCK. If CE# stays low after the last bit of the 2ID will loop until CE# is pulled high. - byte electronic ID, the Manufacturer ID and 2-byte electronic
(^)

Figure 8.71 Read Product Identification by JEDEC ID Read Sequence In SPI Mode
Instruction = 9 Fh
Memory Type(ID 15 - ID 8 )
CE#
SCK
SI
SO (CapacityID 7 - ID 0 )
Mode 3 0 1 ...^789 ...^151617 ...^232425 ...^31
Mode 0
tV Manufacturer ID(MF 7 - MF 0 )
(^) Figure 8.72 RDJDID and RDJDIDQ (Read JEDEC ID) Sequence In QPI MOde
AFh

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
2 3
7 : 4 3 : 0
4 5
7 : 4 3 : 0
6 7
7 : 4 3 : 0
MF 7 - MF 0 ID 15 - ID 8 ID 7 - ID 0
tV
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 109
8.33 READ DEVICE MANUFACTURER AND DEVICE ID OPERATION (RDMDID, 90h)
The Read product ID of devices. Refer to Table Device Manufacturer and Device ID (RDMDID) 8. 7 Product Identification for Manufacturer ID and Device ID. The RDMDID instruction allows the user to read the Manufacturer and
instruction code is followed by two dummy bytduring the rising edge of SCK. If one byte address is initially set as A0 = 0, then the Manufacturer ID is shifted out es and one byte address (A7~A0), each bit being latched-in on SI
on SO with the MSB first followed by the device ID (ID7If one byte address is initially set as A0 = 1, then Device ID7- ID0). Each bit -ID0 will be read first followed by the Manufacturer ID. is shifted out during the falling edge of SCK.
The Manufacturer and Device ID can be read continuously alternating between the two until CE# is driven high.
Figure 8.73 Read Product Identification by RDMDID Sequence In SPI Mode
Instruction = 90 h
Manufacturer ID(MF 7 - MF 0 )
CE#
SCK
SI
SO Device ID(ID 7 - ID 0 )
Mode 3 0 1 ...^789 ...^313233 ...^394041 ...^47
Mode 0
3 - byte Address
tV
Notes:
ADDRESS A0 = 0, will output the 1ADDRESS A0 = 1, will output the 1--byte Manufacturer ID (MF7byte Device ID (ID7-ID0) →- MF0) 1 - byte Manufacturer ID (MF7→ 1 - byte Device ID (ID7-MF0)-ID0) (^)

The Manufacturer and Device ID can be read continuously and will alternate from one to the other until CE# pin is pulled high.

(^)

Figure 8.74 Read Product Identification by RDMDID Sequence In QPI Mode
90 h
CE#
SCK
IO[ 3 : 0 ]
3 - byte Address
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11
Mode 0
23 : 2019 : 1615 : 1211 : 8 7 : 4 3 : 0 7 : 4 3 : 0 7 : 4 3 : 0
tV
Instruction IDManufacturer (MF 7 - MF 0 )Device ID(ID 7 - ID 0 )
(^) Notes:

ADDRESS A0 = 0, will output the 1ADDRESS A0 = 1, will output the 1--byte Manufacturer ID (MF7byte Device ID (ID7-ID0) →- 1 MF0) -byte Manufacturer ID (MF7→ 1 - byte Device ID (ID7-MF0)-ID0) (^)
2. Thepulled high. Manufacturer and Device ID can be read continuously and will alternate from one to the other until CE# pin is
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 110
8.34 READ UNIQUE ID NUMBER (RDUID, 4Bh)
The Read Unique ID Number (RDUID) instruction accesses a factoryto the device. The ID number can be used in conjunction with user software methods to help prevent copying or -set read-only 16-byte number that is unique
cloning of a system. The RDUID instruction is instated by driving the CE# pin low and shifting the instruction code (4Bh) followed by 3 address bytes and dummy cycles (configurable, default is 8 clocks). After which, the 16-byte
ID is shifted out on the falling edge of SCK as shown below.
As a result, tsame as FAST READ sequence in QPI modehe sequence of RDUID instruction except for the instruction code. Refer to the FAST READ operation is same as FAST READ. RDUID sequence in QPI mode is also
in QPI mode.
Note: 16 bytes of data will repeat as long as CE# is low and SCK is toggling.
Figure 8.75 RDUID Sequence In SPI Mode
Instruction = 4 Bh Dummy Cycles
CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^313233 ...^394041 ...^47
Mode 0
3 Byte Address
Data Out
tV
...
Note: Dummy cycles depends on Read Parameter setting. Detailed information in Table 6.11 Read Dummy Cycles.
(^)

Table 8.8 Unique ID Addressing
A[23:16] A[15:9] A[8:4] A[3:0]
XXhXXh XXhXXh 00h00h 0h Byte address1h Byte address (^)
XXhXXh XXhXXh 00h00h 2h Byte address
XXh XXh 00h Fh Byte address...^

Note: XX means “don’t care”.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 111
8.35 READ SFDP OPERATION (RDSFDP, 5Ah)
The Serial Flash Discoverable Parameters (SFDP) standard provides a consistent method of describing the functions and features of serial Flash devices in a standard set of internal parameter tables. These parameters can
be interrogated by host system software to enable adjustments needed to accommodate divergent features from multiple vendors. For more details please refer to the JEDEC Standard JESD 216 (Serial Flash Discoverable
Parameters).
The sequence of issuing RDSFDP instruction in SPI mode is:
CE# goes low after dummy cycles (default 8 cycles) → Send RDSFDP instruction (5Ah) → End RDSF→DP operation by driving CE# hi Send 3 address bytes on SI pin gh at any time during data out.→ Read SFDP code on SO
Figure 8.76 RDSFDP (Read SFDP) Sequence
Instruction = 5 Ah Dummy Cycles
CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^313233 ...^394041 ...^47
Mode 0
3 Byte Address
Data Out
tV
8.36 NO OPERATION (NOP, 00h)
The No Operation command solely cancels a Reset Enable command and has no impact on any other commands. It is available in both SPI and QPI modes. To execute a NOP, the host drives CE# low, sends the NOP command
cycle (00H), then drives CE# high.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 112
8.37 SOFTWARE RESET (RESETRESET ................................................................-ENABLE (RSTEN................................, 66h) AND RESET (RST................................, 99h)) AND HARDWARE
The Reset operation, the value of volatile registers will default back to the value in the corresponding nonSoftware Reset operation is used as a system reset that puts the device in normal operating mode. During the -volatile
register. However, changed by Software Resetthe volatile F. This operation consists of two commands: ResetREEZE bit and the volatile PPB Lock bit in the PPB Lock Register are not -Enable (RSTEN) and Reset (RST).
The operation requires the ResetReset command after the Reset-Enable command will disable the Reset-Enable command followed by the Reset command-Enable.. Any command other than the
(^)

Execute the CE# pin lowCE# low again, sends the Reset command (99 → sends the Reset-Enable command (66h), and pulls CE# high.h), and drives CE# high. Next, the host drives
(^) Only if the RESET# pin is enabled, Hardware Reset function is available.

For the device with HOLD#/RESET#,“0”. For the device with dedicated RESET# the RESET# pin will be solely applicable in SPI mode and when the QE bit = (Dedicated RESET# Disable bit is “0” in Function Register), the RESET#
pin is always applicable regardless of the QE bit value in Status Register and HOLD#/RESET# selection bit (P7) in Read Register in SPI/QPI mode.
(^) In order to activate Hardware Reset, the RESET# pin (or ball) must be driven low for a minimum period of tRESET
(1operations00ns). Drive RESET# low for a minimum period of t, release the device from deep power down modeRESET (^1) , disable all input will interrupt any on signals, force the output pin enter a -going internal and external
state of high impedance, and reset all the read parameters.The required wait time after activating a HW Reset before the device w (^) ill accept another instruction is tHWRST of

35us.
The Software/Hardware Reset during in corrupting or losing the data of the targeted address range. Depending on the prior operation, the reset timing an active Program or Erase operation aborts the operation, which can result
may vary. Recovery from a Write operation will require more latency than recovery from other operations.
Note1: The Status and Function Registers remain unaffected.
Figure 8.77 Software Reset Enable and Software Reset Sequence (RSTEN, 66h + RST, 99h)
Instruction = 66 h
CE#
SCK
SI
Mode 3 0 1
Mode 0
2 3 4 5 6 7
Instruction = 99 h
8 9 10 11 12 13 14 15
SO High Impedance
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 113
Figure 8.78 Software Reset Enable and Software Reset QPI Sequence (RSTEN, 66h + RST, 99h)
66 h
CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
99 h
0 1
8.38 SECURITY INFORMATION ROW
The security Information Row is comprised of an additional 4 x 256 bytes of programmable information. bits can be reprogrammed by the user. Any program security instruction issued while an erase, program or write The security
cycle is in progress is rejected without having any effect on the cycle that is in progress.
Table 8.9 Information Row Valid Address Range
IRL0 Address Assignment (Information Row Lock0)^ A[23:16]00h A[15:8]00h Byte addressA[7:0]^
IRL1 IRL2 00h00h 10h20h Byte addressByte address (^)

IRL3^ 00h^ 30h^ Byte address^
Bit 7~4 of the Function Register is used to permanently lock the programmable memory array.
When Function Register bit IRLx = “0”, When Function Register bit IRLx = “1”, the 256 bytes of the programmable memory array function as read only.the 256 bytes of the programmable memory array can be programmed. (^)
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 114
8.39 INFORMATION ROW ERASE OPERATION (IRER, 64h)
Information Row Erase (IRER) operation, the Write Enable Latch (WEL) must be set via a Write Enable (WREN) instruction. The WEL bit is instruction erases the data in the Information Row x (x: 0~3) array. Prior to the
automatically reset after the completion of the operation.
The sequence of address bytes → Pull CE# high. CE# should remain low during the entire instruction sequence. Once CE# is pulled IRER operation: Pull CE# low to select the device → Send IRER instruction code → Send three
high, Erase operation will begin immtiming. ediately. The internal control logic automatically handles the erase voltage and
(^) Figure 8.79 IRER (Information Row Erase) Sequence
Instruction = 64 h 23

CE#
SCK
SI 3 2
SO
1 0
3 - byte Address
High Impedance
22 21 ...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...^28293031
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 115
8.40 INFORMATION ROW PROGRAM OPERATION (IRP, 62h)
The a single operation. Before the execution of IRP instruction, the Write Enable Latch (WEL) must be enabled through Information Row Program (IRP) instruction allows up to 256 bytes data to be programmed into the memory in
a Write Enable (WREN) instruction.
The Three address bytes has to be inpuIRP instruction code, three address byt as specified in the Table 8.9tes and program data (1 to 256 bytes) should be sequentially input. Information Row Valid Address Range. Program
operation will start once the CE# logic automatically handles the programming voltages and timing. During a program operation, all instructions will goes high, otherwise the IRP instruction will not be executed. The internal control
be ignored except the RDSR instruction. The progress or completion of the program opeby reading the WIP bit. If the WIP bit is “1”, the program operation is still in progress. If WIP bit is “0”, the program ration can be determined
operation has completed.
If more than 256 bytes data are sent to a device, the address counter rolls over wipreviously latched data are discarded and the last 256 bytes data are kept to be programmed into the page. The thin the same page. The
starting byte can be anywhere within the page. When the end of the page is reached, the address will wrap around to the beginning of the same page. If the data to be programmed are less than a full page, the data of all other
bytes on the same page will remain unchanged.
Note: A program operation can alter “1”s into “0”s, but an erase operation is required to change “0”s bac byte cannot be reprogrammed without first erasing the corresponding Information Row array which is one of k to “1”s. A

IR0~3.^
Figure 8.80 IRP (Information Row Program) Sequence
Instruction = 62 h 23
CE#
SCK
SI 7 6
SO
7
3 - byte Address
High Impedance
22 ... 0
Data In 1 Data In 256
Mode 3 0 1 ...^789 ...^313233 ...^39 ... 2072 ... 2079
Mode 0
... 0 ... ... 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 116
8.41 INFORMATION ROW READ OPERATION (IRRD, 68h)
The IRRD instruction is used to read memory data at up to a 166MHz clock.
The is 8 clocks)IRRD instruction code is followed by three address bytes (A23 , transmitted via the SI line, with each bit latched-in during th- A0) and dummy cycles e rising edge of SCK. Then the first data (configurable, default
byte addressed is shifted out on the SO line, with each bit shifted out at a maximum frequency fedge of SCK. CT, during the falling
(^) The address is automatically incremented by one after each byte of data is shifted out. Once the address reaches

the last address of each 256 byte Information Row, the next address will not be valid and the data of the address will be garbage data. It is recommended to repeat four times IRRD operation that reads 256 byte with a valid starting
address of each Information Row in order to read all data in the 4 x 256 byte Information Row array. The instruction is terminated by driving CE# high (VIH). IRRD
(^) If an IRRD instruction is issued while an Erase, Program or Write cycle is in process (WIP=1) the instruction is

ignored and will not have any effects on the current cycle
Tsame as Fast Read QPI except for the instruction code. Refehe sequence of IRRD instruction is same as Fast Read except for the instruction code. IRRD QPI sequence is r to the Fast Read QPI operation.
(^) Figure 8.81 IRRD (Information Row Read) Sequence
Instruction = 68 h Dummy Cycles

CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^313233 ...^394041 ...^47
Mode 0
3 Byte Address
Data Out
tV
...
Note: Dummy cycles depends on Read Parameter setting. Detailed information in Table 6.11 Read Dummy Cycles.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 117
8.42 FAST READ DTR MODE OPERATION (FRDTR, 0Dh or 4FRDTR, 0Eh)
The FRDTR/4edge of clock. The address is latched on both rising and falling edge of SCK, and data of each bit shifts out on both FRDTR instruction is for doubling the data in and out. Signals are triggered on both rising and falling
rising and falling edgeone clock, which means one bit at the rising edge of clock, the other bit at the falling edge of clock. of SCK. The 2-bit address can be latched-in at one clock, and 2-bit data can be read out at
(^) The first address byte can be at any location. The address is automatically increased to the next higher address

after each byte of data is shifted out, so the whole memory can be read out in a single FRDTR/4The address counter rolls over to 0 when the highest address is reached. FRDTR instruction.
(^) • 0Dh (EXTADD=0) is followed by a 3-byte address (A23-A0) or

• • 0Dh (EXTADD=1) is followed by a 40Eh is followed by a 4-byte address (A31-byte address (A31-A0) - A0) or
(^) The sequence of issuing FRDTR/4FRDTR instruction is: CE# goes low → Sending FRDTR/4FRDTR instruction

code (1bit per clock) default is 8 clocks) on SI → 3 - byte or 4→ Data out on SO (2-byte address on SI (2-bit per clock) -bit per clock) as above → End FRDTR/4FRDTR→ 8 dummy clocks (configurable, operation via driving CE#
high at any time durin g data out.
While a Program/Erase/Write Status Register cycle is in progress, FRDTR/4without any effect on the current cycle. FRDTR instruction will be rejected
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 118
Figure 8.82 FRDTR Sequence (0Dh [EXTADD=0], 3-byte address)
CE#
SCK
SI
SO
Data Out 1
Instruction = 0 Dh
CE#
SCK
SI
SO
3 - byte Address
High Impedance
0 1 2 3 4 5 6 7 8 9 10 ... 19 20 21
22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ...
Mode 3
Mode 0
tV
232221 0
7 6 5 4 3 2 1 0
Data Out 2
7 6 5 4 3 2 1 0
Data Out ...
7 6
8 Dummy Cycles
20191817
5 ...
...
Note: Dummy cycles depends on Read Parameter setting. Detailed information in Table 6.11 Read Dummy Cycles.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 119
Figure 8.83 FRDTR Sequence (0Dh [EXTADD=1] or 0Eh, 4-byte address)
Instruction = 0 Dh/ 0 Eh
4 - byte Address
27 28 29
30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ...
31302928272625
CE#
SCK
SI
SO
Data Out 1
CE#
SCK
SI
SO High Impedance
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...
Mode 0
tV
0
7 6 5 4 3 2 1 0
Data Out 2
7 6 5 4 3 2 1 0
Data Out ...
7 6
8 Dummy Cycles
5 ...
...
Note: Dummy cycles depends on Read Parameter setting. Detailed information in Table 6.11 Read Dummy Cycles.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 120
FAST READ DTR MODE OPERATION IN QPI MODE (FRDTR, 0Dh or 4FRDTR, 0Eh)
The FRDTR/4FRDTR clocks are required, while the FRDTR/4FRDTR instructioninstruction in QPI mode utilizes all four IO lines to input the instruction code so that only two in SPI mode requires that the byte-long instruction code
is shifted into the device only via IO0 (SI) line in eight clocks. Ishifted in/out via all four IO lines unlike the FRDTR/4FRDTR instruction. Eventually this operation in addition, subsequent address and data out are s same as the
FRQDTR/4FRQDTR in QPI modeFRDTR/4FRDTR operation in QPI mode., but the only different thing is that AX mode is not available in the
(^)
• • 0Dh (EXTADD=0) is followed by a 30Dh (EXTADD=1) is followed by a 4--byte address (A23byte address (A31--A0) orA0) or (^)

• 0Eh is followed by a 4-byte address (A31-A0)
The sequence of issuing FRDTR/4FRDTR QPI instructiinstruction (4-bit per clock) → 24 - bit or 32-bit address interleave on IO3, IO2, IO1 & IO0 (8on is: CE# goes low → Sending FRDTR/4FRDTR QPI -bit per clock) as above
→→ 6 dummy clocks (configurable, default is 6 clocks) End FRDTR/4FRDTR QPI operation by driving CE# high at any time during data out.→ Data out interleave on IO3, IO2, IO1 & IO0 (8-bit per clock)
(^) If the FRDTR/4FRDTR instruction in QPI mode is issued while an Erase, Program or Write cycle is in process is in

progress (WIP=1), the instruction will be rejected without any effect on the current cycle.
(^) Figure 8.84 FRDTR Sequence In QPI Mode ( (0Dh [EXTADD=0], 3-byte address)
Instruction= 0 Dh

CE#
SCK
3 - byte Address
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12
Mode (^0) tV
201612
211713 5 1
IO (^040)
IO 1
221814
231915

8 4 0
9 5 1
10 6 2
11 7 3
6 Dummy Cycles
IO 2
IO 3
6 2
7 3
5 1
4 0
6 2
7 3
DataOut DataOut
...
4 0
5 1
6 2
7 3
...
...
...
...
Notes:1. Number of dummy cycles depends on clock speed. Detailed information in Table 6.11 Read Dummy Cyc (^) les.

2. Sufficient dummy cycles are required to avoid I/O contention.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 121
Figure 8.85 FRDTR Sequence In QPI Mode (0Dh [EXTADD=1] or 0Eh, 4-byte address)
= Instruction 0 Dh/ 0 Eh
CE#
SCK
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12
Mode 0
IO 0
IO 1
6 Dummy Cycles
IO 2
IO 3
...
4 0
5 1
6 2
7 3
4 - byte Address tV
282420
2521 5 1
4 0
302622
312723
1612 8
1713 9
181410
191511
6 2
7 3
DataOut
...
...
...
...
4 0
5 1
6 2
7 3
29
Notes:1. Number of dummy cycles depends on clock speed. Detailed information in Table 6.11 (^) Read Dummy Cycles.

Sufficient dummy cycles are required to avoid I/O contention.are same, then X should be Hi-Z. If the number of dummy cycles and AX bits cycles
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 122
8.43 FAST READ DUAL IO DTR MODE OPERATION (FRDDTR, BDh or 4FRDDTR, BEh)
The FRDDTR/mode. The address (interleave on dual I/O pins) is latched on both rising and falling edge of SCK, and the data 4 FRDDTR instruction enables Double Transfer Rate throughput on dual I/O of the device in read
(interleave on dual I/O pins) shift out on both rising aone clock, and 4-bit data can be read out at one clock, which means two bits at the rising edge of clock, the other nd falling edge of SCK. The 4-bit address can be latched-in at
two bits at the falling edge of clock.
The first address byte can be at any after each byte of data is shifted out, so the whole memory can be read out with a single FRDDTR/location. The address is automatically increased to the next higher address 4 FRDDTR
instruction. The address counter rolls over to 0 when the highest adFRDDTR/ 4 FRDDTR instruction, the following address/dummy/data out will perform as 4dress is reached. Once writing -bit instead of previous 1-
bit.
• • BDh (EXTADD=0) is followed by a 3BDh (EXTADD=1) is followed by a 4--byte address (A23byte address (A31--A0) orA0) or (^)

• BEh is followed by a 4-byte address (A31-A0)
The sequence of issuing FRDDTR/instruction (1-bit per clock) → 24 - bit or 32 4 FRDDTR-bit address interleave on IO1 & IO0 (4 instruction is: CE# goes low -bit per clock) as above → Sending FRDDTR/→ 4 FRDDTR4 dummy
clocks (configurable, default is 4 clocks) on IO1 & IO0 FRDDTR/ 4 FRDDTR operation via pulling CE# high at any time during data out (Please refer to Figures → Data out interleave on IO1 & IO0 (4-bit per clock) 8. 8 → 6 End and
8.8 7 for 2 x I/O Double Transfer Rate Read Mode Timing Waveform).
If AXh (where X is don’t care) is input for the mode bits during dummy cycles, the device will enter AX read operation mode which enables subsequent FRDDTR/ 4 FRDDTR execution skips command code. It saves cycles as
described in Figures the AX read operation. After finishing the read operation, device becomes ready to receive a new command.8. 88 and 8.8 9. When the code is different from AXh (where X is don’t care), the device exits
(^) If the FRDDTR/ 4 FRDDTR instruction is issued while an Erase, Program or Write cycle is in process is in progress

(WIP=1), the instruction will be rejected without any effect on the current cycle.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 123
Figure 8.86 FRDDTR Sequence (BDh [EXTADD=0], 3-byte address)
CE#
SCK
IO 0
IO 1
Instruction = BDh
CE#
SCK
IO 0
IO 1
3 - byte Address
High Impedance
0 1 2 3 4 5 6 7 8 9 10 ... 13 14
15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
Mode 3
Mode 0
...
tV
222018 0
7 5 3 1 7 5 3 1 7 5 3 1 7 5 3 1 7 5 3 1 7 5 3 1
4 Dummy Cycles
232119 1
Data Out
6 4 2 0 6 4 2 0 6 4 2 0 6 4 2 0 6 4 2 0 6 4 2 0 ...
Data Out Data Out Data Out Data Out Data Out
161412
171513
10
11 7 5
6 4
3 1
2 0
Mode Bits
...
Mode Bits
...
...
Notes:1. If the mode bits=AXh (where X is don’t care), it can execute the AX read mode (without command) (^). When the mode

Number of dummy cycles depends on clock speed. Detailed information in Table 6.bits are different from AXh, the device exits the AX read operation.^ 11 Read Dummy Cycles.
Sufficient dummy cycles are required to avoid I/O contention. If the number of dummy cycles and AX bits cycles are same, then X should be Hi-Z.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 124
Figure 8.87 FRDDTR Sequence (BDh [EXTADD=1] or BEh, 4-byte address)
CE#
SCK
IO 0
IO 1
Instruction = BDh/BEh
CE#
SCK
IO 0
IO 1
4 - byte Address
High Impedance
0 1 2 3 4 5 6 7 8 9 10 ... 17 18
19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
Mode 3
Mode 0
tV
302826 0
7 5 3 1 7 5 3 1 7 5 3 1 7 5 3 1 7 5 3 1 7 5 3 1
4 Dummy Cycles
312927 1
Data Out
6 4 2 0 6 4 2 0 6 4 2 0 6 4 2 0 6 4 2 0 6 4 2 0 ...
Data Out Data Out Data Out Data Out Data Out
242220
252321
18
19 7 5
6 4
3 1
2 0
Mode Bits
...
Mode Bits
...
...
...
Notes:1. If the mode bits=AXh (where X is don’t care), it can execute the AX read mode (without command) (^). When the mode

bits are different from AXh, the device exits the AX read operation.Number of dummy cycles depends on clock speed. Detailed information^ in Table 6.11 Read Dummy Cycles.
Sufficient dummy cycles are required to avoid I/O contention. If the number of dummy cycles and AX bits cycles are same, then X should be Hi-Z.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 125
Figure 8.88 FRDDTR AX Read Sequence (BDh [EXTADD=0], 3-byte address)
IO 0
IO 1
3 - byte Address
...
...
tV
222018
7 5 3 1 7 5 3 1 7 5 3 1
4 Dummy Cycles
232119
6 4 2 0 6 4 2 0 6 4 2 0 ...
Data Out Data Out Data Out
161412
171513
10
11
SCK
Mode 3 0 1 2 ...^678910111213141516
Mode 0
CE#
7 5 3 1
0 6 4 2 0
1
Mode Bits
...
...
Notes:
If the mode bits=AXh (where X is don’t care), it will keep executing the AX read mode (without command) mode bits are different from AXh, the device exits the AX read operation.. When the
2.3. Number of dummy cycles depends onSufficient dummy cycles are required to avoid I/O contention. If the number of dummy cycles and AX bits cycles clock speed. Detailed information in Table 6.11 Read Dummy Cycles.
are same, then X should be Hi-Z.^
(^) Figure 8.89 FRDDTR AX Read Sequence (BDh [EXTADD=1] or BEh, 4-byte address)
4 - byte Address
...
302826
312927
242220
252321
18
19
8 9 10 11 12 13 14 15 16 17 18
IO 0
IO 1 ...
tV
7 5 3 1 7 5 3 1 7 5 3 1
4 Dummy Cycles
6 4 2 0 6 4 2 0 6 4 2 0 ...
Data Out Data Out Data Out
SCK
Mode 3 0 1 2 ...
Mode 0
CE#
7 5 3 1
0 6 4 2 0
1
Mode Bits
...
...

Notes:
If the mode bits=AXh (where X is don’t care), it will keep executing the AX read mode (without command) mode bits are different from AXh, the device exits the AX read operation.. When the
2.3. Number ofSufficient dummy cycles are required to avoid I/O contention. If the number of dummy cycles and AX bits cycles dummy cycles depends on clock speed. Detailed information in Table 6.11 Read Dummy Cycles.
are same, then X should be Hi-Z.^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 126
8.45 SECTOR LOCK/UNLOCK FUNCTIONS 8.44 FAST READ QUAD IO DTR MODE OPERATION IN SPI MODE (FRQDTR, ED ................................................................................................................................................................h or 4FRQDTR, EE.... 126 h)
The FRQDTR/mode. The address (interleave on 4 I/O pins) is latched on both rising and falling edge 4 FRQDTR instruction enables Double Transfer Rate throughput on quad of SCK, and data (interleave I/O of the device in read
on 4 I/O pins) shift out on both rising and falling edgeand 8-bit data can be read out at one clock, which means four bits at the rising edge of clock, of SCK. The 8-bit address can be latchedthe other four b-in at one clock, its at
the fall ing edge of clock.
The first address byte can be at any location. The address is automatically increased to the next higher address after each byte data is shifted out, so the whole memory can be read out with a single FRQDTR/ 4 FRQDTR instruc-
tion. The address counter rolls over to 0 when the highest address is reached. Once writing FRQDTR/instruction, the following address/dummy/data out will perform as 8-bit instead of previous 1-bit. 4 FRQDTR
(^) • EDh (EXTADD=0) is followed by a 3-byte address (A23-A0) or

• • EDh (EXTADD=1) is followed by a 4EEh is followed by a 4-byte address (A31-byte address (A31-A0) - A0) or
(^) The sequence of issuing FRQDTR/ 4 FRQDTR instruction is: CE# goes low → Sending FRQDTR/ 4 FRQDTR

instruction (1→ 6 dummy clocks (configurable, default is 6 clocks) -bit per clock) → 24 - bit or 32-bit address interleave on IO3, IO2, IO1 & IO0 (8→ Data out interleave on IO3, IO2, IO1 & IO0 (8-bit per clock) as above -bit per clock)
→ End FRQDTR/ 4 FRQDTR operation by driving CE# high at any time during data out.
If AXh (where X is don’t care) is input for the mode bits during dummy cycles, the device will enter AX read operation mode which enables subsequent FRQDTR/ 4 FRQDTR execution skips command code. It saves cycles as
described in Figures the AX read operation. After finishing the read operation, device becomes ready to receive a new command.8.9 2 and 8.9 3. When the code is different from AXh (where X is don’t care), the device exits
(^) If the FRQDTR/ 4 FRQDTR instruction is issued while an Erase, Program or Write cycle is in process is in progress

(WIP=1), the instruction will be rejected without any effect on the current cycle.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 127
Figure 8.90 FRQDTR Sequence In SPI Mode (EDh [EXTADD=0], 3-byte address)
CE#
SCK
Instruction = EDh
CE#
SCK
3 - byte Address
High Impedance
0 1 2 3 4 5 6 7 8 9 10 11 12
14 15 16 17 18 19 20 21 22 23 24 25 26 ...
Mode 3
Mode 0
tV
201612
5 1
211713
DataOut
4 0
IO 0
IO 1
IO 0
221814
231915
8 4 0
9 5 1
106 2
117 3
6 Dummy Cycles
IO 2
IO 3
IO 1
IO 2
IO 3
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
DataOut DataOut DataOut DataOut DataOut DataOut DataOut DataOut DataOut
13
5 1
4 0
6 2
7 3
Mode Bits
...
...
...
...
(^) Notes:

If the bits are different from AXh, the device exits the AX read operation. mode bits=AXh (where X is don’t care), it can execute the AX read mode (without command). When the mode
2.3. Number of dummy cycles depends on clock speed. Detailed information in Table 6.11 RSufficient dummy cycles are required to avoid I/O contention. If the number of dummy cycles and AX bits cycles ead Dummy Cycles.
are same, then X should be Hi-Z.^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 128
Figure 8.91 FRQDTR Sequence In SPI Mode (EDh [EXTADD=1] or EEh, 4-byte address)
CE#
SCK
Instruction = EDh/EEh
CE#
SCK
4 - byte Address
High Impedance
0 1 2 3 4 5 6 7 8 9 10 11 12
15 16 17 18 19 20 21 22 23 24 25 26 27 ...
Mode 3
Mode 0
tV
282420
5 1
292521
DataOut
4 0 ...
IO 0
IO 1
IO 0
302622
312723
1612 8
1713 9
181410
191511
6 Dummy Cycles
IO 2
IO 3
IO 1
IO 2
IO 3
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
DataOut DataOut DataOut DataOut DataOut DataOut DataOut DataOut DataOut
14
5 1
4 0
6 2
7 3
Mode Bits
13
5 1
4 0
6 2
7 3
...
...
...
(^) Notes:

If the mode bits=AXh (where X is don’t care), it can execute the AX read mode (without command) bits are different from AXh, the device exits the AX read operation.. When the mode
2.3. Number of dummy cycles depends on clock speed. Detailed Sufficient dummy cycles are required to avoid I/O contention.information in Table 6.11 Read Dummy Cycles. If the number of dummy cycles and AX bits cycles
are same, then X should be Hi-Z.^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 129
Figure 8.92 FRQDTR AX Read Sequence (EDh [EXTADD=0], 3-byte address)
CE#
SCK
3 - byte Address
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11
Mode (^0) tV
201612
211713 5 1
IO (^040)
IO 1
221814
231915

8 4 0
9 5 1
106 2
117 3
6 Dummy Cycles
IO 2
IO 3
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
DataOut DataOut DataOut DataOut
5 1
4 0
6 2
7 3
Mode Bits
12 ...
...
...
...
...
Notes:1. If the mode bits=AXh (where X is don’t care), it will keep executing the AX read mode (without command) (^). When the

Number of dummy cycles depends omode bits are different from AXh, the device exits the AX read operation.n clock speed. Detailed information in Table 6.11 Read Dummy Cycles.^
Sufficient dummy cycles are required to avoid I/O contention.are same, then X should be Hi-Z. If the number of dummy cycles and AX bits cycles
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 130
Figure 8.93 FRQDTR AX Read Sequence (EDh [EXTADD=1] or EEh, 4-byte address)
CE#
SCK
4 - byte Address
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11
Mode (^0) tV
282420
292521 5 1
IO (^040)
IO 1
302622
312723

1612 0
1713 1
1814 2
1915 3
6 Dummy Cycles
IO 2
IO 3
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
5 1
4 0
6 2
7 3
DataOut DataOut DataOut DataOut
5 1
4 0
6 2
7 3
Mode Bits
12 13 ...
8 4
9 5
106
117
...
...
...
...
Notes:1. If the mode bits=AXh (where X is don’t care), it will keep executing the AX read mode (without command) (^). When the

mode bits are different from AXh, the device exits the AX read operation.Number of dummy cycles depends on clock speed. Detailed information in Table 6.11 Read Dummy Cycles.^
Sufficient dummy cycles are required to avoid I/O contention.are same, then X should be Hi-Z. If the number of dummy cycles and AX bits cycles
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 131
FAST READ QUAD IO DTR OPERATION IN QPI MODE (FRQDTR, EDh OR 4FRQDTR, EEh)
The two clocks are required, while the FRQDTR/ 4 FRQDTR instruction in QPI modeFRQDTR/ 4 FRQDTR utilizes all four IO lines to input the instruction code so that only instruction in SPI mode requires that the byte-long
instruction code is shifted into the device only via IO0 line in eight clocks. As a result, 6 command cycles will be reduced by the FRQDTR/ 4 FRQDTR instruction in QPI mode. In addition, subsequent address and data out are
shthe FRQDTR/ifted in/out via all four IO lines like the 4 FRQDTR operation in QPI modeFRQDTR/ is exactly same as the FRQDTR/ 4 FRQDTR instruction. In fact, except for the command cycle, 4 FRQDTR operation in SPI mode.
(^)
• • EDh (EXTADD=0) is followed by a 3EDh (EXTADD=1) is followed by a 4--byte byte address (A31address (A23--A0) orA0) or (^)

• EEh is followed by a 4-byte address (A31-A0)
The sequence of issuing FRQDTR/instruction (4-bit per clock) → 24 - bit or 32 4 FRQDTR-bit address interleave on IO3, IO2, IO1 & IO0 (8 instruction is: CE# goes low → Sending FRQDTR/-bit per clock) as above 4 FRQDTR
→→ 6 dummy clocks (configurable, default is 6 clocks) End FRQDTR/ 4 FRQDTR operation by driving CE# high at any → Data out interleave on IO3, IO2, IO1 & IO0 (8time during data out. - bit per clock)
(^) If AXh (where X is don’t care) is input for the mode bits during dummy cycles, the device will enter AX read operation

mode which enables subsequent FRQDTRas described in Figures 8.92 and 8.93. When the code is different from AXh (where X is don’t care), the device / 4 FRQDTR in QPI mode execution skips command code. It saves cycles
exits the AX read operation. After finishing the read operation, device becomes ready to receive a new command.
If the FRQDTRis in progress (WIP=1), the instruction will be rejected without any effect on the current cycle./ 4 FRQDTR instruction in QPI mode is issued while an Erase, Program or Write cycle is in process
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 132
Figure 8.94 FRQDTR Sequence In QPI Mode (EDh [EXTADD=0], 3-byte address)
Instruction= EDh
CE#
SCK
3 - byte Address
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12
Mode (^0) tV
201612
211713 5 1
IO (^040)
IO 1
221814
231915

8 4 0
9 5 1
10 6 2
11 7 3
6 Dummy Cycles
IO 2
IO 3
6 2
7 3
5 1
4 0
6 2
7 3
DataOut DataOut
5 1
4 0
6 2
7 3
Mode Bits
...
4 0
5 1
6 2
7 3
...
...
...
...
Notes:1. If the mode bits=AXh (where X is don’t care), it can execute the AX read mode (without command) (^). When the mode

bits are different from AXh, the device exits the AX read operation.Number of dummy cycles depends on clock speed. Detailed information in Table 6.11 Read Dummy Cycles.^
Sufficient dummy cycles are required to avoid I/O contention.are same, then X should be Hi-Z. If the number of dummy cycles and AX bits cycles
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 133
Figure 8.95 FRQDTR Sequence In QPI Mode (EDh [EXTADD=1] or EEh, 4-byte address)
= InstructionEDh/EEh
CE#
SCK
4 - byte Address
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12
Mode (^0) tV
282420
292521 5 1
IO (^040)
IO 1
302622
312723

1612 8
1713 9
181410
191511
6 Dummy Cycles
IO 2
IO 3
6 2
7 3
DataOut
5 1
4 0
6 2
7 3
Mode Bits
...
4 0
5 1
6 2
7 3
...
...
...
...
4 0
5 1
6 2
7 3
Notes:1. If the mode bits=AXh (where X is don’t care), it can execute the AX read mode (without command) (^). When the mode

bits are different from AXh, the device exits the AX read operation.Number of dummy cycles depends on clock speed. Detailed information in Table 6.11 Read Dummy Cycles.^
Sufficient dummy cycles are required to avoid I/O contention.are same, then X should be Hi-Z. If the number of dummy cycles and AX bits cycles
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 134
8.45 SECTOR LOCK/UNLOCK FUNCTIONS
SECTOR UNLOCK OPERATION (SECUNLOCK, 26h or 4SECUNLOCK, 2 5 h)
The Sector Unlock command allows the user to select a specific sector to allow program and erase operations. This instruction is effective when the blocks are designated as write-protected through the BP0-BP3 bits in the
Status Register and TBS bit in the Function Register. Only one sector can be enabled at any time. To enable a different sector, a previously enabled sector must be disabled by executing a Sector Lock command.
(^) • 26h (EXTADD=0) is followed by a 3 - byte address (A23-A0) or

• • 26h (EXTADD=1) is followed by a 4 25 h is followed by a 4-byte address (A31-byte address (A31-A0) - A0) or
(^) The instruction code is followed by a 24-bit or 32-bit address specifying the target sector as above, but A0 through

A11 are not decoded. The remaining sectors within the same block remain as read-only.
Figure 8.96 Sector Unlock Sequence In SPI Mode (26h [EXTADD=0], 3-byte address)
Instruction = 26 h 23
CE#
SCK
SI 3 2
SO
1 0
3 - byte Address
High Impedance
22 21 ...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...^28293031
Mode 0
Figure 8.97 Sector Unlock Sequence In SPI Mode (26h [EXTADD=1] or 2 5 h, 4-byte address)
Instruction = 26 h/ 25 h 31
CE#
SCK
SI 3 2
SO
1 0
4 - byte Address
High Impedance
30 29 ...
Mode 3 0 1 2 3 4 5 6 7 8 9 10 ...^36373839
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 135
Figure 8.98 Sector Unlock Sequence In QPI Mode (26h [EXTADD=0], 3-byte address)
26 h
CE#
SCK
IO[ 3 : 0 ]
3 - byte Address
Mode 3 0 1 2 3 4 5 6 7
Mode 0
23 : 2019 : 1615 : 1211 : 8 7 : 4 3 : 0
Instruction
(^) Figure 8.99 Sector Unlock Sequence In QPI Mode (26h [EXTADD=1] or 2 5 h, 4-byte address)
26 h/ 25 h

CE#
SCK
IO[ 3 : 0 ]
4 - byte Address
Mode 3 0 1 2 3 4 5 6 7
Mode 0
31 : 2827 : 2423 : 2019 : 1615 : 1211 : 8 7 : 4 3 : 0
8 9
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 136
SECTOR LOCK OPERATION (SECLOCK, 24h)
Tinhestr (^) uSceticontor c (^) ode doesLock co mmnotand req (^) urelocks a sector that was previously unlocked by ire an address to be specified, as only one sethector Sceacntor be Uennlaobclked c oatm am taimnd.e. TThehe (^)

r emaining sectors within the same block remain in read-only mode.
Figure 8.100 Sector Lock Sequence In SPI Mode
Instruction = 24 h
CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High Impedance^
(^) Figure 8.101 Sector Lock Sequence In QPI Mode
24 h

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 137
8.46 AUTOBOOT
SPI devices normally require 32 or more cycles of command and in order to read boot code from an SPI device, the host memory controller or processor must supply the read address shifting to initiate a read command. And,
command from a hardwired state machine or from some host processor internal ROM code.Parallel NOR devices need only an initial address, supplied in parallel in a single cycle, and initial access time to
start reading boot code.The AutoBoot feature allows the host memory controller to take boot code from the device immediately after the
end of reset, to initiate the reading of boot code.without having to send a read command. This saves 32 or more cycles and simplifies the logic needed
(^) • As part of the Power-up Reset, Hardware Reset, or Software Reset process the AutoBoot feature automatically

starts a ready to deliver code from the starting address. The host memory controller only needs to drive CE# signal from read access from a pre-specified address. At the time the reset process is completed, the device is
high to low and begin toggling the SCK signaclock cycles before code streams out. l. The device will delay code output for a pre-specified number of
(^) – The Auto Boot Start Delay (ABSD) field of the AutoBoot register specifies the initial delay if any is needed by

– The host cannot send comthe host.^ mands during this time.
– If QE bit (Bit 6) in the Status Register is set to “1”, delay is the same as dummy cycles of Fast Read Quad I/O Read operationFast Read Quad I/O operation will be selected. If it is set to “0”, F and initial ast Read
operation will be applied^ and initial delay is the same as dummy cycles of Fast Read operation.^
• The starting address of the boot code is selected by the value programmed into the AutoBoot Start Address (ABSA) field of the AutoBoot Register.
(^) – Data will continuously shift out until CE# returns high.
(^) • At any point after the first data byte is transferred, when CE# returns high, the SPI device will reset to standard

SPI mode; able to accept normal command operations.^
– – A minimum of one byte must be transferred.AutoBoot mode will not initiate again until another power cycle or a reset occurs. (^)
(^) • An AutoBoot Enable bit (ABE) is set to enable the AutoBoot feature.
(^) The AutoBoot register bits are non-volatile and provide:
• • The starting address set by the AutoBoot Start The number of initial delay cycles, set by the AutoBoot Start Delay (ABSD) 4Address (ABSA). (^) - bit count value.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 138
Figure 8.102 AutoBoot Sequence (QE = 0)
7
CE#
SCK
SI
SO 3 2 1 0
High Impedance Data Out 1
6 5 4
Mode 3 0 1 2 ... n-^1 n n+^1 n+^2 n+^3 n+^4 n+^5 n+^6 n+^7 n+^8 n+^9 n+^10
Mode 0
ABSD Delay (n) tV 7 6 ...
Data Out 2 ...
...
Figure 8.103 AutoBoot Sequence (QE = 1)
4
CE#
SCK
4 0 4 0
High Impedance
0 4 0
Mode 3
Mode 0
IO 0
IO 1
IO 2
IO 3
5 1
Data Out 1
5 1 5 1 5 1
7 3
6 2
7 3 7 3
6 2 6 2
7 3
6 2
Data Out 2 Data Out 3 Data Out 4
ABSD Delay (n) tV
0 1 2 ... n- 1 n n+ 1 n+ 2 n+ 3 n+ 4 n+ 5 n+ 6 n+ 7 n+ 8 n+^9 n+^10 ...
4 0
5 1 ...
7 3 ...
6 2 ...
Data Out 5
...
...
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 139
AUTOBOOT REGISTER READ OPERATION (RDABR, 14h)
The AutoBoot Register Read command is shifted in. Then the 32bit AutoBoot Register is shifted out, least significant byte first, most significant bit of each byte first. It is possible to read the AutoBoot Register continuously by providing
multiples of 32bits.
RDABR operation is valid only at SPI mode only.
Figure 8.104 RDABR Sequence In SPI Mode
Instruction = 14 h
7
CE#
SCK
SI
SO 3 2 1 0
Data Out 1
6 5
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
4
tV
...
...
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 140
AUTOBOOT REGISTER WRITE OPERATION (WRABR, 15h)
Before the WRABR command can be accepted, a Write Enable (WREN) command by the device, which sets the Write Enable Latch (WEL) in the Status Register to enable any write operations.must be issued and decoded
(^) The WRABR command is entered by shifting the instruction and the data bytes, least significant byte first, most

signif icant bit of each byte first. The WRABR data is 32bits in length.
CE# must be driven high after the 32nd bit of data has been latched. If not, the WRABR command is not executed. As soon as CE# is driven high, the WRABR operation is initiated. While the WRABR operation is in progress, Status
Register bit is “1” during the WRABR operation, and is “0” when it is completed. When the WRABR cycle is completed, thor Extended Read Register may be read to check the value of the Write In Progress (WIP) bit. The WIP e
WEL is set to “0”.
Figure 8.105 WRABR Sequence In SPI Mode
Instruction = 15 h 7
CE#
SCK
SI 3 2
SO
1 0
Data In 1
6 5
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
4
High Impedance
...
...
Figure 8.106 WRABR Sequence In QPI Mode
15 h
Mode 3 0 1
Mode 0
2 3
7 : 4 3 : 0
CE#
SCK
IO[ 3 : 0 ]
Data In 1
...
...
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 141
8.47 READ BANK ADDRESS REGISTER OPERATION (RDBR: 16h/C8h)
The Read Bank Address Register (RDBR) instruction allows the Bank Address Register contents to be read. is used to read only a volatile Bank Address Register. RDBR
(^) The instruction code is first shifted in. Then the 8-bit Bank Register is shifted out. It is possible to read the Bank
Address Register continuously by pro viding multiples of eight bits.
Data is shifted in from SI and data is shifted out from SO in SPI sequence whereas data in and out is via four pins (IO0-IO3) in QPI sequence.
(^) Figure 8.107 Read Bank Address Register Sequence In SPI Mode
Instruction = 16 h/C 8 h
7

CE#
SCK
SI
SO 3 2 1 0
Data Out
6 5
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
4
tV
Figure 8.108 Read Bank Address Register Sequence In QPI Mode
16 h/C 8 h
Mode 3 0 1
Mode 0
2 3
7 : 4 3 : 0
CE#
SCK
IO[ 3 : 0 ]
tV
Data Out^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 142
8.48 WRITE BANK ADDRESS REGISTER OPERATION (WRBRNV: 18h, WRBRV: 17h/C5h)
The Write Bank Address Register (WRBRNV and WRBRV) instruction is used to write address bits above A23, into the Bank Address Register (BAR). WRBRNV is used to write the non-volatile Bank Address Register and WRBRV
is used to write the volatile Bank Address Register. Control bit (EXTADD) that is also in BAR[7]. BAR provides the high order addresses needed by devices having The instruction is also used to write the Extended Address
more than 128Mbits (16Mbytes), when(BAR[7] EXTADD = 0). using 3-byte address commands without extended addressing enabled
(^) To write non-volatile Bank Address Register, a standard Write Enable (06h) instruction must previously have been

executed for the device to accept WRBRNV(18h) instruction (Status Register bit WEL must equal “1”).
To write volatile When using C5h instruction, a standard Write Enable (06h) instruction must previously have been executed for the Bank Address Register, C5h or 17h command can be used.
device to accept C5h But 17h instruction does not require a standard Write Enable (06h) operation. (Status Register bit WEL remains instruction (Status Register bit WEL must equal “1”).
“0”).
The WRBRNlength. The Write In Progress (WIP) V/WRBRV instructions arebit is “1” during WRBRNV followed by the data byte. The Bank Address Register is one /WRBRV operation, and is “0” when it is completed. data byte in
Any bank address bit reserved for the future should always be written as “0”. whereas data is shifted in via four pins (IO0-IO3) in QPI. Data is shifted in from SI and in SPI
(^) Bit 7 (EXTADD) of volatile Bank Address Register is also writable with EN4B (B7h)/EX4B (29h) instruction.

But B7h/29h instruction does not require a standard Write Enable (06h) (Status Register bit WEL remains 0).
Note: When WRBRNV is executed, the volatile Bank Address Register is set as well as the nonRegister. - volatile Bank Address
Figure 8.109 Write Bank Address Register Sequence In SPI Mode
Instruction = 18 h or 17 h/C 5 h
CE#
SCK
SI
SO
Data In
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
7 6 5 4 3 2 1 0
High Impedence
(^) Figure 8.110 Write Bank Address Register Sequence In QPI Mode
1718 hh or/C 5 h
Mode 3 0 1
Mode 0

2 3
7 : 4 3 : 0
CE#
SCK
IO[ 3 : 0 ]
Data In
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 143
8.49 ENTER 4-BYTE ADDRESS MODE OPERATION (EN4B, B7h)
The Enter 4beyond 128Mb. To execute EN4B operation, the host drives CE# low, sends the instruction code and then drives -byte Address Mode instruction allows 32bit address (A31-A0) to be used to access the memory array
CE# high. The Exit 4 - byte Address Mode instruction can be used to exit the 4-byte address mode.
A Write Enable (WREN, 06h) command is not required prior to EN4B (B7h) command.
Note: The EN4B instruction will set the Bit 7 (EXTADD) of the volatile Bank Address Register to “1” the non-volatile Bank Address Register. , but will not change
(^) Figure 8.111 Enter 4-byte Address Mode Sequence In SPI Mode
Instruction = B 7 h

CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High Impedance^
(^) Figure 8.112 Enter 4-byte Address Mode Sequence In QPI Mode
B 7 h

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 144
8.50 EXIT 4-BYTE ADDRESS MODE OPERATION (EX4B, 29h)
In order to be backward compatible, the Exit used to access the memory array up to 128Mb. The Bank Address Register must be used to access the memory 4 - byte Address Mode instruction allows 24bit address (A23-A0) to be
array beyond 128Mb. To execute EX4B operation, the host drives CE# low, sends the idrives CE# high. nstruction code and then
(^) A Write Enable (WREN, 06h) command is not required prior to EX4B (29h) command.
Note: The EX4B instruction will reset the Bit 7 (EXTADD) of the volatile Bank Address Register to “0” change the non-volatile Bank Address Register. ”, but will not
(^) Figure 8.113 Exit 4-byte Address Mode Sequence In SPI Mode
Instruction = 29 h

CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High Impedance^
(^) Figure 8.114 Exit 4-byte Address Mode Sequence In QPI Mode
29 h

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 145
8.51 READ DYB OPERATION (RDDYB, FAh or 4RDDYB, E0h)
FAh (EXTADD=0) is followed by a 3• FAh (EXTADD=1) is followed by a 4-byte address (A23-byte address (A31-A0) or-A0) or (^)

• E0h is followed by a 4-byte address (A31-A0)
The instruction is used to read Dynamic Protection Bit (DYB) status of the given sector/block. The instruction code is entered first, followed by the 24-bit or 32-bit address selecting location zero within the desired sector/block as
above. Then the 8at the SCK frequency by the falling edge of the SCK signal. It is possible to read the same DYB access register -bit DYB access register contents are shifted out. Each bit (SPI) or four bits (QPI) are shifted out
continuously by providing multiples of eight bita means to read the entire DYB array. Each location must be read with a separate Read DYB instruction. s. The address of the DYB register does not increment so this is not
Note: Data must be either 00h (protected) or FFh (unprotected).
Figure 8.115 Read DYB Sequence In SPI Mode (FAh [EXTADD=0], 3-byte address)
Instruction = FAh
CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^313233343536373839
Mode 0
3 - byte Address
tV
7 6 5 4 3 2 1 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 146
Figure 8.116 Read DYB Sequence In SPI Mode (FAh [EXTADD=1] or E0h, 4-byte address)
Instruction = FAh/E 0 h
CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^394041424344454647
Mode 0
4 - byte Address
tV
7 6 5 4 3 2 1 0
Figure 8.117 Read DYB Sequence In QPI Mode (FAh [EXTADD=0], 3-byte address)
FAh
CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
2 3 4 5 6 7 8 9
3 - byte Address Data Out
tV
Figure 8.118 Read DYB Sequence In QPI Mode (FAh [EXTADD=0] or E0h, 4-byte address)
FAh/E 0 h
CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
2 3 4 5 6 7 10 11
4 - byte Address Data Out
tV
8 9
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 147
8.52 WRITE DYB OPERATION (WRDYB, FBh or 4WRDYB, E1h)
Before the must previously have been executed for the device to accept Write DYB instruction (Status Register bit WEL must WRDYB/4WRDYB command can be accepted by the device, a standard Write Enable (06h) instruction
equal 1).
• • FBh (EXTADD=0) is followed by a 3FBh (EXTADD=1) is followed by a 4 - -byte address (A23byte address (A31--A0) orA0) or (^)

• E1h is followed by a 4-byte address (A31-A0)
The WRDYBbit address selecting location zero within the desired sector/block as abov/4WRDYB command is entered by driving CE# low, followed by the instruction code, the 24e, then the data byte. The DYB Access -bit or 32-
Register is one data byte in length.
CE# must be driven high after the eighth bit of data has been latched in. As soon as CE# is driven high, thWRDYB/4WRDYB operation is initiated. e

Note: Data must be either 00h (protected) or FFh (unprotected).
Figure 8.119 Write DYB Sequence In SPI Mode (FBh [EXTADD=0], 3-byte address)
Instruction = FBh
CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^313233343536373839
Mode 0
3 - byte Address
Data In
High Impedence
7 6 5 4 3 2 1 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 148
Figure 8.120 Write DYB Sequence In SPI Mode (FBh [EXTADD=1] or E1h, 4-byte address)
Instruction = FBh/E 1 h
CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^394041424344454647
Mode 0
4 - byte Address
Data In
High Impedence
7 6 5 4 3 2 1 0
Figure 8.121 Write DYB Sequence In QPI Mode (FBh [EXTADD=0], 3-byte address)
FBh
CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
2 3 4 5 6 7 8 9
3 - byte Address Data In
Figure 8.122 Write DYB Sequence In QPI Mode (FBh [EXTADD=1] or E1h, 4-byte address)
FBh/E 1 h
CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
2 3 4 5 6 7 10 11
4 - byte Address Data In
8 9
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 149
8.53 READ PPB OPERATION (RDPPB, FCh or 4RDPPB, E2h)
FCh (EXTADD=0) is followed by a FCh (EXTADD=1) is followed by a 4 3 - -byte address (A23byte address (A31--A0) orA0) or (^)

E2h is followed by a 4 - byte address (A31-A0)
The instruction code is shifted into SI by the rising edges of the SCK signal, followed by the 24selecting location zero within the desired sector/block as above. Then the 8-bit PPB Access Register contents are -bit or 32-bit address
shifted out on SO. The RDPPB/4RDPPB is supporting only SPI, not supporting QPI.
It is possible to read the same PPB Access Register continuouof the PPB Access Register does not increment so this is not a means to read the entire PPB array. Each location sly by providing multiples of eight bits. The address
must be read with a separate Read PPB command.
Not e: Data must be either 00h (protected) or FFh (unprotected).
Figure 8.123 Read PPB Sequence (FCh [EXTADD=0], 3-byte address)
Instruction = FCh
CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^313233343536373839
Mode 0
3 - byte Address
tV
7 6 5 4 3 2 1 0
Figure 8.124 Read PPB Sequence (FCh [EXTADD=1] or E2h, 4-byte address)
Instruction = FCh/E 2 h
CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^394041424344454647
Mode 0
4 - byte Address
tV
7 6 5 4 3 2 1 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 150
8.54 PROGRAM PPB OPERATION (PGPPB, FDh or 4PGPPB, E3h)
Before the After the WREN command has been decoded, the device will set the Write Enable Latch (WEL) in the Status Program PPB (PGPPB/4PGPPB) command is sent, a Write Enable (WREN) command must be issued.
Register.
FDh (EXTADD=0) is followed by a 3FDh (EXTADD=1) is followed by a 4--byte address (A23byte address (A31--A0) orA0) or (^)

E3h is followed by a 4 - byte address (A31-A0)
The 24 - bit or 32PGPPB/4PGPPB-bit address selecting location zero within the desired sector/block as above. command is entered by driving CE# low, followed by the instruction code, followed by the
(^) The PGPPB/4PGPPB command affects the WIP bit in the same manner as any other programming operation. CE#

must be driven high after the last bit of address has been latched in. As soon as CE# is driven high, the PGPPB/4PGPPB operation is initiated. While the PGPPB/4PGPPB operation is in progress, the Status Register or
Extended Reduring the PGPPB/4PGPPBad Register may be read to check the value of the operation, and is “0” when it is completed. When the Write In Progress (WIP) bit. The WIP bit is “1” PGPPB/4PGPPB operation is
completed, the WEL is set to “0”.
Note: Data must be either 00h (protected) or FFh (unprotected).
Figure 8.125 Program PPB Sequence In SPI Mode (FDh [EXTADD=0], 3-byte address)
Instruction = FDh
CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^31
Mode 0
3 - byte Address
High Impedence
(^) Figure 8.126 Program PPB Sequence In SPI Mode (FDh [EXTADD=1] or E3h, 4-byte address)
Instruction = FDh/E 3 h

CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^39
Mode 0
4 - byte Address
High Impedence
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 151
Figure 8.127 Program PPB Sequence In QPI Mode (FDh [EXTADD=0], 3-byte address)
FDh
CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
2 3 4 5 6 7
3 - byte Address
(^)

Figure 8.128 Program PPB Sequence In QPI Mode (FDh [EXTADD=1] or E3h, 4-byte address)
FDh/E 3 h
CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
2 3 4 5 6 7 8 9
4 - byte Address
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 152
8.55 ERASE PPB OPERATION (ERPPB, E4h)
The Erase PPB device, a Write Enable (WREN) command must be issued and decoded by the device, which sets the Write Enable (ERPPB) command sets all PPB bits to “1”. Before the ERPPB command can be accepted by the
Latch (WEL) in the Status Register to enable any write ope rations.
The instruction code is shifted in by the rising edges of the SCK signal. CE# must be driven high after the eighth bit of the instruction byte has been latched in. This will initiate the beginning of internal erase cycle, which involves
the prebit of the instruction, the PPB erase operation will not be executed.-programming and erase of the entire PPB memory array. Without CE# being driven high after the eighth
(^) With the internal erase cycle in progress, the user can read the value of the Write In Progress (WIP) bit to check if

the operation has been completed. The WIP bit will indicate “1” when the erase cycle is in progress and “0” when the erase cycle has been completed. When the ERPPB operation is completed, the WEL is set to “0”. Erase
suspe nd is not allowed during PPB Erase.
Figure 8.129 Erase PPB Sequence In SPI Mode
Instruction = E 4 h
CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High Impedance^
(^) Figure 8.130 Erase PPB Sequence In QPI Mode
E 4 h

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 153
8.56 READ ASP OPERATION (RDASP, 2Bh)
The is shifted out, least significant byte firstRDASP instruction code is shifted in by the rising edge of the SCK signal. Then the 16, most significant bit of each byte first. Each bit is shifted out at the SCK -bit ASP register contents
frequency by the falling emultiples of 16 bits. dge of the SCK signal. It is possible to read the ASP register continuously by providing
(^) Figure 8.131 Read ASP Sequence In SPI Mode

8 9 ... 15 16 17 ... 23
Instruction = 2 Bh
CE#
SCK
SI
SO
Mode 3 0 1 2 3 4 5 6 7
Mode 0
tV
7 6 ... 0 15 14 ... 8
1 st byte Data Out 2 nd byte Data Out
Figure 8.132 Read ASP Sequence In QPI Mode
2 Bh
CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
2 3 4 5
tV Data Out 1 st byte Data Out 2 nd byte
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 154
8.57 PROGRAM ASP OPERATION (PGASP, 2Fh)
Before the Program ASP (must be issued. After the WREN command has been decoded, the device will set the Write Enable Latch (WEL) in PGASP) command can be accepted by the device, a Write Enable (WREN) command
the Status Register to enable any write operations.
The significant byte first, most significant bit of each byte first. The ASP Register is two data bytes in length. The PGASP command is entered by driving CE# low, followed by the instruction code and two data bytes, least PGASP
command affects the Write In Progress (WIP) bit in the same manner as any other programming operation.
CE# input must be driven high after the sixteenth bit of data has been latched in. If not, the not executed. As soon as CE# is driven high, the PGASP operation is initiated. While the PGASPPGASP operation is in command is
progress, the Status Registerbit is “1” during the PGASP operation, and is “0” when it is completed. When the or the Extended Read Register may be read to check the value of WIP bit. The WIP PGASP operation is completed,
the WEL is set to “0”.
Figure 8.133 Program ASP Sequence In SPI Mode
Instruction = 2 Fh
CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^1314151617 ...^212223
Mode (^01) st byte Data In
High Impedence

7 6 ... 2 1 0 15 14 ...^1098
2 nd byte Data In
(^) Figure 8.134 Program ASP Sequence In QPI Mode
2 Fh

SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
2 3 4 5
(^1) Data Inst byte (^2) Data Innd byte

CE#
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 155
8.58 READ PPB LOCK BIT OPERATION (RDPLB, A7h)
The Read PPB Lock Bit (read the PPB Lock Register continuously by providing multiples of eight bits. The PPB Lock Register contents may RDPLB) command allows the PPB Lock Register contents to be read. It is possible to
only be read when the device is in standby state with no other opthe Write In Progress (WIP) bit before issuing a new command to the device.eration in progress. It is recommended to check
(^) RDPLB operation is valid only at SPI mode only.
(^) Figure 8.135 Read PPB Lock Bit Sequence In SPI Mode
Instruction = A 7 h
7

CE#
SCK
SI
SO 3 2 1 0
Data Out
6 5
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
4
tV
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 156
8.59 WRITE PPB LOCK BIT OPERATION (WRPLB, A6h)
The Write PPB Lock Bit (WRPLB) command mode. Before the WRPLB command can be accepted by the device, a Write Enable (WREN) command must be only clears the PPB Lock (PPBLK) bit to “ 0 ” in the Persistent Protection
issued and dwrite operations.ecoded by the device, which sets the Write Enable Latch (WEL) in the Status Register to enable any
(^) The WRPLB command is entered by driving CE# low, followed by the instruction code. CE# must be driven high

after the eighth bit of instrucis driven high, the WRPLB operation is initiated. While the WRPLB operation is in progress, the Status Register tion has been latched in. If not, the WRPLB command is not executed. As soon as CE# or
Extended Read Register during the WRPLB operation, and is “0” when it is completed. When the WRPLB operation is cmay still be read to check the value of the Write In Progress (WIP) bit. The WIP bit is “1” ompleted, the WEL
is set to “0”.
Figure 8.136 Write PPB Lock Bit Sequence In SPI Mode
Instruction = A 6 h
CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High Impedance^
(^) Figure 8.137 Write PPB Lock Bit Sequence In QPI Mode
A 6 h

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 157
8.60 SET FREEZE BIT OPERATION (SFRZ, 91h)
The Set FREEZE Bit (SFRZ) command section 6.6.3 PPB Lock Register for more only detailsets FREEZE. Before the SFRZ command can be accepted by the device, a (PPB Lock Register bit7) to “1”. Please refer to the
Write Enable (WREN) command must be issued and decoded by the device, which sets the Write Enable Latch (WEL) in the Status Register to enable any write operations.
(^) The SFRZ command is entered by driving CE# low, followed by the instruction code. CE# must be driven high after

the eighth bit of instruction has been latched in. If not, the SFRZ command is not executed. As soon as CE# is driven high, the SFRZ operation is initiated. While the SFRZ operation is in progress, the Status Register or
Extended Read Register during the SFRZ operation, and is “0” when it is completed. When the SFRZ operation is cmay still be read to check the value of the Write In Progress (WIP) bit. The WIP bit is “1” ompleted, the WEL is
set to “0”.
Figure 8.138 Set FREEZE Bit Sequence In SPI Mode
Instruction = 91 h
CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High^ Impedance^
(^) Figure 8.139 Set FREEZE Bit Sequence In QPI Mode
91 h

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 158
8.61 READ PASSWORD OPERATION (RDPWD, E7h)
The correct password value may be read only afterselected by programming the Password Protection Mode bit to “0” in the ASP Register (ASP it is programmed and before the Password Mode has been [2]). After the Password
Protection Mode is selected the RDPWD command is ignored.
The significant bit of each byte first. Each bit is shifted out at the SCK frequency by the falling edge of the SCK signal. RDPWD command is shifted in. Then the 64-bit Password is shifted out, least significant byte first, most
It is possible to read the Password continuously by pr oviding multiples of 64bits.
RDPWD operation is valid only at SPI mode only.
Figure 8.140 Read password Sequence In SPI Mode
Instruction = E 7 h
CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^151617 ...^23 ...^6465 ...
Mode 0
tV
7 6 ... 0 15 14 ...^8 ... 63 62 ... 56
71
1 st byte Data Out 2 nd byte Data Out ... 8 th byte Data Out
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 159
8.62 PROGRAM PASSWORD OPERATION (PGPWD, E8h)
Before the Program Password (command must be issued and decoded by the device which sets the Write Enable Latch (WEL) to enable the PGPWD) command can be accepted by the device, a Write Enable (WREN)
PGPWDthe Password Protection Mode bit to “0” in the ASP Register (ASP operation. The password can only be programmed before the Password Mode is selected [2]). After the Password Protection Mode is by programming
selected the PGPWD command is ignored.
The bytes, least significant byte first, most significant bit of each byte first. The password is 64bits in length.PGPWD command is entered by driving CE# low, followed by the instruction code and the password data
(^) CE# must be driven high after the 64th bit of data has been latched. If not, the PGPWD command is not executed.

As soon as CE# is driven high, the Status Register or Extended Read RegisterPGPWD may be read to check the value of the Write operation is initiated. While the PGPWD operation is in progress, the In Progress (WIP) bit. The
WIP bicompleted, the Write Et is “1” during the nable Latch (WEL) is set to “0”PGPWD operation, and is “0” when it is completed. When the. PGPWD operation is
(^) Figure 8.141 Program Password Sequence In SPI Mode
Instruction = E 8 h

CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^151617 ...^23 ...^6465 ...
Mode 0
7 6 ... 0 15 14 ... 8 ... 63 62 ... 56
71
1 st byte Data In 2 nd byte Data In ... 8 th byte Data In
High Impedence
(^) Figure 8.142 Program Password Sequence In QPI Mode
E 8 h

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
2 3 4 5
(^1) Data Inst byte (^2) Data Innd byte ... (^8) Data Inth byte

... 16 17
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 160
8.63 UNLOCK PASSWORD OPERATION (UNPWD, E9h)
In the Password Protection mode, the PPB Lock bit is cleared to bit can only be set to 1 by the Unlock Password command. “ 0 ” during POR or Hardware Reset. The PPB Lock
(^) A Write Enable (WREN) command is not required prior to UNPWD command

The bytes, least significant byte first, most significant bit of each byte first. The paUNPWD command is entered by driving CE# low, followed by the instruction code and the password data ssword is 64bits in length.
(^) CE# must be driven high after the 64th bit of data has been latched. If not, the UNPWD command is not executed.

As soon as CE# is driven high, the Status Register or Extended Read RegisterUNPWD may be read to check the value of the operation is initiated. While the UNPWDWrite In operation is in progress, the Progress (WIP) bit. The
WIP bit is “1” during the UNPWD operation, and is “0” when it is completed.
If the UNPWD command is ignored. This returns the device to standby state, ready for a new command such as a retry UNPWD command supplied password does not match the hidden password in the Password Register, the
of the UNPWD command. If the password does match, the PPB Lock bit is set to “1”.
Figure 8.143 Unlock Password Sequence In SPI Mode
Instruction = E 9 h
CE#
SCK
SI
SO
Mode 3 0 1 ...^789 ...^151617 ...^23 ...^6465 ...
Mode 0
7 6 ... 0 15 14 ...^8 ... 63 62 ... 56
71
1 st byte Data In 2 nd byte Data In ... 8 th byte Data In
High Impedence
(^) Figure 8.144 Unlock Password Sequence In SPI Mode
E 9 h

CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0
2 3 4 5
(^1) Data Inst byte (^2) Data Innd byte ... (^8) Data Inth byte

... 16 17
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 161
8.64 GANG SECTOR/BLOCK LOCK OPERATION (GBLK, 7Eh)
The Gang Sector/Block Lock (GBLK) instruction provides a quick method to set all bits to “0” at once. DYB (Dynamic Protection Bit)
(^) Before the GBLK (7Eh) command can be accepted by the device, a Write Enable (WREN) command must be

issued and decoded by the device, which sets the Write Enable Latch (WEL) in the Status Register to enable any write operations.
(^) The sequence of issuing GBLK instruction is: drive CE# low → send GBLK instruction code → drive CE# high.

The instruction code will be shifted into the device on the rising edge of SCK.
The GBLK command is accepted in both SPI and QPI mode. The CE# must go high exactly at the byte boundary, otherwise, the instruction will be ignored. While the GBLK operation is in progress, the Status Register or Extended
Read RegisterGBLK operation, and is “0” when it is completed. may be read to check the value of the Write In Progress (WIP) bit. The WIP bit is “1” during the
(^) Figure 8.145 Gang Sector/Block Lock Sequence In SPI Mode
Instruction = 7 Eh

CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High Impedance^
(^) Figure 8.146 Gang Sector/Block Lock Sequence In QPI Mode
7 Eh
CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 162
8.65 GANG SECTOR/BLOCK UNLOCK OPERATION (GBUN, 98h)
The Gang Sector/Block Unlock (GBUN) instruction provides a quick method to clear all Bit) bits to “ 1 ” at once. DYB (Dynamic Protection
(^) Before the GBUN (98h) command can be accepted by the device, a Write Enable (WREN) command must be

issued and decoded by the device, which sets the Write Enable Latch (WEL) in the Status Register to enable any write operations.
(^) The sequence of issuing GBUN instruction is: drive CE# low → send GBUN instruction code → drive CE# high.

The instruction code will be shifted into the device on the rising edge of SCK.
The GBUN command is accepted in both SPI and QPI mode. The CE# must go high exactly at the byte boundary, otherwise, the instruction will be ignored and not be executed. While the GBUN operation is in progress, the Status
Register bit is “1” during the GBUN operation, andor Extended Read Register may be read to check the value of the Write In Progress (WIP) bit. The WIP is “0” when it is completed.
(^) Figure 8.147 Gang Sector/Block Unlock Sequence In SPI Mode
Instruction = 98 h

CE#
SCK
SI
Mode 3 0 1 2 3 4 5 6 7
Mode 0
SO High Impedance^
(^) Figure 8.148 Gang Sector/Block Unlock Sequence In QPI Mode
98 h
CE#
SCK
IO[ 3 : 0 ]
Mode 3 0 1
Mode 0

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 163
9. ELECTRICAL CHARACTERISTICS
9.1 ABSOLUTE MAXIMUM RATINGS (1)
Storage Temperature - 65 °C to +1 50 °C
Surface Mount Lead Soldering Temperature Standard PackageLead-free Package^ 240°C 3 Seconds260°C 3 Seconds^
Input Voltage with Respect to Ground on All PinsAll Output Voltage with Respect to Ground - -0.5V to 0.5V to VVCC + 0.5V
CC^ + 0.5V^
VCC IS25LPIS25WP^ - -0.5V to +6.0V0.5V to +2.5V^
Notes:1. Applied conditions greater than those listed in “Absolute Maximum Ratings” may cause permanent damage to the
device. This is athose indicated in the operational stress rating only and functional operation of the sections of this specification is not implied. Exposure to absolute maximum device at these or any other conditions above

rating conditions for extended periods may affect reliability.ANSI/ESDA/JEDEC JS- 001
9.2 OPERATING RANGE
Operating Temperature Extended Grade EAutomotive Grade A3^ - -^4 40°C to 125°C^0 °C to^105 °C^
VCC Power Supply IS25LPIS25WP^ 2.3V (VMIN) 1.65V (VMIN) –^ – 3.6V (VMAX); 3.01.95V (VMAX); 1.8V (Typ)V (Typ)^
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 164
9.3 DC CHARACTERISTICS
(-40°C to 125°CSymbol , 2.3V Parameter– 3.6V for 3.0V device & 1.65V – 1.95ConditionV for 1.8V device ) (^) Min Typ(2) Max Units
ICC1 VCC Active Read current(3)
NORD at 80 MHz 8 9
mA
FRD Single at FRD Dual at 166166 MHzMHz 191 1112
FRD Quad at FRD Single at 166133 MHzMHz (^194 1015) .5 (^)
FRD Dual at FRD Quad at 133133 MHzMHz (^1102) .5 (^1311) .5 (^)
FRD Quad at FRD Quad at 83104 MHzMHz (^1011 1112)
FRD Single DTR at FRD Dual DTR at 8080 MHzMHz 810 .5 911 .5
FRD Quad DTR at 80 MHz 11 12
ICC2 VCC Program Current CE# = VCC 85 °C^25 30

(6)
mA
105125 °C°C 3030 (6)
ICC3 VCC WRSR Current CE# = VCC 85 °C^25    30
(6)
105125 °C°C 3030 (6)
ICC4 V(SER/4SER/BER32/4BER32/BER64/4BER64)CC^ Erase Current CE# =^ VCC^85 °C^25    30
(6)
105125 °C°C 3030 (6)
ICC5 VCC Erase Current (CE) CE# = VCC 85 °C^25    30
(6)
105125 °C°C 3030 (6)
ISB1 VCurrent CMOSCC^ Standby
IS25LP
CE# = VVIN = GNDCC, or VCC (4)
85 °C 8 30 (6)
μA
105125 °C°C 45 70 (6)
IS25WP 85 °C^8 35
(6)
105125 °C°C 45 75 (6)
ISB2 Deep power down current
IS25LP
CE# = VVIN = GNDCC, or VCC (4)
85 °C 5 15 (6)
μA
105125 °C°C 20 35 (6)
IS25WP 85 °C^1 10
(6)
105125 °C°C 15 25 (6)
IILILO Input Leakage Current Output Leakage Current VVININ = 0V to V= 0V to VCCCC ±1±1(5)(5) μAμA (^)
VVILIH(1)(1) Input Low Voltage Input High Voltage (^) 0.7V-0.5CC (^) V0.CC (^3) + 0.3VCC VV (^)
VVOLOH Output Low Voltage Output High Voltage^ IIOLOH^ = 100 μA= -100 μA^ VCC - 0.2 0. 2 VV^

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 165
Notes:1. Maximum DC voltage on input or I/O pins is VCC + 0.5V. During voltage transitions, input or I/O pins may overshoot
VCC by +2.0V for a period of time not to exceed 20ns. Minimum DC voltage on input or I/O pins is -0.5V. During voltage transitions, input or I/O pins may undershoot GND by -2.0V for a period of time not to exceed

20ns.Typical values are included for reference only and are not guaranteed or tested. Typical values are measured at^ VCC
= Outputs are unconnected during reading VCC^ (Typ), TA=25°C.^ data so that output switching current is not included.
4.5. VThe Max of IIN = Vcc for the dedicatedLI and ILO for the RESET# pindedicated RESET# pin(or ball). (^) (or ball) is ±2 μA.

These parameters are characterized and are not 100% tested.
9.4 AC MEASUREMENT CONDITIONS
Symbol Parameter Min Max Units
CL Load CapacitanceLoad Capacitance 3010 pFpF^
TR,TFVIN Input Rise and Fall TimesInput Pulse Voltages 0.2VCC to 0.8VCC 5 nsV
VREFIVREFO Input Timing Reference VoltagesOutput Timing Reference Voltages 0.3VCC0.5V to 0.7VCC CC VV (^)

Figure 9. 1 Output test load & AC measurement I/O Waveform
OUTPUT PIN
1. 8 k
1. 2 k 10 / 30 pf
0. 8 VCC
0. 2 VCC
Input VCC/ 2 Measurement LevelAC
9.5 PIN CAPACITANCE
(TA = 25°C, VCC=3V for IS25LP, VCC=1.8V for IS25WP, 1MHz)
Symbol Parameter Test Condition (^) MinIS25LP Max MinIS25WP Max^ Units
CIN Input Capacitance (CE#, SCK) VIN = 0V - 6 - 6 pF
CIN/OUT Input/Output Capacitance (other pins) VIN/OUT = 0V - 8 - 10 pF
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 166
9.6 AC CHARACTERISTICS
(Symbol -40°C to 125°C , 2.3V Parameter – 3.6V for 3.0V device & 1.65V– 1.95V for 1.8V device) (^) Min Typ(2) Max Units
fCT
Clexcept for fast read ock Frequency
DTR and read (03h)^
IS25LP VCC = 2.7V to 3.6VVCC = 2.3V to 3.6V^00 166133 MHzMHz^
IS25WP VCC = 1.7V to 1.95VVCC = 1.65V to 1.95V^00 166133 (4, 5 , 6).^ MHzMHz^
Clock Frequency for fast read DTR:SPI DTR, Dual DTR, Dual I/O DTR, Quad I/O DTR, and QPI
fC DTR.Clock Frequency for read^ (03h) 00 8080 MHzMHz^
ttCLCH(1) SCK Rise Time (peak to peak) 0.1 V/ns
CHCL(1)^ SCK Fall Time ( peak to peak)^ 0.1^ V/ns^
tCKH SCK High Time For read For others(03h) 0.45 x 1/0.45 x 1/ffCCTmaxmax^ ns
tCKL SCK Low Time For read For others(03h) 0.45 x 1/0.45 x 1/ffCCTmaxmax^ ns
tCEH CE# High Time For read modeFor write mode^207 nsns^
ttCS CH CE# Setup Time CE# Hold Time 33 nsns (^)
ttCHSL CE# Not Active Hold Time 3 ns
SHCH^ CE# Not Active Setup Time^3 ns^
tDS Data In Setup Time STRDTR^ 1.5^2 ns
tDH Data in Hold Time STRDTR^ 1.5^2 ns
tV Output Valid IS25LP^
2.7~3.6V, -40°C to 8 5°C @10pF^ 5.5(4).^
ns
@30pF 7.0(4).
2.3~3.6V, -40°C to 125°C @10pF@30pF^ 6.58.0.^
IS25WP 1.65~1.95V, -40°C to 125°C^ @10pF@30pF^57 .5.0.^
ttOH Output Hold Time 2 ns
tDISWHSL(1)^ (3) Output Disable Time Write Protect Setup Time^20 8 nsns^

tSHWL(3)^ Write Protect Hold Time 100 ns^
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 167
(^) Symbol Parameter Min Typ(2) Max Units
ttHLCHCHHH HOLD Active Setup Time relative to SCKHOLD Active Hold Time relative to SCK 22 nsns (^)
ttHHCHCHHL HOLD Not Active Setup Time relative to SCKHOLD Not Active Hold Time relative to SCK 22 nsns (^)
ttLZHZ(1)(1) HOLD to Output Low ZHOLD to Output High Z 88 nsns (^)
tEC
Sector Erase Time (4Kbyte)Block Erase Time (32Kbyte) (^) 0.1 (^1004 300) 0.5 mss
Block Erase time (64Kbyte)Chip Erase Time 0.1 357 1.0 90 ss (^)
tPP Page Program Time 0.2 0.8 ms
tRES1(1) Release deep power down IS25LPIS25WP^35 μs
ttDPW (1) Deep power downWrite Status Register time (^2 153) msμs (^)
ttSUSRS(1)(1) Suspend to Resume to next suspendread ready 8 - 0 100 - μsμs (^)
ttSRSTRESET(1)(1) Software Reset recovery timeRESET# pin low pulse width 100 35 μsns (^)
tHWRST(1) Hardware Reset recovery time 35 μs
Notes:1. These parameters (^) are characterized and not 100% tested.

Typical values are for reference VCC = VCC (Typ), TA=25°C. purpose only and are not guaranteed nor tested. Typical values are measured at
3.4. Only applicable as a constraint for a WRITE STATUS REGISTER command when SRWD iValues are guaranteed by characterization and not 100% tested in production. s set at 1
5.6. 166MHz at Max. Frequency for RDDYB (FAh) or 4RDDYB (E0h) in QPI mode is 133MHz.- 40 °C to 1 05 °C (^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 168
9.7 SERIAL INPUT/OUTPUT TIMING
Figure 9.2 SERIAL INPUT/OUTPUT TIMING (Normal Mode) (1)
SO HI-Z
SI
SCK
CE#
VALID IN
tCS
tCKH tCKL
tDS tDH
tCH
tCEH
tV tDIS
HI-Z
tOH
VALID IN
VALID OUTPUT
tCHSL tSHCH
Note1: For SPI Mode 0 (0,0)
(^)

Figure 9.3 SERIAL INPUT/OUTPUT TIMING (DTR Mode) (1)
SCK
CE#
tCS
tCKH tCKL
tCH
tCEH
tCHSL tSHCH
SO HI-Z
SI VALID IN
tDS tDH
tV tOH tDIS HI-Z
VALID IN VALID IN
Output Output
tV
Note1: For SPI Mode 0 (0,0)
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 169
Figure 9. 4 HOLD TIMING
SI
SO
SCK
CE#
HOLD#
tCHHL tHLCH
tCHHH
tHHCH
tHZ tLZ
(^)
(^) Figure 9. 5 WRITE PROTECT SETUP AND HOLD TIMIMNG DURING WRITE STATUS REGISTER (SRWD=1)
Instruction = 01 h

CE#
SCK
SI
SO
Data In
Mode 3 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Mode 0
7 6 5 4 3 2 1 0
High Impedence
WP# tWHSL tSHWL
Note: WP# must be kept high until the embedded operation finish.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 170
9.8 POWER-UP AND POWER-DOWN
At Powersimple pull-up and Power-up resistor on -down, the device must beCE# is recommended.) NOT SELECTED until Vcc reaches at the right level. (Adding a
(^) Power up timing
VCC
VCC(max)
VCC(min)
VWI
tVCE Device is fully accessible
Chip Selection Not Allowed
= Vcc min. to CE# Low
Time
SymboltVCE(1) Vcc(min) to CE# Low Parameter Min. 300 Max Unitus
VWI(1) Write Inhibit Voltage IS25LPIS25WP^ 2.11.4^ V

Note: These parameters are characterized and not 100% tested.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 171
9.9 PROGRAM/ERASE PERFORMANCE
Sector Erase Time (4Kbyte)Parameter^ Typ^100 Max^300 Unitms^
Block Erase Time (32Kbyte)Block Erase Time (64Kbyte) 0.10. 147 0.51.0^ ss^
Page Programming TimeChip Erase Time^ 0.^352 0.8^90 mss^
Byte Program 8 40 μs
Note: These parameters are characterized and not 100% tested.
9.10 RELIABILITY CHARACTERISTICS
ParameterEndurance (^1) 00,000Min Max- CyclesUnit (^) JEDEC Standard Test MethodA117 (^)
Data RetentionLatch-Up - 100 20 +100 - YearsmA JEDEC Standard A117JEDEC Standard 78

Note: These parameters are characterized and not 100% tested.
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 172
10. PACKAGE TYPE INFORMATION
10.1 8 - CONTACT ULTRA-THIN SMALL OUTLINE NO-LEAD (WSON) PACKAGE 8x6mm (L)
Note:
1. Please handling precautions) for assembly guidelinesclick here to refer to Application Note (AN25D011, Thin USON/WSON/XSON package.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 173
10.2 16-LEAD PLASTIC SMALL OUTLINE PACKAGE (300 MILS BODY WIDTH) (M)
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 174
10.3 24-BALL THIN PROFILE FINE PITCH BGA 6x8mm 4x6 BALL ARRAY (G)
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 175
10.4 24-BALL THIN PROFILE FINE PITCH BGA 6x8mm 5x5 BALL ARRAY (H)
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 176
10.5 8-Pin JEDEC 208mil Broad Small Outline Integrated Circuit (SOIC) PACKAGE (B)
IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 177
10.6 8 Contact Ultra-Thin Small Outline No-Lead (WSON) PACKAGE 6X5MM (K)
Note:
1. Please handling precautions) for assembly guidelinesclick here to refer to Application Note (AN25D011, Thin USON/WSON/XSON package.
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 178
11. ORDERING INFORMATION – Valid Part Numbers
(^) IS25LP 128 F - J B L E :P
(^) PBO (Polybenzoxazole) LAYER

:PBlank = Die Overcoat process = Without Die Overcoat process-PBO layer (Call Factory)-PBO layer
(^)
TEMPERATURE RANGEE = Extended (-40°C to +105°C) (^)

A3 = Automotive Grade ( - 40°C to +125°C)
PACKAGING CONTENTL = RoHS compliant
(^) PACKAGE Type
BK = 8 = 8--pin SOICcontact WSON 6x5mm 208mil (^)

L = 8M = 16-contact WSON (8x6mm)-pin SOIC 300mil
G = H = 2424 - -ball TFBGA ball TFBGA 5x5 ball array4x6 ball array (Call Factory)
W = KGD (Call Factory)
(^) Option
JR = = StandardDedicated RESET# for 16 (^) - pin SOIC/24-ball BGA

BQ = = QE bit set to 1Optional BP Table
(^)
Die RevisionF = Revision F (^)
(^)
Density128 = 128 (^) Megabit
(^)
BASE PART NUMBERIS = Integrated Silicon Solution Inc. (^)
(^2) 25WP = FLASH, 1.65V ~ 1.95V, 5 LP = FLASH, 2.30V ~ 3.60V, QPIQPI (^)
(^)
(^)

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 179
(^)
Density,Voltage Frequency (MHz) (^) E-Temp.Order Part Number Package
(-40°C to +105°C) Auto A3(-40°C to +12-Temp.5°C(1))^

128M,3V STR 166,DTR 80
IS25LP128F-JBLE IS25LP128F-JBLA3 8 - pin SOIC 208mil
IS25LP128F-JKLE IS25LP128F-JKLA3 8 - contact WSON 6x5mm
IS25LP128FIS25LP128F--JJLLEMLE^ IS25LP128FIS25LP128F--JJLLMLA3A3^8 - contact WSON 8x6mm 16 - pin SOIC 300mil
IS25LP128F-JHLE IS25LP128F-JHLA3 24 - ball TFBGA 6x8mm 5x5 ball array
IS25LP128F-RMLE IS25LP128F-RMLA3 16 - pin SOIC 300mil
IS25LP128FIS25LP128F--RHLEQBLE IS25LP128FIS25LP128F--RQHLBLA3A3 24 - ball TFBGA 6x8mm 5x5 ball array 8 - pin SOIC 208mil
IS25LP128F-QKLE IS25LP128F-QKLA3 8 - contact WSON 6x5mm
IS25LP128F-QLLE IS25LP128F-QLLA3 8 - contact WSON 8x6mm
IS25LP128FIS25LP128F--QQMLEHLE IS25LP128FIS25LP128F--QQMLHLA3A3 (^24) - ball TFBGA 6x8mm 5x5 ball array 16 - pin SOIC 300mil (^)
IS25LP128F-BBLE IS25LP128F-BBLA3 8 - pin SOIC 208mil
IS25LP128F-BKLE IS25LP128F-BKLA3 8 - contact WSON 6x5mm
IS25LP128FIS25LP128F--BBMLELLE^ IS25LP128FIS25LP128F--BBMLLLA3A3^8 - contact WSON 16 - pin SOIC 300mil8x6mm
IS25LP128F-BHLE IS25LP128F-BHLA3 24 - ball TFBGA 6x8mm 5x5 ball array

IS25WP128F

Integrated Silicon Solution, Inc.Rev.A 8 - http://www.issi.com 180
Notes:1. A3 m (^) eets AEC-Q100 requirements with PPAP.
Density,Voltage Frequency (MHz) (^) E-Temp.Order Part Number Package
(-40°C to +105°C) Auto A3(-40°C to +12-Temp.5°C(1))^

128M,1.8V STR 166,DTR 80
IS25WP128F-JBLE IS25WP128F-JBLA3 8 - pin SOIC 208mil
IS25WP128F-JKLE IS25WP128F-JKLA3 8 - contact WSON 6x5mm
IS25IS25WWP128FP128F--JJLLEMLE^ IS25IS25WWP128FP128F--JJLLMLA3A3^8 - contact WSON 8x6mm 16 - pin SOIC 300mil
IS25WP128F-JGLE IS25WP128F-JGLA3 24 - ball TFBGA 6x8mm 4x6 ball array
IS25WP128F-JHLE IS25WP128F-JHLA3 24 - ball TFBGA 6x8mm 5x5 ball array
IS25IS25WWP128FP128F--RMLERGLE IS25IS25WWP128FP128F--RRMLGLA3A3 (^24) - ball TFBGA 6x8mm 4x6 16 - pin SOIC 300milball array (^)
IS25WP128F-RHLE IS25WP128F-RHLA3 24 - ball TFBGA 6x8mm 5x5 ball array
IS25WP128F-QBLE IS25WP128F-QBLA3 8 - pin SOIC 208mil
IS25WP128F-QKLE IS25WP128F-QKLA3 8 - contact WSON 6x5mm
IS25IS25WP128FWP128F--QQMLELLE^ IS25IS25WWP128FP128F--QQMLLLA3A3^8 - contact WSON 8x6mm 16 - pin SOIC 300mil
IS25WP128F-QGLE IS25WP128F-QGLA3 24 - ball TFBGA 6x8mm 4x6 ball array
IS25WP128F-QHLE IS25WP128F-QHLA3 24 - ball TFBGA 6x8mm 5x5 ball array
IS25IS25WWP128FP128F--BBBLEKLE IS25IS25WWP128FP128F--BBBLKLA3A3 (^8) - contact WSON 6x5mm 8 - pin SOIC 208mil (^)
IS25WP128F-BLLE IS25WP128F-BLLA3 8 - contact WSON 8x6mm
IS25WP128F-BMLE IS25WP128F-BMLA3 16 - pin SOIC 300mil
IS25IS25WWP128P128FF--BBGLEHLE IS25IS25WWP128P128FF--BBGLHLA3A3 2424 - -ball TFBGA 6x8mm 4x6 ball arrayball TFBGA 6x8mm 5x5 ball array (^)

This is a offline tool, your data stays locally and is not send to any server!
Feedback & Bug Reports