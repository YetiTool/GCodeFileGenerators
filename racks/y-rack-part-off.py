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
        'G4 P1', # Allow time to spin up to speed
        'AE' # Switch on extractor
        'G4 P2', # Allow time to spin up to speed
        ]

# Cutting variables
xy_feed_rate = 600 #mm/min
z_feed_rate = 200 #mm/min

# Job start point - Relative to home corner of stock
x_datum = 20.85
y_datum = 50
x_job_size = 262.15
y_job_size = 1321.50

# Job variables
thickest_material_thickness = 13.5 # polymer thickness can have a wild tolerance
z_clearance_above_top_surface = 5 # relative clearance above stock for safe moves
z_height_for_rapid_move = z_clearance_above_top_surface + thickest_material_thickness

rack_width = 20.5
cutter_diameter = 6.35
number_of_racks = 10

number_of_inner_channels = 1.0

inner_part_off_depth_1 = 2
inner_part_off_depth_2 = -0.5

outer_part_off_depth_1 = 10
outer_part_off_depth_2 = 7
outer_part_off_depth_3 = 4
outer_part_off_depth_4 = 1
outer_part_off_depth_5 = -0.5

excess_run = 0.5

# Inner part offs
lines.append("\n(Inner partoffs)")

x_inner_coord = x_datum + rack_width + (cutter_diameter/2)

while number_of_inner_channels < number_of_racks:
    lines.append("G0 Z" + str(z_height_for_rapid_move))
    lines.append("G0 X" + str(x_inner_coord) + " Y" + str(y_datum - excess_run))
    lines.append("G1 Z" + str(inner_part_off_depth_1) + " F" + str(z_feed_rate))
    lines.append("G1 Y" + str(y_datum + y_job_size + excess_run) + " F" + str(xy_feed_rate))
    lines.append("G1 Z" + str(inner_part_off_depth_2) + " F" + str(z_feed_rate))
    lines.append("G1 Y" + str(y_datum - excess_run) + " F" + str(xy_feed_rate * 2))
    number_of_inner_channels += 1.0
    x_inner_coord += rack_width + cutter_diameter

# Outside lengths
lines.append("\n(Outside lengths)")

x_side_coord = x_datum-(cutter_diameter/2)
while x_side_coord < (x_datum + x_job_size + cutter_diameter):
 
    lines.append("G0 Z" + str(z_height_for_rapid_move))
    lines.append("G0 X" + str(x_side_coord) + " Y" + str(y_datum - excess_run))
    lines.append("G1 Z" + str(outer_part_off_depth_1) + " F" + str(z_feed_rate))
    lines.append("G1 Y" + str(y_datum + y_job_size + excess_run) + " F" + str(xy_feed_rate))
    lines.append("G1 Z" + str(outer_part_off_depth_2) + " F" + str(z_feed_rate))
    lines.append("G1 Y" + str(y_datum - excess_run) + " F" + str(xy_feed_rate))
    lines.append("G1 Z" + str(outer_part_off_depth_3) + " F" + str(z_feed_rate))
    lines.append("G1 Y" + str(y_datum + y_job_size + excess_run) + " F" + str(xy_feed_rate))
    lines.append("G1 Z" + str(outer_part_off_depth_4) + " F" + str(z_feed_rate))
    lines.append("G1 Y" + str(y_datum - excess_run) + " F" + str(xy_feed_rate))
    lines.append("G1 Z" + str(outer_part_off_depth_5) + " F" + str(z_feed_rate))
    lines.append("G1 Y" + str(y_datum + y_job_size + excess_run) + " F" + str(xy_feed_rate))   
    x_side_coord += x_job_size + cutter_diameter

# Outside ends
lines.append("\n(Outside ends)")


y_side_coord = y_datum-(cutter_diameter/2)
while y_side_coord < (y_datum + y_job_size + cutter_diameter):
 
    lines.append("G0 Z" + str(z_height_for_rapid_move))
    lines.append("G0 X" + str(x_datum + x_job_size + excess_run) + " Y" + str(y_side_coord))
    lines.append("G1 Z" + str(outer_part_off_depth_1) + " F" + str(z_feed_rate))
    lines.append("G1 X" + str(x_datum - excess_run) + " F" + str(xy_feed_rate))

    lines.append("G0 Z" + str(z_height_for_rapid_move))
    lines.append("G0 X" + str(x_datum + x_job_size + excess_run) + " Y" + str(y_side_coord))
    lines.append("G1 Z" + str(outer_part_off_depth_2) + " F" + str(z_feed_rate))
    lines.append("G1 X" + str(x_datum - excess_run) + " F" + str(xy_feed_rate))

    lines.append("G0 Z" + str(z_height_for_rapid_move))
    lines.append("G0 X" + str(x_datum + x_job_size + excess_run) + " Y" + str(y_side_coord))
    lines.append("G1 Z" + str(outer_part_off_depth_3) + " F" + str(z_feed_rate))
    lines.append("G1 X" + str(x_datum - excess_run) + " F" + str(xy_feed_rate))

    lines.append("G0 Z" + str(z_height_for_rapid_move))
    lines.append("G0 X" + str(x_datum + x_job_size + excess_run) + " Y" + str(y_side_coord))
    lines.append("G1 Z" + str(outer_part_off_depth_4) + " F" + str(z_feed_rate))
    lines.append("G1 X" + str(x_datum - excess_run) + " F" + str(xy_feed_rate))

    lines.append("G0 Z" + str(z_height_for_rapid_move))
    lines.append("G0 X" + str(x_datum + x_job_size + excess_run) + " Y" + str(y_side_coord))
    lines.append("G1 Z" + str(outer_part_off_depth_5) + " F" + str(z_feed_rate))
    lines.append("G1 X" + str(x_datum - excess_run) + " F" + str(xy_feed_rate))


    
    y_side_coord += y_job_size + cutter_diameter


lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("M5") #Kill spindle
lines.append("G0 X0 Y0")    
lines.append("G4 P2") #Pause for vac overrun
lines.append("AF") #Vac off
lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
f = open("y_rack_part_off.nc", "w")
for line in lines:
    f.write(line + "\n")   

print "Done."
