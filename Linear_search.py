def Search(list,target):
    for i in range(len(list)):
        if list[i] == target:
            return i


list = [23,53,565,23,23,232,533,5634,2323,232,2,35,35253,66,2,3,42,24,5,3]
find = 2

print(Search(list,find))