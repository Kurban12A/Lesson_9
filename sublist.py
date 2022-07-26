def isSublist(lst, sublist):
   for i in range(0, len(lst)):
       if lst[i:i+len(sublist)] == sublist:
           return True
   return False

larger = list(map(int, input().split()))
smaller = list(map(int, input().split()))

print(isSublist(smaller, larger))
