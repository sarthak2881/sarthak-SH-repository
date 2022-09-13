em = input("Enter Email address to be validated :- ")
k, j, d = 0, 0, 0
if len(em) >= 6:
    if em[0].isalpha():
        if ("@" in em) and (em.count('@') == 1):
            if (em[-4] == '.') ^ (em[-3] == '.'):
                for i in em:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if (k == 1) or (j == 1) or (d == 1):
                    print(f'Wrong Input {em}')
                else:
                    print(f'Email "{em}" Validated Successfully ')
            else:
                print(f'Wrong Input {em}')
        else:
            print(f'Wrong Input {em}')
    else:
        print(f'Wrong Input {em}')
else:
    print(f'Wrong Input {em}')
em=str(em)
#For Domain Name 
dn=em[em.index('@')+1:]
print(f"The domain name is : '{dn}' ")
# For Username
un=em.split("@")
print(f"The username is : '{un[0]}' ")