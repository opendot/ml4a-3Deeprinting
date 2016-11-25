data = open('output_dataset.txt').readlines()
#data = open('dataset.txt').readlines()
out = open('output_gcode.gcode', 'w')

for j in range(len(data)/4):
    i = j*4
    out.write('G1 X' + data[i][:-2] + ' Y' + data[i+1][:-2] + ' Z' + data[i+2][:-2] + ' E' + data[i+3])

out.close()
