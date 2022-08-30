PassMark USB 2.0 Loopback Plug
Copyright (C) 2003-2011 PassMark Software
All Rights Reserved
http://www.passmark.com

Overview
========
PMUSB.inf, PMUSB.sys and pmusbp.sys are the device driver files 
required for the PassMark USB 2.0 Loopback plug.

Installation
============
See http://www.passmark.com/ftp/USB2LoopbackPlugUsersGuide.pdf

UnInstallation
==============
See http://www.passmark.com/ftp/USB2LoopbackPlugUsersGuide.pdf

Requirements
============
Windows XP, Vista, Windows 7, 2003 Server, 2008 Server, 2008 R2 Server

Only 32-bit Device Drivers should be installed on a 32-bit 
Operating System.

Only 64-bit Device Drivers should be installed on a 64-bit 
Operating System.

80486 200Mhz or faster.
16Meg RAM
USB 1 or USB 2 ports
PassMark USB 2.0 Loopback plug


Version History
===============
Here’s a summary of all the changes that have been made in
each version of the PMUSB device drivers. 

Release V7.0 build 1001 
13/September/2011
- Number of Devices that can be connected to a system increased from 10 to 30.
- Internal name of device changed to avoid conflict with another USB device on
  the market. As such, this version of the driver is only compatible with 
  BurnInTest V7.0 and later.

Release V6.1 build 0001 rev 0002
WIN32 release 28/January/2009
WIN64 release 28/January/2009
- Readme updated to reflect Windows 2008 Server testing and support.

Release V6.1 build 0001
WIN32 release 3/November/2006
WIN64 release 30/October/2006
PMUSB.sys: V2.1.1004.0 (file version)
pmusbp.sys: V2.1.1004.0 (file version)
- A Digital signature has been added to the device driver package. 
  As such, the device drivers can be installed on 64-bit versions
  of Windows Vista. Also, under Windows Vista, the device driver 
  is automatically installed for the 2nd and subsequent USB 2.0 
  Loopback plugs added to a system - like Windows 2000. This is 
  unlike Windows XP/2003 where each device required manual 
  installation via the Windows wizard.

Release V6.1 build 0000
WIN64 release 30/October/2006
- Limited release build for Vista driver signing.

Release V2.1 build 1004  
WIN32 release 19/September/2006
WIN64 release 19/September/2006
PMUSB.sys: V2.1.1004.0
pmusbp.sys: V2.1.1004.0
- Corrected a bug where the usage of the V2.1.1002 device driver over
  many hours with other BurnInTest tests (particularly the disk test)
  could lead to individual BurnInTest tests to stop (particularly a disk 
  test) or BurnInTest may hang on closing the tests. 
- Other minor improvements and corrections have been made, such as:
  - Basic handling of the system control WMI message;
  - Moved some of the request handling functionality to non-paged 
    memory such that it is available all the time (can't be paged out);
  - Improved memory unavailable reporting (in conjunction with BurnInTest 
    5.1.1014 will better report when the device driver fails to allocate 
    memory);
  - Removed a memory leak;
  - Improved parameter checking such as the maximum size of Read/Write 
    packets.

Release V2.1 build 1003
WIN32 release 15/September/2006
PMUSB.sys: V2.1.1003.0
pmusbp.sys: V2.1.1003.0
- Test build - limited release.

Release V2.1 build 1002  
PMUSB.sys: V2.1.1002.0
pmusbp.sys: No change. v2.0.0000.0 (x86) V2.1.1001.0 (x64)
- When the USB host controller detects an error that it is unable to 
  recover from (due to electrically noisy environments), the 
  device driver will now make the Host controller error information 
  available to applications (e.g. BurnInTest V4.1 1026 or above) and 
  will not block the read or write operation.

Release V2.1 build 1001  
WIN64 release 11/February/2005
PMUSB.sys: V2.1.1001.0
pmusbp.sys: V2.1.1001.0
- From SP1 RC1 of Windows 2003 server (3790.1289), device driver 
  ini files must be written specifically for x64 (decorated for 
  NTAMD64). The device driver ini file has been updated to allow 
  the installation of the device driver on this version of 64-bit 
  Windows (and above). The Device driver .sys files have been 
  re-created using the latest DDK development tools (3790.1289).


Release 2.0 build 1001  
WIN32 release 25/November/2004
PMUSB.sys: V2.0.1001.0
- Corrected a bug that caused a system crash with Windows XP
  Service Pack 1a (only).
- Changed the USB2.0 loopback plug device numbering such that logical
  device numbers may be double digits (i.e. greater than 9). Previously, 
  device numbers were allocated PMUSB0, 1, 2 ...9 (i.e. a maximum of 10). 
  However if a large number ports (USB2.0 test plugs), e.g. 10, are used 
  and there are problems with the USB setup on the PC, on unplugging a 
  USB device, the logical device number may not be released (eg. PMUSB0) 
  and on a replug the device would attempt to allocate the next number, 
  e.g. PMUSB10, and fail. The maximum device number is now PMUSB31 (ie. 31, 
  increased from 9). Note: This does not change the maximum number of 
  USB 2.0 Loopback plugs that may be simultaneously connected, which 
  remains 10.
pmusbp.sys: V2.0.0000.0
- No changes

Release 2.0 build 0000  
WIN32 release 28/October/2004
WIN64 release 3/November/2004
Note: From V2.0, two device drivers are included: PMUSB.sys and pmusbp.sys.
PMUSB.sys: V2.0.0.0
pmusbp.sys: V2.0.0.0
- Improved the device driver's Power management and Plug and Play.
  The key improvements are resuming from Hibernation and Sleep 
  states.

Release 1.32 build 0000
WIN64 release 28/Sep/2004
- Minor changes to support the 64-bit version of Windows.

Release 1.31 build 0000  
WIN32 release 10/Aug/2004
- Corrected the device driver to allow up to 10 USB2.0 loopback 
  plugs to be connected to a PC (previously 8).
  
Release 1.30 build 0000  
WIN32 release 25/Aug/2003
- Inital public version.

Documentation
=============
All the documentation is online at:
www.passmark.com


Support
=======
For technical support, questions, suggestions, Mail us at
help@passmark.com
or visit our web page at
http://www.passmark.com


Ordering / Registration
=======================
All the details are in the online documentation
or you can visit our sales information page
http://www.passmark.com/sales

Enjoy..
The PassMark Development team
