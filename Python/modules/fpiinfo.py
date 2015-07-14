# This module is an interface for obtaining site and instrument information
# for all of our FPIs (and potentially others' as well)
#
# When information needs to be added or updated, the "_sites",
# "_dates", and "_instruments" global variables defined below should be changed. Also, the function
# "get_instr_info" may need to be changed if a parameter of an instrument
# depends on the date (e.g., minime06's ccd changed on 2/16/2012)
#
# All users should access this information through the functions in this module.

import datetime


# Define the start and stop dates of the instruments at each site.
# (Dates are inclusive, meaning that the instrument is at the site
#  on both its start and stop dates)
# HISTORY:
#   19 Jul 2013 bjh: Initialized dates by looking at data on remote2.
#   07 Aug 2013 bjh: Moved look direction information from obsfiles to here.

_dates = {}

_dates['minime01'] = {}
_dates['minime01']['uao'] = { 'start': datetime.datetime(2007, 8,27),
                              'stop' : datetime.datetime(2008,10,31), }
_dates['minime01']['car'] = { 'start': datetime.datetime(2009, 7,27),
                              'stop' : None, }

_dates['minime02'] = {}
_dates['minime02']['uao'] = { 'start': datetime.datetime(2007,10,24),
                              'stop' : datetime.datetime(2008, 5,11), }
_dates['minime02']['caj'] = { 'start': datetime.datetime(2009, 9,21),
                              'stop' : None, }

_dates['minime03'] = {}
_dates['minime03']['mor'] = { 'start': datetime.datetime(2013,11, 7),
                              'stop' : None,}

# TODO: Fix me whenever we actually get data from kaf
_dates['minime04'] = {}
_dates['minime04']['kaf'] = { 'start': datetime.datetime(2012, 4, 5), # total guess
                              'stop' : None }

_dates['minime05'] = {}
_dates['minime05']['uao'] = { 'start': datetime.datetime(2012, 7, 3),
                              'stop' : None }

_dates['minime06'] = {}
_dates['minime06']['par'] = { 'start': datetime.datetime(2011, 6,21),
                              'stop' : None, }

_dates['minime07'] = {}
_dates['minime07']['eku'] = { 'start': datetime.datetime(2012, 7,11),
                              'stop' : None, }

_dates['minime08'] = {}
_dates['minime08']['ann'] = { 'start': datetime.datetime(2012, 6,20),
                              'stop' : None, }

# TODO: Fix me
_dates['minime09'] = {}
_dates['minime09']['par'] = { 'start': datetime.datetime(2013, 7,22), 
                              'stop' : datetime.datetime(2013, 7,31)}
_dates['minime09']['vti'] = { 'start': datetime.datetime(2013, 8, 2),
                              'stop' : None, }


# The minime9* instruments have "always" been at their sites. (TODO)
_dates['minime90'] = {}
_dates['minime90']['mrh'] = { 'start': datetime.datetime(2000, 1, 1),
                              'stop' : None, }

_dates['minime91'] = {}
_dates['minime91']['nzk'] = { 'start': datetime.datetime(2000, 1, 1),
                              'stop' : None, }

_dates['minime92'] = {}
_dates['minime92']['a3o'] = { 'start': datetime.datetime(2000, 1, 1),
                              'stop' : None, }

_dates['noto01'] = {}
_dates['noto01']['mh'] = { 'start': datetime.datetime(1900,1,1), # TODO, if it matters
                            'stop' : None, }

_dates['noto02'] = {}
_dates['noto02']['ao'] = { 'start': datetime.datetime(1900,1,1), # TODO, if it matters
                            'stop' : None, }



# Define network information
_networks = {}

_networks['nation'] = {
        'sql_id':           26, # ID on the airglow SQL database
        'quicklook_gif_id': 104, # ID of gif summary image of windfield
        'estimate_vertical_wind': True, # whether to estimate vertical wind for wind field map
        }
        
_networks['renoir'] = {
        'sql_id':           27, # ID on the airglow SQL database
        'quicklook_gif_id': 105, # ID of gif summary image of windfield
        'estimate_vertical_wind': False, # whether to estimate vertical wind for wind field map
        }
        
_networks['peru'] = {
        'sql_id':           28, # ID on the airglow SQL database
        'quicklook_gif_id': 106, # ID of gif summary image of windfield
        'estimate_vertical_wind': False, # whether to estimate vertical wind for wind field map
        }
        





# Define the site information
# HISTORY:
#   19 Jul 2013 bjh - Initialized by using info in Tom's code and FPIprocess.py

_sites = {}

