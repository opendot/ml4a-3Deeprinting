data = open('output_dataset.txt').readlines()
original = open('dataset_ALL.txt').readlines()
#data = open('dataset.txt').readlines()
out = open('output_gcode_merged.gcode', 'w')

for j in range(len(data)/4):
    i = j*4
    out.write('G1 X' + data[i].split()[0][:-2] + ' Y' + data[i+1].split()[0][:-2] + ' Z' + original[i+2].split()[0][:-2] + ' E' + original[i+3].split()[0])

out.close()
