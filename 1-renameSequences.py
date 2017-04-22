# -*- coding: utf-8 -*-
import os, sys, re

def read_files(directory = '.'):
    filesList = [f for f in os.listdir(directory)]
    return filesList

def get_unique_ext(files_list):

    extensions = []
    for s in files_list:
        match = re.search(r'([a-z0-9]+)\_([0-9]{2})\.([a-z0-9]+)$', s)
        if match:
            extensions.append(match.group(3))
    
    return list(set(extensions))

def get_unique_names(files_list, ext):
    names = []
    for s in files_list:
        match = re.search(r'([a-z0-9]+)\_([0-9]{2})\.' + ext + '$', s)
        if match:
            names.append(match.group(1))
    
    return list(set(names))

def get_sequence_files(files_list, name, ext):
    sequenceFiles = []
    for s in files_list:
        match = re.search(r''+name+'\_([0-9]{2}).'+ext+'$', s)
        if match:
            sequenceFiles.append(s)
    
    return sequenceFiles

def find_sequences(files_list):

    # matched files should have: _<seq_num>.
    sequences = []
    for ext in get_unique_ext(files_list):
        for name in get_unique_names(files_list, ext):
            sequences.append(get_sequence_files(files_list, name, ext))
    
    return sequences



def main():

    directory = './data' if len(sys.argv) == 1 else sys.argv[1]

    # read all files in given directory
    files_list = read_files(directory)

    # find all files belonging to sequences and 
    sequences = find_sequences(files_list)

    pattern = re.compile(r'_\d{2}.')
    for seq in sequences:
        for i, old_file_name in enumerate(sorted(seq)):
            new_file_name = re.sub(pattern, "_" + str(i+1).zfill(2) + ".", old_file_name)
            print("Renaming: " + old_file_name + " into: " + new_file_name)

            # rename files withing sequence
            os.rename(directory + "/" + old_file_name, directory + "/" +new_file_name)
            


if __name__ == "__main__":
    main()