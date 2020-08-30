# Moves about in X & Y backwards and forwards to bed the racks into their slots


# DEFINE X AXIS TEST
x_start = 1
x_end = 1296
x_increment = 30
x_ramp_distance = x_increment + 50
total_cycles = 200


# X +ve test
x_count = 0
x_grid = []
x = x_start
while x + x_ramp_distance < x_end:
    x_grid.append(x)
    x = x + x_increment
    x_count += 1

   
lines = ['(T1 SPINDLE ONLY, NO ROUTER CUTTER)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'G4 P1' # Pause, for second thoughts
        ]

lines.append("\n(X shuffle)\n") #Go to X end

n = 0
while n < total_cycles:
    i = 0 
    lines.append("G0 X" + str(x_grid[i])) #Go to X end
    
    while i < x_count:
        lines.append("G0 X" + str(x_grid[i] + x_ramp_distance)) #Go to X end
        lines.append("G0 X" + str(x_grid[i] + x_increment)) #Go to X start + increment
        i += 1
    
    n += 1

lines.append("M30") #Prog end
  
f = open("X+ axis load test.nc", "w")
for line in lines:
    f.write(line + "\n")   

print "X+ File done"


# X -ve test
x_count = 0
x_grid = []
x = x_end
while x - x_ramp_distance > x_start:
    x_grid.append(x)
    x = x - x_increment
    x_count += 1

   
lines = ['(T1 SPINDLE ONLY, NO ROUTER CUTTER)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'G4 P1' # Pause, for second thoughts
        ]

lines.append("\n(X shuffle)\n") #Go to X end

n = 0
while n < total_cycles:
    i = 0 
    lines.append("G0 X" + str(x_grid[i])) #Go to X end
    
    while i < x_count:
        lines.append("G0 X" + str(x_grid[i] - x_ramp_distance)) #Go to X end
        lines.append("G0 X" + str(x_grid[i] - x_increment)) #Go to X start + increment
        i += 1
    n += 1

lines.append("M30") #Prog end
  
f = open("X- axis load test.nc", "w")
for line in lines:
    f.write(line + "\n")   

print "X- File done"



