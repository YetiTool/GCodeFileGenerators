# Turns spindle on and off at an equally spaced mesh of XYZ co-ordinates within a defined volume
# commit test 1

lines = ['(T1  NO TOOL NEEDED)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21' #In MM
        ]

lines.append('G1 X0 Y0 Z-1 F3000') #Ugly, but sets feed rate (can we do F on it's own etc?)

# INPUTS: Grid settings 
x_start = 0
x_end = 1250
x_increment = 50

z_start = -140
z_end = -1
z_increment = 20


# POPULATE GRID
x_grid = []
x = x_start
while x < x_end:
    x_grid.append(x)
    x += x_increment
x_grid.append(x_end)
print x_grid    

z_grid = []
z = z_start
while z < z_end:
    z_grid.append(z)
    z += z_increment
z_grid.append(z_end)
print z_grid    

count = 0 
for x in x_grid:
    for z in z_grid:
        lines.append("G1 X" + str(x) + " Z" + str(z)) #Go to next co-ord
        lines.append("M3 S25000") #Spindle on
        lines.append("G4 P0.5") #Wait (to ensure full speed)
        lines.append("M5") #Kill spindle
        lines.append("G4 P4") #Wait (to ensure full speed)

        count += 1

lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
print count
f = open("QC_spindle_endurance_xz.nc", "w")
for line in lines:
    f.write(line + "\n")   

