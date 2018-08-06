from gnome.model import Model
from datetime import datetime, timedelta
from gnome.map import GnomeMap
from gnome.movers import SimpleMover, RandomMover, GridWindMover
from gnome.spill import PointLineRelease, Spill
from gnome.outputters import Renderer, KMZOutput
from os.path import join
from gnome.utilities.remote_data import get_datafile
from gnome.map import MapFromBNA

lat = 28.738
lon = -88.366
#  SW NW NE SE
# bbox = ((-99,16), (-99,31), (-80,31), (-80,16))
bbox = ((-92,23), (-92,31), (-86,31), (-86,23))
data_path = 'Data'

print("Creating model...")

# time:units = "Hour since 2018-04-19 00:00:00" ;

# TODO dates are wrong compared with NETCDF the day do NOT correspond
start_time = datetime(2018, 05, 01, 1, 0)
model = Model(start_time=start_time,
              duration=timedelta(days=3),
              time_step=60 * 60, #seconds
              )


print("Adding map ...")
map = join(data_path,'gulf.bna')
mapfile = get_datafile(map)
model.map = MapFromBNA(mapfile, refloat_halflife = -1)


print("Adding mover...")
random_mover = RandomMover()
# windFile = 'GFS_Global_0p5deg.nc'
windFile = 'OURS/GFS/gfs.t00z.pgrb2.0p25.f000'
wind_file = get_datafile(join(data_path, windFile))
model.movers += GridWindMover(wind_file)
model.movers += random_mover

print("Adding spill...")
release = PointLineRelease(release_time=start_time,start_position=(lon,lat,0),num_elements=1000)
spill = Spill(release)
model.spills += spill

print("Adding renderer...")


model.outputters += KMZOutput('./output/gnome_results.kmz', output_timestep=timedelta(hours=6))

renderer = Renderer(output_timestep=timedelta(hours=6),output_dir='./output',
                    mapfile=map, map_BB=bbox)

model.outputters += renderer

model.full_run()
