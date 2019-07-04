# Cuts teeth into stock to create Y rack

################################
# ENDURANCE TEST:                     #
# Bottom surface of material   #
################################


# Header
lines = ['(T1 CUSTOM TOOTH CUTTER)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'G0 X0 Y0', #Got to XY datum
        ]

for x in range(10000):
    lines.append("G0 X5.555 Y5.555")
    lines.append("G0 X5.575 Y5.575")
#     lines.append("*L00FF00")
  
f = open("comms_endurance1p0.nc", "w")
for line in lines:
    f.write(line + "\n")   

print "Done"
