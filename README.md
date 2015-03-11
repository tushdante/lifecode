# Usage

There are two scripts ``` data_gen.py``` and ```lifecode.py```

To use ```data_gen.py``` is as follows:
```sh
python data_gen.py <file1.csv> <file2.csv> <number of rows>
```
This file will generate two input files which follow the rules as specificed by the problem statement. The number of rows can be used to determine how many rows of the input are needed. ```file1.csv``` will contain only three columns, while ```file2.csv``` will contain the annotation column as well.

To use ```lifecode.py``` is as follows:
```sh
python lifecode.py --i1 <input_file1.csv> --i2 <input_file2.csv> --o <output_file.csv>
```
Where ```input_file1.csv``` does not have the annotations and ```input_file2.csv``` contains the annotations. The ```output_file.csv``` is where the final output is stored

# Design Considerations

The actual design of my alorithim first sorts each of the input file by the first column **chromosome** and then groups these values together, i.e. first **n** lines have a value of 1, the next **n** have a value of 2 and so on.

The reason for doing this was specificially to be able to parallelize the operations. The way the current algorithim works is that it takes each grouped values together, i.e. **chromosome** value of 1 from **input_file1.csv** with the same value from **input_file2.csv** and then iterates through the rows for both, generating the annotations as per the functional requirements.

Serially, this operation is relatively slow, however if we leverage the power of distributed computing and map/reduce paradigms this solution is a lot more scalable. Also, for a given input set of over  a million we will need atmost 22 (since there are at most 22 discrete values for **cromosome**) processing cores or nodes for the entire input set.

# Assumptions

- The final output will be sorted by the **chromosome** value, i.e. order is not preserved
- The input csv files don't contain any headers
- The csv file is delimited by ','