def main():

    case = 1
    # THIS LOOP CONTINUES THE PROGRAM UNTIL THE USER INPUTS '0 0'
    while True:
        # VALIDATING THE INPUT OF 'm' and 'n'
        while True:
            s, r = input("Enter the number of regions and number of programs(0 0 to exit):").split()
            m = int(s)
            n = int(r)
            if m < 0 or m > 10:
                print("number of regions cannot be more than 10 or lower than 1!")
                continue
            if n < 0 or n > 50:
                print("number of programs cannot be more than 50 or less than 1!")
                continue
            if n == 0 and m == 0:
                print("Thank you!")
                exit()
            break

        # TAKING MEMORY REGIONS SIZE
        memory_size = []
        for i in range(m):
            size = int(input("Enter the size of the region "+str(i+1)+":"))
            memory_size.append(size)

        # TESTING
        prog_list = input_prog(n)
        print(prog_list)
        print(allocate(n, m, prog_list, memory_size))


# TAKING INPUT FOR PROGRAM LIST
def input_prog(n):
    # CREATING A LIST TO STORE PROGRAM LIST
    prog_list = [[0] for y in range(n)]

    # TAKING INPUT TO PROGRAM LIST
    for i in range(n):

        # VALIDATING THE INPUT 'k'
        while True:
            k = int(input("Enter the number of pairs: "))
            if k < 1 or k > 10:
                print("number of pairs should be between 1 to 10")
                continue
            break

        # ASSIGNING 'k' AS THE FIRST ELEMENT TO THE PROGRAM LIST
        prog_list[i][0] = k

        # ASSIGNING MINIMUM REQUIRED SIZE OF MEMORY AND EXECUTION TIME PAIR TO THE PROGRAM LIST
        for j in range(k):
            ms = int(input("Enter the minimum size required: "))
            t = int(input("Enter the execution time: "))
            prog_list[i].append(ms)
            prog_list[i].append(t)

    # RETURNING THE PROGRAM LIST
    return prog_list


# FUNCTION TO SELECT THE MINIMUM SPACE INDEX IF THE K VALUE IS GREATER THAN 1
def get_lowest_exec_time(program=[]):
    min_time = 9223372036854775807
    min_size_index = -1
    for i in range(1, len(program)):
        if i % 2 == 0:
            if min_time > program[i]:
                min_time = program[i]
                min_size_index = i - 1
    return min_size_index


main()
