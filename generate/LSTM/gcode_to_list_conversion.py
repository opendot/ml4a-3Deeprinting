gcode = open('input.gcode').readlines()
out_all = open('dataset_ALL.txt', 'w')
out_x = open('dataset_X.txt', 'w')
out_y = open('dataset_Y.txt', 'w')
out_z = open('dataset_Z.txt', 'w')
out_e = open('dataset_E.txt', 'w')


for l in gcode:
    words = l.split()
    dataset = []
    if len(words) > 0:
        if words[0] == 'G1':
            #print(words)
            count = 0
            vect = [0]*4
            for w in words[1:]:

                if w[0] == 'X':
                    print("x is ok")
                    count = count + 1
                    vect[0] = w[1:]

                elif w[0] == 'Y':
                    print("y is ok")
                    count = count + 1
                    vect[1] = w[1:]

                elif w[0] == 'Z':
                    print("z is ok")
                    count = count + 1
                    vect[2] = w[1:]

                elif w[0] == 'E':
                    print("e is ok")
                    count = count + 1
                    vect[3] = w[1:]

            if count == 4:
                print(vect)
                for d in vect: out_all.write(d + '\n')
                out_x.write(vect[0] + '\n')
                out_y.write(vect[1] + '\n')
                out_z.write(vect[2] + '\n')
                out_e.write(vect[3] + '\n')
                #dataset = dataset + vect

#for d in dataset: out.write(d + '\n')
out_all.close()
out_x.close()
out_y.close()
out_z.close()
out_e.close()
