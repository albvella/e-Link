
## Page 1
 
 
 
 
 
 
 
 
 
 
SIM7000 Series_TCPIP_Application 
Note_V1.01 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
SIMCOM   CONFIDENTIAL FILE

---

## Page 2
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
2
Document Title 
SIM7000 Series_TCPIP_Application Note 
Version 
1.01 
Date 
2017-10-24 
Status 
Release 
Document Control ID 
SIM7000 Series_TCPIP_ Application Note_V1.01 
 
General Notes 
SIMCom offers this information as a service to its customers, to support application and 
engineering efforts that use the products designed by SIMCom. The information provided is based 
upon requirements specifically provided to SIMCom by the customers. SIMCom has not 
undertaken any independent search for additional relevant information, including any information 
that may be in the customer’s possession. Furthermore, system validation of this product designed 
by SIMCom within a larger electronic system remains the responsibility of the customer or the 
customer’s system integrator. All specifications supplied herein are subject to change. 
 
Copyright 
This document contains proprietary technical information which is the property of Shanghai 
SIMCom Wireless Solutions Ltd, copying of this document and giving it to others and the using or 
communication of the contents thereof, are forbidden without express authority. Offenders are 
liable to the payment of damages. All rights reserved in the event of grant of a patent or the 
registration of a utility model or design. All specification supplied herein are subject to change 
without notice at any time. 
 
Copyright © Shanghai SIMCom Wireless Solutions Ltd. 2017 
SIMCOM   CONFIDENTIAL FILE

---

## Page 3
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
3
Contents 
1 
Structure ................................................................................................................ 5 
2 
Single Connection .................................................................................................. 6 
2.1 
Non-transparent mode ................................................................................................... 6 
2.1.1 
How to Establish a TCP Client Connection ...................................................... 6 
2.1.2 
How to Establish a UDP Client Connection ...................................................... 7 
2.1.3 
How to Establish a TCP Server Connection ...................................................... 8 
2.1.4 
UDP Extended Mode ......................................................................................... 9 
2.2 
Transparent Mode ....................................................................................................... 10 
2.2.1 
What is Transparent Mode .............................................................................. 10 
2.2.2 
How to Configure Transparent Mode .............................................................. 10 
2.2.3 
How to Establish Connection under Transparent Mode .................................. 11 
2.2.4 
How to Switch Between Data Mode and Command Mode............................. 12 
2.2.5 
How to handle incoming call and short message in data mode ....................... 12 
2.3 
Fix Local Port of TCP/UDP Client ............................................................................. 12 
3 
Multi Connection ................................................................................................ 13 
3.1 
As a Client ................................................................................................................... 13 
3.2 
As a TCP Server .......................................................................................................... 14 
4 
Two PDP Context ................................................................................................ 17 
5 
DNS Function ...................................................................................................... 19 
6 
Data Sending Related ......................................................................................... 20 
6.1 
Fixed Length Sending ................................................................................................. 20 
6.2 
Timed Sending ............................................................................................................ 20 
6.3 
Query Available Data Length to be Sent ..................................................................... 20 
6.4 
Select Data Transmitting Mode ................................................................................... 20 
6.5 
Query Data Transmitting Amount ............................................................................... 21 
7 
Data Receiving Related ....................................................................................... 24 
7.1 
Receive Data Automatically ........................................................................................ 24 
7.2 
Receive Data Manually ............................................................................................... 24 
8 
APPTCP States Exchange Related .................................................................... 25 
9 
Connection Closing Related ............................................................................... 27 
10 
Connection Activity Checking Related ...................................................... 28 
11 
Power Consumption with Existing Connection......................................... 29 
12 
Error Handling ............................................................................................. 30 
Appendix ..................................................................................................................... 31 
A  Related Documents ............................................................................................................ 31 
B  Terms and Abbreviations ................................................................................................... 31 
SIMCOM   CONFIDENTIAL FILE

---

## Page 4
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
4
Version History 
Date 
Version 
What is new 
Author 
2017-07-03 
1.00 
New version 
Ping.zhang 
2010-10-24 
1.01 
Deleted related description of GPRS 
Wenjie.lai 
 
 
 
Scope 
 
This document presents the AT command of TCPIP stack and application examples.  
This document can apply to SIM7000 series modules with TCPIP function.
SIMCOM   CONFIDENTIAL FILE

---

## Page 5
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
5
 
1 Structure 
 
There are two modes of connection for SIM7000 series TCP/IP application: Single connection and 
Multi connection. When in single connection mode, SIM7000 series can work at both transparent 
mode and non-transparent mode; and under these two transmission modes, SIM7000 series can be 
configured as either TCP/UDP client or TCP server. When in multi connection mode, SIM7000 
series can only work at non-transparent mode. In this mode, SIM7000 series can work as an 
absolute TCP/UDP client, which can establish 8 connections in total. In this mode, it can also be 
configured as one TCP server, which allows 7 TCP/UDP clients to be connected; and the TCP 
server also can act as a client, establishing 7 connections to one remote server. The structure of the 
TCP/IP application is given as below. 
SIM7000
CIPMUX=0
CIPMUX=1(8id)
Transparent mode
NON-Transparent mode
Client
Server
Client
Server
 
Figure1: SIM7000 series TCPIP Structure 
 
SIMCOM   CONFIDENTIAL FILE

---

## Page 6
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
6
 
