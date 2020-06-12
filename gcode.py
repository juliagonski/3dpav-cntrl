import time

d_protocol_inhale={
"300mL_32BPM":"G1 F4300 Z12 Y35\n",
"400mL_12BPM":"G1 F2500 Z14 Y45\n",
"400mL_32BPM":"G1 F6000 Z14 Y45\n",
"500mL_12BPM":"G1 F2000 Z17 Y49\n",
"750mL_20BPM":"G1 F5000 Z23 Y69\n",
"900mL_16BPM":"G1 F4600 Z30 Y76\n",
"1000mL_12BPM":"G1 F3800 Z33 Y85\n",
}
d_protocol_exhale={
"300mL_32BPM":"G1 F2150 Z0 Y0\n",
"400mL_12BPM":"G1 F1250 Z0 Y0\n",
"400mL_32BPM":"G1 F3000 Z0 Y0\n",
"500mL_12BPM":"G1 F1000 Z0 Y0\n",
"750mL_20BPM":"G1 F2500 Z0 Y0\n",
"900mL_16BPM":"G1 F2300 Z0 Y0\n",
"1000mL_12BPM":"G1 F1900 Z0 Y0\n",
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
  answer = self.waitForOk(self.printer)
  #print('answer2:', len(answer2),', answer: ', len(answer))

  if 'ok' in answer.decode("utf-8", "ignore"):
    print("------ Done initializing!")
    print("")

def g_run(self,lookup,debug=False):
  #self.isOk = False
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
  self.waitForOk(self.printer)
  print('g_run,after waitForOk, isOkL ', self.isOk)
  return ''
  

def g_stop(self,debug=False):
  print('Stopping on exhale')
  self.printer.write(str.encode(d_protocol_exhale[self.lookup])) 
  self.started_run = False

