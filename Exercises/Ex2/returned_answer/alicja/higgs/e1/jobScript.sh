#!/bin/bash

# Compiling with Makefile
make
# Making new directory to store the results

DIR="out_bash"
if [ -d "$DIR" ]; then
    rm -r "$DIR"
fi
mkdir -p "$DIR"

# Running parallel jobs
n=10
for i in $(seq 1 $n); do 
    ./ex2 $i > "$DIR/run_$i.txt" &
done
wait
echo "0"