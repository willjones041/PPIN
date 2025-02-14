from netCDF4 import Dataset
rootgrp = Dataset("test.nc","w")
time = rootgrp.createDimension("time",None)
print(rootgrp)