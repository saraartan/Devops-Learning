#!/bin/bash


hello_world() {
    echo "Hello world!"
}

greet_person () {
    local name="$1"
    echo "Hello, $name!"
}

greet_person "Ahmed" 
greet_person "Sam"
