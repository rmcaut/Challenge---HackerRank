if __name__ == '__main__':
    records_list  = []
    lowest_students = []
    second_students = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     records_list = records_list + [[name, score]]
    records_list = [["a", 2], ["b", 3], ["c", 2], ["d", 3], ["e", 1], ["f", 1]]
    print(records_list)
    lowest_students = [records_list[0][0]]
    lowest = 100
    print(type(lowest))
    second_students = [records_list[0][0]]
    second = 100
        
    for item in records_list:
        if item[1] > second:
            continue
        else:
            if item[1] < lowest:
                  second_students = lowest_students
                  second = lowest
                  lowest_students = [item[0]]
                  lowest = item[1]
                  continue
        if item[1] > lowest and item[1] < second:
                second_students = [item[0]]
                second = item[1]
                continue
        if item[1] == second:
            second_students.append(item[0])
            continue
        elif item[1] == lowest:
            lowest_students.append(item[0])

    print(lowest_students)
    print(second_students)