# Generates gcode to create gcode paths to cut shapes
# Parameter illustrations:
# https://docs.google.com/presentation/d/1Y2u2M5wsdi023Vq9FB5F46MBVZMq2P3gxesHQzb4RQw/edit#slide=id.p

################################
# Z-DATUM:                     #
# Top surface of material   #
################################


import math

###### INTERNAL APP SETTINGS

z_height_for_rapid_move = 3 # relative clearance above stock for safe moves


###### USER INPUTS

# MODE
shape = "rectangle"
# shape = "circle"
aperture_or_island = "island"
# aperture_or_island = "aperture"

# TAB PARAMS
tabs = True
tab_height = 4
tab_width = 6
tab_distance = 40

# RECTANGLE PARAMETERS
rect_job_x = 300
rect_job_y = 300
rect_job_rad = 12

# CIRCLE PARAMS
circ_input_diameter = 80

# TOOL
cutter_diameter = 6.35
cutter_rad = cutter_diameter/2

# FEEDS AND SPEEDS
xy_feed_rate = 2500 #mm/min
plunge_feed_rate = 1000 #mm/min
spindle_speed = 25000 #rpm   # if available

# STRATEGY
material_thickness = 12
stock_bottom_offset = 1
stepdown = 3
finishing_pass = 2


# GLOBAL JOB CALCULATIONS

job_name = shape + " " + aperture_or_island
tab_absolute_height = -(material_thickness - tab_height)
tab_effective_width = cutter_diameter + tab_width
z_max = - material_thickness - stock_bottom_offset


# RECTANGLE PARAMS

if shape == "rectangle":

    if aperture_or_island == "aperture":
        # rectangle hack to save a bunch of logic to exclude rads for r0 case: 
        # rad will still be included but so small they won't be noticed visually.
        if rect_job_rad <= cutter_rad: rect_job_rad = cutter_rad + 0.01
        rect_path_rad = rect_job_rad - cutter_rad
        x_min = 0 + cutter_rad
        y_min = 0 + cutter_rad
        x_max = rect_job_x - cutter_rad
        y_max = rect_job_y - cutter_rad
        
    elif aperture_or_island == "island":
        if rect_job_rad == 0: rect_job_rad =  0.01
        rect_path_rad = rect_job_rad + cutter_rad
        x_min = 0 - cutter_rad
        y_min = 0 - cutter_rad
        x_max = rect_job_x + cutter_rad
        y_max = rect_job_y + cutter_rad

    # flat endpoints
    x_flat_min = rect_job_rad
    x_flat_max = rect_job_x - rect_job_rad
    y_flat_min = rect_job_rad
    y_flat_max = rect_job_y - rect_job_rad
    
    # tabs
    
    if tabs:
        
        rect_tab_offset_from_origin = cutter_rad # so tab doesn't start near the flat end point (potential errors with r0 hack
        
        # tab start point containers
        x_out_tabs = []
        x_rtn_tabs = []
        y_out_tabs = []
        y_rtn_tabs = []    
        
        # x-out
        x = x_flat_min + cutter_rad
        while x < (x_flat_max - cutter_rad - tab_effective_width):
            x_out_tabs.append(x) 
            x += tab_distance
    
        # x-rtn
        x = x_flat_max - cutter_rad
        while x > (x_flat_min + cutter_rad + tab_effective_width):
            x_rtn_tabs.append(x) 
            x -= tab_distance
    
        # y-out
        y = y_flat_min + cutter_rad
        while y < (y_flat_max - cutter_rad - tab_effective_width):
            y_out_tabs.append(y) 
            y += tab_distance
    
        # y-rtn
        y = y_flat_max - cutter_rad
        while y > (y_flat_min + cutter_rad + tab_effective_width):
            y_rtn_tabs.append(y) 
            y -= tab_distance
    
        print "Number of tabs in X axis: " + str(len(x_out_tabs))
        print "Number of tabs in Y axis: " + str(len(y_out_tabs))

    else:
        print "No tabs"

# CIRCLE PARAMS

