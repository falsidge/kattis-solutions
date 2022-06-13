print((lambda x: [f"Dr. Chaz needs {x} more piece{['s',''][x==1]} of chicken!",f"Dr. Chaz will have {-x} piece{['s',''][x==-1]} of chicken left over!"][x<0])(int.__sub__(*map(int,input().split()))))
/