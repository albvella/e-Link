SIM 7000 Series_MQTT(S)
_Application Note
SIMComWirelessSolutionsLimited
BuildingB,SIMTechnologyBuilding,No. 633 ,JinzhongRoad
ChangningDistrict,ShanghaiP.R.China
Tel: 86 - 21 - 31575100
support@simcom.com
http://www.simcom.com
LPWAModule
DocumentTitle: SIM 7000 Series_MQTT(S)_ApplicationNote
Version: 1. 02
Date:^2020.^7.^28
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
AboutDocument..................................................................................................................................
VersionHistory.........................................................................................................................................................
Version Date Owner Whatisnew
V 1. 00 2018. 09. 28 Xiaobao.qu FirstRelease

V 1. 01 2019. 01. 23 Xiaobao.qu AddedConnectingAliCloudFunction
V 1. 02 2020. 07. 28 Wenjie.Lai All

Scope........................................................................................................................................................................
Thisdocumentappliestothefollowingproducts

Name Type Size(mm) Comments
SIM 7000 E/C/A/G Cat-M 1 (/NB 1 /EGPRS) 24 * 24
SIM 7000 E-N
SIM 7000 C-N

NB 1 24 * 24
Contents.................................................................................................................................................
Contents
AboutDocument..................................................................................................................................
VersionHistory.........................................................................................................................................................
Scope........................................................................................................................................................................
Contents.................................................................................................................................................
1 Introduction....................................................................................................................................
1 1 Purposeofthedocument...........................................................................................................................
1 2 Relateddocuments.....................................................................................................................................
1 3 Conventionsandabbreviations................................................................................................................
2 MQTT(S)Function.........................................................................................................................
3 ATCommandsforMQTT(S).......................................................................................................
3 1 Overview.......................................................................................................................................................
3 2 DetailedDescriptionsofCommands.......................................................................................................
3 2 1 AT+SMCONF SetMQTTParameter........................................................................................
3 2 2 AT+CSSLCFG SSLConfigure...................................................................................................
3 2 3 AT+SMSSL SelectSSLConfigure............................................................................................
3 2 4 AT+SMCONN MQTTConnection...........................................................................................
3 2 5 AT+SMPUB SendPacket.........................................................................................................
3 2 6 AT+SMSUB SubscribePacket................................................................................................
3 2 7 AT+SMUNSUB UnsubscribePacket......................................................................................
3 2 8 AT+SMSTATE InquireMQTTConnectionStatus.................................................................
3 2 9 AT+SMPUBHEX SetSMPUBDataFormattoHex..............................................................
3 2 10 AT+SMDISC DisconnectMQTT..............................................................................................
4 BearerConfiguration.................................................................................................................
4 1 PDNAuto-activation.................................................................................................................................
4 2 APNManualconfiguration.......................................................................................................................
5 MQTT(S)Examples.....................................................................................................................
5 1 MQTTFunction.........................................................................................................................................
5 2 MQTTSFunction.......................................................................................................................................
5 3 ConnectingAliCloudFunction...............................................................................................................
5 3 1 MQTTConnectingAliCloudFunction.......................................................................................
5 3 2 MQTTSConnectingAliCloudFunction....................................................................................
1 Introduction....................................................................................................................................
1 1 Purposeofthedocument...........................................................................................................................
BasedonmoduleATcommandmanual,thisdocumentwillintroduceMQTT(S)applicationprocess.

Developerscouldunderstandanddevelopapplicationquicklyandefficientlybasedonthisdocument.

1 2 Relateddocuments.....................................................................................................................................
[ 1 ]SIM 7000 Series_ATCommandManual

1 3 Conventionsandabbreviations................................................................................................................
Inthisdocument,theGSMenginesarereferredtoasfollowingterm:
 ME(MobileEquipment);
 MS(MobileStation);
 TA(TerminalAdapter);
 DCE(DataCommunicationEquipment)orfacsimileDCE(FAXmodem,FAXboard);

