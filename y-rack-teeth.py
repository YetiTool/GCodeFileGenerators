# Cuts teeth into stock to create Y rack
# Z-DATUM: Top surface of material

lines = ['(T1 CUSTOM TOOTH CUTTER)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'G1 Z10 F1000', #Ugly, but sets feed rate (can we do F on it's own etc?)
        'G0 X0 Y0',
        'G4 P1', # Pause, for second thoughts
        'M3 S25000', # Turn on spindle
        'G4 P2' # Allow time to spin up to speed
        ]

# DEFINE LIMITS
y_start = 0
y_instances = 275
y_increment = 4.712388

z_start = -1
z_end = -3.38
z_increment = 1
z_safe = 2

x_start = 0.5
x_end = 19.5


# POPULATE GRID
y_grid = []
y_count = 0
y = y_start
while y_count < y_instances:
    y_grid.append(y)
    y += y_increment
    y_count += 1
print y_grid    

z_grid = []
z = z_start
while z > z_end:
    z_grid.append(z)
    z -= z_increment
z_grid.append(z_end)
print z_grid    

for y in y_grid:
    for z in z_grid:
        lines.append("G1 X" + str(x_start) + " Y" + str(y)) #Go to XY start
        lines.append("Z" + str(z)) #Dive to z depth
        lines.append("G1 X" + str(x_end)) #Cut tooth width
        lines.append("Z" + str(z_safe)) #Lift

lines.append("M5") #Kill spindle
lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
f = open("y_rack_teeth.nc", "w")
for line in lines:
    f.write(line + "\n")   

