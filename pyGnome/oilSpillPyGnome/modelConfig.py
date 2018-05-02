def make_model(timeStep,startTime, duration, weatheringSteps, map, uncertain, data_path, reFloatHalfLife, windFile, currFile, tidalFile, num_elements, depths, lat, lon):
    #initalizing the model
    print 'initializing the model:'
    model = Model(time_step = timeStep, start_time= startTime, duration=duration, uncertain = uncertain)

    #adding the map
    print 'adding the map:'

    mapfile = get_datafile(os.path.join(data_path, map))

    model.map = MapFromBNA(mapfile, refloat_halflife = reFloatHalfLife)
    print 'adding a renderer'
    # renderer is a class that writes map images for GNOME results
    model.outputters += Renderer(mapfile, output_path, size=(800, 600), )

    #adding the movers

    print 'adding a wind mover:'
    wind_file = get_datafile(os.path.join(data_path, windFile))
    model.movers += GridWindMover(wind_file)

    print 'adding a current mover: '
    curr_file = get_datafile(os.path.join(data_path,currFile))
    model.movers+= GridCurrentMover(curr_file)

    print 'adding a spill'
    for i in depths:
         model.spills+= point_line_release_spill(num_elements=num_elements, start_position=(lon,lat,i), release_time=startTime)



    return model