2 Single Connection 
Command AT+CIPMUX=<n> is used for selecting TCPIP connection mode, when n=0, it is 
single connection; when n=1, it is multi connection. The default configuration is single connection 
mode. For single connection, SIM7000 series supports both transparent mode and non-transparent 
mode.  
 
2.1 Non-transparent mode 
Command AT+CIPMODE=<n> is used for selecting TCPIP application mode, when n=0, it is 
non-transparent mode (normal mode); when n=1, it is transparent mode. The default configuration 
is non-transparent mode. There are three working modes for SIM7000 series under this mode: 
TCP client, UDP client and TCP server. 
 
2.1.1 
How to Establish a TCP Client Connection 
Firstly, before any TCP/UDP related operation is set up, the module should be connected to 
network. User can use the commands "AT+CGATT?" to query the network registration status 
whether the module has been attached to data service. 
Grammar 
Description 
AT+CPIN? 
+CPIN: READY 
 
OK 
whether some password is required or not 
AT+CSQ 
+CSQ: 20,0 
 
OK 
received signal strength 
AT+CGATT? 
+CGATT: 1 
 
OK 
Data Service’s status 
 
Secondly, user should use the command group AT+CSTT, AT+CIICR and AT+CIFSR to start the 
task and activate the wireless connection. Lastly, user can establish TCP connection between 
SIM7000 series and the server by AT command (AT+CIPSTART="TCP","IP Address of server", 
"port number of server"). If the connection is established successfully, response "CONNECT OK" 
will come up from the module. Now user can send data to the server with "AT+CIPSEND". 
"AT+CIPSEND" will return promoting mark ">", user should write data after ">" then issue 
CTRL+Z (0x1a) to send. If sending is successful, it will respond "SEND OK". And if there is data 
coming from the server, the module will receive the data automatically from the serial port. User 
can close the TCP connection with "AT+CIPCLOSE" command. Below is an example of TCP 
connection to remote server. 
SIMCOM   CONFIDENTIAL FILE

---

## Page 7
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
7
Grammar 
Description 
AT+CGATT? 
+CGATT: 1 
OK 
Data Service’s status 
AT+CSTT="CMNET" 
OK 
Start task and set APN. 
The default APN is "CMNET", with no 
username or password. Check with local 
GSM provider to get the APN. 
AT+CIICR 
OK 
Bring up wireless connection 
AT+CIFSR 
10.78.245.128 
Get local IP address 
AT+CIPSTART="TCP","116.228.221.51","8500" 
OK 
Start up the connection 
CONNECT OK 
The TCP connection has been established 
successfully 
AT+CIPSEND 
> hello TCP serve 
Send data to remote server, CTRL+Z 
(0x1a) to send. User should write data 
only after the promoting mark ">", and 
then use CTRL+Z to send. User can use 
command "AT+CIPSPRT" to set whether 
echo 
promote 
">" 
after 
issuing 
"AT+CIPSEND". 
SEND OK 
Remote server receives data. For TCP, 
"SEND OK" means data has been sent 
out and received successfully by the 
remote 
server, 
due 
to 
the 
TCP 
connection-oriented protocol. 
hello SIM7000 
Received data from remote server 
CLOSED 
Remote server closed the connection 
 
2.1.2 
How to Establish a UDP Client Connection 
 
The process of establishing UDP connection is similar to TCP.  
Grammar 
Description 
AT+CGATT? 
+CGATT: 1 
 
OK 
Data Service’s status 
AT+CSTT="CMNET" 
OK 
Start task and set APN. 
 
SIMCOM   CONFIDENTIAL FILE

---

## Page 8
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
8
AT+CIICR 
OK 
Bring up wireless connection 
AT+CIFSR 
10.78.245.128 
Get local IP address 
AT+CIPSTART="UDP","116.228.221.51","9600" 
OK 
Start up "UDP" the connection 
CONNECT OK 
The UDP connection has been established 
successfully 
AT+CIPSEND 
> SIM7000 UDP test 
Send data to remote server, CTRL+Z 
(0x1a) to send. 
SEND OK 
Data has been sent out from the serial 
port, but it is unknown if the data reaches 
the UDP server. For UDP, “SEND OK” 
just means data has been sent out from the 
serial port of module, not meaning data 
reaching the server, due to the UDP 
simpler message-based connectionless 
protocol. 
UDP test 
Receive data from remote server 
AT+CIPCLOSE 
Close the UDP connection 
CLOSED OK 
Connection is closed 
 
2.1.3 
How to Establish a TCP Server Connection 
 
In single connection mode, when configured as TCP server, SIM7000 series allows one client to 
connect in. User should use the command “AT+CIPSERVER=1,"<port>" to start the server 
function and set listening port. If it is successful, response “SERVER OK” will be returned, and 
now the server starts to listen to the TCP port. And then, user should use command "AT+CIFSR" 
to get local IP address, which is the server IP address.  
 
If the client connects to the server successfully, the IP address of remote client will be displayed at 
server side. And the server can receive TCP data from remote side. Also user can use command 
AT+CIPSEND to send data to remote client. User can use "AT+CIPSERVER=0" to close the 
listening status. Also, user can use AT+CIPCLOSE to close the TCP connection. 
Grammar 
Description 
AT+CGATT? 
+CGATT: 1 
 
OK 
Data Service’s status 
AT+CIPSERVER=1,1234 
OK 
Start the TCP server, listening port:1234 
SIMCOM   CONFIDENTIAL FILE

---

