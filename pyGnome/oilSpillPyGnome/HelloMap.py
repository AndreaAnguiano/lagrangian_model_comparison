from gnome.model import Model
from datetime import datetime, timedelta
from gnome.map import GnomeMap
from gnome.movers import SimpleMover, RandomMover
from gnome.spill import PointLineRelease, Spill
from gnome.outputters import Renderer, KMZOutput
from os.path import join
from gnome.utilities.remote_data import get_datafile
from gnome.map import MapFromBNA

lat = 28.738
lon = -88.366
#  SW NW NE SE
bbox = ((-99,16), (-99,31), (-80,31), (-80,16))
data_path = 'Data'

print("Creating model...")
start_time = datetime(2015, 1, 1, 0, 0)
model = Model(start_time=start_time,
              duration=timedelta(days=5),
              time_step=60 * 60, #seconds
              )


print("Adding map ...")
map = join(data_path,'gulf.bna')
mapfile = get_datafile(map)
model.map = MapFromBNA(mapfile, refloat_halflife = -1)


print("Adding mover...")
velocity = (7,-3,0) #(u,v,w) in m/s
uniform_vel_mover = SimpleMover(velocity)
random_mover = RandomMover()

model.movers += uniform_vel_mover
model.movers += random_mover

print("Adding spill...")
release = PointLineRelease(release_time=start_time,start_position=(lon,lat,0),num_elements=1000)
spill = Spill(release)
model.spills += spill

print("Adding renderer...")
model.outputters += KMZOutput('./output/gnome_results.kmz', output_timestep=timedelta(hours=6))

renderer = Renderer(output_timestep=timedelta(hours=6),output_dir='./output',
                    mapfile=map, draw_map_bounds=True, draw_spillable_area=True)


model.outputters += renderer

model.full_run()
