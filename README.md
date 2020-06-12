# 3dpav-cntrl

1. Getting the code:

`git clone -b dev_signals https://github.com/juliagonski/3dpav-cntrl.git`

2. Run the gui: 
`python gui.py`
(optional --debug argument to turn on print statements: `python gui.py --debug`)

3. Buttons:
- `Connect`: pass the address of your printer to the `Serial port` field.
- `Initialize`: set printer to home. 
- `Run`: starts ventilation based on selected TV, RR, and IE.
- `Stops`: adds an extra exhale to ensure we don't stop the ventilation on a compression, and stops the ventilation. 
-- 
