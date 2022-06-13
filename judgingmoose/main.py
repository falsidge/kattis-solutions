print((lambda x,y: "Not a moose"if x==y==0 else["Odd ","Even "][x==y]+str(2*max(x,y)))(*map(int, input().split())))
