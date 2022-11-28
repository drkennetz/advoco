#!/bin/bash

# Sets up a directory structure for your aoc adventures

usage() {
  cat <<EOF
Usage: setup_year.sh -y YEAR -l LANGUAGE
  YEAR ........ The AoC year you'll be completing
  LANGUAGE .... Setup dirs for this language
EOF
}

YEAR=$(date +"%Y")
LANGUAGE=""

while getopts "y:l:h" opt; do
    case $opt in
	y) YEAR=$OPTARG; ;;
	l) LANGUAGE=$OPTARG; ;;
	h) usage && exit 1; ;;
	?) usage && exit 1; ;;
    esac
done



SRC=${BASH_SOURCE[0]}
CURRENT_DIR=$(readlink -f $(dirname $SRC))
parent=$CURRENT_DIR/..
homebase=$(readlink -f $parent)

for day in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25; do
    if [ $LANGUAGE ]; then
	mkdir -p $homebase/$YEAR/$day/data
	mkdir -p $homebase/$YEAR/$day/$LANGUAGE
	touch $homebase/$YEAR/$day/data/day${day}.txt
	touch $homebase/$YEAR/$day/$LANGUAGE/.placeholder
    else
	mkdir -p $homebase/$YEAR/$day/data
	touch $homebase/$YEAR/$day/data/day${day}.txt
    fi
done
