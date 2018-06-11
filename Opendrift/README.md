
# Installation 

## 1. Cloning the OpenDrift git repository 

> git clone https://github.com/OpenDrift/opendrift.git

## 2. Requirements 
> conda install --yes hdf4 numpy scipy matplotlib basemap netcdf4 configobj pillow gdal pyproj ffmpeg 
## 3. Installing
 
> cd opendrift

> python setup.py develop --user

## 3. Testing 

> python -m unittest discover tests -p test_*.py
