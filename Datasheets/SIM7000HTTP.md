SIM 7000 Series_
HTTP(S)_Application Note
SIMComWirelessSolutionsLimited
BuildingB,SIMTechnologyBuilding,No. 633 ,JinzhongRoad
ChangningDistrict,ShanghaiP.R.China
Tel: 86 - 21 - 31575100
support@simcom.com
http://www.simcom.com
LPWAModule
DocumentTitle: SIM 7000 Series_HTTP(S)_ApplicationNote
Version: 1. 03
Date:^2020.^07.^28
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
V 1. 00 2018. 9. 28 Xiaobao.qu FirstRelease
V 1. 01 2019. 1. 23 Xiaobao.qu ModifiedCharpter 3. 3 andmaxlengthofsomeparameters

V 1. 02 2019. 12. 25 Jiangting.ding AddedHTTPandHTTPSSamples
V. 103 2020. 07. 28 Wenjie.lai All

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
2 HTTP(S)Function..........................................................................................................................
2 1 Characteristic...............................................................................................................................................
2 2 RequestMethod..........................................................................................................................................
3 ATCommandsforHTTP(S)........................................................................................................
4 BearerConfiguration
4 1 PDNAuto-activation.................................................................................................................................
4 2 APNManualconfiguration.......................................................................................................................
5 HTTP(S)Examples......................................................................................................................
5 1 HTTPFunction..........................................................................................................................................
5 1 1 HTTPGET.....................................................................................................................................
5 1 2 HTTPPOST...................................................................................................................................
5 2 HTTPSFunction........................................................................................................................................
5 1 1 HTTPSdownloadandconvertSSLcertificate........................................................................
5 2 1 HTTPSGET...................................................................................................................................
5 2 2 HTTPSPOST................................................................................................................................
1 Introduction....................................................................................................................................
1 1 Purposeofthedocument...........................................................................................................................
BasedonmoduleATcommandmanual,thisdocumentwillintroduceHTTP(S)applicationprocess.

Developerscouldunderstandanddevelopapplicationquicklyandefficientlybasedonthisdocument.

1 2 Relateddocuments.....................................................................................................................................
[ 1 ]SIM 7000 Series_ATCommandManual
[ 2 ]RFC 2616

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

2 HTTP(S)Function..........................................................................................................................
HTTP(HyperTextTransferProtocol)isanapplicationlayerprotocol.Whenyoubrowseawebpage,the
browserandthewebserverwillsendandreceivedataontheInternetthroughtheHTTPprotocol.HTTPis
a stateless protocol based on request and response patterns. That is what we usually call
Request/Response.

2 1 Characteristic...............................................................................................................................................
 Supportclient/servermode;
 Simpleandfast
Whenaclientrequestsaservicefromaserver,itonlyneedstopasstherequestmethodandpath.
BecausetheHTTPprotocolissimple,theprogramsizeoftheHTTPserverissmall,andthecommunication
speedisfast.
 Flexible
HTTPallowsthetransfer of any typeofdataobject. Thetypebeingtransferred is markedby
Content-Type;
 Noconnection
Noconnectionmeanslimitingtheprocessingofonlyonerequestperlink.Aftertheserverprocessesthe
client's requestandreceives thecustomer's response,theserver disconnects thelink.Thisway, the
transmissiontimecanbesaved.
 Stateless
TheHTTPprotocolisastatelessprotocol.Statelessmeansthattheprotocolhasnomemoryfortransaction
processing.Alackofstatemeansthatifsubsequentprocessingrequiresthepreviousinformation,itmust
beretransmitted,whichmayresultinanincreaseintheamountofdatatransferredperconnection.Onthe
otherhand,itrespondsfasterwhentheserverdoesnotneedpreviousinformation.

2 2 RequestMethod..........................................................................................................................................
AccordingtotheHTTPstandard,HTTPrequestscanuseavarietyofrequestmethods.
HTTP 1. 0 definesthreerequestmethods:theGET,POST,andHEADmethods.
HTTP 1. 1 addssixnewrequestmethods:OPTIONS,PUT,PATCH,DELETE,TRACE,andCONNECT
methods.

No Method Description
1 GET Makearequesttoaspecificresource.

