s=input().split()
n=int(input())
l=[]
l+=s[-n:]
print(l[::-1])

"""
input: 
This is my favourite cookie
4
output:['cookie', 'favourite', 'my', 'is']

"""
