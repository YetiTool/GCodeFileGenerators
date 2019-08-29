# Cuts teeth into stock to create Y rack

################################
# Z-DATUM:                     #
# Bottom surface of material   #
################################

# Header
lines = ['(T1 CUSTOM TOOTH CUTTER)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'M3 S25000', # Turn on spindle
        'G4 P1', # Allow time for inrush
        'AE', # Switch on extractor
        'G4 P2', # Allow time to spin up to speed
        ]


# Cutting variables
xy_feed_rate = 1500 #mm/min
z_feed_rate = 200 #mm/min
z_stepdown = 1.5

# Job start point - Relative to home corner of stock
x_datum = 20.85
y_datum = 50
x_job_size = 262.15
y_job_size = 1321.50

rack_width = 20.5
number_of_racks = 10

cutter_diameter = 6.35
cutter_rad = cutter_diameter/2
excess_run = 0.5

# Stock variables
thickest_material_thickness = 13.5 # polymer thickness can have a wild tolerance
z_clearance_above_top_surface = 5 # relative clearance above stock for safe moves
z_height_for_rapid_move = z_clearance_above_top_surface + thickest_material_thickness



# Mating end

final_surface_y_coord = y_datum - (cutter_diameter/2)
finishing_pass_stepover = 0.1 # amount of bite the full face of the cutter engages with
finishing_passes_total = 4
finishing_total_thickness = finishing_passes_total * finishing_pass_stepover

trench_y_max = final_surface_y_coord - finishing_total_thickness
trench_final_z_depth = 1
trench_excess_x_width = 5
trench_y_length = 2

trench_x0 = x_datum  - cutter_rad/2 - trench_excess_x_width # home end
trench_x1 = x_datum  + cutter_rad/2 + trench_excess_x_width + x_job_size
trench_y0 = trench_y_max - trench_y_length # home end
trench_y1 = trench_y_max


lines.append("\n(Mating end trench)")

lines.append("G0 X" + str(trench_x1) + " Y" + str(trench_y0))
lines.append("G0 Z" + str(z_height_for_rapid_move))

z = thickest_material_thickness

while z > trench_final_z_depth:
    
    z -= z_stepdown
    if z < trench_final_z_depth: z = trench_final_z_depth
    lines.append("G1 Z" + str(z) + " F" + str(z_feed_rate))
    lines.append("G1 X" + str(trench_x0) + " Y" + str(trench_y0) + " F" + str(xy_feed_rate))
    lines.append("G1 Y" + str(trench_y1) + " F" + str(xy_feed_rate))
    lines.append("G1 X" + str(trench_x1))
    lines.append("G1 Y" + str(trench_y0))


lines.append("\n(Mating end finishing passes)")

finishing_pass = 1
backlash_comp = 2

while finishing_pass <= finishing_passes_total:
    
    lines.append("G0 Z" + str(z_height_for_rapid_move))
    lines.append("G0 X" + str(trench_x0) + " Y" + str(trench_y1 + (finishing_pass * finishing_pass_stepover) + backlash_comp))
    lines.append("G1 X" + str(trench_x0) + " Y" + str(trench_y1 + (finishing_pass * finishing_pass_stepover)) + " F" + str(xy_feed_rate))
    lines.append("G1 Z" + str(trench_final_z_depth) + " F" + str(z_feed_rate))
    lines.append("G1 X" + str(trench_x1) + " F" + str(xy_feed_rate))

    finishing_pass += 1


 
# Inner part offs
lines.append("\n(Inner partoffs)")
 
x_inner_coord = x_datum + rack_width + (cutter_diameter/2)
 
inner_channel_instance = 1


# height_of_shoulder = 5
inner_part_off_depth_1 = 3.5
inner_part_off_depth_2 = 2
inner_part_off_depth_3 = 0.5
inner_part_off_depth_4 = -0.5
 
