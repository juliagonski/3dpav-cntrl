import time
import threading

d_protocol_inhale={
"300mL_32BPM_1:2":"G1 F4600 Z13 Y39\n",
"400mL_12BPM_1:2":"G1 F2100 Z17 Y51\n",
"400mL_32BPM_1:2":"G1 F6200 Z17 Y51\n",
"500mL_12BPM_1:2":"G1 F2400 Z19 Y57\n",
"750mL_20BPM_1:2":"G1 F5800 Z27 Y81\n",
"900mL_16BPM_1:2":"G1 F5500 Z32 Y96\n",
"1000mL_12BPM_1:2":"G1 F4500 Z35 Y105\n",
}
d_protocol_exhale={
"300mL_32BPM_1:2":"G1 F2300 Z0 Y0\n",
"400mL_12BPM_1:2":"G1 F1050 Z0 Y0\n",
"400mL_32BPM_1:2":"G1 F3100 Z0 Y0\n",
"500mL_12BPM_1:2":"G1 F1200 Z0 Y0\n",
"750mL_20BPM_1:2":"G1 F2900 Z0 Y0\n",
"900mL_16BPM_1:2":"G1 F2750 Z0 Y0\n",
"1000mL_12BPM_1:2":"G1 F2250 Z0 Y0\n",
}

def g_init(self,debug=False):
  print("Initializing 3DPaV protocol....")
  if debug: print(";M502")
  self.printer.write(str.encode('M502\n'))
  if debug: print(";M500")
  self.printer.write(str.encode('M500\n'))
  if debug: print(";G28 Y Z")
  self.printer.write(str.encode('G28 Y Z\n'))
  if debug: print(";M400")
  self.printer.write(str.encode('M400\n'))
  self.printer.write(str.encode('M400\n'))

  #answer2 = self.waitForOk(self.printer)
  time.sleep(0.1) #each command should give an immediate okay, except the second M400
  self.printer.flushInput()
  #self.printer.flushOutput()
  isItOk = self.waitForOk(self.printer)
  #print('answer2:', len(answer2),', answer: ', len(answer))

  #if 'ok' in answer.decode("utf-8", "ignore"):
  if isItOk:
    print("------ Done initializing!")
    print("")

def g_run(self,lookup,debug=False):
  self.isOk = False
  if lookup in d_protocol_inhale.keys():
    compress = d_protocol_inhale[lookup]
    decompress = d_protocol_exhale[lookup]
    if debug: print('compress: ', compress, ', decompress: ', decompress)
    self.printer.write(str.encode(compress)) 
    self.printer.write(str.encode(decompress)) 
    self.printer.write(str.encode('M400\n'))
    self.printer.write(str.encode('M400\n'))
  else: 
    print('ERROR!!!! --------------> No ventilation protocol for this choice of settings!')
    #return ''

  print('g_run, isOk: ', self.isOk)
  isItOk = self.waitForOk(self.printer)
  print('done with thread, setting threadDone and updating self.isOk')
  self.isOk = True
  

def g_stop(self,debug=False):
  print('Stopping on exhale')
  self.printer.write(str.encode(d_protocol_exhale[self.lookup])) 