Inapplication,controllingdevicecontrolstheGSMenginebysendingATCommandviaitsserialinterface.
Thecontrollingdeviceattheotherendoftheseriallineisreferredtoasfollowingterm:
 TE(TerminalEquipment);
 DTE(DataTerminalEquipment)orplainly"theapplication"whichisrunningonanembeddedsystem;

2 MQTT(S)Function.........................................................................................................................
MQTT(MessageQueueTelemetryTransport)isamessagingprotocolbasedonthepublish/subscribe
paradigmundertheISOstandard(ISO/IECPRF 20922 ).ItworksontheTCP/IPprotocolsuiteandisa
publish/subscribemessagingprotocoldesignedforremotedeviceswithpoorhardwareperformanceand
poornetworkconditions.

TheMQTTprotocolisaprotocoldesignedforthecommunicationofremotesensorsandcontroldevices
withlimitedcomputingpowerandworkingonlow-bandwidth,unreliablenetworks.Ithasthefollowingmain
features:

 Usethepublish/subscribemessagemodetoprovideone-to-manymessagepublishinganduncouple
theapplication;

 Messagetransmissionforshieldingthepayloadcontent;

 ProvidenetworkconnectionusingTCP/IP;

 Therearethreetypesofmessagepublishingservicequality:

 "Atmostonce,"messagepublishingreliesentirelyontheunderlyingTCP/IPnetwork.Message
lossorduplicationcanoccur.Thislevelcanbeusedinthefollowingsituations,environmental
sensordata,lossofareadrecorddoesnotmatter,becausetherewillbeasecondtransmissionin
thenearfuture.
 "Atleastonce"toensurethatthemessagearrives,butmessageduplicationmayoccur.
 "Onlyonce"toensurethatthemessagearrivesonce.Thislevelcanbeusedinsituationswhere
repeatedormissingmessagescanresultinincorrectresults.
 smalltransmission,lowoverhead(fixedlengthoftheheadis 2 bytes),protocolexchangeisminimized
toreducenetworktraffic;

 UsetheLastWillandTestamentfeaturestonotifythepartiesaboutthemechanismofclientabort.

3 ATCommandsforMQTT(S).......................................................................................................
3 1 Overview.......................................................................................................................................................
ATCommand Description
AT+SMCONF SetMQTTParameter
AT+CSSLCFG SSLConfigure
AT+SMSSL SelectSSLConfigure

AT+SMCONN MQTTConnection
AT+SMPUB SendPacket
AT+SMSUB SubscribePacket
AT+SMUNSUB UnsubscribePacket

AT+SMSTATE InquireMQTTConnectionStatus
AT+SMPUBHEX SetSMPUBDataFormattoHex
AT+SMDISC DisconnectionMQTT

3 2 DetailedDescriptionsofCommands.......................................................................................................
3 2 1 AT+SMCONF SetMQTTParameter........................................................................................
AT+SMCONF SetMQTTParameter
TestCommand
AT+SMCONF=?

Response
+SMCONF:"MQTTParamTag","MQTTParamValuerange"
OK
ReadCommand
AT+SMCONF?

Response
+SMCONF:<MQTTParamTag>,<MQTTParamValue>
OK
WriteCommand
AT+SMCONF=<MQTTPa

Response
OK
ramTag>,

or
ERROR
Parameters
<MQTTParamTag>
"CLIENTID" Clientconnectionid
"URL" (indispensableparameter)serverURLaddress
"serverdomain",["tcpPort"]
"server":HostorIP
"tcpPort":Portdefaultis 1883
"KEEPTIME" Holdconnecttime.defaultis 60 s
"CLEANSS" Sessioncleanin.Defaultis 0.
Rangeofvalues:( 0 - 1 ).
"USERNAME" Username.defaultnull
"PASSWORD" Password.defaultnull
"QOS" SendpacketQOSlevel.rangeofvalues（ 0 ~ 2 ）
"TOPIC" Publishtopicname
"MESSAGE" Publishmessagedetails
"RETAIN" Retainidentification.Defaultis 0.
Rangeofvalues:( 0 - 1 )
<MQTTParamValue> MQTTParametervalue.Typeandsupported
contentdependonrelated <MQTTParamTag>.
Example

