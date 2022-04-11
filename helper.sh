#!/usr/bin/env bash


read -p "Enter the name of the language: " language
read -p "Enter the extension (py): " extension


# Create the directories and files
mkdir ./src/$language
mkdir ./src/$language/fast
mkdir ./src/$language/slow

touch ./src/$language/slow/main.$extension
touch ./src/$language/fast/main.$extension

echo "Sucessfully created the directories and files!"