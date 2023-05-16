# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 09:00:38 2022
@author: usear
"""

dp = [[0]*500]*500

def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

def minimum(n,m,maximizing):
    if(m>n):
        m,n = swap(m,n)

    if(m==0 or n==0):
        if(maximizing == True):
            return -1
        else:
            return +1

    if(m==1 or n==1):
        if(maximizing == True):
            return +1
        else:
            return -1

    loop=n//m
    if(maximizing):
        mxval=-1e9
        for i in range(1, loop+1):
            eval=minimum(n-i*m,m, False)

            if(eval>mxval):
                mxval=eval
        return mxval

    else:
        mnval=1e9

        for i in range(1, loop+1):
            eval=minimum(n-i*m,m, True)
            if(eval<mnval):
                mnval=eval
                dp[n][m]=i
                dp[m][n]=i
        return mnval

print("-------Number Fight Game--------")
 
print("Enter two initial number a>b:")
while(1):
    ini1,ini2= [int(i) for i in input().split()]
    if ini2>ini1 :
        print("b cann't greater than a. Please enter again.")
    elif ini2<=0:
        print("b can't be 0 or negative number. Please enter again")
    else:
        break
step=0
while(1):
        print("Remaining value : ")
        print(ini1, ini2)
        if(step%2==0):
            if(ini1==0 or ini2==0):
                print("You win.")
                break

            if(ini1==1 or ini2==1):
                print("computer turn : ")
                print("Remaining value : ")
                print("1 0")
                print("computer wins.")
                break

            print("computer turn : ")
            ans=minimum(ini1,ini2, False)
            ini1=ini1-dp[ini1][ini2]*ini2
            if(ini1<ini2):
                ini1,ini2= swap(ini1,ini2);

        else:
            if(ini1==0 or ini2==0):
                print("computer wins.")
                break

            if(ini1==1 or ini2==1):
                print("You win.")
                #break;
            print("your turn: ")

            print("please enter x(b*x<=a):")
            while(1):
                val = int(input())
                if (ini2*val>ini1):
                    print("please enter right value.")
                    print("Enter x(b*x<=a):")
                else:
                    break   
            
            ini1=ini1-ini2*val
            if(ini1<ini2):
                ini1, ini2= swap(ini1,ini2)
        step=step+1