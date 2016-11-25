data = open('output_dataset_ALL.txt').readlines()
#data = open('dataset.txt').readlines()
out = open('output_gcode.gcode', 'w')

for j in range(len(data)/4):
    i = j*4
    x = data[i][:-2].strip()
    y = data[i+1][:-2].strip()
    z = data[i+2][:-2].strip()
    e = data[i+3][:-2].strip()
    out.write('G1 X' + x[:-2] + ' Y' + y[:-2] + ' Z' + z[:-2] + ' E' + e + '\n')

out.close()
