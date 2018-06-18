from gnome.model import Model
from datetime import datetime, timedelta
from gnome.map import GnomeMap
from gnome.movers import SimpleMover, RandomMover
from gnome.spill import PointLineRelease, Spill
from gnome.outputters import Renderer


print("Creating model...")
start_time = datetime(2015, 1, 1, 0, 0)
model = Model(start_time=start_time,
              duration=timedelta(days=3),
              time_step=60 * 15, #seconds
              )


print("Adding map ...")
model.map = GnomeMap(map_bounds=((-145,48), (-145,49), (-143,49), (-143,48)))

print("Adding mover...")
velocity = (.5,0,0) #(u,v,w) in m/s
uniform_vel_mover = SimpleMover(velocity)
random_mover = RandomMover()

model.movers += uniform_vel_mover
model.movers += random_mover

print("Adding spill...")
release = PointLineRelease(release_time=start_time,start_position=(-144,48.5,0),num_elements=1000)
spill = Spill(release)
model.spills += spill

print("Adding renderer...")
renderer = Renderer(output_timestep=timedelta(hours=6),output_dir='./output',
                    map_BB=((-145,48), (-145,49), (-143,49), (-143,48)))

model.outputters += renderer

model.full_run()
