number = float(input())
is_positiv = False
if number>0:
    is_positiv = True

if number==0:
    print("zero")
elif abs(number)>0 and abs(number)<1:
    if is_positiv:
        print("small positive")
    else:
        print("small negative")
elif abs(number)>1000000:
    if is_positiv:
        print("large positive")
    else:
        print("large negative")
else:
    if is_positiv:
        print("positive")
    else:
        print("negative")
