# Cuts teeth into stock to create Y rack

################################
# Z-DATUM:                     #
# Bottom surface of material   #
################################


###### <<<<<<<<<SWITCH HERE>>>>>>>> #############

# Uncomment the job needed

# job_name = "X RACK PARTOFF"
job_name = "Y RACK PARTOFF"

#################################################


if job_name == "X RACK PARTOFF":

    x_datum = 28.85 # Job start point - Relative to home corner of stock
    y_datum = 50.0
    x_job_size = 242.15
    y_job_size = 1394.87
    rack_width = 18.5
    number_of_racks = 10
    shoulder_height = 1.5
    thickest_material_thickness = 9 # polymer thickness can have a wild tolerance
    z_clearance_above_top_surface = 3 # relative clearance above stock for safe moves
    z_height_for_rapid_move = z_clearance_above_top_surface + thickest_material_thickness


elif job_name == "Y RACK PARTOFF":

    x_edge_of_stock_from_datum = 505.5
    x_job_start_from_edge_of_job = 20.85
    x_datum = x_edge_of_stock_from_datum + x_job_start_from_edge_of_job   # Job start point - Relative to home corner of stock

    y_datum = 50.0
    x_job_size = 262.15
    y_job_size = 2643.0
    rack_width = 20.5
    number_of_racks = 10
    shoulder_height = 5.0
    thickest_material_thickness = 13 # polymer thickness can have a wild tolerance
    z_clearance_above_top_surface = 3 # relative clearance above stock for safe moves
    z_height_for_rapid_move = z_clearance_above_top_surface + thickest_material_thickness


else: print "Select job name in the code header"


# Header

if job_name == "X RACK PARTOFF":

    lines = ['(' + job_name + ')',
            '(CUTTER: 6.35 ACR FLAT BOTTOM)',
            'G90', #Absolute
            'G94', #Feed units per mm
            'G17', #XY plane
            'G21', #In MM
            'M3 S25000', # Turn on spindle
            'G4 P1' # Allow time for inrush
            ]


elif job_name == "Y RACK PARTOFF":

    lines = ['(' + job_name + ')',
            '(CUSTOM CODE)',
            '(CUTTER: 6.35 ACR FLAT BOTTOM)'
            'G90', #Absolute
            'G94', #Feed units per mm
            'G17', #XY plane
            'G21', #In MM
            'M3 S25000', # Turn on spindle
            'G4 P1' # Allow time for inrush               
            ]

# Cutting variables
cutter_diameter = 6.35
cutter_rad = cutter_diameter/2
xy_feed_rate = 1500 #mm/min
z_feed_rate = 200 #mm/min
z_stepdown = 2
z_final_part_off_depth = -0.5




# Stock variables



# Common end-trench variables

trench_width = 1
trench_excess_x_width = 1
trench_final_z_depth = 1


# Home end trench

trench_y_max =  y_datum - (cutter_diameter/2)
trench_y_min =  trench_y_max - trench_width 

trench_x0 = x_datum  - cutter_rad/2 - trench_excess_x_width # home end
trench_x1 = x_datum  + cutter_rad/2 + trench_excess_x_width + x_job_size
trench_y0 = trench_y_min # home end
trench_y1 = trench_y_max


lines.append("\n(Home end trench)")
lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(trench_x1) + " Y" + str(trench_y0))

z = thickest_material_thickness

while z > trench_final_z_depth:
    
    z -= z_stepdown
    if z < trench_final_z_depth: z = trench_final_z_depth
    lines.append("G1 Z" + str(z) + " F" + str(z_feed_rate))
    lines.append("G1 X" + str(trench_x0) + " F" + str(xy_feed_rate))
    lines.append("G1 Y" + str(trench_y1))
    lines.append("G1 X" + str(trench_x1))
    lines.append("G1 Y" + str(trench_y0))


# Far end trench

trench_y_min =  y_datum + y_job_size + cutter_rad
trench_y_max = trench_y_min + trench_width

trench_x0 = x_datum - cutter_rad/2 - trench_excess_x_width # home end
trench_x1 = x_datum + cutter_rad/2 + trench_excess_x_width + x_job_size
trench_y0 = trench_y_min # home end
trench_y1 = trench_y_max


lines.append("\n(Far end trench)")
lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(trench_x1) + " Y" + str(trench_y1))

z = thickest_material_thickness

while z > trench_final_z_depth:
    
    z -= z_stepdown
    if z < trench_final_z_depth: z = trench_final_z_depth
    lines.append("G1 Z" + str(z) + " F" + str(z_feed_rate))
    lines.append("G1 X" + str(trench_x0) + " F" + str(xy_feed_rate))
    lines.append("G1 Y" + str(trench_y0))
    lines.append("G1 X" + str(trench_x1))
    lines.append("G1 Y" + str(trench_y1))



# Inner part offs

lines.append("\n(Inner long partoffs)")

part_off_overrun = 1
y0_partoff = y_datum - (cutter_diameter/2) - part_off_overrun
y1_partoff = y_datum + y_job_size + (cutter_diameter/2) + part_off_overrun

lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 Y" + str(y1_partoff)) # picking up from last trench point 
y_general_position = "far"
 
 
x_inner_partoff_coord = x_datum + rack_width + (cutter_diameter/2)


while x_inner_partoff_coord < x_datum + x_job_size:
    
    lines.append("G0 Z" + str(z_height_for_rapid_move))
    lines.append("G0 X" + str(x_inner_partoff_coord))

    z = shoulder_height # shoulder height
    
    while z > z_final_part_off_depth:
        
        z -= z_stepdown
        if z < z_final_part_off_depth: z = z_final_part_off_depth        
        lines.append("G1 Z" + str(z) + " F" + str(z_feed_rate))

        if y_general_position == "far":
            lines.append("G1 Y" + str(y0_partoff) + " F" + str(xy_feed_rate))
            y_general_position = "home"

        else:
            lines.append("G1 Y" + str(y1_partoff) + " F" + str(xy_feed_rate))
            y_general_position = "far"

    x_inner_partoff_coord += rack_width + cutter_diameter



# Outer part offs

lines.append("\n(Outer long partoffs)")


x0_partoff = x_datum - (cutter_diameter/2)
x1_partoff = x_datum + x_job_size + (cutter_diameter/2)

lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(x0_partoff) + "Y" + str(y1_partoff)) # picking up from last trench point 

z = thickest_material_thickness # shoulder height

while z > z_final_part_off_depth:
    
    z -= z_stepdown
    if z < z_final_part_off_depth: z = z_final_part_off_depth        

    lines.append("G1 Z" + str(z) + " F" + str(z_feed_rate))
    lines.append("G1 Y" + str(y0_partoff) + " F" + str(xy_feed_rate))
    lines.append("G0 Z" + str(z_height_for_rapid_move))
    lines.append("G0 X" + str(x1_partoff))    

    lines.append("G1 Z" + str(z) + " F" + str(z_feed_rate))
    lines.append("G1 Y" + str(y1_partoff) + " F" + str(xy_feed_rate))
    lines.append("G0 Z" + str(z_height_for_rapid_move))
    lines.append("G0 X" + str(x0_partoff))    

lines.append("G1 Z" + str(z) + " F" + str(z_feed_rate))



# END
lines.append("\n(Shutdown)")
lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("M5") #Kill spindle
lines.append("G4 P2") #Pause for vac overrun
lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
f = open(job_name + ".nc", "w")
for line in lines:
    f.write(line + "\n")   

print "Done: " + job_name
