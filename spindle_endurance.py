# Turns spindle on and off at an equally spaced mesh of XYZ co-ordinates within a defined volume

lines = ['(T1  NO TOOL NEEDED)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21' #In MM
        ]

lines.append('G1 X0 Y0 Z-1 F3000') #Ugly, but sets feed rate (can we do F on it's own etc?)

# INPUTS: Grid settings 
x_start = 0
x_end = 1100
x_increment = 80

y_start = 0
y_end = 2400
y_increment = 200

z_start = -135
z_end = -1
z_increment = 10


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

z_grid = []
z = z_start
while z < z_end:
    z_grid.append(z)
    z += z_increment
z_grid.append(z_end)
print z_grid    

count = 0 
for y in y_grid:
    for x in x_grid:
        for z in z_grid:
            lines.append("M3 S25000") #Spindle on
            lines.append("G1 X" + str(x) + " Y" + str(y) + " Z" + str(z)) #Go to next co-ord
            lines.append("G4 P1") #Wait (to ensure full speed)
            lines.append("M5") #Kill spindle
            lines.append("G4 P8") #Allow spindle to stop 
            count += 1

lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
print count
f = open("spindle_endurance.nc", "w")
for line in lines:
    f.write(line + "\n")   

