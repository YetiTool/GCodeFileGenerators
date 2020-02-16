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
        'G0 X0 Y0 Z0',
        'G4 P1' # Pause, for second thoughts
        ]


# DEFINE X GRID
x_start = 0
x_end = 1240
x_retract = 10
x_ramp_distance = 20

n = 0
while n < 500:
    x=0    
    while x + x_ramp_distance <= x_end:
        x += x_ramp_distance
        lines.append("G0 X" + str(x)) #Go to X end
        x -= x_retract
        lines.append("G0 X" + str(x)) #Go to X start + increment
    while x - x_ramp_distance >= x_start:
        x -= x_ramp_distance
        lines.append("G0 X" + str(x)) #Go to X end
        x += x_retract
        lines.append("G0 X" + str(x)) #Go to X start + increment

    
    n += 1


lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
f = open("x_loom_endurance.nc", "w")
for line in lines:
    f.write(line + "\n")   

print "File done"