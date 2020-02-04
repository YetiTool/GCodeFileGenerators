# Generates gcode to create rectangular cut

################################
# Z-DATUM:                     #
# Top surface of material   #
################################

###### SETTINGS

z_height_for_rapid_move = 3 # relative clearance above stock for safe moves


###### INPUTS

job_name = "Rectangular cut"

inset_or_outset = "inset"

job_x = 100
job_y = 100
job_z = 10
job_corner_rad = 0


cutter_diameter = 6.35
cutter_rad = cutter_diameter/2

xy_feed_rate = 1500 #mm/min
z_feed_rate = 200 #mm/min
spindle_speed = 25000 #rpm

stepdown = 2
finishing_pass = 1
stock_bottom_offset = 1

# Job numbers

x_min = 0
y_min = 0
z_min = 0

if inset_or_outset == "inset":
    x_max = job_x - cutter_diameter
    y_max = job_y - cutter_diameter

else:
    x_max = job_x + cutter_diameter
    y_max = job_y + cutter_diameter

z_max = - job_z - stock_bottom_offset

# Header

lines = ['(' + job_name + ')',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'M3 S25000', # Turn on spindle
        'G4 P1' # Allow time for inrush
        ]


lines.append("\n(Start of shape)")
lines.append("G0 X" + str(x_min) + " Y" + str(y_min))
lines.append("G0 Z" + str(z_height_for_rapid_move))

z = -stepdown

while z >= z_max:
    
    # plunge and draw square
    lines.append("G1 Z" + str(z) + " F" + str(z_feed_rate))
    lines.append("G1 X" + str(x_max) + " Y" + str(y_min) + " F" + str(xy_feed_rate))
    lines.append("G1 X" + str(x_max) + " Y" + str(y_max) + " F" + str(xy_feed_rate))
    lines.append("G1 X" + str(x_min) + " Y" + str(y_max) + " F" + str(xy_feed_rate))
    lines.append("G1 X" + str(x_min) + " Y" + str(y_min) + " F" + str(xy_feed_rate))
    
    # assess if final_pass
    if z == z_max and finishing_pass <= 0: break
    if z == z_max and finishing_pass > 0: finishing_pass -= 1

    # increment z down for next pass
    z -= stepdown
    if z < z_max: z = z_max
    
lines.append("G0 Z" + str(z_height_for_rapid_move))

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
