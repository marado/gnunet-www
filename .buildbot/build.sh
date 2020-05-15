#!/bin/bash

./bootstrap
./configure
make
if [ $? -eq 0 ]; then
  exit 0
fi
echo "Try again"
make
