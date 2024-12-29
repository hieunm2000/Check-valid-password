def check_password(password):
    condition_1 = False
    # Check được liệu có 1 lowercase letter trong password string hay không?
    for i in password:
        if i.islower():
            condition_1 = True
            break
    
    condition_2 = False
    # Check được liệu có 1 số trong password hay không?
    for i in password:
        if i.isnumeric():
            condition_2 = True
            break
    
    condition_3 = False
    #Check được liệu có 1 uppercase trong password không
    for i in password:
        if i.isupper():
            condition_3 = True
            break
        
    condition_4 = False
    #Check được liệu có 1 ký tự đặc biệt [$, @, #]
    for i in password:  
        if i in ['$', '@', '#']:
            condition_4 = True
            break
    
    # Check độ dài password nằm trong khoảng 6 - 12 ký tự
    do_dai_pass = len(password)
    if do_dai_pass >= 6 and do_dai_pass <= 12:
        condition_5 = True
    else:
        condition_5 = False
    # conditions
    conditions = condition_1 & condition_2 & condition_3 & condition_4 & condition_5
    if conditions:
        print("Valid password")
    else:
        print("Invalid password")
    return 0
password = "Abc1@"
check_password(password)