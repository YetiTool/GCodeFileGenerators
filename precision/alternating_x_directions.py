# Cuts slots in alternating x directions, a tool diameter apart

################################
# Z-DATUM:                     #
# Top surface of material   #
################################

# Header
lines = ['(T1 6.35mm cutter)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        'M3 S25000', # Turn on spindle
        'G4 P1', # Allow time to spin up to speed
        'AE' # Switch on extractor
        'G4 P2', # Allow time to spin up to speed
        ]

# Cutting variables
xy_feed_rate = 600 #mm/min
z_feed_rate = 200 #mm/min

z_height_for_rapid_move = 5 # relative clearance above stock for safe moves
z_height_for_approach = 1 # to dive down at high speed to, before using z_feed_rate
cutter_diameter = 6.35
gap_between_slots = 3


number_of_channels_per_test = 3

plunge_depth = -3
run_length = 30

x = 0
y = 0


# Inner part offs
lines.append("\n(Baseline test, incrementing along y)")

channel = 0
lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("G0 X" + str(x) + " Y" + str(y))

while channel < number_of_channels_per_test:

    lines.append("G0 Z" + str(z_height_for_approach))
    lines.append("G1 Z" + str(plunge_depth) + " F" + str(z_feed_rate))
    lines.append("G1 X" + str(run_length) + " F" + str(xy_feed_rate))
    lines.append("G0 Z" + str(z_height_for_rapid_move))
    y += cutter_diameter + gap_between_slots
    lines.append("G0 Y" + str(y))
    lines.append("G0 Z" + str(z_height_for_approach))
    lines.append("G1 Z" + str(plunge_depth) + " F" + str(z_feed_rate))
    lines.append("G1 X" + str(x) + " F" + str(xy_feed_rate))
    lines.append("G0 Z" + str(z_height_for_rapid_move))
    y += cutter_diameter + gap_between_slots
    lines.append("G0 Y" + str(y))
    
    channel += 1


lines.append("G0 Z" + str(z_height_for_rapid_move))
lines.append("M5") #Kill spindle
lines.append("G4 P2") #Pause for vac overrun
lines.append("AF") #Vac off
lines.append("M30") #Prog end
lines.append("%") #Prog end (redundant?)
  
f = open("alternating_x_directions.nc", "w")
for line in lines:
    f.write(line + "\n")   

print ("Done.")

