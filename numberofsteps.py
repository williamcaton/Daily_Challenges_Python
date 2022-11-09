N = input('how many steps?')
X = [1,3,5]
output=0
summary=0
def fibonacci(N,X):
    summary=0
    if N<0:
        return(0)
    elif N==0:
        return(1)
    else:
        for item in X:
            print(N,item,(N-item))
            summary = summary+fibonacci(N-item,X)
        return(summary)
print(fibonacci(int(N),X))
