#!/usr/bin/env python3

def latest(scores):
    return scores[-1]   


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    if len(scores) < 3:
        return scores[::-1]
    else:
        scores = sorted(scores)
        high_scores = [scores.pop() for i in range(3)]
        return high_scores
        

        
    