2 HEAD
AsktheserverforaresponsethatisconsistentwiththeGETrequest,exceptthat
theresponsebodywillnotbereturned.Thismethodcanobtainthemeta
informationcontainedintheresponsemessageheaderwithouthavingtotransmit
theentireresponsecontent.
3 POST
Submitdatatoaspecifiedresourceforprocessingrequests(suchassubmittinga
formoruploadingafile).Thedataisincludedintherequestbody.POSTrequests
mayresultinthecreationofnewresourcesand/ormodificationstoexisting
resources.
4 PUT Uploadsitslatestcontenttoaspecifiedresourcelocation.
5 DELETE RequeststheservertodeletetheresourceidentifiedbytheRequest-URI.

6 CONNECT
HTheHTTP/ 1. 1 protocolisreservedforproxyserversthatcanconnect
connectionstopipes.

7 OPTIONS

Returns the HTTP request method supported by the server for a particular
resource.Youcanalsotestthefunctionalityoftheserverbysendinga'*'request
tothewebserver.
8 TRACE Echoesrequestsreceivedbytheserver,primarilyfortestingordiagnostics.
9 PATCH ItisasupplementtothePUTmethodforlocalupdatingofknownresources.

TheSIM 7000 seriessupportsseveralmethods:GET,POST,PUT,PATCHandHEAD.

3 ATCommandsforHTTP(S)........................................................................................................
ATCommand Description
AT+SHSSL SelectSSLConfigure
AT+SHCONF SetHTTP(S)Parameter
AT+SHCONN HTTP(S)Connection

AT+SHBOD SetBody
AT+SHBODEXT SetExtensionBody
AT+SHAHEAD AddHead
AT+SHPARA SetHTTP(S)Para
AT+SHCPARA ClearHTTP(S)Para
AT+SHCHEAD ClearHead
AT+SHSTATE QueryHTTP(S)ConnectionStatus
AT+SHREQ SetRequestType
AT+SHREAD ReadResponseValue

AT+SHDISC DisconnectHTTP(S)
AT+HTTPTOFS Downloadfiletoapfilesystem
AT+HTTPTOFSRL Stateofdownloadfiletoapfilesystem

Fordetailinformation,pleasereferto“SIM 7000 Series_ATCommandManual”.

4 BearerConfiguration
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
5 HTTP(S)Examples......................................................................................................................
5 1 HTTPFunction..........................................................................................................................................
5 1 1 HTTPGET.....................................................................................................................................
//ExampleofHTTPGET.

AT+SHCONF="URL","http://httpbin.org"
OK

//SetupserverURL
AT+SHCONF="BODYLEN", 1024
OK

//SetHTTPbodylength,forrangeofmaxbody
length
AT+SHCONF="HEADERLEN", 350
OK

//SetHTTPheadlength,forrangeofmaxhead
length
AT+SHCONN
OK

//HTTPbuild
AT+SHSTATE?
+SHSTATE: 1

OK

//GetHTTPstatus
//“+SHSTATE: 1 ”:connected
//“+SHSTATE: 0 ”:disconnected
AT+SHCHEAD
OK

//ClearHTTPheader,becauseofhttpheaderis
appended
AT+SHAHEAD="User-Agent","curl/ 7. 47. 0 "
OK

//Addheadercontent
//Fordetail,pleasereferto document"rfc 2616 "
AT+SHAHEAD="Cache-control","no-cache"
OK

//Addheadercontent
//Fordetail,pleasereferto document"rfc 2616 "
AT+SHAHEAD="Connection","keep-alive"
OK

//Addheadercontent
//Fordetail,pleasereferto document"rfc 2616 "
AT+SHAHEAD="Accept","/"
OK**

//Addheadercontent
//Fordetail,pleasereferto document"rfc 2616 "
AT+SHREQ="/get?user=jack&password= 123 ", 1
OK