while inner_channel_instance < number_of_racks:
    lines.append("G0 Z" + str(z_height_for_rapid_move))
    lines.append("G0 X" + str(x_inner_coord) + " Y" + str(y_datum - excess_run))
    lines.append("G1 Z" + str(inner_part_off_depth_1) + " F" + str(z_feed_rate))
    lines.append("G1 Y" + str(y_datum + y_job_size + excess_run) + " F" + str(xy_feed_rate))
    lines.append("G1 Z" + str(inner_part_off_depth_2) + " F" + str(z_feed_rate))
    lines.append("G1 Y" + str(y_datum - excess_run) + " F" + str(xy_feed_rate))
    lines.append("G1 Z" + str(inner_part_off_depth_3) + " F" + str(z_feed_rate))
    lines.append("G1 Y" + str(y_datum + y_job_size + excess_run) + " F" + str(xy_feed_rate))
    lines.append("G1 Z" + str(inner_part_off_depth_4) + " F" + str(z_feed_rate))
    lines.append("G1 Y" + str(y_datum - excess_run) + " F" + str(xy_feed_rate))
    inner_channel_instance += 1.0
    x_inner_coord += rack_width + cutter_diameter
 
 
 
# Outside lengths
 
outer_part_off_depth_1 = 11.5
outer_part_off_depth_2 = 10
outer_part_off_depth_3 = 8.5
outer_part_off_depth_4 = 7
outer_part_off_depth_5 = 5.5
outer_part_off_depth_6 = 4
outer_part_off_depth_7 = 2.5
outer_part_off_depth_8 = 1
outer_part_off_depth_9 = -0.5
 
lines.append("\n(Outside lengths: )" )

x0 = x_datum - (cutter_diameter/2)
x1 = x_datum + x_job_size + (cutter_diameter/2)

y0 = y_datum - excess_run
y1 = y_datum + y_job_size + excess_run
 
  
lines.append("G0 Z" + str(z_height_for_rapid_move))

lines.append("G0 X" + str(x0) + " Y" + str(y1))
lines.append("G1 Z" + str(outer_part_off_depth_1) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y0) + " F" + str(xy_feed_rate*2))
lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(x1))
lines.append("G1 Z" + str(outer_part_off_depth_1) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y1) + " F" + str(xy_feed_rate*2))
lines.append("G0 Z" + str(z_height_for_rapid_move))

lines.append("G0 X" + str(x0) + " Y" + str(y1))
lines.append("G1 Z" + str(outer_part_off_depth_2) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y0) + " F" + str(xy_feed_rate*2))
lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(x1))
lines.append("G1 Z" + str(outer_part_off_depth_2) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y1) + " F" + str(xy_feed_rate*2))
lines.append("G0 Z" + str(z_height_for_rapid_move))

lines.append("G0 X" + str(x0) + " Y" + str(y1))
lines.append("G1 Z" + str(outer_part_off_depth_3) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y0) + " F" + str(xy_feed_rate*2))
lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(x1))
lines.append("G1 Z" + str(outer_part_off_depth_3) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y1) + " F" + str(xy_feed_rate*2))
lines.append("G0 Z" + str(z_height_for_rapid_move))

lines.append("G0 X" + str(x0) + " Y" + str(y1))
lines.append("G1 Z" + str(outer_part_off_depth_4) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y0) + " F" + str(xy_feed_rate*2))
lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(x1))
lines.append("G1 Z" + str(outer_part_off_depth_4) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y1) + " F" + str(xy_feed_rate*2))
lines.append("G0 Z" + str(z_height_for_rapid_move))

lines.append("G0 X" + str(x0) + " Y" + str(y1))
lines.append("G1 Z" + str(outer_part_off_depth_5) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y0) + " F" + str(xy_feed_rate*2))
lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(x1))
lines.append("G1 Z" + str(outer_part_off_depth_5) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y1) + " F" + str(xy_feed_rate*2))
lines.append("G0 Z" + str(z_height_for_rapid_move))

lines.append("G0 X" + str(x0) + " Y" + str(y1))
lines.append("G1 Z" + str(outer_part_off_depth_6) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y0) + " F" + str(xy_feed_rate))
lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(x1))
lines.append("G1 Z" + str(outer_part_off_depth_6) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y1) + " F" + str(xy_feed_rate))
lines.append("G0 Z" + str(z_height_for_rapid_move))

