#!/bin/sh

# arrays with prefixes and extensions
prefixes=('awesome_' 'great_' 'super_' 'ultra_' 'weta_')
ext=('jpg' 'png' 'txt')

# amount of files to generate
NOFILES=1000

# folder to generate files
FILESFOLDER=./data

# generate $NOFILES
for x in `seq $NOFILES`; 
do 

    # randomly pick prefix and ext from arrays
    prefixes_idx=$(( RANDOM % ${#prefixes[@]} ))
    ext_idx=$(( RANDOM % ${#ext[@]} ))

    # prepare NAME, EXT and NUMBER
    NAME=${prefixes[$prefixes_idx]}
    EXT=${ext[$ext_idx]}
    NUMBER=`printf %02d $(( ( RANDOM % 100 )  + 1 ))`
    FILENAME="$NAME$NUMBER.$EXT"

    echo "generating file $FILENAME in $FILESFOLDER"
    touch $FILESFOLDER/$FILENAME

done