elif shape == "circle":
    
    if aperture_or_island == "aperture":
        circ_path_rad = (circ_input_diameter - cutter_diameter) / 2
        
    elif aperture_or_island == "island":
        circ_path_rad = (circ_input_diameter + cutter_diameter) / 2

    if tabs:
        
        # calculate an even distribution of tabs along the circumference, based on desired distance between each (round down the distance between tabs as needed to achieve even distribution)
        # working in rads here
        
        total_circumference = 2.0 * math.pi * circ_path_rad
        circ_tabs_qty = math.ceil(total_circumference / tab_distance) #round down
        circ_angle_between_tabs = (2.0 * math.pi) / circ_tabs_qty
        circ_angle_across_tab = (tab_effective_width / total_circumference) * (2.0 * math.pi)

#         print total_circumference, circ_tabs_qty, circ_angle_between_tabs, circ_angle_across_tab, circ_path_rad, math.degrees(circ_angle_across_tab)

        circ_tab_start_pos = []
        circ_tab_end_pos = []

        
        circ_tab_start_angle = 0

        while circ_tab_start_angle < (round(2 * math.pi,6)):
            
            # start co-ords
            x = circ_path_rad * math.cos(circ_tab_start_angle)
            y = circ_path_rad * math.sin(circ_tab_start_angle)
            circ_tab_start_pos.append([round(x,6),round(y,6)])
            
            # end co-ords
            circ_tab_end_angle = circ_tab_start_angle + circ_angle_across_tab
            x = circ_path_rad * math.cos(circ_tab_end_angle)
            y = circ_path_rad * math.sin(circ_tab_end_angle)
            circ_tab_end_pos.append([round(x,6),round(y,6)])

            print str(2*math.pi) + ":   " + str(circ_tab_start_angle)
                        
            circ_tab_start_angle += circ_angle_between_tabs
            
            
        circ_tab_next_start_pos = circ_tab_start_pos[1:] + circ_tab_start_pos[:1] # simple way to rotate a list

        print "Tab qty: " + str(circ_tabs_qty)
        print circ_tab_start_pos

################ GCODE GENERATOR ###############

######## GCODE HEADER

lines = ['(' + job_name + ')',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'M3 S25000', # Turn on spindle
        'G4 P1', # Allow time for inrush
        'G91.1' # relative rad centre definitions. IMPORTANT: "G90.1" (absolute rad centre definitions) DOESN'T WORK IN GRBL
        ]


###### GCODE SHAPE

# Start pos

lines.append("\n(Start of shape)")

if shape == "rectangle":
    lines.append("G0 X" + str(x_flat_min) + " Y" + str(y_min))

elif shape == "circle":
    lines.append("G0 X" + str(circ_path_rad) + " Y" + str(0))

lines.append("G0 Z" + str(z_height_for_rapid_move))


z = -stepdown

