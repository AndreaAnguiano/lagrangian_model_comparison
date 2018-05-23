import os
from datetime import datetime, timedelta
from gnome import basic_types, scripting, utilities
import numpy as np

from modelConfig import *
# add paths

# data_path = os.path.dirname('/home/andrea/python/lagrangian_model_comparison/pyGnome/oilSpillPyGnome/Data/')
# output_path = os.path.dirname('/home/andrea/python/lagrangian_model_comparison/pyGnome/oilSpillPyGnome/outputs/')

data_path = os.path.dirname('/home/olmozavala/Dropbox/MyProjects/UNAM/OilSpill_Andrea/lagrangian_model_comparison/pyGnome/oilSpillPyGnome/Data/')
output_path = os.path.dirname('/home/olmozavala/Dropbox/MyProjects/UNAM/OilSpill_Andrea/lagrangian_model_comparison/pyGnome/oilSpillPyGnome/output/')

#define map name
map = 'gulf.bna'
reFloatHalfLife = -1 # Particles that beach on the shorelines are randomly refloated according to the specified half-life (specified in hours). # If no refloating is desired set this value to -1.

# spill timming
startDate = datetime(2018,05,01)
duration = timedelta(days=7)

#timestep (s)
timeStep = 3600 * 4

#oil decay (weathering)
weatheringSteps = 1 #how many weathering substeps to run inside a single model time step

#model uncertain
uncertain = True

#Files
windFile = 'GFS_Global_0p5deg.nc'
currFile = 'HYCOM_3d.nc'
tidalFile = 'VDATUM_EC2001.nc'

# # Elements
num_elements = 1e5

# depths
depths = [0, 400, 1100]

#spill location
lat = 28.738
lon = -88.366

if __name__ == '__main__':
    scripting.make_images_dir()
    model = make_model(timeStep,startDate, duration, weatheringSteps, map, uncertain, data_path, reFloatHalfLife, windFile,
                       currFile, tidalFile, num_elements, depths, lat, lon, output_path)

for step in model:
    #print step
    print "step: %.4i -- memuse: %fMB" % (step['step_num'],
                                          utilities.get_mem_use())

