base_10_number = int(input("Natural number: "))

binary_number = " "
if base_10_number <= 0:
    exit
else:
    while base_10_number > 0:
        module_division = (base_10_number % 2)
        binary_number = (binary_number + str(module_division))
        base_10_number = (base_10_number // 2)
    print (f"Binary:{binary_number}")

