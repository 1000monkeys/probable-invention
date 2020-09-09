if __name__ == "__main__":
    list = [
        'test',
        'abcdef',
        'python'
    ]

    boolean_true_value = True
    boolean_false_value = False

    number_ten = 10
    number_eleven = 11
    number_hundred = 100

    if 'test' in list:
        print("test is in the list!")

    if 'testing' not in list:
        print("testing is not in the list!")

    if boolean_true_value or boolean_false_value:
        print("One of the boolean values is true!")

    if boolean_true_value and True:
        print("Both values are true!")

    if number_ten >= 10:
        print("Number ten is equal to or greater than 10!")

    if number_ten < number_eleven:
        print("Number eleven is bigger than ten!")

    if 'test' == list[0]:
        print("Test is the first item in the list!")