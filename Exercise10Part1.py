import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
glob_files = glob.glob(pattern)
print(glob_files)

# TODO: use os.path.getsize to find each file's size
file_size = []
for i in glob_files:
    file_size.append(os.path.getsize(i))

print(file_size)

# TODO: Add a test to only display files that are not zero length
glob_and_size = dict(zip(glob_files, file_size))
print(glob_and_size)

for i in glob_and_size:
    if glob_and_size.get(i) != 0:
        print(i)

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
for i in glob_files:
    print(os.path.basename(i))
