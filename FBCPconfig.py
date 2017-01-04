#BlockComPi FBCPconfig
import time
import datetime
import os

from PitftGraphicLib import *

def passs(): pass

class Menu:
 def __init__(self,label,labelcolour,sublabel,sublabelcolour,contents,others):
     #Page Control
     self.back = 0 
     self.page = 0
     #Contents
     self.label = label
     self.labelcolour = labelcolour
     self.sublabel = sublabel
     self.sublabelcolour = sublabelcolour
     self.contents = contents
     self.others = others
 
 # Slot Configuration
 def slotconf(self,slot, app):
    if slot == 1:
        make_button(app[0], 25, 95, 27, 205, 5, app[1], app[2], app[3]) 
    if slot == 2:
        make_button(app[0], 25, 132, 27, 205, 5, app[1], app[2], app[3]) 
    if slot == 3:
        make_button(app[0], 25, 170, 27, 205, 5, app[1], app[2], app[3])
    if slot == 4:
        make_button(app[0], 25, 207, 27, 205, 5, app[1], app[2], app[3])
    if slot == 5:
        make_button(app[0], 25, 245, 27, 205, 5, app[1], app[2], app[3])

 def layout(self):
   clearall()
   #Label
   make_label(self.label, 20, 20, 47, self.labelcolour) #'10:30 am'
   make_label(self.sublabel, 20, 55, 32, self.sublabelcolour) #'16/5/2015'

   def exit():
     self.back = 1 
   def nextpage():
     clearall()
     self.page = self.page + 1
     self.load()
     self.back = 0
     self.page = self.page - 1
     clearall()
     self.layout()
     
   counter = 1  
   while counter <= 5: #Maximun no. of slots
     if self.page*5+counter-1 >= len(self.contents): break #Stop at no. of programs
     self.slotconf(counter, self.contents[self.page*5+counter-1])
     counter = counter + 1
   
   make_button("Back", 25, 282, 27, 95, 5, white, 24, exit)
   if counter > 5:
     make_button("More", 135, 282, 27, 95, 5, white, 24, nextpage)
   self.others()

 def load(self):
  while 1:
    self.layout()
    touchdisch()
    if self.back == 1:
        self.back = 0
        break
    

class Keypad():
 def __init__(self,label,labelcolour):
     self.back = 0
     #Contents
     self.label = label
     self.labelcolour = labelcolour
     self.content = ''

 def layout(self):
     clearall()
     make_label(self.label, 20, 20, 47, self.labelcolour) #'10:30 am'
     def passs(): pass
     def input(insert):
       self.content = self.content+insert
       clearall()
       self.layout()
     def de():
      self.content = self.content[:len(self.content)-1]
      clearall()
      self.layout()
     def one(): input('1')
     def two(): input('2')
     def three(): input('3')
     def four(): input('4')
     def five(): input('5')
     def six(): input('6')
     def seven(): input('7')
     def eight(): input('8')
     def nine(): input('9')
     def zero(): input('0')
     def done(): self.back = 1
     def bck():
         self.content = False
         self.back = 1
     make_button(self.content, 40, 70, 40, 131, 5, green, 40, passs)
     make_button('Del', 171, 70, 35, 35, 5, green, 25, de)
     make_button('1', 40, 120, 35, 35, 5, cyan, 40, one)
     make_button('2', 103, 120, 35, 35, 5, cyan, 40, two)
     make_button('3', 166, 120, 35, 35, 5, cyan, 40, three)
     make_button('4', 40, 173, 35, 35, 5, cyan, 40, four)
     make_button('5', 103, 173, 35, 35, 5, cyan, 40, five)
     make_button('6', 166, 173, 35, 35, 5, cyan, 40, six)
     make_button('7', 40, 221, 35, 35, 5, cyan, 40, seven)
     make_button('8', 103, 221, 35, 35, 5, cyan, 40, eight)
     make_button('9', 166, 221, 35, 35, 5, cyan, 40, nine)
     make_button('0', 103, 269, 35, 35, 5, cyan, 40, zero)
     make_button('<-', 40, 269, 35, 35, 5, green, 25, bck)
     make_button('->', 166, 269, 35, 35, 5, green, 25, done)

 def check(self):
  while 1:
    touchdisch()
    if self.back == 1:
        self.back = 0
        break

 def input(self): return self.content

 def getinput(self):
     self.layout()
     self.check()
     return self.input()

