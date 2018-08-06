from asyncore import file_dispatcher
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np

# fileName = 'HYCOM_3d.nc'
# dataset = Dataset(fileName, 'r+', 'NETCDF3_CLASSIC')
# time = allVariables.get('time')
# dataset.sync()
# dataset.close()

fileName = 'CurrentsRectangular.nc'
dataset = Dataset(fileName, 'w', format='NETCDF3_CLASSIC')
try:
    fillValue = 1.267651e+30
    dims = 10
    tsteps = 1000

    #adding dimensions
    dataset.createDimension('time', None)
    dataset.createDimension('lat',dims)
    dataset.createDimension('lon',dims)

    # Adding variables
    time = dataset.createVariable('time',np.float64, ('time',))
    lon = dataset.createVariable('lon',np.float32, ('lon',))
    lat = dataset.createVariable('lat',np.float32, ('lat',))
    water_u = dataset.createVariable('water_u', np.float32, ('time','lat', 'lon',), fill_value = fillValue)
    water_v = dataset.createVariable('water_v', np.float32, ('time','lat', 'lon',), fill_value = fillValue)

    #adding global atributtes
    dataset.grid_type = 'REGULAR'

    #adding variables atributtes
    lat.long_name='Latitude'
    lat.units='degrees_north'
    lat.point_spacing='even'

    lon.long_name='Longitude'
    lon.units='degrees_east'
    lon.point_spacing='even'

    time.long_name='Valid Time'
    time.units = 'hours since 2000-12-31 00:00:00'

    water_u.long_name = 'eastward_sea_water_velocity'
    water_u.standard_name = 'eastward_sea_water_velocity'
    water_u.units = 'm/s'
    water_u.scale_factor = 1.0
    water_u.add_offset = 0.0

    water_v.long_name = 'northward_sea_water_velocity'
    water_v.standard_name = 'northward_sea_water_velocity'
    water_v.units = 'm/s'
    water_v.scale_factor = 1.0
    water_v.add_offset = 0.0

    # Adding variable data
    time[:] = np.arange(0,tsteps)*60

    bbox = np.array([[20,32.1],[-98,-80]])
    lat[:] = np.arange(bbox[0,0],bbox[0,1],(bbox[0,1]-bbox[0,0])/dims)
    lon[:] = np.arange(bbox[1,0],bbox[1,1],(bbox[1,1]-bbox[1,0])/dims)

    water_u[:] = np.random.random((tsteps,dims,dims))
    water_v[:] = np.random.random((tsteps,dims,dims))
except Exception as e:
    print('---------------------------- Failed {} error: {} ----------------'.format(e))

# dataset.sync()
dataset.close()

dataset = Dataset(fileName, 'r')
print('*************** Dimensions *************** \n', dataset.dimensions.keys())
print('**************  Variables *************** \n', dataset.variables.keys())

allVariables = dataset.variables
water_u = allVariables.get('water_u')
water_v = allVariables.get('water_v')
time = allVariables.get('time')

lat = allVariables.get('lat')
lon = allVariables.get('lon')
print("Time: {} \n Lat: {} \n Lon: {} \n".format(time[:], lat[:], lon[:]))
plt.imshow(water_v[0,:,:])
plt.show()
plt.imshow(water_u[0,:,:])
plt.show()
dataset.close()
