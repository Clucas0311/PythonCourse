from sys import argv
from os.path import exists # returns True if file exists

script, from_file, to_file = argv # declaring parameters

print(f"Copying from {from_file} to {to_file}") # just printing file name

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}") # returns true/false if file exists or not
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w') # we want to open/create our file and what do we want to do that file 'write'
out_file.write(indata) # to write on the file, the parameter is what we want to write on the file - so indata will be written on file

print("Alright, all done.")

out_file.close() # closes file
in_file.close()
