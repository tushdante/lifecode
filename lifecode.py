import sys
from optparse import OptionParser
import csv
import operator
import time
import itertools
import multiprocessing
import os



'''
Read two input files
'''
def main():
    parser = OptionParser(usage="lifecode.py -i1 <inputfile1> -i2 <inputfile2> -o <outputfile>")
    parser.add_option("--i1", "--input1", dest="input1",
                      help="input files")
    parser.add_option("--i2", "--input2", dest="input2",
                      help="input files")
    parser.add_option("--o", "--output", dest="output", help="output file for final output")

    # Error handling
    try:
        opts, args = parser.parse_args()
        if( not opts.input1 or not opts.input2 or not opts.output):
            parser.error("Please sepecify all options")
    except parser.error:
        parser.error('Error getting options')
        sys.exit(2)

    (input1, key1) = read_csv(opts.input1) 
    (input2, key2) = read_csv(opts.input2)

    output = opts.output

    for i in range(0, len(input1)):
        try:
            # To ensure while checking that chromosome value in input 1 is the same in input 2
            index = key2.index(key1[i])
            check_values(input1[i], input2[index])
        # In cases where input file 2 does not have a key which is in input file 1
        except ValueError:
            continue
    write_csv(output, input1)

'''
Compares two lists based on functional requirements
Appends annotations to first list if available else adds empty string
'''
def check_values(input1, input2):
    for row1 in input1:
        for row2 in input2:
            start1 = int(row1[1])
            start2 = int(row2[1])
            end1 = int(row1[2])
            end2 = int(row2[2])
            if((start2 <= start1 <= end2) or (start1 <= start2 <= end1)):
                row1.append(row2[3])
    # If no annotations are found, we want to append an empty string to the row in output
    if(len(row1) < 4):
        row1.append("")
    return

'''
Write to a csv file as specified in output option
Check to make sure file exists else create a new file
Takes [outputList] as param which contains the annotated values
'''
def write_csv(fileName, outputList):
    if (os.path.exists(fileName)):
        csv_file = open(fileName, 'wt')
    else:
        csv_file = open(fileName, 'w')
    writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
    for rows in outputList:
        for row in rows:
            writer.writerow(row)

'''
Read the csv file
Assumption: The csv file does not contain header
Assumption: The csv file is delimited by ,
Returns a tuple of sorted and grouped lists (sorted and grouped by chromosome) with keys (chromosome number)
'''
def read_csv(fileName):
    with open(fileName, "rb") as f:
        reader = csv.reader(f)
        groups = []
        keys = []
        sortedlist = sorted(reader, key=lambda row: int(row[0]), reverse=False)
        for key, rows in itertools.groupby(sortedlist, key=lambda row: int(row[0])):
            groups.append(list(rows))
            keys.append(key)
        return (groups, keys)


if __name__ == "__main__":
   start_time = time.time()
   main()  
   # Measure the time taken to run
   print("--- %s seconds ---" % (time.time() - start_time))


