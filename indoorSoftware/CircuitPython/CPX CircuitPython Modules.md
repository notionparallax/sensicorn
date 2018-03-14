# CPX CircuitPython Modules
## board module
e.g. board.A0
  A0 -- board.A0
  SPEAKER -- board.A0
  A1 -- board.A1
  A2 -- board.A2
  A3 -- board.A3
  A4 -- board.A4
  SCL -- board.A4
  A5 -- board.A5
  SDA -- board.A5
  A6 -- board.A6
  RX -- board.A6
  A7 -- board.A7
  TX -- board.A7
  LIGHT -- board.LIGHT
  A8 -- board.LIGHT
  TEMPERATURE -- board.TEMPERATURE
  A9 -- board.TEMPERATURE
  BUTTON_A -- board.BUTTON_A
  D4 -- board.BUTTON_A
  BUTTON_B -- board.BUTTON_B
  D5 -- board.BUTTON_B
  SLIDE_SWITCH -- board.SLIDE_SWITCH
  D7 -- board.SLIDE_SWITCH
  NEOPIXEL -- board.NEOPIXEL
  D8 -- board.NEOPIXEL
  D13 -- board.D13
  REMOTEIN -- board.REMOTEIN
  IR_RX -- board.REMOTEIN
  REMOTEOUT -- board.REMOTEOUT
  IR_TX -- board.REMOTEOUT
  IR_PROXIMITY -- board.IR_PROXIMITY
  MICROPHONE_CLOCK -- board.MICROPHONE_CLOCK
  MICROPHONE_DATA -- board.MICROPHONE_DATA
  ACCELEROMETER_INTERRUPT -- board.ACCELEROMETER_INTERRUPT
  ACCELEROMETER_SDA -- board.ACCELEROMETER_SDA
  ACCELEROMETER_SCL -- board.ACCELEROMETER_SCL
  SPEAKER_ENABLE -- board.SPEAKER_ENABLE
  SCK -- board.SCK
  MOSI -- board.MOSI
  MISO -- board.MISO
  FLASH_CS -- board.FLASH_CS

## analogio
  AnalogIn -- <class 'AnalogIn'>
  AnalogOut -- <class 'AnalogOut'>

## digitalio
DigitalInOut -- <class 'DigitalInOut'>
Direction -- <class 'Direction'>
DriveMode -- <class 'DriveMode'>
Pull -- <class 'Pull'>

## busio
  I2C -- <class 'I2C'>
  OneWire -- <class 'OneWire'>
  SPI -- <class 'SPI'>
  UART -- <class 'UART'>

## neopixel
  neopixel_write -- <function>
   digitalio -- <module 'digitalio'>
   NeoPixel -- <class 'NeoPixel'>
   \__name\__ -- neopixel
   math -- <module 'math'>

## audiobusio
PDMIn -- <class 'PDMIn'>

##  audioio
  AudioOut -- <class 'AudioOut'>
## pulseio
  PulseIn -- <class 'PulseIn'>
  PulseOut -- <class 'PulseOut'>
  PWMOut -- <class 'PWMOut'>

## microcontroller
  cpu -- <Processor>
  delay_us -- <function>
  disable_interrupts -- <function>
  enable_interrupts -- <function>
  nvm -- <ByteArray>
  Pin -- <class 'Pin'>
  pin -- <module ''>
  Processor -- <class 'Processor'>
  
##  micropython
  const -- <function>
  opt_level -- <function>
  mem_info -- <function>
  qstr_info -- <function>
  stack_use -- <function>
  heap_lock -- <function>
  heap_unlock -- <function>
  kbd_intr -- <function>

## usb_hid
  devices -- (<Device>, <Device>)
  Device -- <class 'Device'>

## storage
  mount -- <function>
  umount -- <function>
  remount -- <function>
  VfsFat -- <class 'VfsFat'>

## gc
  collect -- <function>
  disable -- <function>
  enable -- <function>
  isenabled -- <function>
  mem_free -- <function>
  mem_alloc -- <function>

## builtins
  __build_class__ -- <function>
  __import__ -- <function>
  __repl_print__ -- <function>
  bool -- <class 'bool'>
  bytes -- <class 'bytes'>
  bytearray -- <class 'bytearray'>
  complex -- <class 'complex'>
  dict -- <class 'dict'>
  enumerate -- <class 'enumerate'>
  filter -- <class 'filter'>
  float -- <class 'float'>
  frozenset -- <class 'frozenset'>
  int -- <class 'int'>
  list -- <class 'list'>
  map -- <class 'map'>
  memoryview -- <class 'memoryview'>
  object -- <class 'object'>
  property -- <class 'property'>
  range -- <class 'range'>
  reversed -- <class 'reversed'>
  set -- <class 'set'>
  slice -- <class 'slice'>
  str -- <class 'str'>
  super -- <class 'super'>
  tuple -- <class 'tuple'>
  type -- <class 'type'>
  zip -- <class 'zip'>
  classmethod -- <class 'classmethod'>
  staticmethod -- <class 'staticmethod'>
  Ellipsis -- Ellipsis
  abs -- <function>
  all -- <function>
  any -- <function>
  bin -- <function>
  callable -- <function>
  chr -- <function>
  delattr -- <function>
  dir -- <function>
  divmod -- <function>
  eval -- <function>
  exec -- <function>
  getattr -- <function>
  setattr -- <function>
  globals -- <function>
  hasattr -- <function>
  hash -- <function>
  help -- <function>
  hex -- <function>
  id -- <function>
  input -- <function>
  isinstance -- <function>
  issubclass -- <function>
  iter -- <function>
  len -- <function>
  locals -- <function>
  max -- <function>
  min -- <function>
  next -- <function>
  oct -- <function>
  ord -- <function>
  pow -- <function>
  print -- <function>
  repr -- <function>
  round -- <function>
  sorted -- <function>
  sum -- <function>
  BaseException -- <class 'BaseException'>
  ArithmeticError -- <class 'ArithmeticError'>
  AssertionError -- <class 'AssertionError'>
  AttributeError -- <class 'AttributeError'>
  EOFError -- <class 'EOFError'>
  Exception -- <class 'Exception'>
  GeneratorExit -- <class 'GeneratorExit'>
  ImportError -- <class 'ImportError'>
  IndentationError -- <class 'IndentationError'>
  IndexError -- <class 'IndexError'>
  KeyboardInterrupt -- <class 'KeyboardInterrupt'>
  KeyError -- <class 'KeyError'>
  LookupError -- <class 'LookupError'>
  MemoryError -- <class 'MemoryError'>
  NameError -- <class 'NameError'>
  NotImplementedError -- <class 'NotImplementedError'>
  OSError -- <class 'OSError'>
  OverflowError -- <class 'OverflowError'>
  RuntimeError -- <class 'RuntimeError'>
  StopIteration -- <class 'StopIteration'>
  SyntaxError -- <class 'SyntaxError'>
  SystemExit -- <class 'SystemExit'>
  TypeError -- <class 'TypeError'>
  UnicodeError -- <class 'UnicodeError'>
  ValueError -- <class 'ValueError'>
  ZeroDivisionError -- <class 'ZeroDivisionError'>
  help -- <function>
  input -- <function>
  open -- <function>
