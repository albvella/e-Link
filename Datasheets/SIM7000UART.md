SIM 7000 Series_UART
_Application Note
SIMComWirelessSolutionsLimited
BuildingB,SIMTechnologyBuilding,No. 633 ,JinzhongRoad
ChangningDistrict,ShanghaiP.R.China
Tel: 86 - 21 - 31575100
support@simcom.com
http://www.simcom.com
LPWAModule

DocumentTitle: SIM 7000 Series_UART_ApplicationNote
Version: 1. 01

Date:^2020 -^07 -^29
Status: Released

GENERALNOTES
SIMCOM OFFERS THIS INFORMATION AS A SERVICE TO ITS CUSTOMERS, TO SUPPORT
APPLICATIONANDENGINEERINGEFFORTSTHATUSETHEPRODUCTSDESIGNEDBYSIMCOM.
THEINFORMATIONPROVIDEDISBASEDUPONREQUIREMENTSSPECIFICALLYPROVIDEDTO
SIMCOMBYTHECUSTOMERS.SIMCOMHASNOTUNDERTAKENANYINDEPENDENTSEARCH
FORADDITIONALRELEVANTINFORMATION,INCLUDINGANYINFORMATIONTHATMAYBEINTHE
CUSTOMER’S POSSESSION. FURTHERMORE, SYSTEM VALIDATION OF THIS PRODUCT
DESIGNEDBYSIMCOMWITHINALARGERELECTRONICSYSTEMREMAINSTHERESPONSIBILITY
OF THE CUSTOMER OR THE CUSTOMER’S SYSTEM INTEGRATOR. ALL SPECIFICATIONS
SUPPLIEDHEREINARESUBJECTTOCHANGE.
COPYRIGHT
THISDOCUMENTCONTAINSPROPRIETARYTECHNICALINFORMATIONWHICHISTHEPROPERTY
OFSIMCOMWIRELESSSOLUTIONSLIMITEDCOPYING,TOOTHERSANDUSINGTHISDOCUMENT,
AREFORBIDDENWITHOUTEXPRESSAUTHORITYBYSIMCOM.OFFENDERSARELIABLETOTHE
PAYMENTOFINDEMNIFICATIONS.ALLRIGHTSRESERVED BYSIMCOMINTHEPROPRIETARY
TECHNICALINFORMATION ，INCLUDINGBUTNOTLIMITEDTOREGISTRATIONGRANTINGOFA
PATENT,AUTILITYMODELORDESIGN.ALLSPECIFICATIONSUPPLIEDHEREINARESUBJECTTO
CHANGEWITHOUTNOTICEATANYTIME.
SIMComWirelessSolutionsLimited
BuildingB,SIMTechnologyBuilding,No. 633 JinzhongRoad,ChangningDistrict,ShanghaiP.R.China
Tel:+ 862131575100
Email:simcom@simcom.com

Formoreinformation,pleasevisit:
https://www.simcom.com/download/list- 863 - en.html

Fortechnicalsupport,ortoreportdocumentationerrors,pleasevisit:
https://www.simcom.com/ask/oremailto:support@simcom.com

Copyright© 2020 SIMComWirelessSolutionsLimitedAllRightsReserved.

AboutDocument.................................................................................................................................................
VersionHistory.........................................................................................................................................................
Version Date Owner Whatisnew
V 1. 00 2017. 12. 05 Hongjun.Tu FirstRelease
V 1. 01 2020. 07. 28 Wenjie.Lai All

Scope........................................................................................................................................................................
Thisdocumentappliestothefollowingproducts

Name Type Size(mm) Comments

SIM 7000 E/C/A/G Cat-M 1 (/NB 1 /EGPRS) 24 * 24
SIM 7000 E-N
SIM 7000 C-N NB^124 *^24

Contents................................................................................................................................................................
Contents
AboutDocument.................................................................................................................................................
VersionHistory.........................................................................................................................................................
Scope........................................................................................................................................................................
Contents................................................................................................................................................................
1 Introduction...................................................................................................................................................
1 1 Purposeofthedocument...........................................................................................................................
1 2 Relateddocuments.....................................................................................................................................
1 3 Conventionsandabbreviations................................................................................................................
2 UARTIntroduction......................................................................................................................................
3 Connection....................................................................................................................................................
3 1 HardwareInterface.....................................................................................................................................
3 2 ConnecttoHost...........................................................................................................................................
4 Synchronizebaudrate.............................................................................................................................
5 FlowControl...............................................................................................................................................
5 1 Hardwareflowcontrol(RTS/CTS).........................................................................................................
6 ControlSignals..........................................................................................................................................
6 1 RTS.............................................................................................................................................................
6 2 CTS.............................................................................................................................................................
6 3 DCD.............................................................................................................................................................
6 4 DTR.............................................................................................................................................................
6 5 RI.................................................................................................................................................................
1 Introduction...................................................................................................................................................
1 1 Purposeofthedocument...........................................................................................................................
BasedonmoduleATcommandmanual,thisdocumentwillintroduceUARTapplicationprocess.

