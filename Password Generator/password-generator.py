    import string
    from random import *

    letters = string.ascii_letters 
    digits = string.digits 
    chars = letters + digits

    min_len = 10
    max_len = 15
    password = "".join(choice(chars) for x in range(randint(min_len, max_len)))
    
    print("THE  PASSWORD  GENERATED  IS : ")
    print(password)
