import serial
import time

from tkinter import *
from tkinter.ttk import Combobox

from gcode import *

class MyWindow:
  def __init__(self, win):
    self.txtfld=Entry(win, text="Serial port")
    self.txtfld.place(x=150, y=20)
    self.btn=Button(win, text="Connect printer", command=self.connect)
    self.btn.place(x=60, y=20)

    self.btn2=Button(win, text="Initialize", command=self.init)
    self.btn2.place(x=60, y=100)
    
    self.tidal_vol=("300", "400", "500", "750","900", "1000")
    self.lab_tv=Label(win, text='Tidal volume:')
    self.lab_tv.place(x=20, y=150)
    self.tv=Combobox(win, values=self.tidal_vol)
    self.tv.place(x=180, y=150)

    self.resp_rate=("12", "16", "32")
    self.lab_rr=Label(win, text='Respiratory rate:')
    self.lab_rr.place(x=20, y=180)
    self.rr=Combobox(win, values=self.resp_rate)
    self.rr.place(x=180, y=180)

    self.insp_exp=("1")
    self.lab_ie=Label(win, text='Inspiratory/expiratory:')
    self.lab_ie.place(x=20, y=210)
    self.ie=Combobox(win, values=self.insp_exp)
    self.ie.place(x=180, y=210)

    self.btn3=Button(win, text="Run Ventilation", command=self.run)
    self.btn3.place(x=60, y=250)
    self.btn4=Button(win, text="Stop",command=self.stop)
    self.btn4.place(x=180, y=250)

    self.printer = None
    self.lookup = None
    self.started_run = False
    self.ventilating = False

  def init(self):
    g_init(self)

  def run(self):
    self.started_run = True
    sel_tv=self.tv.get()
    sel_rr=self.rr.get()
    sel_ie=self.ie.get()
    print('initialize with tv ', sel_tv, ' and rr ', sel_rr, ' and ie ' , sel_ie)
    self.lookup = tv+"mL_"+rr+"BPM_"+ie+"to2"
    g_run(self)

  def stop(self):
    print('stop')
    g_stop(self)

  def connect(self):
    if self.txtfld.get() == '': path = '/Users/juliagonski/Documents/Columbia/3DprinterAsVentilator/pronsoleWork/Printator/sim'
    else: path = self.txtfld.get()
    baudRate = 115200
    ser_printer = serial.Serial(path, baudRate)
    print("Connecting to printer...")
    time.sleep(2)  # Allow time for response
    buffer_bytes = ser_printer.inWaiting()
    print("Connection response from printer:", ser_printer.read(buffer_bytes))
    print("Asking for done moving okay...")
    ser_printer.write(str.encode('M400\n'))
    #print("immediate Ok response from printer: ", ser_printer.readline())
    time.sleep(0.1)  # Allow time for response
    print("time.sleep response from printer: ", ser_printer.readline())
    self.printer=ser_printer
    print("------ Done connecting!")
    print("")
    

#-------------------------------------------------------------------------
def main():
  window=Tk()
  
  mywin=MyWindow(window) 
  window.title('3DPaV Control')
  window.geometry("800x500+10+10")
  window.mainloop()

#-------------------------------------------------------------------------
if __name__ == "__main__":
  main()
