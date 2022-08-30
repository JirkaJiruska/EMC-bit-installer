from pywinauto.application import Application
from pywinauto import keyboard as kb
import pywinauto
import pyautogui as pag 
import sys, os, time, subprocess, wmi, datetime, keyboard
import pyperclip, getpass, winshell
from shutil import copyfile
import threading


def windows_security_thread(thread_timeout):

    for t in range(thread_timeout): 
      time.sleep(1)
      try:
        w_handle = pywinauto.findwindows.find_windows(title=u'Windows Security', class_name='#32770')[0]
        pwa_app = pywinauto.application.Application().connect(handle=w_handle)
        window = pwa_app.window(handle=w_handle)
        ctrl = window['Button1']
        ctrl.Click()
        print("[info] Attempt {a}/{b}: One Windows security panel was handled successfully!".format(a=t,b=thread_timeout))

      except:
        print("[info] Attempt {a}/{b}: No Windows security panel was handled...".format(a=t,b=thread_timeout))
    

def close_app_err(log):
  try:
    log.close()
  except:
    print("[error] Unable to close logs properly")

  input("Installation has been unsuccessfull. \nSee the logs. \nPress enter to quit...")
  exit()    # exit command cannot be a part of try-exept block!!! otherwise it does not close the program

  

# variables for 'install bit' part
default_delay = 0.1

installation_timeout = 35
license_timeout = 60
win_sec_timeout = 20


home_dir = os.path.dirname(sys.argv[0]) + "/"
installer_path = home_dir + "bit/bitwindows.exe"
key_path = home_dir + "bit/LicenceKey.txt"

# create a log file 
log = open(home_dir + "log.txt","w")
log.write("*************************************\nTHE EMC SYSTEM PREPARATION REPORT\n*************************************\nDATE:{a}\n\n".format(a=datetime.datetime.now()))
log.close()
log = open(home_dir + "log.txt","a")

# load setup window name (it is the window identifier for this script)
setup_txt_file = open(home_dir + "bit/Setup_window_name.txt","r")
setup_window_name = setup_txt_file.read()
print("[info] BIT setup window name: " + setup_window_name)

# variables for 'create shortcuts with arguments' part
#definition of file names
emission_file_name = "Emission.lnk"
immunity_file_name = "Immunity.lnk"
cfg_emission_file_name = "bit/Emission.bitcfg"
cfg_immunity_file_name = "bit/Immunity.bitcfg"

#create full file paths
bit_file_path_src = "C:\\Program Files\\BurnInTest\\bit.exe"
bit_folder_path_src = "C:\\Program Files\\BurnInTest"
user_name = getpass.getuser()
# print("The username is: {u}".format(u = user_name))
desktop_path = "C:\\Users\\" + user_name + "\\Desktop\\"
# home_path = os.getcwd() + "\\BIT\\"       #cd C:\Users\PA50\Documents\Python scripts
emission_path_dest = desktop_path + emission_file_name
immunity_path_dest = desktop_path + immunity_file_name
cfg_emission_path_dst = "C:\\Users\\" + user_name + "\\Documents\\PassMark\\BurnInTest\\Configs\\Emission.bitcfg" 
cfg_immunity_path_dst = "C:\\Users\\" + user_name + "\\Documents\\PassMark\\BurnInTest\\Configs\\Immunity.bitcfg" 


########### check whether BIT is already installed ###############
##################################################################

try:

  if os.path.isdir(bit_folder_path_src):
    print("[info] BIT has already been installed. The '{a}' folder already exists.".format(a=bit_folder_path_src))
    log.write("[info] BIT has already been installed. The '{a}' folder already exists.\n".format(a=bit_folder_path_src))
    input("Installation has been unsuccessfull. See the logs. \nPress enter to quit...")
    exit()

except:
  print("[info] BIT has already been installed. The '{a}' folder already exists.".format(a=bit_folder_path_src))
  log.write("[info] BIT has already been installed. The '{a}' folder already exists.\n".format(a=bit_folder_path_src))
  input("Installation has been unsuccessfull. See the logs. \nPress enter to quit...")
  exit()



##################### install bit ################################
##################################################################



# check if the install setup .exe exists and has a correct name
print("[info] Installer part: " + installer_path)

if not os.path.isfile(installer_path):
  print("[error] No installer found in: {a}. Check the installer name.".format(a=installer_path))
  log.write("[error] No installer found in: {a}. Check the installer name.\n".format(a=installer_path))
  close_app_err(log)

else:
  print("[OK] Installer exists in: {a}.".format(a=installer_path))
  log.write("[OK] Installer exists in: {a}.\n".format(a=installer_path))

# open install setup 
try:
  bit = Application(backend='win32').start(installer_path)
  time.sleep(1)

except:
  print("[error] Unable to open {a}".format(a=installer_path))
  log.write("[error] Unable to open {a}\n".format(a=installer_path))
  input("Installation has been unsuccessfull. See the logs. \nPress enter to quit...")
  exit()

