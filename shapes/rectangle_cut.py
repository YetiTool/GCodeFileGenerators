# Generates gcode to create rectangular cut

################################
# Z-DATUM:                     #
# Top surface of material   #
################################

###### INTERNAL APP SETTINGS

z_height_for_rapid_move = 3 # relative clearance above stock for safe moves


###### USER INPUTS

# shape = "rectangle"
shape = "circle"
aperture_or_island = "island"
# aperture_or_island = "aperture"

rect_job_x = 100
rect_job_y = 100
circ_input_diameter = 100
job_z = 10
rect_job_rad = 20


cutter_diameter = 8
cutter_rad = cutter_diameter/2

xy_feed_rate = 1500 #mm/min
z_feed_rate = 200 #mm/min
spindle_speed = 25000 #rpm

stepdown = 2
finishing_pass = 1
stock_bottom_offset = 1


# Job calculations

job_name = shape + " " + aperture_or_island

z_min = 0

if aperture_or_island == "aperture":

    if shape == "rectangle":

        # rectangle hack to save a bunch of logic to exclude rads for r0 case: 
        # rad will still be included but so small they won't be noticed.
        if rect_job_rad <= cutter_rad: rect_job_rad = cutter_rad + 0.01
        rect_path_rad = rect_job_rad - cutter_rad
    
        # rectangle
        x_min = 0 + cutter_rad
        y_min = 0 + cutter_rad
        x_max = rect_job_x - cutter_rad
        y_max = rect_job_y - cutter_rad

    elif shape == "circle":
        circ_path_rad = (circ_input_diameter - cutter_diameter) / 2

elif aperture_or_island == "island":

    if shape == "rectangle":

        # rectangle hack to save a bunch of logic to exclude rads for r0 case: 
        # rad will still be included but so small they won't be noticed.
        if rect_job_rad == 0: rect_job_rad =  0.01
        rect_path_rad = rect_job_rad + cutter_rad
        
        # rectangle
        x_min = 0 - cutter_rad
        y_min = 0 - cutter_rad
        x_max = rect_job_x + cutter_rad
        y_max = rect_job_y + cutter_rad

    elif shape == "circle":
        circ_path_rad = (circ_input_diameter + cutter_diameter) / 2

else:
    print "Debug: Aperture or island input not detected"

# rectangle
x_flat_min = rect_job_rad
x_flat_max = rect_job_x - rect_job_rad
y_flat_min = rect_job_rad
y_flat_max = rect_job_y - rect_job_rad
z_max = - job_z - stock_bottom_offset


################ GCODE GENERATOR ###############

######## GCODE HEADER

lines = ['(' + job_name + ')',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'M3 S25000', # Turn on spindle
        'G4 P1' # Allow time for inrush
        ]


###### GCODE SHAPE

# Start pos

lines.append("\n(Start of shape)")

if shape == "rectangle":
    lines.append("G0 X" + str(x_flat_min) + " Y" + str(y_min))
elif shape == "circle":
    lines.append("G0 X" + str(0) + " Y" + str(-circ_path_rad))

lines.append("G0 Z" + str(z_height_for_rapid_move))


z = -stepdown

while z >= z_max:
    
    if shape == "rectangle":
        # plunge and draw square, anti-clockwise
        lines.append("G1 Z" + str(z) + " F" + str(z_feed_rate))
        lines.append("G1 X" + str(x_flat_max) + " Y" + str(y_min) + " F" + str(xy_feed_rate))
        lines.append("G3 X" + str(x_max) + " Y" + str(y_flat_min) + " I" + str(0) +  " J" + str(rect_path_rad))
        lines.append("G1 X" + str(x_max) + " Y" + str(y_flat_max))
        lines.append("G3 X" + str(x_flat_max) + " Y" + str(y_max) + " I" + str(-rect_path_rad) +  " J" + str(0))
        lines.append("G1 X" + str(x_flat_min) + " Y" + str(y_max))
        lines.append("G3 X" + str(x_min) + " Y" + str(y_flat_max) + " I" + str(0) +  " J" + str(-rect_path_rad))
        lines.append("G1 X" + str(x_min) + " Y" + str(y_flat_min))
        lines.append("G3 X" + str(x_flat_min) + " Y" + str(y_min) + " I" + str(rect_path_rad) +  " J" + str(0))


    elif shape == "circle":
        # plunge and draw circle, anti-clockwise
        lines.append("G1 Z" + str(z) + " F" + str(z_feed_rate))
        lines.append("G3 X" + str(0) + " Y" + str(-circ_path_rad) + " I" + str(0) +  " J" + str(circ_path_rad))

    # assess if final_pass
    if z == z_max and finishing_pass <= 0: break
    if z == z_max and finishing_pass > 0: finishing_pass -= 1

    # increment z down for next pass
    z -= stepdown
    if z < z_max: z = z_max
    

######## GCODE FOOTER

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
