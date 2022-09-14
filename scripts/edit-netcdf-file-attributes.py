#!/usr/bin/env python

import sys
from datetime import datetime
import numpy as np
import netCDF4 as nc

with nc.Dataset(sys.argv[1], 'r') as f:
    data = f['CHANNEL_4'][100:200,100:200]

with nc.Dataset("out.nc", "w", format='NETCDF4') as f:
    nx = f.createDimension('x', 100)
    nxs = f.createVariable('x', np.float32, ('x',))
    nxs.standard_name = "projection_x_coordinate"
    nxs.long_name = "x coordinate of projection"
    nxs.units = "m"
    nxs.axis = "X"

    ny = f.createDimension('y', 100)
    nys = f.createVariable('y', np.float32, ('y',))
    nys.standard_name = "projection_y_coordinate"
    nys.long_name = "y coordinate of projection"
    nys.units = "m"
    nys.axis = "Y"

    nxs[:] = np.arange(-250000, 250000, 5000)
    nys[:] = np.arange(250000, 750000, 5000)

    time = f.createDimension('time', None)
    times = f.createVariable('time', np.float64, ('time',))
    times.long_name = "time"
    times.standard_name = "time"
    times.units = "seconds since 1970-01-01 00:00:00 +0000"
    times.calendar = 'gregorian'
    times.axis = "T"

    surface = f.createDimension('surface', 1)
    surfaces = f.createVariable('surface', np.int16, ('surface',), fill_value=-32767)
    surfaces.description = "ground or water surface"
    surfaces.long_name = "surface"
    surfaces.positive = "up"
    surfaces.units = "m"

    projection_regular_grid = f.createVariable('projection_polar_stereographic', np.int32)
    projection_regular_grid.grid_mapping_name = "polar_stereographic"
    projection_regular_grid.proj4 = "+proj=stere +lon_0=0 +lat_0=90 +lat_ts=60 +ellps=WGS84 +datum=WGS84 +no_defs"

    surfaces[:] = 0
    times[:] = nc.date2num(datetime.now(), units=times.units, calendar=times.calendar)

    brightnesstemperature = f.createVariable('brightness_temperature', np.float32, ('time', 'surface', 'y', 'x'),
                                       fill_value=np.nan)
    brightnesstemperature.units = "K"
    brightnesstemperature.standard_name = "toa_bidirectional_temperature"
    brightnesstemperature.grid_mapping = "projection_polar_stereographic"

    brightnesstemperature[:] = data