AT+SMCONF="CLIENTID","id"
OK
AT+SMCONF="KEEPTIME", 60
OK
AT+SMCONF="URL","test.mosquitto.org"," 1883 "
OK
AT+SMCONF="CLEANSS", 1
OK
AT+SMCONF="QOS", 1
OK
AT+SMCONF="TOPIC","willtopic"
OK
AT+SMCONF="MESSAGE","willmessage"
OK
AT+SMCONF="RETAIN", 1
OK
3 2 2 AT+CSSLCFG SSLConfigure...................................................................................................
AT+CSSLCFG SSLConfigure
Writecommand Response

AT+CSSLCFG="convert
",,[,<
keyname>[,]]

OK
Iffailed:
+CMEERROR:
Parameters

1 QAPI_NET_SSL_CERTIFICATE_E
2 QAPI_NET_SSL_CA_LIST_E
3 QAPI_NET_SSL_PSK_TABLE_E
< cname > Stringtype(stringshouldbeincludedinquotationmarks):
nameofcertfile
< keyname > Stringtype(stringshouldbeincludedinquotation
marks):nameofkeyfile
< passkey > String type (string should be included in quotation
marks):valueofpasskey
ParameterSavingMode -
MaxResponseTime -
Reference -

3 2 3 AT+SMSSL SelectSSLConfigure............................................................................................
AT+SMSSL SelectSSLConfigure
ReadCommand
AT+SMSSL?

Response
+SMSSL:<index>,<calist>,<certname>
OK
WriteCommand
AT+SMSSL=,,

Response
OK
or
ERROR
Parameters
< index > SSLstatus,range: 0 - 6
< calist > CA_LISTfilename,length 20 byte
< certname > CERT_NAMEfilename,length 20 byte
Example
AT+SMSSL= 1 ,calist,certname
OK

3 2 4 AT+SMCONN MQTTConnection...........................................................................................
AT+SMCONN MQTTConnection
Execution
Command
AT+SMCONN

Response
OK
or
ERROR
Example

AT+SMCONN
OK
3 2 5 AT+SMPUB SendPacket.........................................................................................................
AT+SMPUB SendPacket
TestCommand
AT+SMPUB=?

Response
+SMPUB:<topic>,<contentlength>,( 0 - 2 ),( 0 - 1 )
OK
WriteCommand
AT+SMPUB=,,,

Response
OK
or
ERROR
Parameters
< topic > Subscribepacket
< qos > SendpacketQOSlevel,range: 0 ~ 2
< contentlength > Messagelength,range: 0 ~ 512
< retain > Serverholdmessagerange: 0 ~ 1
Example

AT+SMPUB=" 001 ", 10 , 1 , 1
OK
3 2 6 AT+SMSUB SubscribePacket................................................................................................
AT+SMSUB SubscribePacket
TestCommand
AT+SMSUB=?

Response
+SMSUB:"topic",qos
OK
WriteCommand
AT+SMSUB=,

Response
OK
or
ERROR
Parameters
< topic > Subscribepacket
< qos > Sendpacketqoslevel,range: 0 ~ 2
Example

AT+SMSUB=" 001 ", 1
OK
3 2 7 AT+SMUNSUB UnsubscribePacket......................................................................................
AT+SMUNSUB UnsubscribePacket
ReadCommand
AT+SMUNSUB=?

Response
+SMUNSUB:"topic"
OK
WriteCommand
AT+SMUNSUB=

Response
OK
or
ERROR
Parameters
< topic > Subscribesubject
Example

