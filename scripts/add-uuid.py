#!/usr/bin/env python

import sys
import netCDF4 as nc
from uuid import uuid4

with nc.Dataset(sys.argv[1], "a") as f:
    f.id = str(uuid4())