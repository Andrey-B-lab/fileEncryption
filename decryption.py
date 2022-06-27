import pyAesCrypt
import os
import sys

# file decryption function
def decryption(file,password):

    # buffer size
    buffer_size = 512 * 1024

    # deryption method
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # print the encrypted file name
    print("[File '" + str(os.path.splitext(file)[0]) + "'decrypted]")

    #delte the old file
    os.remove(file)

# directories scanning function
def walking_by_dirs(dir, password):

    # go through all under directories in a given directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # decrypt file if you find one
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # if we find directory, repeat the file search
        else:
            walking_by_dirs(path, password)

password = input("Enter password for decryption: ")
walking_by_dirs("/Users/andreybyhalenko/Desktop/test_encryption", password)

# remove scripts after done
# os.remove(str(sys.argv[0]))
