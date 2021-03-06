# Cuts teeth into stock to create Y rack

################################
# Z-DATUM:                     #
# Bottom surface of material   #
################################

###### <<<<<<<<<SWITCH HERE>>>>>>>> #############

# Uncomment the job needed

# job_name = "X RACK TEETH"
job_name = "X RACK GUTTER"

# job_name = "Y RACK TEETH"
# job_name = "Y RACK GUTTER"

#################################################

# X

if job_name == "X RACK TEETH":

    x_edge_of_stock_from_datum = 513.0
    x_job_start_from_edge_of_stock = 18.0
    x_datum = x_edge_of_stock_from_datum + x_job_start_from_edge_of_stock   # Job start point - Relative to home corner of stock
    x_job_width = 270.0
    x_end = x_datum + x_job_width
    y_datum = 305 # +50 from the edge of stock
    y_first_valley_position_on_model = 0
    y_last_valey_position_on_model = 1400 # will use a less than loop to stop the while loop, hence 1mm added onto theoretical last position
    y_valleys_to_skip_home = 0 # number of gutters not to be cut at the home end
    y_valleys_to_skip_end = 0 # number of gutters not to be cut at the far end
    thickest_material_thickness = 8 # assuming we've skimmed to 8
    y_increment = 4.712388 # distance between teeth

    # Cutting variables
    xy_feed_rate = 3000 #mm/min
    xy_backlash_compensation_rate = 400 #mm/min
    z_feed_rate = 300 #mm/min
    spindle_speed = 20000
    
    z_grid = [6.75, 5.62] # See sketch which defines even chip load at these depths 
    print z_grid  
    # Safety
    z_clearance_above_top_surface = 3 # relative clearance above stock for safe moves
    z_clearance_above_last_cut = 3 # relative clearance above last cut for next  moves
    z_clearance_on_cut_approach = 1 # as we get very near the material, we need to be at cutting feed for

elif job_name == "X RACK GUTTER":

    x_edge_of_stock_from_datum = 513.0
    x_job_start_from_edge_of_stock = 18.0
    x_datum = x_edge_of_stock_from_datum + x_job_start_from_edge_of_stock   # Job start point - Relative to home corner of stock
    x_job_width = 270.0
    x_end = x_datum + x_job_width
    y_datum = 305 # +50 from the edge of stock
    y_first_valley_position_on_model = 0
    y_last_valey_position_on_model = 1400 # will use a less than loop to stop the while loop, hence 1mm added onto theoretical last position
    y_valleys_to_skip_home = 7 # number of gutters not to be cut at the home end
    y_valleys_to_skip_end = 5 # number of gutters not to be cut at the far end
    thickest_material_thickness = 8 # assuming we've skimmed to 8
    y_increment = 4.712388 # distance between teeth

    # Cutting variables
    xy_feed_rate = 3000 #mm/min
    xy_backlash_compensation_rate = 400 #mm/min
    z_feed_rate = 1000 #mm/min
    spindle_speed = 25000
    
    z_grid = [4.82] # See sketch which defines even chip load at these depths 
    print z_grid    
    # Safety
    z_clearance_above_top_surface = 3 # relative clearance above stock for safe moves
    z_clearance_above_last_cut = 3 # relative clearance above last cut for next  moves
    z_clearance_on_cut_approach = 1.5 # as we get very near the material, we need to be at cutting feed for

# Y

elif job_name == "Y RACK TEETH":
    x_edge_of_stock_from_datum = 505.5
    x_job_start_from_edge_of_stock = 20.0
    x_datum = x_edge_of_stock_from_datum + x_job_start_from_edge_of_stock   # Job start point - Relative to home corner of stock
    x_job_width = 265.0
    x_end = x_datum + x_job_width
    y_datum = 50
    y_first_valley_position_on_model = 72.72
    y_last_valey_position_on_model = 2643 # will use a less than loop to stop the while loop, hence 1mm added onto theoretical last position
    y_valleys_to_skip_home = 0 # number of gutters not to be cut at the home end
    y_valleys_to_skip_end = 0 # number of gutters not to be cut at the far end
    thickest_material_thickness = 13.5 # polymer thickness can have a wild tolerance
    y_increment = 4.712388 # distance between teeth

    # Cutting variables
    xy_feed_rate = 3000 #mm/min
    xy_backlash_compensation_rate = 400 #mm/min
    z_feed_rate = 300 #mm/min
    spindle_speed = 20000

    z_grid = [9.75, 8.62] # See sketch which defines even chip load at these depths 
    print z_grid    
    # Safety
    z_clearance_above_top_surface = 3 # relative clearance above stock for safe moves
    z_clearance_above_last_cut = 3 # relative clearance above last cut for next  moves
    z_clearance_on_cut_approach = 1 # as we get very near the material, we need to be at cutting feed for

elif job_name == "Y RACK GUTTER":
    x_edge_of_stock_from_datum = 505.5
    x_job_start_from_edge_of_stock = 20.0
    x_datum = x_edge_of_stock_from_datum + x_job_start_from_edge_of_stock   # Job start point - Relative to home corner of stock
    x_job_width = 265.0
    x_end = x_datum + x_job_width
    y_datum = 50
    y_first_valley_position_on_model = 72.72
    y_last_valey_position_on_model = 2643 # will use a less than loop to stop the while loop, hence 1mm added onto theoretical last position
    y_valleys_to_skip_home = 4 # number of gutters not to be cut at the home end
    y_valleys_to_skip_end = 1 # number of gutters not to be cut at the far end
    thickest_material_thickness = 13.5 # polymer thickness can have a wild tolerance
    y_increment = 4.712388 # distance between teeth

    # Cutting variables
    xy_feed_rate = 3000 #mm/min
    xy_backlash_compensation_rate = 400 #mm/min
    z_feed_rate = 1000 #mm/min
    spindle_speed = 25000

    z_grid = [7.82] # See sketch which defines even chip load at these depths 
    print z_grid    
    # Safety
    z_clearance_above_top_surface = 3 # relative clearance above stock for safe moves
    z_clearance_above_last_cut = 3 # relative clearance above last cut for next  moves
    z_clearance_on_cut_approach = 1.5 # as we get very near the material, we need to be at cutting feed for

    
else: print "Select job name in the code header"



# Implications
z_height_above_stock = z_clearance_above_top_surface + thickest_material_thickness

# Header
lines = ['(' + job_name + ')',
        '(T1 CUSTOM TOOTH CUTTER)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'G4 P1', # Allow time to spin up to speed
        'M3 S' + str(spindle_speed), # Turn on spindle
        'G4 P1' # Allow time to spin up to speed
        ]

# POPULATE GRID
y_grid = []
y = y_datum + y_first_valley_position_on_model + y_valleys_to_skip_home * y_increment
while y < y_last_valey_position_on_model + y_datum - y_valleys_to_skip_end * y_increment + 1.0:
    y_grid.append(round(y, 3))
    y += y_increment
print y_grid    

backlash_compensation_dist = 2

for y in y_grid:

    lines.append("G0 X" + str(x_datum) + " Y" + str(y+backlash_compensation_dist)) #Go to XY start plus Y backlash comp
    lines.append("G1 X" + str(x_datum) + " Y" + str(y) + " F" + str(xy_backlash_compensation_rate)) #Go to XY start

    for z in z_grid:

        lines.append("G0 X" + str(x_datum) + " Y" + str(y)) #Go to XY start plus Y backlash comp
        lines.append("G0 Z" + str(z + z_clearance_on_cut_approach)) #Dive to just above material
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