## Page 9
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
9
SERVER OK 
TCP server is established successfully 
AT+CIFSR 
10.78.33.227 
Get local IP address 
AT+CIPSTATUS 
OK 
STATE: SERVER LISTENING 
Query current status  
 
TCP server : listening 
REMOTE IP: 10.78.103.220 
Remote client 10.78.103.220 connected in 
hello server 
Receive data from remote client 
AT+CIPSEND 
> hello client 
Send data to remote client 
SEND OK 
Remote client receives data 
AT+CIPSERVER=0 
OK 
Just close the listening status, the current 
connection is still active. 
SERVER CLOSE 
TCP server is closed 
AT+CIPCLOSE 
CLOSE OK 
Close TCP connection 
 
2.1.4 
UDP Extended Mode 
In UDP extended mode, SIM7000 series can receive UDP data from any IP address and port, 
meanwhile it can send UDP data to any IP address and port.  
Grammar 
Description 
AT+CGATT? 
+CGATT: 1 
 
OK 
Data Service’s status 
AT+CSTT="CMNET" 
OK 
Start task and set APN. 
AT+CIICR 
OK 
Bring up wireless connection 
AT+CIFSR 
10.78.245.128 
Get local IP address 
AT+CLPORT="UDP",8888 
OK 
Set local UDP port 
AT+CIPSRIP=1 
OK 
Display IP address and Port of sender 
AT+CIPHEAD=1 
OK 
Add IP head in receiving data 
AT+CIPUDPMODE=1 
OK 
Enable the UDP Extended Mode 
AT+CIPSTART="UDP","116.228.221.51","9600" 
OK 
Start up UDP connection to remote server 
SIMCOM   CONFIDENTIAL FILE

---

## Page 10
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
10
CONNECT OK 
UDP connection has been established 
successfully. 
AT+CIPUDPMODE? 
+CIPUDPMODE: 1,"116.228.221.51",9600 
 
OK 
Check UDP mode’s status 
RECV FROM: 116.228.221.51:9600 
 
+IPD,5:test1 
Receiving data from 116.228.221.51:9600 
RECV FROM: 116.228.221.51:1234 
 
+IPD,5:test2 
Receiving data from 116.228.221.51: 
1234 
RECV FROM: 10.78.103.220: 5678 
 
+IPD,5:test3 
Receiving data from 10.78.103.220: 5678 
AT+CIPSEND 
> Hello 9600 
SEND OK 
Send data to 116.228.221.51:9600 
AT+CIPUDPMODE=2,"211.136.131.65",4500 
OK 
Re-set UDP address to be sent data to. 
AT+CIPUDPMODE? 
+CIPUDPMODE: 1,"211.136.131.65",4500 
 
OK 
The destination UDP address has been  
Updated, and UDP extended mode is  
still on. 
AT+CIPSEND 
> Hello 4500 
SEND OK 
Send data to 211.136.131.65:4500 
 
2.2 Transparent Mode 
2.2.1 
What is Transparent Mode 
SIM7000 series supports transparent mode which provides a special data mode for data receiving 
and sending by TCP/IP application task. Once the connection is established under transparent 
mode, the module will be in data mode. All received data from serial port will be treated as data 
packet to be transferred later, similarly all data received from remote side will be sent to serial port 
directly. In transparent mode, all AT commands are not available. Methods are provided to switch 
back and forth between data mode and command mode. Once it is switched to command mode, all 
AT commands can be used again.  
 
Note: The flow control is default off. It is better to open the hardware flow control for using transparent mode, 
by setting AT+IFC=2,2. 
 
2.2.2 
How to Configure Transparent Mode 
To enable transparent mode, the command AT+CIPMODE should be set to 1. In transparent mode, 
the command AT+CIPCCFG is used for configuring transfer mode, which has 7 parameters 
SIMCOM   CONFIDENTIAL FILE

---

## Page 11
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
11 
NmRetry, WaitTm, SendSz, Esc, Rxmode, RxSize, Rxtimer. 
 
NmRetry: Number of retries to be made for an IP packet. 
 
WaitTm: Number of 200ms intervals to wait for serial input before sending the packet 
 
SendSz: Size in bytes of data block to be received from serial port before sending. 
 
Esc: Whether turn on the escape sequence, default is TRUE. 
 
Rxmode: Whether to set time interval during output data from serial port. 
 
RxSize: Output data length for each time, default value is 1460. 
 
Rxtimer: Time interval (ms) to wait for serial port to output data again. Default value: 
50ms 
 
2.2.3 
How to Establish Connection under Transparent Mode 
The transparent mode is only supported under single connection. In transparent mode, SIM7000 
series can work as three modes too: TCP client, UDP client and TCP server. Once the connection 
is established, CONNECT will be returned in the serial port and the module will be in data mode. 
At the same time, DCD pin will be active low. Below is an example of TCP client connection. 
Grammar 
Description 
AT+CGATT? 
+CGATT: 1 
 
OK 
Data Service’s status 
AT+CIPMODE=1 
OK 
Enable transparent mode 
AT+CSTT="CMNET" 
OK 
Start task and set APN. 
AT+CIICR 
OK 
Bring up wireless connection 
AT+CIFSR 
10.78.245.128 
Get local IP address 
AT+CIPSTART="TCP","116.228.221.51","8500" 
OK 
Start up TCP connection to remote server 
CONNECT 
Connected successfully, enter into data 
mode 
...... 
Input data to serial port, no echo, so can’t 
see input data 
OK 
Quit data mode by pulling DTR or using 
"+++" 
ATO 
CONNECT 
Return to data mode 
SIM7000 channel test 
Data received from remote server 
CLOSED 
Closed by remote server, quit data mode 
 
