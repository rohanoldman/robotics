from goto import
with_gotofrom stddef import *
import var import pio import
resource
from datetime import datetime
# Peripheral Configuration Code (Do Not Edit)#--- CONFIG_BEGIN---
import cpu import
FileStoreimport timer
import VFP import
Generic

def peripheral_setup () :
# Peripheral Constructors pio.cpu=cpu.CPU ()
pio.storage=FileStore.FileStore ()
pio.timer=timer.Timer ()
pio.server=VFP.VfpServer ()
pio.RGBLED1=Generic.RgbLedCa (pio.GPIO19, pio.GPIO20, pio.GPIO26)pio.storage.begin ()
pio.server.begin (0)
# Install interrupt handlersdef peripheral_loop () :
pio.timer.poll () pio.server.poll ()
#---CONFIG_END---
def variables_setup () :
# Flowchart Variablespass # Flowchart Routines
@with_goto
def chart_SETUP () : return
@with_goto def chart_LOOP () :
pio.RGBLED1.set (True, True, True)sleep((500)*0.001) pio.RGBLED1.set (True, False, False)sleep((500)*0.001) pio.RGBLED1.set (True, True, False) sleep((500)*0.001)
pio.RGBLED1.set (False, True, False)sleep((500)*0.001) pio.RGBLED1.set (False, True, True) sleep((500)*0.001)
pio.RGBLED1.set (False, False, True)sleep((500)*0.001) pio.RGBLED1.set (True, False, True) sleep((500)*0.001)
pio.RGBLED1.set (False, False, False)sleep((500)*0.001) return

# Main functiondef main () :
# Setup
variables_setup () peripheral_setup () chart_SETUP ()
# Infinite loop while True :
peripheral_loop ()
chart_LOOP ()
# Command line execution
if name   == ' main ' :main()
