### BITPIM
###
### Copyright (C) 2006 Joe Pham <djpham@bitpim.org>
### Copyright (C) 2006 Roger Binns <rogerb@bitpim.org>
###
### This program is free software; you can redistribute it and/or modify
### it under the terms of the BitPim license as detailed in the LICENSE file.
###
### $Id$


# phone carriers
c_vzw='Verizon Wireless'
c_cingular='Cingular'
c_att='AT&T'
c_telus='Telus Mobility'
c_alltel='Alltel'
c_bell='Bell Mobility'
c_sprint='Sprint'
c_pelephone='Pelephone'
c_sti='STI Mobile'
c_other='Other'

# phone brands
b_lg='LG'
b_samsung='Samsung'
b_sanyo='Sanyo'
b_sk='SK'
b_toshiba='Toshiba'
b_other='Other'
b_audiovox='Audiovox'
b_moto='Motorola'

_phonedata= { 'LG-G4015': { 'module': 'com_lgg4015',
                            'carrier': [c_att],
                            'brand': b_lg,
                            },
              'LG-C2000': { 'module': 'com_lgc2000',
                            'carrier': [c_cingular],
                            'brand': b_lg,
                            },
              'LG-VX3200': { 'module': 'com_lgvx3200',
                             'brand': b_lg,
                             },
              'LG-VX4400': { 'module': 'com_lgvx4400',
                             'brand': b_lg,
                             'carrier': [c_vzw],
                             },
              'LG-VX4500': { 'module': 'com_lgvx4500',
                             'brand': b_lg,
                             },
              'LG-VX4600': { 'module': 'com_lgvx4600',
                             'carrier': [c_telus],
                             'brand': b_lg,
                             },
              'LG-VX4650': { 'module': 'com_lgvx4650',
                             'carrier': [c_vzw],
                             'brand': b_lg,
                             },
              'LG-VX5200': { 'module': 'com_lgvx5200',
                             'carrier': [c_vzw],
                             'brand': b_lg,
                             },
              'LG-LX5450': { 'module': 'com_lglx5450',
                             'carrier': [c_alltel],
                             'brand': b_lg,
                             },
              'LG-LX5550': { 'module': 'com_lglx5550',
                             'carrier': [c_alltel],
                             'brand': b_lg,
                             },
              'LG-VX6000': { 'module': 'com_lgvx6000',
                             'brand': b_lg,
                             },
              'LG-VX6100': { 'module': 'com_lgvx6100',
                             'brand': b_lg,
                             },
              'LG-LG6190': { 'module': 'com_lglg6190',
                             'carrier': [c_bell],
                             'brand': b_lg,
                             },
              'LG-LG6200': { 'module': 'com_lglg6200',
                             'carrier': [c_bell],
                             'brand': b_lg,
                             },
              'LG-VX7000': { 'module': 'com_lgvx7000',
                             'brand': b_lg,
                             },
              'LG-VX8000': { 'module': 'com_lgvx8000',
                             'carrier': [c_vzw],
                             'brand': b_lg,
                             },
              'LG-LG8100': { 'module': 'com_lglg8100',
                             'carrier': [c_telus],
                             'brand': b_lg,
                             },
              'LG-VX8100': { 'module': 'com_lgvx8100',
                             'carrier': [c_vzw],
                             'brand': b_lg,
                             },
              'LG-VX8300': { 'module': 'com_lgvx8300',
                             'carrier': [c_vzw],
                             'brand': b_lg,
                             },
              'LG-VX8500': { 'module': 'com_lgvx8500',
                             'carrier': [c_vzw],
                             'brand': b_lg,
                             },
              'LG-VX8600': { 'module': 'com_lgvx8600',
                             'carrier': [c_vzw],
                             'brand': b_lg,
                             },
              'LG-VX9800': { 'module': 'com_lgvx9800',
                             'carrier': [c_vzw],
                             'brand': b_lg,
                             },
              'LG-VI125': { 'module': 'com_lgvi125',
                            'carrier': [c_sprint],
                            'brand': b_lg,
                            },
              'LG-PM225': { 'module': 'com_lgpm225',
                            'carrier': [c_sprint],
                            'brand': b_lg,
                            },
              'LG-PM325': { 'module': 'com_lgpm325',
                            'carrier': [c_sprint],
                            'brand': b_lg,
                            },
              'LG-TM520': { 'module': 'com_lgtm520',
                            'brand': b_lg,
                            },
              'LG-VX10': { 'module': 'com_lgtm520',
                           'brand': b_lg,
                           },
              'MM-5600': { 'module': 'com_sanyo5600',
                           'carrier': [c_sprint],
                           'brand': b_sanyo,
                           },
              'SCP-6600 (Katana)': { 'module': 'com_sanyo6600',
                                     'carrier': [c_sprint],
                                     'brand': b_sanyo,
                                     },
              'MM-7400': { 'module': 'com_sanyo7400',
                           'carrier': [c_sprint],
                           'brand': b_sanyo,
                           },
              'MM-7500': { 'module': 'com_sanyo7500',
                           'carrier': [c_sprint],
                           'brand': b_sanyo,
                           },
              'MM-8300': { 'module': 'com_sanyo8300',
                           'carrier': [c_sprint],
                           'brand': b_sanyo,
                           },
              'PM-8200': { 'module': 'com_sanyo8200',
                           'carrier': [c_sprint],
                           'brand': b_sanyo,
                           },
              'RL-4920': { 'module': 'com_sanyo4920',
                           'carrier': [c_sprint],
                           'brand': b_sanyo,
                           },
              'RL-4930': { 'module': 'com_sanyo4930',
                           'carrier': [c_sprint],
                           'brand': b_sanyo,
                           },
              'SCP-3100': { 'module': 'com_sanyo3100',
                            'carrier': [c_sprint],
                            'brand': b_sanyo,
                            },
              'SCP-4900': { 'module': 'com_sanyo4900',
                            'carrier': [c_sprint],
                            'brand': b_sanyo,
                            },
              'SCP-5300': { 'module': 'com_sanyo5300',
                            'carrier': [c_sprint],
                            'brand': b_sanyo,
                            },
              'SCP-5400': { 'module': 'com_sanyo5400',
                            'carrier': [c_sprint],
                            'brand': b_sanyo,
                            },
              'SCP-5500': { 'module': 'com_sanyo5500',
                            'carrier': [c_sprint],
                            'brand': b_sanyo,
                            },
              'SCP-7200': { 'module': 'com_sanyo7200',
                            'carrier': [c_sprint],
                            'brand': b_sanyo,
                            },
              'SCP-7300': { 'module': 'com_sanyo7300',
                            'carrier': [c_sprint],
                            'brand': b_sanyo,
                            },
              'SCP-8100': { 'module': 'com_sanyo8100',
                            'carrier': [c_sprint],
                            'brand': b_sanyo,
                            },
              'SCP-8100 (Bell)': { 'module': 'com_sanyo8100_bell',
                                   'carrier': [c_bell],
                                   'brand': b_sanyo,
                                   },
              'SCH-A310': { 'module': 'com_samsungscha310',
                            'carrier': [c_vzw],
                            'brand': b_samsung,
                            },
              'SPH-A460': { 'module': 'com_samsungspha460',
                            'brand': b_samsung,
                            },
              'SPH-A620 (VGA1000)': { 'module': 'com_samsungspha620',
                                      'carrier': [c_sprint],
                                      'brand': b_samsung,
                                      },
              'SPH-A660 (VI660)': { 'module': 'com_samsungspha660',
                                    'carrier': [c_sprint],
                                    'brand': b_samsung,
                                    },
              'SPH-A680': { 'module': 'com_samsungspha680',
                            'carrier': [c_sprint],
                            'brand': b_samsung,
                            },
              'SPH-A740': { 'module': 'com_samsungspha740',
                            'carrier': [c_sprint],
                            'brand': b_samsung,
                            },
              'SPH-A840': { 'module': 'com_samsungspha840',
                            'carrier': [c_sprint],
                            'brand': b_samsung,
                            },
              'SPH-A840 (Telus)': { 'module': 'com_samsungspha840_telus',
                                    'brand': b_samsung,
                                    'carrier': [c_telus],
                                    },
              'SPH-N200': { 'module': 'com_samsungsphn200',
                            'carrier': [c_sprint],
                            'brand': b_samsung,
                            },
              'SPH-N400': { 'module': 'com_samsungsphn400',
                            'carrier': [c_sprint],
                            'brand': b_samsung,
                            },
              'SCH-A650': { 'module': 'com_samsungscha650',
                            'brand': b_samsung,
                            'carrier': [c_vzw],
                            },
              'SCH-A670': { 'module': 'com_samsungscha670',
                            'brand': b_samsung,
                            'carrier': [c_vzw],
                            },
              'SCH-A950': { 'module': 'com_samsungscha950',
                            'brand': b_samsung,
                            'carrier': [c_vzw],
                            },
              'SCH-A930': { 'module': 'com_samsungscha930',
                            'brand': b_samsung,
                            'carrier': [c_vzw],
                            },
              'SK6100' : { 'module': 'com_sk6100',
                           'brand': b_sk,
                           'carrier': [c_pelephone],
                           },
              'VM4050' : { 'module': 'com_toshibavm4050',
                           'brand': b_toshiba,
                           'carrier': [c_sprint],
                           },
              'VI-2300': { 'module': 'com_sanyo2300',
                           'carrier': [c_sprint],
                           'brand': b_sanyo,
                           },
              'LG-VI5225': { 'module': 'com_lgvi5225',
                             'carrier': [c_sti],
                             'brand': b_lg,
                             },
              'V710': { 'module': 'com_motov710',
                        'brand': b_moto,
                        'carrier': [c_vzw],
                        },
              'V710m': { 'module': 'com_motov710m',
                         'brand': b_moto,
                         'carrier': [c_vzw],
                         },
              'V3c': { 'module': 'com_motov3c',
                       'brand': b_moto,
                       'carrier': [c_vzw],
                       },
              'V3cm': { 'module': 'com_motov3cm',
                        'brand': b_moto,
                        'carrier': [c_vzw],
                        },
              'E815': { 'module': 'com_motoe815',
                        'brand': b_moto,
                        'carrier': [c_vzw],
                        },
              'E815m': { 'module': 'com_motoe815m',
                         'brand': b_moto,
                         'carrier': [c_vzw],
                         },
              'Other CDMA phone': { 'module': 'com_othercdma',
                                    'carrier': [c_other],
                                    'brand': b_other,
                                    },
              }