Developerscouldunderstandanddevelopapplicationquicklyandefficientlybasedonthisdocument.

1 2 Relateddocuments.....................................................................................................................................
[ 1 ]SIM 7000 Series_ATCommandManual

1 3 Conventionsandabbreviations................................................................................................................
Abbreviation Description

UART UniversalAsynchronousReceiver/Transmitter
URC UnsolicitedResultCode

DTE DataTerminalEquipment
DCE DataCommunicationEquipment
SMS ShortMessageService

2 UARTIntroduction......................................................................................................................................
ThisdocumentdescribestheUARTinterfaceofSIMComSIM 7000 module.TheUARTporthasseveral
features:
 SupportHigh-speedUART,thebaudrateisupto 4 Mbps,thecommunicationbaudrates
include: 0 , 300 , 600 , 1200 , 2400 , 4800 , 9600 , 19200 , 38400 , 57600 , 115200 , 230400 , 921600 , 2000000 , 29
00000 , 3000000 , 3200000 , 3686400 , 4000000 bps.Therate 0 bpsmarkautobaudrate.
 SupportHardwareflowcontrol.
 Support auto baud rate, but auto baud rate only supported 9600 bps, 19200 bps, 38400 bps,
57600 bpsand 115200 bps.

3 Connection....................................................................................................................................................
SIM 7000 moduleisdesignedasaDCE(DataCommunicationEquipment).ItprovidesaUARTinterface
whichisusedfordatatransmissionandsendingATcommands.

Thedefaultbaudrateisautobaudrate,datasizeis 8 bits,stopbitsis 1 bit,andparityisnone.

3 1 HardwareInterface.....................................................................................................................................
Table 1 :Pindescription

Pintype Pinname PinNumber I/O Activevoltage DefaultStatus

UART
UART_RXD 10 I Low Pull-Down
UART_TXD 9 O Low Pull-Up
UART_RTS 8 I Low Pull-Down
UART_CTS 7 O Low Pull-Down
UART_DTR 3 I Low Pull-Up
UART_DCD 5 O Low Pull-Up
UART_RI 4 O Low Pull-Up
Fordifferentdevices,thenameofRTSPINmaybeconfusedasCTSPIN,andthenameofCTSPIN
maybeconfusedasRTSPIN,theI/OdirectionofSIM 7000 module’sCTSPINisOUT,andRTSPINis
IN,userscanclearthisconfusionbytheI/Odirection.

Table 2 :Logiclevel

Parameter Min Max Unit

Logiclowinput - 0. 3 0. 65 V

Logichighinput 1. 17 1. 8 V

Logiclowoutput - 0. 3 0. 45 V

Logichighoutput 1. 35 1. 8 V

NOTE

3 2 ConnecttoHost...........................................................................................................................................
Whenthemoduleisusedas 2 - lineUARTfordatatransmission,onlyRXDandTXDsignalPINsareused,
thefollowingfigureshowstheconnectionbetweenSIM 7000 moduleandDTE(customer’sCPU).

Figure 1 : 2 - lineUART
Whenmoduleisusedas 7 - lineUARTfordatatransmission,allthesignalPINsshouldbeconnected,
includingTXD,RXD,RTS,CTS,DTR,DCDandRI,andthecorrespondingPINsshouldbeconfiguredas
UARTfunction.ThefollowingfigureshowstheconnectionbetweenSIM 7000 moduleandDTE(customer’s
CPU).

Figure 2 :UARTfullmodem
TheSIM 7000 UARTis 1. 8 Vvoltageinterface.Ifuser’sUARTapplicationcircuitis 3. 3 Vvoltageinterface,

thelevelshifter circuitsshouldbeusedfor voltagematching.TheTXB 0108 RGYRprovided by Texas
Instrumentsisrecommended.Thefollowingfigureshowsthevoltagematchingreferencedesign.

Figure 3 :Referencecircuitoflevelshift
4 Synchronizebaudrate.............................................................................................................................
SIM 7000 supportsautobaudrate,buttherateonlysupportedon 9600 , 19200 , 38400 , 57600 , 115200 .If
usersneedtochangetootherbaudrate,itneedstoswitchasATcommandAT+IPR.

AutobaudratingallowsSIM 7000 moduletoautomaticallydetectthebaudratebasedonthehostdevice.
HostdevicemustsynchronizethebaudratewithSIM 7000 modulefirstbeforecommunication.

Hostmustsend“AT”stringtosynchronizethemodule,ifmodulematchesthebaudrateitwillrespondwith
response:“OK”,ifnoresponseisreported,hostmustsendthesynchronizestringagainuntiltheresponse
isreceived.

