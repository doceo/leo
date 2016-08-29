#!/usr/bin/python


def mov_or(pm):
    fine = 640
    inizio = int(fine/15)
    passo = inizio
    col = 0;
	
    #print pm
	
    for i in range (0, fine, passo):
    	
    	print i
        if(pm < i):
            return col
        
        col=col+1
        if (col==10): return 10	