SIMCOM   CONFIDENTIAL FILE

---

## Page 12
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
12
2.2.4 
How to Switch Between Data Mode and Command Mode 
To switch from data mode to command mode, following methods are available:  
(1) The escape sequence can be used if the fourth parameter of AT+CIPCCFG is TRUE. The 
default escape sequence is +++, and to use this sequence, there should be 1000ms idle period 
before this sequence and 1000ms idle period after this sequence. Besides, the interval between 
each + should not exceed 1000ms, otherwise it will be treated as TCP/IP data. 
(2) DTR line of serial port can also be used. To use this method, AT&D1 should be set firstly. 
Pull DTR line to ground for at least 1 second and then pull up, the module will be switched 
from data mode to command mode and OK will be returned indicating the module is in 
command mode.  
(3) For TCP client connection, if the remote server closes the connection, the module will be 
switched back to command mode automatically.  
(4) For TCP server connection, if the remote client closes the connection, the module will be 
switched back to command mode automatically.  
(5) If the module is deactivated from PDP context (+PDP DEACT) during data transferring, 
module will be switched back to command mode automatically. 
ATO command can be used to switch the module from command mode to data mode if the 
connection is active, and CONNECT will be returned again. 
 
2.2.5 
How to handle incoming call and short message in data mode 
RI pin will give a 120ms low pulse when a short message is received.  
 
To handle the SMS, the module need to enter command mode first (using DTR or +++), and then 
the module will give the normal unsolicited responses as following: 
Grammar 
Description 
+CMTI: "SM", 10 
New short message 
And then it is able to read the short message. 
 
2.3 Fix Local Port of TCP/UDP Client 
Normally, if client SIM7000 series establishes TCP/UDP connection to remote server, the 
TCP/UDP connection will be dynamically allocated a local port when AT+CLPORT is set to 0. If 
AT+CLPORT is set to a nonzero value, the local port will be fixed at this value. The default 
configuration of this command is 0. Be aware that this command will be effective only in single 
connection mode and when the module is as a client.  
SIMCOM   CONFIDENTIAL FILE

---

## Page 13
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
13
 
3 Multi Connection 
To enable multi connection mode, the command AT+CIPMUX must be set to 1. Be aware that in 
the multi connection mode, SIM7000 series only supports non-transparent mode. Due to this 
matter, the command AT+CIPMODE is invalid under multi connection mode.  
 
In multi connection mode, SIM7000 series can work as a TCP/UDP client or a TCP server.  
As a client, it can establish 8 connections to remote server in total, both TCP and UDP.  
 
As a TCP server, it allows remote clients to connect in; at the same time, it can establish 
TCP/UDP connections to upper remote servers. Total 7 available connections are supported, with 
the server itself occupying one connection. 
 
3.1 As a Client 
Being a client, SIM7000 series can establish both TCP and UDP connection to remote server. 
Total 8 connections are supported. The command "AT+CIPSTART=<n>,<mode>,<IP 
Address>,<port>" is needed. When the connection is established successfully, "<n>, CONNECT 
OK" will be returned. And then user can use command AT+CIPSNED=<n> to send data to the 
connection <n>. User should write data after the promoting mark ">" and use CTRL+Z (0x1a) to 
send. If sending is successfully, "<n>, SEND OK" will be returned. User can use command 
AT+CIPCLOSE=<n> to close one specific connection with number <n>. Also user can send 
AT+CIPSHUT to close all connections. 
Grammar 
Description 
AT+CGATT? 
+CGATT: 1 
 
OK 
Data Service’s status 
AT+CIPMUX=1 
OK 
Enable multi connection 
AT+CSTT="CMNET" 
OK 
Start task and set APN. 
AT+CIICR 
OK 
Bring up wireless connection 
AT+CIFSR 
10.78.245.128 
Get local IP address 
AT+CIPSTART=0,"TCP","116.228.221.51","8500" 
OK 
 
0, CONNECT OK 
Establish 
a 
TCP 
connection, 
connection number 0 
AT+CIPSTART=1,"UDP","116.228.221.51","9600" 
OK 
Establish a UDP connection, 
connection number 1 
SIMCOM   CONFIDENTIAL FILE

---

## Page 14
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
14
 
1, CONNECT OK 
AT+CIPSEND=0 
> TCP test 
 
0, SEND OK 
Send data to connection 0 
AT+CIPSEND=1 
> UDP test 
 
1, SEND OK 
Send data to connection 1 
+RECEIVE,0,17: 
SIM7000 TCP test 
Received data from connection 0, 
data length 17 
+RECEIVE,1,17: 
SIM7000 UDP test 
Received data from connection 1, 
data length 17 
0, CLOSED 
Connection 0 is closed by remote 
server 
AT+CIPSTATUS 
OK 
 
STATE: IP PROCESSING 
 
C: 0,0,"TCP","116.228.221.51","8500"," CLOSED " 
C: 1,0,"UDP","116.228.221.51","9600"," CONNECTED " 
C: 2,,"","","","INITIAL" 
C: 3,,"","","","INITIAL" 
C: 4,,"","","","INITIAL" 
C: 5,,"","","","INITIAL" 
C: 6,,"","","","INITIAL" 
C: 7,,"","","","INITIAL" 
Query the current connection status 
 