if __debug__:
    _phonedata.update( {'Audiovox CDM-8900': { 'module': 'com_audiovoxcdm8900',     # phone is too fragile for normal use
                                               'brand': b_audiovox,
                                               },
                        'SCH-A870': { 'module': 'com_samsungscha870',
                                      'brand': b_samsung,
                                      'carrier': [c_vzw],
                                      },
                        'SPH-A790': { 'module': 'com_samsungspha790',
                                      'brand': b_samsung,
                                      'carrier': [c_sprint],
                                      },
                        })

# update the module path
for k, e in _phonedata.items():
    _phonedata[k]['module']=__name__+'.'+e['module']

phonemodels=_phonedata.keys()
phonemodels.sort()

def module(phone):
    return _phonedata[phone].get('module', None)

def carriers(phone):
    return _phonedata[phone].get('carrier', [c_other])

def manufacturer(phone):
    return _phonedata[phone].get('brand', b_other)

_tmp1={}
_tmp2={}
for x in phonemodels:
    for y in carriers(x):
        _tmp1[y]=True
    _tmp2[manufacturer(x)]=True
phonecarriers=_tmp1.keys()
phonecarriers.sort()
phonemanufacturers=_tmp2.keys()
phonemanufacturers.sort()
del _tmp1, _tmp2

def phoneslist(brand=None, carrier_name=None):
    return [x for x in phonemodels if (brand is None or manufacturer(x)==brand) \
            and (carrier_name is None or carrier_name in carriers(x))]

def carrier2phones(carrier_name):
    # return the list of phone belongs to this carrier
    return [x for x in phonemodels if carrier_name in carriers(x)]

def manufacturer2phones(brand_name):
    # return a list of phone belongs to this brand
    return [x for x in phonemodels if manufacturer(x)==brand_name]

def getallmodulenames():
    return [_phonedata[k]['module'] for k in _phonedata]
