from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

schem_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'PCA9685PW', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', 'description':'16-channel 12-bit PWM Fm+ I2C-bus LED controller RGBA TSSOP', 'keywords':'PWM LED driver I2C TSSOP', 'value_str':'PCA9685PW', '_match_pin_regex':False, 'datasheet':'http://www.nxp.com/documents/data_sheet/PCA9685.pdf', 'ref_prefix':'U', 'num_units':1, 'fplist':['TSSOP*4.4x9.7mm*P0.65mm*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'TSSOP-28_8x9.7mm_P0.65mm', 'pins':[
            Pin(num='1',name='A0',func=Pin.types.INPUT,do_erc=True),
            Pin(num='10',name='LED4',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='11',name='LED5',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='12',name='LED6',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='13',name='LED7',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='14',name='VSS',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='15',name='LED8',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='16',name='LED9',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='17',name='LED10',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='18',name='LED11',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='19',name='LED12',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='2',name='A1',func=Pin.types.INPUT,do_erc=True),
            Pin(num='20',name='LED13',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='21',name='LED14',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='22',name='LED15',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='23',name='~OE',func=Pin.types.INPUT,do_erc=True),
            Pin(num='24',name='A5',func=Pin.types.INPUT,do_erc=True),
            Pin(num='25',name='EXTCLK',func=Pin.types.INPUT,do_erc=True),
            Pin(num='26',name='SCL',func=Pin.types.INPUT,do_erc=True),
            Pin(num='27',name='SDA',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='28',name='VDD',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='3',name='A2',func=Pin.types.INPUT,do_erc=True),
            Pin(num='4',name='A3',func=Pin.types.INPUT,do_erc=True),
            Pin(num='5',name='A4',func=Pin.types.INPUT,do_erc=True),
            Pin(num='6',name='LED0',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='7',name='LED1',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='8',name='LED2',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='9',name='LED3',func=Pin.types.OUTPUT,do_erc=True)] }),
        Part(**{ 'name':'C', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', 'description':'Unpolarized capacitor', 'keywords':'cap capacitor', 'value_str':'100n', '_match_pin_regex':False, 'datasheet':'~', 'ref_prefix':'C', 'num_units':1, 'fplist':['C_*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'C_0603_1608Metric', 'pins':[
            Pin(num='1',name='~',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'R', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', 'description':'Resistor', 'keywords':'R res resistor', 'value_str':'100R', '_match_pin_regex':False, 'datasheet':'~', 'ref_prefix':'R', 'num_units':1, 'fplist':['R_*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'R_0603_1608Metric', 'pins':[
            Pin(num='1',name='~',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'ZXGD3001E6', 'dest':TEMPLATE, 'tool':SKIDL, '_aliases':Alias({'ZXGD3002E6', 'ZXGD3004E6', 'ZXGD3003E6'}), 'tool_version':'kicad', 'description':'8A (peak) Gate driver, 40V, 1ns delay, SOT-23-6', 'keywords':'gate driver', 'value_str':'ZXGD3001E6', '_match_pin_regex':False, 'datasheet':'http://www.diodes.com/_files/datasheets/ZXGD3004E6.pdf', 'ref_prefix':'U', 'num_units':1, 'fplist':['SOT?23*'], 'do_erc':True, 'aliases':Alias({'ZXGD3002E6', 'ZXGD3004E6', 'ZXGD3003E6'}), 'pin':None, 'footprint':'SOT-23-6', 'pins':[
            Pin(num='1',name='VCC',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='2',name='IN1',func=Pin.types.INPUT,do_erc=True),
            Pin(num='3',name='GND',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='4',name='SINK',func=Pin.types.OPENCOLL,do_erc=True),
            Pin(num='5',name='IN2',func=Pin.types.INPUT,do_erc=True),
            Pin(num='6',name='SOURCE',func=Pin.types.OPENEMIT,do_erc=True)] }),
        Part(**{ 'name':'Conn_01x01', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', 'description':'Generic connector, single row, 01x01, script generated (kicad-library-utils/schlib/autogen/connector/)', 'keywords':'connector', 'value_str':'Conn_01x01', '_match_pin_regex':False, 'datasheet':'~', 'ref_prefix':'J', 'num_units':1, 'fplist':['Connector*:*_1x??_*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'SolderWire-1.5sqmm_1x01_D1.7mm_OD3mm', 'pins':[
            Pin(num='1',name='Pin_1',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'S5DC-13-F', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad_v6', 'description':'', 'keywords':'', 'value_str':'S5DC-13-F', '_match_pin_regex':False, 'datasheet':'https://lcsc.com/product-detail/Diodes-General-Purpose_Diodes-Incorporated_S5DC-13-F_Diodes-Incorporated-S5DC-13-F_C211427.html', 'ref_prefix':'D', 'num_units':1, 'fplist':[], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'D_SMC', 'pins':[
            Pin(num='1',name='K',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='A',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'AOD508', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad_v6', 'description':'', 'keywords':'', 'value_str':'AOD508', '_match_pin_regex':False, 'datasheet':'https://lcsc.com/product-detail/_Alpha-Omega-Semicon_AOD508_Alpha-Omega-Semicon-AOS-AOD508_C80964.html', 'ref_prefix':'Q', 'num_units':1, 'fplist':[], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'TO-252-3_L6.5-W5.8-P4.58-BR', 'pins':[
            Pin(num='2',name='D',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='1',name='G',func=Pin.types.INPUT,do_erc=True),
            Pin(num='3',name='S',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'74LS04', 'dest':TEMPLATE, 'tool':SKIDL, '_aliases':Alias({'74AHC04', '74AHCT04', '74HCT04', '74HC04'}), 'tool_version':'kicad', 'description':'Hex Inverter', 'keywords':'TTL not inv', 'value_str':'74LS04', '_match_pin_regex':False, 'datasheet':'http://www.ti.com/lit/gpn/sn74LS04', 'ref_prefix':'U', 'num_units':7, 'fplist':['DIP*W7.62mm*', 'SSOP?14*', 'TSSOP?14*'], 'do_erc':True, 'aliases':Alias({'74AHC04', '74AHCT04', '74HCT04', '74HC04'}), 'pin':None, 'footprint':'SOIC-14_3.9x8.7mm_P1.27mm', 'pins':[
            Pin(num='1',name='1A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='2',name='1Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='3',name='2A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='4',name='2Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='5',name='3A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='6',name='3Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='8',name='4Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='9',name='4A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='10',name='5Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='11',name='5A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='12',name='6Y',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='13',name='6A',func=Pin.types.INPUT,do_erc=True),
            Pin(num='14',name='VCC',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='7',name='GND',func=Pin.types.PWRIN,do_erc=True)] }),
        Part(**{ 'name':'LED', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', 'description':'Light emitting diode', 'keywords':'LED diode', 'value_str':'LED', '_match_pin_regex':False, 'datasheet':'~', 'ref_prefix':'D', 'num_units':1, 'fplist':['LED*', 'LED_SMD:*', 'LED_THT:*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'LED_0603_1608Metric', 'pins':[
            Pin(num='1',name='K',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='A',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'ATX-24', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', 'description':'ATX Power supply 24pins', 'keywords':'ATX PSU', 'value_str':'ATX-24', '_match_pin_regex':False, 'datasheet':'https://www.intel.com/content/dam/www/public/us/en/documents/guides/power-supply-design-guide-june.pdf#page=33', 'ref_prefix':'J', 'num_units':1, 'fplist':['*Mini?Fit*2x12*Vertical*', '*Mini?Fit*2x12*Horizontal*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'Molex_Mini-Fit_Jr_5566-24A_2x12_P4.20mm_Vertical', 'pins':[
            Pin(num='1',name='+3.3V',func=Pin.types.PWROUT,do_erc=True),
            Pin(num='10',name='+12V',func=Pin.types.PWROUT,do_erc=True),
            Pin(num='11',name='+12V',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='12',name='+3.3V',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='13',name='+3.3V',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='14',name='-12V',func=Pin.types.PWROUT,do_erc=True),
            Pin(num='15',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='16',name='PS_ON#',func=Pin.types.OPENCOLL,do_erc=True),
            Pin(num='17',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='18',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='19',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='+3.3V',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='20',name='NC',func=Pin.types.NOCONNECT,do_erc=True),
            Pin(num='21',name='+5V',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='22',name='+5V',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='23',name='+5V',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='24',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='3',name='GND',func=Pin.types.PWROUT,do_erc=True),
            Pin(num='4',name='+5V',func=Pin.types.PWROUT,do_erc=True),
            Pin(num='5',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='6',name='+5V',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='7',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='8',name='PWR_OK',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='9',name='+5VSB',func=Pin.types.PWROUT,do_erc=True)] }),
        Part(**{ 'name':'EPS12V', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad_v6', 'description':'', 'keywords':'', 'value_str':'EPS12V', '_match_pin_regex':False, 'datasheet':'https://lcsc.com/product-detail/PCB-Connectors-Headers-Receptacles-Female-Sockets_MOLEX-39281083_C293503.html', 'ref_prefix':'U', 'num_units':1, 'fplist':[], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'Molex_Mini-Fit_Jr_5566-08A_2x04_P4.20mm_Vertical', 'pins':[
            Pin(num='1',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='3',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='4',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='5',name='+12V',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='6',name='+12V',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='7',name='+12V',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='8',name='+12V',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'AP1117-15', 'dest':TEMPLATE, 'tool':SKIDL, '_aliases':Alias({'LD1117S33TR_SOT223', 'AMS1117-5.0', 'AP1117-33', 'AP1117-50', 'AMS1117-1.8', 'LD1117S25TR_SOT223', 'LD1117S12TR_SOT223', 'AMS1117-2.5', 'NCP1117-2.0_SOT223', 'NCP1117-12_SOT223', 'NCP1117-2.85_SOT223', 'NCP1117-1.8_SOT223', 'LD1117S50TR_SOT223', 'NCP1117-1.5_SOT223', 'AMS1117-3.3', 'NCP1117-3.3_SOT223', 'LD1117S18TR_SOT223', 'AP1117-25', 'AMS1117-2.85', 'AP1117-18', 'AMS1117-1.5', 'NCP1117-2.5_SOT223', 'NCP1117-5.0_SOT223'}), 'tool_version':'kicad', 'description':'1A Low drop-out regulator, Fixed Output 5V, SOT-223', 'keywords':'REGULATOR LDO 5V', 'value_str':'AP1117-15', '_match_pin_regex':False, 'datasheet':'http://www.onsemi.com/pub_link/Collateral/NCP1117-D.PDF', 'ref_prefix':'U', 'num_units':1, 'fplist':['SOT?223*TabPin2*'], 'do_erc':True, 'aliases':Alias({'LD1117S33TR_SOT223', 'AMS1117-5.0', 'AP1117-33', 'AP1117-50', 'AMS1117-1.8', 'LD1117S25TR_SOT223', 'LD1117S12TR_SOT223', 'AMS1117-2.5', 'NCP1117-2.0_SOT223', 'NCP1117-12_SOT223', 'NCP1117-2.85_SOT223', 'NCP1117-1.8_SOT223', 'LD1117S50TR_SOT223', 'NCP1117-1.5_SOT223', 'AMS1117-3.3', 'NCP1117-3.3_SOT223', 'LD1117S18TR_SOT223', 'AP1117-25', 'AMS1117-2.85', 'AP1117-18', 'AMS1117-1.5', 'NCP1117-2.5_SOT223', 'NCP1117-5.0_SOT223'}), 'pin':None, 'footprint':'SOT-89-3', 'pins':[
            Pin(num='1',name='GND',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='2',name='VO',func=Pin.types.PWROUT,do_erc=True),
            Pin(num='3',name='VI',func=Pin.types.PWRIN,do_erc=True)] }),
        Part(**{ 'name':'Conn_01x16', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', 'description':'Generic connector, single row, 01x16, script generated (kicad-library-utils/schlib/autogen/connector/)', 'keywords':'connector', 'value_str':'Conn_01x16', '_match_pin_regex':False, 'datasheet':'~', 'ref_prefix':'J', 'num_units':1, 'fplist':['Connector*:*_1x??_*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'PinHeader_1x16_P2.54mm_Vertical', 'pins':[
            Pin(num='1',name='Pin_1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='10',name='Pin_10',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='11',name='Pin_11',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='12',name='Pin_12',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='13',name='Pin_13',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='14',name='Pin_14',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='15',name='Pin_15',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='16',name='Pin_16',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='Pin_2',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='3',name='Pin_3',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='4',name='Pin_4',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='5',name='Pin_5',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='6',name='Pin_6',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='7',name='Pin_7',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='8',name='Pin_8',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='9',name='Pin_9',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'SS8050-G', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad_v6', 'description':'', 'keywords':'', 'value_str':'SS8050-G', '_match_pin_regex':False, 'datasheet':'https://lcsc.com/product-detail/Transistors-NPN-PNP_SS8050-L-120-200_C164886.html', 'ref_prefix':'Q', 'num_units':1, 'fplist':[], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'SOT-23-3', 'pins':[
            Pin(num='1',name='B',func=Pin.types.INPUT,do_erc=True),
            Pin(num='3',name='C',func=Pin.types.INPUT,do_erc=True),
            Pin(num='2',name='E',func=Pin.types.INPUT,do_erc=True)] }),
        Part(**{ 'name':'SW_Push', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', 'description':'Push button switch, generic, two pins', 'keywords':'switch normally-open pushbutton push-button', 'value_str':'SW_Push', '_match_pin_regex':False, 'datasheet':'~', 'ref_prefix':'SW', 'num_units':1, 'fplist':[], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'KEY-SMD_L6.2-W3.6-LS8.0', 'pins':[
            Pin(num='1',name='1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='2',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'Rotary_Encoder_Switch', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', 'description':'Rotary encoder, dual channel, incremental quadrate outputs, with switch', 'keywords':'rotary switch encoder switch push button', 'value_str':'Rotary_Encoder_Switch', '_match_pin_regex':False, 'datasheet':'~', 'ref_prefix':'SW', 'num_units':1, 'fplist':['RotaryEncoder*Switch*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'RotaryEncoder_Bourns_Horizontal_PEC12R-2xxxF-Sxxxx', 'pins':[
            Pin(num='A',name='A',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='B',name='B',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='C',name='C',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='S1',name='S1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='S2',name='S2',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'LM75AD', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad_v6', 'description':'', 'keywords':'', 'value_str':'LM75AD', '_match_pin_regex':False, 'datasheet':'https://lcsc.com/product-detail/Temperature-Sensors_NXP_LM75AD_LM75AD_C7963.html', 'ref_prefix':'U', 'num_units':1, 'fplist':[], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.29x3mm', 'pins':[
            Pin(num='2',name='SCL',func=Pin.types.INPUT,do_erc=True),
            Pin(num='1',name='SDA',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='3',name='OS',func=Pin.types.OPENCOLL,do_erc=True),
            Pin(num='7',name='A0',func=Pin.types.INPUT,do_erc=True),
            Pin(num='6',name='A1',func=Pin.types.INPUT,do_erc=True),
            Pin(num='5',name='A2',func=Pin.types.INPUT,do_erc=True),
            Pin(num='4',name='GND',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='8',name='VCC',func=Pin.types.PWRIN,do_erc=True)] }),
        Part(**{ 'name':'ACS71240LLCBTR-030B3', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad_v6', 'description':'', 'keywords':'', 'value_str':'ACS71240LLCBTR-030B3', '_match_pin_regex':False, 'datasheet':'', 'ref_prefix':'U', 'num_units':1, 'fplist':[], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.29x3mm', 'pins':[
            Pin(num='1',name='IP+',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='2',name='IP+',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='3',name='IP-',func=Pin.types.PWROUT,do_erc=True),
            Pin(num='4',name='IP-',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='5',name='GND',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='6',name='~{FAULT}',func=Pin.types.OPENCOLL,do_erc=True),
            Pin(num='7',name='VIOUT',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='8',name='VCC',func=Pin.types.PWRIN,do_erc=True)] }),
        Part(**{ 'name':'AP358SG-13', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad_v6', 'description':'', 'keywords':'', 'value_str':'AP358SG-13', '_match_pin_regex':False, 'datasheet':'https://lcsc.com/product-detail/General-Purpose-Amplifiers_Diodes-Incorporated_AP358SG-13_Diodes-Incorporated-AP358SG-13_C128760.html', 'ref_prefix':'U', 'num_units':1, 'fplist':[], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.29x3mm', 'pins':[
            Pin(num='1',name='OUTPUT1',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='2',name='IN1-',func=Pin.types.INPUT,do_erc=True),
            Pin(num='3',name='IN1+',func=Pin.types.INPUT,do_erc=True),
            Pin(num='4',name='GND',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='5',name='IN2+',func=Pin.types.INPUT,do_erc=True),
            Pin(num='6',name='IN2-',func=Pin.types.INPUT,do_erc=True),
            Pin(num='7',name='OUTPUT2',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='8',name='VCC',func=Pin.types.PWRIN,do_erc=True)] }),
        Part(**{ 'name':'MCP3201', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', 'description':'2.7V 12-Bit A/D Converter with SPIâ\x84¢ Serial Interface, PDIP-8/SOIC-8/MSOP-8/TSSOP-8', 'keywords':'12-Bit Differential ADC SPI 1ch', 'value_str':'MCP3201', '_match_pin_regex':False, 'datasheet':'http://ww1.microchip.com/downloads/en/DeviceDoc/21290D.pdf', 'ref_prefix':'U', 'num_units':1, 'fplist':['SOIC*3.9x4.9mm*P1.27mm*', 'DIP*W7.62mm*', 'TSSOP*4.4x3mm*P0.65mm*', 'MSOP*3x3mm*P0.65mm*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'SOP-8_3.9x4.9mm_P1.27mm', 'pins':[
            Pin(num='1',name='Vref',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='2',name='IN+',func=Pin.types.INPUT,do_erc=True),
            Pin(num='3',name='IN-',func=Pin.types.INPUT,do_erc=True),
            Pin(num='4',name='Vss',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='5',name='~CS~/SHDN',func=Pin.types.INPUT,do_erc=True),
            Pin(num='6',name='Dout',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='7',name='CLK',func=Pin.types.INPUT,do_erc=True),
            Pin(num='8',name='Vdd',func=Pin.types.PWRIN,do_erc=True)] }),
        Part(**{ 'name':'YTC-TC16S-26', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad_v6', 'description':'', 'keywords':'', 'value_str':'YTC-TC16S-26', '_match_pin_regex':False, 'datasheet':'', 'ref_prefix':'U', 'num_units':1, 'fplist':[], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'USB-C-SMD_YTC-TC16S-26-A', 'pins':[
            Pin(num='A12B1',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='A7',name='DN1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='A6',name='DP1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='A5',name='CC1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='A1B12',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='B7',name='DN2',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='B6',name='DP2',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='B5',name='CC2',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='A8',name='SBU1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='B8',name='SBU2',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='A9B4',name='VBUS',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='A4B9',name='VBUS',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='12',name='12',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='13',name='13',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='14',name='14',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='15',name='15',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'RCLAMP7534P-N', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad_v6', 'description':'', 'keywords':'', 'value_str':'RCLAMP7534P-N', '_match_pin_regex':False, 'datasheet':'https://lcsc.com/product-detail/Others_Bourne-Semicon-Shenzhen-RClamp7534P-N_C344004.html', 'ref_prefix':'D', 'num_units':1, 'fplist':[], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'DFN2010-5L_L2.0-W1.0-P0.8-BL', 'pins':[
            Pin(num='4',name='4',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='3',name='3',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='1',name='1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='5',name='5',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='GND',func=Pin.types.PWRIN,do_erc=True)] }),
        Part(**{ 'name':'CP2102N-A01-GQFN28', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', 'description':'USB to UART master bridge, QFN-28', 'keywords':'USB UART bridge', 'value_str':'CP2102N-A01-GQFN28', '_match_pin_regex':False, 'datasheet':'https://www.silabs.com/documents/public/data-sheets/cp2102n-datasheet.pdf', 'ref_prefix':'U', 'num_units':1, 'fplist':['QFN*1EP*5x5mm*P0.5mm*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'QFN-28_L5.0-W5.0-P0.50-TL-EP3.3', 'pins':[
            Pin(num='1',name='~DCD',func=Pin.types.INPUT,do_erc=True),
            Pin(num='10',name='NC',func=Pin.types.NOCONNECT,do_erc=True),
            Pin(num='11',name='~SUSPENDb',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='12',name='SUSPEND',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='13',name='CHREN',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='14',name='CHR1',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='15',name='CHR0',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='16',name='~WAKEUP~/GPIO.3',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='17',name='RS485/GPIO.2',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='18',name='~RXT~/GPIO.1',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='19',name='~TXT~/GPIO.0',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='2',name='~RI~/CLK',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='20',name='GPIO.6',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='21',name='GPIO.5',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='22',name='GPIO.4',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='23',name='~CTS',func=Pin.types.INPUT,do_erc=True),
            Pin(num='24',name='~RTS',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='25',name='RXD',func=Pin.types.INPUT,do_erc=True),
            Pin(num='26',name='TXD',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='27',name='~DSR',func=Pin.types.INPUT,do_erc=True),
            Pin(num='28',name='~DTR',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='29',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='3',name='GND',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='4',name='D+',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='5',name='D-',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='6',name='VDD',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='7',name='REGIN',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='8',name='VBUS',func=Pin.types.INPUT,do_erc=True),
            Pin(num='9',name='~RSTb',func=Pin.types.INPUT,do_erc=True)] }),
        Part(**{ 'name':'ESP32-WROOM-32', 'dest':TEMPLATE, 'tool':SKIDL, '_aliases':Alias({'ESP32-WROOM-32D'}), 'tool_version':'kicad', 'description':'RF Module, ESP32-D0WD SoC, Wi-Fi 802.11b/g/n, Bluetooth, BLE, 32-bit, 2.7-3.6V, onboard antenna, SMD', 'keywords':'RF Radio BT ESP ESP32 Espressif onboard PCB antenna', 'value_str':'ESP32-WROOM-32', '_match_pin_regex':False, 'datasheet':'https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf', 'ref_prefix':'U', 'num_units':1, 'fplist':['ESP32?WROOM?32*'], 'do_erc':True, 'aliases':Alias({'ESP32-WROOM-32D'}), 'pin':None, 'footprint':'ESP32-WROOM-32D', 'pins':[
            Pin(num='1',name='GND',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='10',name='IO25',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='11',name='IO26',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='12',name='IO27',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='13',name='IO14',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='14',name='IO12',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='15',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='16',name='IO13',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='17',name='SHD/SD2',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='18',name='SWP/SD3',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='19',name='SCS/CMD',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='2',name='VDD',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='20',name='SCK/CLK',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='21',name='SDO/SD0',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='22',name='SDI/SD1',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='23',name='IO15',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='24',name='IO2',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='25',name='IO0',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='26',name='IO4',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='27',name='IO16',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='28',name='IO17',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='29',name='IO5',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='3',name='EN',func=Pin.types.INPUT,do_erc=True),
            Pin(num='30',name='IO18',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='31',name='IO19',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='32',name='NC',func=Pin.types.NOCONNECT,do_erc=True),
            Pin(num='33',name='IO21',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='34',name='RXD0/IO3',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='35',name='TXD0/IO1',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='36',name='IO22',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='37',name='IO23',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='38',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='39',name='GND',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='4',name='SENSOR_VP',func=Pin.types.INPUT,do_erc=True),
            Pin(num='5',name='SENSOR_VN',func=Pin.types.INPUT,do_erc=True),
            Pin(num='6',name='IO34',func=Pin.types.INPUT,do_erc=True),
            Pin(num='7',name='IO35',func=Pin.types.INPUT,do_erc=True),
            Pin(num='8',name='IO32',func=Pin.types.BIDIR,do_erc=True),
            Pin(num='9',name='IO33',func=Pin.types.BIDIR,do_erc=True)] }),
        Part(**{ 'name':'Conn_01x04_Male', 'dest':TEMPLATE, 'tool':SKIDL, 'tool_version':'kicad', 'description':'Generic connector, single row, 01x04, script generated (kicad-library-utils/schlib/autogen/connector/)', 'keywords':'connector', 'value_str':'Conn_01x04_Male', '_match_pin_regex':False, 'datasheet':'~', 'ref_prefix':'J', 'num_units':1, 'fplist':['Connector*:*_1x??_*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'PinHeader_1x04_P2.54mm_Vertical', 'pins':[
            Pin(num='1',name='Pin_1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='Pin_2',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='3',name='Pin_3',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='4',name='Pin_4',func=Pin.types.PASSIVE,do_erc=True)] })])