3.2 As a TCP Server 
Being a TCP server, SIM7000 series allows remote clients to connect in; meanwhile, it can 
establish TCP/UDP connections to remote servers as well.  
 
Before launching the server function, command group "AT+CSTT, AT+CIICR, AT+CIFSR" 
should be executed to activate the PDP context and get local IP address. Then user can send 
command "AT+CIPSERVER=1, <port>" to start the server function. If it is successfully, response 
“SERVER OK” will be returned, and now the server starts to listen to the TCP port.  
 
If the clients connect to the server successfully, the IP addresses of remote clients together with 
connection numbers <n> will be displayed at server side. Then the server can receive TCP data 
from remote clients. Also user can use command AT+CIPSEND=<n> to send data to remote 
client <n>. Simultaneously, user can connect the server SIM7000 series to remote servers by 
SIMCOM   CONFIDENTIAL FILE

---

## Page 15
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
15
TCP/UDP using command "AT+CIPSTART=<n>,<mode>,<IP Address>,<port>". Command 
"AT+CIPSERVER=0" can be used to close the listening status. User can use the command 
AT+CIPCLOSE=<n> to close one specific connection with number <n> and use AT+CIPSHUT 
to close all connections. 
Grammar 
Description 
AT+CGATT? 
+CGATT: 1 
 
OK 
Data Service’s status 
AT+CIPMUX=1 
OK 
 
AT+CSTT="CMNET" 
OK 
 
AT+CIICR 
OK 
Bring up wireless connection 
AT+CIFSR 
10.76.40.73 
Get local IP address 
AT+CIPSERVER=1,8888 
OK 
 
SERVER OK 
Start server;listeninig port:8888 
0, REMOTE IP: 10.76.40.73 
Remote client connect in, connection 
number 0 allocated 
+RECEIVE,0,39: 
SIM7000 multi connection TCP server test 
Received data from remote client, 
data length 39 
AT+CIPSEND=0 
> hello client 
0, SEND OK 
Send data to remote client 
AT+CIPSTART=1,"TCP","116.228.221.51","8500" 
OK 
 
1, CONNECT OK 
Establish TCP connection to remote 
server 
AT+CIPSTART=2,"UDP","116.228.221.51","9600" 
OK 
 
2, CONNECT OK 
Establish UDP connection to remote 
server  
AT+CIPSEND=1 
> data from connection 1 
 
1, SEND OK 
Send TCP data to remote server 
 
+RECEIVE,1,20: 
data to connection 1 
Received TCP data from remote 
serve 
SIMCOM   CONFIDENTIAL FILE

---

## Page 16
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
16
AT+CIPCLOSE=2 
2, CLOSE OK 
Close the UDP connection with 
remote server 
AT+CIPSTATUS 
OK 
 
STATE: IP PROCESSING 
 
S: 0,0,"8888","LISTENING" 
 
C: 0,0,"TCP","10.76.40.73","2020","CONNECTED" 
C: 1,0,"TCP","116.228.221.51","8500","CONNECTED" 
C: 2,0,"UDP","116.228.221.51","9600","CLOSED" 
C: 3,,"","","","INITIAL" 
C: 4,,"","","","INITIAL" 
C: 5,,"","","","INITIAL" 
C: 6,,"","","","INITIAL" 
C: 7,,"","","","INITIAL" 
Query current connection status  
 
 
 
TCP server is in the process of 
listening, occupying one connection  
 
A client is accepted  
TCP connection is connected 
UDP connction is closed 
AT+CIPSERVER=0 
OK 
 
SERVER CLOSE 
Close server listening 
AT+CIPSHUT 
SHUT OK 
Deactivate the PDP context &close 
all connections 
 
SIMCOM   CONFIDENTIAL FILE

---

## Page 17
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
17
 
4 Two PDP Context 
SIM7000 series supports the use of two different APN, that is , two different PDP context for data 
connection. This mode must be used in multi connection. Customer activated PDP in first Context , 
do some connection. When need second Context to data connection, use "at+cipsgtxt=1" to switch, 
after this, active the second Context and do data connection. 
 
Grammar 
Description 
AT+CGATT? 
+CGATT: 1 
 
OK 
Data Service’s status 
AT+CIPMUX=1 
OK 
Set multi connection mode 
AT+CSTT="CMNET" 
OK 
Start task and set APN. "CMNET" 
AT+CIICR 
OK 
Bring up wireless connection 
AT+CIFSR 
10.126.186.232 
Get local IP address 
AT+CIPSTART=0,"TCP","116.236.221.75",5555 
OK 
 
0, CONNECT OK 
Establish TCP connection at 0 
channel in first Context 
AT+CIPSGTXT=1 
OK 
Switch to second Context 
AT+CSTT="CMWAP" 
OK 
Start task and set APN. "CMWAP" 
AT+CIICR 
OK 
Bring up wireless connection 
AT+CIFSR 
10.204.70.11 
Get local IP address 
AT+CIPSTART=1,"TCP","116.236.221.75",5555 
OK 
 
1, CONNECT OK 
Establish TCP connection at 1 
channel in second Context 
+RECEIVE,0,15: 
Hello world 000 
Receive two channel’s data as 
normal multi connection 
+RECEIVE,1,15: 
Hello world 111 
 
SIMCOM   CONFIDENTIAL FILE

---

