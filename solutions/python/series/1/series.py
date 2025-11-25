#!/usr/bin/env python3

def slices(series, length):
    if length > len(series):
        raise ValueError("Slice greater than series length")
    if length <= 0:
        raise ValueError("Length must be greater than 0")
    if not series:
        raise ValueError("Empty series not valid")
    series = [series[i:i+length] for i in range(len(series)-length + 1)]
    return series
