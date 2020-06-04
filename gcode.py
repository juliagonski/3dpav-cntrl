d_protocol_inhale={
"400mL_16BPM_1to2":"G1 F2500 Z116 Y100 E14"
}
d_protocol_exhale={
"400mL_16BPM_1to2":"G1 F1250 Z130 Y145 E-14"
}

def g_init(self):
  print("Initializing 3DPaV protocol....")
  self.printer.write(str.encode('M502\n'))
  print(";factory reset")
  self.printer.write(str.encode("G21\n"))
  print(";metric values")
  self.printer.write(str.encode("G90\n"))
  print(";ABSOLUTE positioning")
  self.printer.write(str.encode("M83\n"))
  print(";RELATIVE POSITIONING ONLY FOR E")
  self.printer.write(str.encode("M107\n"))
  print(";start with the fan off")
  self.printer.write(str.encode("M203 Z800 E800\n"))
  print(";Z1 AND Z2 MAX FEEDRATE")
  self.printer.write(str.encode("M201 Z100 E100\n"))
  print(";Z1 AND Z2 MAX ACCEL [110 WORKS AND 130 MAKES IT FAIL]")
  self.printer.write(str.encode("M205 Z000.40 E000.40\n"))
  print(";SET Z1 AND Z2 JERK")
  self.printer.write(str.encode("M92 Z400 E400\n"))
  print(";SET Z1 AND Z2 ESTEPS")
  self.printer.write(str.encode("M302 S0\n"))
  print(";ALLOW EXTRUDER TO COLD EXTRUDE")
  self.printer.write(str.encode("M18 E\n"))
  print(";DISABLE Z2 FOR HOMING")
  self.printer.write(str.encode("M0 CHK NO BUNGEE+ Y BACK\n"))
  print(";NO BUNGEE+ Y BACK")
  self.printer.write(str.encode("G28 Z\n"))
  print(";home z")
  self.printer.write(str.encode("M17 E\n"))
  print(";ENABLE Z2 AGAIN")
  self.printer.write(str.encode("G92 E0\n"))
  print(";define Z2 position as zero")
  self.printer.write(str.encode("G1 F500 Z5\n"))
  print(";ADDING 5 MM TO Z1 TO CORRECT FOR HOMING DRAG")
  self.printer.write(str.encode("G1 F2000 Z130 E-125\n"))
  print(";move z1 and z2 together to decompress position")
  self.printer.write(str.encode("G28 Y\n"))
  print(";home y")
  self.printer.write(str.encode("G1 F2000 Y150\n"))
  print(";move y to decompress position")
  self.printer.write(str.encode("M0 ADD BUNGEE TO CONT.\n"))
  print(";M400")
  self.printer.write(str.encode('M400\n'))
  print("------ Done initializing!")
  print("")

def g_run(self, tv, rr, ie):
  lookup = tv+"mL_"+rr+"BPM_"+ie+"to2"
  compress = d_protocol_inhale[lookup]
  decompress = d_protocol_exhale[lookup]
  print('compress: ', compress, ', decompress: ', decompress)
  


