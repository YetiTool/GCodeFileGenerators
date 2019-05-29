# Blast with list of very short movements - this exhausts serial and line buffers as grbl consumes the lines. Effectively the machine would be reaching the destinations faster than the processing rate for a gcode command. At that point, line buffer would be empty and the character buffer would be only getting filled as fast as EasyCut can fill. This sets the stage for the stress test.
# 
# At point of exhaustion, call circle command.
# This requires:
# Grbl calculations
# Motor firings
# And while the move is being executed, the line and serial buffer will still be being filled at maximum rate. Eventually the few lines of GCode which define the circle will cause a log jam in the line buffer, so the line buffer will cease to fill rapidly.


# INPUTS: Grid settings 
x_start = 10
x_end = 150
# x_end = 1100
x_increment = 2

y_start = 10
y_end = 150
# y_end = 2400
y_increment = 10


lines = ['(T1  NO TOOL NEEDED)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'G1 Z-10 F10000',
        'G0 X0 Y0' 
        ]

# POPULATE GRID
x_grid = []
x = x_start
while x < x_end:
    x_grid.append(x)
    x += x_increment
x_grid.append(x_end)
print x_grid    

y_grid = []
y = y_start
while y < y_end:
    y_grid.append(y)
    y += y_increment
y_grid.append(y_end)
print y_grid    

x_pos= 5
x_nudge = 0.002

circle_radius = 3.0

count = 0 
for y_target in y_grid:

    lines.append("G0 X" + str(x_start) + " Y" + str(y_target)) #Go to next co-ord

    for x_target in x_grid:
        while x_pos < x_target:
            lines.append("X" + str(x_pos))
            x_pos = x_pos + x_nudge
        x_pos = x_target
        lines.append("X" + str(x_pos))
        lines.append("G2 X" + str(x_pos) + "Y"+ str(y_target) + "I" + str(circle_radius) + "J0")
        lines.append("G0")

        count += 1
           


lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
print count
f = open("endurance_circles.nc", "w")
for line in lines:
    f.write(line + "\n")   

