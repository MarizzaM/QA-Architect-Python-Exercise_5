id = int(input('Please enter ID number of the Person: '))
name = input('Please enter Name and Last Name of the Person: ')

archive = {}

while id != 1:
    archive.setdefault(id, name)
    id = int(input('Please enter ID number of the Person: '))
    if id == 1:
        break
    name = input('Please enter Name and Last Name of the Person: ')

print(archive)
