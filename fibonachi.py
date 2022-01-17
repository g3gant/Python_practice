def fibonachiRecursive(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fibonachiRecursive(n-1) + fibonachiRecursive(n-2)

def fibIterative(n):
    sum = 0
    stack = []
    stack.append(n)
    while (len(stack)>0):
        n = stack.pop()

        if (n==0):
            sum += 0
            continue
        if (n == 1):
            sum += 1
            continue
        stack.append(n-1)
        stack.append(n-2)

    return sum



def fibIterative2(n):
    stack = []
    stack.append(n)
    sum = 0
    while(len(stack) > 0):
      n = stack.pop()
      if n == 0:
        sum += 0
      elif n == 1:
        sum +=1
      else:
        stack.append(n-1)
        stack.append(n-2)
    return sum


print (fibonachiRecursive(15))
print(fibIterative(15))
print(fibIterative2(15))