#!/usr/sbin/env python3

def convert(number):
    option = {3:"Pling", 5:"Plang", 7:"Plong"}
    string = "".join([option[i] for i in option if number%i == 0])
    if not string:
        return str(number)
    return string
