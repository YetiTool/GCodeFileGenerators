# Cuts teeth into stock to create Y rack

################################
# Z-DATUM:                     #
# Bottom surface of material   #
################################

###### <<<<<<<<<SWITCH HERE>>>>>>>> #############

# Uncomment the job needed

# job_name = "02 X RACK TEETH"
# job_name = "03 X RACK GUTTER"

job_name = "02 Y RACK TEETH"
# job_name = "03 Y RACK GUTTER"

#################################################

# Y

if job_name == "02 X RACK TEETH":

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
    
    z_grid = [6.25, 5.12] # See sketch which defines even chip load at these depths 
    print z_grid  
    # Safety
    z_clearance_above_top_surface = 3 # relative clearance above stock for safe moves
    z_clearance_above_last_cut = 3 # relative clearance above last cut for next  moves
    z_clearance_on_cut_approach = 1 # as we get very near the material, we need to be at cutting feed for

elif job_name == "03 X RACK GUTTER":

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
    
    z_grid = [4.32] # See sketch which defines even chip load at these depths 
    print z_grid    
    # Safety
    z_clearance_above_top_surface = 3 # relative clearance above stock for safe moves
    z_clearance_above_last_cut = 3 # relative clearance above last cut for next  moves
    z_clearance_on_cut_approach = 1.5 # as we get very near the material, we need to be at cutting feed for

# Y

elif job_name == "02 Y RACK TEETH":
    x_edge_of_stock_from_datum = 0
    x_job_start_from_edge_of_stock = 30.0
    x_datum = x_edge_of_stock_from_datum + x_job_start_from_edge_of_stock   # Job start point - Relative to home corner of stock
    x_job_width = 550.0
    x_end = x_datum + x_job_width
    y_datum = 178.5
    y_first_valley_position_on_model = 72.72
    y_last_valey_position_on_model = 2643 # will use a less than loop to stop the while loop, hence 1mm added onto theoretical last position
    y_valleys_to_skip_home = 0 # number of gutters not to be cut at the home end
    y_valleys_to_skip_end = 0 # number of gutters not to be cut at the far end
    thickest_material_thickness = 13.5 # polymer thickness can have a wild tolerance
    y_increment = 4.712388 # distance between teeth

    # Cutting variables
    xy_feed_rate = 3000 #mm/min
    xy_backlash_compensation_rate = 500 #mm/min
    z_feed_rate = 1000 #mm/min
    spindle_speed = 20000
    tool_position = 11

    z_grid = [8.62] # See sketch which defines even chip load at these depths 
    print z_grid    
    # Safety
    z_clearance_above_top_surface = 3 # relative clearance above stock for safe moves
    z_clearance_above_last_cut = 3 # relative clearance above last cut for next  moves
    z_clearance_on_cut_approach = 1 # as we get very near the material, we need to be at cutting feed for

elif job_name == "03 Y RACK GUTTER":
    x_edge_of_stock_from_datum = 0
    x_job_start_from_edge_of_stock = 30.0
    x_datum = x_edge_of_stock_from_datum + x_job_start_from_edge_of_stock   # Job start point - Relative to home corner of stock
    x_job_width = 550.0
    x_end = x_datum + x_job_width
    y_datum = 178.5
    y_first_valley_position_on_model = 72.72
    y_last_valey_position_on_model = 2643 # will use a less than loop to stop the while loop, hence 1mm added onto theoretical last position
    y_valleys_to_skip_home = 4 # number of gutters not to be cut at the home end
    y_valleys_to_skip_end = 1 # number of gutters not to be cut at the far end
    thickest_material_thickness = 13.5 # polymer thickness can have a wild tolerance
    y_increment = 4.712388 # distance between teeth
    tool_position = 12

    # Cutting variables
    xy_feed_rate = 3000 #mm/min
    xy_backlash_compensation_rate = 500 #mm/min
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

'''
%
:1248
G90
N30G0X0Y0
N40G40G17G80G49
N50T5M6
N60G90G54
N70G43H5
N80G0X0.000Y0.000S16000M3
'''

lines = ['% ' + job_name,
        ':1248',
        'N30 G0 X0 Y0', #
        'N40 G40 G17 G80 G49', #
        'N50 T' + str(tool_position) + ' M6', #
        'N60 G90 G54', #
        'N70 G43 H' + str(tool_position), # 
        'N80 G0 X0.000 Y0.000 S' + str(spindle_speed) + ' M3', # Turn on spindle
        ]

# POPULATE GRID
y_grid = []
y = y_datum + y_first_valley_position_on_model + y_valleys_to_skip_home * y_increment
while y < y_last_valey_position_on_model + y_datum - y_valleys_to_skip_end * y_increment + 1.0:
    y_grid.append(round(y, 3))
    y += y_increment
print y_grid    

backlash_compensation_dist = 2
line_number = 100

for y in y_grid:

    lines.append("N" + str(line_number) + " G0 X" + str(x_datum) + " Y" + str(y+backlash_compensation_dist)) #Go to XY start plus Y backlash comp
    line_number += 10
    lines.append("N" + str(line_number) + " G1 X" + str(x_datum) + " Y" + str(y) + " F" + str(xy_backlash_compensation_rate)) #Go to XY start
    line_number += 10

    for z in z_grid:

        lines.append("N" + str(line_number) + " G0 X" + str(x_datum) + " Y" + str(y)) #Go to XY start plus Y backlash comp
        line_number += 10
        lines.append("N" + str(line_number) + " G0 Z" + str(z + z_clearance_on_cut_approach)) #Dive to just above material
        line_number += 10
        lines.append("N" + str(line_number) + " G1 Z" + str(z) + " F" + str(z_feed_rate)) #Feed dive to z depth
        line_number += 10
        lines.append("N" + str(line_number) + " G1 X" + str(x_end) + " F" + str(xy_feed_rate)) #Feed cut face width of tooth
        line_number += 10
        lines.append("N" + str(line_number) + " G1 Z" + str(z + z_clearance_on_cut_approach) + " F" + str(z_feed_rate)) #Lift off material surface slowly
        line_number += 10
        lines.append("N" + str(line_number) + " G0 Z" + str(z + z_clearance_above_last_cut)) #Lift to safe distance above last cut
        line_number += 10

    lines.append("N" + str(line_number) + " G0 Z" + str(z_height_above_stock)) #Lift to clear stock, so we can increment in y
    line_number += 10

lines.append("N" + str(line_number) + " M5") #Kill spindle
line_number += 10
lines.append("N" + str(line_number) + " M30") #Prog end
line_number += 10
  
f = open("AI-YETI " + job_name + ".nc", "w")
for line in lines:
    f.write(line + "\n")   

print "Done: " + job_name