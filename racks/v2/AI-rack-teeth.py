# Cuts teeth into stock to create Y rack

################################
# Z-DATUM:                     #
# Bottom surface of material   #
################################

###### <<<<<<<<<SWITCH HERE>>>>>>>> #############

# Uncomment the job needed

job_name = "Y RACK TEETH"
# job_name = "Y RACK TEETH"

#################################################

if job_name == "X RACK TEETH":

    x_edge_of_stock_from_datum = 513.0
    x_job_start_from_edge_of_stock = 18.0
    x_datum = x_edge_of_stock_from_datum + x_job_start_from_edge_of_stock   # Job start point - Relative to home corner of stock
    x_job_width = 270.0
    x_end = x_datum + x_job_width
    y_datum = 305 # +50 from the edge of stock
    y_first_valley_position_on_model = 0
    y_last_valey_position_on_model = 1400 # will use a less than loop to stop the while loop, hence 1mm added onto theoretical last position
    thickest_material_thickness = 8 # polymer thickness can have a wild tolerance
    z_end = 5.62 # height of tooth depth, measured from bottom surface. Note we are assuming 8.5mm stock since we need rack to project far enough out to constrain energy chain! Ideally, we'd nominal at 8, but needs must.
    y_increment = 4.712388 # distance between teeth

    # Cutting variables
    xy_feed_rate = 2400 #mm/min
    xy_backlash_compensation_rate = 400 #mm/min
    z_feed_rate = 300 #mm/min
    z_cut_depth_per_pass = 1
    spindle_speed = 20000
    
    z_grid = [7.2,6.3,5.62] # See sketch which defines even chip load at these depths 
    print z_grid    


elif job_name == "Y RACK TEETH":
    x_edge_of_stock_from_datum = 505.5
    x_job_start_from_edge_of_stock = 20.0
    x_datum = x_edge_of_stock_from_datum + x_job_start_from_edge_of_stock   # Job start point - Relative to home corner of stock
    x_job_width = 265.0
    x_end = x_datum + x_job_width
    y_datum = 50
    y_first_valley_position_on_model = 72.72
    y_last_valey_position_on_model = 2631.54 # will use a less than loop to stop the while loop, hence 1mm added onto theoretical last position
    thickest_material_thickness = 13.5 # polymer thickness can have a wild tolerance
    z_end = 8.62 # height of tooth depth, measured from bottom surface
    y_increment = 4.712388 # distance between teeth
    tool_position = 11

    # Cutting variables
    xy_feed_rate = 2400 #mm/min
    xy_backlash_compensation_rate = 400 #mm/min
    z_feed_rate = 300 #mm/min
    z_cut_depth_per_pass = 1.5
    spindle_speed = 20000

    z_grid = [TODO] # See sketch which defines even chip load at these depths 
    print z_grid    
    
else: print "Select job name in the code header"


# Safety
z_clearance_above_top_surface = 2 # relative clearance above stock for safe moves
z_clearance_above_last_cut = 2 # relative clearance above last cut for next  moves
z_clearance_on_cut_approach = 0.5 # as we get very near the material, we need to be at cutting feed for

# Implications
z_height_above_stock = z_clearance_above_top_surface + thickest_material_thickness
z_start = thickest_material_thickness - z_cut_depth_per_pass





# Header
lines = ['%',
        ':1248',
        'N30G0X0Y0', #
        'N40G40G17G80G49', #
        'N50T' + str(tool_position) + 'M6', #
        'N60G90G54', #
        'N70G43H' + str(tool_position), # 
        'N80G0X0.000Y0.000S' + str(spindle_speed) + '16000M3', # Turn on spindle
        ]

# POPULATE GRID
y_grid = []
y = y_datum + y_first_valley_position_on_model
while y < y_last_valey_position_on_model + y_datum + 1.0:
    y_grid.append(round(y, 3))
    y += y_increment
print y_grid    

backlash_compensation_dist = 2

for y in y_grid:

    lines.append("G0 X" + str(x_datum) + " Y" + str(y+backlash_compensation_dist)) #Go to XY start plus Y backlash comp
    lines.append("G1 X" + str(x_datum) + " Y" + str(y) + " F" + str(xy_backlash_compensation_rate)) #Go to XY start

    for z in z_grid:

        lines.append("G0 X" + str(x_datum) + " Y" + str(y)) #Go to XY start plus Y backlash comp
        lines.append("G0 Z" + str(z + z_cut_depth_per_pass + z_clearance_on_cut_approach)) #Dive to just above material
        lines.append("G1 Z" + str(z) + " F" + str(z_feed_rate)) #Feed dive to z depth
        lines.append("G1 X" + str(x_end) + " F" + str(xy_feed_rate)) #Feed cut face width of tooth
        lines.append("G1 Z" + str(z + z_clearance_on_cut_approach) + " F" + str(z_feed_rate)) #Lift off material surface slowly
        lines.append("G0 Z" + str(z + z_clearance_above_last_cut)) #Lift to safe distance above last cut

    lines.append("G0 Z" + str(z_height_above_stock)) #Lift to clear stock, so we can increment in y

lines.append("M5") #Kill spindle
lines.append("G4 P1") #Pause for vac overrun
lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
f = open(job_name + ".nc", "w")
for line in lines:
    f.write(line + "\n")   

print "Done: " + job_name