#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    last_list = []
    for i in range(list_length):
        try:
            safe_div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            safe_div = 0
        except ZeroDivisionError:
            print("division by 0")
            safe_div = 0
        except IndexError:
            print("out of range")
            safe_div = 0
        finally:
            last_list.append(safe_div)
    return last_list
