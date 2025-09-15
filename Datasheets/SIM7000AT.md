SIM 7000 Series_
AT Command Manual
SIMComWirelessSolutionsLimited
BuildingB,SIMTechnologyBuilding,No. 633 ,JinzhongRoad
ChangningDistrict,ShanghaiP.R.China
Tel: 86 - 21 - 31575100
support@simcom.com
http://www.simcom.com
LPWAModule
DocumentTitle: SIM 7000 Series_ATCommandManual
Version: 1. 06
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
VersionHistory.....................................................................................................................................
Version Date Chapter Whatisnew
V 1. 00 2017. 06. 22 Newversion

V 1. 01 2017. 09. 08
5. 2. 22 AT+CPSI AddATcommand
5. 2. 23 AT+CGNAPN AddATcommand
5. 2. 24 AT+CSDP AddATcommand
5. 2. 25 AT+MCELLLOCK AddATcommand
5. 2. 26 AT+NCELLLOCK AddATcommand
5. 2. 27 AT+NBSC AddATcommand
Chapter 7 AddIP
Chapter 9 AddHTTP
Chapter 10 AddPINGs
Chapter 13 AddGNSS
V 1. 02 2017. 12. 18
DeleteATZ,AT&F,AT&V
All
Modify parameter save mode and max
responsetime
1. 7. 1 AddAUTO_SAVE_REBOOT
1. 7. 2 AddMaxresponsetime
2. 2. 2 ATD Deleteparameters<;>
3. 2. 14 AT+CREG Changedescriptionofparameters
5. 2. 28 AT+CAPNMODE AddATcommand
5. 2. 29 AT+CRRCSTATE AddATcommand
5. 2. 30 AT+CBANDCFG AddATcommand
8. 2. 2 AT+CIPSTART
Changerangeofparameter<n>from 0 ... 5
to 0 ... 7
8. 2. 32 AT+CIPTKA AddATcommand
8. 2. 33 AT+CIPOPTION AddATcommand
Chapter 11 AddFTP
Chapter 12 AddNTP
13. 3. 10 AT+CGNSTST AddATCommand
V 1. 03 2018. 05. 08
3. 2. 17 AT+CPOL Modifyparameters
3. 2. 24 AT+CNUM AddATCommand
5. 2. 1 AT+CEDRXS Modifyrangeof<AcT-type>
5. 2. 31 AT+CNACT AddATCommand
5. 2. 32 AT+CEDUMP AddATCommand
5. 2. 33 AT+CNBS AddATCommand
5. 2. 34 AT+CNDS AddATCommand
5. 2. 35 AT+CENG AddATCommand
9. 2. 9 AT+HTTPTOFS AddATCommand
Chapter 13 AddOneNet
Chapter 14 AddTelecomIOT
Chapter 15 AddGNSS
Chapter 16 AddFilesystem
Chapter 17 AddSAT
Chapter 18 AddSSL
V 1. 04 2108. 12. 25
DeleteAT+CASSL
5. 2. 36 AT+CNACTCFG AddATCommand
5. 2. 37 AT+CTLIIC AddATCommand
5. 2. 38 AT+CWIIC AddATCommand
5. 2. 39 AT+CRIIC AddATCommand
5. 2. 40 AT+CMCFG AddATCommand
5. 2. 41 AT+CSIMLOCK AddATCommand
5. 2. 42 AT+CRATSRCH AddATCommand
5. 2. 43 AT+SPWM AddATCommand
5. 2. 44 AT+CASRIP AddATCommand
5. 2. 45 AT+CEDRX AddATCommand
6. 2. 7 AT+CEREG AddATCommand
9. 2. 10 AT+HTTPTOFSRL AddATCommand
13. 2. 16
AT+MIPLBOOTSTRAP
AddATCommand
13. 2. 17 +MIPLREAD AddATCommand
13. 2. 18 +MIPLWRITE AddATCommand
13. 2. 19 +MIPLEXECUTE AddATCommand
13. 2. 20 +MIPLOBSERVE AddATCommand
13. 2. 21 +MIPLDISCOVER AddATCommand
13. 2. 22
+MIPLPARAMETER
AddATCommand
13. 2. 23 +MIPLEVENT AddATCommand
15. 2. 13 AT+CGNSRTMS AddATCommand
18. 2. 2 AT+CASSLCFG ExtendATcommand
18. 2. 8 AT+CACFG AddATCommand
18. 2. 9 AT+CASWITCH AddATCommand
Chapter 19 AddPING
Chapter 20 AddSupportedUnsolicitedResultCodes
V 1. 05 2020. 01. 20
AT+CNBP DeleteATCommand
5. 2. 45 AT+CPSMRDP AddATCommand
5. 2. 46 AT+CPSMCFG AddATCommand
5. 2. 47 AT+CPSMCFGEXT AddATCommand
5. 2. 48 AT+CPSMSTATUS AddATCommand
49 AT+CEDRXRDP AddATCommand
50 AT+CRAI AddATCommand
14 AT+CGNSHOR AddATCommand
15 AT+CGNSUTIPR AddATCommand
16 AT+CGNSNMEA AddATCommand
17 AT+CGTP AddATCommand
18 AT+CGNSSUPLCFG AddATCommand
19 AT+CGNSSUPL AddATCommand
V 1. 06 2020. 07. 28 All
Contents.................................................................................................................................................
Contents
VersionHistory.....................................................................................................................................
Contents.................................................................................................................................................
1 Introduction..................................................................................................................................
1 1 Scopeofthedocument........................................................................................................................
1 2 Relateddocuments...............................................................................................................................
1 3 Conventionsandabbreviations..........................................................................................................
1 4 ATCommandsyntax............................................................................................................................
1 4 1 Basicsyntax...................................................................................................................................
1 4 2 SParametersyntax......................................................................................................................
1 4 3 ExtendedSyntax...........................................................................................................................
1 4 4 CombiningATcommandsonthesameCommandline........................................................
1 4 5 EnteringsuccessiveATcommandsonseparatelines...........................................................
1 5 Supportedcharactersets....................................................................................................................
1 6 Flowcontrol............................................................................................................................................
1 6 1 Softwareflowcontrol(XON/XOFFflowcontrol)......................................................................
1 6 2 Hardwareflowcontrol(RTS/CTSflowcontrol)........................................................................
1 7 Definitions...............................................................................................................................................
1 7 1 ParameterSavingMode..............................................................................................................
1 7 2 MaxResponseTime.....................................................................................................................
2 ATCommandsAccordingtoV. 25 TER...................................................................................
2 1 OverviewofATCommandsAccordingtoV. 25 TER........................................................................
2 2 DetailedDescriptionofATCommandsAccordingtoV. 25 TER.....................................................
2 2 1 A/ Re-issuestheLastCommandGiven.................................................................................
2 2 2 ATD MobileOriginatedCalltoDialANumber......................................................................
2 2 3 ATE SetCommandEchoMode..............................................................................................
2 2 4 ATH DisconnectExistingConnection.....................................................................................
2 2 5 ATI DisplayProductIdentificationInformation......................................................................
2 2 6 ATL SetMonitorspeakerloudness.........................................................................................
2 2 7 ATM SetMonitorSpeakerMode.............................................................................................
2 2 8 +++ SwitchfromDataModeorPPPOnlineModetoCommandMode...........................
2 2 9 ATO SwitchfromCommandModetoDataMode................................................................
2 2 10 ATQ SetResultCodePresentationMode.............................................................................
2 2 11 ATS 0 SetNumberofRingsbeforeAutomaticallyAnsweringtheCall..............................
2 2 12 ATS 3 SetCommandLineTerminationCharacter................................................................
2 2 13 ATS 4 SetResponseFormattingCharacter...........................................................................
2 2 14 ATS 5 SetCommandLineEditingCharacter.........................................................................
2 2 15 ATS 6 PauseBeforeBlindDialing...........................................................................................
2 2 16 ATS 7 SetNumberofSecondstoWaitforConnectionCompletion..................................
StringofDCommand................................................................................................................................... 2 2 17 ATS 8 SetNumberofSecondstoWaitforCommaDialModifierEncounteredinDial
2 2 18 ATS 10 SetDisconnectDelayafterIndicatingtheAbsenceofDataCarrier....................
2 2 19 ATV TAResponseFormat........................................................................................................
2 2 20 ATX SetCONNECTResultCodeFormatandMonitorCallProgress..............................
2 2 21 AT&C SetDCDFunctionMode...............................................................................................
2 2 22 AT&D SetDTRFunctionMode................................................................................................
2 2 23 AT&E SetCONNECTResultCodeFormatAboutSpeed..................................................
2 2 24 AT+GCAP RequestCompleteTACapabilitiesList..............................................................
2 2 25 AT+GMI RequestManufacturerIdentification.......................................................................
2 2 26 AT+GMM RequestTAModelIdentification............................................................................
2 2 27 AT+GMR RequestTARevisionIdentificationofSoftwareRelease..................................
2 2 28 AT+GOI RequestGlobalObjectIdentification......................................................................
2 2 29 AT+GSN RequestTASerialNumberIdentification(IMEI)..................................................
2 2 30 AT+ICF SetTE-TAControlCharacterFraming....................................................................
2 2 31 AT+IFC SetTE-TALocalDataFlowControl.........................................................................
2 2 32 AT+IPR SetTE-TAFixedLocalRate......................................................................................
3 ATCommandsAccordingto 3 GPPTS
3 1 OverviewofATCommandAccordingto 3 GPPTS
3 2 DetailedDescriptionsofATCommandAccordingto 3 GPPTS
3 2 1 AT+CGMI RequestManufacturerIdentification....................................................................
3 2 2 AT+CGMM RequestModelIdentification..............................................................................
3 2 3 AT+CGMR RequestTARevisionIdentificationofSoftwareRelease...............................
3 2 4 AT+CGSN RequestProductSerialNumberIdentification..................................................
3 2 5 AT+CSCS SelectTECharacterSet.......................................................................................
3 2 6 AT+CIMI RequestInternationalMobileSubscriberIdentity................................................
3 2 7 AT+CLCK FacilityLock.............................................................................................................
3 2 8 AT+CMEE ReportMobileEquipmentError...........................................................................
3 2 9 AT+COPS OperatorSelection.................................................................................................
3 2 10 AT+CPAS PhoneActivityStatus.............................................................................................
3 2 11 AT+CPIN EnterPIN...................................................................................................................
3 2 12 AT+CPWD ChangePassword.................................................................................................
3 2 13 AT+CRC SetCellularResultCodesforIncomingCallIndication.....................................
3 2 14 AT+CREG NetworkRegistration.............................................................................................
3 2 15 AT+CRSM RestrictedSIMAccess..........................................................................................
3 2 16 AT+CSQ SignalQualityReport...............................................................................................
3 2 17 AT+CPOL PreferredOperatorList..........................................................................................
3 2 18 AT+COPN ReadOperatorNames..........................................................................................
3 2 19 AT+CFUN SetPhoneFunctionality........................................................................................
3 2 20 AT+CCLK Clock.........................................................................................................................
3 2 21 AT+CSIM GenericSIMAccess................................................................................................
3 2 22 AT+CBC BatteryCharge..........................................................................................................
3 2 23 AT+CUSD UnstructuredSupplementaryServiceData.......................................................
3 2 24 AT+CNUM SubscriberNumber...............................................................................................
4 ATCommandsAccordingto 3 GPPTS
4 1 OverviewofATCommandsAccordingto 3 GPPTS
4 2 DetailedDescriptionsofATCommandsAccordingto 3 GPPTS
4 2 1 AT+CMGD DeleteSMSMessage...........................................................................................
4 2 2 AT+CMGF SelectSMSMessageFormat..............................................................................
4 2 3 AT+CMGL ListSMSMessagesfromPreferredStore.........................................................
4 2 4 AT+CMGR ReadSMSMessage.............................................................................................
4 2 5 AT+CMGS SendSMSMessage.............................................................................................
4 2 6 AT+CMGW WriteSMSMessagetoMemory........................................................................
4 2 7 AT+CMSS SendSMSMessagefromStorage.....................................................................
4 2 8 AT+CNMI NewSMSMessageIndications............................................................................
4 2 9 AT+CPMS PreferredSMSMessageStorage.......................................................................
4 2 10 AT+CRES RestoreSMSSettings...........................................................................................
4 2 11 AT+CSAS SaveSMSSettings................................................................................................
4 2 12 AT+CSCA SMSServiceCenterAddress...............................................................................
4 2 13 AT+CSDH ShowSMSTextModeParameters.....................................................................
4 2 14 AT+CSMP SetSMSTextModeParameters.........................................................................
4 2 15 AT+CSMS SelectMessageService.......................................................................................
5 ATCommandsSpecialforSIMCom.......................................................................................
5 1 Overview.................................................................................................................................................
5 2 DetailedDescriptionsofCommands.................................................................................................
5 2 1 AT+CPOWD Poweroff..............................................................................................................
5 2 2 AT+CADC ReadADC................................................................................................................
5 2 3 AT+CFGRI IndicateRIWhenUsingURC.............................................................................
5 2 4 AT+CLTS GetLocalTimestamp..............................................................................................
5 2 5 AT+CBAND GetandSetMobileOperationBand................................................................
5 2 6 AT+CNSMODShowNetworkSystemMode...........................................................................
5 2 7 AT+CSCLK ConfigureSlowClock..........................................................................................
5 2 8 AT+CCID ShowICCID..............................................................................................................
5 2 9 AT+CDEVICE ViewCurrentFlashDeviceType...................................................................
5 2 10 AT+GSV DisplayProductIdentificationInformation............................................................
5 2 11 AT+SGPIO ControltheGPIO..................................................................................................
5 2 12 AT+SLEDS SettheTimerPeriodofNetLight......................................................................
5 2 13 AT+CNETLIGHT ClosetheNetLightorOpenIttoShining...............................................
5 2 14 AT+CSGS NetlightIndicationofGPRSStatus.....................................................................
5 2 15 AT+CGPIO ControltheGPIObyPINIndex..........................................................................
5 2 16 AT+CBATCHK SetVBATCheckingFeatureON/OFF........................................................
5 2 17 AT+CNMP PreferredModeSelection....................................................................................
5 2 18 AT+CMNB PreferredSelectionbetweenCAT-MandNB-IoT............................................
5 2 19 AT+CPSMS PowerSavingModeSetting..............................................................................
5 2 20 AT+CEDRXS Extended-DRXSetting.....................................................................................
5 2 21 AT+CPSI InquiringUESystemInformation...........................................................................
5 2 22 AT+CGNAPN GetNetworkAPNinCAT-MOrNB-IOT.....................................................
5 2 23 AT+CSDP ServiceDomainPreference...............................................................................
5 2 24 AT+MCELLLOCKLockthespecialCAT-Mcell.....................................................................
5 2 25 AT+NCELLLOCKLockthespecialNB-IOTcell....................................................................
5 2 26 AT+NBSC ConfigureNB-IOTScramblingFeature............................................................
5 2 27 AT+CAPNMODE SelecttheModeofApplicationConfigureAPN..................................
5 2 28 AT+CRRCSTATE QueryRRCState....................................................................................
5 2 29 AT+CBANDCFG ConfigureCAT-MOrNB-IOTBand.......................................................
5 2 30 AT+CNACT APPNetworkActive..........................................................................................
5 2 31 AT+CNCFG PDPConfigure...................................................................................................
5 2 32 AT+CEDUMP SetWhethertheModuleResetWhenTheModuleisCrashed.............
5 2 33 AT+CNBS ConfigureBandScanOptimizationForNB-IOT.............................................
5 2 34 AT+CNDS ConfigureServiceDomainPreferenceForNB-IOT......................................
5 2 35 AT+CENG SwitchOnorOffEngineeringMode.................................................................
5 2 36 AT+CNACTCFG ConfigureIPProtocolType......................................................................
5 2 37 AT+CTLIIC ControltheSwitchofIIC....................................................................................
5 2 38 AT+CWIIC WriteValuestoRegisterofIICDevice.............................................................
5 2 39 AT+CRIIC ReadValuesfromRegisterofIICDevice.........................................................
5 2 40 AT+CMCFG ManageMobileOperatorConfiguration........................................................
5 2 41 AT+CSIMLOCK SIMLock......................................................................................................
5 2 42 AT+CRATSRCH ConfigureParameterforBetterRATSearch........................................
5 2 43 AT+SPWM GeneratethePulse-Width-Modulation............................................................
5 2 44 AT+CASRIP ShowRemoteIPaddressandPortWhenReceivedData........................
5 2 45 AT+CEDRX ConfigureEDRXparameters...........................................................................
5 2 46 AT+CPSMRDP ReadPSMDynamicParameters.............................................................
5 2 47 AT+CPSMCFG ConfigurePSMversionandMinimumThresholdValue.......................
5 2 48 AT+CPSMCFGEXT ConfigureModemOptimizationofPSM..........................................
5 2 49 AT+CPSMSTATUS EnableDeepSleepWakeupIndication............................................
5 2 50 AT+CEDRXRDP eDRXReadDynamicParameters.........................................................
5 2 51 AT+CRAI ConfigureReleaseAssistanceIndicationinNB-IOTnetwork........................
6 ATCommandsforGPRSSupport........................................................................................
6 1 Overview..............................................................................................................................................
6 2 DetailedDescriptionsofATCommandsforGPRSSupport.......................................................
6 2 1 AT+CGATT AttachorDetachfromGPRSService............................................................
6 2 2 AT+CGDCONT DefinePDPContext...................................................................................
6 2 3 AT+CGACT PDPContextActivateorDeactivate..............................................................
6 2 4 AT+CGPADDR ShowPDPAddress.....................................................................................
6 2 5 AT+CGREG NetworkRegistrationStatus...........................................................................
6 2 6 AT+CGSMS SelectServiceforMOSMSMessages........................................................
6 2 7 AT+CEREG EPSNetworkRegistrationStatus..................................................................
7 ATCommandsforIPApplication.........................................................................................
7 1 Overview..............................................................................................................................................
7 2 DetailedDescriptionsofCommands...............................................................................................
7 2 1 AT+SAPBR BearerSettingsforApplicationsBasedonIP...............................................
8 ATCommandsforTCPIPApplicationToolkit...................................................................
8 1 Overview..............................................................................................................................................
8 2 DetailedDescriptionsofCommands...............................................................................................
8 2 1 AT+CIPMUX StartUpMulti-IPConnection.........................................................................
8 2 2 AT+CIPSTART StartUpTCPorUDPConnection.............................................................
8 2 3 AT+CIPSEND SendDataThroughTCPorUDPConnection..........................................
8 2 4 AT+CIPQSEND SelectDataTransmittingMode................................................................
8 2 5 AT+CIPACK QueryPreviousConnectionDataTransmittingState................................
8 2 6 AT+CIPCLOSE CloseTCPorUDPConnection................................................................
8 2 7 AT+CIPSHUT DeactivateGPRSPDPContext..................................................................
8 2 8 AT+CLPORT SetLocalPort..................................................................................................
8 2 9 AT+CSTT StartTaskandSetAPN,USERNAME,PASSWORD...................................
8 2 10 AT+CIICR BringUpWirelessConnectionwithGPRS......................................................
8 2 11 AT+CIFSR GetLocalIPAddress..........................................................................................
8 2 12 AT+CIFSREX GetLocalIPAddressextend.......................................................................
8 2 13 AT+CIPSTATUS QueryCurrentConnectionStatus..........................................................
8 2 14 AT+CDNSCFG ConfigureDomainNameServer..............................................................
8 2 15 AT+CDNSGIP QuerytheIPAddressofGivenDomainName........................................
8 2 16 AT+CIPHEAD AddanIPHeadattheBeginningofaPackageReceived.....................
8 2 17 AT+CIPATS SetAutoSendingTimer...................................................................................
8 2 18 AT+CIPSPRT SetPromptof‘>’WhenModuleSendsData............................................
8 2 19 AT+CIPSERVER ConfigureModuleasServer..................................................................
8 2 20 AT+CIPCSGP SetGPRSforConnectionMode.................................................................
8 2 21 AT+CIPSRIP ShowRemoteIPAddressandPortWhenReceivedData......................
8 2 22 AT+CIPDPDP SetWhethertoCheckStateofGPRSNetworkTiming..........................
8 2 23 AT+CIPMODE SelectTCPIPApplicationMode.................................................................
8 2 24 AT+CIPCCFG ConfigureTransparentTransferMode......................................................
8 2 25 AT+CIPSHOWTP DisplayTransferProtocolinIPHeadWhenReceivedData...........
8 2 26 AT+CIPUDPMODE UDPExtendedMode...........................................................................
8 2 27 AT+CIPRXGET GetDatafromNetworkManually.............................................................
8 2 28 AT+CIPRDTIMER SetRemoteDelayTimer.......................................................................
8 2 29 AT+CIPSGTXT SelectGPRSPDPcontext........................................................................
8 2 30 AT+CIPSENDHEX SetCIPSENDDataFormattoHex....................................................
8 2 31 AT+CIPHEXS SetOutput-dataFormatwithsuffix.............................................................
8 2 32 AT+CIPTKA SetTCPKeepaliveParameters......................................................................
8 2 33 AT+CIPOPTION EnableorDisableTCPnaglealgorithm................................................
9 ATCommandsforHTTP (S) Application.............................................................................
9 1 Overview..............................................................................................................................................
9 2 DetailedDescriptionsofCommands...............................................................................................
9 2 1 AT+SHSSL SelectSSLConfigure........................................................................................
9 2 2 AT+SHCONF SetHTTP(S)Parameter................................................................................
9 2 3 AT+SHCONN HTTP(S)Connection.....................................................................................
9 2 4 AT+SHBOD SetBody.............................................................................................................
9 2 5 AT+SHBODEXT SetExtensionBody..................................................................................
9 2 6 AT+SHAHEAD AddHead.......................................................................................................
9 2 7 AT+SHCHEAD ClearHead....................................................................................................
9 2 8 AT+SHPARA SetHTTP(S)Para...........................................................................................
9 2 9 AT+SHCPARA ClearHTTP(S)Para..................................................................................
9 2 10 AT+SHSTATE QueryHTTP(S)ConnectionStatus............................................................
9 2 11 AT+SHREQ SetRequestType.............................................................................................
9 2 12 AT+SHREAD ReadResponseValue...................................................................................
9 2 13 AT+SHDISC DisconnectHTTP(S)........................................................................................
9 2 14 AT+HTTPTOFS DownloadFiletoAPFileSystem............................................................
9 2 15 AT+HTTPTOFSRL StateofDownloadFiletoAPFileSystem........................................
10 ATCommandsforFTPApplication..............................................................................
10 1 Overview..............................................................................................................................................
10 2 DetailedDescriptionsofCommands...............................................................................................
10 2 1 AT+FTPPORT SetFTPControlPort....................................................................................
10 2 2 AT+FTPMODE SetActiveorPassiveFTPMode..............................................................
10 2 3 AT+FTPTYPE SettheTypeofDatatoBeTransferred.....................................................
10 2 4 AT+FTPPUTOPT SetFTPPutType....................................................................................
10 2 5 AT+FTPCID SetFTPBearerProfileIdentifier....................................................................
10 2 6 AT+FTPREST SetResumeBrokenDownload..................................................................
10 2 7 AT+FTPSERV SetFTPServerAddress..............................................................................
10 2 8 AT+FTPUN SetFTPUserName..........................................................................................
10 2 9 AT+FTPPW SetFTPPassword............................................................................................
10 2 10 AT+FTPGETNAME SetDownloadFileName............................................................
10 2 11 AT+FTPGETPATH SetDownloadFilePath...............................................................
10 2 12 AT+FTPPUTNAME SetUploadFileName.................................................................
10 2 13 AT+FTPPUTPATH SetUploadFilePath.....................................................................
10 2 14 AT+FTPGET DownloadFile..........................................................................................
10 2 15 AT+FTPPUT SetUploadFile.........................................................................................
10 2 16 AT+FTPDELE DeleteSpecifiedFileinFTPServer...................................................
10 2 17 AT+FTPSIZE GettheSizeofSpecifiedFileinFTPServer.....................................
10 2 18 AT+FTPSTATE GettheFTPState...............................................................................
10 2 19 AT+FTPEXTPUTExtendUploadFile.............................................................................
10 2 20 AT+FTPMKD MakeDirectoryontheRemoteMachine............................................
10 2 21 AT+FTPRMD RemoveDirectoryontheRemoteMachine.......................................
10 2 22 AT+FTPLIST ListContentsofDirectoryontheRemoteMachine..........................
10 2 23 AT+FTPEXTGET ExtendDownloadFile.....................................................................
10 2 24 AT+FTPETPUT UploadFile...........................................................................................
10 2 25 AT+FTPETGET DownloadFile.....................................................................................
10 2 26 AT+FTPQUIT QuitCurrentFTPSession....................................................................
10 2 27 AT+FTPRENAME RenametheSpecifiedFileontheRemoteMachine................
RemoteMachine......................................................................................................................................... 10 2 28 AT+FTPMDTM Get theLast Modification Timestamp of Specified File onthe
11 ATCommandforNTPfunction......................................................................................
11 1 Overview..............................................................................................................................................
11 2 DetailedDescriptionsofCommands...............................................................................................
11 2 1 AT+CNTPCID SetGPRSBearerProfile’sID.....................................................................
11 2 2 AT+CNTP SynchronizeNetworkTime.................................................................................
12 ATCommandsforOneNetApplication........................................................................
12 1 Overview..............................................................................................................................................
12 2 DetailedDescriptionsofCommands...............................................................................................
12 2 1 AT+MIPLCREATE CreateOneNetconfiguration...............................................................
12 2 2 AT+MIPLDELETE DeleteOneNetconfiguration................................................................
12 2 3 AT+MIPLOPEN ConnecttoOneNet....................................................................................
12 2 4 AT+MIPLADDOBJ Addobject...............................................................................................
12 2 5 AT+MIPLDELOBJ DeleteObject..........................................................................................
12 2 6 AT+MIPLCLOSE DisconnecttoOneNet.............................................................................
12 2 7 AT+MIPLNOTIFY NotifyDatatoOneNet............................................................................
12 2 8 AT+MIPLREADRSP SendResponseonReadCommand..............................................
12 2 9 AT+MIPLWRITERSP SendResponseonWriteCommand.............................................
12 2 10 AT+MIPLEXECUTERSP SendResponseonExecuteCommand.........................
12 2 11 AT+MIPLOBSERVERSP SendResponseOnObserveCommand.......................
12 2 12 AT+MIPLDISCOVERRSP SendResponseonDiscoverCommand......................
12 2 13 AT+MIPLPARAMETERRSP SendResponseonParameterCommand...............
12 2 14 AT+MIPLUPDATE UpdateRegistration.......................................................................
12 2 15 AT+MIPLVER VersionofOneNetSDK........................................................................
12 2 16 AT+MIPLBOOTSTRAP BootstrapMode.....................................................................
12 2 17 +MIPLREAD ReadRequesttoUser............................................................................
12 2 18 +MIPLWRITE WriteRequesttoUser...........................................................................
12 2 19 +MIPLEXECUTE ExecuteRequesttoUser...............................................................
12 2 20 +MIPLOBSERVE ObserveRequesttoUser..............................................................
12 2 21 +MIPLDISCOVER DiscoverRequesttoUser............................................................
12 2 22 +MIPLPARAMETER SetParameterRequesttoUser..............................................
12 2 23 +MIPLEVENT EventIndicationtoUser.......................................................................
13 ATCommandsforTelecomIOTApplication..............................................................
13 1 Overview..............................................................................................................................................
13 2 DetailedDescriptionsofCommands...............................................................................................
13 2 1 AT+SIMLCREATE CreateConfiguration.............................................................................
13 2 2 AT+SIMLMODE ConnectionMode.......................................................................................
13 2 3 AT+SIMLOPEN ConnecttoTelecomIOT............................................................................
13 2 4 AT+SIMLSEND SendDatatoTelecomIOT........................................................................
13 2 5 AT+SIMLCLOSE DisconnecttoTelecomIOT....................................................................
14 ATCommandsforGNSSApplication...........................................................................
14 1 Overview..............................................................................................................................................
14 2 DetailedDescriptionsofCommands...............................................................................................
14 2 1 AT+CGNSPWR GNSSPowerControl.................................................................................
14 2 2 AT+CGNSINF GNSSNavigationInformationParsedFromNMEASentences...........
14 2 3 AT+CGNSURC GNSSNavigationURCReport.................................................................
14 2 4 AT+CGNSPORT GNSSNMEAOutPortSet......................................................................
14 2 5 AT+CGNSCOLD GNSSColdStart......................................................................................
14 2 6 AT+CGNSWARM GNSSWarmStart...................................................................................
14 2 7 AT+CGNSHOT GNSSHotStart...........................................................................................
14 2 8 AT+CGNSMOD GNSSWorkModeSet..............................................................................
14 2 9 AT+CGNSCFG GNSSNMEAOutConfigure.....................................................................
14 2 10 AT+CGNSTST GNSSNMEADataOutputtoATPort...............................................
14 2 11 AT+CGNSXTRA GNSSXTRAFunctionOpen...........................................................
14 2 12 AT+CGNSCPY GNSSXTRAFileCopy.......................................................................
14 2 13 AT+CGNSRTMS GNSSNMEAOutFrequencyConfigure......................................
14 2 14 AT+CGNSHOR ConfigurePositioningDesiredAccuracy......................................
14 2 15 AT+CGNSUTIPR ConfigureBaudRateWhenNMEAOutputfromUART
14 2 16 AT+CGNSNMEA ConfigureNMEAOutputSentences.............................................
14 2 17 AT+CGTP IZATGNSSConfigure.................................................................................
14 2 18 AT+CGNSSUPLCFG GNSSSUPLConfigure..........................................................
14 2 19 AT+CGNSSUPL GNSSSUPLControl.......................................................................
15 ATCommandsforFileSystem......................................................................................
15 1 Overview..............................................................................................................................................
15 2 DetailedDescriptionsofCommands...............................................................................................
15 2 1 AT+CFSINIT GetFlashDataBuffer.....................................................................................
15 2 2 AT+CFSWFILE WriteFiletotheFlashBufferAllocatedbyCFSINIT.............................
15 2 3 AT+CFSRFILE ReadFilefromFlash...................................................................................
15 2 4 AT+CFSDFILE DeletetheFilefromtheFlash...................................................................
15 2 5 AT+CFSGFIS GetFileSize...................................................................................................
15 2 6 AT+CFSREN RenameaFile.................................................................................................
15 2 7 AT+CFSGFRS GettheSizeofFileSystem........................................................................
15 2 8 AT+CFSTERM FreetheFlashBufferAllocatedbyCFSINIT...........................................
15 2 9 AT+CBAINIT InitializetheAPBackupFileSystem............................................................
15 2 10 AT+CBALIST SetthefilesWhichWanttoBackup....................................................
15 2 11 AT+CBAPPS StarttoBackupAPFileSystemAllocatedbyCBAINITandCBALIST
15 2 12 AT+CBART RestoretheFileintoAPFileSystem......................................................
16 ATCommandsforSIMApplicationToolkit.................................................................
16 1 Overview..............................................................................................................................................
16 2 DetailedDescriptionsofCommands...............................................................................................
16 2 1 AT+STIN SATIndication.........................................................................................................
16 2 2 AT+STGI GetSATInformation..............................................................................................
16 2 3 AT+STGR SATRespond........................................................................................................
16 2 4 AT+STK STKSwitch...............................................................................................................
17 ATCommandsforSSLApplication..............................................................................
17 1 OverviewofATCommandsforSSLApplication...........................................................................
17 2 DetailedDescriptionsofATCommandsforSSLApplication......................................................
17 2 1 AT+CSSLCFG ConfigureSSLParametersofContextIdentifier.....................................
18 ATCommandsforTCP/UDPApplication....................................................................
18 1 Overview..............................................................................................................................................
18 2 DetailedDescriptionsofCommands...............................................................................................
18 2 1 AT+CACID SetTCP/UDPIdentifier......................................................................................
18 2 2 AT+CASSLCFG SetSSLCertificateandTimeoutParameters.......................................
18 2 3 AT+CAOPEN OpenaTCP/UDPConnection.....................................................................
18 2 4 AT+CASERVER OpenaTCP/UDPServer.........................................................................
18 2 5 AT+CASEND SendDataviaanEstablishedConnection................................................
18 2 6 AT+CARECV ReceiveDataviaanEstablishedConnection...........................................
18 2 7 AT+CAACK QuerySendDataInformation.........................................................................
18 2 8 AT+CASTATE QueryTCP/UDPConnectionState............................................................
18 2 9 AT+CACLOSE CloseaTCP/UDPConnection...................................................................
18 2 10 AT+CACFG ConfigureTransparentTransmissionParameters...............................
18 2 11 AT+CASWITCH SwitchtoTransparentTransportMode..........................................
19 ATCommandsforPING...................................................................................................
19 1 Overview..............................................................................................................................................
19 2 DetailedDescriptionsofCommands...............................................................................................
19 2 1 AT+SNPING 4 SendsanIPv 4 ping.......................................................................................
19 2 2 AT+SNPING 6 SendsanIPv 6 ping.......................................................................................
20 SupportedErrorCodesandUnsolicitedResultCodes..........................................
20 1 SummaryofCMEERRORCodes...................................................................................................
20 2 SummaryofCMSERRORCodes...................................................................................................
20 3 SummaryofUnsolicitedResultCodes...........................................................................................
THISDOCUMENTISAREFERENCEGUIDETOALLTHEATCOMMANDS.
1 Introduction..................................................................................................................................
1 1 Scopeofthedocument........................................................................................................................
ThisdocumentpresentstheATCommandSetforSIMComSIM 7000 Series,includingSIM 7000 A,SIM 700 C,
SIM 7000 E,SIM 7000 C-N,SIM 7000 E-N,SIM 7000 JCandSIM 7000 G.

1 2 Relateddocuments...............................................................................................................................
YoucanvisittheSIMComWebsiteusingthefollowinglink:
http://www.simcom.com

1 3 Conventionsandabbreviations..........................................................................................................
Inthisdocument,theGSMenginesarereferredtoasfollowingterm:
ME(MobileEquipment);
MS(MobileStation);
TA(TerminalAdapter);
DCE(DataCommunicationEquipment)orfacsimileDCE(FAXmodem,FAXboard);

Inapplication,controllingdevicecontrolstheGSMenginebysendingATCommandviaitsserialinterface.
Thecontrollingdeviceattheotherendoftheseriallineisreferredtoasfollowingterm:
TE(TerminalEquipment);
DTE(DataTerminalEquipment)orplainly"theapplication"whichisrunningonanembeddedsystem;

1 4 ATCommandsyntax............................................................................................................................
The"AT"or"at"or"aT"or"At"prefixmustbesetatthebeginningofeachCommandline.Toterminatea

Commandlineenter .
Commandsareusuallyfollowedbyaresponsethatincludes. ""
Throughoutthisdocument,onlytheresponsesarepresented,< CR> areomittedintentionally.

TheATCommandsetimplementedbySIM 7080 Seriesisacombinationof 3 GPPTS 27. 005 , 3 GPPTS

007 andITU-TrecommendationV. 25 terandtheATcommandsdevelopedbySIMCom.
OnlyenterATCommandthroughserialportafterSIM 7080 SeriesispoweredonandUnsolicitedResult
Code"RDY"isreceivedfromserialport.Ifauto-baudingisenabled,theUnsolicitedResultCodes
"RDY"andsoonarenotindicatedwhenyoustartuptheME,andthe"AT"prefix,or"at"prefixmustbe
setatthebeginningofeachcommandline.

All theseAT commands canbe split into threecategories syntactically:" basic "," S parameter ", and
" extended ".Theseareasfollows:

1 4 1 Basicsyntax...................................................................................................................................
TheseATcommandshavetheformatof" AT ",or" AT& ",where" "istheCommand,and
" "is/aretheargument(s)for thatCommand.An example ofthis is " ATE ",which tellstheDCE
whetherreceivedcharactersshouldbeechoedbacktotheDTEaccordingtothevalueof" "." "is
optionalandadefaultwillbeusedifmissing.

1 4 2 SParametersyntax......................................................................................................................
TheseATcommandshavetheformatof" ATS = ",where" "istheindexofthe S registertoset,
and " " isthevaluetoassigntoit." "isoptional;ifitismissing,thenadefaultvalueisassigned.

1 4 3 ExtendedSyntax...........................................................................................................................
Thesecommandscanoperateinseveralmodes,asinthefollowingtable:

Table 1 :TypesofATcommandsandresponses
TestCommand

AT+=?

Themobileequipmentreturns thelistofparametersandvalue
rangessetwiththecorrespondingWriteCommandorbyinternal
processes.
ReadCommand

AT+?

Thiscommandreturnsthecurrentlysetvalueoftheparameteror
parameters.
NOTE
WriteCommand

AT+=<...> Thiscommandsetstheuser-definableparametervalues.

ExecutionCommand

AT+

Theexecutioncommandreadsnon-variableparametersaffected
byinternalprocessesintheGSMengine.
1 4 4 CombiningATcommandsonthesameCommandline........................................................
YoucanenterseveralATcommandsonthesameline.Inthiscase,youdonotneedtotypethe" AT "or" at "
prefixbeforeeverycommand.Instead,youonlyneedtype" AT "or" at "thebeginningofthecommandline.
Pleasenotetouseasemicolonasthecommanddelimiterafteranextendedcommand;inbasicsyntaxorS
parameter syntax, the semicolon need not enter, for example:
ATE 1 Q 0 S 0 = 1 S 3 = 13 V 1 X 4 ;+IFC= 0 , 0 ;+IPR= 115200.

TheCommandlinebuffercanacceptamaximumof 559 characters(countedfromthefirstcommand
without"AT"or"at"prefix)or 39 ATcommands.Ifthecharactersenteredexceededthisnumberthennone
oftheCommandwillexecutedandTAwillreturn" ERROR ".

1 4 5 EnteringsuccessiveATcommandsonseparatelines...........................................................
WhenyouneedtoenteraseriesofATcommandsonseparatelines,pleaseNotethatyouneedtowaitthe
finalresponse(forexampleOK,CMEerror,CMSerror)oflastATCommandyouenteredbeforeyouenter
thenextATCommand.

1 5 Supportedcharactersets....................................................................................................................
TheSIM 7080 SeriesAT Commandinterfacedefaults tothe IRA character set.The SIM 7080 Series
supportsthefollowingcharactersets:
GSMformat
UCS 2
IRA
Thecharactersetcanbesetandinterrogatedusingthe"AT+CSCS"Command( 3 GPPTS 27. 007 ). The
charactersetisdefinedinGSMspecification 3 GPPTS 27. 005.

ThecharactersetaffectstransmissionandreceptionofSMSandSMSCellBroadcastmessages,theentry
anddisplayofphonebookentriestextfieldandSIMApplicationToolkitalphastrings.

1 6 Flowcontrol............................................................................................................................................
FlowcontrolisveryimportantforcorrectcommunicationbetweentheGSMengineandDTE.Forinthe
casesuchasadataorfaxcall,thesendingdeviceistransferringdatafasterthanthereceivingsideisready
toaccept.Whenthereceivingbufferreachesitscapacity,thereceivingdeviceshouldbecapabletocause
thesendingdevicetopauseuntilitcatchesup.

Therearebasicallytwoapproachestoachievedataflowcontrol:softwareflowcontrolandhardwareflow
control.SIM 7080 Seriessupportbothtwokindsofflowcontrol.
InMultiplexmode,itisrecommendedtousethehardwareflowcontrol.

1 6 1 Softwareflowcontrol(XON/XOFFflowcontrol)......................................................................
Softwareflowcontrolsendsdifferentcharacterstostop(XOFF,decimal 19 )andresume(XON,decimal 17 )
dataflow.Itisquiteusefulinsomeapplicationsthatonlyusethreewiresontheserialinterface.

ThedefaultflowcontrolapproachofSIM 7080 Seriesishardwareflowcontrol(RTS/CTSflowcontrol),to
enablesoftwareflowcontrolintheDTEinterfaceandwithinGSMengine,typethefollowingATCommand:
AT+IFC= 1 , 1

Ensurethatanycommunicationssoftwarepackage(e.g.Hyperterminal)usessoftwareflowcontrol.

SoftwareFlowcontrol shouldnotbeusedfor data calls wherebinary data willbe transmittedor
received(e.g.TCP/IP)astheDTEinterfacemayinterpretbinarydataasflowcontrolcharacters.

1 6 2 Hardwareflowcontrol(RTS/CTSflowcontrol)........................................................................
Hardwareflowcontrol achievesthedataflowcontrol bycontrollingtheRTS/CTSline.Whenthedata
transfershouldbesuspended,theCTSlineissetinactiveuntilthetransferfromthereceivingbufferhas
completed.Whenthereceivingbufferisoktoreceivemoredata,CTSgoesactiveonceagain.

Toachievehardwareflowcontrol,ensurethattheRTS/CTSlinesarepresentonyourapplicationplatform.

NOTE
1 7 Definitions...............................................................................................................................................
1 7 1 ParameterSavingMode..............................................................................................................
Forthepurposesofthepresentdocument,thefollowingsyntacticaldefinitionsapply:
 NO_SAVE :TheparameterofthecurrentATcommandwillbelostifmoduleisrebootedorcurrentAT
commanddoesn'thaveparameter.
 AUTO_SAVE :TheparameterofthecurrentATcommandwillbekeptinNVRAMautomaticallyand
takeineffectimmediately,anditwon'tbelostifmoduleisrebooted.
 AUTO_SAVE_REBOOT : The parameter of the current AT command will be kept in NVRAM
automaticallyandtakeineffectafterreboot,anditwon'tbelostifmoduleisrebooted.
 - :"-"meansthisATcommanddoesn'tcaretheparametersavingmode.

1 7 2 MaxResponseTime.....................................................................................................................
Maxresponsetimeisestimatedmaximumtimetogetresponse,theunitisseconds.
"-"meansthisATcommanddoesn'tcaretheresponsetime.

2 ATCommandsAccordingtoV. 25 TER...................................................................................
TheseAT Commands are designed according to the ITU-T (International Telecommunication Union,
Telecommunicationsector)V. 25 terdocument.

2 1 OverviewofATCommandsAccordingtoV. 25 TER........................................................................
Command Description
A/ Re-issuesthelastcommandgiven
ATD Mobileoriginatedcalltodialanumber
ATE Setcommandechomode
ATH Disconnectexistingconnection

ATI Displayproductidentificationinformation
ATL Setmonitorspeakerloudness
ATM Setmonitorspeakermode
+++ Switchfromdatamodeorppponlinemodetocommandmode

ATO Switchfromcommandmodetodatamode
ATQ Setresultcodepresentationmode
ATS 0 Setnumberofringsbeforeautomaticallyansweringthecall
ATS 3 Setcommandlineterminationcharacter

ATS 4 Setresponseformattingcharacter
ATS 5 Setcommandlineeditingcharacter
ATS 6 Pausebeforeblinddialing
ATS 7 Setnumberofsecondstowaitforconnectioncompletion

ATS 8
Setnumberofsecondstowaitforcommadialmodifierencounteredindial
stringofDcommand
ATS 10 Setdisconnectdelayafterindicatingtheabsenceofdatacarrier
ATV TAresponseformat
ATX Setconnectresultcodeformatandmonitorcallprogress

ATZ Resetdefaultconfiguration
AT&C SetDCDfunctionmode
AT&D SetDTRfunctionmode
AT&F Factorydefinedconfiguration

AT&V Displaycurrentconfiguration
AT&E SetCONNECTResultCodeFormatAboutSpeed

AT+GCAP RequestcompleteTAcapabilitieslist
AT+GMI Requestmanufactureridentification

AT+GMM RequestTAmodelidentification
AT+GMR RequestTArevisionidentificationofsoftwarerelease
AT+GOI Requestglobalobjectidentification
AT+GSN RequestTAserialnumberidentification(IMEI)

AT+ICF SetTE-TAcontrolcharacterframing
AT+IFC SetTE-TAlocaldataflowcontrol
AT+IPR SetTE-TAfixedlocalrate

2 2 DetailedDescriptionofATCommandsAccordingtoV. 25 TER.....................................................
2 2 1 A/ Re-issuestheLastCommandGiven.................................................................................
A/ Re-issuestheLastCommandGiven
ExecutionCommand

A/

Response
Re-issuesthepreviousCommand
Reference
V. 25 ter

Note
2 2 2 ATD MobileOriginatedCalltoDialANumber......................................................................
ATD MobileOriginatedCalltoDialANumber
ExecutionCommand
ATD[<mgsm]

Response
Thiscommandcanbeusedtosetupoutgoingdatacalls.Italsoservesto
controlsupplementaryservices.
Note: This command may be aborted generally by receiving an ATH
Commandor acharacter duringexecution.Theabortingisnotpossible
duringsomestatesofconnectionestablishmentsuchashandshaking.
IferrorisrelatedtoMEfunctionality
+CMEERROR:<err>
Ifnodialtoneand(parametersetting ATX 2 or ATX 4 )
NODIALTONE
Ifbusyand(parametersetting ATX 3 or ATX 4 )
BUSY
Ifaconnectioncannotbeestablished
NOCARRIER
Iftheremotestationdoesnotanswer
NOANSWER
Ifconnectionsuccessfulandnon-voicecall.
CONNECT<text> TAswitchestodatamode.
Note: <text> output only if ATX<value> parameter setting with the
<value> > 0
WhenTAreturnstocommandmodeaftercallrelease
OK
Parameters
<n> StringofdialingdigitsandoptionallyV. 25 termodifiersdialing
digits: 0 - 9 ,*,#,+,A,B,C
FollowingV. 25 termodifiersareignored:
,(comma),T,P,!,W,@
Emergencycall:
Standardizedemergencynumber 112 (noSIMneeded)
Stringof GSM modifiers:
I Actives CLIR (Disablespresentationofownnumberto
calledparty)
i Deactivates CLIR (Enablepresentationofownnumber
tocalledparty)
G ActivatesClosedUserGroupinvocationforthiscallonly
g DeactivatesClosedUserGroupinvocationforthiscall
only
ParameterSavingMode NO_SAVE
MaxResponseTime TimeoutsetwithATS 7 (datacall)

Reference
V. 25 ter

Note
2 2 3 ATE SetCommandEchoMode..............................................................................................
ATE SetCommandEchoMode
ExecutionCommand
Response
ThissettingdetermineswhetherornottheTAechoescharactersreceived

ATE fromTEduringCommandstate.
OK
Parameters
0 Echomodeoff
1 Echomodeon
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
V. 25 ter

Note
2 2 4 ATH DisconnectExistingConnection.....................................................................................
ATH DisconnectExistingConnection
ExecutionCommand
ATH

Response
DisconnectexistingcallbylocalTEfromCommandlineandterminatecall
OK
Note:OKisissuedaftercircuit 109 (DCD)isturnedoff,ifitwaspreviously
on.
ParameterSavingMode NO_SAVE

MaxResponseTime 20 s
Reference
V. 25 ter

Note
2 2 5 ATI DisplayProductIdentificationInformation......................................................................
ATI DisplayProductIdentificationInformation
ExecutionCommand

ATI

Response
TAissuesproductinformationtext
Example:
SIM 7000 R 1351
OK
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
V. 25 ter

Note
2 2 6 ATL SetMonitorspeakerloudness.........................................................................................
ATL SetMonitorspeakerloudness
ExecutionCommand

ATL

Response
OK
Parameters
0 .. 3 Volume
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference
V. 25 ter

Note
NoeffectinGSM
2 2 7 ATM SetMonitorSpeakerMode.............................................................................................
ATM SetMonitorSpeakerMode
ExecutionCommand

ATM

Response
OK
Parameters
0 .. 2 Mode
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
V. 25 ter

Note
NoeffectinGSM
2 2 8 +++ SwitchfromDataModeorPPPOnlineModetoCommandMode...........................
+++ SwitchfromDataModeorPPPOnlineModetoCommandMode
ExecutionCommand

+++

Response
The +++ charactersequencecausestheTAtocancelthedataflowoverthe
ATinterfaceandswitchtoCommandmode.Thisallows youtoenterAT
Commandwhilemaintainingthedataconnectiontotheremoteserver.
OK
Topreventthe +++ escapesequencefrombeingmisinterpretedasdata,it
shouldcomplytofollowingsequence:
NocharactersenteredforT 1 time( 1 second)
"+++"charactersenteredwithnocharactersinbetween( 1 second)
NocharactersenteredforT 1 timer( 1 second)
SwitchtoCommandmode,otherwisegotostep 1.
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference
V. 25 ter

Note
ToreturnfromCommandmodebacktodatamode:Enter ATO.
2 2 9 ATO SwitchfromCommandModetoDataMode................................................................
ATO SwitchfromCommandModetoDataMode
ExecutionCommand

ATO[n]

Response
TAresumestheconnectionandswitchesbackfromcommandmodetodata
mode.
CONNECT
Ifconnectionisnotsuccessfullyresumed
ERROR
else
TAreturnstodatamodefromcommandmode CONNECT
Note:< text >onlyifparametersetting ATX> 0
Parameter
0 Switchfromcommandmodetodatamode.
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
V. 25 ter

Note
2 2 10 ATQ SetResultCodePresentationMode.............................................................................
ATQ SetResultCodePresentationMode
ExecutionCommand
ATQ

Response
This parameter setting determines whether or not theTAtransmitsany
result code to the TE. Information text transmitted in response is not
affectedbythissetting.
If< n >= 0 :
OK
If< n >= 1 :
(none)
Parameters
<n> 0 TAtransmitsresultcode
1 Resultcodesaresuppressedandnottransmitted
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
V. 25 ter

Note
2 2 11 ATS 0 SetNumberofRingsbeforeAutomaticallyAnsweringtheCall..............................
ATS 0 SetNumberofRingsbeforeAutomaticallyAnsweringtheCall
ReadCommand

ATS 0?

Response
<n>
OK
Parameters
SeeWriteCommand
WriteCommand

ATS 0 =

Response
Thisparametersettingdeterminesthenumberofringsbeforeauto-answer.
OK
or
ERROR
Parameters
0 Automaticansweringisdisable.
1 - 255 Numberofringsthemodemwillwaitforbeforeanswering
thephoneifaringisdetected.
ParameterSavingMode -
MaxResponseTime -

Reference
V. 25 ter

Note
If<n>issettoohigh,thecallingpartymayhangupbeforethecallcanbe
answeredautomatically.
Ifusingcmuxport,ATHandAT+CHUPcanhangupthecall(automatically
answering)onlyintheCMUXchannel 0.
Ifusingdual-physicalserialport,ATHandAT+CHUPcanhangupthecall
(automaticallyanswering)onlyinUART 1.
2 2 12 ATS 3 SetCommandLineTerminationCharacter................................................................
ATS 3 SetCommandLineTerminationCharacter
ReadCommand

ATS 3?

Response
<n>
OK
Parameters
SeeWriteCommand
WriteCommand
ATS 3 =

Response
This parameter setting determines the character recognized by TA to
terminateanincomingcommandline.TheTAalsoreturnsthischaracterin
output.
OK
or
ERROR
Parameters
13 Commandlineterminationcharacter
ParameterSavingMode -
MaxResponseTime -
Reference
V. 25 ter

Note
Default 13 =CR.Itonlysupportsdefaultvalue.
2 2 13 ATS 4 SetResponseFormattingCharacter...........................................................................
ATS 4 SetResponseFormattingCharacter
ReadCommand

ATS 4?

Response
<n>
OK
Parameters
SeeWriteCommand
WriteCommand

ATS 4 =

Response
Thisparameter settingdeterminesthecharacter generatedbytheTAfor
resultcodeandinformationtext.
OK
or
ERROR
Parameters
10 Responseformattingcharacter
ParameterSavingMode -
MaxResponseTime -
Reference
V. 25 ter

Note
Default 10 =LF.Itonlysupportsdefaultvalue.
2 2 14 ATS 5 SetCommandLineEditingCharacter.........................................................................
ATS 5 SetCommandLineEditingCharacter
ReadCommand

ATS 5?

Response
<n>
OK
Parameters
SeeWriteCommand
WriteCommand

ATS 5 =

Response
This parameter settingdetermines thecharacter recognized by TAasa
request to delete from the command line the immediately preceding
character.
OK
or
ERROR
Parameters
0 - 8 - 127 Responseformattingcharacter
ParameterSavingMode -

MaxResponseTime -
Reference
V. 25 ter

Note
Default 8 =Backspace.
2 2 15 ATS 6 PauseBeforeBlindDialing...........................................................................................
ATS 6 PauseBeforeBlindDialing
ReadCommand

ATS 6?

Response
<n>
OK
WriteCommand

ATS 6 =

Response
OK
or
ERROR
Parameters
0 - 2 - 999 Time
ParameterSavingMode -
MaxResponseTime -
Reference
V. 25 ter

Note
NoeffectinGSM
2 2 16 ATS 7 SetNumberofSecondstoWaitforConnectionCompletion..................................
ATS 7 SetNumberofSecondstoWaitforConnectionCompletion
ReadCommand

ATS 7?

Response
<n>
OK
Parameters
SeeWriteCommand
WriteCommand

ATS 7 =

Response
Thisparametersettingdeterminestheamountoftimetowaitforthe
connectioncompletionincaseofansweringororiginatingacall.
OK
or
ERROR
Parameters
0 - 255 Numberofsecondstowaitforconnectioncompletion
ParameterSavingMode -

MaxResponseTime -

Reference
V. 25 ter

Note
IfcalledpartyhasspecifiedahighvalueforATS 0 =<n>,callsetupmayfail.
ThecorrelationbetweenATS 7 andATS 0 isimportant
Example:CallmayfailifATS 7 = 30 andATS 0 = 20.
ATS 7 isonlyapplicabletodatacall.
StringofDCommand................................................................................................................................... 2 2 17 ATS 8 SetNumberofSecondstoWaitforCommaDialModifierEncounteredinDial
DialStringofDCommand
ATS 8 SetNumberofSecondstoWaitforCommaDialModifierEncounteredinDial
StringofDCommand
ReadCommand

ATS 8?

Response
<n>
OK
Parameters
SeeWriteCommand
WriteCommand

ATS 8 =

Response
OK
or
ERROR
Parameters
0 - 2 - 255 Thevalueofthisregisterdetermineshowlongthe
modemshouldpausewhenitseesacommainthedialingstring.
ParameterSavingMode -

MaxResponseTime -
Reference
V. 25 ter

Note
NoeffectinGSM
2 2 18 ATS 10 SetDisconnectDelayafterIndicatingtheAbsenceofDataCarrier....................
ATS 10 SetDisconnectDelayafterIndicatingtheAbsenceofDataCarrier
ReadCommand

ATS 10?

Response
<n>
OK
Parameters
SeeWriteCommand
WriteCommand

ATS 10 =

Response
ThisparametersettingdeterminestheamountoftimethattheTAwill
remainconnectedinabsenceofdatacarrier.Ifthedatacarrierisoncemore
detectedbeforedisconnecting,theTAremainsconnected.
OK
or
ERROR
Parameters
1 - 14 - 255 Numberoftenthssecondsofdelay
ParameterSavingMode -
MaxResponseTime -
Reference
V. 25 ter

Note
2 2 19 ATV TAResponseFormat........................................................................................................
ATV TAResponseFormat
ExecutionCommand

ATV

Response
Thisparameter settingdeterminesthecontentsoftheheader andtrailer
transmittedwithresultcodesandinformationresponses.
When<value>= 0
0
When= 1
OK
Parameters

0 Informationresponse:
Shortresultcodeformat:
1 Informationresponse:
Longresultcodeformat:
Theresultcodes,theirnumericequivalentsandbriefdescriptionsoftheuse
ofeacharelistedinthefollowingtable.
ParameterSavingMode -
MaxResponseTime -
Reference
V. 25 ter

Note
ATV 1 ATV 0 Description
OK 0 AcknowledgesexecutionofaCommand

CONNECT 1
Aconnectionhasbeenestablished; theDCEismovingfrom
Commandstatetoonlinedatastate
RING 2 TheDCEhasdetectedanincomingcallsignalfromnetwork

NOCARRIER 3
Theconnectionhasbeenterminatedortheattempttoestablish
aconnectionfailed

ERROR 4

Command not recognized, Command line maximum length
exceeded, parameter value invalid, or other problem with
processingtheCommandline
NODIALTONE 6 Nodialtonedetected
BUSY 7 Engaged(busy)signaldetected

NOANSWER 8

"@"(WaitforQuietAnswer)dialmodifierwasused,butremote
ringingfollowedbyfivesecondsofsilencewas notdetected
beforeexpirationoftheconnectiontimer(S 7 )
PROCEEDING 9 AnATcommandisbeingprocessed

CONNECT Manufacturer-
specific

SameasCONNECT,butincludesmanufacturer-specifictext
thatmayspecifyDTEspeed,linespeed,errorcontrol,data
compression,orotherstatus
2 2 20 ATX SetCONNECTResultCodeFormatandMonitorCallProgress..............................
ATX SetCONNECTResultCodeFormatandMonitorCallProgress
ExecutionCommand
ATX

Response
This parameter setting determines whether or not the TA detected the
presenceofdial toneandbusy signal andwhether or notTAtransmits
particularresultcodes.
OK
ERROR
Parameters
0 CONNECT resultcodeonlyreturned,dialtoneandbusy
detectionarebothdisabled.
1 CONNECT resultcodeonlyreturned,dialtoneand
busydetectionarebothdisabled.
2 CONNECT resultcodereturned,dialtonedetection
isenabled,busydetectionisdisabled.
3 CONNECT resultcodereturned,dialtonedetection
isdisabled,busydetectionisenabled.
4 CONNECT resultcodereturned,dialtoneandbusy
detectionarebothenabled.
ParameterSavingMode -
MaxResponseTime -
Reference
V. 25 ter

Note
2 2 21 AT&C SetDCDFunctionMode...............................................................................................
AT&C SetDCDFunctionMode
ExecutionCommand

AT&C

Response
Thisparameterdetermineshowthestateofcircuit 109 (DCD) relatestothe
detectionofreceivedlinesignalfromthedistantend.
OK
ERROR
Parameters
0 DCD lineisalwaysON
1 DCD lineisONonlyinthepresenceofdatacarrier
ParameterSavingMode -

MaxResponseTime -
Reference
V. 25 ter

Note
2 2 22 AT&D SetDTRFunctionMode................................................................................................
AT&D SetDTRFunctionMode
ExecutionCommand

AT&D[]

Response
ThisparameterdetermineshowtheTArespondswhencircuit 108 / 2 (DTR)
ischangedfromtheONtotheOFFconditionduringdatamode.
OK
or
ERROR
Parameters
0 TAignoresstatusonDTR.
1 ON->OFFonDTR:ChangetoCommandmodewith
remainingtheconnectedcall.
2 ON->OFFonDTR:Disconnectcall,changetoCommand
mode.DuringstateDTR=OFFisauto-answeroff.
ParameterSavingMode -
MaxResponseTime -
Reference
V. 25 ter

Note
2 2 23 AT&E SetCONNECTResultCodeFormatAboutSpeed..................................................
AT&E SetCONNECTResultCodeFormatAboutSpeed
ExecutionCommand

AT&E[]

ThisparametersettingdeterminestoreportSerialconnectionrateor
Wirelessconnectionspeed.ItisvalidonlyATXabove 0.
Response
OK
or
ERROR
Parameters

0 Wirelessconnectionspeedinintegerformat.
1 Serialconnectionrateinintegerformat.Suchas:" 115200 "
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
V. 25 ter

Note
2 2 24 AT+GCAP RequestCompleteTACapabilitiesList..............................................................
AT+GCAP RequestCompleteTACapabilitiesList
ExecutionCommand Response

AT+GCAP TAreportsalistofadditionalcapabilities.
+GCAP: listofsupported s

OK
Parameters
+CGSM GSMfunctionissupported
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference
V. 25 ter

Note
2 2 25 AT+GMI RequestManufacturerIdentification.......................................................................
AT+GMI RequestManufacturerIdentification
TestCommand

AT+GMI=?

Response
OK
Parameters
ExecutionCommand

AT+GMI

TAreportsoneormorelinesofinformationtextwhichpermittheuserto
identifythemanufacturer.
SIMCOM_Ltd
OK
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
V. 25 ter

Note
2 2 26 AT+GMM RequestTAModelIdentification............................................................................
AT+GMM RequestTAModelIdentification
TestCommand

AT+GMM=?

Response
OK
ExecutionCommand
AT+GMM

TAreportsoneormorelinesofinformationtextwhichpermittheuserto
identifythespecificmodelofdevice.
<model>
OK
Parameters
Productmodelidentificationtext
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
V. 25 ter

Note
2 2 27 AT+GMR RequestTARevisionIdentificationofSoftwareRelease..................................
AT+GMR RequestTARevisionIdentificationofSoftwareRelease
TestCommand

AT+GMR=?

Response
OK
ExecutionCommand

AT+GMR

TAreportsoneormorelinesofinformationtextwhichpermittheuserto
identifytherevisionofsoftwarerelease.
Revision:<revision>
OK
Parameters
Revisionofsoftwarerelease
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
V. 25 ter

Note
2 2 28 AT+GOI RequestGlobalObjectIdentification......................................................................
AT+GOI RequestGlobalObjectIdentification
TestCommand

AT+GOI=?

Response
OK
ExecutionCommand

AT+GOI

Response
TAreportsoneormorelinesofinformationtextwhichpermittheuserto
identifythedevice,basedontheISOsystemforregisteringuniqueobject
identifiers.
<ObjectId>
OK
Parameters
<ObjectId> Identifierofdevicetype
seeX. 208 , 209 fortheformatof<ObjectId>
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
V. 25 ter

Note
2 2 29 AT+GSN RequestTASerialNumberIdentification(IMEI)..................................................
AT+GSN RequestTASerialNumberIdentification(IMEI)
TestCommand

AT+GSN=?

Response
OK
ExecutionCommand

AT+GSN

Response
TAreportstheIMEI(internationalmobileequipmentidentifier) number in
informationtextwhichpermittheusertoidentifytheindividualMEdevice.
<sn>
OK
Parameters
IMEIofthetelephone(International Mobile stationEquipment
Identity)
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference
V. 25 ter

Note
Theserialnumber(IMEI)isvariedbyindividualMEdevice.
2 2 30 AT+ICF SetTE-TAControlCharacterFraming....................................................................
AT+ICF SetTE-TAControlCharacterFraming
TestCommand

AT+ICF=?

Response
+ICF:( listofsupported <format> s ),( listofsupported <parity> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+ICF?

Response
+ICF:<format>,<parity>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+ICF=[,]

Response
This parameter setting determines theserial interfacecharacter framing
formatandparityreceivedbyTAfromTE.
OK
Parameters
1 8 data 0 parity 2 stop
2 8 data 1 parity 1 stop
3 8 data 0 parity 1 stop
4 7 data 0 parity 2 stop
5 7 data 1 parity 1 stop
6 7 data 0 parity 1 stop
0 odd
1 even
3 space( 0 )
ParameterSavingMode -
MaxResponseTime -

Reference
V. 25 ter

Note
TheCommandisappliedforCommandstate;
In<format>parameter," 0 parity"meansnoparity;
The<parity>fieldisignoredifthe<format>fieldspecifiesnoparityand
string"+ICF:<format>, 255 "willberesponseto"AT+ICF?"Command.
2 2 31 AT+IFC SetTE-TALocalDataFlowControl.........................................................................
AT+IFC SetTE-TALocalDataFlowControl
TestCommand

AT+IFC=?

Response
+IFC:( listofsupported <dce_by_dte> s ),( listofsupported <dte_by_dce> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+IFC?

Response
+IFC:<dce_by_dte>,<dte_by_dce>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+IFC=<dce_by_dte>
[,<dte_by_dce>]

Response
This parameter setting determines the data flow control on the serial
interfacefordatamode.
OK
Parameters
<dce_by_dte> SpecifiesthemethodwillbeusedbyTEatreceiveof
datafromTA
0 Noflowcontrol
1 Softwareflowcontrol
2 Hardwareflowcontrol
<dte_by_dce> SpecifiesthemethodwillbeusedbyTAatreceiveofdata
fromTE
0 Noflowcontrol
1 Softwareflowcontrol
2 Hardwareflowcontrol
ParameterSavingMode -
MaxResponseTime -
Reference
V. 25 ter

Note
2 2 32 AT+IPR SetTE-TAFixedLocalRate......................................................................................
AT+IPR SetTE-TAFixedLocalRate
TestCommand

AT+IPR=?

Response
+IPR: ( list of supported auto detectable < rate >s ),( list of supported
fixed-only <rate> s )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+IPR?

Response
+IPR:<rate>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+IPR=

Response
This parameter settingdetermines thedatarateoftheTAon theserial
interface.TherateofCommandtakeseffectfollowingtheissuanceofany
resultcodeassociatedwiththecurrentCommandline.
OK
Parameters
<rate> Baudratepersecond
0
300
600
1200
2400
4800
9600
19200
38400
57600
115200
230400
921600
2000000
2900000
3000000
3200000
3686400
4000000
ParameterSavingMode AUTO_SAVE
MaxResponseTime -
Reference
V. 25 ter
Note

3 AT Commands According to 3 GPP
TS 27. 007
3 1 OverviewofATCommandAccordingto 3 GPPTS
Command Description
AT+CGMI Requestmanufactureridentification
AT+CGMM Requestmodelidentification
AT+CGMR RequestTArevisionidentificationofsoftwarerelease
AT+CGSN Requestproductserialnumberidentification(identicalwith+GSN)

AT+CSCS SelectTEcharacterset
AT+CIMI Requestinternationalmobilesubscriberidentity
AT+CLCK Facilitylock
AT+CMEE Reportmobileequipmenterror

AT+COPS Operatorselection
AT+CPAS Phoneactivitystatus
AT+CPIN EnterPIN
AT+CPWD Changepassword

AT+CRC Setcellularresultcodesforincomingcallindication
AT+CREG Networkregistration
AT+CRSM RestrictedSIMaccess
AT+CSQ Signalqualityreport

AT+CPOL Preferredoperatorlist
AT+COPN Readoperatornames
AT+CFUN Setphonefunctionality
AT+CCLK Clock

AT+CSIM GenericSIMaccess
AT+CBC Batterycharge
AT+CUSD Unstructuredsupplementaryservicedata
AT+CNUM SubscriberNumber

3 2 DetailedDescriptionsofATCommandAccordingto 3 GPPTS
3 2 1 AT+CGMI RequestManufacturerIdentification....................................................................
AT+CGMI RequestManufacturerIdentification
TestCommand

AT+CGMI=?

Response
OK
ExecutionCommand

AT+CGMI

Response
TAreturnsmanufactureridentificationtext.
<manufacturer>
OK
Parameters
TheIDofmanufacturer
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 2 AT+CGMM RequestModelIdentification..............................................................................
AT+CGMM RequestModelIdentification
TestCommand

AT+CGMM=?

Response
OK
ExecutionCommand

AT+CGMM

Response
TAreturnsproductmodelidentificationtext.
<model>
OK
Parameters
Productmodelidentificationtext
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 3 AT+CGMR RequestTARevisionIdentificationofSoftwareRelease...............................
AT+CGMR RequestTARevisionIdentificationofSoftwareRelease
TestCommand

AT+CGMR=?

Response
OK
ExecutionCommand

AT+CGMR

Response
TAreturnsproductsoftwareversionidentificationtext.
Revision:<revision>
OK
Parameters
Productsoftwareversionidentificationtext
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 4 AT+CGSN RequestProductSerialNumberIdentification..................................................
AT+CGSN RequestProductSerialNumberIdentification(Identicalwith+GSN)
TestCommand
AT+CGSN=?

Response
OK
ExecutionCommand

AT+CGSN

Response
see+GSN
<sn>
OK
Parameters
Internationalmobileequipmentidentity(IMEI)
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 5 AT+CSCS SelectTECharacterSet.......................................................................................
AT+CSCS SelectTECharacterSet
TestCommand Response
+CSCS:( listofsupported s )

AT+CSCS=?
OK
Parameters
<chset> "GSM" GSM 7 bitdefaultalphabet( 3 GPPTS 23. 038 );
"UCS 2 " 16 - bituniversal multiple-octetcoded character set
(ISO/IEC 10646 ); UCS 2 character strings are converted to
hexadecimalnumbersfrom 0000 toFFFF;e.g." 004100620063 "
equalsthree 16 - bitcharacterswithdecimalvalues 65 , 98 and
99
"IRA" Internationalreferencealphabet(ITU-TT. 50 )
ReadCommand
AT+CSCS?

Response
+CSCS:<chset>
OK
Parameters
SeeTestCommand
WriteCommand

AT+CSCS=

Response
Setswhichcharacterset areusedbytheTE. TheTAcanthen
convertcharacterstringscorrectlybetweentheTEandMEcharactersets.
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
SeeTestCommand
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 6 AT+CIMI RequestInternationalMobileSubscriberIdentity................................................
AT+CIMI RequestInternationalMobileSubscriberIdentity
TestCommand

AT+CIMI=?

Response
OK
ExecutionCommand

AT+CIMI

Response
TAreturns< IMSI >foridentifyingtheindividualSIMwhichisattachedtoME.
<IMSI>
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
<IMSI> InternationalMobileSubscriberIdentity(stringwithoutdouble
quotes)
ParameterSavingMode NO_SAVE

MaxResponseTime 20 s
Reference
3 GPPTS 27. 007 [ 13 ]
Note

3 2 7 AT+CLCK FacilityLock.............................................................................................................
AT+CLCK FacilityLock
TestCommand

AT+CLCK=?

Response
+CLCK:( listofsupported <fac> s )
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CLCK=,[,[,
]]

Response
ThisCommandisusedtolock,unlockorinterrogateaMEoranetwork
facility < fac >. Password is normally needed to do such actions. When
queryingthestatusofanetworkservice(< mode >= 2 )theresponselinefor
‘not active’ case (< status >= 0 ) should be returnedonly if service is not
activeforany< class >.
If< mode >≠ 2 andCommandissuccessful
OK
If< mode >= 2 andCommandissuccessful
+CLCK:<status>[,<class 1 >[<CR><LF>+CLCK:
<status>,<class 2 >[...]]
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
<fac>
"AB" AllBarringservices(onlyfor<mode>= 0 )
"AC" AllinComingbarringservices(onlyfor<mode>= 0 )"AG"
AlloutGoingbarringservices(onlyfor<mode>= 0 )
"AI" BAIC(BarrAllIncomingCalls)
"AO" BAOC(BarrAllOutgoingCalls)
"IR" BIC-Roam(BarrIncomingCallswhenRoaming
outsidethehomecountry)
"OI" BOIC(BarrOutgoingInternationalCalls)
"OX" BOIC-exHC(BarrOutgoingInternationalCallsexceptto
HomeCountry)
"SC" SIM(lockSIM/UICCcard)(SIM/UICCaskspasswordin
MTpower-upandwhenthislockcommandissued)Correspondto
PIN 1 code.
"FD" SIMcardoractiveapplicationintheUICC(GSMor
USIM)fixeddiallingmemoryfeature(ifPIN 2 authenticationhasnot
beendoneduringthecurrentsession,PIN 2 isrequiredas)
"PN" NetworkPersonalization,CorrespondtoNCKcode
"PU" NetworksubsetPersonalizationCorrespondtoNSCK
code
"PP" ServiceProviderPersonalizationCorrespondtoSPCK
code

0 unlock
1 lock
2 querystatus
Stringtype(Shallbethesameaspasswordspecifiedforthe
facilityfromtheMTuserinterfaceorwithcommandChangePassword
+CPWD)
1 - 255
1 Voice(telephony)
2 Datareferstoallbearerservices;with= 2 thismayrefer
onlytosomebearerserviceifTAdoesnotsupportvalues 16 , 32 , 64 and
128 )
4 Fax(facsimileservices)
7 Allclasses

0 Notactive
1 Active
ParameterSavingMode NO_SAVE

MaxResponseTime 15 s
Reference
3 GPPTS 27. 007 [ 14 ]

Note
 CMEerrorsifSIMnotinsertedorPINisnotentered.
3 2 8 AT+CMEE ReportMobileEquipmentError...........................................................................
AT+CMEE ReportMobileEquipmentError
TestCommand

AT+CMEE=?

Response
+CMEE:( listofsupported <n> s )
OK
Parameters
SeeWriteCommand
ReadCommand Response

AT+CMEE? +CMEE:

OK
Parameters
SeeWriteCommand
WriteCommand
AT+CMEE=[]

Response
TAdisablesorenablestheuseofresultcode +CMEERROR: asan
indicationofanerrorrelatingtothefunctionalityoftheME.
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
0 Disable +CMEERROR: resultcodeanduseERROR
instead.
1 Enable +CMEERROR: resultcodeandusenumeric
< err >
2 Enable +CMEERROR: resultcodeanduseverbose
< err >values
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 9 AT+COPS OperatorSelection.................................................................................................
AT+COPS OperatorSelection
TestCommand

AT+COPS=?

Response
TAreturnsalistofquadruplets,eachrepresentinganoperatorpresentin
thenetwork.Anyoftheformatsmaybeunavailableandshouldthenbean
emptyfield.Thelistofoperatorsshallbeinorder:homenetwork,networks
referencedinSIM,andothernetworks.
+COPS:( listofsupported <stat>, longalphanumeric <oper>, short
alphanumeric <oper>, numeric <oper>,<netact>) s [,,( listofsupported
<mode> s ),( listofsupported <format> s )]
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
SeeWriteCommand
ReadCommand
Response
TAreturns the current mode andthe currently selected operator. If no

AT+COPS? operatorisselected,< format >and< oper >areomitted.
+COPS:[,,,]

OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
SeeWriteCommand
WriteCommand
AT+COPS=,[[,]]

Response
TAforcesanattempttoselectandregistertheGSMnetworkoperator.Ifthe
selected operator is not available, no other operator shall be selected
(except = 4 ). The selected operator name format shall apply to
furtherreadcommands(AT+COPS?).
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
0 Unknown
1 Operatoravailable
2 Operatorcurrent
3 Operatorforbidden
Referto[ 27. 007 ]
operatorinformatasper
0 Automaticmode;fieldisignored
1 Manual(fieldshallbepresent,andoptionally)
2 manualderegisterfromnetwork
3 setonly(forreadCommand+COPS?)-not
showninReadCommandresponse
4 Manual/automatic(fieldshallbepresent);if
manualselectionfails,automaticmode(= 0 )is
entered
0 Longformatalphanumeric
1 Shortformatalphanumeric
2 Numeric;GSMLocationAreaIdentification
number
0 User-specifiedGSMaccesstechnology
1 GSMcompact
3 GSMEGPRS
7 User-specifiedLTEM 1 AGBaccesstechnology
9 User-specifiedLTENBS 1 accesstechnology
ParameterSavingMode AUTO_SAVE

MaxResponseTime
Testcommand: 45 seconds
Writecommand: 120 seconds
Reference
3 GPPTS 27. 007 [ 14 ]

Note
3 2 10 AT+CPAS PhoneActivityStatus.............................................................................................
AT+CPAS PhoneActivityStatus
TestCommand

AT+CPAS=?

Response
+CPAS:( listofsupported <pas> s )
OK
Parameters
SeeExecutionCommand
ExecutionCommand

AT+CPAS

Response
TAreturnstheactivitystatusofME.
+CPAS:<pas>
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters

0 Ready(MTallowscommandsfromTA/TE)
3 Ringing(MTisreadyforcommandsfromTA/TE,buttheringeris
active)
4 Callinprogress(MTisreadyforcommandsfromTA/TE,butacall
isinprogress)
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 11 AT+CPIN EnterPIN...................................................................................................................
AT+CPIN EnterPIN
TestCommand

AT+CPIN=?

Response
OK
ReadCommand

AT+CPIN?

Response
TAreturns analphanumericstringindicatingwhether some passwordis
requiredornot.
+CPIN:<code>
OK
Parameters
<code>
READY MTisnotpendingforanypassword
SIMPIN MTiswaitingSIMPINtobegiven
SIMPUK MTiswaitingforSIMPUKtobegiven
PH_SIMPIN MEiswaitingforphonetoSIMcard(antitheft)
PH_SIMPUK MEiswaitingforSIMPUK(antitheft)
SIMPIN 2 PIN 2 ,e.g.foreditingtheFDNbookpossibleonlyif
precedingCommandwasacknowledgedwith+CMEERROR: 17
SIMPUK 2 Possible only if preceding Command was
acknowledgedwitherror+CMEERROR: 18.
WriteCommand

AT+CPIN=[,]

Response
TAstoresapasswordwhichisnecessarybeforeitcanbeoperated(SIM
PIN,SIMPUK,PH-SIMPIN,etc.).
IfthePINrequiredisSIMPUKorSIMPUK 2 ,thesecondpinisrequired.
Thissecondpin,isusedtoreplacetheoldpinintheSIM.
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
Stringtype;password
Stringtype;IfthePINrequiredisSIMPUKorSIMPUK 2 :
newpassword
ParameterSavingMode NO_SAVE
MaxResponseTime 5 s
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 12 AT+CPWD ChangePassword.................................................................................................
AT+CPWD ChangePassword
TestCommand

AT+CPWD=?

Response
TAreturns a listof pairs whichpresent the available facilities and the
maximumlengthoftheirpassword.
+CPWD:( listofsupported <fac> s,listofsupported <pwdlength> s )
OK
Parameters
<fac> SeeWriteCommand
<pwdlength> Integermax.lengthofpassword
WriteCommand

AT+CPWD=,<old

Response
TAsetsanewpasswordforthefacilitylockfunction.
OK
pwd>, Parameters

"AB" AllBarringservices
"AC" AllinComingbarringservices(onlyfor
= 0 )
"AG" AlloutGoingbarringservices(onlyfor
= 0 )
"AI" BAIC(BarrAllIncomingCalls)
"AO" BAOC(BarrAllOutgoingCalls)
"IR" BIC-Roam(BarrIncomingCallswhen
Roamingoutsidethehomecountry)
"OI" BOIC(BarrOutgoingInternationalCalls)
"OX" BOIC-exHC(BarrOutgoingInternationalCalls
excepttoHomeCountry)
"SC" SIM(lockSIM/UICCcard)(SIM/UICCasks
passwordinMTpower-upandwhenthislock
commandissued)CorrespondtoPIN 1 code.
"P 2 " SIMPIN 2
Stringtype(stringshouldbeincludedinquotationmarks):
passwordspecifiedforthefacilityfromtheuserinterfaceorwithcommand.
Ifanoldpasswordhasnotyetbeenset,isnottoenter.
Stringtype(stringshouldbeincludedinquotationmarks):
newpassword
ParameterSavingMode NO_SAVE

MaxResponseTime 15 s
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 13 AT+CRC SetCellularResultCodesforIncomingCallIndication.....................................
AT+CRC SetCellularResultCodesforIncomingCallIndication
TestCommand

AT+CRC=?

Response
+CRC:( listofsupported <mode> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CRC?

Response
+CRC:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CRC=[]

Response
TAcontrolswhetherornottheextendedformatofincomingcallindicationis
used.
OK
Parameters
0 Disableextendedformat
1 Enableextendedformat
OmittedUsepreviousvalue
UnsolicitedResultCode
Whenenabled,anincomingcallisindicatedtotheTEwithunsolicitedresult
code +CRING: insteadofthenormal RING.
Parameters
ASYNC Asynchronoustransparent
SYNC Synchronoustransparent
RELASYNCAsynchronousnon-transparent
RELSYNC Synchronousnon-transparent
FAX Facsimile
VOICE Voice
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 14 AT+CREG NetworkRegistration.............................................................................................
AT+CREG NetworkRegistration
TestCommand

AT+CREG=?

Response
+CREG:( listofsupported <n> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CREG?

Response
TAreturns thestatus of result codepresentationandan integer <stat>
whichshowswhetherthenetworkhascurrentlyindicatedtheregistrationof
theME.Locationinformationelements<lac>and<ci>arereturnedonly
when<n>= 2 andMEisregisteredinthenetwork.
+CREG:<n>,<stat>[,<lac>,<ci>,<netact>]
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
WriteCommand Response

AT+CREG[=] TAcontrolsthepresentationofanunsolicitedresultcode +CREG:
when< n >= 1 andthereisachangeintheMEnetworkregistrationstatus.
OK
Parameters
0 Disablenetworkregistrationunsolicitedresultcode
1 Enablenetworkregistrationunsolicitedresultcode
+CREG: < stat >
2 Enablenetworkregistrationunsolicitedresultcodewith
locationinformation( 2 isonlyfor 7000 seriesmodulewhich
supportGPRS.)
CREG:[,,,]
0 Notregistered,MTisnotcurrentlysearchinganew
operatortoregisterto
1 Registered,homenetwork
2 Not registered, but MT is currently searching a new
operatortoregisterto
3 Registrationdenied
4 Unknown
5 Registered,roaming
Stringtype(stringshouldbeincludedinquotationmarks);two
bytelocationareacodeinhexadecimalformat
Stringtype(stringshouldbeincludedinquotationmarks);two
bytecellIDinhexadecimalformat
0 User-specifiedGSMaccesstechnology
1 GSMcompact
3 GSMEGPRS
7 User-specifiedLTEM 1 AGBaccesstechnology
9 User-specifiedLTENBS 1 accesstechnology
UnsolicitedResultCode
If< n >= 1 andthereisachangeintheMTnetworkregistrationstatus
+CREG:
If< n >= 2 andthereisachangeintheMTnetworkregistrationstatusora
changeofthenetworkcell:
+CREG:[,,,]
Parameters
SeeWriteCommand
ParameterSavingMode -
MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 15 AT+CRSM RestrictedSIMAccess..........................................................................................
AT+CRSM RestrictedSIMAccess
TestCommand
AT+CRSM=?

Response
OK
WriteCommand
**AT+CRSM=<Command

[,[,<P 1 >,<P 2 >,

[,]]]**

Response
+CRSM:<sw 1 >,<sw 2 >[,<response>]
OK
ERROR
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters

176 READBINARY
178 READRECORD
192 GETRESPONSE
214 UPDATEBINARY
220 UPDATERECORD
242 STATUS
Allothervaluesarereserved;referGSM 11. 11.
Integertype;thisistheidentifierforanelementarydatafileon
SIM.MandatoryforeveryCommandexceptSTATUS
<P 1 >,<P 2 >,<P 3 > Integertype,range 0 – 255
ParameterstobepassedonbytheMEtotheSIM;referGSM

InformationwhichshallbewrittentotheSIM(hex-decimal
characterformat)
<sw 1 >,<sw 2 > Integertype,range 0 - 255
StatusinformationfromtheSIMabouttheexecutionofthe
actualCommand.TheseparametersaredeliveredtotheTEin
bothcases,onsuccessfulorfailedexecutionoftheCommand;
referGSM 11. 11.
ResponseofasuccessfulcompletionoftheCommand
previouslyissued(hexadecimalcharacterformat)
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 007
GSM 11. 11

Note
3 2 16 AT+CSQ SignalQualityReport...............................................................................................
AT+CSQ SignalQualityReport
TestCommand
AT+CSQ=?

Response
+CSQ:( listofsupported <rssi> s ),( listofsupported <ber> s )
OK
ExecutionCommand

AT+CSQ

Response
+CSQ:<rssi>,<ber>
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err >
ExecutionCommandreturnsreceivedsignalstrengthindication< rssi >and
channelbiterror rate< ber >fromtheME.TestCommandreturnsvalues
supportedbytheTA.
Parameters

0 - 115 dBmorless
1 - 111 dBm
2 ... 30 - 110 ...- 54 dBm
31 - 52 dBmorgreater
99 notknownornotdetectable
(inpercent):
0 ... 7 As RXQUAL values in the table in GSM 05. 08 [ 20 ]
subclause 7. 2. 4
99 Notknownornotdetectable
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 17 AT+CPOL PreferredOperatorList..........................................................................................
AT+CPOL PreferredOperatorList
TestCommand

AT+CPOL=?

Response
+CPOL:( listofsupported <index> s ),( listofsupported <format> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CPOL?

Response
+CPOL:
<index 1 >,<format>,<oper 1 >[,<GSM>,<GSM_compact>,<UTRAN>,<E-U
TRAN>][<CR><LF>+CPOL:
<index 2 >,<format>,<oper 2 >[,<GSM,<GSM_compact>,<UTRAN>,<E-UT
RAN>][...]]
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
SeeWriteCommand
WriteCommand

**AT+CPOL=[,[,[<GSM

,<GSM_compact>,,<E-UTRAN>]]]**

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
Integertype:ordernumberofoperatorinSIMpreferred
operatorlist
Indicateswhetheralphanumericornumeric
formatused(see +COPS Command)
0 Longformatalphanumeric< oper >
1 Shortformatalphanumeric< oper >
2 Numeric< oper >
Stringtype(stringshouldbeincludedinquotationmarks)
GSMaccesstechnology
0 Accesstechnologyisnotselected
1 Accesstechnologyisselected
<GSM_compact> GSMcompactaccesstechnology
0 Accesstechnologyisnotselected
1 Accesstechnologyisselected
UTRANaccesstechnology
0 Accesstechnologyisnotselected
1 Accesstechnologyisselected
<E-UTRAN> E-UTRANaccesstechnology
0 Accesstechnologyisnotselected
1 Accesstechnologyisselected
ParameterSavingMode -
MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 18 AT+COPN ReadOperatorNames..........................................................................................
AT+COPN ReadOperatorNames
TestCommand

AT+COPN=?

Response
OK
ExecutionCommand Response

AT+COPN +COPN:<numeric^1 >,<alpha^1 >
[+COPN:<numeric 2 >,<alpha 2 >
[...]]

OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
<numeric n > Stringtype(stringshouldbeincludedinquotationmarks):
operatorinnumericformat(see +COPS )
<alpha n > String type (string should be included inquotationmarks):
operatorinlongalphanumericformat(see +COPS )
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 19 AT+CFUN SetPhoneFunctionality........................................................................................
AT+CFUN SetPhoneFunctionality
TestCommand

AT+CFUN=?

Response
+CFUN:( listofsupported <fun> s ),( listofsupported <rst> s )
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
SeeWriteCommand
ReadCommand
AT+CFUN?

Response
+CFUN:<fun>
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
SeeWriteCommand
WriteCommand

**AT+CFUN=[,<rst

]**

Response
OK
IferrorisrelatedtoMEfunctionality:
+ CMEERROR:<err>
Parameters
<fun>
0 Minimumfunctionality
1 Fullfunctionality(Default)
4 DisablephonebothtransmitandreceiveRFcircuits.
5 FactoryTestMode
6 Reset
7 OfflineMode
<rst>
0 DonotResettheMTbeforesettingitto< fun >powerlevel.
(^1) ResettheMTbeforesettingitto< fun >powerlevel.
ParameterSavingMode -
MaxResponseTime 10 s
Reference
3 GPPTS 27. 007 [ 13 ]
Note
 The< fun >powerlevelwillbewrittentoflashexceptminimum
functionality.
 AT+CFUN= 1 , 1 canbeusedtoresetmodulepurposelyatminimum/full
functionalitymode.
 Responsestring" OK "willbereturnedaftermoduleresetsifbaudrate
issettofixedbaudrate.

3 2 20 AT+CCLK Clock.........................................................................................................................
AT+CCLK Clock
TestCommand

AT+CCLK=?

Response
OK
ReadCommand

AT+CCLK?

Response
+CCLK:<time>
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
SeeWriteCommand
WriteCommand

AT+CCLK=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
<time> Stringtype(stringshouldbeincludedinquotationmarks)value;
formatis"yy/MM/dd,hh:mm:ss±zz",wherecharactersindicateyear(twolast
digits),month,day,hour,minutes,secondsandtimezone(indicatesthe
difference,expressedinquartersofanhour,betweenthelocaltimeand
GMT;range- 47 ...+ 48 ).E.g. 6 thofMay 2010 , 00 : 01 : 52 GMT+ 2 hours
equalsto" 10 / 05 / 06 , 00 : 01 : 52 + 08 ".
ParameterSavingMode AUTO_SAVE

MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
Onlytimezoneisautosaved.
3 2 21 AT+CSIM GenericSIMAccess................................................................................................
AT+CSIM GenericSIMAccess
TestCommand

AT+CSIM=?

Response
OK
WriteCommand

AT+CSIM=,

Response
+CSIM:<length>,<response>
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
Integertype:lengthofcharacterssenttotheTEin
< Command >or< response >(i.e.twicethenumberofoctetsintheraw
data).
Stringtype(stringshouldbeincludedinquotationmarks):
hexformat:GSM 11. 11 SIMCommandsentfromtheMEtotheSIM.
Stringtype(stringshouldbeincludedinquotationmarks):
hexformat:GSM 11. 11 responsefromSIMto< Command >.
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
3 2 22 AT+CBC BatteryCharge..........................................................................................................
AT+CBC BatteryCharge
TestCommand

AT+CBC=?

Response
+CBC:( listofsupported <bcs> s ),( listofsupported <bcl> s ),(<voltage>)
OK
Parameters
SeeExecutionCommand
ExecutionCommand Response

AT+CBC +CBC:,,

OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
Chargestatus
0 MEisnotcharging
1 MEischarging
2 Charginghasfinished
Batteryconnectionlevel
1 ... 100 batteryhas 1 - 100 percentofcapacityremainingvent
Batteryvoltage(mV)
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]
Note

3 2 23 AT+CUSD UnstructuredSupplementaryServiceData.......................................................
AT+CUSD UnstructuredSupplementaryServiceData
TestCommand

AT+CUSD=?

Response
+CUSD:( listofsupported <n> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CUSD?

Response
+CUSD:<n>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CUSD=,,<
dcs>

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
<n> Anumericparameterwhichindicatescontroloftheunstructured
supplementaryservicedata
0 disabletheresultcodepresentationintheTE
1 enabletheresultcodepresentationintheTE
2 cancelsession(notapplicabletoreadCommandresponse)
Stringtype(stringshouldbeincludedinquotationmarks)
USSD-string
CellBroadcastDataCodingSchemeinintegerformat
(default 0 )
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
GSM 03. 38 [ 25 ]

Note
Whenussdisnotsuportorreturnerror,TEwillprint+CUSD: 4.
3 2 24 AT+CNUM SubscriberNumber...............................................................................................
AT+CNUM SubscriberNumber
TestCommand

AT+CNUM=?

Response
OK
ExecutionCommand

AT+CNUM

Response
+CNUM: "" ,<number 1 >,<type 1 >
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
< number x > Stringtype(stringshouldbeincludedinquotationmarks)
phonenumberofformatspecifiedby< type x >
< type x > Typeofaddressoctetinintegerformat(referGSM 04. 08 [ 8 ]
subclause 10. 5. 4. 7 )
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 007 [ 13 ]

Note
4 AT Commands According to 3 GPP
TS 27. 005
The 3 GPPTS 27. 005 commandsareforperformingSMSandCBSrelatedoperations.SIM 7000 Series
supportsbothTextandPDUmodes.

4 1 OverviewofATCommandsAccordingto 3 GPPTS
Command Description
AT+CMGD DeleteSMSmessage

AT+CMGF SelectSMSmessageformat
AT+CMGL ListSMSmessagesfrompreferredstore
AT+CMGR ReadSMSmessage
AT+CMGS SendSMSmessage

AT+CMGW WriteSMSmessagetomemory
AT+CMSS SendSMSmessagefromstorage
AT+CNMI NewSMSmessageindications
AT+CPMS PreferredSMSmessagestorage

AT+CRES RestoreSMSsettings
AT+CSAS SaveSMSsettings
AT+CSCA SMSservicecenteraddress
AT+CSDH ShowSMStextmodeparameters

AT+CSMP SetSMStextmodeparameters
AT+CSMS Selectmessageservice

4. 2 Detailed Descriptions of AT Commands According to 3 GPP TS
27. 005
4 2 1 AT+CMGD DeleteSMSMessage...........................................................................................
AT+CMGD DeleteSMSMessage
TestCommand Response

AT+CMGD=? +CMGD:( listofsupported s ),( listofsupported s )

OK
Parameters
SeeWriteCommand
WriteCommand
AT+CMGD=[,<
delflag>]

Response
TAdeletesmessage frompreferredmessagestorage < mem 1 > location
< index >.
OK
ERROR
IferrorisrelatedtoMEfunctionality:
+CMSERROR:
Parameters
Integertype;valueintherangeoflocationnumberssupportedby
theassociatedmemory
0 Deletethemessagespecifiedin< index >
1 Deleteallreadmessagesfrompreferredmessagestorage,
leavingunreadmessagesandstoredmobileoriginated
messages(whethersentornot)untouched
2 Deleteallreadmessagesfrompreferredmessagestorage
andsentmobileoriginatedmessages,leavingunread
messagesandunsentmobileoriginatedmessages
untouched
3 Deleteallreadmessagesfrompreferredmessagestorage,
sentandunsentmobileoriginatedmessagesleaving
unreadmessagesuntouched
4 Deleteallmessagesfrompreferredmessagestorage
includingunreadmessages
ParameterSavingMode NO_SAVE

MaxResponseTime

5 s(delete 1 message)
25 s(delete 50 messages)
25 s(delete 150 messages)
Reference
3 GPPTS 27. 005

Note
4 2 2 AT+CMGF SelectSMSMessageFormat..............................................................................
AT+CMGF SelectSMSMessageFormat
TestCommand

AT+CMGF=?

Response
+CMGF:( listofsupported <mode> s )
OK
Parameter
SeeWriteCommand
ReadCommand

AT+CMGF?

Response
+CMGF:<mode>
OK
Parameter
SeeWriteCommand
WriteCommand

AT+CMGF=[]

Response
TAsetsparametertodenotewhichinputandoutputformatofmessagesto
use.
OK
Parameter
0 PDUmode
1 Textmode
ParameterSavingMode -

MaxResponseTime -
Reference
3 GPPTS 27. 005
Note

4 2 3 AT+CMGL ListSMSMessagesfromPreferredStore.........................................................
AT+CMGL ListSMSMessagesfromPreferredStore
TestCommand

AT+CMGL=?

Response
+CMGL:( listofsupported <stat> s )
OK
Parameter
SeeWriteCommand
WriteCommand

AT+CMGL=[,]

Parameters
1 )Iftextmode:
<stat> "RECUNREAD" Receivedunreadmessages
"RECREAD" Receivedreadmessages
"STOUNSENT" Storedunsentmessages
"STOSENT" Storedsentmessages
"ALL" Allmessages
<mode> 0 Normal
1 NotchangestatusofthespecifiedSMSrecord
2 )IfPDUmode:
<stat> 0 Receivedunreadmessages
1 Receivedreadmessages
2 Storedunsentmessages
3 Storedsentmessages
4 Allmessages
0 Normal
1 NotchangestatusofthespecifiedSMSrecord
Response
TA returns messages with status value < stat > from message storage
< mem 1 >totheTE.Ifstatusofthemessageis'receivedunread',statusin
thestoragechangesto'receivedread'.

1 )Iftextmode( +CMGF= 1 )andCommandsuccessful:
forSMS-SUBMITsand/orSMS-DELIVERs:
+CMGL:,,<oa/da>[,][,]
[,<tooa/toda>,]
[+CMGL:,,<da/oa>
[,][,][,<tooa/toda>,][...]]

forSMS-STATUS-REPORTs:
+CMGL:,,,[,][,],,

,
[+CMGL:,,,
[,][,],,
,[...]]
forSMS-COMMANDs:
+CMGL:,,,[
+CMGL:,,,[...]]

forCBMstorage:
+CMGL:,,,,,

+CMGL:,,,,,
[...]]
OK

2 )IfPDUmode( +CMGF= 0 )andCommandsuccessful:
+CMGL:,[,],

+CMGL:,[,alpha],
[...]]
OK

3 )IferrorisrelatedtoMEfunctionality:
+CMSERROR:
Parameters
Stringtype(stringshouldbeincludedinquotationmarks)
alphanumericrepresentationof< da >or< oa >correspondingtotheentry
foundinMTphonebook;implementationofthisfeatureismanufacturer
specific;usedcharactersetshouldbetheoneselectedwithCommand
SelectTECharacterSet +CSCS (seedefinitionofthisCommandin 3 GPP

TS 27. 007 )
GSM 03. 40 TP-Destination-AddressAddress-Valuefieldin
stringformat;BCDnumbers(orGSMdefaultalphabetcharacters)are
convertedtocharactersofthecurrentlyselectedTEcharacterset(refer
Command +CSCS in 3 GPPTS 27. 007 );typeofaddressgivenby< toda >
InthecaseofSMS:GSM 03. 40 TP-User-Dataintextmode
responses;format:

if< dcs >indicatesthatGSM 03. 38 defaultalphabetisusedand
< fo >indicatesthatGSM 03. 40 TPUser-Data-Header-Indication
isnotset:
ifTEcharactersetotherthan"HEX"(referCommandSelectTE
CharacterSet+CSCSin 3 GPPTS 27. 007 ):ME/TAconverts
GSMalphabetintocurrentTEcharactersetaccordingtorulesof
AnnexA
ifTEcharactersetis"HEX":ME/TAconvertseach 7 - bit
characterofGSMalphabetintotwoIRAcharacterlong
hexadecimalnumber(e.g.characterP(GSM 23 )ispresentedas
17 (IRA 49 and 55 ))
if< dcs >indicatesthat 8 - bitorUCS 2 datacodingschemeis
used,or< fo >indicatesthatGSM 03. 40
TP-User-Data-Header-Indicationisset:ME/TAconvertseach
8 - bitoctetintotwoIRAcharacterlonghexadecimalnumber(e.g.
octetwithintegervalue 42 ispresentedtoTEastwocharacters
2 A(IRA 50 and 65 ))InthecaseofCBS:GSM 03. 41 CBM
ContentofMessageintextmoderesponses;format:
if< dcs >indicatesthatGSM 03. 38 defaultalphabetisused:
ifTEcharactersetotherthan"HEX"(referCommand+CSCSin
3 GPPTS 27. 007 ):ME/TAconvertsGSMalphabetintocurrent
TEcharactersetaccordingtorulesofAnnexA
ifTEcharactersetis"HEX":ME/TAconvertseach 7 - bit
characterofGSMalphabetintotwoIRAcharacterlong
hexadecimalnumber
if< dcs >indicatesthat 8 - bitorUCS 2 datacodingschemeis
used:ME/TAconvertseach 8 - bitoctetintotwoIRAcharacter
longhexadecimalnumber
Integertypevalueindicatinginthetextmode( +CMGF= 1 )the
lengthofthemessagebody< data > (or< cdata >)incharacters;orinPDU
mode( +CMGF= 0 ),thelengthoftheactualTPdataunitinoctets(i.e.theRP
layerSMSCaddressoctetsarenotcountedinthelength)
Integertype;valueintherangeoflocationnumberssupported
bytheassociatedmemory
GSM 03. 40 TP-Originating-AddressAddress-Valuefieldin
stringformat;BCDnumbers(orGSMdefaultalphabetcharacters)are
convertedtocharactersofthecurrentlyselectedTEcharacterset(refer
Command +CSCS in 3 GPPTS 27. 007 );typeofaddressgivenby
InthecaseofSMS:GSM 04. 11 SCaddressfollowedby
GSM 03. 40 TPDUinhexadecimalformat:ME/TAconvertseachoctetofTP
dataunitintotwoIRAcharacterlonghexadecimalnumber(e.g.octetwith
integervalue 42 ispresentedtoTEastwocharacters 2 A(IRA 50 and 65 )).
InthecaseofCBS:GSM 03. 41 TPDUinhexadecimalformat.
<scts> GSM 03. 40 TP-Service-Center-Time-Stampintime-string
format(refer< dt >)
<toda> GSM 04. 11 TP-Destination-AddressType-of-Addressoctetin
integerformat(whenfirstcharacterof< da >is+(IRA 43 )defaultis 145 ,
otherwisedefaultis 129 )
<tooa> GSM 04. 11 TP-Originating-AddressType-of-Addressoctetin
integerformat(defaultrefer< toda >)
ExecutionCommand

AT+CMGL

1 )Iftextmode:
thesameas AT+CMGL="RECUNREAD" , receivedunreadmessages
2 )IfPDUmode:
thesameas AT+CMGL= 0 ,receivedunreadmessages
SeemoremessagespleaserefertoWriteCommand.
Parameters
SeeWriteCommand
ParameterSavingMode NO_SAVE

MaxResponseTime
20 s(list 50 messages)
20 s(list 150 messages)
Reference
3 GPPTS 27. 005

Note
4 2 4 AT+CMGR ReadSMSMessage.............................................................................................
AT+CMGR ReadSMSMessage
TestCommand

AT+CMGR=?

Response
OK
WriteCommand
AT+CMGR=[,<
mode>]

Parameters
<index> Integertype;valueintherangeoflocationnumberssupported
bytheassociatedmemory
<mode> 0 Normal
1 NotchangestatusofthespecifiedSMSrecord
Response
TA returns SMS message with location value < index > from message
storage< mem 1 >totheTE.Ifstatusofthemessageis'receivedunread',
statusinthestoragechangesto'receivedread'.
1 )Iftextmode( +CMGF= 1 )andCommandsuccessful:
forSMS-DELIVER:
+CMGR:<stat>,<oa>[,<alpha>],<scts>[,<tooa>,<fo>,<pid>,<dcs>
,,,]
forSMS-SUBMIT:
+CMGR:,[,][,,,,[,]
,,,]

forSMS-STATUS-REPORTs:
+CMGR:,,[,][,],,

,
forSMS-COMMANDs:
+CMGR:,,[,[,][,][,]
,]

forCBMstorage:
+CMGR:,,,,,
2 )IfPDUmode(+CMGF= 0 )andCommandsuccessful:
+CMGR:[,],

OK
3 )IferrorisrelatedtoMEfunctionality:
+CMSERROR:
Parameters
Stringtype(stringshouldbeincludedinquotationmarks)
alphanumericrepresentationof< da >or< oa >correspondingtotheentry
foundinMTphonebook;implementationofthisfeatureismanufacturer
specific
GSM 03. 40 TP-Destination-AddressAddress-Valuefieldin
stringformat;BCDnumbers(orGSMdefaultalphabetcharacters)are
convertedtocharactersofthecurrentlyselectedTEcharacterset(specified
by +CSCS in 3 GPPTS 27. 007 );typeofaddressgivenby< toda >
InthecaseofSMS:GSM 03. 40 TP-User-Dataintextmode
responses;format:

if< dcs >indicatesthatGSM 03. 38 defaultalphabetisusedand
< fo >indicatesthatGSM 03. 40 TPUser-Data-Header-Indication
isnotset:
ifTEcharactersetotherthan"HEX"(referCommandSelectTE
CharacterSet+CSCSin 3 GPPTS 27. 007 ):ME/TAconverts
GSMalphabetintocurrentTEcharactersetaccordingtorulesof
AnnexA
ifTEcharactersetis"HEX":ME/TAconvertseach 7 - bit
characterofGSMalphabetintotwoIRAcharacterlong
hexadecimalnumber(e.g.characterP(GSM 23 )ispresentedas
17 (IRA 49 and 55 ))
if< dcs >indicatesthat 8 - bitorUCS 2 datacodingschemeis
used,or< fo >indicatesthatGSM 03. 40
TP-User-Data-Header-Indicationisset:ME/TAconvertseach
8 - bitoctetintotwoIRAcharacterlonghexadecimalnumber(e.g.
octetwithintegervalue 42 ispresentedtoTEastwocharacters
2 A(IRA 50 and 65 ))InthecaseofCBS:GSM 03. 41 CBM
ContentofMessageintextmoderesponses;format:
if< dcs >indicatesthatGSM 03. 38 defaultalphabetisused:
ifTEcharactersetotherthan"HEX"(referCommand+CSCSin
3 GPPTS 27. 007 ):ME/TAconvertsGSMalphabetintocurrent
TEcharactersetaccordingtorulesofAnnexA
ifTEcharactersetis"HEX":ME/TAconvertseach 7 - bit
characterofGSMalphabetintotwoIRAcharacterlong
hexadecimalnumber
if< dcs >indicatesthat 8 - bitorUCS 2 datacodingschemeis
used:ME/TAconvertseach 8 - bitoctetintotwoIRAcharacter
longhexadecimalnumber
DependingontheCommandorresultcode:GSM 03. 38 SMS
DataCodingScheme(default 0 ),orCellBroadcastDataCodingSchemein
integerformat
DependingontheCommandorresultcode:firstoctetofGSM
40 SMS-DELIVER,SMS-SUBMIT(default 17 ),
SMS-STATUS-REPORT,orSMS-COMMAND(default 2 )inintegerformat
integertypevalueindicatinginthetextmode( +CMGF= 1 )the
lengthofthemessagebody< data > (or< cdata >)in characters;orin
PDUmode( +CMGF= 0 ),thelengthoftheactualTPdataunitinoctets(i.e.
theRPlayerSMSCaddressoctetsarenotcountedinthelength)
GSM 03. 41 CBMMessageIdentifierinintegerformat
GSM 03. 40 TP-Originating-AddressAddress-Valuefieldin
stringformat;BCDnumbers(orGSMdefaultalphabetcharacters)are
convertedcharactersofthecurrentlyselectedTEcharacterset(specified
by+CSCSin 3 GPPTS 27. 007 );typeofaddressgivenby< tooa >
InthecaseofSMS:GSM 04. 11 SCaddressfollowedbyGSM
40 TPDUinhexadecimalformat:ME/TAconvertseachoctetofTPdata
unitintotwoIRAcharacterlonghexadecimalnumber(e.g.octetwithinteger
value 42 ispresentedtoTEastwocharacters 2 A(IRA 50 and 65 )). Inthe
caseofCBS:GSM 03. 41 TPDUinhexadecimalformat.
GSM 03. 40 TP-Protocol-Identifierinintegerformat
(default 0 )
GSM 04. 11 RPSCaddressAddress-Valuefieldinstring
format;BCDnumbers(orGSMdefaultalphabetcharacters)areconverted
tocharactersofthecurrentlyselectedTEcharacterset(specifiedby
+CSCSin 3 GPPTS 27. 007 );typeofaddressgivenby< tosca >
GSM 03. 40 TP-Service-Centre-Time-Stampintime-string
format(refer< dt >)
0 "RECUNREAD" Receivedunreadmessages
1 "RECREAD" Receivedreadmessages
2 "STOUNSENT" Storedunsentmessages
3 "STOSENT" Storedsentmessages
4 "ALL" Allmessages
GSM 04. 11 TP-Destination-AddressType-of-Addressoctet
inintegerformat(whenfirstcharacterof< da >is+(IRA 43 )defaultis 145 ,
otherwisedefaultis 129 )
GSM 04. 11 TP-Originating-AddressType-of-Addressoctetin
integerformat(defaultrefer< toda >)
GSM 04. 11 RPSCaddressType-of-Addressoctetininteger
format(defaultrefer< toda >)
DependingonSMS-SUBMIT< fo >setting:GSM 03. 40
TP-Validity-Periodeitherinintegerformat(default 167 )orintime-string
format(refer< dt >)
ParameterSavingMode NO_SAVE

MaxResponseTime 5 s
Reference
3 GPPTS 27. 005

Note
4 2 5 AT+CMGS SendSMSMessage.............................................................................................
AT+CMGS SendSMSMessage
TestCommand
AT+CMGS=?

Response
OK
WriteCommand
1 ) If text mode
(+CMGF= 1 ):
AT+CMGS=[,]
text is entered
<ctrl-Z/ESC>
ESC quits without
sending

2 ) If PDU mode
(+CMGF= 0 ):

AT+CMGS=
PDU is given
<ctrl-Z/ESC>

Parameters
<da> GSM 03. 40 TP-Destination-AddressAddress-Valuefieldin
stringformat(stringshouldbeincludedinquotationmarks);BCDnumbers
(orGSMdefaultalphabetcharacters)areconvertedtocharactersofthe
currentlyselectedTEcharacterset(specifiedby +CSCS in 3 GPPTS
27. 007 );typeofaddressgivenby< toda >
<toda> GSM 04. 11 TP-Destination-AddressType-of-Addressoctetin
integerformat(whenfirstcharacterof< da >is+(IRA 43 )defaultis 145 ,
otherwisedefaultis 129 )
<length> Integertypevalue(notexceed 160 bytes)indicatinginthetext
mode( +CMGF= 1 )thelengthofthemessagebody< data > (or< cdata >)in
characters;orinPDUmode(+CMGF= 0 ),thelengthoftheactualTPdata
unitinoctets(i.e.theRPlayerSMSCaddressoctetsarenotcountedinthe
length)
Response
TAsendsmessagefromaTEtothenetwork(SMS-SUBMIT).Message
referencevalue< mr >isreturnedtotheTEonsuccessfulmessagedelivery.
Optionally(when +CSMS<service> valueis 1 andnetworksupports)
< scts >isreturned.Valuescanbeusedtoidentifymessageupon
unsoliciteddeliverystatusreportresultcode.
1 )Iftextmode( +CMGF= 1 )andsendingsuccessful:
+CMGS:<mr>
OK
2 )IfPDUmode( +CMGF= 0 )andsendingsuccessful:
+CMGS:<mr>
OK
3 )IferrorisrelatedtoMEfunctionality:
+CMSERROR:
Parameter
GSM 03. 40 TP-Message-Referenceinintegerformat
ParameterSavingMode NO_SAVE
MaxResponseTime 60 s
Reference
3 GPPTS 27. 005

Note
 Rejectincomingcallwhensendingmessages.
4 2 6 AT+CMGW WriteSMSMessagetoMemory........................................................................
AT+CMGW WriteSMSMessagetoMemory
TestCommand
AT+CMGW=?

Response
OK
WriteCommand
1 )Iftextmode
(+CMGF= 1 ):

AT+CMGW=<oa/da>[,<
tooa/toda>][,]

textisentered
<ctrl-Z/ESC>
quitswithout
sending

2 )IfPDUmode
(+CMGF= 0 ):

AT+CMGW=[,
]

PDUisgiven
<ctrl-Z/ESC>

Response
TAtransmitsSMSmessage(eitherSMS-DELIVERorSMS-SUBMIT)from
TEtomemorystorage< mem 2 >.Memorylocation< index >ofthestored
message is returned. By default message status will be set to 'stored
unsent',butparameter< stat >allowsalsootherstatusvaluestobegiven.
Ifwritingissuccessful:
+CMGW:<index>
OK
IferrorisrelatedtoMEfunctionality:
+CMSERROR:<err>
Parameters
<oa> GSM 03. 40 TP-Originating-AddressAddress-Valuefieldin
stringformat(stringshouldbeincludedinquotationmarks);BCDnumbers
(orGSMdefaultalphabetcharacters)areconvertedtocharactersofthe
currentlyselectedTEcharacterset(specifiedby+CSCSin 3 GPPTS
27. 007 );typeofaddressgivenby< tooa >
<da> GSM 03. 40 TP-Destination-AddressAddress-Valuefieldin
stringformat(stringshouldbeincludedinquotationmarks);BCDnumbers
(orGSMdefaultalphabetcharacters)areconvertedtocharactersofthe
currentlyselectedTEcharacterset(specifiedby +CSCS in 3 GPPTS
27. 007 );typeofaddressgivenby< toda >
<tooa> GSM 04. 11 TP-Originating-AddressType-of-Addressoctet in
integerformat(defaultrefer< toda >)
<toda> GSM 04. 11 TP-Destination-AddressType-of-Addressoctetin
integerformat(whenfirstcharacterof< da >is+(IRA 43 )defaultis 145 ,
otherwisedefaultis 129 )
129 Unknowntype(IDSNformatnumber)
161 Nationalnumbertype(IDSNformat)
145 Internationalnumbertype(ISDNformat)
177 Networkspecificnumber(ISDNformat)
<length> Integertypevalue(notexceed 160 bytes)indicatinginthetext
mode( +CMGF= 1 )thelengthofthemessagebody< data > (or< cdata >)in
characters;
orinPDUmode( +CMGF= 0 ),thelengthoftheactualTPdata
unitinoctets(i.e.theRPlayerSMSCaddressoctetsarenot
countedinthelength)
<stat> inthetextmode( +CMGF= 1 ):
"STOUNSENT" Storedunsentmessages
"STOSENT" Storedsentmessages
inPDUmode( +CMGF= 0 ):
0 Receivedunreadmessages
1 Receivedreadmessages
2 Storedunsentmessages
3 Storedsentmessages
<pdu> InthecaseofSMS:GSM 04. 11 SCaddressfollowedbyGSM
03. 40 TPDUinhexadecimalformat:ME/TAconvertseachoctetofTPdata
unitintotwoIRAcharacterlonghexadecimalnumber(e.g.octetwithinteger
value 42 ispresentedtoTEastwocharacters 2 A(IRA 50 and 65 )). Inthe
caseofCBS:GSM 03. 41 TPDUinhexadecimalformat.
<index> Indexofmessageinselectedstorage< mem 2 >
ExecutionCommand
AT+CMGW

Response
TAtransmitsSMSmessage(eitherSMS-DELIVERorSMS-SUBMIT)from
TEtomemorystorage< mem 2 >.Memorylocation< index >ofthestored
message is returned. By default message status will be set to 'stored
unsent',butparameter< stat >allowsalsootherstatusvaluestobegiven.
Ifwritingissuccessful:
+CMGW:<index>
OK
IferrorisrelatedtoMEfunctionality:
+CMSERROR:
ParameterSavingMode NO_SAVE
MaxResponseTime 5 s
Reference
3 GPPTS 27. 005
Note

4 2 7 AT+CMSS SendSMSMessagefromStorage.....................................................................
AT+CMSS SendSMSMessagefromStorage
TestCommand

AT+CMSS=?

Response
OK
WriteCommand
AT+CMSS=[,<
da>,]

Response
TAsends messagewith location value < index > from message storage
< mem 2 >tothenetwork(SMS-SUBMIT).Ifnewrecipientaddress< da >is
given, it shall be used instead of the one stored with the message.
Reference value < mr > is returned to the TE on successful message
delivery.Valuescanbeusedtoidentifymessageuponunsoliciteddelivery
statusreportresultcode.
1 )Iftextmode( +CMGF= 1 )andsendingsuccessful:
+CMSS:<mr>
OK
2 )IfPDUmode( +CMGF= 0 )andsendingsuccessful:
+CMSS:<mr>
OK
3 )IferrorisrelatedtoMEfunctionality:
+CMSERROR:
Parameters
Integertype;valueintherangeoflocationnumberssupported
bytheassociatedmemory
GSM 03. 40 TP-Destination-AddressAddress-Valuefieldin
stringformat(stringshouldbeincludedinquotationmarks);BCDnumbers
(orGSMdefaultalphabetcharacters)areconvertedtocharactersofthe
currentlyselectedTEcharacterset(specifiedby +CSCS in 3 GPPTS

007 );typeofaddressgivenby< toda >
GSM 04. 11 TP-Destination-AddressType-of-Addressoctet
inintegerformat(whenfirstcharacterof< da >is+(IRA 43 )defaultis 145 ,
otherwisedefaultis 129 )
GSM 03. 40 TP-Message-Referenceinintegerformat
ParameterSavingMode NO_SAVE
MaxResponseTime 60 s
Reference
3 GPPTS 27. 005
Note
4 2 8 AT+CNMI NewSMSMessageIndications............................................................................
AT+CNMI NewSMSMessageIndications
TestCommand
AT+CNMI=?

Response
+CNMI:( listofsupported <mode> s ),( listofsupported <mt> s ),( listof
supported <bm> s ),( listofsupported <ds> s ),( listofsupported <bfr> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CNMI?

Response
+CNMI:<mode>,<mt>,<bm>,<ds>,<bfr>
OK
Parameters
SeeWriteCommand
WriteCommand

**AT+CNMI=[,<
mt>[,[,[,<bfr

]]]]**

Response
TAselectstheprocedureforhowthereceivingofnewmessagesfromthe
networkisindicatedtotheTEwhenTEisactive,e.g.DTRsignalisON.If
TEisinactive(e.g.DTRsignalisOFF),messagereceivingshouldbedone
asspecifiedinGSM 03. 38.
OK
or
ERROR
Parameters
<mode> 0 BufferunsolicitedresultcodesintheTA.IfTAresultcode
bufferisfull,indicationscanbebufferedinsomeotherplaceortheoldest
indicationsmaybediscardedandreplacedwiththenewreceived
indications.
1 Discardindicationandrejectnewreceivedmessage
unsolicitedresultcodeswhenTA-TElinkisreserved(e.g.inon-linedata
mode).OtherwiseforwardthemdirectlytotheTE.
2 BufferunsolicitedresultcodesintheTAwhenTA-TElink
isreserved(e.g.inon-linedatamode)andflushthemtotheTEafter
reservation.OtherwiseforwardthemdirectlytotheTE.
<mt> (therulesforstoringreceivedSMsdependonitsdatacoding
scheme(referGSM 03. 38 [ 2 ]),preferredmemorystorage(+CPMS)setting
andthisvalue):
0 NoSMS-DELIVERindicationsareroutedtotheTE.
1 IfSMS-DELIVERisstoredintoME/TA,indicationofthe
memorylocationisroutedtotheTEusingunsolicitedresultcode:+CMTI:
<mem>,<index>
2 SMS-DELIVERs(exceptclass 2 )arerouteddirectlytothe
TEusingunsolicitedresultcode:
+CMT:[], (PDUmodeenabled)
or
+CMT:
,[],[,,,,,,,] (textmodeenabled;aboutparametersinitalics,refer
CommandShowTextModeParameters+CSDH).Class 2 messagesresult
inindicationasdefinedin< mt >= 1.
3 Class 3 SMS-DELIVERsarerouteddirectlytoTE
usingunsolicitedresultcodesdefinedin< mt >= 2 .Messagesofother
classes
resultinindicationasdefinedin< mt >= 1.
(therulesforstoringreceivedCBMsdependonitsdatacoding
scheme(referGSM 03. 38 [ 2 ]),thesettingofSelectCBMTypes(+CSCB)
andthisvalue):
0 NoCBMindicationsareroutedtotheTE.
2 NewCBMsarerouteddirectlytotheTEusingunsolicited
resultcode:
+CBM: (PDUmodeenabled)
or
+CBM:,,,, (text
modeenabled).
0 NoSMS-STATUS-REPORTsareroutedtotheTE.
1 SMS-STATUS-REPORTsareroutedtotheTEusing
unsolicitedresultcode:
+CDS: (PDUmodeenabled)
or
+CDS:,[,][,],,

, (textmodeenabled)
2 IfSMS-STATUS-REPORTisstoredintoME/TA,indication
ofthememorylocationisroutedtotheTEusingunsolicitedresultcode:
+CDSI:<mem 3 >,
0 TAbufferofunsolicitedresultcodesdefinedwithinthis
CommandisflushedtotheTEwhen< mode > 1 ... 3 isentered(OKresponse
shallbegivenbeforeflushingthecodes).
1 TAbufferofunsolicitedresultcodesdefinedwithinthis
commandisclearedwhen< mode > 1 ... 3 isentered
Unsolicitedresultcode
1 .Indicatesthatnewmessagehasbeenreceived
If< mt >= 1 :
+CMTI:<mem 3 >,
If< mt >= 2 (PDUmodeenabled):
+CMT:[],
If< mt >= 2 (textmodeenabled):
+CMT:
,[,,,,,,,]<
LF>
2 .Indicatesthatnewcellbroadcastmessagehasbeenreceived
If< bm >= 2 (PDUmodeenabled):
+CBM:<length><CR><LF><pdu>
If< bm >= 2 (textmodeenabled):
+CBM:<sn>,<mid>,<dcs>,<page>,<pages><CR><LF><data>
3 .IndicatesthatnewSMSstatusreporthasbeenreceived
If< ds >= 1 (PDUmodeenabled):
+CDS:
If< ds >= 1 (textmodeenabled):
+CDS:,[,][,],,

,
ParameterSavingMode -
MaxResponseTime -
Reference
3 GPPTS 27. 005

Note
 Thiscommandisusedtoselecttheprocedurehowreceivingofnew
messagesfromthenetworkisindicatedtotheTEwhenTEisactive,
e.g.DTRsignalisON.IfTEisinactive(e.g.DTRsignalisOFF).Ifset
<mt>＝ 2 ,<mt>＝ 3 or<ds>＝ 1 ,makesure<mode>＝ 1 ,otherwiseitwill
returnerror..
4 2 9 AT+CPMS PreferredSMSMessageStorage.......................................................................
AT+CPMS PreferredSMSMessageStorage
TestCommand

AT+CPMS=?

Response
+CPMS:( listofsupported <mem 1 > s ),( listofsupported <mem 2 > s ),( listof
supported <mem 3 > s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CPMS?

Response
+CPMS:<mem 1 >,<used 1 >,<total 1 >,<mem 2 >,<used 2 >,<total 2 >,
<mem 3 >,<used 3 >,<total 3 >
OK
ERROR
Parameters
SeeWriteCommand
WriteCommand

AT+CPMS=<mem 1 >[,<
mem 2 >[,<mem 3 >]]

Response
TAselectsmemorystorages<mem 1 >,<mem 2 >and<mem 3 >tobeusedfor
reading,writing,etc.
+CPMS:<used 1 >,<total 1 >,<used 2 >,<total 2 >,<used 3 >,<total 3 >
OK
ERROR
Parameters
<mem 1 > Messagestobereadanddeletedfromthismemorystorage
"SM"SIMmessagestorage
<mem 2 > Messageswillbewrittenandsenttothismemorystorage
"SM"SIMmessagestorage
<mem 3 > Receivedmessageswillbeplacedinthismemorystorageif
routingtoPCisnotset("+CNMI")
"SM"SIMmessagestorage
Integertype;Numberofmessagescurrentlyin
Integertype;Numberofmessagesstorablein
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 005 Note

4 2 10 AT+CRES RestoreSMSSettings...........................................................................................
AT+CRES RestoreSMSSettings
TestCommand
AT+CRES=?

Response
+CRES: listofsupported <profile> s
OK
Parameter
SeeWriteCommand
WriteCommand

AT+CRES=

Response
Executioncommandrestoresmessageservicesettingsfromnon-volatile
memorytoactivememory.ATAcancontainseveralprofilesofsettings.
SettingsspecifiedincommandsServiceCentreAddress+CSCAand Set
MessageParameters +CSMParerestored.Certainsettings may not be
supportedbythestorage(e.g.(U)SIMSMSparameters)andthereforecan
notberestored.
OK
ERROR
Parameter
<profile> 0 RestoreSMservicesettingsfromprofile 0
ExecutionCommand

AT+CRES

Response
Sameas AT+CRES= 0.
OK
IferrorisrelatedtoMEfunctionality:
+CMSERROR
ParameterSavingMode NO_SAVE

MaxResponseTime 5 s
Reference
3 GPPTS 27. 005

Note
4 2 11 AT+CSAS SaveSMSSettings................................................................................................
AT+CSAS SaveSMSSettings
TestCommand
AT+CSAS=?

Response
+CSAS: listofsupported <profile> s
OK
Parameter
SeeWriteCommand
WriteCommand

AT+CSAS=

Response
Execution command saves active message service settings to a
non-volatile memory. Settings specified in commands Service Centre
Address+CSCAandSetMessageParameters+CSMParesaved.Certain
settings may not be supported by the storage (e.g. (U)SIM SMS
parameters)andthereforecannotbesaved.
OK
ERROR
Parameter
<profile> 0 SaveSMservicesettinginprofile 0
ExecutionCommand

AT+CSAS

Response
Sameas AT+CSAS= 0
OK
IferrorisrelatedtoMEfunctionality:
+CMSERROR
ParameterSavingMode NO_SAVE
MaxResponseTime 5 s
Reference
3 GPPTS 27. 005

Note
4 2 12 AT+CSCA SMSServiceCenterAddress...............................................................................
AT+CSCA SMSServiceCenterAddress
TestCommand

AT+CSCA=?

Response
OK
ReadCommand Response

AT+CSCA? +CSCA:,[,]

OK
Parameters
SeeWriteCommand
WriteCommand

AT+CSCA=[,]

Response
TAupdatestheSMSCaddress,throughwhichmobileoriginatedSMSare
transmitted.Intextmode,settingisusedbysendandwritescommands.In
PDUmode,settingis usedby thesamecommands,butonlywhenthe
lengthoftheSMSCaddresscodedinto<pdu>parameterequalszero.
Note:TheCommandwritestheparametersinNON-VOLATILEmemory.
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
GSM 04. 11 RPSCaddressAddress-Valuefieldinstring
format(stringshouldbeincludedinquotationmarks);BCDnumbers(or
GSMdefaultalphabetcharacters)areconvertedtocharactersofthe
currentlyselectedTEcharacterset(specifiedby+CSCSin 3 GPPTS

007 );typeofaddressgivenby
ServicecenteraddressformatGSM 04. 11 RPSCaddress
Type-of-Addressoctetinintegerformat(defaultrefer)
Stringtype(stringshouldbeincludedinquotation
marks)
Servicecenteraddressalphadata
ParameterSavingMode NO_SAVE
MaxResponseTime 5 s
Reference
3 GPPTS 27. 005
Note
4 2 13 AT+CSDH ShowSMSTextModeParameters.....................................................................
AT+CSDH ShowSMSTextModeParameters
TestCommand
AT+CSDH=?

Response
+CSDH:( listofsupported <show> s )
OK
Parameter
SeeWriteCommand
ReadCommand

AT+CSDH?

Response
+CSDH:<show>
OK
Parameter
SeeWriteCommand
WriteCommand

AT+CSDH=

Response
TAdetermineswhetherdetailedheaderinformationisshownintextmode
resultcodes.
OK
Parameter
0 Donotshowheadervaluesdefinedincommands+CSCA
and+CSMP(,,,,and)nor
,orin+CMT,+CMGL,+CMGRresultcodesfor
SMS-DELIVERsandSMS-SUBMITsintextmode
1 Showthevaluesinresultcodes
ExecutionCommand

AT+CSDH

Response
OK
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference
3 GPPTS 27. 005

Note
4 2 14 AT+CSMP SetSMSTextModeParameters.........................................................................
AT+CSMP SetSMSTextModeParameters
TestCommand

AT+CSMP=?

Response
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CSMP?

Response
+CSMP:<fo>,<vp>,<pid>,<dcs>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CSMP=[[,
,,]]

Response
TAselectsvaluesforadditionalparametersneededwhenSMissenttothe
networkorplacedinastoragewhentextmodeisselected(+CMGF= 1 ).Itis
possibletosetthevalidityperiodstartingfromwhentheSMisreceivedby
theSMSC(< vp >isinrange 0 ... 255 ) or definetheabsolutetimeofthe
validityperiodtermination(< vp >isastring).
Note:TheCommandwritestheparameter<fo>inNON-VOLATILEmemory.
OK
Parameters
Dependingonthecommandorresultcode:firstoctetofGSM

40 SMS-DELIVER,SMS-SUBMIT(default 17 ),
SMS-STATUS-REPORT,orSMS-COMMAND(default 2 )inintegerformat.
SMSstatusreportissupportedundertextmodeif< fo >issetto 49.
DependingonSMS-SUBMIT< fo >setting:GSM 03. 40
TP-Validity-Periodeitherinintegerformat(default 167 )orintime-string
format(refer< dt >)
GSM 03. 40 TP-Protocol-Identifierinintegerformat(default 0 ).
GSM 03. 38 SMSDataCodingSchemeinIntegerformat.
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 005

Note
4 2 15 AT+CSMS SelectMessageService.......................................................................................
AT+CSMS SelectMessageService
TestCommand

AT+CSMS=?

Response
+CSMS:( listofsupported <service> s )
OK
Parameter
SeeWriteCommand
ReadCommand

AT+CSMS?

Response
+CSMS:<service>,<mt>,<mo>,<bm>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CSMS=

Response
+CSMS:<mt>,<mo>,<bm>
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
<service> 0 GSM 03. 40 and 03. 41 (thesyntaxofSMSATcommands
iscompatiblewith 3 GPPTS 27. 005 Phase 2 version 4. 7. 0 ;Phase 2 +
featureswhichdonotrequirenewCommandsyntaxmaybesupported(e.g.
correctroutingofmessageswithnewPhase 2 +datacodingschemes))
1 GSM 03. 40 and 03. 41 (thesyntaxofSMSATcommands
iscompatiblewith 3 GPPTS 27. 005 Phase 2 +
version;therequirementofsetting 1 is
mentionedundercorrespondingcommanddescriptions)
MobileTerminatedMessages:
0 Typenotsupported
1 Typesupported
MobileOriginatedMessages:
0 Typenotsupported
1 Typesupported
BroadcastTypeMessages:
0 Typenotsupported
1 Typesupported
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
3 GPPTS 27. 005

Note
5 ATCommandsSpecialforSIMCom.......................................................................................
5 1 Overview.................................................................................................................................................
Command Description
AT+CPOWD Poweroff
AT+CADC ReadADC
AT+CFGRI IndicateRIwhenusingURC
AT+CLTS Getlocaltimestamp

AT+CBAND Getandsetmobileoperationband
AT+CNSMOD Shownetworksystemmode
AT+CSCLK Configureslowclock
AT+CCID ShowICCID

AT+CDEVICE ViewCurrentFlashDeviceType
AT+GSV Displayproductidentificationinformation
AT+SGPIO ControltheGPIO
AT+SLEDS Setthetimerperiodofnetlight

AT+CNETLIGHT Closethenetlightoropenittoshining
AT+CSGS NetlightindicationofGPRSstatus
AT+CGPIO ControltheGPIObyPINIndex
AT+CBATCHK SetVBATcheckingfeatureON/OFF

AT+CNMP Preferredmodeselection
AT+CMNB PreferredselectionbetweenCAT-MandNB-IoT
AT+CPSMS PowerSavingModeSetting
AT+CEDRXS Extended-DRXSetting

AT+CPSI InquiringUEsysteminformation
AT+CGNAPN GetNetworkAPNinCAT-MOrNB-IOT
AT+CSDP ServiceDomainPreference
AT+MCELLLOCK LockthespecialCAT-Mcell

AT+NCELLLOCK LockthespecialNB-IOTcell
AT+NBSC ConfigureNB-IOTScramblingFeature
AT+CAPNMODE SelectthemodeofapplicationconfigureAPN
AT+CRRCSTATE QueryRRCState

AT+CBANDCFG ConfigureCAT-MOrNB-IOTBand
AT+CNACT APPNetworkActive
AT+CNCFG PDPConfigure

AT+CEDUMP Setwhetherthemoduleresetwhenthemoduleiscrashed
AT+CNBS ConfigureBandScanOptimizationforNB-IOT

AT+CNDS ConfigureServiceDomainPreferenceForNB-IOT
AT+CENG SwitchonoroffEngineeringMode
AT+CNACTCFG ConfigureIPProtocolType
AT+CTLIIC ControltheSwitchofIIC

AT+CWIIC WriteValuestoRegisterofIICDevice
AT+CRIIC ReadValuesfromRegisterofIICDevice
AT+CMCFG ManageMobileOperatorConfiguration
AT+CSIMLOCK SIMLock

AT+CRATSRCH ConfigureparameterforbetterRATsearch
AT+SPWM GeneratethePulse-Width-Modulation
AT+CASRIP ShowRemoteIPAddressandPortWhenReceivedData
AT+CEDRX ConfigureEDRXparameters

AT+CPSMRDP ReadPSMDynamicParameters
AT+CPSMCFG ConfigurePSMversionandMinimumThresholdValue
AT+CPSMCFGEXT ConfigureModemOptimizationofPSM
AT+CPSMSTATUS EnableDeepSleepWakeupIndication

AT+CEDRXRDP eDRXReadDynamicParameters
AT+CRAI ConfigureReleaseAssistanceIndicationinNB-IOTnetwork

5 2 DetailedDescriptionsofCommands.................................................................................................
5 2 1 AT+CPOWD Poweroff..............................................................................................................
AT+CPOWD PowerOff
WriteCommand

AT+CPOWD=

Response
[NORMALPOWERDOWN]
Parameter

0 Poweroffurgently(WillnotsendoutNORMALPOWERDOWN)
1 Normalpoweroff (WillsendoutNORMALPOWERDOWN)
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference
Note

5 2 2 AT+CADC ReadADC................................................................................................................
AT+CADC ReadADC
TestCommand

AT+CADC=?

Response
+CADC:( listofsupported <status> s ),( listofsupported <value> s )
OK
Parameters
<status> 1 Success
0 Fail
<value> Integer 0 , 100 - 1700
ReadCommand

AT+CADC?

Response
+CADC:<status>,<value>
OK
Parameters
SeeTestCommand
ParameterSavingMode NO_SAVE
MaxResponseTime 2 s

Reference Note

5 2 3 AT+CFGRI IndicateRIWhenUsingURC.............................................................................
AT+CFGRI IndicateRIWhenUsingURC
TestCommand
AT+CFGRI=?

Response
+CFGRI:( 0 - 2 )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CFGRI?

Response
+CFGRI:<status>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CFGRI=

Response
OK
ERROR
Parameters
0 Off
1 On(TCPIP,FTPandURCcontrolRIpin)
2 On(onlyTCPIPcontrolRIpin)
ParameterSavingMode -

MaxResponseTime -

Reference

Note
 RIpincannotcontrollby"AT+CFGRI"commandwhenmodulehascall
serviceorreceivingSMS.
5 2 4 AT+CLTS GetLocalTimestamp..............................................................................................
AT+CLTS GetLocalTimestamp
TestCommand

AT+CLTS=?

Response
+CLTS:"yy/MM/dd,hh:mm:ss+/-zz"
OK
ReadCommand
AT+CLTS?

Response
+CLTS:<mode>
OK
WriteCommand

AT+CLTS=

Response
OK
or
ERROR
Parameters
<mode>
0 Disable
1 Enable
UnsolicitedResultCode
When"getlocaltimestamp"functionisenabled,thefollowingURCmaybe
reportedifnetworksendsthemessagetotheMStoprovidetheMSwith
subscriberspecificinformation.
1 .Refreshnetworknamebynetwork:
*PSNWID:"<mcc>","<mnc>","<fullnetworkname>",<fullnetwork
nameCI>,"<shortnetworkname>",<shortnetworknameCI>
2 .Refreshtimeandtimezonebynetwork:
ThisisUTCtime,thetimequeriedbyAT+CCLKcommandislocaltime.
*PSUTTZ:<year>,<month>,<day>,<hour>,<min>,<sec>,"<time
zone>",<dst>
3 .Refreshnetworktimezonebynetwork:
+CTZV:"<timezone>"
4 .RefreshNetworkDaylightSavingTimebynetwork:
DST:
Parameters
Stringtype;mobilecountrycode
Stringtype;mobilenetworkcode
Stringtype;nameofthenetworkinfulllength.
Integertype;indicateswhethertoaddCI.
0 TheMSwillnotaddtheinitiallettersoftheCountry's
Nametothetextstring.
1 TheMSwilladdtheinitiallettersoftheCountry's
Nameandaseparator(e.g.aspace)tothetextstring.
Stringtype;abbreviatednameofthenetwork
Integertype;indicateswhethertoaddCI.
0 TheMSwill notaddthe initial letters oftheCountry's
Nametothetextstring.
1 TheMSwilladdtheinitiallettersoftheCountry's
Nameandaseparator(e.g.aspace)tothetextstring.
4 digitsofyear(fromnetwork)
Month(fromnetwork)
Day(fromnetwork)
Hour(fromnetwork)
Minute(fromnetwork)
Second(fromnetwork)
Stringtype;networktimezone.Ifthenetworktimezonehas
beenadjustedforDaylightSavingTime,thenetworkshallindicatethisby
includingthe(NetworkDaylightSavingTime)
NetworkDaylightSavingTime;thecontentofthis
indicatesthevaluethatusedtoadjustthenetworktimezone
0 NoadjustmentforDaylightSavingTime
1 + 1 houradjustmentforDaylightSaving
2 + 2 hoursadjustmentforDaylightSavingTime
others Reserved
ParameterSavingMode -
MaxResponseTime -

Reference

Note
SupportforthisCommandwillbenetworkdependent.
SetAT+CLTS= 1 ,itmeansusercanreceivenetworktimeupdating and
useAT+CCLKtoshowcurrenttime.
*PSUTTZmayreporttwice.
5 2 5 AT+CBAND GetandSetMobileOperationBand................................................................
AT+CBAND GetandSetMobileOperationBand
TestCommand

AT+CBAND=?

Response
+CBAND:( listofsupported <op_band> s )
OK
Parameter
SeeWriteCommand
ReadCommand

AT+CBAND?

Response
+CBAND:<op_band>
OK
Parameter
SeeWriteCommand
WriteCommand

**AT+CBAND=<op_band

**

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameter
<op_band> Astringparameterwhichindicatetheoperationband.
Andthefollowingstringsshouldbeincludedinquotationmarks.
EGSM_MODE
DCS_MODE
ALL_MODE
ParameterSavingMode AUTO_SAVE
MaxResponseTime -

Reference

Note
 Radiosettingsarestoredinnon-volatilememory.
 OnlyforGSM
5 2 6 AT+CNSMODShowNetworkSystemMode...........................................................................
AT+CNSMOD ShowNetworkSystemMode
TestCommand

AT+CNSMOD=?

Response
+CNSMOD:(listofsupported<n>s)
OK
Parameter
SeeWriteCommand
ReadCommand Response

AT+CNSMOD? +CNSMOD:,

OK
Parameter
SeeWriteCommand
WriteCommand

AT+CNSMOD=

Response
OK
ERROR:
Parameter

0 Disableautoreportthenetworksystemmodeinformation
1 Autoreportthenetworksystemmodeinformation,command:
+CNSMOD:
< stat >
0 noservice
1 GSM
3 EGPRS
7 LTEM 1
9 LTENB
ParameterSavingMode -
MaxResponseTime
Reference

5 2 7 AT+CSCLK ConfigureSlowClock..........................................................................................
AT+CSCLK ConfigureSlowClock
TestCommand

AT+CSCLK=?

Response
+CSCLK:( listofsupported <n> s )
OK
Parameter
SeeWriteCommand
ReadCommand

AT+CSCLK?

Response
+CSCLK:<n>
OK
Parameter
SeeWriteCommand
WriteCommand
AT+CSCLK=

Response
OK
or
ERROR
Parameter
0 Disableslowclock,modulewillnotentersleepmode.
1 Enableslowclock,itiscontrolledbyDTR.WhenDTRis
high,modulecanentersleepmode.WhenDTRchangestolow
level,modulecanquitsleepmode.
ParameterSavingMode AUTO_SAVE

MaxResponseTime -

Reference
Note

5 2 8 AT+CCID ShowICCID..............................................................................................................
AT+CCID ShowICCID
TestCommand

AT+CCID=?

Response
OK
ExecutionCommand

AT+CCID

Response
Cciddata [ex. 898600810906 F 8048812 ]
OK
ParameterSavingMode NO_SAVE

MaxResponseTime 2 s

Reference
Note

5 2 9 AT+CDEVICE ViewCurrentFlashDeviceType...................................................................
AT+CDEVICE ViewCurrentFlashDeviceType
ReadCommand

AT+CDEVICE?

Response
DeviceName:Currentflashdevicetype
RamSize:CurrentRAMsize
OK
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
V. 25 ter

Note
5 2 10 AT+GSV DisplayProductIdentificationInformation............................................................
AT+GSV DisplayProductIdentificationInformation
ExecutionCommand

AT+GSV

Response
TAreturnsproductinformationtext
Example:
SIMCOM_Ltd
SIMCOM_SIM 7000
Revision: 1351 B 01 SIM 7000
OK
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

5 2 11 AT+SGPIO ControltheGPIO..................................................................................................
AT+SGPIO ControltheGPIO
TestCommand

AT+SGPIO=?

Response
+SGPIO:( 0 - 1 ),( 0 - 4 ),( 0 - 1 ),( 0 - 1 )
OK
Parameters
SeeWriteCommand
WriteCommand

**AT+SGPIO=<operation

,,,<
level>**

Response
OK
or
ERROR
Parameters
<operation>
0 SettheGPIOfunctionincludingtheGPIOoutput.
1 ReadtheGPIOlevel.Pleasenotethatonlywhenthegpioisset
asinput,usercanuseparameter 1 toreadtheGPIOlevel,otherwisethe
modulewillreturn"ERROR".
<GPIO> TheGPIOyouwanttobeset.(Ithasrelationswiththehardware,
pleaserefertothehardwaremanual)
<function> Onlywhen< operation >issetto 0 ,thisoptiontakeseffect.
0 SettheGPIOtoinput.
1 SettheGPIOtooutput
0 SettheGPIOlowlevel
1 SettheGPIOhighlevel
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference
Note

5 2 12 AT+SLEDS SettheTimerPeriodofNetLight......................................................................
AT+SLEDSSettheTimerPeriodofNetLight
TestCommand

AT+SLEDS=?

Response
+SLEDS:( 1 - 3 ),( 0 , 40 - 65535 ),( 0 , 40 - 65535 )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+SLEDS?

Response
+SLEDS:<mode>,<timer_on>,<timer_off>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+SLEDS=,,<timer_off>

Response
OK
ERROR
Parameters

1 Set the timer periodofnet lightwhile SIM 7000 series does not
registertothenetwork
2 SetthetimerperiodnetlightwhileSIM 7000 serieshasalready
registeredtothenetwork
3 SetthetimerperiodnetlightwhileSIM 7000 seriesisinthestateof
PPPcommunication
< timer_on >
Timerperiodof"LEDON"indecimalformatwhichrangeis 0 or
40 - 65535 (ms)
< timer_off >
Timerperiodof"LEDOFF"indecimalformatwhichrangeis 0 or
40 - 65535 (ms)
ParameterSavingMode -
MaxResponseTime -
Reference Note

Thedefaultvalueis:
<mode>,<timer_on>,<timer_off>
1 , 64 , 800
2 , 64 , 3000
3 , 64 , 300
5 2 13 AT+CNETLIGHT ClosetheNetLightorOpenIttoShining...............................................
AT+CNETLIGHTClosetheNetLightorOpenIttoShining
TestCommand

AT+CNETLIGHT=?

Response
+CNETLIGHT: ( 0 , 1 )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CNETLIGHT?

Response
+CNETLIGHT:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CNETLIGHT=

Response
OK
ERROR
Parameters

0 Closethenetlight
1 Openthenetlighttoshining
ParameterSavingMode AUTO_SAVE
MaxResponseTime -
Reference Note

5 2 14 AT+CSGS NetlightIndicationofGPRSStatus.....................................................................
AT+CSGSNetlightIndicationofGPRSStatus
TestCommand

AT+CSGS=?

Response
+CSGS: ( 0 - 2 )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CSGS?

Response
+CSGS:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CSGS=

Response
OK
ERROR
Parameters

0 Disable
1 Enable,thenetlightwillbeforcedtoenterinto 64 mson/ 300 msoff
blinkingstateinGPRSdatatransmissionservice.Otherwise,the
netlightstateisnotrestricted.
2 Enable,thenetlightwillblinkaccordingto AT+SLEDS inGPRSdata
transmissionservice.
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

5 2 15 AT+CGPIO ControltheGPIObyPINIndex..........................................................................
AT+CGPIO ControltheGPIObyPINIndex
TestCommand
AT+CGPIO=?

Response
+CGPIO:( 0 - 1 ),( listofsupported< pin >s ),( 0 - 1 ),( 0 - 1 )
OK
Parameters
SeeWriteCommand
WriteCommand

**AT+CGPIO=<operation

,,,**

Response
OK
or
ERROR
Parameters
<operation>
0 SettheGPIOfunctionincludingtheGPIOoutput.
1 ReadtheGPIOlevel.Pleasenotethatonlywhenthegpioisset
asinput,usercanuseparameter 1 toreadtheGPIOlevel,otherwisethe
modulewillreturn"ERROR".
The PIN index you wantto beset. (Ithas relations withthe
hardware,pleaserefertothehardwaremanual)
Onlywhen< operation >issetto 0 ,thisoptiontakeseffect.
0 SettheGPIOtoinput.
1 SettheGPIOtooutput

0 SettheGPIOlowlevel
1 SettheGPIOhighlevel
ParameterSavingMode -
MaxResponseTime -

Reference Note

5 2 16 AT+CBATCHK SetVBATCheckingFeatureON/OFF........................................................
AT+CBATCHK SetVBATCheckingFeatureON/OFF
TestCommand

AT+CBATCHK=?

Response
+CBATCHK:( 0 , 1 )
OK
ReadCommand

AT+CBATCHK?

Response
+CBATCHK:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand

**AT+CBATCHK=<mode

**

Response
OK
Iffailed:
+CMEERROR:
Parameters
0 ClosethefunctionofVBATchecking
1 OpenthefunctionofVBATchecking
ParameterSavingMode AUTO_SAVE
MaxResponseTime -
Reference Note

5 2 17 AT+CNMP PreferredModeSelection....................................................................................
AT+CNMP PreferredModeSelection
TestCommand

AT+CNMP=?

Response
+CNMP:( listofsupported <mode> s )
OK
ReadCommand

AT+CNMP?

Response
+CNMP:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CNMP=

Response
OK
Iffailed:
+CMEERROR:
Parameters
2 Automatic
13 GSMonly
38 LTEonly
51 GSMandLTEonly
ParameterSavingMode AUTO_SAVE
MaxResponseTime -

Reference
Note
Defaultvalueofparameter < mode > is differentamong SIM 7000 series
project.

5 2 18 AT+CMNB PreferredSelectionbetweenCAT-MandNB-IoT............................................
AT+CMNB PreferredSelectionbetweenCAT-MandNB-IoT
TestCommand
AT+CMNB=?

Response
+CMNB:( listofsupported <mode> s )
OK
ReadCommand

AT+CMNB?

Response
+CMNB:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CMNB=

Response
OK
Iffailed:
+CMEERROR:
Parameters
1 CAT-M
2 NB-Iot
3 CAT-MandNB-IoT
ParameterSavingMode AUTO_SAVE

MaxResponseTime -

Reference

Note
Defaultvalueofparameter < mode > is differentamong SIM 7000 series
project.
5 2 19 AT+CPSMS PowerSavingModeSetting..............................................................................
AT+CPSMS PowerSavingModeSetting
TestCommand

AT+CPSMS=?

Response
+CPSMS: ( list of supported < mode >s),(list of supported
< Requested_Periodic-RAU >s),(list of supported
< Requested_GPRS-READY-timer >s),(list of supported
< Requested_Periodic-TAU >s),(list of supported
< Requested_Active-Time >s )
OK
ReadCommand

AT+CPSMS?

Response
+CPSMS: <mode>,[<Requested_Periodic-RAU>],[<Requested_GPRS-
READY-timer>],[<Requested_Periodic-TAU>],[<Requested_Active-Tim
e>]
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CPSMS=[[,
<Requested_Periodic-
RAU>[,<Requested_G
PRS-READY-timer>[,<
Requested_Periodic-T
AU>[,<Requested_Acti
ve-Time>]]]]]

Response
OK
Iffailed:
+CMEERROR:<err>
Parameters
<mode>
0 DisabletheuseofPSM
1 EnabletheuseofPSM
<Requested_Periodic-RAU> Notsupported
<Requested_GPRS-READY-timer> Notsupported
<Requested_Periodic-TAU>
Stringtype;onebyteinan 8 bitformat.Requestedextendedperiodic
TAUvalue (T 3412 ) to be allocated tothe UE in E-UTRAN. The
requested extended periodic TAU value is coded as one byte
(octet 3 ) of the GPRSTimer 3 information elementcoded as bit
format(e.g." 01000111 "equals 70 hours).For thecodingandthe
value range,see theGPRS Timer 3 IEin 3 GPP TS 24. 008 [ 8 ]
Table 10. 5. 163 a/ 3 GPPTS 24. 008 .Seealso 3 GPPTS 23. 682 [ 149 ]
and 3 GPP TS 23. 401 [ 82 ]. The default value, if available, is
manufacturerspecific.
<Requested_Active-Time>
Stringtype;onebyteinan 8 bitformat.RequestedActiveTimevalue
(T 3324 )tobeallocatedtotheUE.TherequestedActiveTimevalue
is codedasonebyte(octet 3 )oftheGPRSTimer 2 information
elementcodedasbitformat(e.g." 00100100 "equals 4 minutes).For
the coding and the value range, see the GPRS Timer 2 IE in
3 GPP TS 24. 008 [ 8 ]Table 10. 5. 163 / 3 GPP TS 24. 008. See also
3 GPP TS 23. 682 [ 149 ], 3 GPP TS 23. 060 [ 47 ] and
3 GPPTS 23. 401 [ 82 ].Thedefaultvalue,ifavailable,ismanufacturer
specific.
ParameterSavingMode AUTO_SAVE
MaxResponseTime -

Reference Note

5 2 20 AT+CEDRXS Extended-DRXSetting.....................................................................................
AT+CEDRXS Extended-DRXSetting
TestCommand
AT+CEDRXS=?

Response
+CEDRXS:( listofsupported
<n> s ),<AcT-type>,<Requested_eDRX_value>
OK
ReadCommand

AT+CEDRXS?

Response
+CEDRXS:<AcT-type>,<Requested_eDRX_value>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CEDRXS=,,<Requested_e

Response
OK
Iffailed:
DRX_value> +CMEERROR:

Parameters

0 DisabletheuseofeDRX
1 EnabletheuseofeDRX
2 EnabletheuseofeDRXandautoreport
3 DisabletheuseofeDRX(Reserved)
<AcT-type>
4 CAT-M
5 NB-IoT
<Requested_eDRX_value> RequestedeDRXvalue. 4 bitformat.
" 0000 "-" 1111 "
ParameterSavingMode AUTO_SAVE

MaxResponseTime -

Reference

Note
 TheRequested_eDRX_valueisthevalueofcyclelength,separately
means
5. 12 , 10. 24 , 20. 48 , 40. 96 , 61. 44 , 81. 92 , 102. 40 , 122. 88 , 143. 36 , 163. 84 , 327
. 68 , 655. 36 , 1310. 72 , 2621. 44 , 5242. 88 , 10485. 76 .(seconds)

5 2 21 AT+CPSI InquiringUESystemInformation...........................................................................
AT+CPSI InquiringUESystemInformation
TestCommand

AT+CPSI=?

Response
OK
ReadCommand

AT+CPSI?

Ifcampingonagsmcell:
+CPSI : <System Mode> , <OperationMode> , <MCC> - <MNC> , <LAC> , <C
ell ID> , <Absolute RF Ch Num> , <RxLev> , <TrackLOAdjust> , <C 1 - C
2 >
OK
IfcampingonaCAT-MorNB-IOTcell:
+CPSI : <System Mode> , <Operation Mode> , <MCC> - <MNC> , <TAC> , <S
CellID> , <PCellID> , <Frequency Band> , <earfcn> , <dlbw> , <ulbw> , <RSR
Q> , <RSRP> , <RSSI> , <RSSNR>
OK
If no service:
+CPSI : NOSERVICE , Online
OK
Iffailed:
+CMEERROR:
Parameters
Systemmode.
"NOSERVICE"
"GSM"
"LTECAT-M 1 "
"LTENB-IOT"
UEoperationmode.
"Online",
"Offline",
"FactoryTestMode",
"Reset",
"LowPowerMode".
MobileCountryCode(firstpartofthePLMNcode)
MobileNetwork Code(secondpartofthePLMNcode)
LocationAreaCode(hexadecimaldigits)
Service-cell Identify
AFRCNfor service-cell.
Track LOAdjust
<C 1 > Coefficientfor base stationselection
<C 2 > Coefficientfor Cell re-selection
TracingAreaCode
Serving Cell ID
Physical CellID
FrequencyBandofactiveset
E-UTRAabsoluteradiofrequencychannelnumber for se
arching CAT-Mor NB-IOT cells
Transmissionbandwidthconfigurationof theservingcello
n thedownlink
Transmissionbandwidth configurationoftheservingcell
on theuplink
Currentreferencesignal received power.Availablefor CA
T-Mor NB-IOT.
Currentreferencesignal receivequality asmeasuredbyL 1.
CurrentReceivedsignalstrengthindicator
Averagereferencesignal signal-to-noiseratiooftheservi
ngcellThe valueof SINR canbecalculatedaccording to ,t
heformulais as below:
SINR= 2 * - 20
Therangeof SINR isfrom- 20 to 30
ParameterSavingMode -
MaxResponseTime -

Reference Note

5 2 22 AT+CGNAPN GetNetworkAPNinCAT-MOrNB-IOT.....................................................
AT+CGNAPN GetNetworkAPNinCAT-MOrNB-IOT
TestCommand

AT+CGNAPN=?

Response
+CGNAPN:( listofsupported <valid> s ),<length>
OK
ExecutionCommand

AT+CGNAPN

Response
+CGNAPN:<valid>,<Network_APN>
OK
Iffailed:
+CMEERROR:
Parameters

0 The network did not sent APN parameter to UE.In the
case,< Network_APN> isNULL.
1 ThenetworksentAPNparametertoUE.

Maxthelengthof <network_APN>.
<Network_APN>
String type.The network sends APN parameter to UE when UE
registers CAT-M or NB-IOT network successfully.In
GSM,< Network_APN> alwaysisNULL.
ParameterSavingMode -
MaxResponseTime -

Reference

Note
 InCAT-MorNB-IOT,afterUEsendingattachrequestmessage,Ifcore
network responds attach accept message that includes APN
parameter, <Netwok_APN> isvalid.
5 2 23 AT+CSDP ServiceDomainPreference...............................................................................
AT+CSDP ServiceDomainPreference
TestCommand

AT+CSDP=?

Response
+CSDP:( listofsupported <domain> s )
OK
ReadCommand
AT+CSDP?

Response
+CSDP:<domain>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CSDP=

Response
OK
Iffailed:
+CMEERROR:
Parameters

0 CS(CircuitSwitchedDomain)ONLY
1 PS(PacketSwitchedDomain)ONLY
2 CS(CircuitSwitchedDomain)+PS(PacketSwitchedDomain)
ParameterSavingMode AUTO_SAVE_REBOOT
MaxResponseTime -
Reference Note

5 2 24 AT+MCELLLOCKLockthespecialCAT-Mcell.....................................................................
AT+MCELLLOCK LockthespecialCAT-Mcell
TestCommand

AT+MCELLLOCK=?

Response
+MCELLLOCK:( 0 , 1 ),( 0 - 65535 ),( 0 - 503 )
OK
ReadCommand

AT+MCELLLOCK?

Response
+MCELLLOCK:<mode>[,<earfcn>,<pci>]
OK
Parameters
SeeWriteCommand
WriteCommand

AT+MCELLLOCK=[,,]

Response
OK
Iffailed:
+CMEERROR:
Parameter
0 Unlock
1 Lock
Anumberintherange 0 - 65535 representingtheEARFCN
tosearch
Anumberintherange 0 - 503 representingthePhysicalCellID
tosearch
ParameterSavingMode AUTO_SAVE_REBOOT
MaxResponseTime -
Reference Note

5 2 25 AT+NCELLLOCKLockthespecialNB-IOTcell....................................................................
AT+NCELLLOCK LockthespecialNB-IOTcell
TestCommand
AT+NCELLLOCK=?

Response
+NCELLLOCK:( 0 , 1 ),( 0 - 65535 ),( 0 - 503 )
OK
ReadCommand

AT+NCELLLOCK?

Response
+NCELLLOCK:<mode>[,<earfcn>,<pci>]
OK
Parameters
SeeWriteCommand
WriteCommand

AT+NCELLLOCK=[,,]

Response
OK
Iffailed:
+CMEERROR:
Parameter
0 Unlock
1 Lock
Anumberintherange 0 - 65535 representingtheEARFCN
tosearch
Anumberintherange 0 - 503 representingthePhysicalCellID
tosearch
ParameterSavingMode AUTO_SAVE_REBOOT
MaxResponseTime -
Reference Note

5 2 26 AT+NBSC ConfigureNB-IOTScramblingFeature............................................................
AT+NBSC ConfigureNB-IOTScramblingFeature
TestCommand
AT+NBSC=?

Response
+NBSC:( listofsupported <mode> s )
OK
ReadCommand
Response
+NBSC:

AT+NBSC?
OK
Parameters
SeeWriteCommand
WriteCommand

AT+NBSC=

Response
OK
Iffailed:
+CMEERROR:
Parameters

0 DisablethescramblingfeatureinNB-IOTnetwork.
1 EnablethescramblingfeatureinNB-IOTnetwork.
ParameterSavingMode AUTO_SAVE_REBOOT

MaxResponseTime -

Reference

Note
 PleaseconfigureUEinaccordancewiththebasestation,OtherwiseUE
cannotregisterNB-IOTnetwork.
5 2 27 AT+CAPNMODE SelecttheModeofApplicationConfigureAPN..................................
AT+CAPNMODE SelecttheModeofApplicationConfigureAPN
TestCommand

AT+CAPNMODE=?

Response
+CAPNMODE:( listofsupported <mode> s )
OK
ReadCommand

AT+CAPNMODE?

Response
+CAPNMODE:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CAPNMODE=

Response
OK
Iffailed:
+CMEERROR:<err>
Parameters
<mode> modeofapplicationconfigureAPN.InCAT-MorNB-IOT
network,ifmodule has registeredtothe network successfully,i
twill get anAPNfrombasestationdelivering.
0 Automaticmode.Applications(AT+CSTTandAT+SAPBR)donot
needtoconfigAPN,itwillusetheAPNfrombasestation
delivering.
1 Manualmode,Applications(AT+CSTT,AT+SAPBR)needtoconfig
APN,theseAPNscangetfromoperators.
ParameterSavingMode -
MaxResponseTime -

Reference
Note
 IfmoduleareusinginGPRSnetwork,youmustconfig to 1

5 2 28 AT+CRRCSTATE QueryRRCState....................................................................................
AT+CRRCSTATE QueryRRCState
TestCommand
AT+CRRCSTATE=?

Response
+CRRCSTATE:( listofsupported <n> s )
OK
ReadCommand

AT+CRRCSTATE?

Response
+CRRCSTATE:<n>,<state>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CRRCSTATE=

Response
OK
Iffailed:
+CMEERROR:
Parameters
Integertype
0 Disableunsolicitedresultcode
1 Enableunsolicitedresultcode "+CRRCSTATE:"
< state > Integertype,indicatesRRCconnectionstate
0 Idle
1 Connected
255 Other
ParameterSavingMode -

MaxResponseTime -

Reference

Note
 ThecommandisonlyvalidthatmoduleregisteringinCAT-MorNB-IOT
network.
5 2 29 AT+CBANDCFG ConfigureCAT-MOrNB-IOTBand.......................................................
AT+CBANDCFG ConfigureCAT-MOrNB-IOTBand
TestCommand

AT+CBANDCFG=?

Response
+CBANDCFG:(CAT-M,NB-IOT) ,(listofsupported <band> s)
OK
ReadCommand

AT+CBANDCFG?

Response
+CBANDCFG:"CAT-M",<band>[,<band>...]
<CR><LF>+CBANDCFG:"NB-IOT",<band>[,<band>...]
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CBANDCFG=,[,...]

Response
OK
Iffailed:
+CMEERROR:
Parameters
stringtype;networksystemmode.
" CAT-M " LTECat.M 1 (eMTC)
" NB-IOT " NarrowBandInternetofThings
< band > Integer type;Thevalueof< band > mustisinthebandlistof
gettingfrom AT+CBANDCFG=?
ParameterSavingMode AUTO_SAVE
MaxResponseTime -

Reference

Note
 Thecommandcantakeeffectimmediately,Itdoesnotneedtoreboot
module.
5 2 30 AT+CNACT APPNetworkActive..........................................................................................
AT+CNACT APPNetworkActive
ReadCommand

AT+CNACT?

Response
+CNACT:<status>,<ip_addr>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CNACT=[,
]

Response
OK
Iffailed:
+CMEERROR:<err>
Parameters

0 Deactive
1 Active
2 AutoActive

(AccessPointName)Astringparameter(stringshouldbeincludedin
quotationmarks)whichisalogicalnamethatisusedtoselectthe
GGSNortheexternalpacketdatanetwork.Ifthevalueisnullor
omitted,thenthesubscriptionvaluewillberequested.Thedefault
valueisNULL.
< status >
0 Deactived
1 Actived
2 Inoperation
ParameterSavingMode NO_SAVE

MaxResponseTime -

Reference

Note
"+APPPDP:ACTIVE"willbereportediftheappnetworkactived,and"+APP
PDP:DEACTIVE"willbereportediftheappnetworkdeactived.
AutoActivemeansthewillactiveautomaticallyiftheactivationfailed.
5 2 31 AT+CNCFG PDPConfigure...................................................................................................
AT+CNCFG PDPConfigure
TestCommand
AT+CNCFG=?

Response
+CNCFG: (list of supported
< ip_type >s) ,<len_APN>,<len_usename>,<len_password>, (list of
supported< authentication >s)
OK
ReadCommand
AT+CNCFG?

Response
+CNCFG:
<ip_type>,<APN>,<usename>,<password>,<authentication>
OK
WriteCommand
**AT+CNCFG=<ip_type>[,[,,<password

[,]]]**

Response
OK
Iffailed:
+CMEERROR:
ParameterSavingMode -

MaxResponseTime -

Reference

DefinedValues
0 Deactive
1 Active
2 AutoActive
<ip_type> PacketDataProtocoltype)AIntegertypeparameterwhichspecifies
thetypeofpacketdataprotocol.
0 DualPDNStack
1 InternetProtocolVersion 4
2 InternetProtocolVersion 6
(AccessPointName)Astringparameter(stringshouldbeincludedin
quotationmarks)whichisalogicalnamethatis usedtoselectthe
GGSNor theexternal packetdatanetwork.If the valueis null or
omitted, then the subscription value will be requested.The default
valueisNULL.
Usernameforauthentication.

Passwordforauthentication.
0 NONE
1 PAP
2 CHAP
3 PAPorCHAP
<len_APN> Integertype.Maximumlengthofparameter.
<len_name> Integertype.Maximumlengthofparameter.
<len_password> Integertype.Maximumlengthofparameter.

5 2 32 AT+CEDUMP SetWhethertheModuleResetWhenTheModuleisCrashed.............
AT+CEDUMP SetWhethertheModuleResetWhenTheModuleisCrashed
ReadCommand
AT+CEDUMP?

Response
+CEDUMP:<mode>
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
SeeWriteCommand
WriteCommand
AT+CEDUMP=

Response
OK
IferrorisrelatedtoMEfunctionality:
+ CMEERROR:<err>
Parameters

0 Themodulewillresetwhenthemoduleiscrashed(Default)
1 Themodulewillgointodownloadmodewhenthemoduleis
crashed
ParameterSavingMode -

MaxResponseTime
Reference
Note

5 2 33 AT+CNBS ConfigureBandScanOptimizationForNB-IOT.............................................
AT+CNBS ConfigureBandScanOptimizationforNB-IOT
TestCommand

AT+CNBS=?

Response
+CNBS:( 1 - 5 )
OK
ReadCommand

AT+CNBS?

Response
+CNBS:<n>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CNBS=

Response
OK
Iffailed:
+CMEERROR:<err>
Parameters
BandscanisperformedinthefollowinglevelsbasedontheSNR:
level 0 UsedforgoodSNRlevels( 0 dbandabove);detectsstrongcells
firstandtakestheshortesttimetoacquirecells.UEscanseach
rasterin 30 ms.
level 1 UsedformediumSNRlevels(- 9 dBandabove),UEscanseach
rasterfor 200 ms
level 2 UsedforpoorSNRlevels(- 12. 6 dBandabove),UEscanseach
rasterfor 500 ms.
<n>
1 UEtriesSNRlevel 0 bandscan
2 UEtriesSNRlevel 0 andlevel 1 bandscan
3 UEtriesSNRlevel 0 ,level 1 ,andlevel 2 bandscan
4 Reserved
5 UEtriesSNRlevel 2 bandscanonly
ParameterSavingMode AUTO_SAVE_REBOOT
MaxResponseTime -

Reference

Note
 ThecommandcontrolsthebandscanfordifferentSNRlevels.This
optimizationisapplicableonlyforNB-IOTanditreducesthebandscan
timeandpowerconsumption.
5 2 34 AT+CNDS ConfigureServiceDomainPreferenceForNB-IOT......................................
AT+CNDS ConfigureServiceDomainPreferenceForNB-IOT
TestCommand

AT+CNDS=?

Response
+CNDS:(listofsupported<domain>s)
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CNDS?

Response
+CNDS:<domain>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CNDS=

Response
OK
Iffailed:
+CMEERROR:
Parameters

1 PS(PacketSwitchedDomain)ONLY
2 CS(CircuitSwitchedDomain)+PS(PacketSwitchedDomain)
ParameterSavingMode AUTO_SAVE_REBOOT
MaxResponseTime -

Reference

Note
 The command of AT+CSDP is used to config service domain
preferenceforGSMandCAT-M.Ifyouwanttoconfigservicedomain
preferenceforNB-IOT,youcanuse AT+CNDS.
5 2 35 AT+CENG SwitchOnorOffEngineeringMode.................................................................
AT+CENG SwitchOnorOffEngineeringMode
TestCommand

AT+CENG=?

Response
TAreturnsthelistofsupportedmodes.
+CENG:( listofsupported <mode> s ),( listofsupported <Ncell> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CENG?

Response
EngineeringModeisdesignedtoallowafieldengineertoviewandtestthe
networkinformationreceivedbyahandset,whenthehandsetiseitherin
idlemodeordedicatedmode(thatis:withacallactive).Ineachmode,the
engineerisabletoviewnetworkinteractionforthe"servingcell"(thecellthe
handsetiscurrentlyregisteredwith)orfortheneighboringcells.
TAreturnsthecurrentengineeringmode.Thenetworkinformationincluding
servingcellandneighboringcellsarereturned.< cell >carrywiththem
correspondingnetworkinteraction.
Ifcampingonagsmcell:
+CENG:<mode>,<Ncell>,<cellnum>,<SystemMode>
[+CENG:,",,, , ,,"
+CENG:
<cell>,"<bcch>,<rxl>,<bsic>,<cellid>,<mcc>,<mnc>,<lac>"...]
OK
IfcampingonaCAT-MorNB-IOTcell:
+CENG:<mode>,<Ncell>,<cellnum>,<SystemMode>
[+CENG:
<cell>,"<earfcn>,<pci>,<rsrp>,<rssi>,<rsrq>,<sinr>,<tac>,<cellid>,<mc
c>,<mnc>,<txpower>"
<CR><LF>+CENG:
<cell>,"<earfcn>,<pci>,<rsrp>,<rssi>,<rsrq>,<sinr>"...]
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CENG=[,<
Ncell>]

Switchonoroffengineeringmode.
OK
Iffailed:
+CMEERROR:<err>
Parameters
<mode> 0 Switchoffengineeringmode
1 Switchonengineeringmode
<Ncell> 1 DisplayneighborcellID
<cellnum> Thenumberofcell,itincludesservingcellandneighborcells.
<SystemMode> Systemmode.
"NOSERVICE"
"GSM"
"LTECAT-M 1 "
"LTENB-IOT"
<cell> 0 Theservingcell
1 - 6 Theindexoftheneighboringcell
<bcch> ARFCN(Absoluteradiofrequencychannelnumber)ofBCCH
carrier,indecimalformat
<rxl> Receivelevel,indecimalformat
<mcc> Mobilecountrycode,indecimalformat
<mnc> Mobilenetworkcode,indecimalformat
<bsic> Basestationidentitycode,indecimalformat
<cellid> Cellid,inhexadecimalformat
<lac> Locationareacode,inhexadecimalformat
<earfcn> E-UTRAabsoluteradio frequency channel number forsea
rchingCAT-Mor NB-IOT cells
<pci> Physical Cell ID
<rsrp> Current referencesignal receivedpower.Availablefor
CAT-Mor NB-IOT.
<rssi> CurrentReceivedsignalstrengthindicator
<rsrq> Current referencesignal receivequality as measuredby
L 1.
<sinr> Signal toInterferenceplusNoise Ratio,Therangeisfrom
20 to 30.
TracingAreaCode, indecimalformat
Txpowervaluein 1 / 10 dBm. isonlymeaningful
whenthedeviceisintraffic.Whenthereisnotraffic,thevalue
isinvalid.Thevalueof is 255.
ParameterSavingMode -
MaxResponseTime -

Reference
Note

5 2 36 AT+CNACTCFG ConfigureIPProtocolType......................................................................
AT+CNACTCFG ConfigureIPProtocolType
TestCommand
Response
+CNACTCFG:("IPV 4 ","IPV 6 ","IPV 4 V 6 ")

AT+CNACTCFG=?
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CNACTCFG?

Response
+CNACTCFG:<IPType>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CNACTCFG=

Response
OK
Iffailed:
+CMEERROR:
Parameters

"IPV 4 " IPv 4 protocol
"IPV 6 " IPv 6 protocol
"IPV 4 V 6 " IPv 4 andIPv 6 protocol
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference
Note

5 2 37 AT+CTLIIC ControltheSwitchofIIC....................................................................................
AT+CTLIIC ControltheSwitchofIIC
TestCommand

AT+CTLIIC=?

Response
+CTLIIC:( 0 , 1 )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CTLIIC?

Response
+CTLIIC:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CTLIIC=

Response
OK
or
ERROR
Parameters

0 SwitchofftheIIC
1 SwitchontheIIC
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

5 2 38 AT+CWIIC WriteValuestoRegisterofIICDevice.............................................................
AT+CWIICWriteValuestoRegisterofIICDevice
TestCommand

AT+CWIIC=?

Response
OK
WriteCommand

AT+CWIIC=,,,

Response
OK
or
ERROR
Parameters
< addr > Deviceaddress.Inputformatmustbehex,suchas 0 xFF.
< reg > Registeraddress.Inputformatmustbehex,suchas 0 xFF.
< len > Readlength.Range: 1 - 4 ;unit:byte.
< data > Datawritten.Inputformatmustbehex,suchas
0 xFF– 0 xFFFFFFFF
ParameterSavingMode -
MaxResponseTime -
Reference Note

5 2 39 AT+CRIIC ReadValuesfromRegisterofIICDevice.........................................................
AT+CRIIC ReadValuesfromRegisterofIICDevice
TestCommand

AT+CRIIC=?

Response
OK
WriteCommand

AT+CRIIC=,,

Response
+CRIIC:<data>
OK
or
ERROR
Parameters
< addr > Deviceaddress.Inputformatmustbehex,suchas 0 xFF.
< reg > Registeraddress.Inputformatmustbehex,suchas 0 xFF.
< len > Readlength.Range: 1 - 4 ;unit:byte.
< data > Dataread.Inputformatmustbehex,suchas 0 xFF.
ParameterSavingMode -
MaxResponseTime -
Reference Note

5 2 40 AT+CMCFG ManageMobileOperatorConfiguration........................................................
AT+CMCFG ManageMobileOperatorConfiguration
TestCommand

AT+CMCFG=?

Response
TAreturnsthelistofsupportedmodes.
+CMCFG:( listofsupported <mode> s ),<length>
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CMCFG?

Response
+CMCFG:<mode>,<config_num>
[+CMCFG:<index>,<config_name>,<config_version>,<state>...]
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CMCFG=[,
<config_name>]

when< mode >= 0 , 1 , 2 or 3 andcommandsuccessful:
OK
when< mode >= 4 andcommandsuccessful:
+CMCFG: 4 , <flag> , <config_name>
OK
Iffailed:
+CMEERROR:<err>
Parameters
<mode> 0 Manuallyselectmobileoperatorconfiguration
1 Automaticallyselectmobileoperatorconfiguration
accordingtoICCIDinformationinSIMcard
2 Activate specifiedmobile operator configuration,
<config_name> mustbe provided.
3 Deactivationspecifiedmobileoperator configuration,
<config_name> mustbe provided.
Intergertype,themaximumlengthof <config_name>
<config_num> Integertype,thenumberofmobilenetworkconfiguration
Integertype,theindexofmobilenetworkconfiguration
<config_name> Stringtype,thenameofmobilenetworkconfiguration.
"Default" Defaultnetworkconfiguration
"ATT" ATTnetworkconfiguration,notsupport
VOLTE
"Verizon" Verizonnetworkconfiguration,notsupport
VOLTE
<config_version> Hextype,theversionofmobilenetworkconfiguration
Integertype,thestateofmobilenetworkconfiguration
0 Inactive
1 Active
Integertype,itindicateswhethermodulehasactivateda
networkconfiguration.Ifnetworkconfigurationhasbeen
activated,Thethirdparameter <config_name> isthe
nameofactivatingnetworkconfiguration.
0 Networkconfigurationhasbeenactivated
1 Notanynetworkconfigurationisactivated
ParameterSavingMode -
MaxResponseTime -

Reference

Note
 After setting AT+CMCFG= 1 ,module can select mobile operator
configuration according to ICCID information in SIM card
automatically,Ifnetworkconfigurationhaschanged,modulewillreboot
andmakeconfigurationeffective
 Ifmoduleneedstoselectmobileoperatorconfigurationmanually,you
shoulddoasthefollowingsteps.
1 ) Settingmanualmode
AT+CMCFG= 0
2 ) Activatespecifiedconfiguration
AT+CMCFG= 2 , <config_name>
3 ) Rebootthemodule
AT+CFUN= 1 , 1
5 2 41 AT+CSIMLOCK SIMLock......................................................................................................
AT+CSIMLOCK SIMLock
TestCommand
Response
TAreturnsthelistofsupportedmodes.

AT+CSIMLOCK=? +CSIMLOCK: (listofsupported s),(listofsupported s>,
,

OK
Parameters
SeeWriteCommand
ReadCommand

AT+CSIMLOCK?

Response
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CSIMLOCK=,[,[,<pers_code_list>]]

If< mode >≠ 2 andCommandissuccessful
OK
If< mode >= 2 andCommandissuccessful
+CSIMLOCK:<status>,<pers_code_list>
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR: Iffailed:
Parameters
Stringtype,Phonesecuritylockssetbyfactoryorcustomer.
whichcanbe:
"PN" NetworkPersonalisation
0 unlock
1 lock
2 querystatus
Integertype,maximumlengthof ,themaxinum
lengthis 16.
Integertype,maximumlengthof <pers_code_list> ,the
maxinumlengthis 160.
Stringtype,passwordisusedtolockorunlocka .
<pers_code_list> Stringtype,codelistfordevicepersonalization.The
contentsdependontheselected .
If is"PN":
<pers_code_list> isintheformat:
"MCC 1 - MNC 1 [;MCC 2 - MNC 2 [...]]"
ItcontainsalistofpairsofMCCandMNC.MCCandMNC
isseparatedbya‘-‘,everypairofMCCandMNCis
separatedbysemicolon.
Forexample:
" 460 - 00 ; 460 - 01 "
Integertype,thestatusoflock
0 lockisinactive
1 lockisactive
ParameterSavingMode -
MaxResponseTime -

Reference

Note
 Lockdevice
CustomercansendATcommandtolockthedeivcethatcanonlyuse
somespecificSIMcard.
AT+CSIMLOCK= " PN " , 1 , " 0123456789 ABCDEF " , " 460 - 00 ; 460 - 01 "
 Unlockdevice
Ifthedeviceislocking,CustomercansendATcommandtounlockthe
device.
AT+CSIMLOCK= " PN " , 0 , " ABCDEFGH 12345678 "
 Querydevicestatus
customer may sendAT command as follow to query status ofthe
device
AT+CSIMLOCK= " PN " , 2
5 2 42 AT+CRATSRCH ConfigureParameterforBetterRATSearch........................................
AT+CRATSRCH ConfigureParameterforBetterRATSearch
TestCommand
AT+CRATSRCH=?

Response
TAreturnsthelistofsupportedmodes.
+CRATSRCH: (list of supported <rat_timer> s),(list of supported
<srch_align >),
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CRATSRCH?

Response
+CRATSRCH:<rat_timer> , <srch_align >
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CRATSRCH=<rat_t
imer>,<srch_align>

OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err> Iffailed:
Parameters
<rat_timer> Integertype, <rat_timer> istimeoutforbetterRAT(radio
accesstechnology)search.Thedefaultvalueis 60 ,expressed
inminutes.ForSIM 7000 seriesmodules,thepriorityofRATis
asfollows:
CAT-M > NB-IOT > GSM
IfUEhasregisteredsuccessfullyGSMnetwork,itwilltryto
searchCAT-MandNB-IOTnetworkafterthetimerexpiring.
<srch_align> Integertype, <srch_align> specifiesanintervalbefore
eDRXpagewhenascanshouldbegin.Thedefaultvalueis
20 ,expressedinminutes.
ParameterSavingMode -

MaxResponseTime -

Reference
Note

5 2 43 AT+SPWM GeneratethePulse-Width-Modulation............................................................
AT+SPWM GeneratethePulse-Width-Modulation
TestCommand

AT+SPWM=?

Response
+SPWM:( listofsupported <div> s ),( listofsupported <level> s )
OK
Parameters
SeeWriteCommand
WriteCommand
AT+SPWM=

,
Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
<div> Therangeof<div>is 0 - 31 ,theoutputfrequencyequalsto
( 192 KHz)/(period+ 1 ).
<level> 0 - 100 :tonelevel,whichcanbeconvertedtodutyratio.
Reference

Note
 Theequationoffinalfrequencyand<period>isthis:
frequency= 192 KHz/(period+ 1 ),when div is 0 or 1 ,theperiodis 1.
When div is 2 ,theperiodis 1. 5 .When div is 3 ,theperiodis 2 .When
div is 4 ,theperiodis 2. 5 ........
 Theequationof<level>anddutyfactoris:dutyfactor=(level+ 1 ).
5 2 44 AT+CASRIP ShowRemoteIPaddressandPortWhenReceivedData........................
AT+CASRIP ShowRemoteIPAddressandPortWhenReceivedData
ReadCommand

AT+CASRIP?

Response
+CASRIP : <mode>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CASRIP=

Response
OK
or
ERROR
Parameters
AnumericparameterwhichshowsremoteIPaddressandport.
0 Donotshowtheprompt
1 Showtheprompt,theformatisasfollows:
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference

5 2 45 AT+CEDRX ConfigureEDRXparameters...........................................................................
AT+CEDRX ConfigureEDRXparameters
TestCommand

AT+CEDRX=?

Response
+CEDRX:( 0 - 3 ),( 0 - 1 ),( 0 - 15 ),( 0 - 15 )
OK
ReadCommand

AT+CEDRX?

Response
+CEDRX:<mode>,<enabled>,<ptw>,<cycle_length>
...
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CEDRX=,<
enabled>,,

Response
OK
Iffailed:
+CMEERROR:<err>
Parameters
<mode> 0 GSM
1 LTE
2 NB-IoT
3 CAT-M
<enabled> 0 Disable
1 Enable
<ptw> Pagetimewindow
0 - 15
<cycle_length> 0 - 15
Reference

Note
 Thevalue 0 - 15 ofptwseparatelymeans 1280 , 2560 , 3840 , 5120 , 6400 ,
7680 , 8960 , 10240 , 11520 , 12800 , 14080 , 15360 , 16640 , 17920 , 19200 ,
20480 .(ms)
 Thevalue 0 - 15 ofcycle_lengthseparatelymeans 5. 12 , 10. 24 , 20. 48 ,
40. 96 , 61. 44 , 81. 92 , 102. 40 , 122. 88 , 143. 36 , 163. 84 , 327. 68 , 655. 36 , 1310.
72 , 2621. 44 , 5242. 88 , 10485. 76 .(seconds)
 Therehasnoeffectif<mode>is 0 or 1.
 Theedrxparameterscantakeeffectaftermodulerestarting
5 2 46 AT+CPSMRDP ReadPSMDynamicParameters.............................................................
AT+CPSMRDP ReadPSMDynamicParameters
TestCommand

AT+CPSMRDP=?

Response
+CPSMRDP:( 0 , 1 )
OK
ExecutionCommand

AT+CPSMRDP

Response
+CPSMRDP:
<mode>,<Requested_active_Time>,<Requested_Periodic_TAU>,<Net
work_Active_Time>,<Network_T 3412 _EXT_value>,<Network_T 3412 _v
alue>
OK
Parameters
< mode > Integertype.DisableorenabletheuseofPSMintheUE.
0 DisabletheuseofPSM
1 EnabletheuseofPSM
< Requested_active_Time > Integer type.Requested active time
value(T 3324 ) to beconfiged by UE in E-UTRAN network.Unit:
second.
< Requested_Periodic_TAU > Integertype.Requestedextendedperiodic
TAU value (T 3412 _EXT) to be configed by UE in E-UTRAN
network.Unit:second.
< Network_Active_Time > Integer type.Network assign active timer
value(T 3324 ) in E-UTRANnetwork.If<network_Active_Time>is
0 ,it show s that network does not support PSM
feature.Unit:second.
< Network_T 3412 _EXT_value > Integertype.Network assignextended
periodic TAU value(T 3412 _EXT) in E-UTRAN
network.Unit:second.
< Network_T 3412 _value > Integer type.Network assign periodic TAU
value(T 3412 )in E-UTRANnetwork.Unit:second.
ParameterSavingMode NO_SAVE

MaxResponseTime -

Reference

Note
 If <Network_T 3412 _EXT_value> isgreaterthan 0 ,UEwillstartTAU
procedureaccordingto <Network_T 3412 _EXT_value>.
5 2 47 AT+CPSMCFG ConfigurePSMversionandMinimumThresholdValue.......................
AT+CPSMCFG ConfigurePSMversionandMinimumThresholdValue
TestCommand

AT+CPSMCFG=?

Response
TAreturnsthelistofsupportedmodes.
+CPSMCFG: (list of supported <threshold> s),(list of supported
<psm_version >s)
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CPSMCFG?

Response
+CPSMCFG:<threshold> , <psm_version >
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CPSMCFG=[,<psm_version>
]

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
Integertype.Minimumthresholdvalue(insecond)toenter
PSM.Therangefrom 60 to 86400 .Thedefaultvalueis 60 seconds.
<psm_version> Integertype.BitmasktoindicatePSMmodes( 1 - Enable/ 0 -
Disable).Eachbitisconfiguredindependentyly.Therangefrom 0 to
15 .Thedefaultvalueis 15.
BIT 0 PSMwithoutnetworkcoordination
BIT 1 Rel 12 PSMwithoutcontextretention
BIT 2 Rel 12 PSMwithcontextretention
BIT 3 PSMinbetweeneDRXcycles
ParameterSavingMode -
MaxResponseTime -

Reference Note

5 2 48 AT+CPSMCFGEXT ConfigureModemOptimizationofPSM..........................................
AT+CPSMCFGEXTConfigureModemOptimizationofPSM
TestCommand

AT+CPSMCFGEXT=?

Response
TAreturnsthelistofsupportedmodes.
+CPSMCFGEXT: (listofsupported <psm_opt_mask> s),(listofsupported
<max_oos_full_scans >s),(list of supported
<psm_duration_due_to_oos> s),(list of supported
<psm_randomization_window> s),(listofsupported <max_oos_time> s),
(listofsupported <early_wake_up_time> s)
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CPSMCFGEXT?

Response
+CPSMCFGEXT:
<psm_opt_mask> , <max_oos_full_scans >, <psm_duration_due_to_oos
> , <psm_randomization_window> , <max_oos_time> , <early_wake_up_ti
me>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CPSMCFGEXT=

[,[,[,<psm_randomizat
ion_window>[,<max_o
os_time>[,<early_wake
_up_time>]]]]]

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
<psm_opt_mask> Integertype.Therangeisfrom 0 to 15 .Thedefault
value
is 10.
1 stbitof <psm_opt_mask> isusedtoenable/disablePSMENTER
requestwithoutsendingPSM_READY_REQtoNAS.ThisisaquickPSM
operation.
2 nd bit of <psm_opt_mask> is used to enable/disable Out of
Service(OoS)statusindicationfromModemtoAP.
3 rd bit of <psm_opt_mask> is used to enable/disable limited
servicestatusindicationfromModemtoAP.
4 thbitof <psm_opt_mask> isusedtoenable/disabledeep-sleep
mode.IfPSMdurationislessthanthethresholdvalue.Ifenabled,itputsthe
device in deep-sleep mode,if PSM is not entered due to not meeting
thresholdvalue.
<max_oos_full_scans> Integertype.Maximumnumberoffullscansto
waitbeforemodemdeclaresSYS_PSM_STATUS_OOSto
clients.Therangeisfrom 1 to 100 .Thedefaultvalueis 2.
<psm_duration_due_to_oos> Integertype.PSMdurationusedbyPSM
daemonuponOOS/LimitedServiceindication,duetoservice
outage.Therangeisfrom 120 to 4294967295 .Thedefaultvalueis
120 .Theunitissecond.
<psm_randomization_window> Integertype.PSMwakeuprandomization
windowtoavoidnetworkcongestionduetoallthePSMdevices
wakingupatthesametime.TheRangeisfrom 1 to 1000 .The
defaultvalueis 5 .Theunitis 5.
<max_oos_time> Integertype.Maximumtimeinsecondstowaitbefore
declaringSYS_PSM_STATUS_OOStoclients.Therangeisfrom 1
to 65535 .Theunitissecond.
< early_wakeup_time > Integertype.Devicewakesupearlytoaccount
forboot-upandacquisitiondelay.WhileprogrammingPMIC,PSM
daemonreducesPSMdurationbythisduration.Therangeisfrom
1 to 1000 .Thedefaultvalueis 3 .Theunitissecond.
ParameterSavingMode -

MaxResponseTime -

Reference
Note

5 2 49 AT+CPSMSTATUS EnableDeepSleepWakeupIndication............................................
AT+CPSMSTATUS EnableDeepSleepWakeupIndication
TestCommand

AT+CPSMSTATUS=?

Response
+CPSMSTATUS:( 0 - 1 )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CPSMSTATUS?

Response
+CPSMSTATUS:<enable>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CPSMSTATUS=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters

0 Disableindicationwhenmodemwakesupfromdeepsleep
1 Enableindicationwhenmodemwakesupfromdeepsleep
ParameterSavingMode -
MaxResponseTime -

Reference Note

5 2 50 AT+CEDRXRDP eDRXReadDynamicParameters.........................................................
AT+CEDRXRDP eDRXReadDynamicParameters
TestCommand

AT+CEDRXRDP=?

Response
OK
Parameters
SeeWriteCommand
ExecutionCommand

AT+CEDRXRDP

Response
+CEDRXRDP:
<AcT-type>[,<Requested_eDRX_value>[,<NW-provided_eDRX_value>[
,<Paging_time_window>]]]
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
<AcT-type> Integer type,indicates the typeof access technology.This
AT-commandisusedtospecifytherelationshipbetweenthetype
ofaccesstechnologyandtherequestedeDRXvalue
0 AccesstechnologyisnotusingEdrx
4 E-UTRAN(CAT-M 1 )
5 E-UTRAN(NB-S 1 mode)
<Requested_Edrx_value> Stringtype;halfabyteina 4 - bitformat.The
Edrxvaluerefers tobit 4 to 1 ofoctet 3 oftheExtendedDRX
parameters information element (see sub-clause 10. 5. 5. 32 of
3 GPP TS 24. 008 ).For the coding and the value range,see
Extended DRX parameters information element in 3 GPP TS
24. 008 Table 10. 5. 5. 32 / 3 GPPTS 24. 008.
<NW-provided_eDRX_value> Stringtype;halfabyteina 4 - bitformat.The
edrxvalueReferstobit 4 to 1 ofoctet 3 oftheExtendedDRX
parameters information element (see sub-clause 10. 5. 5. 32 of
3 GPP TS 24. 008 ).For the coding and thevalue range,seethe
Extended DRX parameters information element in 3 GPP TS
008 Table 10. 5. 5. 32 / 3 GPPTS 24. 008.
<Paging_time_window> Stringtype;halfabyteina 4 - bitformat.The
pagingtimewindowrefers tobit 8 to 5 octet 3 oftheExtended
DRX.Parametersinformationelement(seesub-clause 10. 5. 5. 32
of 3 GPPTS 24. 008 ).Forthecodingandthevaluerange,seethe
Extended DRX parameters information element in 3 GPP TS
008 Table 10. 5. 5. 32 / 3 GPPTS 24. 008.
ParameterSavingMode -
MaxResponseTime -
Reference
Note

5 2 51 AT+CRAI ConfigureReleaseAssistanceIndicationinNB-IOTnetwork........................
AT+CRAI ConfigureReleaseAssistanceIndicationinNB-IOTnetwork
TestCommand

AT+CRAI=?

Response
+CRAI:( listofsupported <rai> s),(listofsupported <valid >s),
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CRAI?

Response
+CRAI:<rai> , <valid_time >
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CRAI=[,]

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
<rai> Integer type. Indicates the value of the release assistance
indication,refer 3 GPPTS 24. 301 [ 83 ] subclause 9. 9. 4. 25 .V
0 Noinformationavailable
1 TheMTexpectsthatexchangeofdatawillbecompletedwiththe
transmissionoftheESMDATATRANSPORTmessage.
2 TheMTexpectsthatexchangeofdatawillbecompletedwiththe
receiptofanESMDATATRANSPORTmessage.
<valid_time> Integertype.<valid_time>isvalidtimeofreleaseassistance
indication.
0 Thevalidtimeis 1
1 unlimitedtime
ParameterSavingMode NO_SAVE

MaxResponseTime -

Reference

Note
 BeforeUEsendsthelastpacketofdata,AT+CRAIshouldbeexecuted
firstly.
6 ATCommandsforGPRSSupport........................................................................................
6 1 Overview..............................................................................................................................................
Command Description
AT+CGATT AttachordetachfromGPRSservice
AT+CGDCONT DefinePDPcontext
AT+CGACT PDPcontextactivateordeactivate
AT+CGPADDR ShowPDPaddress

AT+CGREG Networkregistrationstatus
AT+CGSMS SelectserviceforMOSMSmessages
AT+CEREG EPSNetworkRegistrationStatus

6 2 DetailedDescriptionsofATCommandsforGPRSSupport.......................................................
6 2 1 AT+CGATT AttachorDetachfromGPRSService............................................................
AT+CGATT AttachorDetachfromGPRSService
TestCommand

AT+CGATT=?

Response
+CGATT:( listofsupported <state> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CGATT?

Response
+CGATT:<state>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CGATT=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
IndicatesthestateofGPRSattachment
0 Detached
1 Attached
OthervaluesarereservedandwillresultinanERRORresponsetothe
WriteCommand.
ParameterSavingMode NO_SAVE

MaxResponseTime 75 seconds
Reference Note

6 2 2 AT+CGDCONT DefinePDPContext...................................................................................
AT+CGDCONT DefinePDPContext
TestCommand
AT+CGDCONT=?

Response
+CGDCONT: (range of supported <cid>s),<PDP_type>,,,(list of
supported <d_comp>s),(list of supported <h_comp>s)(list of
<ipv 4 _ctrl>s),(listof<emergency_flag>s)
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CGDCONT?

Response
+CGDCONT:
[<cid>,<PDP_type>,<APN>,<PDP_addr>,<d_comp>,<h_comp>,<ipv 4 _c
trl>,<emergency_flag>[<CR><LF>+CGDCONT:
<cid>,<PDP_type>,<APN>,<PDP_addr>,<d_comp>,<h_comp>,<ipv 4 _ct
rl>,<emergency_flag>[...]]]
OK
Parameters
SeeWriteCommand
WriteCommand

**AT+CGDCONT=[,
<PDP_type>[,[,<
PDP_addr>[,<d_comp

[,<h_comp>][,<ipv 4 _c
trl>[,<emergency_flag
]]]]]]**

Response
OK
or
ERROR
Parameters
<cid> (PDPContextIdentifier)anumericparameterwhich
specifiesaparticularPDPcontextdefinition.Theparameter
islocaltotheTE-MTinterfaceandisusedinotherPDP
context-relatedcommands.Therangeofpermittedvalues
(minimumvalue= 1 )isreturnedbythetestformofthe
command.
1 ... 24
<PDP_type> (PacketDataProtocoltype)Astringparameterwhich
specifiesthetypeofpacketdataprotocol.
IP InternetProtocol(IETFSTD 5 )
PPP PointtoPointProtocol
IPV 6 InternetProtocolVersion 6
IPV 4 V 6 DualPDNStack
(AccessPointName)Astringparameter(stringshouldbe
includedinquotationmarks)whichisalogicalnamethatis
usedtoselecttheGGSNortheexternalpacketdata
network.Ifthevalueisnulloromitted,thenthesubscription
valuewillberequested.ThedefaultvalueisNULL.
<PDP_addr> AstringparameterthatidentifiestheMTintheaddress
spaceapplicabletothePDP.
Format:" ... "where< n >= 0 .. 255
Ifthevalueisnullorequals 0. 0. 0. 0 adynamicaddresswill
berequested.Theallocatedaddressmaybereadusingthe
+CGPADDRcommand.
<d_comp> AnumericparameterthatcontrolsPDPdatacompression
0 Off(defaultifvalueisomitted)
1 On
2 V. 42 bis
<h_comp> AnumericparameterthatcontrolsPDPheadcompression
0 Off(defaultifvalueisomitted)
1 On
2 RFC 1144
3 RFC 2507
4 RFC 3095
<ipv 4 _ctrl> ParameterthatcontrolshowtheMT/TArequeststogetthe
IPv 4 addressinformation:
0 AddressAllocationthroughNASSignaling
1 on
<emergency_flag> Emergency_flag:
0 Off(defaultifvalueisomitted)
1 On
ParameterSavingMode AUTO_SAVE
MaxResponseTime -
Reference Note
values 17 to 24 aresupportedfromMPSSJO 1. 0 +onwards.

6 2 3 AT+CGACT PDPContextActivateorDeactivate..............................................................
AT+CGACT PDPContextActivateorDeactivate
TestCommand

AT+CGACT=?

Response
+CGACT:( listofsupported <state> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CGACT?

Response
+CGACT:<cid>,<state>[<CR><LF>+CGACT:<cid>,<state>...]
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CGACT=[,<
cid>[,[,...]]]

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
IndicatesthestateofPDPcontextactivation
0 Deactivated
1 Activated
OthervaluesarereservedandwillresultinanERRORresponse
totheWriteCommand.
AnumericparameterwhichspecifiesaparticularPDPcontext
definition(see+CGDCONTCommand).Iftheisomitted,it
onlyaffectsthefirstcid.
values 17 to 24 aresupportedfromMPSSJO 1. 0 +
onwards.
1 ... 24
ParameterSavingMode NO_SAVE
MaxResponseTime 150 seconds

Reference
Note
 This command is used to test PDPs with network simulators.
SuccessfulactivationofPDPonrealnetworkisnotguaranteed.

6 2 4 AT+CGPADDR ShowPDPAddress.....................................................................................
AT+CGPADDR ShowPDPAddress
TestCommand
Response
+CGPADDR:( listofdefined s )

AT+CGPADDR=?
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CGPADDR=[,
[,...]]

Response
+CGPADDR:<cid>,<PDP_addr>
[<CR><LF>+CGPADDR:<cid>,<PDP_addr>[...]]
OK
If SIMcard supports IPV 4 V 6 type and the PDP_type of the command
"AT+CGDCONT"definedisipv 4 v 6 :
[+CGPADDR:<cid>,<PDP_addr_IPV 4 >,<PDP_addr_IPV 6 >]
+CGPADDR:<cid>,<PDP_addr_IPV 4 >,<PDP_addr_IPV 6 >[...]]]
OK
or
ERROR
Parameters
<cid> AnumericparameterwhichspecifiesaparticularPDPcontext
definition(see +CGDCONT Command)
1 ... 24
<PDP_addr> Stringtype,IPaddress
Format: <n>.<n>.<n>.<n> where< n >= 0 .. 255
<PDP_addr_IPV 4 >
AstringparameterthatidentifiestheMTintheaddressspace
applicabletothePDP.
<PDP_addr_IPV 6 >
AstringparameterthatidentifiestheMTintheaddressspace
applicabletothePDPwhenthesim_cardsupportsipv 6.
Thepdptypemustbesetto"ipv 6 "or"ipv 4 v 6 "bythe
AT+CGDCONTcommand.
ExecutionCommand

AT+CGPADDR

Response
[+CGPADDR:<cid>,<PDP_addr>]
+CGPADDR:<cid>,<PDP_addr>[...]]]
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
If SIMcard supports IPV 4 V 6 type and the PDP_type of the command
"AT+CGDCONT"definedisipv 4 v 6 :
[+CGPADDR:<cid>,<PDP_addr_IPV 4 >,<PDP_addr_IPV 6 >]
+CGPADDR:<cid>,<PDP_addr_IPV 4 >,<PDP_addr_IPV 6 >[...]]]
OK
Parameters
SeeWriteCommand
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

Note
 <cid>values 17 to 24 aresupportedfromMPSSJO 1. 0 +onwards.
 Write command returns address provided by the network if a
connectionhasbeenestablished.
6 2 5 AT+CGREG NetworkRegistrationStatus...........................................................................
AT+CGREG NetworkRegistrationStatus
TestCommand

AT+CGREG=?

Response
+CGREG:( listofsupported <n> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CGREG?

Response
+CGREG:
<n>,<stat>[,<lac>,<ci>,<netact>[,[<Active-Time>],[<Periodic-RAU>],[<
GPRS-READY-timer>]]]
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
SeeWriteCommand
WriteCommand

AT+CGREG[=]

Response
OK
ERROR
Parameters
<n> 0 Disablenetworkregistrationunsolicitedresultcode
1 Enablenetworkregistrationunsolicitedresultcode +CGREG:
<stat>
2 Enablenetworkregistrationandlocationinformation
unsolicitedresultcode +CGREG:<stat>[,<lac>,<ci>,<netact>]
4 EnabledisplaygprstimeandperiodicRAU
<stat>
0 Not registered, MT is not currently searching an
operatortoregisterto.TheGPRSserviceisdisabled,theUEis
allowedtoattachforGPRSifrequestedbytheuser.
1 Registered,homenetwork.
2 Not registered, but MT is currently trying to attach or
searching an operator to register to. The GPRS service is
enabled,butanallowablePLMNiscurrentlynotavailable.The
UEwillstartaGPRSattachassoonasanallowablePLMNis
available.
3 Registrationdenied,TheGPRSserviceisdisabled,theUE
isnotallowedtoattachforGPRSifitisrequestedbytheuser.
4 Unknown
5 Registered,roaming
Stringtype(stringshouldbeincludedinquotationmarks);two
bytelocationareacodeinhexadecimalformat(e.g." 00 C 3 "
equals 195 indecimal)
Stringtype(stringshouldbeincludedinquotationmarks);two
bytescellIDinhexadecimalformat
0 User-specifiedGSMaccesstechnology
1 GSMcompact
3 GSMEGPRS
7 User-specifiedLTEM 1 AGBaccesstechnology
9 User-specifiedLTENBS 1 accesstechnology
< Active-Time >
Stringtype;onebyteinan 8 bitformat.RequestedActiveTime
value(T 3324 )tobeallocatedtotheUE.TherequestedActive
Timevalueiscodedasonebyte(octet 3 )oftheGPRSTimer 2
informationelementcodedasbitformat(e.g." 00100100 "equals
4 minutes).
< Periodic-RAU >
Stringtype;onebyteinan 8 bitformat.Requestedextended
periodicTAUvalue(T 3412 )tobeallocatedtotheUEin
E-UTRAN.TherequestedextendedperiodicTAUvalueiscoded
asonebyte(octet 3 )oftheGPRSTimer 3 informationelement
codedasbitformat(e.g." 01000111 "equals 70 hours).
< GPRS-READY-timer >
Stringtype;onebyteinan 8 bitformat.RequestedGPRSREADY
timervalue(T 3314 )tobeallocatedtotheUEinGERAN/UTRAN.
TherequestedGPRSREADYtimervalueiscodedasonebyte
(octet 2 )oftheGPRSTimerinformationelementcodedasbit
format(e.g." 01000011 "equals 3 decihoursor 18 minutes).
ParameterSavingMode -
MaxResponseTime -
Reference Note

6 2 6 AT+CGSMS SelectServiceforMOSMSMessages........................................................
AT+CGSMS SelectServiceforMOSMSMessages
TestCommand

AT+CGSMS=?

Response
+CGSMS:( listofcurrentlyavailable <service> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CGSMS?

Response
+CGSMS:<service>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CGSMS=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
Anumericparameterwhichindicatestheserviceorservice
preferencetobeused
0 PacketDomain(valueisnotreallysupportedandis
internallymappedto 2 )
1 Circuitswitched(valueisnotreallysupportedandis
internallymappedto 3 )
2 PacketDomainpreferred(usecircuitswitchedif
GPRSnotavailable)
3 Circuitswitchedpreferred(usePacketDomainifcircuit
switchednotavailable)
ParameterSavingMode AUTO_SAVE
MaxResponseTime -
Reference
Note

6 2 7 AT+CEREG EPSNetworkRegistrationStatus..................................................................
AT+CEREG EPSNetworkRegistrationStatus
TestCommand

AT+CEREG=?

Response
+CEREG:( listofsupported <n> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CEREG?

Response
when< n >= 0 , 1 , 2 andcommandsuccessful:
+CEREG:<n>,<stat>[,[<tac>],[<rac>],[<ci>],[<AcT>]]
OK
when< n >= 4 andcommandsuccessful:
+CEREG: <n>,<stat>[,[<tac>],[<rac>],[<ci>],[<AcT>][,,[,[<Active-Time>]
,[<Periodic-TAU>]]]]
OK
IferrorisrelatedtowrongATsyntaxoroperationnotallowed:
+CMEERROR:<err>
Parameters
SeeWriteCommand
WriteCommand

AT+CEREG[=]

Response
OK
or
ERROR
Parameters
<n> 0 Disablenetworkregistrationunsolicitedresultcode
1 Enablenetworkregistrationunsolicitedresultcode +CEREG:
<stat>
2 Enablenetworkregistrationandlocationinformation
unsolicitedresultcode
+CEREG:<stat>[,[<tac>],[<rac>],[<ci>],[<AcT>]]
4 ForaUEthatwantstoapplyPSM,enablenetwork
registrationandlocation informationunsolicitedresultcode
+CEREG:<stat>[ ,[ <tac> ], [<rac>] , [<ci>] , [<AcT>][,,[,[<Active-
Time>] ,[ <Periodic-RAU>]]]]
<stat>
0 Notregistered,MTisnotcurrentlysearchinganoperatorto
registerto.TheGPRSserviceisdisabled,theUEisallowedto
attachforGPRSifrequestedbytheuser.
1 Registered,homenetwork.
2 Not registered, but MT is currently trying to attach or
searching an operator to register to. The GPRS service is
enabled,butanallowablePLMNiscurrentlynotavailable.The
UEwillstartaGPRSattachassoonasanallowablePLMNis
available.
3 Registrationdenied,TheGPRSserviceisdisabled,theUE
isnotallowedtoattachforGPRSifitisrequestedbytheuser.
4 Unknown
5 Registered,roaming
Stringtype(stringshouldbeincludedinquotationmarks);two
bytelocationareacodeinhexadecimalformat(e.g." 00 C 3 "
equals 195 indecimal)
Stringtype(stringshouldbeincludedinquotationmarks);two
bytescellIDinhexadecimalformat
0 User-specifiedGSMaccesstechnology
7 User-specifiedLTEM 1 AGBaccesstechnology
9 User-specifiedLTENBS 1 accesstechnology
< Active-Time >
Stringtype;onebyteinan 8 bitformat.RequestedActiveTime
value(T 3324 )tobeallocatedtotheUE.TherequestedActive
Timevalueiscodedasonebyte(octet 3 )oftheGPRSTimer 2
informationelementcodedasbitformat(e.g." 00100100 "equals
4 minutes).
< Periodic-RAU >
Stringtype;onebyteinan 8 bitformat.Requestedextended
periodicTAUvalue(T 3412 )tobeallocatedtotheUEin
E-UTRAN.TherequestedextendedperiodicTAUvalueiscoded
asonebyte(octet 3 )oftheGPRSTimer 3 informationelement
codedasbitformat(e.g." 01000111 "equals 70 hours).
ParameterSavingMode -
MaxResponseTime -
Reference Note

7 ATCommandsforIPApplication.........................................................................................
7 1 Overview..............................................................................................................................................
Command Description
AT+SAPBR BearersettingsforapplicationsbasedonIP

7 2 DetailedDescriptionsofCommands...............................................................................................
7 2 1 AT+SAPBR BearerSettingsforApplicationsBasedonIP...............................................
AT+SAPBR BearerSettingsforApplicationsBasedonIP
TestCommand

AT+SAPBR=?

Response
+SAPBR:( 0 - 4 ),( 1 - 3 ),"ConParamTag","ConParamValue"
OK
Parameters
SeeWriteCommand
WriteCommand

AT+SAPBR=<cmd_typ
e>,[,,
]

Response
OK
If <cmd_type>= 2
+SAPBR:<cid>,<Status>,<IP_Addr>
OK
If <cmd_type>= 4
+SAPBR:
<ConParamTag>,<ConParamValue>
OK
UnsolicitedResultCode
+SAPBR<cid>:DEACT
Parameters
<cmd_type>
0 Closebearer
1 Openbearer
2 Querybearer
3 Setbearerparameters
4 Getbearerparameters
Bearerprofileidentifier

0 Bearerisconnecting
1 Bearerisconnected
2 Bearerisclosing
3 Bearerisclosed
Bearerparameter
"APN" Access point name string: maximum 64
characters
"USER" Usernamestring:maximum 32 characters
"PWD" Passwordstring:maximum 32 characters
Bearerparamervalue
<IP_Addr> TheIPaddressofbearer
ParameterSavingMode NO_SAVE

MaxResponseTime
When <cmd_type> is 1 , 85 seconds
When <cmd_type> is 0 , 65 seconds
Reference Note
ThiscommandisappliedtoactivatesomeapplicationssuchasHTTP,FTP.

8 ATCommandsforTCPIPApplicationToolkit...................................................................
8 1 Overview..............................................................................................................................................
Command Description
AT+CIPMUX Startupmulti-IPconnection

AT+CIPSTART StartupTCPorUDPconnection
AT+CIPSEND SenddatathroughTCPorUDPconnection

AT+CIPQSEND Selectdatatransmittingmode
AT+CIPACK Querypreviousconnectiondatatransmittingstate

AT+CIPCLOSE CloseTCPorUDPconnection
AT+CIPSHUT DeactivateGPRSPDPcontext

AT+CLPORT Setlocalport

AT+CSTT StarttaskandsetAPN,username,password
AT+CIICR BringupwirelessconnectionwithGPRS

AT+CIFSR GetlocalIPaddress
AT+CIFSREX GetLocalIPAddressextend

AT+CIPSTATUS Querycurrentconnectionstatus
AT+CDNSCFG Configuredomainnameserver

AT+CDNSGIP QuerytheIPaddressofgivendomainname
AT+CIPHEAD AddanIPheadatthebeginningofapackagereceived

AT+CIPATS Setautosendingtimer

AT+CIPSPRT Setpromptof‘>’whenmodulesendsdata
AT+CIPSERVER Configuremoduleasserver

AT+CIPCSGP SetGPRSforconnectionmode
AT+CIPSRIP ShowremoteIPaddressandportwhenreceiveddata

AT+CIPDPDP SetwhethertocheckstateofGPRSnetworktiming
AT+CIPMODE SelectTCPIPapplicationmode

AT+CIPCCFG Configuretransparenttransfermode
AT+CIPSHOWTP DisplaytransferprotocolinIPheadwhenreceiveddata

AT+CIPUDPMODE UDPextendedmode
AT+CIPRXGET Getdatafromnetworkmanually

AT+CIPRDTIMER Setremotedelaytimer

AT+CIPSGTXT SelectGPRSPDPcontext

AT+CIPSENDHEX SetCIPSENDDataFormattoHEX

AT+CIPHEXS SetOutput-dataFormatwithsuffix
AT+CIPTKA SetTCPkeepaliveparameters

AT+CIPOPTION EnableorDisableTCPnaglealgorithm

8 2 DetailedDescriptionsofCommands...............................................................................................
8 2 1 AT+CIPMUX StartUpMulti-IPConnection.........................................................................
AT+CIPMUX StartUpMulti-IPConnection
TestCommand

AT+CIPMUX=?

Response
+CIPMUX:( 0 , 1 )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CIPMUX?

Response
+CIPMUX:<n>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CIPMUX=

Response
OK
Parameters
0 SingleIPconnection
1 MultiIPconnection
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

Note
 OnlyinIPinitialstate, AT+CIPMUX= 1 iseffective;
 OnlywhenmultiIPconnectionandGPRSapplicationarebothshut
down, AT+CIPMUX= 0 iseffective.
8 2 2 AT+CIPSTART StartUpTCPorUDPConnection.............................................................
AT+CIPSTART StartUpTCPorUDPConnection
TestCommand

AT+CIPSTART=?

Response
1 )IfAT+CIPMUX= 0
+CIPSTART:( listofsupported <mode>),(<IPaddress>),(<port>)
+CIPSTART:( listofsupported <mode>),(<domainname>),(<port>)
OK
2 )IfAT+CIPMUX= 1
+CIPSTART: ( list of supported <n>),( list of supported <mode>),(<IP
address>),(<port>)
+CIPSTART:( listofsupported <n>),( listofsupported <mode>),(<domain
name>),(<port>)
OK
Parameters
SeeWriteCommand
WriteCommand
1 )IfsingleIPconnection
(+CIPMUX= 0 )

**AT+CIPSTART=<mode

,,**

or
**AT+CIPSTART=<mode

,,**

2 )Ifmulti-IPconnection
(+CIPMUX= 1 )

AT+CIPSTART=,<
mode>,

,
or
AT+CIPSTART=,<
mode>,,

Response
1 )IfsingleIPconnection( +CIPMUX= 0 )
Ifformatisrightresponse
OK
otherwiseresponse
IferrorisrelatedtoMEfunctionality:
+CMEERROR<err>
Responsewhenconnectionexists
ALREADYCONNECT
Responsewhenconnectionissuccessful
CONNECTOK
Otherwise
STATE:<state>
CONNECTFAIL
2 )Ifmulti-IPconnection
(+CIPMUX= 1 )
Ifformatisright
OK ,
otherwiseresponse
IferrorisrelatedtoMEfunctionality:
+CMEERROR<err>
Responsewhenconnectionexists
<n>,ALREADYCONNECT
Ifconnectionissuccessful
<n>,CONNECTOK
Otherwise
<n>,CONNECTFAIL
Parameters
0 .. 7 Anumericparameterwhichindicatestheconnection
number
Astringparameterwhichindicatestheconnectiontype
"TCP" EstablishaTCPconnection
"UDP" EstablishaUDPconnection
AstringparameterwhichindicatesremoteserverIPaddress
Remoteserverport
Astringparameterwhichindicatesremoteserverdomain
name
Astringparameterwhichindicatestheprogressofconnecting
0 IPINITIAL
1 IPSTART
2 IPCONFIG
3 IPGPRSACT
4 IPSTATUS
5 TCPCONNECTING/UDPCONNECTING/
SERVERLISTENING
6 CONNECTOK
7 TCPCLOSING/UDPCLOSING
8 TCPCLOSED/UDPCLOSED
9 PDPDEACT
InMulti-IPstate:
0 IPINITIAL
1 IPSTART
2 IPCONFIG
3 IPGPRSACT
4 IPSTATUS
5 IPPROCESSING
9 PDPDEACT
ParameterSavingMode NO_SAVE

MaxResponseTime

Whenmodeismulti-IPstate,themaxresponsetime 75 seconds.
Whenmodeissinglestate,andthestateisIPINITIAL,themaxresponse
timeis 160 seconds.
Reference

Note
 ThiscommandallowsestablishmentofaTCP/UDPconnectiononly
whenthestateisIPINITIALorIPSTATUSwhenitisinsinglestate. In
multi-IPstate,thestateisinIPSTATUSonly. Soitisnecessaryto
process " AT+CIPSHUT " before user establishes a TCP/UDP
connectionwiththiscommandwhenthestateisnotIPINITIALorIP
STATUS.
 Whenmoduleisinmulti-IPstate,beforethiscommandisexecuted,itis
necessarytoprocess" AT+CSTT , AT+CIICR , AT+CIFSR ".
8 2 3 AT+CIPSEND SendDataThroughTCPorUDPConnection..........................................
AT+CIPSEND SendDataThroughTCPorUDPConnection
TestCommand

AT+CIPSEND=?

Response
1 )ForsingleIPconnection(+CIPMUX= 0 )
+CIPSEND:<length>
OK
2 )FormultiIPconnection(+CIPMUX= 1 )
+CIPSEND:( 0 - 7 ),<length>
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CIPSEND?

Response
1 )ForsingleIPconnection(+CIPMUX= 0 )
+CIPSEND:<size>
OK
2 )FormultiIPconnection(+CIPMUX= 1 )
+CIPSEND:<n>,<size>
OK
Parameters
<n> Anumericparameterwhichindicatestheconnectionnumber
<size> Anumericparameterwhichindicatesthedatalengthsentatatime
WriteCommand
1 )IfsingleIPconnection
(+CIPMUX= 0 )

**AT+CIPSEND=<length

**

2 )IfmultiIPconnection
(+CIPMUX= 1 )

AT+CIPSEND=[,]

Response
ThisCommandisusedtosendchangeablelengthdata
IfsingleIPisconnected(+CIPMUX= 0 )
Ifconnectionisnotestablishedormoduleisdisconnected:
IferrorisrelatedtoMEfunctionality:
+CMEERROR<err>
Ifsendingissuccessful:
When+CIPQSEND= 0
SENDOK
When+CIPQSEND= 1
DATAACCEPT:<length>
Ifsendingfails:
SENDFAIL
IfmultiIPconnectionisestablished(+CIPMUX= 1 )
Ifconnectionisnotestablishedormoduleisdisconnected:
IferrorisrelatedtoMEfunctionality:
+CMEERROR<err>
Ifsendingissuccessful:
When+CIPQSEND= 0
<n>,SENDOK
When+CIPQSEND= 1
DATAACCEPT:<n>,<length>
Ifsendingfails:
<n>,SENDFAIL
Parameters
<n> Anumericparameterwhichindicatestheconnectionnumber
<length> Anumericparameterwhichindicatesthelengthofsending
data,itmustbelessthan<size>
ExecutionCommand

AT+CIPSEND
Response">",thentype
dataforsend,tap
CTRL+Ztosend,tap
ESCtocancelthe
operation

Response
ThisCommandisusedtosendchangeablelengthdata.
IfsingleIPconnectionisestablished(+CIPMUX= 0 )
Ifconnectionisnotestablishedormoduleisdisconnected:
IferrorisrelatedtoMEfunctionality:
+CMEERROR<err>
Ifsendingissuccessful:
When+CIPQSEND= 0
SENDOK
When+CIPQSEND= 1
DATAACCEPT:<length>
Ifsendingfails:
SENDFAIL
Note
ThisCommandcanonlybeusedinsingleIPconnectionmode
(+CIPMUX= 0 )andtosenddataontheTCPorUDPconnectionthathas
beenestablishedalready.Ctrl-Zisusedasaterminationsymbol.ESCis
usedtocancelsendingdata.Thereareatmost byteswhichcanbe
sentatatime.
ParameterSavingMode NO_SAVE

MaxResponseTime
When+CIPQSEND= 0 andtheremoteservernoresponse,after 645
seconds," CLOSE "willbereported.

Reference

Note
 Thedatalengthwhichcanbesentdependsonnetworkstatus.
 SetthetimethatsenddataautomaticallywiththeCommandof
AT+CIPATS.
 Onlysenddataatthestatusofestablishedconnection.
8 2 4 AT+CIPQSEND SelectDataTransmittingMode................................................................
AT+CIPQSEND SelectDataTransmittingMode
TestCommand
AT+CIPQSEND=?

Response
+CIPQSEND:( 0 , 1 )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CIPQSEND?

Response
+CIPQSEND:<n>
OK
Parameter
SeeWriteCommand
WriteCommand

AT+CIPQSEND=

Response
OK
Parameters

0 Normalmode–whentheserverreceivesTCPdata,itwillresponse
SENDOK.
1 Quicksendmode–whenthedataissenttomodule,itwillresponse
DATAACCEPT: (ForsingleIPconnection(+CIPMUX= 0 ))or
DATAACCEPT:, (FormultiIPconnection(+CIPMUX= 1 ))
whilenotresponding SENDOK.
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

8 2 5 AT+CIPACK QueryPreviousConnectionDataTransmittingState................................
AT+CIPACK QueryPreviousConnectionDataTransmittingState
TestCommand
AT+CIPACK=?

Response
OK
WriteCommand
If multi IP connection
(+CIPMUX= 1 )
AT+CIPACK=

Response
+CIPACK:<txlen>,<acklen>,<nacklen>
OK
Parameters
Anumericparameterwhichindicatestheconnectionnumber
Thedataamountwhichhasbeensent
Thedataamountconfirmedsuccessfullybytheserver
Thedataamountwithoutconfirmationbytheserver
ExecutionCommand Response

If single IP connection
(+CIPMUX= 0 )

AT+CIPACK

+CIPACK:<txlen>,<acklen>,<nacklen>
OK
Parameters
SeeWriteCommand
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

8 2 6 AT+CIPCLOSE CloseTCPorUDPConnection................................................................
AT+CIPCLOSE CloseTCPorUDPConnection
TestCommand

AT+CIPCLOSE=?

Response
OK
WriteCommand
1 )IfsingleIPconnection
(+CIPMUX= 0 )
AT+CIPCLOSE=

2 )IfmultiIPconnection
(+CIPMUX= 1 )

AT+CIPCLOSE=,[<
n>]

Response:
1 )ForsingleIPconnection(+CIPMUX= 0 )
CLOSEOK
2 )FormultiIPconnection(+CIPMUX= 1 )
<id>,CLOSEOK
Parameters
<n> 0 Slowclose
1 Quickclose
<id> Anumericparameterwhichindicatestheconnectionnumber
ExecutionCommand

AT+CIPCLOSE

Response
Ifcloseissuccessfully:
CLOSEOK
Ifclosefails:
ERROR
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

Note
AT+CIPCLOSEonlyclosesconnectionatcorrespondingstatusofTCP/UDP
stack.ToseethestatususeAT+CIPSTATUScommand.Statusshouldbe:
TCPCONNECTING,UDPCONNECTING,SERVERLISTENINGor
CONNECTOKinsingle-connectionmode(see<state>parameter);
CONNECTINGorCONNECTEDinmulti-connectionmode(see<client
state>);
OPENINGorLISTENINGinmulti-connectionmode(see<serverstate>).
Otherwiseitwillreturn"ERROR".
8 2 7 AT+CIPSHUT DeactivateGPRSPDPContext..................................................................
AT+CIPSHUT DeactivateGPRSPDPContext
TestCommand

AT+CIPSHUT=?

Response
OK
ExecutionCommand

AT+CIPSHUT

Response
Ifcloseissuccessful:
SHUTOK
Ifclosefails:
ERROR
ParameterSavingMode NO_SAVE
MaxResponseTime 65 seconds

Reference

Note
 Ifthiscommandisexecutedinmulti-connectionmode,alloftheIP
connectionwillbeshut.
 UsercanclosegprspdpcontextbyAT+CIPSHUT.Afteritisclosed,the
statusisIPINITIAL.
 If"+PDP:DEACT"urcisreportedwhichmeansthegprsisreleasedby
thenetwork,thenuserstillneedstoexecute"AT+CIPSHUT"command
tomakePDPcontextcomebacktooriginalstate.
8 2 8 AT+CLPORT SetLocalPort..................................................................................................
AT+CLPORT SetLocalPort
TestCommand

AT+CLPORT=?

Response
1 )ForsingleIPconnection(+CIPMUX= 0 )
+CLPORT:("TCP","UDP"),( 0 - 65535 )
OK
2 )FormultiIPconnection(+CIPMUX= 1 )
+CLPORT:( 0 - 7 ),("TCP","UDP"),( 0 - 65535 )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CLPORT?

Response
1 )ForsingleIPconnection(+CIPMUX= 0 )
+CLPORT:<TCPport>,<UDPport>
OK
2 )FormultiIPconnection(+CIPMUX= 1 )
+CLPORT: 0 ,<TCPport>,<UDPport>
+CLPORT: 1 ,<TCPport>,<UDPport>
+CLPORT: 2 ,<TCPport>,<UDPport>
+CLPORT: 3 ,<TCPport>,<UDPport>
+CLPORT: 4 ,<TCPport>,<UDPport>
+CLPORT: 5 ,<TCPport>,<UDPport>
+CLPORT: 6 ,<TCPport>,<UDPport>
+CLPORT: 7 ,<TCPport>,<UDPport>
OK
Parameters
SeeWriteCommand
WriteCommand
1 )ForsingleIP
connection
(+CIPMUX= 0 )

AT+CLPORT=,

2 )FormultiIP
connection
(+CIPMUX= 1 )

AT+CLPORT=,,

Response
OK
or
ERROR
Parameters
0 .. 7 Anumericparameterwhichindicatestheconnection
number thisusedinmultiIPconnection
Astringparameterwhichindicatestheconnectiontype
"TCP" TCPlocalport
"UDP" UDPlocalport
0 - 65535 Anumericparameterwhichindicatesthelocalport.
Defaultvalueis 0 ,aportcanbedynamicallyallocatedaport.
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note
ThiscommandwillbeeffectivewhenmoduleissetasaClient.

8 2 9 AT+CSTT StartTaskandSetAPN,USERNAME,PASSWORD...................................
AT+CSTT StartTaskandSetAPN,USERNAME,PASSWORD
TestCommand

AT+CSTT=?

Response
+CSTT:"APN","USER","PWD"
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CSTT?

Response
+CSTT:<apn>,<username>,<password>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CSTT=,,

Response
OK
or
ERROR
Parameters
AstringparameterwhichindicatestheGPRSaccesspoint
name.Themaxlengthis 50 bytes.Defautlvalueis " CMNET ".
AstringparameterwhichindicatestheGPRSusername.
Themaxlengthis 50 bytes.
AstringparameterwhichindicatestheGPRSpassword.
Themaxlengthis 50 bytes.
ParameterSavingMode NO_SAVE
MaxResponseTime -

ExecutionCommand

AT+CSTT

Response
OK
or
ERROR
Reference

Note
Thewritecommandandexecutioncommandofthiscommandisvalidonly
atthestateofIPINITIAL.Afterthiscommandisexecuted,thestatewillbe
changedtoIPSTART.
8 2 10 AT+CIICR BringUpWirelessConnectionwithGPRS......................................................
AT+CIICR BringUpWirelessConnectionwithGPRS
TestCommand

AT+CIICR=?

Response
OK
ExecutionCommand
AT+CIICR

Response
OK
or
ERROR
ParameterSavingMode NO_SAVE
MaxResponseTime 85 seconds

Reference

Note
 AT+CIICRonlyactivatesmovingsceneatthestatusofIPSTART,after
operatingthisCommandisexecuted,thestatewillbechangedtoIP
CONFIG.
 Aftermoduleacceptstheactivatedoperation,ifitisactivated
successfully,modulestatewillbechangedtoIPGPRSACT,andit
respondsOK,otherwiseitwillrespondERROR.
8 2 11 AT+CIFSR GetLocalIPAddress..........................................................................................
AT+CIFSR GetLocalIPAddress
TestCommand

AT+CIFSR=?

Response
OK
ExecutionCommand
AT+CIFSR

Response

or
ERROR
Parameter
AstringparameterwhichindicatestheIPaddressassigned
fromGPRS
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

Note
OnlyafterPDPcontextisactivated,localIPaddresscanbeobtainedby
AT+CIFSR, otherwise it will respond ERROR. To see the status use
AT+CIPSTATUScommand.Statusshouldbe:
IP GPRSACT, TCP CONNECTING, UDP CONNECTING, SERVER
LISTENING,IPSTATUS,CONNECTOK,TCPCLOSING,UDPCLOSING,
TCP CLOSED, UDP CLOSED in single-connection mode (see <state>
parameter);
IPSTATUS,IPPROCESSINGinmulti-connectionmode(see<state>
parameter).
8 2 12 AT+CIFSREX GetLocalIPAddressextend.......................................................................
AT+CIFSREX GetLocalIPAddressextend
TestCommand
AT+CIFSREX=?

Response
OK
ExecutionCommand

AT+CIFSREX

Response
+CIFSREX:<IPaddress>
OK
Parameter
AstringparameterwhichindicatestheIPaddressassigned
fromGPRS
ParameterSavingMode NO_SAVE

MaxResponseTime -

Reference

Note
OnlyafterPDPcontextisactivated,localIPaddresscanbeobtainedby
AT+CIFSR, otherwise it will respond ERROR. To see the status use
AT+CIPSTATUScommand.Statusshouldbe:
IP GPRSACT, TCP CONNECTING, UDP CONNECTING, SERVER
LISTENING,IPSTATUS,CONNECTOK,TCPCLOSING,UDPCLOSING,
TCP CLOSED, UDP CLOSED in single-connection mode (see <state>
parameter);
IPSTATUS,IPPROCESSINGinmulti-connectionmode(see<state>
parameter).
8 2 13 AT+CIPSTATUS QueryCurrentConnectionStatus..........................................................
AT+CIPSTATUS QueryCurrentConnectionStatus
TestCommand

AT+CIPSTATUS=?

Response
OK
WriteCommand
IfmultiIPconnection
mode (+CIPMUX= 1 )

AT+CIPSTATUS=

Response
+CIPSTATUS:<n>,<bearer>,<TCP/UDP>,<IPaddress>,<port>,<client
state>
OK
Parameters
SeeExecutionCommand
ExecutionCommand
AT+CIPSTATUS

Response
1 )Ifinsingleconnectionmode(+CIPMUX= 0 )
OK
STATE:<state>
2 )Ifinmulti-connectionmode(+CIPMUX= 1 )
OK
STATE:<state>
Ifthemoduleissetasserver
S: 0 ,<bearer>,<port>,<serverstate>
C:<n>,<bearer>,<TCP/UDP>,<IPaddress>,<port>,<clientstate>
Parameters
<n> 0 - 7 Anumericparameterwhichindicatestheconnection
number
<bearer> 0 - 1 GPRSbearer,defaultis 0
<serverstate> OPENING
LISTENING
CLOSING
INITIAL
CONNECTING
CONNECTED
REMOTECLOSING
CLOSING
CLOSED
Astringparameterwhichindicatestheprogressof
connecting
0 IPINITIAL
1 IPSTART
2 IPCONFIG
3 IPGPRSACT
4 IPSTATUS
5 TCPCONNECTING/UDPCONNECTING
/SERVERLISTENING
6 CONNECTOK
7 TCPCLOSING/UDPCLOSING
8 TCPCLOSED/UDPCLOSED
9 PDPDEACT
InMulti-IPstate:
0 IPINITIAL
1 IPSTART
2 IPCONFIG
3 IPGPRSACT
4 IPSTATUS
5 IPPROCESSING
9 PDPDEACT
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference Note

8 2 14 AT+CDNSCFG ConfigureDomainNameServer..............................................................
AT+CDNSCFG ConfigureDomainNameServer
TestCommand

AT+CDNSCFG=?

Response
+CDNSCFG:("PrimaryDNS"),("SecondaryDNS")
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CDNSCFG?

Response
PrimaryDns:<pri_dns>
SecondaryDns:<sec_dns>
OK
Parameter
SeeWriteCommand
WriteCommand
AT+CDNSCFG=<pri_d
ns>[,<sec_dns>]

Response
OK
or
ERROR
Parameters
<pri_dns> AstringparameterwhichindicatestheIPaddressofthe
primarydomainnameserver.Defaultvalueis 0. 0. 0. 0.
<sec_dns> AstringparameterwhichindicatestheIPaddressofthe
secondarydomainnameserver.Defaultvalueis 0. 0. 0. 0.
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

8 2 15 AT+CDNSGIP QuerytheIPAddressofGivenDomainName........................................
AT+CDNSGIP QuerytheIPAddressofGivenDomainName
TestCommand

AT+CDNSGIP=?

Response
OK
WriteCommand
AT+CDNSGIP=

Response
OK
or
ERROR
Ifsuccessful,return:
+CDNSGIP: 1 ,<domainname>,<IP 1 >[,<IP 2 >]
Iffail,return:
+CDNSGIP: 0 ,<dnserrorcode>
Parameters
<domainname> Astringparameterwhichindicatesthedomainname
<IP 1 > AstringparameterwhichindicatesthefirstIPaddress
correspondingtothedomainname
<IP 2 > AstringparameterwhichindicatesthesecondIPaddress
correspondingtothedomainname
<dnserrorcode> Anumericparameterwhichindicatestheerrorcode
8 DNSCOMMONERROR
3 NETWORKERROR
Therearesomeothererrorcodesaswell.
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

8 2 16 AT+CIPHEAD AddanIPHeadattheBeginningofaPackageReceived.....................
AT+CIPHEAD AddanIPHeadattheBeginningofaPackageReceived
TestCommand

AT+CIPHEAD=?

Response
+CIPHEAD:( listofsupported <mode> s )
OK
Parameter
SeeWriteCommand
ReadCommand

AT+CIPHEAD?

Response
+CIPHEAD:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CIPHEAD=

Response
OK
or
ERROR
Parameters
AnumericparameterwhichindicateswhetheranIPheader
isaddedtothereceiveddataornot.
0 NotaddIPheader
1 AddIPheader,theformatis:
1 )ForsingleIPconnection(+CIPMUX= 0 )
+IPD,:
2 )FormultiIPconnection(+CIPMUX= 1 )
+RECEIVE,,:
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

8 2 17 AT+CIPATS SetAutoSendingTimer...................................................................................
AT+CIPATS SetAutoSendingTimer
TestCommand

AT+CIPATS=?

Response
+CIPATS:( listofsupported <mode> s ),( listofsupported <time >)
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CIPATS?

Response
+CIPATS:<mode>,<time>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CIPATS=[,
]

Response
OK
or
ERROR
Parameters
Anumericparameterwhichindicateswhethersettimerwhen
moduleissendingdata
0 Notsettimerwhenmoduleissendingdata
1 Settimerwhenmoduleissendingdata
1 .. 100 Anumericparameterwhichindicatestheseconds
afterwhichthedatawillbesent
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
Note

8 2 18 AT+CIPSPRT SetPromptof‘>’WhenModuleSendsData............................................
AT+CIPSPRT SetPromptof‘>’WhenModuleSendsData
TestCommand

AT+CIPSPRT=?

Response
+CIPSPRT:( listofsupported <sendprompt> s )
OK
Parameters
SeeWriteCommand
ReadCommand Response

AT+CIPSPRT? +CIPSPRT:

OK
Parameters
SeeWriteCommand
WriteCommand
AT+CIPSPRT=

Response
OK
or
ERROR
Parameters
Anumericparameterwhichindicateswhethertoecho
prompt‘>’aftermoduleissuesAT+CIPSENDcommand.
0 Itshows"sendok"butdoesnotpromptecho‘>’whensendingis
successful.
1 It prompts echo ‘>’ and shows "send ok"whensending is
successful.
2 Itneitherpromptsecho‘>’norshows"sendok"whensendingis
successful.
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

8 2 19 AT+CIPSERVER ConfigureModuleasServer..................................................................
AT+CIPSERVER ConfigureModuleasServer
TestCommand

AT+CIPSERVER=?

Response
+CIPSERVER:( 0 - CLOSESERVER, 1 - OPENSERVER),( 1 - 65535 )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CIPSERVER?

Response
+ CIPSERVER:<mode>[,<port>,<channelid>,<bearer>]
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CIPSERVER=[,]

Response
OK
or
ERROR
Parameters
0 Closeserver
1 Openserver
1 .. 65535 Listeningport
Channelid
GPRSbearer
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

Note
ThiscommandisallowedtoestablishaTCPserveronlywhenthestateis
IPINITIALorIPSTATUSwhenitisinsinglestate.Inmulti-IPstate,the
stateisinIPSTATUSonly.
8 2 20 AT+CIPCSGP SetGPRSforConnectionMode.................................................................
AT+CIPCSGP SetGPRSforConnectionMode
TestCommand

AT+CIPCSGP=?

Response
+CIPCSGP: 1 - GPRS,APN,USERNAME,PASSWORD
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CIPCSGP?

Response
+CIPCSGP:<mode>,<apn>,<username>,<password>[,<rate>]
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CIPCSGP=
[,(,,)]

Response
OK
or
ERROR
Parameters
Anumericparameterwhichindicatesthewirelessconnection
mode
1 setGPRSaswirelessconnectionmode
Astringparameterwhichindicatestheaccesspointname
Astringparameterwhichindicatestheusername
Astringparameterwhichindicatesthepassword
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

8 2 21 AT+CIPSRIP ShowRemoteIPAddressandPortWhenReceivedData......................
AT+CIPSRIP ShowRemoteIPAddressandPortWhenReceivedData
TestCommand

AT+CIPSRIP=?

Response
+CIPSRIP:( listofsupported <mode> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CIPSRIP?

Response
+CIPSRIP : <mode>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CIPSRIP=

Response
OK
or
ERROR
Parameters
AnumericparameterwhichshowsremoteIPaddressandport.
0 Donotshowtheprompt
1 Showtheprompt,theformatisasfollows:
1 )ForsingleIPconnection(+CIPMUX= 0 )
RECVFROM::
1 )FormultiIPconnection(+CIPMUX= 1 )
+RECEIVE,,,:
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference

8 2 22 AT+CIPDPDP SetWhethertoCheckStateofGPRSNetworkTiming..........................
AT+CIPDPDP SetWhethertoCheckStateofGPRSNetworkTiming
TestCommand

AT+CIPDPDP=?

Response
+CIPDPDP:( listofsupported <mode> s , listofsupported <interval>, listof
supported <timer>)
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CIPDPDP?

Response
+CIPDPDP:<mode>,<interval>,<timer>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CIPDPDP=
[,,]

Response
OK
or
ERROR
Parameters

0 NotsetdetectPDP
1 SetdetectPDP

1 <=interval<= 180 (s),defaultvalueis 10.

1 <=timer<= 10 ,defaultvalueis 3.
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

Note
If"+PDP:DEACT"urcisreportedbecauseofmodulenotattachingtogprs
foracertaintimeorotherreasons,userstillneedstoexecute
"AT+CIPSHUT"commandmakesPDPcontextcomebacktooriginalstate.
8 2 23 AT+CIPMODE SelectTCPIPApplicationMode.................................................................
AT+CIPMODE SelectTCPIPApplicationMode
TestCommand

AT+CIPMODE=?

Response
+CIPMODE:( 0 - NORMALMODE, 1 - TRANSPARENTMODE)
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CIPMODE?

Response
+CIPMODE:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand

**AT+CIPMODE=<mode

**

Response
OK
or
ERROR
Parameters
0 Normalmode
1 Transparentmode
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference Note

8 2 24 AT+CIPCCFG ConfigureTransparentTransferMode......................................................
AT+CIPCCFG ConfigureTransparentTransferMode
TestCommand
AT+CIPCCFG=?

Response
+CIPCCFG:
(NmRetry: 3 - 8 ),(WaitTm: 1 - 10 ),(SendSz: 1 - 1460 ),(esc: 0 , 1 ) ,(Rxmode: 0 , 1 ),(
RxSize: 50 - 1460 ),(Rxtimer: 20 - 1000 )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CIPCCFG?

Response
+CIPCCFG:
<NmRetry>,<WaitTm>,<SendSz>,<esc>,<Rxmode>,<RxSize>,<Rxtimer
>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CIPCCFG=,,,[,,<
RxSize>,]

Response
OK
or
ERROR
Parameters
<NmRetry> NumberofretriestobemadeforanIPpacket.Default
valueis 5.
<WaitTm> Numberof 100 msintervalstowaitforserialinputbefore
sendingthepacket.Defaultvalueis 2.
Sizeinbytesofdatablocktobereceivedfromserialport
beforesending.Defaultvalueis 1024.
Whetherturnontheescapesequence,defaultisTRUE.
0 Turnofftheescapesequence
1 Turnontheescapesequence
Whethertosettimeintervalduringoutputdatafromserial
port.
0 outputdatatoserialportwithoutinterval
1 outputdatatoserialportwithininterval.
Outputdatalengthforeachtime.Defaultvalueis 1460.
Timeinterval(ms)towaitforserialporttooutputdataagain.
Defaultvalue: 50 ms
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference
Note
Thiscommandwillbeeffectiveonlyinsingleconnectionmode
(+CIPMUX= 0 )

8 2 25 AT+CIPSHOWTP DisplayTransferProtocolinIPHeadWhenReceivedData...........
AT+CIPSHOWTP DisplayTransferProtocolinIPHeadWhenReceivedData
TestCommand

AT+CIPSHOWTP=?

Response
+CIPSHOWTP:( listofsupported <mode> s )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CIPSHOWTP?

Response
+CIPSHOWTP:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand

AT+CIPSHOWTP=

Response
OK
or
ERROR
Parameters
<mode> Anumericparameter whichindicates whether todisplay
transferprotocolinIPheadertoreceiveddataornot
0 Notdisplaytransferprotocol
1 Displaytransferprotocol,theformatis"+IPD,
<datasize>,<TCP/UDP>:<data>"
ParameterSavingMode NO_SAVE

MaxResponseTime -

Reference

Note
 Thiscommandwillbeeffectiveonlyinsingleconnectionmode
(+CIPMUX= 0 ).
 Onlywhen+CIPHEADissetto 1 ,thesettingofthiscommandwillwork.
8 2 26 AT+CIPUDPMODE UDPExtendedMode...........................................................................
AT+CIPUDPMODE UDPExtendedMode
TestCommand

AT+CIPUDPMODE=?

Response
1 )ForsingleIPconnection(+CIPMUX= 0 )
+CIPUDPMODE:( 0 - 2 ),("( 0 - 255 ).( 0 - 255 ).( 0 - 255 ).( 0 - 255 )"),( 1 - 65535 )
OK
2 )FormultiIPconnection(+CIPMUX= 1 )
+CIPUDPMODE:( 0 - 5 ),( 0 - 2 ),("( 0 - 255 ).( 0 - 255 ).( 0 - 255 ).( 0 - 255 )"),( 1 - 65535 )
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CIPUDPMODE?

Response
1 )ForsingleIPconnection(+CIPMUX= 0 )
+CIPUDPMODE:<mode>[,<IPaddress>,<Port>]
OK
2 )FormultiIPconnection(+CIPMUX= 1 )
+CIPUDPMODE: 0 ,<mode>[,<IPaddress>,<Port>]
+CIPUDPMODE: 1 ,<mode>[,<IPaddress>,<Port>]
+CIPUDPMODE: 2 ,<mode>[,<IPaddress>,<Port>]
+CIPUDPMODE: 3 ,<mode>[,<IPaddress>,<Port>]
+CIPUDPMODE: 4 ,<mode>[,<IPaddress>,<Port>]
+CIPUDPMODE: 5 ,<mode>[,<IPaddress>,<Port>]
+CIPUDPMODE: 6 ,<mode>[,<IPaddress>,<Port>]
+CIPUDPMODE: 7 ,<mode>[,<IPaddress>,<Port>]
OK
Parameter
SeeWriteCommand
WriteCommand
1 )ForsingleIP

Response
OK
connection
(+CIPMUX= 0 )

AT+CIPUDPMODE=[,,]

2 )FormultiIP
connection
(+CIPMUX= 1 )

**AT+CIPUDPMODE=<n

,[,,]**

or
ERROR
<n> 0 - 7 Anumericparameterwhichindicatestheconnection
number
<mode> 0 UDPNormalMode
1 UDPExtendedMode
2 SetUDPaddresstobesent
<IPaddress> Astringparameter whichindicatesremoteIPaddress
<port> Remoteport
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

8 2 27 AT+CIPRXGET GetDatafromNetworkManually.............................................................
AT+CIPRXGET GetDatafromNetworkManually
TestCommand

AT+CIPRXGET=?

Response
IfsingleIPconnection(+CIPMUX= 0 )
+CIPRXGET:( listofsupported <mode> s ),( listofsupported <reqlength>)
OK
IfmultiIPconnection(+CIPMUX= 1 )
+CIPRXGET:( listofsupported <mode> s ),( listofsupported <id> s ),( listof
supported <reqlength>)
OK
Parameters
SeeWriteCommand
ReadCommand

AT+CIPRXGET?

Response
+CIPRXGET:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand
1 )IfsingleIPconnection
(+CIPMUX= 0 )

**AT+CIPRXGET=<mode

[,]**

Response
OK
or
ERROR
1 )ForsingleIPconnection
If"AT+CIPSRIP= 1 "isset,IPaddressandportarecontained.
2 )IfmultiIPconnection
(+CIPMUX= 1 )

**AT+CIPRXGET=<mode

[,,]**

if<mode>= 1
+CIPRXGET: 1 [,<IPADDRESS>:<PORT>]
if<mode> = 2
+CIPRXGET: 2 ,<reqlength>,<cnflength>[,<IPADDRESS>:<PORT>]
1234567890 ...
OK
if<mode> = 3
+CIPRXGET: 3 ,<reqlength>,<cnflength>[,<IPADDRESS>:<PORT>]
5151 ...
OK
if<mode>= 4
+CIPRXGET: 4 ,<cnflength>
OK
2 )FormultiIPconnection
If"AT+CIPSRIP= 1 "isset,IPaddressandportiscontained.
if<mode>= 1
+CIPRXGET: 1 [,<id>,<IPADDRESS>:<PORT>]
if<mode> = 2
+CIPRXGET: 2 ,<id>,<reqlength>,<cnflength>[,<IP
ADDRESS>:<PORT>]
1234567890 ...
OK
if<mode> = 3
+CIPRXGET: 3 ,<id>,<reqlength>,<cnflength>[,<IP
ADDRESS>:<PORT>]
5151 ...
OK
if<mode>= 4
+CIPRXGET: 4 ,<id>,<cnflength>
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
<mode>
0 Disablegettingdatafromnetworkmanually,themoduleis
settonormalmode,datawillbepushedtoTEdirectly.
1 Enablegettingdatafromnetworkmanually.
2 Themodulecangetdata,butthelengthofoutputdatacan
notexceed 1460 bytesatatime.
3 Similar tomode 2 ,butin HEX mode,whichmeansthe
modulecanget 730 bytesmaximumatatime.
4 QueryhowmanydataarenotreadwithagivenID.
<id> Anumericparameterwhichindicatestheconnectionnumber
Requestednumberofdatabytes( 1 - 1460 bytes)toberead.
If= 4 ,therangeofis 0 - 2920 bytes.
Confirmednumberofdatabytestoberead,whichmaybeless
than. 0 indicatesthatnodatacanberead.
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference Note
Toenablethisfunction,parametermustbesetto 1 before
connection.

8 2 28 AT+CIPRDTIMER SetRemoteDelayTimer.......................................................................
AT+CIPRDTIMER SetRemoteDelayTimer
TestCommand
AT+CIPRDTIMER=?

Response
+CIPRDTIMER:( 100 - 4000 ),( 100 - 7000 )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CIPRDTIMER?

Response
+CIPRDTIMER:<rdsigtimer>,<rdmuxtimer>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CIPRDTIMER=,

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
Remotedelaytimerofsingleconnection.Defaultvalueis

Remotedelaytimerofmulti-connections.Defaultvalueis

ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

Note
Thiscommandisusedtoshortenthedisconnecttimelocallywhenthe
remoteserverhasbeendisconnected.
8 2 29 AT+CIPSGTXT SelectGPRSPDPcontext........................................................................
AT+CIPSGTXT SelectGPRSPDPcontext
TestCommand
AT+CIPSGTXT=?

Response
+CIPSGTXT:( 0 , 1 )
OK
Parameters
SeeWriteCommand
WriteCommand
**AT+CIPSGTXT=<mode

**

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
0 SelectfirstPDPcontext
1 SelectsecondPDPcontext
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

Note
Thiscommandisusedtoselectpdpcontext,onlyformultiIPconnection
(+CIPMUX= 1 ).
8 2 30 AT+CIPSENDHEX SetCIPSENDDataFormattoHex....................................................
AT+CIPSENDHEX SetCIPSENDDataFormattoHEX
TestCommand
AT+CIPSENDHEX=?

Response
+CIPSENDHEX:( 0 , 1 )
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CIPSENDHEX=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
0 ThedefaultformatofoutputdatainAT+CIPSEND.
1 SettheinputdatainHEXformatwhenusingCIPSEND
commandtosenddata.
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference
Note

8 2 31 AT+CIPHEXS SetOutput-dataFormatwithsuffix.............................................................
AT+CIPHEXS SetOutput-dataFormatwithsuffix
TestCommand
AT+CIPHEXS=?

Response
+CIPHEXS:(listofsupported<mode>s)
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CIPHEXS=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
0 Thedefaultformatofoutputdata
1 Settheoutputdatawithsuffix" 0 d 0 a"
2 SettheoutputdatainHEXformatwithsuffix" 0 d 0 a".
ParameterSavingMode NO_SAVE

MaxResponseTime -

Reference
Note:
Thiscommandisonlyavailablewhen"AT+CIPHEAD= 1 ".

8 2 32 AT+CIPTKA SetTCPKeepaliveParameters......................................................................
AT+CIPTKA SetTCPKeepaliveParameters
TestCommand
AT+CIPTKA=?

Response
+CIPTKA: (listofsupported <mode> s) , (listof supported
<keepIdle> s) , (listofsupported <keepInterval> ) , (listof
supported <keepCount> s)
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CIPTKA?

Response
+CIPTKA:<mode>,<keepIdle>,<keepInterval>,<keepCount>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CIPTKA=[,
[,[,]]]

Response
OK
IferrorisrelatedtoMEfunctionality:
ERROR
Parameters
SetTCPkeepaliveoption.
0 DisableTCPkeepalivemechanism
1 EnableTCPkeepalivemechanism
Integertype;Idletime(insecond)beforeTCPsendtheinitial
keepaliveprobe.
30 - 7200
Interval time (in second) between keepalive probes
retransmission.
30 - 75 - 600
Integer type;Maximumnumberofkeepaliveprobestobe
sent.
1 - 9
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

8 2 33 AT+CIPOPTION EnableorDisableTCPnaglealgorithm................................................
AT+CIPOPTION EnableorDisableTCPnaglealgorithm
TestCommand
AT+CIPOPTION=?

Response
+CIPOPTION: (list of supported <mode> s)
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CIPOPTION?

Response
+CIPOPTION:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CIPOPTION=<mod

Response
e> OK
IferrorisrelatedtoMEfunctionality:
ERROR
Parameters
ConfigtoenableordisableTCPnaglealgorithm
0 EnableTCPnagle algorithm
1 DisableTCPnaglealgorithm
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

9 ATCommandsforHTTP (S) Application.............................................................................
SIM 7000 serieshasanembeddedTCP/IPstackthatis drivenbyATcommandsandenablesthehost
applicationtoeasilyaccesstheInternetHTTP(S)service.ThischapterisareferenceguidetoalltheAT
commandsandresponsesdefinedtousewiththeTCP/IPstackinHTTP(S)Service.

9 1 Overview..............................................................................................................................................
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

9 2 DetailedDescriptionsofCommands...............................................................................................
9 2 1 AT+SHSSL SelectSSLConfigure........................................................................................
AT+SHSSL SelectSSLConfigure
Testcommand
AT+SHSSL=?

Response
+SHSSL:( 0 - 5 ),"calist","certname"
OK
Readcommand
AT+SHSSL?

Response
+SHSSL:<index>,<calist>,<certname>
OK
Writecommand
AT+SHSSL=,,

Response
OK
or
ERROR
Parameters
< index > CSSLCFGsetConfigureindex
< calist > CaCertificatename
< certname > CertCertificatename
ParameterSavingMode AUTO_SAVE
MaxResponseTime -

Reference -

9 2 2 AT+SHCONF SetHTTP(S)Parameter................................................................................
AT+SHCONF SetHTTP(S)Parameter
Testcommand
AT+SHCONF=?

Response
+SHCONF:"HTTPParamTag","HTTPParamValue"
OK
Readcommand
AT+SHCONF?

Response
+SHCONF:<HTTPParamTag>,<HTTPParamValue>
OK
Writecommand
AT+SHCONF=,

Response
OK
or
ERROR
Parameters
<HTTPParaTag> <HTTPParamValue>
"URL" ServerURLaddress(maxis 64 bytes)
"serverdomain[:tcpPort]"
"TIMEOUT" Holdoncerequesttime.
Unitissecond.Default 60 s.range: 30 - 1800
"BODYLEN" Setbodymaxlength(maxis 1024 bytes)
"HEADERLEN" Setheadmaxlength(maxis 350 bytes)
"IPVER" SetIPversion
0 IPv 4
1 IPv 6
ParameterSavingMode AUTO_SAVE

MaxResponseTime -

Reference

Note:
MustsetURL,BODYLEN,HEADERLENvalue,TIMEOUTdefaultis 60 s,
URLformatmust"http://xxx.xx.xx"or"https://xxx.xx.xx"
9 2 3 AT+SHCONN HTTP(S)Connection.....................................................................................
AT+SHCONN HTTP(S)Connection
Executioncommand
AT+SHCONN

Response
OK
or
ERROR
ParameterSavingMode -
MaxResponseTime -
Reference -

9 2 4 AT+SHBOD SetBody.............................................................................................................
AT+SHBOD SetBody
Testcommand
AT+SHBOD=?

Response
+SHBOD:"body",<bodylen>
OK
Readcommand
AT+SHBOD?

Response
+SHBOD:<body>,<bodylen>
OK
Writecommand
AT+SHBOD=,

Response
OK
or
ERROR
Parameters
< body > Setbodyvalue (maxlengthisSHCONFSetvalue)
< bodylen > Setbodylength (maxlengthisSHCONFSetvalue)
ParameterSavingMode AUTO_SAVE

MaxResponseTime -

Reference
Note:
Mustbeexecutedaftertheconnection

9 2 5 AT+SHBODEXT SetExtensionBody..................................................................................
AT+SHBODEXT SetExetensionBody
TestCommand
AT+SHBODEXT=?

Response
+SHBODEXT: (rangeofsupported <bodylen> s),(rangeofsupported
<timeout> s)
OK
ReadCommand
AT+SHBODEXT?

Response
+SHBODEXT:<body>,<len_body>
OK
WriteCommand
**AT+SHBODEXT=<len_body

,
text is entered
<ctrl-Z/ESC>
ESCquitswithoutsending**

Response
OK
or
ERROR
Parameters
Setbodyvalue (maxlengthisSHCONFSetvalue)
<len_body> Lengthof.Maxvalueis.
Max length set by
"AT+SHCONF="BODYLEN","
Timeout for automatically sending edited data
( 100 - 10000 ms)
ParameterSavingMode AUTO_SAVE

MaxResponseTime -

Reference
Note:
Mustbeexecutedaftertheconnection

9 2 6 AT+SHAHEAD AddHead.......................................................................................................
AT+SHAHEAD AddHead
Testcommand
AT+SHAHEAD=?

Response
+SHAHEAD:"type",”value”
OK
Readcommand
AT+SHAHEAD?

Response
+SHAHEAD:<type>,<value>
OK
Writecommand
AT+SHAHEAD=,<
value>

Response
OK
OR
ERROR
Parameters
< type > Headtype(maxlengthisSHCONFSetvalue)
< value > Headvalue(maxlengthisSHCONFSetvalue)
Note:Thesumoftypeandvaluemaxlengthis 350
ParameterSavingMode AUTO_SAVE
MaxResponseTime -

Reference
Note:
Mustbeexecutedaftertheconnection

9 2 7 AT+SHCHEAD ClearHead....................................................................................................
AT+SHCHEAD ClearHead
ExecutionCommand
AT+SHCHEAD

Response
OK
or
ERROR
ParameterSavingMode -
MaxResponseTime -

Reference
Note:
Mustbeexecutedaftertheconnection

9 2 8 AT+SHPARA SetHTTP(S)Para...........................................................................................
AT+SHPARA SetHTTP(S)Para
Testcommand
AT+SHPARA=?

Response
+SHPARA:"key",”value”
OK
Readcommand
AT+SHPARA?

Response
+SHPARA:<key>,<value>
OK
Writecommand
AT+SHPARA=,

Response
OK
or
ERROR
Parameters
< key > Setkey(maxis 64 bytes)
< value >Setvalue(maxis 64 bytes)
ParameterSavingMode AUTO_SAVE
MaxResponseTime -

Reference
Note:
Mustbeexecutedaftertheconnection.

9 2 9 AT+SHCPARA ClearHTTP(S)Para..................................................................................
AT+SHCPARA ClearHTTP(S)Para
TestCommand
AT+SHCPARA=?

Response
OK
ExecutionCommand
AT+SHCPARA

Response
OK
or
ERROR
ParameterSavingMode -

MaxResponseTime -

Reference
Note:
Mustbeexecutedaftertheconnection.

9 2 10 AT+SHSTATE QueryHTTP(S)ConnectionStatus............................................................
AT+SHSTATE QueryHTTP(S)ConnectionStatus
Readcommand
AT+SHSTATE?

Response
+SHSTATE:<status>
OK
Parameters
< status >
0 ExpressionHTTP(S)disconnectstate；
1 ExpressionHTTP(S)connectstate；
ParameterSavingMode -
MaxResponseTime -
Reference -

9 2 11 AT+SHREQ SetRequestType.............................................................................................
AT+SHREQ SetRequestType
Testcommand
AT+SHREQ=?

Response
+SHREQ:url,( 1 - 5 )
OK
Readcommand
AT+SHREQ?

Response
+SHREQ:<url>,<type>
OK
Writecommand
**AT+SHREQ=,<type

**

Response
OK
or
ERROR
UnsolicitedResultCode
+SHREQ:<typestring>,<StatusCode>,<DataLen>
Parameters
< url > Requestserverdomain(maxis 512 bytes)
<type>
1 GET
2 PUT
3 POST
4 PATCH
5 HEAD
<typestring> StringoftypeareGET,PUT,POST,PATCH,HEAD.
<timeout> WaitingforResponsetime(defaultis 60 sec)
<StatusCode> HTTP(S) Status Code responded by remote server, it
identifierrefertoHTTP 1. 1 (RFC 2616 )
100 Continue
101 SwitchingProtocols
200 OK
201 Created
202 Accepted
203 Non-AuthoritativeInformation
204 NoContent
205 ResetContent
206 PartialContent
300 MultipleChoices
301 MovedPermanently
302 Found
303 SeeOther
304 NotModified
305 UseProxy
307 TemporaryRedirect
400 BadRequest
401 Unauthorized
402 PaymentRequired
403 Forbidden
404 NotFound
405 MethodNotAllowed
406 NotAcceptable
407 ProxyAuthenticationRequired
408 RequestTime-out
409 Conflict
410 Gone
411 LengthRequired
412 PreconditionFailed
413 RequestEntityTooLarge
414 Request-URITooLarge
415 UnsupportedMediaType
416 Requestedrangenotsatisfiable
417 ExpectationFailed
500 InternalServerError
501 NotImplemented
502 BadGateway
503 ServiceUnavailable
504 GatewayTime-out
505 HTTP(S)Versionnotsupported
Thelengthofdatagot
ParameterSavingMode -
MaxResponseTime -

Reference Note:
Mustbeexecutedaftertheconnection

9 2 12 AT+SHREAD ReadResponseValue...................................................................................
AT+SHREAD ReadResponseValue
Testcommand
AT+SHREAD=?

Response
+SHREAD:( 0 - 306176 ),( 1 - 306176 )
OK
Writecommand
AT+SHREAD=,

Response
OK
+SHREAD:<data_len>
<data>
+SHREAD:<data_len>
<data>
or
ERROR
Ifisbiggerthanthedatasizereceived,it’serror
Ifisbiggerthan 2048 ,willgotmultiURC+SHREAD
Parameters
< startaddress >Startaddressofdata
< datalen > Setreadvalueslength
< data_len > Returndatalengthmaxis 2048 bytesonce,
ifmorethan 2048 bytes,willreturnmanytimeruntilalldataare
readout
< data > Responsedata
ParameterSavingMode -
MaxResponseTime -

Reference
Note:
Readdataafterrequest

9 2 13 AT+SHDISC DisconnectHTTP(S)........................................................................................
AT+SHDISC DisconnectHTTP(S)
ExecutionCommand
AT+SHDISC

Response
OK
or
ERROR
ParameterSavingMode -
MaxResponseTime -

Reference -

9 2 14 AT+HTTPTOFS DownloadFiletoAPFileSystem............................................................
AT+HTTPTOFS DownloadFiletoAPFileSystem
TestCommand
AT+HTTPTOFS=?

Response
+HTTPTOFS:( 1 - 255 ),( 1 - 127 )
OK
ReadCommand
AT+HTTPTOFS?

Response
+HTTPTOFS:<status>,<url>,<file_path>
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
SeeWriteCommand
WriteCommand
AT+HTTPTOFS=,
<file_path>[,
[,]]

Response
OK
+HTTPTOFS:<StatusCode>,<DataLen>
Parameters
<status>
0 Idle
1 Busy
<url> Theurl
<file_path>
FilepathandnameonAPside,
Forexample:"/customer/test.bin","/custapp/test.bin","/fota/test.bin"
< timeout> TimeoutofHTTPrequest.Unitissecond.
Rangeis 10 - 1000 ,defaultvalueis 50.
<retrycnt> RetrytimesofHTTPrequest.
Rangeis 5 - 100 ,defaultvalueis 5.
<StatusCode> HTTP Status Code responded by remote server, it
identifierrefertoHTTP 1. 1 (RFC 2616 )
100 Continue
200 OK
206 PartialContent
400 BadRequest
404 NotFound
408 RequestTime-out
500 InternalServerError
600 NotHTTPPDU
601 NetworkError
602 Nomemory
603 DNSError
604 StackBusy
620 SSLcontinue
65535 OtherErrors

Thelengthofdatadownload
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference Note

9 2 15 AT+HTTPTOFSRL StateofDownloadFiletoAPFileSystem........................................
AT+HTTPTOFSRL StateofDownloadFiletoAPFileSystem
TestCommand
AT+HTTPTOFSRL=?

Response
OK
ReadCommand
AT+HTTPTOFSRL?

Response
+HTTPTOFSRL:<status>,<curlen>,<totallen>
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
Downloadingstate
0 Idle
1 Duringdownloading
Thelengthofdatahavebeendownloadsuccessfully
Thelengthofdatadownload.Iftotallengthdoesnotbeengot,
willbe 0.
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference
Note

10 ATCommandsforFTPApplication..............................................................................
SIM 7000 serieshasanembeddedTCP/IPstackthatis drivenbyATcommandsandenablesthehost
applicationtoeasilyaccesstheInternetFTPservice.This chapter is areference guidetoall theAT
commandsandresponsesdefinedforusingwiththeTCP/IPstackinFTPService.

10 1 Overview..............................................................................................................................................
Command Description
AT+FTPPORT SetFTPcontrolport
AT+FTPMODE SetactiveorpassiveFTPmode
AT+FTPTYPE Setthetypeofdatatobetransferred

AT+FTPPUTOPT SetFTPputtype
AT+FTPCID SetFTPbearerprofileidentifier
AT+FTPREST Setresumebrokendownload
AT+FTPSERV SetFTPserveraddress

AT+FTPUN SetFTPusername
AT+FTPPW SetFTPpassword
AT+FTPGETNAME Setdownloadfilename
AT+FTPGETPATH Setdownloadfilepath

AT+FTPPUTNAME Setuploadfilename
AT+FTPPUTPATH Setuploadfilepath
AT+FTPGET Downloadfile
AT+FTPPUT Setuploadfile

AT+FTPDELE DeletespecifiedfileinFTPserver
AT+FTPSIZE GetthesizeofspecifiedfileinFTPserver
AT+FTPSTATE GettheFTPstate
AT+FTPEXTPUT Extenduploadfile

AT+FTPMKD Makedirectoryontheremotemachine
AT+FTPRMD Removedirectoryontheremotemachine
AT+FTPLIST Listcontentsofdirectoryontheremotemachine
AT+FTPEXTGET Extenddownloadfile

AT+FTPETPUT UploadFile
AT+FTPETGET DownloadFile
AT+FTPQUIT QuitcurrentFTPsession
AT+FTPRENAME RenametheSpecifiedFileontheRemoteMachine

AT+FTPMDTM GettheLastModificationTimestampofSpecifiedFileontheRemoteMachine

10 2 DetailedDescriptionsofCommands...............................................................................................
10 2 1 AT+FTPPORT SetFTPControlPort....................................................................................
AT+FTPPORT SetFTPControlPort
TestCommand
AT+FTPPORT=?

Response
OK
ReadCommand
AT+FTPPORT?

Response
+FTPPORT:<value>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+FTPPORT=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
ThevalueofFTPControlport,from 1 to 65535.
Defaultvalueis 21
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

Note
Numbersabove 65535 areillegalastheportidentificationfieldsare 16 bits
longintheTCPheader.
10 2 2 AT+FTPMODE SetActiveorPassiveFTPMode..............................................................
AT+FTPMODE SetActiveorPassiveFTPMode
TestCommand
AT+FTPMODE=?

Response
OK
ReadCommand
AT+FTPMODE?

Response
+FTPMODE:<value>
OK
Parameters
SeeWriteCommand
WriteCommand
**AT+FTPMODE=<value

**

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
0 ActiveFTPmode
1 PassiveFTPmode
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference Note

10 2 3 AT+FTPTYPE SettheTypeofDatatoBeTransferred.....................................................
AT+FTPTYPE SettheTypeofDatatoBeTransferred
TestCommand
AT+FTPTYPE=?

Response
OK
ReadCommand
AT+FTPTYPE?

Response
+FTPTYPE:<value>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+FTPTYPE=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
"A" ForFTPASCIIsessions
"I" ForFTPBinarysessions
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

Note
WhenthisvalueissettoA,allthedatasentbythestacktotheFTPserver
is made of 7 bits characters (NVT-ASCII: the MSB is set to 0 ). As a
consequence binary datacontaining 8 bits characters will be corrupted
duringthetransferiftheFTPTYPEissettoA.
10 2 4 AT+FTPPUTOPT SetFTPPutType....................................................................................
AT+FTPPUTOPT SetFTPPutType
TestCommand
AT+FTPPUTOPT=?

Response
OK
ReadCommand
AT+FTPPUTOPT?

Response
+FTPPUTOPT:<value>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+FTPPUTOPT=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
"APPE" Forappendingfile
"STOU" Forstoringuniquefile
"STOR" Forstoringfile
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

10 2 5 AT+FTPCID SetFTPBearerProfileIdentifier....................................................................
AT+FTPCID SetFTPBearerProfileIdentifier
TestCommand
AT+FTPCID=?

Response
OK
Parameters
SeeWriteCommand
ReadCommand
AT+FTPCID?

Response
+FTPCID:<value>
OK
Parameter
SeeWriteCommand
WriteCommand
AT+FTPCID=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
BearerprofileidentifierrefertoAT+SAPBR
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

10 2 6 AT+FTPREST SetResumeBrokenDownload..................................................................
AT+FTPREST SetResumeBrokenDownload
TestCommand
AT+FTPREST=?

Response
OK
ReadCommand
AT+FTPREST?

Response
+FTPREST:<value>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+FTPREST=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
Brokenpointtoberesumed
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
Note

10 2 7 AT+FTPSERV SetFTPServerAddress..............................................................................
AT+FTPSERV SetFTPServerAddress
TestCommand
AT+FTPSERV=?

Response
OK
ReadCommand
AT+FTPSERV?

Response
+FTPSERV:<value>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+FTPSERV=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
32 - bitnumberindotted-decimalnotation(i.e.xxx.xxx.xxx.xxx)
oralphanumericASCIItextstringupto 49 charactersifDNSisavailable
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

10 2 8 AT+FTPUN SetFTPUserName..........................................................................................
AT+FTPUN SetFTPUserName
TestCommand
AT+FTPUN=?

Response
OK
Parameters
SeeWriteCommand
ReadCommand
AT+FTPUN?

Response
+FTPUN:<value>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+FTPUN=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
AlphanumericASCIItextstringupto 49 characters.
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

10 2 9 AT+FTPPW SetFTPPassword............................................................................................
AT+FTPPW SetFTPPassword
TestCommand
AT+FTPPW=?

Response
OK
Parameters
SeeWriteCommand
ReadCommand
AT+FTPPW?

Response
+FTPPW:<value>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+FTPPW=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
AlphanumericASCIItextstringupto 49 characters.
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference Note

10 2 10 AT+FTPGETNAME SetDownloadFileName............................................................
AT+FTPGETNAME SetDownloadFileName
TestCommand
AT+FTPGETNAME=?

Response
OK
ReadCommand
AT+FTPGETNAME?

Response
+FTPGETNAME:<value>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+FTPGETNAME=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
AlphanumericASCIItextstringupto 99 characters
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference Note

10 2 11 AT+FTPGETPATH SetDownloadFilePath...............................................................
AT+FTPGETPATH SetDownloadFilePath
TestCommand
AT+FTPGETPATH=?

Response
OK
ReadCommand
AT+FTPGETPATH?

Response
+FTPGETPATH:<value>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+FTPGETPATH=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
AlphanumericASCIItextstringupto 255 characters
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

10 2 12 AT+FTPPUTNAME SetUploadFileName.................................................................
AT+FTPPUTNAME SetUploadFileName
TestCommand
AT+FTPPUTNAME=?

Response
OK
ReadCommand
AT+FTPPUTNAME?

Response
+FTPPUTNAME:<value>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+FTPPUTNAME=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameters
AlphanumericASCIItextstringupto 99 characters
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

10 2 13 AT+FTPPUTPATH SetUploadFilePath.....................................................................
AT+FTPPUTPATH SetUploadFilePath
TestCommand
AT+FTPPUTPATH=?

Response
OK
ReadCommand
AT+FTPPUTPATH?

Response
+FTPPUTPATH:<value>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+FTPPUTPATH=

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
AlphanumericASCIItextstringupto 255 characters
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

10 2 14 AT+FTPGET DownloadFile..........................................................................................
AT+FTPGET DownloadFile
TestCommand
AT+FTPGET=?

Response
OK
WriteCommand
AT+FTPGET=[,
]

Response
Ifmodeis 1 anditisasuccessfulFTPgetsession:
OK
+FTPGET: 1 , 1
Ifdatatransferfinished:
+FTPGET: 1 , 0
Ifmodeis 1 anditisafailedFTPgetsession:
OK
+FTPGET: 1 ,<error>
Ifmodeis 2 :
+FTPGET: 2 ,
012345678 ...
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
1 ForopeningFTPgetsession
2 ForreadingFTPdownloaddata.
Requestednumberofdatabytes( 1 - 1460 )toberead
Confirmednumberofdatabytestoberead,whichmaybeless
than< length >. 0 indicatesthatnodatacanberead.
61 Neterror
62 DNSerror
63 Connecterror
64 Timeout
65 Servererror
66 Operationnotallow
70 Replayerror
71 Usererror
72 Passworderror
73 Typeerror
74 Resterror
75 Passiveerror
76 Activeerror
77 Operateerror
78 Uploaderror
79 Downloaderror
80 Manualquit
ParameterSavingMode NO_SAVE

MaxResponseTime 75 seconds(Incasenoresponseisreceivedfromserver)

Reference

Note
When" +FTPGET: 1 , 1 "isshown,thenuse" AT+FTPGET= 2 ,<reqlength> "
toreaddata. Ifthemodulestillhasunreaddata," +FTPGET: 1 , 1 "willbe
shownagaininacertaintime.
10 2 15 AT+FTPPUT SetUploadFile.........................................................................................
AT+FTPPUT SetUploadFile
TestCommand
AT+FTPPUT=?

Response
OK
WriteCommand
AT+FTPPUT=[,
]

Response
Ifmodeis 1 anditisasuccessfulFTPgetsession:
OK
+FTPPUT: 1 , 1 ,<maxlength>
Ifmodeis 1 anditisafailedFTPgetsession:
OK
+FTPPUT: 1 ,<error>
Ifmodeis 2 and< reqlength >isnot 0
+FTPPUT: 2 ,<cnflength>
...... //Inputdata
OK
+FTPPUT: 1 , 1 , 1360
Ifmodeis 2 and< reqlength >is 0 ,itwillrespondOK,andFTPsessionwill
beclosed
OK
Ifdatatransferfinished.
+FTPPUT: 1 , 0
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
1 ForopeningFTPputsession
2 ForwritingFTPuploaddata.
Requestednumberofdatabytes( 0 - < maxlength >)tobe
transmitted
Confirmednumberofdatabytestobetransmitted
Themaxlengthofdatacanbesentatatime.Itdependson
thenetworkstatus.
See" AT+FTPGET "
ParameterSavingMode NO_SAVE
MaxResponseTime 75 seconds(Incasenoresponseisreceivedfromserver)

Reference
Note
When" +FTPPUT: 1 , 1 , "isshown,thenuse" AT+FTPPUT= 2 ,
"towritedata.

10 2 16 AT+FTPDELE DeleteSpecifiedFileinFTPServer...................................................
AT+FTPDELE DeleteSpecifiedFileinFTPServer
TestCommand
AT+FTPDELE=?

Response
OK
Parameters
SeeExecutionCommand
ExecutionCommand
AT+FTPDELE

Response
Ifsuccessed:
OK
+FTPDELE: 1 , 0
Iffailed:
OK
+FTPDELE: 1 ,<error>
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
See" AT+FTPGET "
ParameterSavingMode NO_SAVE
MaxResponseTime 75 seconds(Incasenoresponseisreceivedfromserver)

Reference
Note
The file to be deleted is specified by the " AT+FTPGETNAME " and
" AT+FTPGETPATH "commands.

10 2 17 AT+FTPSIZE GettheSizeofSpecifiedFileinFTPServer.....................................
AT+FTPSIZE GettheSizeofSpecifiedFileinFTPServer
TestCommand
AT+FTPSIZE=?

Response
OK
Parameters
SeeExecutionCommand
ExecutionCommand Response

AT+FTPSIZE Ifsuccessed:
OK

+FTPSIZE: 1 , 0 ,<size>
Iffailed:
OK
+FTPSIZE: 1 ,<error>, 0
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
See" AT+FTPGET "
Thefilesize.Unit:byte
ParameterSavingMode NO_SAVE
MaxResponseTime 75 seconds(Incasenoresponseisreceivedfromserver)

Reference Note
Thefileisspecifiedbythe" AT+FTPGETNAME "and" AT+FTPGETPATH "
commands.

10 2 18 AT+FTPSTATE GettheFTPState...............................................................................
AT+FTPSTATE GettheFTPState
TestCommand
AT+FTPSTATE=?

Response
OK
Parameters
SeeExecutionCommand
ExecutionCommand
AT+FTPSTATE

Response
+FTPSTATE:<state>
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters

0 Idle
1 IntheFTPsession,includingFTPGET,FTPPUT,FTPDELEand
FTPSIZEoperation.
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

10 2 19 AT+FTPEXTPUTExtendUploadFile.............................................................................
AT+FTPEXTPUTExtendUploadFile
TestCommand
AT+FTPEXTPUT=?

Response
OK
WriteCommand
AT+FTPEXTPUT=[,,,]

Response
Ifmodeis 0 or 1
OK
Ifmodeis 2
+FTPEXTPUT:<address>,<len>
...... //Inputdata
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
0 usedefaultFTPPUTmethod
1 useextendFTPPUTmethod
2 senddatatoRAMthroughserialport,thenFTPPUTmethod
willgetthedatafromRAM.
dataoffsetaddress 0 - 300 k
datalength 0 - 300 k
timeoutvalueofserialport. 1000 ms- 1000000 ms
< filename >Filenamelengthshouldlessorequal 50 characters.
< err > See"AT+FTPGET"
ParameterSavingMode NO_SAVE

MaxResponseTime 75 seconds(Incasenoresponseisreceivedfromserver)

Reference

Note
 When extend FTPPUT mode is activated,inputdatathenexecute
"AT+FTPPUT= 1 "totransmit,aftersessioniscomplete,ifsuccessful,it
returns "+FTPPUT: 1 , 0 ",otherwiseit returns "+FTPPUT: 1 ,<error>",
<error>see"AT+FTPGET".
10 2 20 AT+FTPMKD MakeDirectoryontheRemoteMachine............................................
AT+FTPMKD MakeDirectoryontheRemoteMachine
TestCommand Response

AT+FTPMKD=? OK
ExecutionCommand
AT+FTPMKD

Response
Ifsuccess:
OK
+FTPMKD: 1 , 0
Iffailed:
OK
+FTPMKD: 1 ,<error>
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
See" AT+FTPGET "
ParameterSavingMode NO_SAVE
MaxResponseTime 75 seconds(Incasenoresponseisreceivedfromserver)
Reference Note
Thecreatedfolderisspecifiedbythe" AT+FTPGETPATH "command.

10 2 21 AT+FTPRMD RemoveDirectoryontheRemoteMachine.......................................
AT+FTPRMD RemoveDirectoryontheRemoteMachine
TestCommand
AT+FTPRMD=?

Response
OK
ExecutionCommand
AT+FTPRMD

Response
Ifsuccess:
OK
+FTPRMD: 1 , 0
Iffailed:
OK
+FTPRMD: 1 ,<error>
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
See" AT+FTPGET "
ParameterSavingMode NO_SAVE

MaxResponseTime 75 seconds(Incasenoresponseisreceivedfromserver)
Reference Note
Theremovedfolderisspecifiedbythe" AT+FTPGETPATH "command.

10 2 22 AT+FTPLIST ListContentsofDirectoryontheRemoteMachine..........................
AT+FTPLIST ListContentsofDirectoryontheRemoteMachine
TestCommand
AT+FTPLIST=?

Response
OK
WriteCommand
AT+FTPLIST=[,
]

Response
Ifmodeis 1 anditisasuccessfulFTPgetsession:
OK
+FTPLIST: 1 , 1
Ifdatatransferisfinished:
+FTPLIST: 1 , 0
Ifmodeis 1 anditisafailedFTPgetsession:
OK
+FTPLIST: 1 ,<error>
Ifmodeis 2 :
+FTPLIST: 2 ,<cnflength>
012345678 ...
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters

1 ForopeningFTPgetfilelistsession
2 ForreadingFTPfilelist
< reqlength > Requestednumberofdatabytes( 1 - 1460 )toberead
< cnflength > Confirmednumberofdatabytestoberead,whichmaybe
lessthan. 0 indicatesthatnodatacanberead.
< error > See" AT+FTPGET "
ParameterSavingMode NO_SAVE
MaxResponseTime 75 seconds(Incasenoresponseisreceivedfromserver)
Reference Note
 When" +FTPLIST: 1 , 1 "isshown," AT+FTPLIST= 2 , "can

beusedtoreaddata.Ifthemodulestillhasunreaddata," +FTPLIST:
1 , 1 "willbeshownagaininacertaintime.
 Ifusing"AT+FTPGETPATH"tosetadirectorypath,itwillreturnedthe
filescontents underthis directory;ifsetafilepath,itwillreturnthe
informationofthefilespecified.
10 2 23 AT+FTPEXTGET ExtendDownloadFile.....................................................................
AT+FTPEXTGET ExtendDownloadFile
TestCommand
AT+FTPEXTGET=?

Response
OK
Parameters
SeeWriteCommand
ReadCommand
AT+FTPEXTGET?

Response
+FTPEXTGET:<mode>,<length>
OK
Parameters
SeeWriteCommand
WriteCommand
1 )ifmodeis 0 or 1
AT+FTPEXTGET=
3 )ifmodeis 3
AT+FTPEXTGET=,,

Response
Ifmodeis 0 :
OK
Ifmodeis 1 andsuccessfullydownloaddata:
OK
+FTPEXTGET: 1 , 0
Ifmodeis 1 andfailedtodownloaddata:
OK
+FTPEXTGET: 1 ,<error>
Ifmodeis 3 andsuccessfullydownloaddata:
+FTPEXTGET: 3 ,<length>
0123456 ...
OK
If<filename>isalreadyexistinflash:
ERROR
Parameters
<mode> 0 usedefaultFTPGETmethod.
1 openextendFTPgetsessionanddownloaddatatoRAM.
3 readthedownloadeddatafromRAM,thenoutputittothe
serialport.
Filenamelengthshouldlessthanorequalto 50 characters.
< pos > dataoffsetshouldlessthan.
< len > datalength 0 - 300 k.
< length > Thelengthofthedownloadeddatafromtheremotemachine.
< error > See"AT+FTPGET"
ParameterSavingMode NO_SAVE

MaxResponseTime 75 seconds(Incasenoresponseisreceivedfromserver)
Reference Note
 Thedataitcangetis 300 katmost.

10 2 24 AT+FTPETPUT UploadFile...........................................................................................
AT+FTPETPUT UploadFile
TestCommand
AT+FTPETPUT=?

Response
OK
Parameters
SeeWriteCommand
WriteCommand
**AT+FTPETPUT=<mode

**

Response
Ifmodeis 1 andsuccessfullyopenPUTsession:
OK
+FTPETPUT: 1 , 1
Ifmodeis 1 andfailedtoopenPUTsession:
OK
+FTPETPUT: 1 ,<error>
Ifmodeis 2 :
+FTPETPUT: 2 , 1
... //Inputdata
<ETX> //Tonotifythemodulethatalldatahasbeensent,switch
fromdatamodetocommandmode
OK
Ifdatatransferfinished:
+FTPETPUT: 1 , 0
Ifdatatransferfailed:
+FTPETPUT: 1 ,<error>
Parameters
1 ForopeningFTPETPUTsession.
2 ForwritingFTPuploaddata.
< error > See"AT+FTPEXTGET"
ParameterSavingMode NO_SAVE

MaxResponseTime -

Reference

Note
 TheTCP/IPstackwillonlyinterpretan<ETX>characterastheendof
thefiletobetransferredifit'snotprecededbya<DLE>character.Asa
consequencetheattachedhostmustsend<ETX>characterspreceded
by <DLE> characters and it must also code <DLE> characters in
<DLE><DLE>.
10 2 25 AT+FTPETGET DownloadFile.....................................................................................
AT+FTPETGET DownloadFile
TestCommand
AT+FTPETGET=?

Response
OK
Parameters
SeeWriteCommand
WriteCommand
**AT+FTPETGET=<mode

**

Response
Ifmodeis 1 andsuccessfullyopenGETsession:
OK
+FTPETGET: 1 , 1
Ifdatatransferfinished:
0123456789 ...
<ETX> //Tonotify theuser thatall datatransfer has beenfinished,
switchfromdatamodetocommandmode.
+FTPETGET: 1 , 0
Ifmodeis 1 andfailedtodownloaddata:
OK
+FTPETGET: 1 ,
Parameters
1 OpenFTPETGETsessionanddownloaddata.
< error > See"AT+FTPEXTGET"
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

Note
 Each<ETX>characterpresentinthepayloaddataoftheFTPflowwill
becodedbytheTCP/IPstackontheserialportas<DLE><ETX>.Each
<DLE>characterwillbecodedas<DLE><DLE>.Theattachedhost
mustthendecodetheFTPflowtoremovetheseescapecharacters.
10 2 26 AT+FTPQUIT QuitCurrentFTPSession....................................................................
AT+FTPQUIT QuitCurrentFTPSession
TestCommand
AT+FTPQUIT=?

Response
OK
ExecutionCommand
AT+FTPQUIT

Response
IfthecurrentoperationisGETmethod:
OK
+FTPGET: 1 , 80
IfthecurrentoperationisPUTmethod:
OK
+FTPPUT: 1 , 80
IfFTPisinidlestate:
ERROR
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

10 2 27 AT+FTPRENAME RenametheSpecifiedFileontheRemoteMachine................
AT+FTPRENAMERenametheSpecifiedFileontheRemoteMachine
TestCommand
AT+FTRENAME=?

Response
OK
Parameters
SeeExecutionCommand
ExecutionCommand
AT+FTPRENAME

Response
Ifsuccess:
OK
+FTPRENAME: 1 , 0
Iffailed:
OK
+FTPRENAME: 1 ,<error>
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameter
See"AT+FTPGET"
ParameterSavingMode NO_SAVE

MaxResponseTime -

Reference

Note
 The file is specified by the "AT+FTPGETNAME" and
"AT+FTPGETPATH"commands.
 The new file name is set by "AT+FTPPUTNAME" and
"AT+FTPPUTPATH"command.
10. 2. 28 AT+FTPMDTM GettheLastModificationTimestampofSpecifiedFileon the
RemoteMachine
RemoteMachine......................................................................................................................................... 10 2 28 AT+FTPMDTM Get theLast Modification Timestamp of Specified File onthe
RemoteMachine
TestCommand
AT+FTPMDTM=?

Response
OK
Parameters
SeeExecutionCommand
ExecutionCommand
AT+FTPMDTM

Response
Ifsuccess:
OK
+FTPMDTM: 1 , 0 ,<timestamp>
Iffailed:
OK
+FTPMDTM: 1 ,<error>
IferrorisrelatedtoMEfunctionality:
+CMEERROR:<err>
Parameter
<error> See"AT+FTPGET"
<timestamp> Thelastmodificationtimestampofthespecifiedfile.
ParameterSavingMode NO_SAVE

MaxResponseTime -

Reference

Note
Thefileisspecifiedbythe"AT+FTPGETNAME"and"AT+FTPGETPATH"
commands.
11 ATCommandforNTPfunction......................................................................................
11 1 Overview..............................................................................................................................................
Command Description
AT+CNTPCID SetGPRSbearerprofile’sID
AT+CNTP Synchronizenetworktime

11 2 DetailedDescriptionsofCommands...............................................................................................
11 2 1 AT+CNTPCID SetGPRSBearerProfile’sID.....................................................................
AT+CNTPCID SetGPRSBearerProfile’sID
TestCommand
AT+CNTPCID=?

Response
+CNTPCID:( rangeofsupporded <cid> s )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CNTPCID?

Response
+CNTPCID:<cid>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CNTPCID=

Response
OK
IferrorisrelatedtoMEfunctionality:
ERROR
Parameters
Bearer profileidentifier,refer toAT+SAPBR
ParameterSavingMode -
MaxResponseTime -

Reference Note

11 2 2 AT+CNTP SynchronizeNetworkTime.................................................................................
AT+CNTP SynchronizeNetworkTime
TestCommand
AT+CNTP=?

Response
+CNTP:( lengthof <ntpserver>) ,(rangeof <timezone>),( rangeof <cid>),
(rangeof <mode>)
OK
Parameter
SeeWriteCommand
ReadCommand
AT+CNTP?

Response
+CNTP:<ntpsever>,<timezone>,<cid>,<mode>
OK
Parameter
SeeWriteCommand
WriteCommand
**AT+CNTP=[,][,][,<mode

]**

Response
OK
Parameter
<ntpserver> NTPserver’surl
<timezone> Localtimezone,therangeis(- 47 to 48 ),infact,time
zonerange(- 12 to 12 ),buttakingintoaccountthatsomecountriesand
regionswillusehalftimezone,orevenfourthtimezone,sotheentire
extendedfourtimezonesX,sothatwhenthetimezoneoftheinputintegers
areused,withouttheneedfordecimal.TimezoneinfrontoftheWestifitis
anegativenumberindicatesthetimezone.
<cid> Bearerprofileidentifier,refertoAT+SAPBR
<mode> printnetworktimeonuartandsettolocaltime
0 Justsetnetworktolocaltime
1 JustoutputnetworktimetoATport
2 SetnetworktolocaltimeandoutputnetworktimetoATport
Executioncommand
AT+CNTP

Response
OK
+CNTP:<code>[,<time>]
Parameter
<code> 1 Networktimesynchronizationissuccessful
61 NetworkError
62 DNSresolutionerror
63 ConnectionErro
64 Serviceresponseerror
65 ServiceResponseTimeout
Networktime
ParameterSavingMode -
MaxResponseTime -

Reference

Note
 Aftersuccessfulsynchronizationtime,youcanuseAT+CCLKtoquery
localtime.
12 ATCommandsforOneNetApplication........................................................................
12 1 Overview..............................................................................................................................................
Command Description
AT+MIPLCREATE CreateOneNetconfiguration
AT+MIPLDELETE DeleteOneNetconfiguration
AT+MIPLOPEN ConnecttoOneNet
AT+MIPLADDOBJ Addobject

AT+MIPLDELOBJ Deleteobject
AT+MIPLCLOSE DisconnecttoOneNet
AT+MIPLNOTIFY NotifydatatoOneNet
AT+MIPLREADRSP Sendresponseonreadcommand

AT+MIPLWRITERSP Sendresponseonwritecommand
AT+MIPLEXECUTERSP Sendresponseonexecutecommand
AT+MIPLOBSERVERSP Sendresponseonobservecommand
AT+MIPLDISCOVERRSP Sendresponseondiscovercommand

AT+MIPLPARAMETERRSP Sendresponseonparametercommand
AT+MIPLUPDATE Updateregistration
AT+MIPLVER VersionofOneNetSDK
AT+MIPLBOOTSTRAP Bootstrapmode

+MIPLREAD Readrequesttouser
+MIPLWRITE Writerequesttouser
+MIPLEXECUTE Executerequesttouser
+MIPLOBSERVE Observerequesttouser

+MIPLDISCOVER Discoverrequesttouser
+MIPLPARAMETER Setparameterrequesttouser
+MIPLEVENT Eventindicationtouser

12 2 DetailedDescriptionsofCommands...............................................................................................
12 2 1 AT+MIPLCREATE CreateOneNetconfiguration...............................................................
AT+MIPLCREATE CreateOneNetconfiguration
TestCommand
AT+MIPLCREATE=?

Response
+MIPLCREATE:<size>,<config>,<index>,<totalsize>,<flag>
OK
Parameters
SeeWriteCommand
ExecutionCommand
AT+MIPLCREATE

Response
<ref>
OK
WriteCommand
AT+MIPLCREATE=,,,,

Response
<ref>
OK
Parameters
Currentsize
Configinhexformat
Currentconfigindex
Totalconfigsize
Indicatetheinputisoverornot
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

12 2 2 AT+MIPLDELETE DeleteOneNetconfiguration................................................................
AT+MIPLDELETE DeleteOneNetconfiguration
TestCommand
AT+MIPLDELETE=?

Response
+MIPLDELETE:<ref>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+MIPLDELETE=<ref

Response
OK
> Parameters
Configid
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

12 2 3 AT+MIPLOPEN ConnecttoOneNet....................................................................................
AT+MIPLOPEN ConnecttoOneNet
TestCommand
AT+MIPLOPEN=?

Response
+MIPLOPEN:<ref>,<lifetime>,<param>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+MIPLOPEN=,<
lifetime>,

Response
OK
Parameters
Configid
Lifetimetoupdateautomatically
Reserved
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference Note

12 2 4 AT+MIPLADDOBJ Addobject...............................................................................................
AT+MIPLADDOBJ Addobject
TestCommand
AT+MIPLADDOBJ=?

Response
+MIPLADDOBJ:
<ref>,<objectid>,<instancecount>,<instanceBitmap>,<attributeCount>
,<actionCount>
OK
Parameters
SeeWriteCommand
WriteCommand
**AT+MIPLADDOBJ=<ref

,,<instance**

Response
OK
Parameters
count>,,,<
actionCount>

Configid
Objectid
Countofinstance
Bitmapofinstance
Countofattributeresource
Countofactionresource
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference Note

12 2 5 AT+MIPLDELOBJ DeleteObject..........................................................................................
AT+MIPLDELOBJ Deleteobject
TestCommand
AT+MIPLDELOBJ=?

Response
+MIPLDELOBJ:<ref>,<objectid>
OK
Parameters
SeeWriteCommand
WriteCommand
**AT+MIPLDELOBJ=<ref

,**

Response
OK
Parameters
Configid
Objectid
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note
12 2 6 AT+MIPLCLOSE DisconnecttoOneNet.............................................................................
AT+MIPLCLOSE DisconnecttoOneNet
TestCommand
AT+MIPLCLOSE=?

Response
+MIPLCLOSE:<ref>
OK
Parameters
SeeWriteCommand
WriteCommand Response

AT+MIPLCLOSE= OK

Parameters
Configid
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

12 2 7 AT+MIPLNOTIFY NotifyDatatoOneNet............................................................................
AT+MIPLNOTIFY NotifyDatatoOneNet
TestCommand
AT+MIPLNOTIFY=?

Response
+MIPLNOTIFY:
<ref>,<msgid>,<objectid>,<instanceid>,<resourceid>,<valuetype>,<le
n>,<value>,<index>,<flag>[,<ackid>]
OK
Parameters
SeeWriteCommand
WriteCommand
**AT+MIPLNOTIFY=
,,,,,,,
,,<flag

[,]**

Response
OK
Parameters
Configid
Objectid
Instanceid
Resourceid
Typeofvalue
1 String
2 Opaque
3 Integer
4 Float
5 Bool
Length
Valuestring
Indexofcurrentinput
Indicatetheinputisoverornot
Needackornot
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

12 2 8 AT+MIPLREADRSP SendResponseonReadCommand..............................................
AT+MIPLREADRSP SendResponseonReadCommand
TestCommand
AT+MIPLREADRSP=?

Response
+MIPLREADRSP:
<ref>,<msgid>,<result>,<objectid>,<instanceid>,<resourceid>,<valuet
ype>,<len>,<value>,<index>,<flag>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+MIPLREADRSP=,,,<
objectid>,
,,,,,,

Response
OK
Parameters
Configid
Messageid
Result
Objectid
Instanceid
Resourceid
Typeofvalue
1 String
2 Opaque
3 Integer
4 Float
5 Bool
Length
Valuestring
Indexofcurrentinput
Indicatetheinputisoverornot
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
Note

12 2 9 AT+MIPLWRITERSP SendResponseonWriteCommand.............................................
AT+MIPLWRITERSP SendResponseonWriteCommand
TestCommand
AT+MIPLWRITERSP=?

Response
+MIPLWRITERSP:<ref>,<msgid>,<result>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+MIPLWRITERSP=<
ref>,,

Response
OK
Parameters
Configid
Messageid
Result
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
Note

12 2 10 AT+MIPLEXECUTERSP SendResponseonExecuteCommand.........................
AT+MIPLEXECUTERSP SendResponseonExecuteCommand
TestCommand
AT+MIPLEXECUTERS
P=?

Response
+MIPLEXECUTERSP:<ref>,<msgid>,<result>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+MIPLEXECUTERS
P=,,

Response
OK
Parameters
Configid
Messageid
Result
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

12 2 11 AT+MIPLOBSERVERSP SendResponseOnObserveCommand.......................
AT+MIPLOBSERVERSP SendResponseonObserveCommand
TestCommand Response

AT+MIPLOBSERVERS
P=?
+MIPLOBSERVERSP:<ref>,<msgid>,<result>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+MIPLOBSERVERS
P=,,

Response
OK
Parameters
Configid
Messageid
Result
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

12 2 12 AT+MIPLDISCOVERRSP SendResponseonDiscoverCommand......................
AT+MIPLDISCOVERRSP SendResponseonDiscoverCommand
TestCommand
AT+MIPLDISCOVERRS
P=?

Response
+MIPLDISCOVERRSP:<ref>,<msgid>,<result>,<length>,<valuestring>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+MIPLDISCOVERRS
P=,,,,

Response
OK
Parameters
Configid
Messageid
Result
Numberofresourceid
Resourceidstring
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
Note

12 2 13 AT+MIPLPARAMETERRSP SendResponseonParameterCommand...............
AT+MIPLPARAMETERRSP SendResponseonParameterCommand
TestCommand
AT+MIPLPARAMETER
RSP=?

Response
+MIPLPARAMETERRSP:<ref>,<msgid>,<result>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+MIPLPARAMETER
RSP=,,

Response
OK
Parameters
Configid
Messageid
Result
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference
Note

12 2 14 AT+MIPLUPDATE UpdateRegistration.......................................................................
AT+MIPLUPDATE UpdateRegistration
TestCommand
AT+MIPLUPDATE=?

Response
+MIPLUPDATE:<ref>,<lifetime>,<flag>
OK
Parameters
SeeWriteCommand
WriteCommand
**AT+MIPLUPDATE=<ref

,,**

Response
OK
Parameters
Configid
Lifetimetoupdate
Updatewithobjectupdateornot
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
Note

12 2 15 AT+MIPLVER VersionofOneNetSDK........................................................................
AT+MIPLVER VersionofOneNetSDK
ReadCommand
AT+MIPLVER?

Response
+MIPLVER:<version>
OK
Parameters
VersionofSDK
ParameterSavingMode -

MaxResponseTime -
Reference
Note

12 2 16 AT+MIPLBOOTSTRAP BootstrapMode.....................................................................
AT+MIPLBOOTSTRAP BootstrapMode
WriteCommand
AT+MIPLBOOTSTRAP
=

Response
OK
Parameters
Bootstrapmode
0 Disable
1 Enable
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

12 2 17 +MIPLREAD ReadRequesttoUser............................................................................
+MIPLREAD ReadRequesttoUser
Response
+MIPLREAD:<ref>,<msgid>,<objectid>,<instanceid>,<resourceid>
Parameters
<ref> Integer,OneNETinstancereturnedbyAT+MIPLCREATE
<msgid> Integer,messageid
<objectid> Integer,objectid
<instanceid> Integer,instanceid,readallresourcesofallinstancesof
theobjectifinstanceidequals- 1
<resourceid> Integer,resourceid,readallresourcesoftheinstanceif
resourceidequals- 1
12 2 18 +MIPLWRITE WriteRequesttoUser...........................................................................
+MIPLWRITE WriteRequesttoUser
Response
+MIPLWRITE:
<ref>,<msgid>,<objectid>,<instanceid>,<resourceid>,<valuetype>,<le
n>,<value>,<flag>,<index>
Parameters
<ref> Integer,OneNETinstancereturnedbyAT+MIPLCREATE
<msgid> Integer,messageid
<objectid> Integer,objectid
<instanceid> Integer,instanceid
<resourceid> Integer,resourceid
<valuetype> Integer,writedatavaluetype
1 String
2 Opaque
3 Integer
0 Float
5 Bool
<len> Integer,writedatalength.Itcanbeommited,ifvaluetypeisInteger
orFloat,orBool
<value> Integer,writedatavalue
< flag > Integer,messageflag
1 Firstmessage;
2 Middlemessage;
0 Lastmessage
< index > Integer,messageindex,from 0 to 1024
12 2 19 +MIPLEXECUTE ExecuteRequesttoUser...............................................................
+MIPLEXECUTE ExecuteRequesttoUser
Response
+MIPLEXECUTE:
<ref>,<msgid>,<objectid>,<instanceid>,<resourceid>,<len>,<argumen
ts>
Parameters
<ref> Integer,OneNETinstancereturnedbyAT+MIPLCREATE
<msgid> Integer,messageid
<objectid> Integer,objectid
<instanceid> Integer,instanceid
<resourceid> Integer,resourceid
<len> Integer,parameterlength
<arguments> String,parameterstring
12 2 20 +MIPLOBSERVE ObserveRequesttoUser..............................................................
+MIPLOBSERVE ObserveRequesttoUser
Response
+MIPLOBSERVE:
<ref>,<msgid>,<flag>,<objectid>,<instanceid>,<resourceid>
Parameters
<ref> Integer,OneNETinstancereturnedbyAT+MIPLCREATE
<msgid> Integer,messageid
< flag > Integer,observeflag.
1 Indicatesobserve
0 Indicatescancelobserve
<objectid> Integer,objectid
<instanceid> Integer,instanceid,observeallresourcesofallinstances
oftheobjectifinstanceidequals- 1
<resourceid> Integer,resourceid,observeallresourcesoftheinstanceif
resourceidequals- 1
12 2 21 +MIPLDISCOVER DiscoverRequesttoUser............................................................
+MIPLDISCOVER DiscoverRequesttoUser
Response
+MIPLDISCOVER:<ref>,<msgid>,<objectid>
Parameters
<ref> Integer,OneNETinstancereturnedbyAT+MIPLCREATE
<msgid> Integer,messageid
<objectid> Integer,objectid
12 2 22 +MIPLPARAMETER SetParameterRequesttoUser..............................................
+MIPLPARAMETER SetParameterRequesttoUser
Response
+MIPLPARAMETER:
<ref>,<msgid>,<objectid>,<instanceid>,<resourceid>,<len>,<paramete
r>
Parameters
<ref> Integer,OneNETinstancereturnedbyAT+MIPLCREATE
<msgid> Integer,messageid
<objectid> Integer,objectid
<instanceid> Integer,instanceid,observeallresourcesofallinstances
oftheobjectifinstanceidequals- 1
<resourceid> Integer,resourceid,observeallresourcesoftheinstanceif
resourceidequals- 1
< len > Integer,parameterlength
< parameter > String,parameterstring,muststartwith"andendwith"
pmin=xxx;pmax=xxx;gt=xxx;lt=xxx;stp=xxx
12 2 23 +MIPLEVENT EventIndicationtoUser.......................................................................
+MIPLEVENT EventIndicationtoUser
Response
+MIPLEVENT:<ref>,<evtid>
Parameters
<ref> Integer,OneNETinstancereturnedbyAT+MIPLCREATE
<evtid> Integer,eventid
1 BOOTSTRAP_START
2 BOOTSTRAP_SUCCESS
3 BOOTSTRAP_FAILED
4 CONNECT_SUCCESS
5 CONNECT_FAILED
6 REG_SUCCESS
7 REG_FAILED
8 REG_TIMEOUT
9 LIFETIME_TIMEOUT
10 STATUS_HALT
11 UPDATE_SUCCESS
12 UPDATE_FAILED
13 UPDATE_TIMEOUT
14 UPDATE_NEED
15 UNREG_DONE
20 RESPONSE_FAILED
21 RESPONSE_SUCCESS
25 NOTIFY_FAILED
26 NOTIFY_SUCCESS
13 ATCommandsforTelecomIOTApplication..............................................................
13 1 Overview..............................................................................................................................................
Command Description
AT+SIMLCREATE Createconfiguration
AT+SIMLMODE Connectionmode
AT+SIMLOPEN ConnecttoTelecomIOT
AT+SIMLSEND SenddatatoTelecomIOT

AT+SIMLCLOSE DisconnecttoTelecomIOT

13 2 DetailedDescriptionsofCommands...............................................................................................
13 2 1 AT+SIMLCREATE CreateConfiguration.............................................................................
AT+SIMLCREATE CreateConfiguration
TestCommand
AT+SIMLCREATE=?

Response
+SIMLCREATE:<config>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+SIMLCREATE=

Response
OK
Parameters
Configinhexformat
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference
Note

13 2 2 AT+SIMLMODE ConnectionMode.......................................................................................
AT+SIMLMODE ConnectionMode
TestCommand
AT+SIMLMODE=?

Response
+SIMLMODE:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+SIMLMODE=

Response
OK
Parameters
Connectionmode
1 Other
2 ChinaTelecomIOT
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
Note

13 2 3 AT+SIMLOPEN ConnecttoTelecomIOT............................................................................
AT+SIMLOPEN ConnecttoTelecomIOT
TestCommand
AT+SIMLOPEN=?

Response
+SIMLOPEN:<lifetime>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+SIMLOPEN=

Response
OK
Parameters
Reserved
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
Note

13 2 4 AT+SIMLSEND SendDatatoTelecomIOT........................................................................
AT+SIMLSEND SendDatatoTelecomIOT
TestCommand
AT+SIMLSEND=?

Response
+SIMLSEND:<data>,<flag>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+SIMLSEND=
,

Response
OK
Parameters
Stringinhexformat
< flag >
0 Inputover
1 Inputnotover
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference
Note

13 2 5 AT+SIMLCLOSE DisconnecttoTelecomIOT....................................................................
AT+SIMLCLOSE DisconnecttoTelecomIOT
ExecutionCommand
AT+SIMLCLOSE

Response
OK
Parameters
ParameterSavingMode -

MaxResponseTime -
Reference
Note

14 ATCommandsforGNSSApplication...........................................................................
SIM 7000 seriesmodulesprovideGNSSATcommandisasfollows:

14 1 Overview..............................................................................................................................................
Command Description
AT+CGNSPWR GNSSPowerControl

AT+CGNSINF GNSSNavigationInformationParsedFromNMEASentences
AT+CGNSURC GNSSNavigationURCReport
AT+CGNSPORT GNSSNMEAOutPortSet
AT+CGNSCOLD GNSSColdStart

AT+CGNSWARM GNSSWarmStart
AT+CGNSHOT GNSSHotStart
AT+CGNSMOD GNSSWorkModeSet
AT+CGNSCFG GNSSNMEAOutConfigure

AT+CGNSTST GNSSNMEADataOutputtoATPort
AT+CGNSXTRA GNSSXTRAFunctionOpen
AT+CGNSCPY GNSSXTRAFileCopy
AT+CGNSRTMS GNSSNMEAoutfrequencyconfigure

AT+CGNSHOR ConfigurePositioningDesiredAccuracy
AT+CGNSUTIPR ConfigureBaudRateWhenNMEAOutputFromUART 3
AT+CGNSNMEA ConfigureNMEAoutputsentences
AT+CGTP IZATGNSSConfigure

AT+CGNSSUPLCFG GNSSSUPLConfigure
AT+CGNSSUPL GNSSSUPLControl

14 2 DetailedDescriptionsofCommands...............................................................................................
14 2 1 AT+CGNSPWR GNSSPowerControl.................................................................................
AT+CGNSPWR GNSSPowerControl
TestCommand
AT+CGNSPWR=?

Response
+CGNSPWR:( listofsupported <mode> s )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CGNSPWR?

Response
TAreturnsthecurrentstatusofGNSSPowersupply
+CGNSPWR:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CGNSPWR=

Response
OK
or
ERROR
Parameters

0 TurnoffGNSSpowersupply
1 TurnonGNSSpowersupply
ParameterSavingMode NO_SAVE

MaxResponseTime -

Reference
NMEAdatawillnotoutputtousb’sNMEAportwhensetAT+CGNSPWR= 1
throughuartportexceptconfigitbyAT+CGNSCFG= 1.

14 2 2 AT+CGNSINF GNSSNavigationInformationParsedFromNMEASentences...........
AT+CGNSINFGNSSNavigationInformationParsedFromNMEASentences
TestCommand
AT+CGNSINF=?

Response
OK
Parameters
SeeExecutionCommand
ExecutionCommand
AT+CGNSINF

Response
+CGNSINF: <GNSS run status>,<Fix status>,<UTC date &
Time>,<Latitude>,<Longitude>,<MSL Altitude>,<Speed Over
Ground>,<Course Over Ground>,<Fix
Mode>,<Reserved 1 >,<HDOP>,<PDOP>,<VDOP>,<Reserved 2 >,<GNSS
Satellites in View>,<GNSS Satellites Used>,<GLONASS Satellites
Used>,<Reserved 3 >,<C/N 0 max>,<HPA>,<VPA>
OK
Parameters

0 GNSSoff
1 GNSSon

0 Notfixedposition
1 Fixedposition
Seebelowtable 15 - 1.
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference

Table 15 - 1 :AT+CGNSINFreturnParameters

Index Parameter Unit Range Length
1 GNSSrunstatus -- 0 - 1 1
2 Fixstatus -- 0 - 1 1
3 UTCdate&Time
yyyyMMddhhmm
ss.sss
yyyy:[ 1980 , 2039 ]
MM:[ 1 , 12 ]
dd: [ 1 , 31 ]
hh: [ 0 , 23 ]
mm: [ 0 , 59 ]
ss.sss:[ 0. 000 , 60. 999 ]
18
4 Latitude ±dd.dddddd [- 90. 000000 , 90. 000000 ] 10
5 Longitude ±ddd.dddddd [- 180. 000000 , 180. 000000 ] 11
6 MSLAltitude meters 8
7 SpeedOverGround Km/hour [ 0 , 999. 99 ] 6
8 CourseOverGround degrees [ 0 , 360. 00 ] 6
9 FixMode -- 0 , 1 , 2 [^1 ] 1
10 Reserved 1 0
11 HDOP -- [ 0 , 99. 9 ] 4
12 PDOP -- [ 0 , 99. 9 ] 4
13 VDOP -- [ 0 , 99. 9 ] 4
14 Reserved 2 0
15 GNSSSatellitesinView -- [ 0 , 99 ] 2
16 GPSSatellitesUsed -- [ 0 , 99 ] 2
17 GLONASSSatellitesused -- [ 0 , 99 ] 2
18 Reserved 3 0
19 C/N 0 max dBHz [ 0 , 55 ] 2
20 HPA[^2 ] meters [ 0 , 9999. 9 ] 6
21 VPA[^2 ] meters [ 0 , 9999. 9 ] 6
Total：( 94 ) chars
**_Note:

TherangeofdependsontheGNSSchipused._**
Reserved.
14 2 3 AT+CGNSURC GNSSNavigationURCReport.................................................................
AT+CGNSURC GNSSNavigationURCReport
TestCommand
AT+CGNSURC=?

Response
+CGNSURC:( 0 - 255 )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CGNSURC?

Response
TAreturnsthecurrentURCsetting
+CGNSURC:<Navigationmode>
OK
Parameters
SeeWriteCommand
UnsolicitedResultCode
+UGNSINF: <GNSS run status>,<Fix status>,<UTC date &
Time>,<Latitude>,<Longitude>,<MSL Altitude>,<Speed Over
Ground>,<Course Over Ground>,<Fix
Mode>,<Reserved 1 >,<HDOP>,<PDOP>,<VDOP>,<Reserved 2 >,<GNSS
Satellites in View>,<GNSS Satellites Used>,<GLONASS Satellites
Used>,<Reserved 3 >,<C/N 0 max>,<HPA>,<VPA>
WriteCommand
AT+CGNSURC=

Response
OK
or
ERROR
Parameters
:
0 TurnoffnavigationdataURCreport
1 TurnonnavigationdataURCreport,andreporteveryGNSSFIX
2 TurnonnavigationdataURCreport,andreportevery 2 GNSSFIX
...
255 TurnonnavigationdataURCreport,andreportevery 255 GNSSFIX
ParameterSavingMode NO_SAVE

MaxResponseTime -

Reference

Note
 Factorysettingis " AT+CGNSURC= 0 ".
 URC "+UGNSINF:" parametersarethesameas "+CGNSINF:" return.
14 2 4 AT+CGNSPORT GNSSNMEAOutPortSet......................................................................
AT+CGNSPORT GNSSNMEAOutPortSet
TestCommand
AT+CGNSPORT=?

Response
+CGNSPORT:( listofsupported <port>)
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CGNSPORT?

Response
+CGNSPORT:<port>
OK
WriteCommand
**AT+CGNSPORT=<port

**

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
NumoftheportNMEAout
3 NMEAport
4 NONE
ParameterSavingMode AUTO_SAVE_REBOOT
MaxResponseTime -
Reference Note
Modulemustreboottomakeiteffectifvalueischanged.

14 2 5 AT+CGNSCOLD GNSSColdStart......................................................................................
AT+CGNSCOLD GNSSColdStart
Test Command
AT+CGNSCOLD=?

Response
OK
Execution Command
AT+CGNSCOLD

Response
IfAT+CGNSXTRA= 0
OK
ElseifAT+CGNSXTRA= 1
OK
+CGNSXTRA:
Parameters

0 AidXTRAfilesuccess
1 XTRAfileisnotexist
2 XTRAfileisnoteffective
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

14 2 6 AT+CGNSWARM GNSSWarmStart...................................................................................
AT+CGNSWARMGNSSWarmStart
Test Command
AT+CGNSWARM=?

Response
OK
Execution Command
AT+CGNSWARM

Response
OK
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

14 2 7 AT+CGNSHOT GNSSHotStart...........................................................................................
AT+CGNSHOT GNSSHotStart
Test Command
AT+CGNSHOT=?

Response
OK
Execution Command
AT+CGNSHOT

Response
OK
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference Note

14 2 8 AT+CGNSMOD GNSSWorkModeSet..............................................................................
AT+CGNSMOD GNSSWorkModeSet
TestCommand
AT+CGNSMOD=?

Response
+CGNSMOD: ( list of supported <gps mode>),( list of supported <glo
mode>s),( listofsupported <bdmode>s),( listofsupported <galmode>s)
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CGNSMOD?

Response
+CGNSMOD:<gpsmode>,<glomode>,<bdmode>,<galmode>
OK
WriteCommand
AT+CGNSMOD=,,,

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
GPSworkmode
1 StartGPSNMEAout
GLONASSworkmode
0 StopGLONASSNMEAout
1 StartGLONASSNMEAout
BEIDOUworkmode
0 StopBEIDOUNMEAout
1 StartBEIDOUNMEAout
2 BEIDOUoutsideofus
GALILEANworkmode
0 StopGALILEANNMEAout
1 StartGALILEANNMEAout
2 GALILEANoutsideofus
ParameterSavingMode AUTO_SAVE_REBOOT
MaxResponseTime -

Reference Note

14 2 9 AT+CGNSCFG GNSSNMEAOutConfigure.....................................................................
AT+CGNSCFG GNSSNMEAOutConfigure
TestCommand
AT+CGNSCFG=?

Response
+CGNSCFG:( listofsupported <mode> s )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CGNSCFG?

Response
TAreturnsthecurrentstatusofconfigure
+CGNSCFG:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand
**AT+CGNSCFG=<mode

**

Response
OK
or
ERROR
Parameters
<mode>
0 TurnoffGNSSNMEAdataoutputtoUSB’sNMEAportwhenset
AT+CGNSPWR= 1 / 0 throughUART
1 TurnonGNSSNMEAdataoutputtoUSB’sNMEAportwhenset
AT+CGNSPWR= 1 / 0 throughUART
2 Turn on GNSS NMEA data output to UART 3 port when set
AT+CGNSPWR= 1 / 0
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference
Note
ThiscommandonlysupportedinUARTport.

14 2 10 AT+CGNSTST GNSSNMEADataOutputtoATPort...............................................
AT+CGNSTST GNSSNMEADataOutputtoATPort
TestCommand
AT+CGNSTST=?

Response
+CGNSTST:( 0 - 1 ),( 1 - 255 )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CGNSTST?

Response
TAreturnsthecurrentstatusofconfigure
+CGNSTST:<TST>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CGNSTST=[,
]

Response
OK
or
ERROR
Parameters

0 TurnoffGNSSNMEAdataoutputtoATport
1 TurnonGNSSNMEAdataoutputtoATport
thenumberofNMEAdatapackage
1 - 255
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

14 2 11 AT+CGNSXTRA GNSSXTRAFunctionOpen...........................................................
AT+CGNSXTRA GNSSXTRAFunctionOpen
TestCommand
AT+CGNSXTRA=?

Response
+CGNSXTRA:( 0 - 1 )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CGNSXTRA?

Response
TAreturnsthecurrentstatusofconfigure
+CGNSXTRA:<enable>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CGNSXTRA=

Response
OK
or
ERROR
Parameters

0 DisableXTRAfunction
1 EnableXTRAfunction
ExecutionCommand
AT+CGNSXTRA

Response
ThiscommandisusedtoqueryvalidatetimeofXTRAfile.TheXTRAfile
existsifthedownloadandcopyaresuccessful.
IfXTRAfileisnotexist
ERROR
ElseifXTRAfileisexist
<validDurationHours>,<InjectgpsOneXTRGPStime>
OK
Parameters
Validate time of XTRA file,Unit is Hour. Defaut
valueis 168.
DownloadtimeofXTRAfile.
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference Note

14 2 12 AT+CGNSCPY GNSSXTRAFileCopy.......................................................................
AT+CGNSCPYGNSSXTRAFileCopy
TestCommand
AT+CGNSCPY=?

Response
OK
Parameters
SeeExecutionCommand
ExecutionCommand
AT+CGNSCPY

Response
+CGNSCPY:<ret>
OK
Parameters

1 Filenotexist
0 Copysuccess
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference

14 2 13 AT+CGNSRTMS GNSSNMEAOutFrequencyConfigure......................................
AT+CGNSRTMS GNSSNMEAOutFrequencyConfigure
TestCommand
AT+CGNSRTMS=?

Response
+CGNSRTMS:( listofsupported <frequency> s )
OK
Parameters
SeeReadCommand
ReadCommand
AT+CGNSRTMS?

Response
+CGNSRTMS:<frequency>
OK
Parameters
GNSSNMEAOutFrequency,rangeis 50 - 1000.
Defaultvalueis 1000.
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference

14 2 14 AT+CGNSHOR ConfigurePositioningDesiredAccuracy......................................
AT+CGNSHOR ConfigurePositioningDesiredAccuracy
TestCommand
AT+CGNSHOR=?

Response
+CGNSHOR:( 0 - 1800000 )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CGNSHOR?

Response
TAreturnsthecurrentstatusofconfigure
+CGNSHOR:<acc>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CGNSHOR=

Response
OK
or
ERROR
Parameters
Configurethepositioningdesiredaccuracythresholdinmeters.
Range: 0 - 1800000 Defaultvalueis 50
ParameterSavingMode NO_SAVE

MaxResponseTime -
Reference

14 2 15 AT+CGNSUTIPR ConfigureBaudRateWhenNMEAOutputfromUART
AT+CGNSUTIPR ConfigureBaudRateWhenNMEAOutputfromUART 3
TestCommand
AT+CGNSUTIPR=?

Response
+CGNSUTIPR:( 9600 , 19200 , 38400 , 57600 , 115200 )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CGNSUTIPR?

Response
TAreturnsthecurrentstatusofconfigure
+CGNSUTIPR:<ipr>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CGNSUTIPR=

Response
OK
or
ERROR
Parameters
< ipr > BaudratewhenNMEAoutputfromUART 3.
9600
19200
38400
57600
115200
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

Note
When GPS is started, set AT+CGNSUTIPR=<ipr> first, then use
AT+CGNSCFG= 2 toconfigureUART 3 output.After turningonGPS,you
canusethesetbaudrateoutputinUART 3.
14 2 16 AT+CGNSNMEA ConfigureNMEAOutputSentences.............................................
AT+CGNSNMEA ConfigureNMEAOutputSentences
TestCommand
AT+CGNSNMEA=?

Response
+CGNSNMEA:( rangeofsupported <nmea> s )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CGNSNMEA?

Response
+CGNSNMEA:<nmea>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CGNSNMEA=

This command is used toconfigureNMEAoutputsentences which are
generatedbytheGPSOneenginewhenpositiondataisavailable.
Response
OK
or
ERROR
Parameters
< nmea > Rangeis 0 - 262143.
EachbitenablesanNMEAsentenceoutputasfollows:
Bit 0 GPGGA(globalpositioningsystemfixdata)
Bit 1 GPRMC(recommendedminimumspecificGPS/TRANSITdata)
Bit 2 GPGSV(GPSsatellitesinview)
Bit 3 GPGSA(GPSDOPandactivesatellites)
Bit 4 GPVTG(trackmadegoodandgroundspeed)
Bit 5 PQXFI(GlobalPositioningSystemExtendedFixData.)
Bit 6 GLGSV(GLONASSsatellitesinviewGLONASSfixesonly)
Bit 7 GNGSA( 1 .GPS/ 2 .Glonass/ 3 .GALILEDOPandActive
Satellites.)
Bit 8 GNGNS(fixdataforGNSSreceivers;outputfor
GPS,GLONASS,GALILEO)
Bit 9 Reserved
Bit 10 GAGSV(GALILEOsatellitesinview)
Bit 11 Reserved
Bit 12 Reserved
Bit 13 Reserved
Bit 14 Reserved
Bit 15 Reserved,
Bit 16 BDGSA/PQGSA(BEIDOU/QZSSDOPandactivesatellites)
Bit 17 BDGSV/PQGSV(BEIDOUQZSSsatellitesinview)
SetthedesiredNMEAsentencebit(s).IfmultipleNMEAsentenceformats
aredesired,"OR"thedesiredbitstogether.
ParameterSavingMode AUTO_SAVE_REBOOT
MaxResponseTime -
Reference Note:
 Reserveddefault 0 ,setinvalid.

14 2 17 AT+CGTP IZATGNSSConfigure.................................................................................
AT+CGTP IZATGNSSConfigure
TestCommand
AT+CGTP=?

Response
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CGTP?

Response
+CGTP:
<feature_control>,<user_session_control>,<primary_svr_address>,<p
rimary_svr_port>,<secondary_svr_address>,<secondary_svr_port>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CGTP=<feature_co
ntrol>

Response
Ifsuccessfully:
OK
Iffailed:
ERROR
Parameters
<feature_control>
0 GTPdisabled
1 GTPenabled
IfyouwanttouseIZATfunction,thisvaluemustbe 1
<user_session_control>
0 ConnectiontotheXTSisneverpermitted
1 ConnectiontotheXTSisalwayspermitted
IfyouwanttouseIZATfunction,thisvaluemustbe 1
<primary_svr_address> theIPaddressoftheprimaryGTPServer.
IfyouwanttouseIZATfunction,thisvaluemustbegtp 1 .izatclout.net
<primary_svr_port> theportnumberoftheprimary
IfyouwanttouseIZATfunction,thisvaluemustbe 443
<secondary_svr_address> the IP address of the secondary GTP
Server.
IfyouwanttouseIZATfunction,thisvaluemustbegtp 2 .izatclout.net
<secondary_svr_port> theportnumberoftheprimary
IfyouwanttouseIZATfunction,thisvaluemustbe 443
<latitude> Latitude(specifiedinWGS 84 datum).
Type:Floatingpoint
Units:Degrees
Range:- 90. 0 to 90. 0
Positivevaluesindicatenorthernlatitude
Negativevaluesindicatesouthernlatitude
<longitude> Longitude(specifiedinWGS 84 datum).
Type:Floatingpoint
Units:Degrees
Range:- 180. 0 to 180. 0
Positivevaluesindicateeasternlongitude
Negativevaluesindicatewesternlongitude
<date> Outputformatisyyyy-mm-dd
<time> UTCtimeoutputformatishh:mm:ss
<accuary> Horizontalpositionuncertainty(circular).
Type:Floatingpoint
Units:Meters
ExecutionCommand
AT+CGTP

Response
OK
+GTPCELL:,,,,
Parameters
SeeWriteCommand
ParameterSavingMode NO_SAVE
MaxResponseTime -

Reference

Note
 Before all IZAT related operations, we should ensure network is
registered.
 IZATflow
Step 1 :ConfigureIZATNVparambyAT+CGTP= 1.
Step 2 :QueryIZATNVparambyAT+CGTP?
Step 3 :StartIZATlocationbyAT+CGTP
 ATcommandexample
//QueryIZATNVset
AT+CGTP?
+CGTP: 1 , 1 ,gtp 1 .izatcloud.net, 443 ,gtp 2 .izatcloud.net, 443
OK
//Ifqueryresultisnotthis,needsetit
AT+CGTP= 1
OK
//StartIZATlocation
AT+CGTP
OK
+GTPCELL:
32. 943878 ,- 117. 214508 , 2019 - 08 - 23 , 17 : 28 : 03 , 1330. 200928
14 2 18 AT+CGNSSUPLCFG GNSSSUPLConfigure..........................................................
AT+CGNSSUPLCFG GNSSSUPLConfigure
TestCommand
AT+CGNSSUPLCFG=?

Response
+CGNSSUPLCFG:"APN","SUPLURL",( 0 - 31 ),( 1 - 4 ),( 0 - 1 )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CGNSSUPLCFG?

Response
+CGNSSUPLCFG:<APN>,<URL>,<SRV>,<PDN>,<SECURITY>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CGNSSUPLCFG=<
APN>,,,,

Response
OK
or
ERROR
Parameters
< APN > APNname
< SUPLURL > Serveraddressurl
< SRV > Servingsystemstype
Bit 0 CDMA
Bit 1 HDR
Bit 2 GSM
Bit 3 WCDMA
Bit 4 LTE
< PDN >
1 IPV 4
2 IPV 6
3 IPV 4 V 6
4 PPP
< SECURITY >
0 Disablessecurity
1 Enablessecurity
ParameterSavingMode AUTO_SAVE_REBOOT
MaxResponseTime -
Reference Note

14 2 19 AT+CGNSSUPL GNSSSUPLControl.......................................................................
AT+CGNSSUPL GNSSSUPLControl
TestCommand
AT+CGNSSUPL=?

Response
+CGNSSUPL:( listofsupported <mode> s )
OK
Parameters
SeeWriteCommand
ReadCommand
AT+CGNSSUPL?

Response
+CGNSSUPL:<mode>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CGNSSUPL=

Response
OK
or
ERROR
Parameters
< mode >
0 TurnoffGNSSSUPL
1 TurnonGNSSSUPL
ParameterSavingMode NO_SAVE
MaxResponseTime -
Reference Note

15 ATCommandsforFileSystem......................................................................................
15 1 Overview..............................................................................................................................................
Command Description
AT+CFSINIT GetFlashDataBuffer
AT+CFSWFILE WriteFiletotheFlashBufferAllocatedbyCFSINIT
AT+CFSRFILE ReadFilefromFlash
AT+CFSDFILE DeletetheFilefromtheFlash

AT+CFSGFIS GetFileSize
AT+CFSREN Renameafile
AT+CFSGFRS Getthesizeoffilesystem
AT+CFSTERM FreetheFlashBufferAllocatedbyCFSINIT

AT+CBAINIT Initializetheapbackupfilesystem
AT+CBALIST Setthefileswhichwanttobackup
AT+CBAPPS StarttobackupapfilesystemallocatedbyCBAINITandCBALIST
AT+CBART Restorethefileintoapfilesystem

15 2 DetailedDescriptionsofCommands...............................................................................................
15 2 1 AT+CFSINIT GetFlashDataBuffer.....................................................................................
AT+CFSINITGetFlashDataBuffer
ExecutionCommand
AT+CFSINIT

Response
OK
or
ERROR
or
+CMEERROR:<err>
Parameters
ParameterSavingMode -

MaxResponseTime -
Reference Note

15 2 2 AT+CFSWFILE WriteFiletotheFlashBufferAllocatedbyCFSINIT.............................
AT+CFSWFILE WriteFiletotheFlashBufferAllocatedbyCFSINIT
TestCommand
AT+CFSWFILE=?

Response
+CFSWFILE:( 0 - 3 ),"fileName",( 0 - 1 ),( 1 - 10240 ),( 100 - 10000 )
OK
Parameters
SeeWriteCommand
WriteCommand
**AT+CFSWFILE=<index

,,,,**

Response
OK
or
ERROR
or
+CMEERROR:
Parameters

DirectoryofAPfilesystem:
0 "/custapp/"
1 "/fota/"
2 "/datatx/"
3 "/customer/"

Filenamelengthshouldlessorequal 50 characters

0 Ifthefilealreadyexisted,writethedataatthebeginningofthe
file.
1 Ifthefilealreadyexisted,addthedataattheendofthefile.

Filesizeshouldbelessthan 10240 bytes.
Millisecond,shouldsendfileduringthisperiodoryoucan’t
sendfilewhentimeout.Thevalueshouldbelessthan 10000 ms.
ParameterSavingMode -
MaxResponseTime -
Reference Note

15 2 3 AT+CFSRFILE ReadFilefromFlash...................................................................................
AT+CFSRFILE ReadFilefromFlash
TestCommand
AT+CFSRFILE=?

Response
+CFSRFILE:( 0 - 3 ),"fileName",( 0 - 1 ),( 1 - 10240 ),( 0 - filesize)
OK
Parameters
SeeWriteCommand
WriteCommand
**AT+CFSRFILE=<index

,<file

name>,,,**

Response
OK
or
ERROR
or
+CMEERROR:
Parameters

DirectoryofAPfilesystem:
0 "/custapp/"
1 "/fota/"
2 "/datatx/"
3 "/customer/"

Filenamelengthshouldbelessthanorequalto 50 characters,

0 Readdataatthebeginningofthefile.
1 Readdataattheofthefile.

Thesizeofthefilethatyouwanttoreadshouldbelessthan 10240.
Thestartingpositionthatwillbereadinthefile.
When= 0 ,isinvalid.Readdatafromthebeginning
totheendofthefile.
When= 1 ,isvalid.Readdatafromtheto
theendofthefile.
ParameterSavingMode -
MaxResponseTime -
Reference Note

15 2 4 AT+CFSDFILE DeletetheFilefromtheFlash...................................................................
AT+CFSDFILE DeletetheFilefromtheFlash
TestCommand
AT+CFSDFILE=?

Response
+CFSDFILE:( 0 - 3 ),"fileName"
OK
Parameters
SeeWriteCommand
WriteCommand
**AT+CFSDFILE=<index

,**

Response
OK
or
ERROR
or
+CMEERROR:
Parameters

DirectoryofAPfilesystem:
0 "/custapp/"
1 "/fota/"
2 "/datatx/"
3 "/customer/"

Filenamelengthshouldbelessthanorequalto 50 characters.
ParameterSavingMode -
MaxResponseTime -
Reference Note

15 2 5 AT+CFSGFIS GetFileSize...................................................................................................
AT+CFSGFIS GetFileSize
TestCommand
AT+CFSGFIS=?

Response
+CFSGFIS:( 0 - 3 ),"fileName"
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CFSGFIS=,

Response
ERROR
or
+CMEERROR:<err>
or
+CFSGFIS:<n>
OK
Parameters

Filenamelengthshouldbelessthanorequalto 50 characters.
Filesize

DirectoryofAPfilesystem:
0 "/custapp/"
1 "/fota/"
2 "/datatx/"
3 "/customer/"
ParameterSavingMode -
MaxResponseTime -
Reference Note

15 2 6 AT+CFSREN RenameaFile.................................................................................................
AT+CFSREN RenameaFile
TestCommand
AT+CFSREN=?

Response
+CFSREN:( 0 - 3 ),"old_name","new_name"
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CFSREN=,
,

Response
OK
or
ERROR
or
+CMEERROR:<err>
Parameters
<index>
DirectoryofAPfilesystem:
0 "/custapp/"
1 "/fota/"
2 "/datatx/"
3 "/customer/"
<oldfilename>
Filenamelengthshouldbelessthanorequalto 50 characters.
<newfile name>
Filenamelengthshouldbelessthanorequalto 50 characters.
ParameterSavingMode -
MaxResponseTime -
Reference Note

15 2 7 AT+CFSGFRS GettheSizeofFileSystem........................................................................
AT+CFSGFRS GettheSizeoffilesystem
ReadCommand
AT+CFSGFRS?

Response
ERROR
or
+CMEERROR:<err>
or
+CFSGFRS:<n>
OK
Parameters
thesizeoffilesystem
ParameterSavingMode -
MaxResponseTime -
Reference Note

15 2 8 AT+CFSTERM FreetheFlashBufferAllocatedbyCFSINIT...........................................
AT+CFSTERM FreetheFlashBufferAllocatedbyCFSINIT
ExecutionCommand
AT+CFSTERM

Response
OK
or
ERROR
or
+CMEERROR:<err>
Parameters
ParameterSavingMode -
MaxResponseTime -
Reference Note

15 2 9 AT+CBAINIT InitializetheAPBackupFileSystem............................................................
AT+CBAINIT InitializetheAPBackupFileSystem
ExecutionCommand
AT+CBAINIT

Response
OK
or
ERROR
or
+CMEERROR:
ParameterSavingMode -

MaxResponseTime 3 seconds
Reference Note

15 2 10 AT+CBALIST SetthefilesWhichWanttoBackup....................................................
AT+CBALIST SettheFilesWhichWanttoBackup
ReadCommand
AT+CBALIST?

Response
+CBALIST:<index>,<filename>
OK
Parameters
SeeWriteCommand
WriteCommand
AT+CBALIST=,

Response
OK
IferrorisrelatedtoMEfunctionality:
+CMEERROR:
Parameters
0 - 9 Thefileindex.
10 Disablelog
11 Enablelog
Filenamelengthshouldlessthanorequalto 80 characters.
ParameterSavingMode NO_SAVE
MaxResponseTime
Reference Note

15 2 11 AT+CBAPPS StarttoBackupAPFileSystemAllocatedbyCBAINITandCBALIST
AT+CBAPPS StarttoBackupAPFileSystemAllocatedbyCBAINITandCBALIST
ExecutionCommand
AT+CBAPPS

Response
OK
or
ERROR
or
+CMEERROR:
ParameterSavingMode -
MaxResponseTime 3 seconds
Reference Note

15 2 12 AT+CBART RestoretheFileintoAPFileSystem......................................................
AT+CBART RestoretheFileintoAPFileSystem
ExecutionCommand
AT+CBART

Response
OK
or
ERROR
or
+CMEERROR:<err>
Parameters
ParameterSavingMode -

MaxResponseTime 3 seconds
Reference Note
Thefilesshouldhavebeenbackupintoapfilesystem.

16 ATCommandsforSIMApplicationToolkit.................................................................
16 1 Overview..............................................................................................................................................
Command Description
AT+STIN SATindication
AT+STGI GetSATinformation
AT+STGR SATrespond
AT+STK STKswitch

16 2 DetailedDescriptionsofCommands...............................................................................................
16 2 1 AT+STIN SATIndication.........................................................................................................
AT+STIN SATIndication
TestCommand
AT+STIN=?

Response
OK
Parameters
SeeReadCommand
ReadCommand
AT+STIN?

Response
+STIN:<cmd_id>
OK
Ifthecurrentproactivecommandhasbeenchanged:
+STIN:<cmd_id>
Parameters
<cmd_id> Indicatethe typeof proactive commandissued.
21 Displaytext
22 Getinkey
23 Getinput
24 Selectitem
25 Setupmenu
ParameterSavingMode -

MaxResponseTime -
Reference Notificationthatapplicationwillreturntomainmenuautomaticallyifuser
doesn’tdoanyactionin 2 minutes.

16 2 2 AT+STGI GetSATInformation..............................................................................................
AT+STGI GetSATInformation
TestCommand
AT+STGI=?

Response
OK
Parameters
SeeWriteCommand
WriteCommand
AT+STGI=<cmd_id>

Response
If<cmd_id>= 21 :
+STGI: 21 ,<prio>,<clear_mode>,<text_len>,<text>
OK
If <cmd_id> = 22 :
+STGI: 22 ,<rsp_format>,<help>,<text_len>,<text>
OK
If<cmd_id>= 23 :
+STGI: 23 ,<rsp_format>,<max_len>,<min_len>,<help>,<show><text_le
n>,<text>
OK
If<cmd_id>= 24 :
+STGI: 24 ,<help>,<softkey>,<present>,<title_len>,<title><item_num>
+STGI: 24 ,<item_id>,<item_len>,<item_data>
[...]
OK
If<cmd_id>= 25 :
+STGI: 25 ,<help>,<softkey>,<title_len>,<title><item_num>
+STGI: 25 ,<item_id>,<item_len>,<item_data>
[...]
OK
or
ERROR
Parameters
<cmd_id> SeeAT+STIN.
Priorityofdisplaytext.
0 Normalpriority
1 Highpriority
<clear_mode>
0 Clearafteradelay
1 Clearbyuser
<text_len> Lengthoftext
<rsp_format>
0 SMSdefaultalphabet
1 YESorNO
2 Numericalonly
3 UCS 2

0 Helpunavailable
1 Helpavailable
<max_len> Maximumlengthofinput
<min_len> Minimumlengthofinput

0 Hideinputtext
1 Displayinputtext

0 Nosoftkeypreferred
1 Softkeypreferred
Menupresentationformatavailableforselectitem
0 Presentationnotspecified
1 Datavaluepresentation
2 Navigationpresentation
<title_len> Lengthoftitle
<item_num> Numberofitemsinthemenu
<item_id> Identifierofitem
<item_len> Lengthofitem


This is a offline tool, your data stays locally and is not send to any server!
Feedback & Bug Reports