AT+SMUNSUB=" 001 "
OK
3 2 8 AT+SMSTATE InquireMQTTConnectionStatus.................................................................
AT+SMSTATE InquireMQTTConnectionStatus
ReadCommand
AT+SMSTATE?

Response
+SMSTATE:<status>
OK
Parameters
< status >
0 ExpressionMQTTdisconnectstate
1 ExpressionMQTTon-linestate
Example

AT+SMSTATE?
+SMSTATE: 1
OK
3 2 9 AT+SMPUBHEX SetSMPUBDataFormattoHex..............................................................
AT+SMPUBHEX SetSMPUBDataFormattoHex
TestCommand
AT+SMPUBHEX=?

Response
+SMPUBHEX:( 0 - 1 )
OK
ReadCommand
AT+SMPUBHEX?

Response
+SMPUBHEX:<status>
OK
PARAMETERS
< status >
0 SMPUBdataformatisnormal
1 SMPUBdataformatishex
WriteCommand
AT+SMPUBHEX=

Response
OK
or
ERROR
Parameters
< status > SMPUBformatstatus,range: 0 ~ 1
Example

AT+SMPUBHEX= 1
OK
3 2 10 AT+SMDISC DisconnectMQTT..............................................................................................
AT+SMDISC DisconnectMQTT
ExecutionCommand
AT+SMDISC

Response
OK
or
ERROR
Example

AT+SMDISC
OK
4 BearerConfiguration.................................................................................................................
UsuallymodulewillregisterPSserviceautomatically.

4 1 PDNAuto-activation.................................................................................................................................
//ExampleofPDNAuto-activation.

AT+CPIN? //CheckSIMcardstatus
+CPIN:READY

OK
AT+CGDCONT= 1 ,"IP","" //ConfigureAPNforregistrationwhenneeded
OK
AT+CSQ //CheckRFsignal
+CSQ: 27 , 99

OK
AT+CGATT? //CheckPSservice.
+CGATT: 1

OK

// 1 indicatesPShasattached.
AT+COPS?
+COPS: 0 , 0 ,"CHN-CT", 9
OK
//QueryNetworkinformation,operatorandnetwork
mode 9 ,NB-IOTnetwork
AT+CGNAPN //QuerytheAPNdeliveredbythenetworkafterthe
CAT-M or NB-IOT network is successfully
registered.
+CGNAPN: 1 ,"ctnb"

OK

//"ctnb"isAPNdeliveredbytheCAT-MorNB-IOT
network.APNisemptyundertheGSMnetwork.
AT+CNCFG= 1 ,"ctnb","cdma"," 1234 " //BeforeactivationpleaseuseAT+CNCFGtoset
APN\username\passwordifneeded.
OK
AT+CNACT= 1
OK

//Activatenetwork
+APPPDP:ACTIVE
AT+CNACT?
+CNACT: 0 , 1 ," 10. 94. 36. 44 "
OK
//GetlocalIP
4 2 APNManualconfiguration.......................................................................................................................
Ifnotattachedautomatically,couldconfigurecorrectAPNsetting.

//ExampleofAPNManualconfiguration.

AT+CFUN= 0 //DisableRF
+CPIN:NOTREADY

OK
AT+CGDCONT= 1 ,"IP","ctnb" //SettheAPNmanually
OK
AT+CFUN= 1 //EnableRF
OK

+CPIN:READY
AT+CGATT? //CheckPSservice.
+CGATT: 1

OK

// 1 indicatesPShasattached.
AT+CGNAPN //QuerytheAPNdeliveredbythenetworkafterthe
CAT-M or NB-IOT network is successfully
registered.
+CGNAPN: 1 ,"ctnb"

OK

//"ctnb"isAPNdeliveredbytheCAT-MorNB-IOT
network.APNisemptyundertheGSMnetwork.
AT+CNCFG= 1 ,"ctnb","cdma"," 1234 " //BeforeactivationpleaseuseAT+CNCFGtoset
APN\username\passwordifneeded.
OK
AT+CNACT= 1
OK

