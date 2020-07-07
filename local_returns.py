eggs = 40

def spam():
    eggs = 99
    print(eggs)
    # bacon()
    print(eggs + bacon())

def bacon():
    ham = 101
    toast = 30
    # print(toast)
    return toast
    

spam()
# print(eggs)




gusto = "with gusto"

def moreVigor():
    global gusto
    gusto = "larry"
    print(gusto)
    
moreVigor()