new_lst = list(map(int, input().split()))
maxi = new_lst.index(max(new_lst))
mini = new_lst.index(min(new_lst))
new_lst[maxi], new_lst[mini] = new_lst[mini], new_lst[maxi]
print(new_lst)
