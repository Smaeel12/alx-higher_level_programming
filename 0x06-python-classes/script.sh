#!/bin/bash
my_module=$1
MyClass=$2
my_function=$3
python3 -c "print(__import__(\"$my_module\").__doc__)"
if [ "$MyClass" ]
then
	python3 -c "print(__import__(\"$my_module\").$MyClass.__doc__)"
fi
if [ "$my_function" ]
then
	python3 -c "print(__import__("$my_module").$my_function.__doc__)"
	python3 -c "print(__import__(\"$my_module\").$MyClass.$my_function.__doc__)"
fi
