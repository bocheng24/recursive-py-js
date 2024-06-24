print('Code in a loop')

i = 0

while i < 5:
    print(i, 'Hello')
    i += 1

def hello(i = 0):

    print(i, 'Hello')
    if i + 1 < 5:
        hello(i + 1)

print('Code in recursive function')
hello()