
################################
# ENDURANCE TEST:              #
# Repeats block of known offending gcode   #
################################


# Header
lines = ['(T1 CUSTOM TOOTH CUTTER)',
        'G90', #Absolute
        'G94', #Feed units per mm
        'G17', #XY plane
        'G21', #In MM
        ]



for x in range(100):
    lines.append("G90G94")
    lines.append("G17")
    lines.append("G21")
    lines.append("M9")
    lines.append("S34000M3")
    lines.append("G54")
    lines.append("G0X140.655Y962.993")
    lines.append("Z27")
    lines.append("Z17")
    lines.append("Z12.77")
    lines.append("G1Z12.135F2200")
    lines.append("X140.653Y962.985Z12.036")
    lines.append("X140.647Y962.963Z11.939")
    lines.append("X140.638Y962.926Z11.847")
    lines.append("X140.625Y962.875Z11.762")
    lines.append("X140.609Y962.813Z11.686")
    lines.append("X140.59Y962.739Z11.621")
    lines.append("X140.569Y962.657Z11.569")
    lines.append("X140.546Y962.568Z11.531")
    lines.append("X140.522Y962.474Z11.508")
    lines.append("X140.497Y962.378Z11.5")
    lines.append("G3X140Y958.921I15.704J-4.023")
    lines.append("G1Y958.771")
    lines.append("X140.203Y957.777")
    lines.append("X140.342Y956.772")
    lines.append("X140.437Y955.762")
    lines.append("X140.501Y954.749")
    lines.append("X140.544Y953.735")
    lines.append("X140.574Y952.721")
    lines.append("X140.594Y951.707")
    lines.append("X140.607Y950.692")
    lines.append("X140.616Y949.678")
    lines.append("X140.622Y948.663")
    lines.append("X140.626Y947.649")
    lines.append("X140.631Y945.62")
    lines.append("X140.634Y942.576")
    lines.append("X140.635Y932.43")
    lines.append("Y913.661")
    lines.append("X140.574Y913.157")
    lines.append("X140.349Y912.702")
    lines.append("X139.722Y911.905")
    lines.append("X138.889Y911.325")
    lines.append("X137.961Y910.915")
    lines.append("X136.988Y910.63")
    lines.append("X135.993Y910.433")
    lines.append("X134.987Y910.298")
    lines.append("X133.977Y910.206")
    lines.append("X132.964Y910.144")
    lines.append("X131.95Y910.102")
    lines.append("X130.936Y910.073")
    lines.append("X129.922Y910.054")
    lines.append("X128.907Y910.041")
    lines.append("X127.893Y910.032")
    lines.append("X126.878Y910.026")
    lines.append("X125.863Y910.022")
    lines.append("X123.834Y910.018")
    lines.append("X120.791Y910.015")
    lines.append("X109.63Y910.014")
    lines.append("X86.295")
    lines.append("X85.281Y909.983")
    lines.append("X85.154Y909.982")
    lines.append("X85.004Y909.979")
    lines.append("X84.854Y909.973")
    lines.append("X84.705Y909.965")
    lines.append("X84.555Y909.955")
    lines.append("X84.405Y909.943")
    lines.append("X84.256Y909.928")
    lines.append("X84.107Y909.912")
    lines.append("X83.958Y909.894")
    lines.append("X83.81Y909.873")
    lines.append("X83.662Y909.848")
    lines.append("X83.514Y909.82")
    lines.append("X83.368Y909.789")
    lines.append("X83.221Y909.756")
    lines.append("X83.076Y909.72")
    lines.append("X82.931Y909.681")
    lines.append("X82.786Y909.641")
    lines.append("X82.643Y909.598")
    lines.append("X82.5Y909.551")
    lines.append("X82.359Y909.501")
    lines.append("X82.218Y909.448")

#     lines.append("*L00FF00")
  
f = open("comms_endurance_block1.nc", "w")
for line in lines:
    f.write(line + "\n")   

print "Done"
