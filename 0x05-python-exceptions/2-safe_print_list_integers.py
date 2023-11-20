#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            value = my_list[i]
            if type(value) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except ValueError as e:
            print(str(e))
        except IndexError as e:
            raise
        except TypeError as e:
            print(str(e))
            break
    print("")
    return (count)

