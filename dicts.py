# 1
lst_1 = [1, 2, 3]
lst_2 = ['1', '2', '3']
res = dict(zip(lst_1, lst_2))
print(res)


# 2 
lst_1 = [1, 2, 3]
lst_2 = ['1', '2', '3']
lst_3 = ['A', 'B', 'C']
dicts = dict(zip(lst_1, zip(lst_2,lst_3)))
print(dicts)
