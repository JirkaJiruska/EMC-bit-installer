echo off

echo "Current directory: %cd%"

set "SystemPath=%SystemRoot%\Sysnative"
echo "Install passmark pcie card driver..." >> log.txt
%SystemPath%\pnputil.exe /add-driver "%cd%\bit\drivers\pcie_card_driver\IGLx.inf" >> log.txt

echo "Install passmark USB 2.0 loopback driver..." >> log.txt
%SystemPath%\pnputil.exe /add-driver "%cd%\bit\drivers\usb2_loopback_driver\PMUSB2.inf" >> log.txt

echo "Install passmark USB 3.0 loopback driver..." >> log.txt
%SystemPath%\pnputil.exe /add-driver "%cd%\bit\drivers\usb3_loopback_driver\cyusb3.inf" >> log.txt