##########################################################################################
initdis()

def fbcp(state):
  def run():
    disinitdis()
    os.system("rmmod fb_ili9340")# Change rotation
    os.system("rmmod fbtft_device")# Change rotation
    if state == 1:
          os.system("modprobe fbtft_device name=pitft rotate=90")# Change rotation
          os.system("adafruit-pitft-touch-cal -f -r 90")# Change rotation
    elif state == 2:
          os.system("modprobe fbtft_device name=pitft rotate=180")# Change rotation
          os.system("adafruit-pitft-touch-cal -f -r 180")# Change rotation
    elif state == 3:
          os.system("modprobe fbtft_device name=pitft rotate=270")# Change rotation
          os.system("adafruit-pitft-touch-cal -f -r 270")# Change rotation
    elif state == 4:
          os.system("modprobe fbtft_device name=pitft rotate=0")# Change rotation
          os.system("adafruit-pitft-touch-cal -f -r 0")# Change rotation
    os.system('fbcp')
  return run
fbcpmenu = Menu('FBCP',green,'rotation',yellow,(),passs)
fbcpmenu.contents = (('90 degrees',orange,24,fbcp(1)),('180 degrees',blue,24,fbcp(2)),('270 degrees',green,24,fbcp(3)),('360 degrees',red,24,fbcp(4)))

from Variables import *
def varwrite():
    os.system('echo "currentresolution = '+str(currentresolution)+'" > Variables.py')
    os.system('echo "resolutions = []" >> Variables.py')
    for r in range(len(resolutions)):
        os.system('echo "resolutions.append('+str(resolutions[r])+')" >> Variables.py')