## Page 18
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
18
AT+CIPSEND=0 
> test 0 
0, SEND OK 
Send data at two channel as normal 
multi connection 
AT+CIPSEND=1  
>test 2 
1, SEND OK 
 
AT+CIPCLOSE=0 
0, CLOSE OK 
Close data connection as normal 
multi connection.  
AT+CIPSTATUS 
OK 
 
STATE: IP PROCESSING 
 
C: 0,0,"TCP","116.236.221.75","5555","CLOSED"       
C: 1,1,"TCP","116.236.221.75","5555","CONNECTED"  
C: 2,,"","","","INITIAL" 
C: 3,,"","","","INITIAL" 
C: 4,,"","","","INITIAL" 
C: 5,,"","","","INITIAL" 
C: 6,,"","","","INITIAL" 
C: 7,,"","","","INITIAL" 
Query Connection’s status 
 
 
 
 
0 channel’s connection is closed 
1 
channel’s 
connection 
is 
connected 
AT+CIPSHUT 
SHUT OK 
Shut up second Context, but first 
Context is active. 
AT+CIPSGTXT=0 
OK 
Switch to first Context 
AT+CIPSHUT 
SHUT OK 
Shut up first Context 
 
SIMCOM   CONFIDENTIAL FILE

---

## Page 19
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
19
 
5 DNS Function 
SIM7000 series supports DNS auto parsing, so user can establish TCP/UDP connection to remote 
sever using domain name directly by the command "AT+CIPSTART=<mode>, <domain name>, 
<port>". And then user can send data to remote server by AT+CIPSEND. In multi connection, the 
connection number <n> is needed. 
 
User also can use command AT+CDNSGIP=<domain name > to query the IP address of given 
domain name. 
Grammar 
Description 
AT+CGATT? 
+CGATT: 1 
 
OK 
Query data Service’s status 
AT+CSTT="CMNET" 
OK 
Start up task and set APN 
AT+CIICR 
OK 
Bring up wireless connection 
AT+CIFSR 
10.126.186.232 
Get local IP address 
AT+CDNSGIP=www.baidu.com 
OK 
Query 
IP 
address 
of 
www.baidu.com  
+CDNSGIP: 
1,"www.baidu.com","119.75.218.77","119.75.217.56" 
Parsing succeed, the IP address has 
two results. 
AT+CDNSGIP="abctest" 
OK 
Query "abctest" 
+CDNSGIP: 0,8 
Parsing error. 
AT+CIPSTART="TCP","WWW.SIM.COM",80 
OK 
 
CONNECT OK 
Establish TCP connection. 
AT+CIPSNED 
> DNS test 
SEND OK 
Send data 
 
SIMCOM   CONFIDENTIAL FILE

---

## Page 20
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
20
 
6 Data Sending Related 
SIM7000 series provides three ways to send data: changeable data length sending, fixed data 
length sending and timed sending. SIM7000 series also provides a method to let user know how 
much data is sent out from the module and received by remote server on an active TCP 
connection. 
 
6.1 Fixed Length Sending 
User can send the fixed length of data with "AT+CIPSEND=<LENGTH>", then input data after 
getting promoting mark ">". Data will be sent automatically when the length of the input data 
equals to the value “LENGTH”. User does not need the terminal symbol CTRL+Z (0x1a) in this 
case. For multi connection mode, the command is "AT+CIPSEND=<n>,<LENGTH>". 
 
6.2 Timed Sending 
There is another way to send data automatically. First, set the timer of sending data automatically 
by 
the 
command 
"AT+CIPATS=<mode>,<time>", 
then 
issue 
"AT+CIPSEND" 
("AT+CIPSEND=<n>" for multi connection) and lastly input the data after getting promoting 
mark ">".  Data will be sent automatically when the set timer expires. 
 
6.3 Query Available Data Length to be Sent 
User can use the command "AT+CIPSEND?" to query the current maximum data length available 
to be sent, which is determined by the network. In fact, the maximum data length is variable, 
depending on the actual network. The maximum data length can be up to 1460 bytes. In multi 
connection, the command "AT+CIPSEND?" will tell current available maximum data length for 
all active connections. 
Grammar 
Description 
AT+CIPSEND? 
+CIPSEND: 1460 
 
OK 
Current maximum value 1460 
AT+CIPSEND=1461 
ERROR 
The fixed length exceeds maximum 
value 
AT+CIPSEND 
>123….999 
ERROR 
The input data exceeds maximum 
value 
 
6.4 Select Data Transmitting Mode 
SIM7000 series supports quick sending mode. When command AT+CIPQSEND=0, it is in normal 
sending mode. In this mode, after user sends data by AT+CIPSEND, if the server receives TCP 
data, it will give ACK message to module, and the module will respond SEND OK. When 
command AT+CIPQSEND=1, it is in quick sending mode. When the data is input to the serial 
port of module by AT+CIPSEND, it will respond DATA ACCEPT, while not respond SEND OK. 
In such case, user can continuously use AT+CIPSEND to send data to the server. 
SIMCOM   CONFIDENTIAL FILE

---

## Page 21
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
21
Single connection: 
Grammar 
Description 
AT+CIPQSEND=1  
OK 
Enable quick sending mode 
AT+CIPSEND 
> hello 
 
DATA ACCEPT:5 
 
 
 
Data has been sent, not sure 
whether to be accepted 
 
Multi connection: 
Grammar 
Description 
AT+CIPSTART=0,"TCP","116.236.221.75",5107 
OK 
 