_sites['uao'] = {
        'Location':     (40.133, -88.2, 200),
        'Name':         'Urbana Atmospheric Observatory',
        'Abbreviation': 'uao',
        'Timezone':     'US/Central',
        'CloudThresh':  -25.0,
        'BufferTime':   45,
        'scpUser':      'MiniME',
        'scpPort':      19999,
        'Network':      'nation',
        'sql_id':       6, # ID on the airglow SQL database
        'share':        False, # whether or not to save a copy of the npz file in a separate folder
        'borders':      True,
        'Directions':   {
                'Laser': {'ze': 180, 'az': 87, 'exptime': 30, 
		            'n_exp': 0, 'last_exp': None, 'delay': 600}, 
	            'Zenith': {'ze': 0, 'az': 0, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':1500}, 
	            'North': {'ze': 45, 'az': 0, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0}, 
	            'South': {'ze': -45, 'az': 0, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0}, 
	            'East': {'ze': 45, 'az': 90, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0}, 
	            'West': {'ze': -45, 'az': 90, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'CV_ANN_UAO_1': {'ze': 53.34, 'az': 11.08, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'CV_ANN_UAO_2': {'ze': 53.34, 'az': 101.12, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'IN_ANN_UAO': {'ze': 42.07, 'az': 56.1, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'CV_EKU_UAO_1': {'ze': 52.46, 'az': 82.58, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'CV_EKU_UAO_2': {'ze': -52.54, 'az': -7.23, 'exptime': 180,
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'IN_EKU_UAO': {'ze': 42.25, 'az': 127.75, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'IN_PAR_UAO_EKU': {'ze': 57.47, 'az': 138.12, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Windfield01': {'ze': -59.4, 'az': 38.6, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Windfield02': {'ze': -15.2, 'az': 80.7, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Windfield03': {'ze': 58.4, 'az': 91.6, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Along_B': {'ze': -23.6, 'az': -2.6, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'MTM_Search': {'ze': 56.55, 'az': 105.72, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
                },
    }

_sites['ann'] = {
        'Location':     (42.27, -83.75, 300),
        'Name':         'Peach Mountain',
        'Abbreviation': 'ann',
        'Timezone':     'US/Eastern',
        'BufferTime':   45,
        'CloudThresh':  -25.0,
        'scpUser':      'fpi',
        'scpPort':      19996,
        'Network':      'nation',
        'sql_id':       19, # ID on the airglow SQL database
        'share':        False, # whether or not to save a copy of the npz file in a separate folder
        'borders':      True,
        'Directions':   {
                'Laser': {'ze': -180, 'az': 90, 'exptime': 30,
		            'n_exp': 0, 'last_exp': None, 'delay':600},
	            'Zenith': {'ze': 0, 'az': 90, 'exptime': 300, # BJH changed az from 0 to 90, 19 Aug 2014
		            'n_exp': 0, 'last_exp': None, 'delay':1500},
	            'North': {'ze': 45, 'az': 0, 'exptime': 300,
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'South': {'ze': -45, 'az': 0, 'exptime': 300,
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'East': {'ze': 45, 'az': 90, 'exptime': 300,
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'West': {'ze': -45, 'az': 90, 'exptime': 300,
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'CV_ANN_UAO_1': {'ze': -53.34, 'az': 104.08, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'CV_ANN_UAO_2': {'ze': -53.34, 'az': 13.97, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'IN_ANN_UAO': {'ze': -43.07, 'az': 59.03, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'CV_ANN_EKU_1': {'ze': 57.98, 'az': 138.65, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'CV_ANN_EKU_2': {'ze': -57.98, 'az': 48.75, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'IN_ANN_EKU': {'ze': -47.86, 'az': 3.70, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Windfield10': {'ze': -45.1, 'az': -7.2, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Windfield11': {'ze': -10.9, 'az': 48.4, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Windfield12': {'ze': -54.5, 'az': 137.0, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Along_B': {'ze': -22.1, 'az': -6.3, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'MTM_Search': {'ze': -27.77, 'az': -21.47, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
                },
    }

_sites['eku'] = {
        'Location':     (37.75, -84.29, 300),
        'Name':         'Eastern Kentucky University',
        'Abbreviation': 'eku',
        'Timezone':     'US/Eastern',
        'BufferTime':   45,
        'CloudThresh':  -25.0,
        'scpUser':      'meriwej',
        'scpPort':      19998,
        'Network':      'nation',
        'sql_id':       20, # ID on the airglow SQL database
        'share':        False, # whether or not to save a copy of the npz file in a separate folder
        'borders':      True,
        'Directions':   {
                'Laser': {'ze': 180, 'az': 104, 'exptime': 30, 
		            'n_exp': 0, 'last_exp': None, 'delay':600,}, 
	            'Zenith': {'ze': 0, 'az': 0, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':1500,}, 
	            'North': {'ze': 45, 'az': 0, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'South': {'ze': -45, 'az': 0, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'East': {'ze': 45, 'az': 90, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'West': {'ze': -45, 'az': 90, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'CV_EKU_UAO_1': {'ze': 52.61, 'az': -4.93, 'exptime': 300,
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'CV_EKU_UAO_2': {'ze': -52.54, 'az': 85.12, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0, },
	            'IN_EKU_UAO': {'ze': -42.26, 'az': 130.17, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'IN_PAR_UAO_EKU': {'ze': 0, 'az': 0, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'CV_EKU_PAR_1': {'ze': 42.72, 'az': 110.08, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'CV_EKU_PAR_2': {'ze': -42.73, 'az': 19.98, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'IN_EKU_PAR': {'ze': 32.91, 'az': 155.04, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'CV_ANN_EKU_1': {'ze': 57.98, 'az': 48.51, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'CV_ANN_EKU_2': {'ze': -57.98, 'az': 138.41, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'IN_ANN_EKU': {'ze': 47.86, 'az': 3.45, 'exptime': 300, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_EKU_VTI_1': {'ze': 46.24, 'az': 53.86, 'exptime': 300,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_EKU_VTI_2': {'ze': 46.25, 'az': 143.79, 'exptime': 300,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
                'IN_EKU_VTI': {'ze': 36.14, 'az': 98.82, 'exptime': 300,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_VTI_EKU_PAR': {'ze': 38.38, 'az': 120.72, 'exptime': 300,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'Windfield07': {'ze': -59.2, 'az': 39.5, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Windfield08': {'ze': -16.4, 'az': 120.5, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Windfield09': {'ze': 46.5, 'az': 15.8, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Along_B': {'ze': -26.1, 'az': -5.1, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'MTM_Search': {'ze': -65.26, 'az': -0.11, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
                },
    }

_sites['par'] = {
        'Location':     (35.2, -82.85, 900),
        'Name':         'Pisgah Astronomical Research Institute',
        'Abbreviation': 'par',
        'Timezone':     'US/Eastern',
        'BufferTime':   45,
        'CloudThresh':  -25.0,
        'scpUser':      'meriwej',
        'scpPort':      19997,
        'Network':      'nation',
        'sql_id':       17, # ID on the airglow SQL database
        'share':        False, # whether or not to save a copy of the npz file in a separate folder
        'borders':      True,
        'Directions':   {
                'Laser': {'ze': -180, 'az': 88.5, 'exptime': 30, 
	                'n_exp': 0, 'last_exp': None, 'delay':600,}, 
                'Zenith': {'ze': 0, 'az': 0, 'exptime': 180, 
	                'n_exp': 0, 'last_exp': None, 'delay':1500,}, 
                'North': {'ze': 45, 'az': 0, 'exptime': 180, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,}, 
                'North60': {'ze': 60, 'az': 0, 'exptime': 180, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,}, 
                'South': {'ze': -45, 'az': 0, 'exptime': 180, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,}, 
                'South60': {'ze': -60, 'az': 0, 'exptime': 180, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,}, 
                'East': {'ze': 45, 'az': 90, 'exptime': 180, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,}, 
                'East60': {'ze': 60, 'az': 90, 'exptime': 180, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,}, 
                'West': {'ze': -45, 'az': 90, 'exptime': 180, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_EKU_PAR_1': {'ze': 42.73, 'az': 20.96, 'exptime': 180, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_EKU_PAR_2': {'ze': -42.72, 'az': 110.80, 'exptime': 180, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,},
                'IN_EKU_PAR': {'ze': -32.97, 'az': 155.89, 'exptime': 180, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,},
                'IN_PAR_UAO_EKU': {'ze': -57.47, 'az': 141.36, 'exptime': 180, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'CV_PAR_VTI_1': {'ze': 43.10, 'az': 88.73, 'exptime': 300,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
		        'CV_PAR_VTI_2': {'ze': 43.07, 'az': -1.28, 'exptime': 300,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
                'IN_PAR_VTI': {'ze': 33.26, 'az': 43.76, 'exptime': 300,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_VTI_EKU_PAR': {'ze': 38.48, 'az': 10.20, 'exptime': 180,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'Windfield04': {'ze': -37.8, 'az': 18.3, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Windfield05': {'ze': 38.5, 'az': 158.0, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Windfield06': {'ze': -38.7, 'az': 78.4, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Along_B': {'ze': -28.5, 'az': -5.9, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'MTM_Search_1': {'ze':-64.16, 'az': 17.4, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'MTM_Search_2': {'ze': -47.6, 'az': 31.63, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
                },
    }



_sites['kaf'] = { 
        'Location':     (35.05, -106.58, 1641),
        'Name':         'Kirtland Air Force Base',
        'Abbreviation': 'kaf',
        'Timezone':     'US/Mountain',
        'BufferTime':   45,
        'CloudThresh':  -25.0,
        'scpUser':      'meriwej',
        'scpPort':      19997,
        'Network':      'none',
        'sql_id':       21, # ID on the airglow SQL database
        'share':        False, # whether or not to save a copy of the npz file in a separate folder
        'borders':      True,
        'Directions':   {
                'Laser': {'ze': 180, 'az': 0, 'exptime': 30, 
		            'n_exp': 0, 'last_exp': None, 'delay': 600,}, 
	            'Zenith': {'ze': 0, 'az': 0, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':1500,}, 
	            'North': {'ze': 45, 'az': 0, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'South': {'ze': -45, 'az': 0, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'East': {'ze': 45, 'az': 90, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'West': {'ze': -45, 'az': 90, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
                },
    }

_sites['vti'] = {
        'Location':     (37.206, -80.42, 650),
        'Name':         'Virginia Tech',
        'Abbreviation': 'vti',
        'Timezone':     'US/Eastern',
        'BufferTime':   45,
        'CloudThresh':  -25.0,
        'scpUser':      'meriwej',
        'scpPort':      19995,
        'Network':      'nation',
        'sql_id':       22, # ID on the airglow SQL database
        'share':        False, # whether or not to save a copy of the npz file in a separate folder
        'borders':      True,
        'Directions':   {
                'Laser': {'ze': -180, 'az': 82, 'exptime': 30, 
		            'n_exp': 0, 'last_exp': None, 'delay':600,}, 
	            'Zenith': {'ze': 0, 'az': 0, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':1500,}, 
	            'North': {'ze': 45, 'az': 0, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'South': {'ze': -45, 'az': 0, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'East': {'ze': 45, 'az': 90, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'West': {'ze': -45, 'az': 90, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_EKU_VTI_1': {'ze': 46.22, 'az': -33.75, 'exptime': 300,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
		        'CV_EKU_VTI_2': {'ze': 46.23, 'az': -123.91, 'exptime': 300,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
                'IN_EKU_VTI': {'ze': 36.18, 'az': -78.82, 'exptime': 300,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_PAR_VTI_1': {'ze': 43.02, 'az': -179.88, 'exptime': 300,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
		        'CV_PAR_VTI_2': {'ze': 43.06, 'az': -89.81, 'exptime': 300,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
                'IN_PAR_VTI': {'ze': 33.26, 'az': -134.81, 'exptime': 300,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_VTI_EKU_PAR': {'ze': 38.20, 'az': -100.90, 'exptime': 180,
                    'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'Windfield13': {'ze': 16.1, 'az': 69.2, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Windfield14': {'ze': 58.4, 'az': 86.4, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Windfield15': {'ze': -58.9, 'az': 139.2, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
	            'Along_B': {'ze': -26.7, 'az': -7.5, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0},
                },
    }

_sites['mor'] = {
        'Location':     (31.206, -7.866, 2700),
        'Name':         'Morocco Oukaimeden Observatory',
        'Abbreviation': 'mor',
        'Timezone':     'Africa/Casablanca',
        'BufferTime':   45,
        'CloudThresh':  -25.0,
        'scpUser':      'MiniME',
        'scpPort':      19979,
        'Network':      'morocco',
        'sql_id':       24, # ID on the airglow SQL database
        'share':        True, # whether or not to save a copy of the npz file in a separate folder
        'borders':      False,
        'Directions':   {
                'Laser': {'ze': -179, 'az': 212, 'exptime': 30, 
		            'n_exp': 0, 'last_exp': None, 'delay':600,}, 
	            'Zenith': {'ze': 0, 'az': 0, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':1500,}, 
	            'North': {'ze': 45, 'az': 0, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'South': {'ze': 45, 'az': 180, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'East': {'ze': 45, 'az': 90, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'West': {'ze': 45, 'az': -90, 'exptime': 180, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
                },
    }

_sites['car'] = {
        'Location':     (-7.38, -36.52, 460),
        'Name':         'Cariri',
        'Abbreviation': 'car',
        'Timezone':     'America/Recife',
        'BufferTime':   45,
        'CloudThresh':  -25.0,
        'scpUser':      'MiniME',
        'scpPort':      19988,
        'Network':      'renoir',
        'sql_id':       10, # ID on the airglow SQL database
        'share':        False, # whether or not to save a copy of the npz file in a separate folder
        'borders':      True,
        'Directions':   {
                'Laser': {'ze': 178, 'az': -24, 'exptime': 30, 
		            'n_exp': 0, 'last_exp': None, 'delay': 600,}, 
	            'Zenith': {'ze': 0, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':1500,}, 
	            'North': {'ze': 45, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'South': {'ze': -45, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'East': {'ze': -45, 'az': -90, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'West': {'ze': -45, 'az': 90, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'CV_CAJ_CAR_1': {'ze': 34.4, 'az': -30.9, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'CV_CAJ_CAR_2': {'ze': -34.4, 'az': 59.1, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
	            'IN_CAJ_CAR': {'ze': 25.8, 'az': -78.8, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
                },
    }


_sites['caj'] = {
        'Location':     (-6.876, -38.56, 320),
        'Name':         'Cajazeiras',
        'Abbreviation': 'caj',
        'Timezone':     'America/Recife',
        'BufferTime':   45,
        'CloudThresh':  -25.0,
        'scpUser':      'MiniME',
        'scpPort':      19989,
        'Network':      'renoir',
        'sql_id':       11, # ID on the airglow SQL database
        'share':        False, # whether or not to save a copy of the npz file in a separate folder
        'borders':      True,
        'Directions':   {
                'Laser': {'ze': 178, 'az': -102, 'exptime': 30, 
	                'n_exp': 0, 'last_exp': None, 'delay': 600,}, 
                'Zenith': {'ze': 0, 'az': 0, 'exptime': 210, 
	                'n_exp': 0, 'last_exp': None, 'delay':1500,}, 
                'North': {'ze': 45, 'az': 0, 'exptime': 210, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,}, 
                'South': {'ze': -45, 'az': 0, 'exptime': 210, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,}, 
                'East': {'ze': -45, 'az': -90, 'exptime': 210, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,}, 
                'West': {'ze': -45, 'az': 90, 'exptime': 210, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_CAJ_CAR_1': {'ze': 34.4, 'az': 59.1, 'exptime': 210, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_CAJ_CAR_2': {'ze': -34.4, 'az': -30.9, 'exptime': 210, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,},
                'IN_CAJ_CAR': {'ze': -25.8, 'az': -75.8, 'exptime': 210, 
	                'n_exp': 0, 'last_exp': None, 'delay':0,},
                },
    }

# TODO: If we ever end up controlling these peruvian sites, make sure
# this stuff is correct.
_sites['mrh'] = {
        'Location':     (-11.958256, -76.859012, 1090),
        'Name':         'Merihill',
        'Abbreviation': 'mrh',
        'Timezone':     'America/Lima',
        'BufferTime':   45,
        'CloudThresh':  -25.0,
        'scpUser':      None,
        'scpPort':      None,
        'Network':      'peru',
        'sql_id':       14, # ID on the airglow SQL database
        'share':        False, # whether or not to save a copy of the npz file in a separate folder
        'borders':      True,
        'Directions':   {
                'Laser': {'ze': 178, 'az': -102, 'exptime': 30, 
		            'n_exp': 0, 'last_exp': None, 'delay': 600,}, 
	            'Zenith': {'ze': 0, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':1500,}, 
	            'North': {'ze': 45, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'South': {'ze': -45, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'East': {'ze': -45, 'az': -90, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'West': {'ze': -45, 'az': 90, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_MRH_NZK_1': {'ze': 50.2, 'az': 102.6,},
                'IN_MRH_NZK'  : {'ze': 39.9, 'az': 147.7,},
                'CV_MRH_NZK_2': {'ze': 50.2, 'az': 192.7,},
                'Aux1': {'ze':45, 'az':45},
                'Aux2': {'ze':45, 'az':225},
                'Aux3': {'ze':45, 'az':315},
                },
    }

_sites['nzk'] = {
        'Location':     (-14.972699, -74.891393, 590),
        'Name':         'Nazca',
        'Abbreviation': 'nzk',
        'Timezone':     'America/Lima',
        'BufferTime':   45,
        'CloudThresh':  -25.0,
        'scpUser':      None,
        'scpPort':      None,
        'Network':      'peru',
        'sql_id':       15, # ID on the airglow SQL database
        'share':        False, # whether or not to save a copy of the npz file in a separate folder
        'borders':      True,
        'Directions':   {
                'Laser': {'ze': 178, 'az': -102, 'exptime': 30, 
		            'n_exp': 0, 'last_exp': None, 'delay': 600,}, 
	            'Zenith': {'ze': 0, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':1500,}, 
	            'North': {'ze': 45, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'South': {'ze': -45, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'East': {'ze': -45, 'az': -90, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'West': {'ze': -45, 'az': 90, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_MRH_NZK_1': {'ze': 50.2, 'az': 12.3,},
                'IN_MRH_NZK'  : {'ze': 39.9, 'az': 327.2,},
                'CV_MRH_NZK_2': {'ze': 50.2, 'az': 282.2,},
                'CV_NZK_A3O_1': {'ze': 50.5, 'az': 69.8,},
                'IN_NZK_A3O'  : {'ze': 40.2, 'az': 114.9,},
                'CV_NZK_A3O_2': {'ze': 48.2, 'az': 159.6,},
                'Aux1':         {'ze':45.0, 'az':45.0},
                'Aux2':         {'ze':45.0, 'az':225.0},
                },
    }

_sites['a3o'] = {
        'Location':     (-16.465722, -71.493239, 2400),
        'Name':         'Arequipa Automatic Airglow Observatory',
        'Abbreviation': 'a3o',
        'Timezone':     'America/Lima',
        'BufferTime':   45,
        'CloudThresh':  -25.0,
        'scpUser':      None,
        'scpPort':      None,
        'Network':      'peru',
        'sql_id':       23, # ID on the airglow SQL database
        'share':        False, # whether or not to save a copy of the npz file in a separate folder
        'borders':      True,
        'Directions':   {
                'Laser': {'ze': 178, 'az': -102, 'exptime': 30, 
		            'n_exp': 0, 'last_exp': None, 'delay': 600,}, 
	            'Zenith': {'ze': 0, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':1500,}, 
	            'North': {'ze': 45, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'South': {'ze': -45, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'East': {'ze': -45, 'az': -90, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'West': {'ze': -45, 'az': 90, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
                'CV_NZK_A3O_1': {'ze': -52.05, 'az': 159.61,},
                'IN_NZK_A3O'  : {'ze': -41.7, 'az': 113.55,},
                'CV_NZK_A3O_2': {'ze': -50.93, 'az': 68.96,},
                'Aux1': {'ze':45, 'az':45},
                'Aux2': {'ze':45, 'az':135},
                'Aux3': {'ze':45, 'az':225},
                },
    }

_sites['mh'] = {
        'Location':     (42.6190, -71.4913, 0),
        'Name':         'Millstone Hill',
        'Abbreviation': 'mh',
        'Timezone':     'US/Eastern',
        'BufferTime':   None,
        'CloudThresh':  None,
        'scpUser':      None,
        'scpPort':      None,
        'Network':      'mh',
        'sql_id':       None, # ID on the airglow SQL database
        'share':        False, # whether or not to save a copy of the npz file in a separate folder
        'borders':      True,
        'Directions':   {
                'Laser': None, 
	            'Zenith': {'ze': 0, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':1500,}, 
	            'North': {'ze': 45, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'South': {'ze': -45, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'East': {'ze': -45, 'az': -90, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'West': {'ze': -45, 'az': 90, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
                },
    }

_sites['ao'] = {
        'Location':     (18.3442, -66.7528, 0),
        'Name':         'Arecibo Observatory',
        'Abbreviation': 'ao',
        'Timezone':     'America/Puerto_Rico',
        'BufferTime':   None,
        'CloudThresh':  None,
        'scpUser':      None,
        'scpPort':      None,
        'Network':      'ao',
        'sql_id':       None, # ID on the airglow SQL database
        'share':        False, # whether or not to save a copy of the npz file in a separate folder
        'borders':      True,
        'Directions':   {
                'Laser': None, 
	            'Zenith': {'ze': 0, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':1500,}, 
	            'North': {'ze': 45, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'South': {'ze': -45, 'az': 0, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'East': {'ze': -45, 'az': -90, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,}, 
	            'West': {'ze': -45, 'az': 90, 'exptime': 210, 
		            'n_exp': 0, 'last_exp': None, 'delay':0,},
                },
    }


_instruments = {}

_instruments['minime01'] = {
        'name'          : 'minime01',    
        'N'             : 500,          # Number of annuli
        'N0'            : 0,            # First annulus to use
        'N1'            : 500,          # Last annulus to use
        'focal_length'  : 300e-3,       # focal length of lens in m
        'pix_size'      : 13e-6,        # pixel size on CCD in m
        'lam_laser'     : 632.8e-9,     # laser wavelength in m
        'lam0'          : 630.0e-9,     # nominal line center wavelength in m
        'nominal_t'     : 1.5e-2,       # approximate etalon gap in m
        'default_params': {# instrument params to be used if the laser fails (i.e., zenith reference)
                                'R': 0.77,
                            'alpha': 8.7e-5,
                                'I': 1.0,
                                'B': 0.0,
                               'a1': 7.0e-2,
                               'a2': -4.5e-2,
                              'b0': 1.06,
                              'b1': 2.06e-1,
                              'b2': -6.6e-2, 
                           'center':  (251.7, 265.1),
                          },
        'sql_winds_id'          : 56,           # ID for SQL database
        'sql_temperatures_id'   : 57,           # ID for SQL database
        'sql_diagnostics_id'    : 82,           # ID for SQL database
        'many_fringes'          : True,         # indicates whether radial falloff terms should be used
        'bad_wind_dates'        : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'bad_temperature_dates' : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'send_to_madrigal'      : True, # whether or not we should send this instrument's data to Madrigal
    }
            
_instruments['minime02'] = {
        'name'          : 'minime02',    
        'N'             : 500,          # Number of annuli
        'N0'            : 0,            # First annulus to use
        'N1'            : 500,          # Last annulus to use
        'focal_length'  : 300e-3,       # focal length of lens in m
        'pix_size'      : 13e-6,        # pixel size on CCD in m
        'lam_laser'     : 632.8e-9,     # laser wavelength in m
        'lam0'          : 630.0e-9,     # nominal line center wavelength in m
        'nominal_t'     : 1.5e-2,       # approximate etalon gap in m
        'default_params': {# instrument params to be used if the laser fails (i.e., zenith reference)
                                'R': 0.77,
                            'alpha': 8.7e-5,
                                'I': 1.0,
                                'B': 0.0,
                               'a1': 1.7e-1,
                               'a2': -5.7e-2,
                               'b0': 7.6e-1,
                               'b1': 1.0e-1,
                               'b2': -6.4e-2, 
                           'center':  (261.0, 254.6),
                          },
        'sql_winds_id'          : 52,           # ID for SQL database
        'sql_temperatures_id'   : 53,           # ID for SQL database
        'sql_diagnostics_id'    : 83,           # ID for SQL database
        'many_fringes'          : True,         # indicates whether radial falloff terms should be used
        'bad_wind_dates'        : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'bad_temperature_dates' : [(datetime.datetime(2013,5,1), datetime.datetime(2013,9,20),1,)],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'send_to_madrigal'      : True, # whether or not we should send this instrument's data to Madrigal
    }

# TODO: Fill in this instrument's parameters when it ships.            
_instruments['minime03'] = {
        'name'          : 'minime03',
        'N'             : 500,          # Number of annuli
        'N0'            : 50,            # First annulus to use
        'N1'            : 500,          # Last annulus to use
        'focal_length'  : 310e-3,       # focal length of lens in m
        'pix_size'      : 13e-6,        # pixel size on CCD in m
        'lam_laser'     : 632.8e-9,     # laser wavelength in m
        'lam0'          : 630.0e-9,     # nominal line center wavelength in m
        'nominal_t'     : 1.5e-2,       # approximate etalon gap in m        
        'default_params': {# instrument params to be used if the laser fails (i.e., zenith reference)
                                'R': 5.266e-01,
                            'alpha': 8.380e-05,
                                'I': 1.0,
                                'B': 0.0,
                               'a1': 2.809e-01,
                               'a2': -1.472e-01,
                               'b0': -1.197e-01,
                               'b1': -2.140e-01,
                               'b2': 9.668e-01, 
                           'center':  (259.64, 263.79),
                          },
        'sql_winds_id'          : 99,           # ID for SQL database
        'sql_temperatures_id'   : 100,           # ID for SQL database
        'sql_diagnostics_id'    : 84,           # ID for SQL database
        'many_fringes'          : True,         # indicates whether radial falloff terms should be used
        'bad_wind_dates'        : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'bad_temperature_dates' : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'send_to_madrigal'      : False, # whether or not we should send this instrument's data to Madrigal
        'share'                 : False, # whether or not to save a copy of the npz file in a separate folder
    }
            
_instruments['minime04'] = {
        'name'          : 'minime04',
        'N'             : 500,          # Number of annuli
        'N0'            : 0,            # First annulus to use
        'N1'            : 500,          # Last annulus to use
        'focal_length'  : 310e-3,       # focal length of lens in m
        'pix_size'      : 13e-6,        # pixel size on CCD in m
        'lam_laser'     : 632.8e-9,     # laser wavelength in m
        'lam0'          : 630.0e-9,     # nominal line center wavelength in m
        'nominal_t'     : 1.5e-2,       # approximate etalon gap in m
        'default_params': {# instrument params to be used if the laser fails (i.e., zenith reference)
                                'R': 0.74,
                            'alpha': 8.4e-5,
                                'I': 1.0,
                                'B': 0.0,
                               'a1': -3.6e-2,
                               'a2': -1.8e-2,
                               'b0': 1.8,
                               'b1': 9.2e-1,
                               'b2': -4.4e-1, 
                           'center':  (253.1, 255.7),
                          },
        'sql_winds_id'          : 80,           # ID for SQL database
        'sql_temperatures_id'   : 81,           # ID for SQL database
        'sql_diagnostics_id'    : 90,           # ID for SQL database
        'many_fringes'          : True,         # indicates whether radial falloff terms should be used
        'bad_wind_dates'        : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'bad_temperature_dates' : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'send_to_madrigal'      : False, # whether or not we should send this instrument's data to Madrigal
    }

           
_instruments['minime05'] = {
        'name'          : 'minime05',
        'N'             : 500,          # Number of annuli
        'N0'            : 0,            # First annulus to use
        'N1'            : 500,          # Last annulus to use
        'focal_length'  : 300e-3,       # focal length of lens in m
        'pix_size'      : 13e-6,        # pixel size on CCD in m
        'lam_laser'     : 632.8e-9,     # laser wavelength in m
        'lam0'          : 630.0e-9,     # nominal line center wavelength in m
        'nominal_t'     : 1.5e-2,       # approximate etalon gap in m
        'default_params': {# instrument params to be used if the laser fails (i.e., zenith reference)
                                'R': 0.89,
                            'alpha': 8.8e-5,
                                'I': 1.0,
                                'B': 0.0,
                               'a1': -2.6e-3,
                               'a2': -4.4e-2,
                               'b0': 1.1,
                               'b1': 2.0e-1,
                               'b2': -2.0e-1, 
                           'center':  (254.2, 254.6),
                          },
        'sql_winds_id'          : 72,           # ID for SQL database
        'sql_temperatures_id'   : 73,           # ID for SQL database
        'sql_diagnostics_id'    : 87,           # ID for SQL database
        'many_fringes'          : True,         # indicates whether radial falloff terms should be used
        'bad_wind_dates'        : [(datetime.datetime(2012,7,1), datetime.datetime(2013,11,20),1,)],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'bad_temperature_dates' : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'send_to_madrigal'      : True, # whether or not we should send this instrument's data to Madrigal
    }

_instruments['minime06'] = {
        'name'          : 'minime06',
        'N'             : 500,          # Number of annuli
        'N0'            : 0,            # First annulus to use
        'N1'            : 500,          # Last annulus to use
        'focal_length'  : 300e-3,       # focal length of lens in m
        'pix_size'      : 13e-6,        # pixel size on CCD in m
        'lam_laser'     : 632.8e-9,     # laser wavelength in m
        'lam0'          : 630.0e-9,     # nominal line center wavelength in m
        'nominal_t'     : 1.5e-2,       # approximate etalon gap in m
        'default_params': {# instrument params to be used if the laser fails (i.e., zenith reference)
                                'R': 0.77,
                            'alpha': 7.7e-5,
                                'I': 1.0,
                                'B': 0.0,
                               'a1': -8.6e-1,
                               'a2': -4.0e-1,
                               'b0': 1.3,
                               'b1': 2.7e-1,
                               'b2': -3.8e-1, 
                           'center':  (262.4, 259.5),
                          },
        'sql_winds_id'          : 68,           # ID for SQL database
        'sql_temperatures_id'   : 69,           # ID for SQL database
        'sql_diagnostics_id'    : 86,           # ID for SQL database
        'many_fringes'          : True,         # indicates whether radial falloff terms should be used
        'bad_wind_dates'        : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'bad_temperature_dates' : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'send_to_madrigal'      : True, # whether or not we should send this instrument's data to Madrigal
    }
            
_instruments['minime07'] = {
        'name'          : 'minime07',
        'N'             : 500,          # Number of annuli
        'N0'            : 60,           # First annulus to use # mm07 has that weird dip in the center
        'N1'            : 500,          # Last annulus to use
        'focal_length'  : 310e-3,       # focal length of lens in m
        'pix_size'      : 13e-6,        # pixel size on CCD in m
        'lam_laser'     : 632.8e-9,     # laser wavelength in m
        'lam0'          : 630.0e-9,     # nominal line center wavelength in m
        'nominal_t'     : 1.5e-2,       # approximate etalon gap in m
        'default_params': {# instrument params to be used if the laser fails (i.e., zenith reference)
                                'R': 0.59,
                            'alpha': 8.4e-5,
                                'I': 1.0,
                                'B': 0.0,
                               'a1': -1.9e-1,
                               'a2': 5.3e-3,
                               'b0': -6.3e-2,
                               'b1': -5.2e-1,
                               'b2': 3.0e-1, 
                           'center':  (250.0, 255.0),
                          },
        'sql_winds_id'          : 76,           # ID for SQL database
        'sql_temperatures_id'   : 77,           # ID for SQL database
        'sql_diagnostics_id'    : 89,           # ID for SQL database
        'many_fringes'          : True,         # indicates whether radial falloff terms should be used
        'bad_wind_dates'        : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'bad_temperature_dates' : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'send_to_madrigal'      : True, # whether or not we should send this instrument's data to Madrigal
    }
            
_instruments['minime08'] = {
        'name'          : 'minime08',
        'N'             : 500,          # Number of annuli
        'N0'            : 0,            # First annulus to use
        'N1'            : 500,          # Last annulus to use
        'focal_length'  : 310e-3,       # focal length of lens in m
        'pix_size'      : 13e-6,        # pixel size on CCD in m
        'lam_laser'     : 632.8e-9,     # laser wavelength in m
        'lam0'          : 630.0e-9,     # nominal line center wavelength in m
        'nominal_t'     : 1.5e-2,       # approximate etalon gap in m
        'default_params': {# instrument params to be used if the laser fails (i.e., zenith reference)
                                'R': 0.72,
                            'alpha': 8.4e-5,
                                'I': 1.0,
                                'B': 0.0,
                               'a1': -1.1e-1,
                               'a2': 4.0e-3,
                               'b0': 2.5,
                               'b1': 1.2,
                               'b2': -3.2e-1, 
                           'center':  (278.9, 262.9),
                          },
        'sql_winds_id'          : 74,           # ID for SQL database
        'sql_temperatures_id'   : 75,           # ID for SQL database
        'sql_diagnostics_id'    : 88,           # ID for SQL database
        'many_fringes'          : True,         # indicates whether radial falloff terms should be used
        'bad_wind_dates'        : [(datetime.datetime(2015,6,26), datetime.datetime(2015,7,14),2,)],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'bad_temperature_dates' : [(datetime.datetime(2015,6,26), datetime.datetime(2015,7,14),2,)],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'send_to_madrigal'      : True, # whether or not we should send this instrument's data to Madrigal
    }

         
_instruments['minime09'] = {
        'name'          : 'minime09',
        'N'             : 500,          # Number of annuli
        'N0'            : 0,            # First annulus to use
        'N1'            : 500,          # Last annulus to use
        'focal_length'  : 300e-3,       # focal length of lens in m
        'pix_size'      : 13e-6,        # pixel size on CCD in m
        'lam_laser'     : 632.8e-9,     # laser wavelength in m
        'lam0'          : 630.0e-9,     # nominal line center wavelength in m
        'nominal_t'     : 1.5e-2,       # approximate etalon gap in m
        'default_params': {# instrument params to be used if the laser fails (i.e., zenith reference)
                                'R': 0.75,
                            'alpha': 8.4e-5,
                                'I': 1.0,
                                'B': 0.0,
                               'a1': 3.0e-2,
                               'a2': -3.1e-2,
                               'b0': 2.0,
                               'b1': 1.1,
                               'b2': -2.8e-1, 
                           'center':  (254.3, 258.7),
                          },
        'sql_winds_id'          : 91,           # ID for SQL database
        'sql_temperatures_id'   : 92,           # ID for SQL database
        'sql_diagnostics_id'    : 93,           # ID for SQL database
        'many_fringes'          : True,         # indicates whether radial falloff terms should be used
        'bad_wind_dates'        : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'bad_temperature_dates' : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'send_to_madrigal'      : True, # whether or not we should send this instrument's data to Madrigal
    }

# TODO: Default instrument params for minime90
_instruments['minime90'] = {
        'name'          : 'minime90',
        'N'             : 500,          # Number of annuli
        'N0'            : 0,            # First annulus to use
        'N1'            : 500,          # Last annulus to use
        'focal_length'  : 310e-3,       # focal length of lens in m
        'pix_size'      : 21e-6,        # pixel size on CCD in m # TODO: Is this right?
        'lam_laser'     : 632.8e-9,     # laser wavelength in m
        'lam0'          : 630.0e-9,     # nominal line center wavelength in m
        'nominal_t'     : 1.5e-2,       # approximate etalon gap in m
        'default_params': {# instrument params to be used if the laser fails (i.e., zenith reference)
                                'R': 0.72,
                            'alpha': 6.9e-5,
                                'I': 1.0,
                                'B': 0.0,
                               'a1': -4.8e-2,
                               'a2': -1.5e-2,
                               'b0': 1.0,
                               'b1': -2.1e-1,
                               'b2': -4.9e-2, 
                           'center':  (254.4, 253.2),
                          },
        'sql_winds_id'          : 64,           # ID for SQL database
        'sql_temperatures_id'   : 65,           # ID for SQL database
        'sql_diagnostics_id'    : 94,           # ID for SQL database
        'many_fringes'          : True,         # indicates whether radial falloff terms should be used
        'bad_wind_dates'        : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'bad_temperature_dates' : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'send_to_madrigal'      : False, # whether or not we should send this instrument's data to Madrigal
    }

_instruments['minime91'] = {
        'name'          : 'minime91',
        'N'             : 500,          # Number of annuli
        'N0'            : 0,            # First annulus to use
        'N1'            : 500,          # Last annulus to use
        'focal_length'  : 310e-3,       # focal length of lens in m
        'pix_size'      : 13e-6,        # pixel size on CCD in m
        'lam_laser'     : 632.8e-9,     # laser wavelength in m
        'lam0'          : 630.0e-9,     # nominal line center wavelength in m
        'nominal_t'     : 1.5e-2,       # approximate etalon gap in m
        'default_params': {# instrument params to be used if the laser fails (i.e., zenith reference)
                                'R': 0.746,
                            'alpha': 8.373e-5,
                                'I': 1.0,
                                'B': 0.0,
                               'a1': 1.8e-2,
                               'a2': -3.24e-2,
                               'b0': 1.14,
                               'b1': 3.67e-1,
                               'b2': 5.7e-2, 
                           #'center':  (253.14137959, 255.67217962), # from 2012
                           'center': (251.366416846, 252.039655294) # from Sep 01 2013
                          },
        'sql_winds_id'          : 66,           # ID for SQL database
        'sql_temperatures_id'   : 67,           # ID for SQL database
        'sql_diagnostics_id'    : 95,           # ID for SQL database
        'many_fringes'          : True,         # indicates whether radial falloff terms should be used
        'bad_wind_dates'        : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'bad_temperature_dates' : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'send_to_madrigal'      : False, # whether or not we should send this instrument's data to Madrigal
    }

# TODO: Default instrument params for minime92
_instruments['minime92'] = {
        'name'          : 'minime92',
        'N'             : 500,          # Number of annuli
        'N0'            : 0,            # First annulus to use
        'N1'            : 500,          # Last annulus to use
        'focal_length'  : 300e-3,       # focal length of lens in m # Is this right?
        'pix_size'      : 6.4e-6,       # pixel size on CCD in m # Is this right?
        'lam_laser'     : 632.8e-9,     # laser wavelength in m
        'lam0'          : 630.0e-9,     # nominal line center wavelength in m
        'nominal_t'     : 1.0e-2,       # approximate etalon gap in m
        'default_params': {# instrument params to be used if the laser fails (i.e., zenith reference)
                                'R': 0.746,
                            'alpha': 8.373e-5,
                                'I': 1.0,
                                'B': 0.0,
                               'a1': 1.8e-2,
                               'a2': -3.24e-2,
                               'b0': 1.14,
                               'b1': 3.67e-1,
                               'b2': 5.7e-2, 
                           'center':  (253.14137959, 255.67217962),
                          },
        'sql_winds_id'          : 96,           # ID for SQL database
        'sql_temperatures_id'   : 97,           # ID for SQL database
        'sql_diagnostics_id'    : 98,           # ID for SQL database
        'many_fringes'          : False,        # indicates whether radial falloff terms should be used
        'bad_wind_dates'        : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'bad_temperature_dates' : [],   # Each entry is a tuple (start_date, stop_date, flag), between which data are bad. flag is a number, indicating the severity.
        'send_to_madrigal'      : False, # whether or not we should send this instrument's data to Madrigal
    }

_instruments['noto01'] = {} # TODO (if we need to)

_instruments['noto02'] = {} # TODO (if we need to)

# Add "Abbreviation" key to the instrument dictionary
for instr_name in _instruments.iterkeys():
    _instruments[instr_name]['Abbreviation'] = instr_name



################## Site information functions ####################
    

def get_site_info(site_name):
    '''
    Return a dictionary with information about a site.

    INPUT:
        site_name - abbreviated site name (e.g., 'uao')
    OUTPUT:
        site_info - dictionary with information about the site.
        (keys are 'Location', 'TimeZone', 'Name', etc.)
    '''
    
    try:
        site_info = _sites[site_name].copy()
    except KeyError:
        raise Exception('Site name ("%s") not recognized. Try one of %s.' % \
                         (site_name, str(_sites.keys())))         
    
    return _sites[site_name].copy()

def get_network_info(network_name):
    '''
    Return a dictionary of site dictionaries, keyed by the site name. Only 
    sites in the network specified by network_name are included.

    INPUT:
        network_name - abbreviated network name (e.g., 'nation')
    OUTPUT:
        network_dict - dictionary whose keys are site names (e.g., 'uao') and values
        are dictionaries with information about the site (see get_site_info).
        For example, network_dict['uao'] is the same as get_site_info('uao')
        Also, network_dict has keys describing network level information, such
        as the network's sql_id.
    '''
    
    network_dict = {}
    if network_name in _networks.keys():
        network_dict = _networks[network_name].copy()
    
    for site_name in _sites:
        if _sites[site_name]['Network'] == network_name:
            network_dict[site_name] = _sites[site_name]

    if len(network_dict) == 0: # network_name not recognized
        allowable_names = list(set([_sites[site_name]['Network'] for site_name in _sites]))
        raise Exception('Network name ("%s") not recognized. Try one of %s.' % \
                         (network_name, str(allowable_names)))
    return network_dict

def get_all_sites_info():
    '''
    Return a dictionary of all site dictionaries, keyed by the site name.

    OUTPUT:
        all_site_dicts - dictionary whose keys are site names (e.g., 'uao') and values
        are dictionaries with information about the site (see get_site_info).
        For example, all_site_dicts['uao'] is the same as get_site_info('uao')
    '''
    
    return _sites.copy()




################### Instrument information functions #######################

def get_site_of(instr_name, dn):
    '''
    Return the name of the site where the instrument with name
    instr_name was on the day with date number dn. Return None
    if this instrument was nowhere on this date.
    INPUTS:
        instr_name - str, e.g., 'minime05'
        dn - datetime.datetime
    OUTPUTS:
        site_name - str, site name on this day, or None
    ''' 
    
    try:
        startstop = _dates[instr_name]
    except KeyError:
        raise Exception('Instrument name "%s" not recognized. Try one of: %s' \
                        % ( instr_name, str(sorted(_instruments.keys())) ))
    site_name = None
    for sn in startstop:
        start = startstop[sn]['start']
        stop  = startstop[sn]['stop' ]
        if start <= dn and (stop is None or dn <= stop):
            # We have a match. Make sure that we haven't found > one matches.
            if site_name is not None:
                raise Exception('Two sites ("%s", "%s") found for instrument "%s" on "%s")' \
                                % (site_name, sn, instr_name, str(dn)))
            site_name = sn

    return site_name
        

def get_instr_at(site_name, dn):
    '''
    Return the names of the instruments at site site_name
    on the day with date number dn.
    INPUTS:
        site_name - str, e.g., 'uao'
        dn - datetime.datetime
    OUTPUTS:
        instr_names - list of strs, comprising instrument names
    '''

    instr_names = []
    for n in _dates: # loop over possible instrument names
        if get_site_of(n, dn) == site_name:
            # add it to the list
            instr_names.append(n)
    return instr_names
        

def get_instr_info(instr_name, dn = datetime.datetime.now()):
    '''
    Return an instrument dictionary for instrument with name instr_name.
    This may depend on the date number dn.
    INPUTS:
        instr_name - str, e.g., 'minime01'
        dn - datetime.datetime
    OUTPUTS:
        instrument - dictionary specifying instrument parameters
    '''
    try:
        instrument = _instruments[instr_name].copy()
    except KeyError:
        raise Exception('Instrument name "%s" not recognized. Try one of: %s' \
                        % ( instr_name, str(sorted(_instruments.keys())) ))

    # minime06 ccd was changed on 2/16/2012
    if instr_name == 'minime06' and dn > datetime.datetime(2012,2,17,12,0,0):
        instrument['pix_size'] = 24e-6


    if instr_name == 'minime03':
        # minime03 had its laser installed on 12/16/2013.
        # These are the retroactive instrument parameters for the pre-laser
        # period:
        if dn < datetime.datetime(2013,12,17,0,0):
            instrument['default_params'] = {# instrument params to be used if the laser fails (i.e., zenith reference)
                                    'R': 4.722e-01,
                                'alpha': 8.357e-05,
                                    'I': 1.0,
                                    'B': 0.0,
                                   'a1': 4.128e-01,
                                   'a2': -1.968e-01,
                                   'b0': -4.654e-01,
                                   'b1': 4.003e-01,
                                   'b2': 4.973e-01, 
                               'center':  (266.3, 265.7),
                              }
        # On 1/5/2014, the instrument was tuned and refocused. 
        # These are the instrument parameters from before that period:
        elif dn < datetime.datetime(2014,1,5,0,0):
            instrument['default_params'] = {# instrument params to be used if the laser fails (i.e., zenith reference)
                                    'R': 5.098e-01,
                                'alpha': 8.378e-05,
                                    'I': 1.0,
                                    'B': 0.0,
                                   'a1': -3.791e-01,
                                   'a2': 4.388e-02,
                                   'b0': 2.319e-01,
                                   'b1': 3.423e-01,
                                   'b2': 7.130e-02, 
                               'center':  (266.3, 265.7),
                              }

    
    return instrument

def get_all_instr_names():
    '''
    Return a list of all of the instrument names (strings).
    '''
    return _instruments.keys()

def get_bad_data_flags(instr_name, dn = datetime.datetime.now()):
    '''
    Return flags indicating if the wind and/or temperature
    data are not believable.
    INPUTS:
        instr_name - str, e.g., 'minime01'
        dn - datetime.datetime
    OUTPUTS:
        data_flags: length-2 list, [bad_wind_flag, bad_temperature_flag], where each is
                    a flag indicating the quality of the data. 0 is good.
    '''
    try:
        windstartstops = _instruments[instr_name]['bad_wind_dates']
        tempstartstops = _instruments[instr_name]['bad_temperature_dates']
    except KeyError:
        raise Exception('Instrument name "%s" not recognized. Try one of: %s' \
                        % ( instr_name, str(sorted(_instruments.keys())) ))
    
    bad_wind_flag = 0
    for (start,stop,flag) in windstartstops:
        if start <= dn and (stop is None or dn <= stop):
            bad_wind_flag = flag
    bad_temp_flag = 0
    for (start,stop,flag) in tempstartstops:
        if start <= dn and (stop is None or dn <= stop):
            bad_temp_flag = flag   

    return [bad_wind_flag, bad_temp_flag]

def angle_correction(az, ze, instr_name, dn):
    '''
    Return corrected azimuth and zenith angles. Nominally,
    this function should just return (az,ze), unless there
    is something wrong with the angles reported in the image
    header.
    INPUTS:
        az - azimuth angle (accepts an array)
        ze - zenith angle (accepts an array)
        instr_name - string, e.g., 'minime05'
        dn - datetime.datetime specifying the date of observation
    OUTPUTS:
        az - corrected azimuth angle
        ze - corrected zenith angle
    '''
    
    # Make the corrections for the gear-vs-chain drive issue pre-2012 in Peru
    if instr_name == 'minime90' and dn < datetime.datetime(2011, 11, 18):
        az = -az

    if instr_name == 'minime91' and dn < datetime.datetime(2011, 12, 1):
        az = -az

    
    
    return (az,ze)













