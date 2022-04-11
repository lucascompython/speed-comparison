#!/usr/bin/env pwsh

$language = Read-Host "Enter the language"
$extension = Read-Host "Enter the extension (py)"


# Create the directories and files

mkdir ./src/$language
mkdir ./src/$language/slow
mkdir ./src/$language/fast

New-Item ./src/$language/slow/$language.$extension
New-Item ./src/$language/fast/$language.$extension
