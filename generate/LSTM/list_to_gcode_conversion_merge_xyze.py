index = '2'
dataset_X = open('output_dataset_X' + index + '.txt').readlines()
dataset_Y = open('output_dataset_Y' + index + '.txt').readlines()
dataset_Z = open('output_dataset_Z' + index + '.txt').readlines()
dataset_E = open('output_dataset_E' + index + '.txt').readlines()
#data = open('dataset.txt').readlines()
out = open('output_gcode_merged' + index + '.gcode', 'w')

for j in range(len(dataset_X)/4):
    i = j*4
    x = dataset_X[i].strip()
    y = dataset_Y[i].strip()
    z = dataset_Z[i].strip()
    e = dataset_E[i].strip()
    out.write('G1 X' + x[:-2] + ' Y' + y[:-2] + ' Z' + z[:-2] + ' E' + e + '\n')

out.close()
