# Moves X Y Z along lengths of axes at fast speed
# Z-DATUM: Top of axis

#     fast_x_speed = 6000
#     fast_y_speed = 6000
#     fast_z_speed = 750

lines = ['(T1 SPINDLE ONLY, NO ROUTER CUTTER)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'G1 Z-1 F1000', #Ugly, but sets feed rate (can we do F on it's own etc?)
        'G0 X0 Y0',
        'M3 S25000',
        'G4 P1' # Pause, for second thoughts
        ]

# DEFINE X GRID
x_start = 0
x_end = 1295.0

y_start = 0
y_end = 2495.0

z_start = 0
z_end = -147.0

cycles = 240

n = 0
while n < cycles:
    lines.append("G0 X" + str(x_start)) #Go to X end
    lines.append("G0 Y" + str(y_start)) #Go to X start + increment
    lines.append("G0 Z" + str(z_start)) #Go to X end
    lines.append("G0 X" + str(x_end)) #Go to X start + increment
    lines.append("G0 Y" + str(y_end)) #Go to X end
    lines.append("G0 Z" + str(z_end)) #Go to X start + increment
    
    n += 1
    
lines.append("AF") #Kill spindle
lines.append("M5") #Kill spindle
lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
f = open("xyz_endurance_speed.nc", "w")
for line in lines:
    f.write(line + "\n")   

print "File done"