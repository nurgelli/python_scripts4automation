#!/bin/bash


for file in *.docx; do
    name=$(basename "$file" .dox)
    mv "$file" "$name.doc"
done