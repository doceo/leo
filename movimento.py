#!/usr/bin/python


def mov_or(pm):
    fine = 640
    inizio = int(fine/10)
    passo = inizio
    col = 1;
	
    print pm
	
    for i in range (0, fine, passo):
		
        if(pm < i):
            return col
        col=col+1
