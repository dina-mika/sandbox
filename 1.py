from argparse import ArgumentParser
import os
import multiprocessing as mp
import time

parser = ArgumentParser()
parser.add_argument('-files', dest='quantity')
parser.add_argument('-size', dest='size')
parser.add_argument('-dir', dest='location')
parser.add_argument('-P', dest='pattern')
parser.add_argument('-parallel', dest='parallel')
args = parser.parse_args()



if args.size.endswith("K"):
    x = args.size[0:len(args.size)-1:1]
    x = int(x)*1024
elif args.size.endswith("M"):
    x = args.size[0:len(args.size)-1:1]
    x = int(x)*1048576
elif args.size.endswith("G"):
    x = args.size[0:len(args.size)-1:1]
    x = int(x)*1073741824
elif args.size.isdigit():
    x = int(args.size)

list = []
def create_files(location, quantity, x, pattern, list):
    filepath = os.path.join('C:/Users/Public' + location + '/', 'file_')
    if not os.path.exists('C:/Users/Public' + location + '/'):
        os.makedirs('C:/Users/Public' + location + '/')
    i=0
    
    while i < int(quantity):
        start=time.time()
        name = str(i) + '.txt'
        f = open(filepath + name,"w+")
        f.seek(x - len(pattern)-1)
        f.write(pattern)
        end=time.time()
        list.insert(i, float("{0:.2f}".format(end-start)))
        i = i+1


#pool = mp.Pool(mp.cpu_count())
#result = [pool.apply(create_files(args.location, args.quantity, x, args.pattern))]
#pool.close()
create_files(args.location, args.quantity, x, args.pattern, list)

summ = 0
for k in range(len(list)):
    summ = summ + list[k]
    
avg = summ / len(list)
list.sort()

print("Creating " + args.quantity + " files in " + args.location)
print("Min: " + str(list[0]) + "sec Max: " + str(list[len(list)-1]) + "sec Avg: " + str(float("{0:.2f}".format(avg))) + "sec Total: " + str(float("{0:.2f}".format(summ))) + "sec")