+SHREQ:"GET", 200 , 387
//SetrequesttypeisGET.
//Getdatasizeis 387.
AT+SHREAD= 0 , 387
OK
//Readdatalengthis 387
//Thedatacontentisfollow“ +SHREAD: 387 ”
+SHREAD: 387
{
"args":{
"password":" 123 ",
"user":"jack"
},
"headers":{
"Accept":"/",
"Cache-Control":"no-cache",
"Content-Length":" 0 ",
"Host":"httpbin.org",
"User-Agent":"curl/ 7. 47. 0 ",
"X-Amzn-Trace-Id":
"Root= 1 - 5 ed 706 c 8 - 99 b 97372 ae 6 f 043 f 805 cf 243 "
},
"origin":" 117. 132. 195. 245 ",
"url":
"http://httpbin.org/get?user=jack&password= 12
3 "
}**

AT+SHDISC
OK

//DisconnectHTTPconnect
5 1 2 HTTPPOST...................................................................................................................................
//Example 1 ofHTTPPOST.

AT+SHCONF="URL","http://httpbin.org"
OK

//SetupserverURL
AT+SHCONF="BODYLEN", 1024
OK

//SetHTTPbodylength
AT+SHCONF="HEADERLEN", 350
OK

//SetHTTPheadlength
AT+SHCONN
OK

//HTTPbuild
AT+SHSTATE?
+SHSTATE: 1

OK

//GetHTTPstatus
AT+SHCHEAD
OK
//ClearHTTPheader
AT+SHAHEAD="Content-Type","application/x- //Addheadercontent

www-form-urlencoded"
OK
AT+SHAHEAD="Cache-control","no-cache"
OK

//Addheadercontent
AT+SHAHEAD="Connection","keep-alive"
OK

//Addheadercontent
AT+SHAHEAD="Accept","/"
OK**

//Addheadercontent
AT+SHCPARA
OK

//Clearbodycontentparameter
AT+SHPARA="product","apple"
OK

//Addbodycontentparameter
AT+SHPARA="price"," 1 "
OK

//Addbodycontentparameter
AT+SHREQ="/post", 3
OK

+SHREQ:"POST", 200 , 452

//SetrequesttypeisPOST
//Getdatasizeis 452.
AT+SHREAD= 0 , 452
OK
+SHREAD: 452
{
"args":{},
"data":"",
"files":{},
"form":{
"price":" 1 ",
"product":"apple"
},
"headers":{
"Accept":"/",
"Cache-Control":"no-cache",
"Content-Length":" 21 ",
"Content-Type":
"application/x-www-form-urlencoded",
"Host":"httpbin.org",
"X-Amzn-Trace-Id":
"Root= 1 - 5 ed 633 df- 058 feb 6412204392 e 95333 b 2
"
},
"json":null,
"origin":" 218. 204. 252. 187 ",
"url":"http://httpbin.org/post"
}**

//Readdatalengthis 452
//Thedatacontentisfollow“ +SHREAD: 452 ”
AT+SHDISC
OK
//DisconnectHTTPconnect
//Example 2 ofHTTPPOST.

AT+SHCONF="URL","http://httpbin.org"
OK

//SetupserverURL
AT+SHCONF="BODYLEN", 1024
OK

//SetHTTPbodylength
AT+SHCONF="HEADERLEN", 350
OK

//SetHTTPheadlength
AT+SHCONN
OK

//HTTPbuild
AT+SHSTATE?
+SHSTATE: 1

OK

//GetHTTPstatus
AT+SHCHEAD
OK
//ClearHTTPheader
AT+SHAHEAD="Content-Type","application/x-
www-form-urlencoded"
OK

//Addheadercontent
AT+SHAHEAD="Cache-control","no-cache"
OK

//Addheadercontent
AT+SHAHEAD="Connection","keep-alive"
OK

//Addheadercontent
AT+SHAHEAD="Accept","/"
OK**

//Addheadercontent
AT+SHBOD="{"title":"Hellohttpserver"}", 29

OK

//Setbodycontent
AT+SHREQ="/post", 3
OK

+SHREQ:"POST", 200 , 457

