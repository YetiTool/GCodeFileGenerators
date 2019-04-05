# Moves about in X Y Z in a "lets break the mechanics" kinda way
# Z-DATUM: Top surface of material

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
        'G4 P1' # Pause, for second thoughts
        ]


# DEFINE X GRID
x_start = 0
x_end = 1240
x_increment = 0.5
x_ramp_distance = 10

x_count = 0

x_grid = []
x = x_start
while x < x_end - x_ramp_distance:
    x_grid.append(x)
    x = x + x_increment
    x_count += 1
   
    
# DEFINE Y GRID
y_start = 0
y_end = 2450.0
y_ramp_distance = 10
y_increment = (y_end - y_ramp_distance) / x_count

y_count = 0
y_grid = []
y = y_start
while y < y_end - y_ramp_distance:
    y_grid.append(y)
    y = y + y_increment
    y_count += 1


# DEFINE Z GRID
z_start = 0
z_end = 120.0
z_ramp_distance = 3
z_increment = (z_end - z_ramp_distance) / x_count

z_count = 0
z_grid = []
z = z_start
while z < z_end - z_ramp_distance:
    z_grid.append(z)
    z = z + z_increment
    z_count += 1

n = 0
while n < 10:
    i=0    
    while i < x_count:
        lines.append("G0 X" + str(x_grid[i] + x_ramp_distance)) #Go to X end
        lines.append("G0 X" + str(x_grid[i] + x_increment)) #Go to X start + increment
        lines.append("G0 Y" + str(y_grid[i] + y_ramp_distance)) #Go to X end
        lines.append("G0 Y" + str(y_grid[i] + y_increment)) #Go to X start + increment
        lines.append("G0 Z" + str(-(z_grid[i] + z_ramp_distance))) #Go to X end
        lines.append("G0 Z" + str(-(z_grid[i] + z_increment))) #Go to X start + increment
        i += 1
    n += 1


lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
f = open("xyz_endurance.nc", "w")
for line in lines:
    f.write(line + "\n")   

print "File done"