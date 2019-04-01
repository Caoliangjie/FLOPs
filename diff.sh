#!/bin/bash
#output is the different line in file1 andfile2
for line1 in $(cat $1)
    do
        grep $line1 $2 > /dev/null
            if [ $? -eq 1 ]; then
               echo "${line1}" >> diff.txt
            fi
    done
