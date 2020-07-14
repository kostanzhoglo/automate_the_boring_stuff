def eggs(parameter):
    parameter.append('hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)