class Resolution:
  def __init__(self):
      self.resolmenu = Menu('Resolution',green,'profiles',yellow,(),self.addremove)
      self.update()

  def reset(self):
        def escape(): confirmation.back = 1
        def ok():
            clearall()
            configfile = '/boot/config.txt'
            os.system('cp '+configfile+' config.txt.bak')
            os.system('sed -i /hdmi_force_hotplug=1/d '+configfile)
            os.system('sed -i /hdmi_group=2/d '+configfile)
            os.system('sed -i /hdmi_mode=87/d '+configfile)
            os.system('sed -i /hdmi_cvt='+str(currentresolution[0])+'\ '+str(currentresolution[1])+'\ 60\ 1\ 0\ 0\ 0\ 0/d '+configfile)
            global currentresolution
            currentresolution = ('Not Set','')
            self.update()
            make_label('Reboot', 20, 50, 55, green)
            make_label('To ', 20, 100, 55, green)
            make_label('Apply', 20, 150, 55, green)
            make_label('Changes', 20, 200, 55, green)
            touchdisch()
            time.sleep(1)
            escape()
        confirmation = Menu('Sure?',green,'',yellow,(('No',yellow,24,escape),('Yes',blue,24,ok)),passs)
        confirmation.load()

  def change(self,resolution):
    def func():
        def escape(): confirmation.back = 1
        def ok():
            clearall()
            configfile = '/boot/config.txt'
            os.system('cp '+configfile+' config.txt.bak')
            os.system('sed -i /hdmi_force_hotplug=1/d '+configfile)
            os.system('sed -i /hdmi_group=2/d '+configfile)
            os.system('sed -i /hdmi_mode=87/d '+configfile)
            if currentresolution != ('Not Set',''):os.system('sed -i /hdmi_cvt='+str(currentresolution[0])+'\ '+str(currentresolution[1])+'\ 60\ 1\ 0\ 0\ 0\ 0/d '+configfile)
            os.system('echo "hdmi_force_hotplug=1" >> '+configfile)
            os.system('echo "hdmi_group=2" >> '+configfile)
            os.system('echo "hdmi_mode=87" >> '+configfile)
            os.system('echo "hdmi_cvt='+str(resolution[0])+' '+str(resolution[1])+' 60 1 0 0 0 0" >> '+configfile)
            global currentresolution
            currentresolution = resolution
            self.update()
            make_label('Reboot', 20, 50, 55, green)
            make_label('To ', 20, 100, 55, green)
            make_label('Apply', 20, 150, 55, green)
            make_label('Changes', 20, 200, 55, green)
            touchdisch()
            time.sleep(1)
            escape()
        confirmation = Menu('Sure?',green,str(resolution[0])+','+str(resolution[1]),yellow,(('No',yellow,24,escape),('Yes',blue,24,ok)),passs)
        confirmation.load()
    return func

  def add(self):
      Length = Keypad('Length',green)
      Breadth = Keypad('Breadth',green)
      L = int(Length.getinput())
      if L != False:
          B = int(Breadth.getinput())
          if B != False:
           def escape(): confirmation.back = 1
           def ok():
               clearall()
               resolutions.append((L,B))
               self.update()
               make_label('Added!', 20, 50, 55, green)
               touchdisch()
               time.sleep(1)
               escape()
           confirmation = Menu('Sure?',green,'',green,(('No',yellow,24,escape),('Yes',blue,24,ok)),passs)
           confirmation.load()

  removeselect = Menu('Remove',yellow,'',yellow,(),passs)
  def remove(self,thing,position):
    def func():
      def escape(): confirmation.back = 1
      def ok():
          clearall()
          resolutions.pop(position)
          self.update()
          make_label('Removed!', 20, 50, 55, green)
          touchdisch()
          time.sleep(1)
          escape()
      confirmation = Menu('Sure?',green,thing,green,(('No',yellow,24,escape),('Yes',blue,24,ok)),passs)
      confirmation.load()
    return func

  moveselect = Menu('Move',orange,'',yellow,(),passs)
  def movepos(self,thing,position):
    def func():
      self.resolpositions = []
      for r in range(len(resolutions)):
          self.resolpositions.append((str(r+1),orange,24,self.move(thing,position,r)))
      self.pos = Menu('New Position',orange,thing,green,self.resolpositions,passs)
      self.pos.load()
    return func
  def move(self,thing,position,newposition):
    def func():
      def escape():
          self.pos.back = 1
          confirmation.back = 1
      def ok():
          clearall()
          resolutions.pop(position)
          resolutions.insert(newposition,thing)
          self.update()
          make_label('Moved!', 20, 50, 55, green)
          touchdisch()
          time.sleep(1)
          escape()
      confirmation = Menu('Sure?',green,thing,green,(('No',yellow,24,escape),('Yes',blue,24,ok)),passs)
      confirmation.load()
    return func

  def update(self):
      self.resolselection = [('Key: Length, Height',yellow,24,passs),('Current:'+str(currentresolution[0])+','+str(currentresolution[1]),yellow,24,passs),('Clear Settings',orange,24,self.reset)]
      for r in range(len(resolutions)):
          self.resolselection.append((str(resolutions[r][0])+','+str(resolutions[r][1]),orange,24,self.change(resolutions[r])))
      self.resolmenu.contents = self.resolselection
      self.resolremoval = []
      for r in range(len(resolutions)):
          self.resolremoval.append((str(resolutions[r][0])+','+str(resolutions[r][1]),orange,24,self.remove(resolutions[r],r)))
      self.removeselect.contents = self.resolremoval
      self.resolmoving = []
      for r in range(len(resolutions)):
          self.resolmoving.append((str(resolutions[r][0])+','+str(resolutions[r][1]),orange,24,self.movepos(resolutions[r],r)))
      self.moveselect.contents = self.resolmoving
      varwrite()

  def addremove(self):
    make_button('+', 200, 22, 25, 25, 0, blue, 40, self.add)
    make_button('-', 200, 58, 25, 25, 0, red, 40, self.removeselect.load)
    make_button('Move',110 ,60, 20, 75, 2, orange, 20, self.moveselect.load)
    
resol = Resolution()
mainmenu = Menu('FBCPconfig',cyan,'Main Menu',green,(),passs)
mainmenu.contents=(('FBCP',yellow,24,fbcpmenu.load),('Resolution Profiles',orange,24,resol.resolmenu.load))
while 1: mainmenu.load()