# try:
#   print("[info] Active window title: " + pag.getActiveWindowTitle())
#   time.sleep(1)
# except:
#   print("[info] Active window title: " + pag.getActiveWindowTitle())


try:
  time.sleep(default_delay)
  w_handle = pywinauto.findwindows.find_windows(title=setup_window_name, class_name='TWizardForm')[0]
  time.sleep(default_delay)
  window = bit.window(handle=w_handle)
  
  print("[OK] Setup BIT window identified and handled successfully")
  log.write("[OK] Setup BIT window identified and handled successfully\n")

  

  for i in range(installation_timeout):        
    time.sleep(default_delay)
    if window['TNewRadioButton'].exists():
      ctrl = window['TNewRadioButton'].click()
      break

  while(not window['&Install'].exists()):
    for i in range(installation_timeout):
      time.sleep(default_delay)
      if window['&Next >'].exists():
        ctrl = window['&Next >'].click()
        break


  for i in range(installation_timeout):        
    time.sleep(default_delay)
    if window['&Install'].exists():
      ctrl = window['&Install'].click()
      break

  """
    time.sleep(default_delay)
    ctrl = window['TNewRadioButton'].click()
    time.sleep(default_delay)
    ctrl = window['&Next >'].click()
    time.sleep(default_delay)
    ctrl = window['&Next >'].click()
    time.sleep(default_delay)
    ctrl = window['&Next >'].click()
    time.sleep(default_delay)
    ctrl = window['&Install'].click()
    time.sleep(default_delay)
  """


  time.sleep(default_delay)
  ctrl_installation = window['Installing']
  time.sleep(default_delay)


  for i in range(installation_timeout):
      time.sleep(1)
      if not ctrl_installation.exists():
        break
      print("[info] Waiting for finishing the installation... attempt {a}/{b}".format(a=i, b=installation_timeout))

      if i == installation_timeout-1:
        print("[error] Something went wrong. Installation lasts longer than timeout.")
        log.write("[error] Something went wrong. Installation lasts longer than timeout.\n")
        
        #close_app_err(log)


  ctrl = window[u'TNewCheckListBox'].click()
  time.sleep(default_delay)
  kb.send_keys('{VK_DOWN}')
  kb.send_keys('{VK_SPACE}')

  ctrl = window['&Finish'].click()
  time.sleep(default_delay)

except:

  if not window[setup_window_name].exists():
    print("[error] Window setup identifier might be wrong. Check the '/bit/Setup_window_name.txt' whether the text matches the BIT Setup installation window name.")
    log.write("[error] Window setup identifier might be wrong. Check the '/bit/Setup_window_name.txt' whether the text matches the BIT Setup installation window name.\n")
  
  print("[error] Error has occured during the BIT installation...")
  log.write("[error] Error has occured during the BIT installation...\n")
  input("Installation has been unsuccessfull. See the logs. \nPress enter to quit...")
  exit()


################ create shortcuts with arguments #################
##################################################################

try:
  # copy config files
  copyfile(home_dir + cfg_emission_file_name, cfg_emission_path_dst)
  copyfile(home_dir + cfg_immunity_file_name, cfg_immunity_path_dst)

  if os.path.isfile(cfg_emission_path_dst):
    print("[OK] Emissions config files copied to: {a}".format(a=cfg_emission_path_dst))
    log.write("[OK] Emissions config files copied to: {a}\n".format(a=cfg_emission_path_dst))
  else:
    print("[error] Emissions config files not copied.")
    log.write("[error] Emissions config files not copied.\n")

  if os.path.isfile(cfg_immunity_path_dst):
    print("[OK] Immunity config files copied to: {a}".format(a=cfg_immunity_path_dst))
    log.write("[OK] Immunity config files copied to: {a}\n".format(a=cfg_immunity_path_dst))
  else:
    print("[error] Immunity config files not copied.")
    log.write("[error] Immunity config files not copied.\n")

except:
  print("[error] Error has occured during copying config files.")
  log.write("[error] Error has occured during copying config files.\n")



try:
  # create shorcuts
  with winshell.shortcut(emission_path_dest) as emission:
    emission.path = bit_file_path_src
    emission.description = "Emission setup"
    emission.arguments = ' -r -c "{a}"'.format(a=cfg_emission_path_dst)

  with winshell.shortcut(immunity_path_dest) as immunity:
    immunity.path = bit_file_path_src
    immunity.description = "Immunity setup"
    immunity.arguments = ' -r -c "{a}"'.format(a=cfg_immunity_path_dst)

except:
  print("[error] Error has occured during creating the desktop shortcuts...")
  log.write("[error] Error has occured during creating the desktop shortcuts...\n")


################ activate the licence ############################
##################################################################

try:
  time.sleep(2)
  bit_app = Application(backend='win32').start(bit_file_path_src)
  time.sleep(default_delay)