0, CONNECT OK 
Establish TCP connection 
AT+CIPQSEND=1  
OK 
Enable quick sending mode 
AT+CIPSEND=0 
> 1234567890 
 
DATA ACCEPT:0,10 
 
 
 
Data has been sent, not sure 
whether to be accepted  
 
6.5 Query Data Transmitting Amount 
The command AT+CIPACK is used to query previous connection data transmitting state. In single 
connection, the execution command AT+CIPACK will return +CIPACK: <txlen>,<acklen>, 
<nacklen>. The first parameter <txlen> is the data amount which has been sent; the second 
parameter <acklen> is the data amount confirmed successfully by the server; and the third 
parameter <nacklen> is the data amount without confirmed by the server. As long as the 
connection is still active, user can know how much TCP data user sent to server and how much is 
received successfully by the server in total. By this means, user can get the total data transmitting 
amount. 
Grammar 
Description 
AT+CIPQSEND=1  
OK 
Enable quick sending mode 
AT+CIPSTART="TCP","116.236.221.75",5107 
OK 
 
CONNECT OK 
Establish TCP connection 
AT+CIPSTATUS 
OK 
Query connection’s status 
SIMCOM   CONFIDENTIAL FILE

---

## Page 22
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
22
 
STATE: CONNECT OK 
AT+CIPSEND  
> 012345678912 
DATA ACCEPT:12 
 
AT+CIPACK 
+CIPACK: 12,12,0 
 
OK 
Query status of data send 
12 be Send , 12 be confirmed 
 
For multi connection, the correct command type is AT+CIPACK=<n>. <n> is the connection 
number. 
Grammar 
Description 
AT+CIPSTATUS 
OK 
 
STATE: IP PROCESSING 
 
C: 0,,"","","","INITIAL" 
C: 1,0,"TCP","116.228.221.51","8500","CONNECTED" 
C: 2,0,"UDP","116.228.221.51","9600","CONNECTED" 
C: 3,,"","","","INITIAL" 
C: 4,,"","","","INITIAL" 
C: 5,,"","","","INITIAL" 
C: 6,,"","","","INITIAL" 
C: 7,,"","","","INITIAL" 
Query connection’s status 
AT+CIPQSEND=1  
OK 
Enable quick sending mode 
AT+CIPSEND=1 
> TCP 
DATA ACCEPT:1,3 
Send data at 1 channel 
AT+CIPACK=1 
+CIPACK: 3, 3, 0 
 
OK 
Query status about 1 channel 
3 be send, 3 be confirm 
AT+CIPSEND=1 
> TCP again 
DATA ACCEPT:1,9 
Send data at 1 channel 
AT+CIPACK=1 
+CIPACK: 12, 12, 0 
 
OK 
 
SIMCOM   CONFIDENTIAL FILE

---

## Page 23
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
23
AT+CIPSEND=2 
> UDP 
DATA ACCEPT:2,3 
Send data at 2 channel 
AT+CIPACK=2 
+CIPACK: 3, 0, 3 
 
OK 
Query status about 2 channel 
3 be send, 3 be unconfirmed.  
 
SIMCOM   CONFIDENTIAL FILE

---

## Page 24
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
24
 
7 Data Receiving Related 
7.1 Receive Data Automatically 
The module will receive data automatically if there is data coming from remote server. Several 
commands can help to get the information header. 
 
"AT+CIPHEAD=1" helps to add IP header in the format "+IPD (data length): payload". 
 
"AT+CIPSRIP=1" helps to show the data source information in the format "RECV 
FROM:  <IP ADDRESS>:<PORT >". 
 
"AT+CIPSHOWTP" helps to show the protocol (TCP/UDP) in the IP header. It takes 
effect only if "CIPHEAD" is enabled. 
With these information, user can easily know the source of the data frame, the amount of the 
payload and the protocol. It can also help user to distinguish the received data from AT command 
responses. 
 
7.2 Receive Data Manually 
The module provides user a way to get data from the network manually instead of pushing data to 
the TE automatically.  
 
"AT+CIPRXGET=1" enables getting data from network manually, which should be set before 
connection. If it is set to 0 (default value if not set), data will be pushed to TE directly. 
 
"AT+CIPRXGET=<mode>[,<len>]" helps to get data with a given length. If it is multi IP 
connection, the connection ID should be given. "AT+CIPRXGET=<mode>,<id>[,<len>]" 
Grammar 
Description 
AT+CIPRXGET=1 
OK 
Enables getting data from network 
manually 
AT+CIPSTART="TCP","116.228.221.51",5555 
OK 
 
CONNECT OK 
 
+CIPRXGET: 1 
Data incoming from server 
AT+CIPRXGET=2,1460 
+CIPRXGET: 2,11,0 
HELLO WORLD 
 
OK 
The mode is set to 2, the output 
data will be in normal mode, not 
exceeding 1460 bytes at a time. 
+CIPRXGET: 1 
Data incoming from server 
AT+CIPRXGET=3,730 
+CIPRXGET: 3,11,0  
48454C4C4F20574F524C44  
OK 
The mode is set to 3, user can get 
data in HEX mode with the length 
not exceeding 730 bytes at a time. 
 
SIMCOM   CONFIDENTIAL FILE

---

