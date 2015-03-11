import csv
import random
import string
import sys
import os

'''
Generate csv data based on requirements:

1.
Chromosome (int) [1-22]
Start Position (int) [1-100000000]
End Position (int) [1-100000000]

2.
Chromosome (int) [1-22]
Start Position (int) [1-100000000]
End Position (int) [1-100000000]
Annotation Value (string) [1-20]

'''
def generate_annotation(size):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(size))


def flush_to_file(fileName, chromosome, start, end, annotation=None):
    writer = csv.writer(fileName)
    if(annotation):
        writer.writerow( (chromosome, start, end, annotation))
    else:
        writer.writerow( (chromosome, start, end))

def date_range():
    start, end = random.randint(1,100000000), random.randint(1, 100000000)
    while(start>end):
        start, end = random.randint(1,100000000), random.randint(1, 100000000)
    return [start, end]



def main(length):
    if (os.path.exists(sys.argv[1]) and  os.path.exists(sys.argv[1])):
        input_1 = open(sys.argv[1], 'wt')
        input_2 = open(sys.argv[2], 'wt')
    else:
        input_1 = open(sys.argv[1], 'w')
        input_2 = open(sys.argv[2], 'w')

    for i in range(0, length):
        (chromosome, start, end) = (random.randint(1,22), date_range()[0], date_range()[1])
        (chromosome1, start1, end1, annotation) = (random.randint(1,22), date_range()[0], date_range()[1], generate_annotation(random.randint(1,20)))
        flush_to_file(input_1, *(chromosome, start, end))
        flush_to_file(input_2, *(chromosome1, start1, end1, annotation))

if __name__ == "__main__":
    length = int(sys.argv[3])
    main(length)
