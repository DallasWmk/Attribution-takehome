#!/bin/bash

echo "Building image for the restricted section..."
cd ./restrictedsection 
docker build -t rescrictedsection .

echo "Building image for the librarian"
cd ../librarian
docker build -t librarian .

cd ..