+APPPDP:ACTIVE

//Activatenetwork
AT+CNACT?
+CNACT: 0 , 1 ," 10. 94. 36. 44 "
//GetlocalIP
OK
5 MQTT(S)Examples.....................................................................................................................
5 1 MQTTFunction.........................................................................................................................................
//ExampleofMQTTFunction

AT+CNACT= 1 ,"cmnet" //Openwirelessconnection//parameterCMNETis
APN,thisparameterneeds tosetdifferentAPN
valuesaccordingtodifferentcards
OK

+APPPDP:ACTIVE
AT+CNACT? //GetlocalIP
+CNACT: 1 ," 10. 181. 182. 177 "

OK
AT+SMCONF="URL", 117. 131. 85. 139 , 6000 //SetupserverURL
OK
AT+SMCONF="KEEPTIME", 60 //SetMQTTtimetoconnectserver
OK
AT+SMCONN
OK
AT+SMSUB="update", 1 //Subscriptionpacket
**OK
AT+SMPUB="update"," 5 ", 1 , 1

hello**

//Sendpacket
//Getdataonserver
OK
+SMSUB:"update","hello"
AT+SMUNSUB="update" //Unsubscriptionpacket
OK
AT+SMDISC //DisconnectMQTT
OK
AT+CNACT= 0 //Disconnectwireless
OK

+APPPDP:DEACTIVE
AT+CNACT= 1 ,"cmnet"

5 2 MQTTSFunction.......................................................................................................................................
//ExampleofMQTTSFunction

AT+CNACT= 1 ,"cmnet" //Openwirelessconnection//parameterCMNETis
APN,thisparameterneedstosetdifferentAPN
valuesaccordingtodifferentcards
OK

+APPPDP:ACTIVE
AT+CNACT? //GetlocalIP
+CNACT: 1 ," 10. 181. 182. 177 "

OK
AT+CFSINIT //InitFSATcommand
OK
AT+CFSWFILE= 3 ,"ca.crt", 0 , 2110 , 1000 //Afterdownload,sentcertificatefilethroughthe
serialport.
// 2110 iscertificatesize.
DOWNLOAD

OK

//SendCAfilesuccess
AT+CFSWFILE= 3 ,"myclient.crt", 0 , 2110 , 1000 //Sendcertfilesuccess
DOWNLOAD

OK
AT+CFSTERM //Freedatabuffer
OK
AT+SMCONF="URL", 117. 131. 85. 139 , 6001 //SetupserverURL
OK
AT+SMCONF="KEEPTIME", 60 //SetMQTTtimetoconnectserver
OK
AT+CSSLCFG=convert, 2 ,ca.crt //rootCA.pemisCAcertificate
OK
AT+CSSLCFG=convert, 1 ,myclient.crt,myclient.
key

//cert.pemiscertificate,key.pemiskeyofcert.pem
OK
AT+SMSSL= 1 ,ca.crt,myclient.crt //SetCAcertificateandcert//certificatename
OK
AT+SMCONN
OK
AT+SMSUB="update", 1 //Subscriptionpacket
OK
AT+SMPUB="update"," 5 ", 1 , 1 //Sendpacket

>hello //Getdataonserver
OK
+SMSUB:"update","hello"
AT+SMUNSUB="update" //Unsubscriptionpacket
OK
AT+SMDISC //DisconnectMQTT
OK
AT+CNACT= 0 //Disconnectwireless
OK

+APPPDP:DEACTIVE

5 3 ConnectingAliCloudFunction...............................................................................................................
5 3 1 MQTTConnectingAliCloudFunction.......................................................................................
//ExampleofMQTTConnectingAliCloudFunction

AT+CNACT= 1 ,"cmnet" //Openwirelessconnectionparameter//CMNETis
APN,thisparameter//needstosetdifferentAPN
values//accordingtodifferentcards
OK

