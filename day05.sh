#!/usr/bin/env bash

sorted=$(sed "s@[BR]@1@g;s@[LF]@0@g" 2020day05input | sort); max=$(echo $sorted | grep --only-matching "[0-1]\+$"); echo "$((2#${max}))"

min=$(echo $sorted | grep --only-matching "^[0-1]\+"); comm -3 <(for f in $sorted ; do echo "$((2#$f))" ; done) <(seq "$((2#${min}))" "$((2#${max}))")
