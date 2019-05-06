# Cuts teeth into stock to create Y rack

################################
# Z-DATUM:                     #
# Bottom surface of material   #
################################

# Cutting variables
xy_feed_rate = 1000 #mm/min
z_feed_rate = 400 #mm/min
z_cut_depth_per_pass = 1.5

# Job variables
thickest_material_thickness = 13.5 # polymer thickness can have a wild tolerance
z_end = 8.62 # height of tooth depth, measured from bottom surface
y_start = 0
valleys_to_cut = 274 # number of valleys to cut
y_increment = 4.712388 # distance between teeth
x_start = 0.5
x_end = 19.5

# Safety
z_clearance_above_top_surface = 1 # relative clearance above stock for safe moves
z_clearance_above_last_cut = 1 # relative clearance above last cut for next  moves
z_clearance_on_cut_approach = 0.25 # as we get very near the material, we need to be at cutting feed for

# Implications
z_height_above_stock = z_clearance_above_top_surface + thickest_material_thickness
z_start = thickest_material_thickness - z_cut_depth_per_pass

# Header
lines = ['(T1 CUSTOM TOOTH CUTTER)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'G0 Z0',
        'G0 X0 Y0', #Got to XY datum
        'G0 Z' + str(z_height_above_stock), #Approach material
        'M3 S25000', # Turn on spindle
        'G4 P2' # Allow time to spin up to speed
        ]

# POPULATE GRID
y_grid = []
y_count = 0
y = y_start
while y_count < valleys_to_cut:
    y_grid.append(y)
    y += y_increment
    y_count += 1
print y_grid    

z_grid = []
z = z_start
while z > z_end:
    z_grid.append(z)
    z -= z_cut_depth_per_pass
z_grid.append(z_end)
print z_grid    

for y in y_grid:
    for z in z_grid:
        lines.append("G0 X" + str(x_start) + " Y" + str(y)) #Go to XY start
        lines.append("G0 Z" + str(z + z_cut_depth_per_pass + z_clearance_on_cut_approach)) #Dive to just above material
        lines.append("G1 Z" + str(z) + " F" + str(z_feed_rate)) #Feed dive to z depth
        lines.append("G1 X" + str(x_end) + " F" + str(xy_feed_rate)) #Feed cut face width of tooth
        lines.append("G1 Z" + str(z + z_clearance_on_cut_approach) + " F" + str(z_feed_rate)) #Lift off material surface slowly
        lines.append("G0 Z" + str(z + z_clearance_above_last_cut)) #Lift to safe distance above last cut
    lines.append("G0 Z" + str(z_height_above_stock)) #Lift to clear stock, so we can increment in y

lines.append("M5") #Kill spindle
lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
f = open("y_rack_teeth_home.nc", "w")
for line in lines:
    f.write(line + "\n")   

