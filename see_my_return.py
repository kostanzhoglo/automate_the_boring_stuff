def this_will_show_print(word):
    print(word)                     # it will print to console
                                    # but return value is NONE

this_will_show_print("I printed this!")


def this_will_show_return_value(number):
    new_num = number + 10
    return print(new_num)           # it will print to console
                                    # but return value is still NONE

this_will_show_return_value(7)          # prints 17 to console.
                                        # return value == None


def another_way_to_return_a_value_and_print(secret):
    return 2 * secret               # return value is INTACT.

shocking = another_way_to_return_a_value_and_print("zanzibar ")
print(shocking)