Thefunctionissupportedin“AT+IPR”.When“AT+IPR”issetto 0 ，autobaudisactivated.IfTAsends
“AT+IPR= 0 ”commandtothemodem,thenmodulewillbesavedasautobaudmode.

5 FlowControl...............................................................................................................................................
Flowcontrolisveryimportantduringthetransmission(largedata)betweenthemodule(DCE)andthe
terminaldevice(DTE).Whenreceivingbufferreachesitscapacity,thereceivingdeviceshouldbecapable
ofpausethesendingdeviceuntilitoverflows.SIM 7000 moduleisdesignedasnoflowcontrolbydefault,
butuserscanenablethisfunctionbyATcommand.

5 1 Hardwareflowcontrol(RTS/CTS).........................................................................................................
HardwareflowcontrolachievesthedataflowcontrolbycontrollingtheRTS/CTSlinewhichfollowsthe
RS 232 standard.Thecommand“AT+IFC= 2 , 2 ”canbeusedtoenablehardwareflowcontrol,thesesettings
can'tbestoredautomatically.

Toenablehardwareflowcontrol,ensurethattheRTS/CTSlinesarepresentonuser’sapplicationplatform.

6 ControlSignals..........................................................................................................................................
6 1 RTS.............................................................................................................................................................
WhenRTSpinisinhardwareflowcontrolmode,thissignalisasserted(lowlevel)topreparethemodule
(DCE)foracceptingtransmitteddatafromtheDTEdevice.

DCEstoptransmittingdataifRTSpinisathighlevel,transmissionbeginsorcontinuesifRTSisatlowlevel,
ifRTSgoeshighinthemiddleoftransmission,themodule(DCE)waitsforacompletedtransmissionbefore
stoptransmittingdata.

ThispinisinGPIOmodebydefault,usercanswitchittoflowcontrolmodeby“AT+IFC= 2 , 2 ”command.

6 2 CTS.............................................................................................................................................................
Whenthispinisinhardwareflowcontrolmode,thesignalisassertedbythemodule(DCE)toinformthe
DTEdevicethattransmissionmaybegin.

TheCTSpinoutputshighlevelwhentheRXFIFOlevelofthemodule(DCE)isuptothethreshold,when
theRXFIFOlevelfallsbelowthethreshold,theCTSpinoutputslowlevel.

ThispinisinGPIOmodebydefault,usercanswitchtoflowcontrolmodeby“AT+IFC= 2 , 2 ” command.

6 3 DCD.............................................................................................................................................................
ATcommandAT&CcanbeusedtosetDCDfunctionmode.Whenset“AT&C 0 ”,DCDlineisalwaysON
(low).Whenset“AT&C 1 ”,DCDlineisON(low)onlyinthepresenceofdatacarrier.

6 4 DTR.............................................................................................................................................................
Thepinisusedtocontrolmoduleintosleepmodeorwakeupmodule.WhenusershadsetATcommand
“AT+CSCLK= 1 ”,thenpullingupthepinDTRby host,Modulewill beintosleepmode.Insleepmode,
modulewillneverrespondATrequest.

IfDTRpinwaspulleddownbyhost,modulewillbewakeup.

IfsettingATcommand“AT+CSCLK= 0 ”,Modulewillbeneverintosleepmode.Anditwilldonothingwhen
theDTRpinispullingup.

IftherehasSMSduringmodulesleepmode,therewillbeURCreportedtohost,andmodulewillbe
wakedupbythisSMS.OnceDTRisathighlevel,andtherehasnoairdataorUARTcommunication,
modulewillgobacktosleepmodeagain.

6 5 RI.................................................................................................................................................................
Thispinisusedtowakeuphostwhenmodulehasmessagetooutput,messagecouldbeSMSorDATA
URC.

Table 3 :RIRespond

State RIrespond

Standby HIGHlevel

SMS WthehnenitriesccehiavinnggeSdMtoSH,ItGheHRleIvPeIl.NwillbechangedtoLOWlevelforabout^120 ms,and

DATAURC
WhenreceivingDATAURC,theRIPINwillbechangedtoLOWlevelforabout 120 ms,
and then it is changed to HIGH level. This function can be enable/disable by
“AT+CFGRI”command.
TheRIpincanbeusedtointerruptoutputsignaltoinformthehostcontrollersuchasapplicationCPU.
Beforethat,usersmustuseATcommand“AT+CFGRI= 1 ”toenablethisfunction.

NormallyRIwillkeephighleveluntilcertainconditionssuchasreceivingSMS,oraDATAURCreport
coming.Thenitwilloutputalowlevelpulse 120 ms,intheend,itwillbecomehighlevel.

NOTE

Figure 4 :RIbehaviour （ SMSandDATAURCreport

This is a offline tool, your data stays locally and is not send to any server!
Feedback & Bug Reports