//SetrequesttypeisPOST
//Getdatasizeis 457.
AT+SHREAD= 0 , 457
OK
+SHREAD: 457
{
"args":{},
"data":"{\"title\":\"Hellohttpserver\"}",
"files":{},
//Readdatalengthis 457
//Thedatacontentisfollow“ +SHREAD: 457 ”
"form":{},
"headers":{
"Accept":"/",
"Cache-Control":"no-cache",
"Content-Length":" 29 ",
"Content-Type":"application/json",
"Host":"httpbin.org",
"X-Amzn-Trace-Id":
"Root= 1 - 5 ed 63 fa 7 - 3 dda 07707 b 3 f 2 ea 63 e 092 a 3 a"
},
"json":{
"title":"Hellohttpserver"
},
"origin":" 218. 204. 252. 187 ",
"url":"http://httpbin.org/post"
}**

AT+SHDISC
OK

//DisconnectHTTPconnect
5 2 HTTPSFunction........................................................................................................................................
5 1 1 HTTPSdownloadandconvertSSLcertificate........................................................................
//ExampleofHTTPSdownloadandconvertSSLCertificate.

AT+CFSINIT
OK
//InitFSATcommand
AT+CFSWFILE= 3 ,"httpbin_root_ca.cer", 0 , 1492
, 1000

//Afterdownload,sentcertificatefilethroughthe
serialport. 1492 iscertificatesize.
DOWNLOAD

OK

//SendCAfilesuccess
AT+CFSTERM
OK
//Freedatabuffer

AT+CSSLCFG="convert", 2 ,"httpbin_root_ca.c
er"
OK

//ConversionCAcertificateformat.
// 2 meansCAtype.
//httpbin_root_ca.cerisCAcertificatename.
5 2 1 HTTPSGET...................................................................................................................................
//ExampleofHTTPSGET.

AT+CSSLCFG="sslversion", 1 , 3 //ConfigureSSL/TLSversion
OK

AT+SHSSL= 1 ,"httpbin_root_ca.cer"
OK

//SetHTTPSSLConfigure
//if you would skip certificate verify, use
AT+SHSSL= 1 ,""instead
AT+SHCONF="URL","https://httpbin.org"
OK

//Setconnectserverparameter
AT+SHCONF="BODYLEN", 1024
OK

//Setmaxbodylength
AT+SHCONF="HEADERLEN", 350
OK

//Setmaxheaderlength
AT+SHCONN
OK

//ConnectHTTPSserver
AT+SHSTATE?
+SHSTATE: 1

OK

//GetHTTPstatus
AT+SHCHEAD
OK
//ClearHTTPheadercontent
AT+SHAHEAD="User-Agent","curl/ 7. 47. 0 "
OK

//Addheadercontent
AT+SHAHEAD="Cache-control","no-cache"
OK

//Addheadercontent
AT+SHAHEAD="Connection","keep-alive"
OK

//Addheadercontent
AT+SHAHEAD="Accept","/"
OK**

//Addheadercontent
AT+SHREQ="/get?user=jack&password= 123 ", 1
OK

+SHREQ:"GET", 200 , 388
//SetrequesttypeisGET.
//Getdatasizeis 388
AT+SHREAD= 0 , 388
OK
+SHREAD: 388
{
"args":{
"password":" 123 ",
"user":"jack"
},
//Readdatalengthis 388
//Thedatacontentisfollow“ +SHREAD: 388 ”
"headers":{
"Accept":"/",
"Cache-Control":"no-cache",
"Content-Length":" 0 ",
"Host":"httpbin.org",
"User-Agent":"curl/ 7. 47. 0 ",
"X-Amzn-Trace-Id":
"Root= 1 - 5 ed 706 c 8 - 99 b 97372 ae 6 f 043 f 805 cf 243 "
},
"origin":" 117. 132. 195. 245 ",
"url":
"https://httpbin.org/get?user=jack&password= 1
23 "
}**

AT+SHDISC
OK

//DisconnectHTTPconnect
5 2 2 HTTPSPOST................................................................................................................................
//Example 1 ofHTTPSPOST.

AT+CSSLCFG="sslversion", 1 , 3
OK

//ConfigureSSL/TLSversion
AT+SHSSL= 1 ,"baidu_root_ca.cer"
OK

//SetHTTPSSLConfigure
//if you would skip certificate verify, use
AT+SHSSL= 1 ,""instead
AT+SHCONF="URL","https://httpbin.org"
OK

//Setconnectserverparameter
AT+SHCONF="BODYLEN", 1024
OK

//Setmaxbodylength
AT+SHCONF="HEADERLEN", 350
OK

