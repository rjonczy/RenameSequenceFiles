# RenameSequenceFiles

## Requirements

Write a tool to assist with renumbering sequences of images in your language of choice. The tool takes a path to a directory containing one or more sequences of images.
 
Each sequence is named like so: `_<seq_num>`.
 
e.g.
 
`awesome_01.jpg awesome_27.jpg`
 
Files with the same name and extension belong in the same sequence.
 
i.e
`awesome_01.jpg` and `awesome_27.jpg` are part of the same sequence
`awesome_01.jpg` and `awesome_02.png` are NOT part of the same sequence
`awesome_01.jpg` and `weta_02.jpg` are NOT part of the same sequence
 
Rename the files in the directory so that each sequence is still in the same order, but the files in that sequence are numbered sequentially
 
You can assume the following:
 
- The numbers are always 2 digits (0 padded if required)
- The resulting sequences all start at 01
- The filesystem is a POSIX compliant filesystem
 
For example:
`awesome_11.jpg awesome_11.png awesome_27.jpg awesome_32.jpg awesome_32.png awesome_33.png awesome_47.png awesome_55.jpg awesome_55.png awesome_56.jpg awesome_68.jpg awesome_72.png awesome_94.png weta_17.jpg weta_22.jpg weta_37.jpg weta_55.jpg weta_96.jpg`
 
Would become:
- (seq1): `awesome_01.jpg awesome_02.jpg awesome_03.jpg awesome_04.jpg awesome_05.jpg awesome_06.jpg`
- (seq2): `awesome_01.png awesome_02.png awesome_03.png awesome_04.png awesome_05.png awesome_06.png awesome_07.png`
- (seq3): `weta_01.jpg weta_02.jpg weta_03.jpg weta_04.jpg weta_05.jpg`

## Generating sample data

In order to prepare sample data, following BASH script should be run:
```
./0-generateFiles.sh
```

## Renaming files withing sequence

In order to rename files withing sequences, followign Python script should be run:
```
python 1-renameSequences.py ./data
```