+APPPDP:ACTIVE
AT+CNACT? //GetlocalIP
+CNACT: 1 ," 10. 181. 182. 177 "

OK
AT+SMCONF=url,a 1 kUAJknr 0 y.iot-as-mqtt.cn

- shanghai.aliyuncs.com, 1883

//Theformatofdomainnameis:
//productKey.iot-as-mqtt.cn-//shanghai.aliyuncs.co
m
Note:
//a 1 kUAJknr 0 yisproduct_key
OK
AT+SMCONF=username, 7000 C&a 1 kUAJknr 0
y

//Theformatofusernameis:
//deviceName&productKey
//Note:
//a 1 kUAJknr 0 yisproduct_key
// 7000 CisdeviceName
OK

AT+SMCONF=password, 56 bf 1 f 37 de 9 ce 2591 f 5
699 eea 1117 a 43 dae 9 bd 11

//ThepasswordisgeneratedbySHA 1 algorithm
OK
AT+SMCONF=clientid,"a 1 kUAJknr 0 y. 7000 C|s
ecuremode= 3 ,timestamp= 2524608000000 ,sig
nmethod=hmacsha 1 ,gw= 0 |"

//Theformatofclientidis:
//productKey.deviceName|securemod///e= 3 ,signme
thod=hmacsha 1 ,gw= 0 |
//Note:
//a 1 kUAJknr 0 yisproduct_key
// 7000 CisdeviceName
OK
AT+SMCONN //Connectok
OK

5 3 2 MQTTSConnectingAliCloudFunction....................................................................................
//Example of MQTTS Connecting Ali Cloud
Function

AT+CNACT= 1 ,"cmnet" //Openwirelessconnectionparameter//CMNETis
APN,thisparameterneedstosetdifferentAPN
values//accordingtodifferentcards
OK

+APPPDP:ACTIVE
AT+CNACT? //GetlocalIP
+CNACT: 1 ," 10. 181. 182. 177 "

OK
AT+CSSLCFG=convert, 2 ,aliiot_ca.pem //Convertaliiot_ca.pem
//Note:Importcertificates,pleasereferto
CFSWFILEcommand
OK
AT+CSSLCFG=convert, 1 ,simcom.cert.pem,si
mcom.private.key

//Convertcertfile
OK
AT+SMCONF=url,a 1 kUAJknr 0 y.iot-as-mqtt.cn

- shanghai.aliyuncs.com, 1883

//Theformatofdomainnameis:
//productKey.iot-as-mqtt.cn-//shanghai.aliyuncs.co
m
//Note:
//a 1 kUAJknr 0 yisproduct_key
OK
AT+SMCONF=username, 7000 C&a 1 kUAJknr 0 //Theformatofusernameis:

y //deviceName&productKey
//Note:
//a 1 kUAJknr 0 yisproduct_key
// 7000 CisdeviceName
OK
AT+SMCONF=password, 56 bf 1 f 37 de 9 ce 2591 f 5
699 eea 1117 a 43 dae 9 bd 11

//ThepasswordisgeneratedbySHA 1 algorithm
OK
AT+SMCONF=clientid,"a 1 kUAJknr 0 y. 7000 C|s
ecuremode= 3 ,timestamp= 2524608000000 ,sig
nmethod=hmacsha 1 ,gw= 0 |"

//Theformatofclientidis:
//productKey.deviceName|securemode= 3 ,signmeth
od=hmacsha 1 ,gw= 0 |
//a 1 kUAJknr 0 yisproduct_key
// 7000 CisdeviceName
OK
AT+SMSSL= 2 ,aliiot_ca.pem,simcom.cert.pem //ConfigureSSLconnectindex
OK
AT+SMCONN //Connectok
OK

This is a offline tool, your data stays locally and is not send to any server!
Feedback & Bug Reports