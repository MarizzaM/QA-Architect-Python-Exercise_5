str = 'I love to eat ice cream in the beach'

lst_1 = str.upper().split()
print(lst_1)
print('*************************************')
lst_2 = str.split()
lst_2 = [x[:1] for x in lst_2]
print(lst_2)
print('*************************************')
lst_3 = str.split()
lst_3 = [x[2:] for x in lst_3 if len(x) >= 3]
print(lst_3)
print('*************************************')
lst_4 = str.split()
lst_4 = [len(x) for x in lst_4]
print(lst_4)
