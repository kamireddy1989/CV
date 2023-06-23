import numpy as np

def binary_search(inv,t,ub,lb=0):
    rate=lb
    npv=np.sum(inv/(1+(rate/100))**t)
    i=0
    while(True):
        if(npv>0):
            lb=rate
            ub=ub
        else:
            ub=rate
            lb=lb
        rate=(lb+ub)/2
        npv=np.sum(inv/(1+(rate/100))**t)
        if(npv<=1e-10 and npv>=1e-12):
            break
        if(i>1000):
            print('Solution did not converge')
            break
        i+=1
    return(i,rate,npv)
        
arr=np.array([[-100,0,0,0,100,100],[0,1,2,3,4,5]])

x=binary_search(arr[0],arr[1],ub=90)

print(f'Iterations:{x[0]}\nRate:{x[1]} \nNPV:{x[2]}')
