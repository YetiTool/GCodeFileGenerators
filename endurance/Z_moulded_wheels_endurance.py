# Moves Z axis up and down along the length of axis, and returns. And repeats
# Z-DATUM: Top surface of material

#     fast_z_speed = 750


lines = ['(T1 SPINDLE ONLY, NO ROUTER CUTTER)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'G0 X0 Y0'
        ]

# CYCLES
cycles_to_test = 1000

# DEFINE Z GRID
z_start = 1.000
z_end = 148.000

lines_count = 0

while lines_count < cycles_to_test:
	lines.append("G0 Z"+str(z_end)) #Go to bottom
	lines.append("G0 Z"+str(z_start)) #Go to top
	lines_count += 1
  
lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
print "Lines: " + str(lines_count)
  
f = open("Z_moulded_wheels_endurance.nc", "w")
for line in lines:
	f.write(line + "\n")   

print "File done."