## Page 25
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
25
8 APPTCP States Exchange Related 
For single connection, there are 10 states in total; for multi connection, there are 7 states. After 
some AT commands are executed, the corresponding state will be changed. User can get a general 
idea from the following diagrams:  
0. IP INITIAL
1. IP START
2. IP CONFIG
3. IP GPRSACT
4. IP STATUS
5. TCP/UDP 
CONNECTING/
SERVER LISTENING
6. CONNECT OK
7.  TCP/UDP 
CLOSING
8. TCP/UDP CLOSED
9. PDP DEACT
AT+CIICR
AT+CGATT
AT+CIPCLOSE
AT+CIPSTART
AT+CIFSR
AT+CSTT
AT+CIPSHUT
Figure2: APPTCP States Diagram for single connection 
 
 
SIMCOM   CONFIDENTIAL FILE

---

## Page 26
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
26
0. IP INITIAL
1. IP START
2. IP CONFIG
3. IP GPRSACT
4. IP STATUS
5. IP PROCESSING
9. PDP DEACT
AT+CIICR
AT+CIPSTART
AT+CIFSR
AT+CSTT
AT+CIPSHUT
AT+CGATT=0
AT+CGATT=0
AT+CIPCLOSE
 
Figure3: APPTCP States Diagram for multi connection 
 
 
IP INTIAL:  Initial status 
 
IP START:  Start a TCP/UDP task 
 
IP CONFIG:  Configure PDP context 
 
IP GPRSACT:  Context active already 
 
IP STATUS:  Get local IP address 
 
TCP/UDP CONNECTING:  Connecting to server now 
 
SERVER LISTENING:  Listening to server port now 
 
IP PROCESSING:  Processing the existing connection now 
 
CONNECT OK:  Connection to the server is successful 
 
TCP/UDP CLOSING:  Closing connection now 
 
TCP/UDP CLOSED:  Connection closed (local IP/PDP context still there) 
 
PDP DEACT:  Context deactivated 
 
SIMCOM   CONFIDENTIAL FILE

---

## Page 27
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
27
 
9 Connection Closing Related 
User can use the command AT+CIPCLOSE=<mode> to close the TCP or UDP connection. If 
<mode> is 0, it is slow closing, if <mode> is 1, it is quick closing. In slow closing, the module 
will interactive with the server when it closes the TCP connection. Thus, the time of returning 
"CLOSE OK" will be a bit long. This method is suitable for steady network. In quick closing, the 
module will disconnect the connection compulsorily and return “CLOSE OK” immediately, 
without interaction with the server.  
 
The default setting is slow closing, so the <mode> 0 can be omitted. And in multi connection, the 
connection number <n> should be added in front of <mode>.  
 
Be noted that command AT+CIPCLOSE only closes current TCP/UDP connection, but PDP 
context is still active. Also user can close connection by AT+CIPSHUT, with current PDP context 
being deactivated. 
SIMCOM   CONFIDENTIAL FILE

---

## Page 28
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
28
 
10 Connection Activity Checking Related 
User can use the command AT+CIPSTATUS to query current connection status.  
 
In transparent mode, DCD pin can be used for this purpose. If TCP/UDP connection exists, the 
DCD pin will be active (low). At any time if the connection is dropped, DCD pin will go inactive 
(high). 
SIMCOM   CONFIDENTIAL FILE

---

## Page 29
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
29
 
11 Power Consumption with Existing Connection 
The module can enter sleep mode to save power consumption with existing connection, in which 
the current consumption is reduced to only several mA. The sleep mode function is enabled by 
setting "AT+CSCLK=1". With this setting, if the DTR maintains HIGH and there is no 
interruption on either H/W of S/W or event over-the-air, module will go into sleep. In the sleep 
mode, the serial port stops working, which means no AT command can be issued any more. 
During the sleep mode with existing connection, the incoming data from the remote end can wake 
up the module. Any event over-the-air, such as incoming call or SMS etc, will wake up the 
module too. But At command is not be respond now, If need input AT command, must pull low 
DTR 50ms or more, after this, the serial port can receive data again. More detail please refer to 
HD document. 
SIMCOM   CONFIDENTIAL FILE

---

## Page 30
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
30
 
12 Error Handling 
If an error occurs in TCP/UDP connection, for example TCP sending data error or TCP 
connection dropping, it is suggested to close the connection by command AT+CIPCLOSE and 
then restart the connection by AT+CIPSTART. If the error still occurs, please use AT+CIPSHUT 
to shut off the PDP context and then restart the connection. If these two methods above can’t help 
to solve it, SIMCom recommends user to reset the module. 
SIMCOM   CONFIDENTIAL FILE

---

## Page 31
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
31
 
Appendix 
A  Related Documents 
SN 
Document name 
Remark 
[1] 
SIM7000 Series_AT Command Manual 
 
 
B  Terms and Abbreviations 
Abbreviation  Description 
TCP 
Transmission Control Protocol 
UDP 
User Datagram Protocol 
APN 
Access Point Name 
PDP 
Packet Data Protocol 
DNS 
Domain Name System 
SIMCOM   CONFIDENTIAL FILE

---

## Page 32
                                                        Smart Machine Smart Decision 
SIM7000 Series_TCPIP_Application Note_V1.01                                    2017-10-24 
32
Contact us: 
Shanghai SIMCom Wireless Solutions Co.,Ltd. 
Address: Building A, SIM Technology Building, No. 633, Jinzhong Road, Shanghai, P. R. China 
200335 
Tel: +86 21 3252 3300 
Fax: +86 21 3252 3020 
URL: www.simcomm2m.com 
SIMCOM   CONFIDENTIAL FILE

---
