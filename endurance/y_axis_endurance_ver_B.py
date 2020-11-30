# Moves X axes backwards and forwards along length of axis, and returns. And repeats
# Z-DATUM: Top surface of material

#     fast_x_speed = 6000
#     fast_y_speed = 6000
#     fast_z_speed = 750


lines = ['(T1 SPINDLE ONLY, NO ROUTER CUTTER)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'G4 P1' # Pause, for second thoughts
        ]

# CYCLES
cycles_to_test = 1000

# DEFINE X GRID
y_start = 0.000
y_end = 2400.000

# Comms intensity
# The smaller the value, the higher the intensity of communications. 
# However, too small and the look ahead buffer will not be able to move the axis quickly

data_loading_increment = y_end
round_trip_count = 0
lines_count = 0

while round_trip_count < cycles_to_test:
    
    y = y_start
    
    while y < y_end:

        lines.append("G0 Y" + str(y)) #Go to next co-ord
        lines_count += 1
        y += data_loading_increment
        
    while y > y_start:

        lines.append("G0 Y" + str(y)) #Go to next co-ord
        lines_count += 1
        y -= data_loading_increment
        
    round_trip_count += 1



lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
print "Lines: " + str(lines_count)
  
f = open("QC_y_axis_endurance_ver_B.nc", "w")
for line in lines:
    f.write(line + "\n")   

print "File done."