//Setmaxheaderlength
AT+SHCONN
OK

//ConnectHTTPSserver
AT+SHSTATE?
+SHSTATE: 1

OK

//GetHTTPstatus
AT+SHCHEAD
OK
//ClearHTTPheader
AT+SHAHEAD="Content-Type","application/x-
www-form-urlencoded"
OK

//Addheadercontent
AT+SHAHEAD="Cache-control","no-cache"
OK

//Addheadercontent
AT+SHAHEAD="Connection","keep-alive"
OK

//Addheadercontent
AT+SHAHEAD="Accept","/"
OK**

//Addheadercontent
AT+SHCPARA
OK

//Clearbodycontentpara
AT+SHPARA="product","apple"
OK

//Addbodycontentpara
AT+SHPARA="price"," 1 "
OK

//Addbodycontentpara
AT+SHREQ="/post", 3
OK

+SHREQ:"POST", 200 , 453

//SetrequesttypeisPOST
//Getdatasizeis 453.
AT+SHREAD= 0 , 453
OK
+SHREAD: 453
{
"args":{},
"data":"",
"files":{},
"form":{
"price":" 1 ",
"product":"apple"
},
"headers":{
"Accept":"/",
"Cache-Control":"no-cache",
"Content-Length":" 21 ",
"Content-Type":
"application/x-www-form-urlencoded",
"Host":"httpbin.org",
"X-Amzn-Trace-Id":
"Root= 1 - 5 ed 633 df- 058 feb 6412204392 e 95333 b 2
"
},
"json":null,
"origin":" 218. 204. 252. 187 ",
"url":"https://httpbin.org/post"
}**

//Readdatalengthis 453
//Thedatacontentisfollow“ +SHREAD: 453 ”
AT+SHDISC
OK
//DisconnectHTTPconnect
//Example 2 ofHTTPSPOST.

AT+CSSLCFG="sslversion", 1 , 3
OK

//ConfigureSSL/TLSversion
AT+SHSSL= 1 ,"baidu_root_ca.cer"
OK

//SetHTTPSSLConfigure
//if you would skip certificate verify, use
AT+SHSSL= 1 ,"" instead
AT+SHCONF="URL","https://httpbin.org"
OK

//Setconnectserverparameter
AT+SHCONF="BODYLEN", 1024
OK

//Setmaxbodylength
AT+SHCONF="HEADERLEN", 350
OK

//Setmaxheaderlength
AT+SHCONN
OK

//ConnectHTTPSserver
AT+SHSTATE?
+SHSTATE: 1

OK

//GetHTTPstatus
AT+SHCHEAD
OK
//ClearHTTPheader
AT+SHAHEAD="Content-Type","application/js
on"
OK

//Addheadercontent
AT+SHAHEAD="Cache-control","no-cache"
OK

//Addheadercontent
AT+SHAHEAD="Connection","keep-alive"
OK

//Addheadercontent
AT+SHAHEAD="Accept","/"
OK**

//Addheadercontent
AT+SHBOD="{"title":"Hellohttpserver"}", 29
OK

//Setbodycontent
AT+SHREQ="/post", 3
OK

+SHREQ:"POST", 200 , 458

//SetrequesttypeisPOST
//Getdatasizeis 458.
AT+SHREAD= 0 , 458
OK
+SHREAD: 458
{
"args":{},
"data":"{\"title\":\"Hellohttpserver\"}",
//Readdatalengthis 458
//Thedatacontentisfollow“ +SHREAD: 458 ”
"files":{},
"form":{},
"headers":{
"Accept":"/",
"Cache-Control":"no-cache",
"Content-Length":" 29 ",
"Content-Type":"application/json",
"Host":"httpbin.org",
"X-Amzn-Trace-Id":
"Root= 1 - 5 ed 63 fa 7 - 3 dda 07707 b 3 f 2 ea 63 e 092 a 3 a
"
},
"json":{
"title":"Hellohttpserver"
},
"origin":" 218. 204. 252. 187 ",
"url":"https://httpbin.org/post"
}**

AT+SHDISC
OK

//DisconnectHTTPconnect
This is a offline tool, your data stays locally and is not send to any server!
Feedback & Bug Reports