while z >= z_max:
    
    if shape == "rectangle":
        
        
        # plunge and draw square, anti-clockwise
        lines.append("G1 Z" + str(z) + " F" + str(plunge_feed_rate))
        
        # x-out
        if tabs and z < tab_absolute_height:
            for start_tab_coord in x_out_tabs:
                lines.append("G1 X" + str(start_tab_coord) + " F" + str(xy_feed_rate))
                lines.append("G1 Z" + str(tab_absolute_height) + " F" + str(plunge_feed_rate))
                lines.append("G1 X" + str(start_tab_coord + tab_effective_width) + " F" + str(xy_feed_rate))
                lines.append("G1 Z" + str(z) + " F" + str(plunge_feed_rate))
        lines.append("G1 X" + str(x_flat_max) + " Y" + str(y_min) + " F" + str(xy_feed_rate))
        
        # rad 1
        lines.append("G3 X" + str(x_max) + " Y" + str(y_flat_min) + " I" + str(0) +  " J" + str(rect_path_rad))
        
        # y-out
        if tabs and z < tab_absolute_height:
            for start_tab_coord in y_out_tabs:
                lines.append("G1 Y" + str(start_tab_coord) + " F" + str(xy_feed_rate))
                lines.append("G1 Z" + str(tab_absolute_height) + " F" + str(plunge_feed_rate))
                lines.append("G1 Y" + str(start_tab_coord + tab_effective_width) + " F" + str(xy_feed_rate))
                lines.append("G1 Z" + str(z) + " F" + str(plunge_feed_rate))
        lines.append("G1 X" + str(x_max) + " Y" + str(y_flat_max) + " F" + str(xy_feed_rate))
        
        # rad 2
        lines.append("G3 X" + str(x_flat_max) + " Y" + str(y_max) + " I" + str(-rect_path_rad) +  " J" + str(0))
        
        # x-rtn
        if tabs and z < tab_absolute_height:
            for start_tab_coord in x_rtn_tabs:
                lines.append("G1 X" + str(start_tab_coord) + " F" + str(xy_feed_rate))
                lines.append("G1 Z" + str(tab_absolute_height) + " F" + str(plunge_feed_rate))
                lines.append("G1 X" + str(start_tab_coord - tab_effective_width) + " F" + str(xy_feed_rate))
                lines.append("G1 Z" + str(z) + " F" + str(plunge_feed_rate))
        lines.append("G1 X" + str(x_flat_min) + " Y" + str(y_max) + " F" + str(xy_feed_rate))
        
        # rad 3
        lines.append("G3 X" + str(x_min) + " Y" + str(y_flat_max) + " I" + str(0) +  " J" + str(-rect_path_rad))
        
        # y-rtn
        if tabs and z < tab_absolute_height:
            for start_tab_coord in y_rtn_tabs:
                lines.append("G1 Y" + str(start_tab_coord) + " F" + str(xy_feed_rate))
                lines.append("G1 Z" + str(tab_absolute_height) + " F" + str(plunge_feed_rate))
                lines.append("G1 Y" + str(start_tab_coord - tab_effective_width) + " F" + str(xy_feed_rate))
                lines.append("G1 Z" + str(z) + " F" + str(plunge_feed_rate))
        lines.append("G1 X" + str(x_min) + " Y" + str(y_flat_min) + " F" + str(xy_feed_rate))
        
        # rad 4
        lines.append("G3 X" + str(x_flat_min) + " Y" + str(y_min) + " I" + str(rect_path_rad) +  " J" + str(0))

        

    elif shape == "circle":
        

        # plunge and draw circle, anti-clockwise
        lines.append("G1 Z" + str(z) + " F" + str(plunge_feed_rate))
        if tabs and z < tab_absolute_height:
            tab_count = 0
            for (xy_start, xy_end, xy_next) in zip(circ_tab_start_pos, circ_tab_end_pos, circ_tab_next_start_pos):
                                
                tab_count += 1
                
                lines.append("(Z" + str(z) + ": Tab " + str(tab_count) + ")")
#                 if xy_start[0] != circ_path_rad: # hack to prevent repetition of co-ordinates from triggering a 360 degree revolution (makes sure that x co-ords aren't the same before appending - only works in this template with start point position etc)
#                     lines.append("G3 X" + str(xy_start[0]) + " Y" + str(xy_start[1]) + " I" + str(-xy_start[0]) + " J" + str(-xy_start[1]) + " F" + str(xy_feed_rate))
                lines.append("G1 Z" + str(tab_absolute_height) + " F" + str(plunge_feed_rate))
                lines.append("G3 X" + str(xy_end[0]) + " Y" + str(xy_end[1]) + " I" + str(-xy_start[0]) + "J" + str(-xy_start[1]) + " F" + str(xy_feed_rate))
                lines.append("G1 Z" + str(z) + " F" + str(plunge_feed_rate))
                lines.append("G3 X" + str(xy_next[0]) + " Y" + str(xy_next[1]) + " I" + str(-xy_end[0]) + " J" + str(-xy_end[1]) + " F" + str(xy_feed_rate))
          
        else:
            lines.append("G3 X" + str(circ_path_rad) + " Y0 I" + str(-circ_path_rad) + " J0 F" + str(xy_feed_rate))

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
