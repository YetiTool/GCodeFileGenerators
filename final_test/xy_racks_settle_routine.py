# Moves about in X & Y backwards and forwards to bed the racks into their slots


lines = ['(T1 SPINDLE ONLY, NO ROUTER CUTTER)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'G0 X0 Y0 Z-130', #Goto XY datum, put spindle at point of lowest moment
        'G4 P1' # Pause, for second thoughts
        ]


# DEFINE X GRID
x_start = 0
x_end = 1280
x_increment = 2
x_ramp_distance = 20

x_count = 0

x_grid = []
x = x_start
while x < x_end:
    x_grid.append(x)
    x = x + x_increment
    x_count += 1
   
    
# DEFINE Y GRID
y_start = 0
y_end = 2480.0
y_ramp_distance = 20
y_increment = 2

y_count = 0
y_grid = []
y = y_start
while y < y_end:
    y_grid.append(y)
    y = y + y_increment
    y_count += 1


lines.append("\n(X shuffle)\n") #Go to X end

i = 0 
while i < x_count:
    lines.append("G0 X" + str(x_grid[i] + x_ramp_distance)) #Go to X end
    lines.append("G0 X" + str(x_grid[i] + x_increment)) #Go to X start + increment
    i += 1

lines.append("\n(Beam mass centre)\n") #Go to X end

lines.append('G0 X900') #Put z head head in position where X beam CoG is mid plane of machine

lines.append("\n(Y shuffle)\n") #Go to X end

i = 0 
while i < y_count:
    lines.append("G0 Y" + str(y_grid[i] + y_ramp_distance)) #Go to X end
    lines.append("G0 Y" + str(y_grid[i] + y_increment)) #Go to X start + increment
    i += 1

lines.append("M30") #Prog end
  
f = open("Final test OP1 (XY rack wear in).nc", "w")
for line in lines:
    f.write(line + "\n")   

print "File done"