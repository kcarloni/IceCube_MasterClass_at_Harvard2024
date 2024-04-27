
from pyorbital.planets import Moon

import numpy as np
from datetime import datetime

from src.jdutil import mjd_to_datetime

global moon
moon = Moon( mjd_to_datetime(58931) )


def str_to_datetime( time_str ):
    t_split = t.replace(":", "-")
    t_split = [int(x) for x in t.split("-")]
    try:
        return datetime(*t_split)
    
    except:
        raise ValueError(
            f"Cannot convert {t} to datetime"
        )

"""
calculate the position of the moon at 
- earth surface position defined by (long, lat) in degrees
- time t 
"""
def get_moon_position_at( t, long, lat ):

    moon.datetime = mjd_to_datetime( t )
    moon.get_lonsun()

    # in degrees !!
    _, decl, _, azi = moon.topocentric_position( long, lat )

    zen = 90 - decl
    return azi, zen  


# from .utils import is_floatable
# class Moon:

#     def __init__(self):
#         pass

#     def position(self, t, lat=-90.0, lon=45.0):
        
#         if is_floatable(t):
#             t = mjd_to_datetime(t)

#         if isinstance(t, str):
#             t_split = t.replace(":", "-")
#             t_split = [int(x) for x in t.split("-")]
#             try:
#                 t = datetime(*t_split)
#             except:
#                 raise ValueError(
#                     f"Cannot convert {t} to datetime"
#                 )

#         moon = POMoon(t)
#         _, decl, _, azi = moon.topocentric_position(lon, lat)
#         zen = 90 - decl
#         azi = azi
#         return zen, azi
