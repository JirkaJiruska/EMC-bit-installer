echo off

echo "Sleep mode off:" >> log.txt
powercfg -x -standby-timeout-ac 0 >> log.txt

echo "Screen still on:" >> log.txt
powercfg -x -monitor-timeout-ac 0 >> log.txt

echo "Hard disk turn off disable:" >> log.txt
powercfg -x -disk-timeout-ac 0 >> log.txt

echo "Hibernation timeout disabled:" >> log.txt
powercfg -x hibernate-timeout-ac 0 >> log.txt

echo "Enable wake timers" >> log.txt
powercfg /SETACVALUEINDEX SCHEME_CURRENT 238c9fa8-0aad-41ed-83f4-97be242c8f20 bd3b718a-0680-4d9d-8ab2-e1d2b4ac806d 1 >> log.txt

echo "User account controll off:" >> log.txt
reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f >> log.txt

echo "Turn off the firewall" >> log.txt
NetSh Advfirewall set allprofiles state off >> log.txt

echo "Sound scheme: No sound" >> log.txt
reg.exe ADD HKCU\AppEvents\Schemes /ve /t REG_SZ /d ".None" /f >> log.txt