except: 
  print("[error] Unable to open: {a}".format(a=bit_file_path_src))
  log.write("[error] Unable to open: {a}\n".format(a=bit_file_path_src))

# open bit.exe for the first time after being installed and wait until the license window shows up
for i in range(license_timeout):
  time.sleep(1)
  try:
    w_handle = pywinauto.findwindows.find_windows(title=u'BurnInTest by PassMark Software')[0]
    window = bit_app.window(handle=w_handle)
    time.sleep(1)
    if window['Exit BurnInTest'].exists():
      break

  except:
    print("[info] Waiting for licence window... attempt {a}/{b}".format(a=i, b=license_timeout))
    

if i == license_timeout -1:
    print("[error] License window did not show up")
    log.write("[error] License window did not show up\n")
    input("Installation has been unsuccessfull. See the logs. \nPress enter to quit...")
    exit()

# copy and paste license from LicenseKey.txt
key = open(key_path, 'r')
license = key.read()
print("[info] Licence: \n" + license + "\n")
pyperclip.copy(license)
for i in range(3):
  kb.send_keys('{VK_TAB}')
  time.sleep(default_delay)
kb.send_keys('^v')

# wait for the 'Thanks' pop-up window and click OK
window['Continue'].click()
time.sleep(default_delay)
for j in range(license_timeout):
  time.sleep(1)
  try:
    w_handle = pywinauto.findwindows.find_windows(title=u'Thanks')[0]
    window = bit_app.window(handle=w_handle)
    time.sleep(1)
    if window['OK'].exists():
      break

  except:
    print("[info] Waiting for pop-up window... attempt {a}/{b}".format(a=j, b=license_timeout))

if j == license_timeout -1:
  print("[error] License key is not valid")
  log.write("[error] License key is not valid\n")
  input("Installation has been unsuccessfull. See the logs. \nPress enter to quit...")
  exit()
else:
  print("[OK] License activated")
  log.write("[OK] License activated\n")

window['OK'].click()
time.sleep(default_delay)


print("[OK] BIT was installed successfully!")
log.write("[OK] BIT was installed successfully!\n")

################# change IP addresses ############################
##################################################################

print("\n[info] Setting up the IP addresses...\n")
log.write("\n[info] Setting up the IP addresses...\n")
try:
  nics = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
  print("[info] {a} nics visible".format(a=len(nics)))
  log.write("[info] {a} nics visible\n".format(a=len(nics)))
  for i in range(len(nics)):
    ip=u'192.168.0.' + str(i+2)
    subnetmask=u'255.255.255.0'
    gateway=u'192.168.0.1'

    nic = nics[i]
    nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway]) 
    print('nic{a} changed to static IP={b}\n'.format(a=i, b=ip))
    log.write('nic{a} changed to static IP={b}\n'.format(a=i, b=ip))

except:
  print("[error] Error has occured during IP addresses setting...\n")
  log.write("[error] Error has occured during IP addresses setting...\n")


#################### setup Windows ############################
#################################################################


print("\n[info] Setting up the Windows setup...\n")
log.write("\n[info] Setting up the Windows setup...\n")
try:
  log.close()
  time.sleep(default_delay)
  subprocess.call(home_dir + 'bit\\Windows_setup.bat')
  log = open(home_dir + "log.txt","a")
except:
  print("[error] Error has occured during setting up the Windows setting...\n")
  log.write("[error] Error has occured during setting up the Windows setting...\n")


###################### install drivers ############################
###################################################################


win_sec_thr = threading.Thread(target=windows_security_thread, args=(win_sec_timeout,))
win_sec_thr.start()

print("\n[info] Installing Passmark loopback drivers...")
log.write("\n[info] Installing Passmark loopback drivers...\n")
try:
  log.close()
  time.sleep(default_delay)
  subprocess.call(home_dir + 'bit\\Install_drivers.bat')
  log = open(home_dir + "log.txt","a")
  print("[OK] Passmark drivers installation PASSED")
  log.write("[OK] Passmark drivers installation PASSED\n")
except:
  print("[error] Error has occured during installing the passmark loopback drivers...\n")
  log.write("[error] Error has occured during installing the passmark loopback drivers...\n")

print("\n[OK] Passmark loopback drivers installed.")
log.write("\n[OK] Passmark loopback drivers installed.\n")
win_sec_thr.join()



###################### system reboot ############################
#################################################################
print("[OK] DONE")
log.write("[OK] DONE\n")
log.close()
print("[info] System will reboot in 10 second. To postpone the reboot, hold 'R'\n")
for t in range(10):
  time.sleep(1)
  print("{a}".format(a=(10-t)))
  try:
    if keyboard.is_pressed('r'):
      print("[info] The system restart has been postponed")
      break
  except:
    pass
    
  if t==9:
    print("[info] System is shutting down...")
    subprocess.call("shutdown /r")

input("[OK] Installation has been successfull. \nPress enter to quit...")
