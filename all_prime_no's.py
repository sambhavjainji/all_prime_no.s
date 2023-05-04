n=int(input("Enter a no.:-"))
i=1
j=1
f=0
while(i<=n):
    while(j<=i):
        if(i%j==0):
            f=f+1
            j=j+1
    if (f==2):
        print(i)
    i=i+1

        
    