lines.append("G0 X" + str(x0) + " Y" + str(y1))
lines.append("G1 Z" + str(outer_part_off_depth_7) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y0) + " F" + str(xy_feed_rate))
lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(x1))
lines.append("G1 Z" + str(outer_part_off_depth_7) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y1) + " F" + str(xy_feed_rate))
lines.append("G0 Z" + str(z_height_for_rapid_move))

lines.append("G0 X" + str(x0) + " Y" + str(y1))
lines.append("G1 Z" + str(outer_part_off_depth_8) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y0) + " F" + str(xy_feed_rate))
lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(x1))
lines.append("G1 Z" + str(outer_part_off_depth_8) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y1) + " F" + str(xy_feed_rate))
lines.append("G0 Z" + str(z_height_for_rapid_move))

lines.append("G0 X" + str(x0) + " Y" + str(y1))
lines.append("G1 Z" + str(outer_part_off_depth_9) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y0) + " F" + str(xy_feed_rate))
lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(x1))
lines.append("G1 Z" + str(outer_part_off_depth_9) + " F" + str(z_feed_rate))
lines.append("G1 Y" + str(y1) + " F" + str(xy_feed_rate))
lines.append("G0 Z" + str(z_height_for_rapid_move))


 
# Compression end part off
lines.append("\n(Compression end)")

y_end_coord = y_datum + y_job_size + (cutter_diameter/2)

x0 = x_datum - excess_run
x1 = x_datum + x_job_size + excess_run


lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(x0) + " Y" + str(y_end_coord))

 
  
lines.append("G1 Z" + str(outer_part_off_depth_1) + " F" + str(z_feed_rate))
lines.append("G1 X" + str(x1) + " F" + str(xy_feed_rate))
lines.append("G1 Z" + str(outer_part_off_depth_2) + " F" + str(z_feed_rate))
lines.append("G1 X" + str(x0) + " F" + str(xy_feed_rate))
lines.append("G1 Z" + str(outer_part_off_depth_3) + " F" + str(z_feed_rate))
lines.append("G1 X" + str(x1) + " F" + str(xy_feed_rate))
lines.append("G1 Z" + str(outer_part_off_depth_4) + " F" + str(z_feed_rate))
lines.append("G1 X" + str(x0) + " F" + str(xy_feed_rate))
lines.append("G1 Z" + str(outer_part_off_depth_5) + " F" + str(z_feed_rate))
lines.append("G1 X" + str(x1) + " F" + str(xy_feed_rate))
lines.append("G1 Z" + str(outer_part_off_depth_6) + " F" + str(z_feed_rate))
lines.append("G1 X" + str(x0) + " F" + str(xy_feed_rate))
lines.append("G1 Z" + str(outer_part_off_depth_7) + " F" + str(z_feed_rate))
lines.append("G1 X" + str(x1) + " F" + str(xy_feed_rate*0.8))
lines.append("G1 Z" + str(outer_part_off_depth_8) + " F" + str(z_feed_rate))
lines.append("G1 X" + str(x0) + " F" + str(xy_feed_rate*0.8))
# lines.append("G1 Z" + str(outer_part_off_depth_9) + " F" + str(z_feed_rate))
# lines.append("G1 X" + str(x1) + " F" + str(xy_feed_rate*0.8))


# Final part off for reference end

y_part_off_excess = 0.2
part_off_depth = -0.5

lines.append("G0 Z" + str(z_height_for_rapid_move))
# lines.append("G0 X" + str(trench_x0) + " Y" + str(final_surface_y_coord - y_part_off_excess))
# lines.append("G1 Z" + str(part_off_depth) + " F" + str(z_feed_rate))
# lines.append("G1 X" + str(trench_x1) + " F" + str(xy_feed_rate*.5))



lines.append("\n(Shutdown)")

lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("M5") #Kill spindle
lines.append("G4 P2") #Pause for vac overrun
lines.append("AF") #Vac off
lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
f = open("y_rack_part_off.nc", "w")
for line in lines:
    f.write(line + "\n")   

print "Done."
