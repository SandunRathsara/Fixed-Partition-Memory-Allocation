def main():

    # VALIDATING THE INPUT OF 'm' and 'n'
    while True:
        m = int(input("Enter the number of regions:"))
        if m < 0 or m > 10:
            print("number of regions cannot be more than 10 or lower than 1!")
            continue
        n = int(input("Enter the number of programs: "))
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

    # FIRST TEST CASE PROGRAM LIST
    prog_list1 = input_prog(n)

    print(prog_list1)


# TAKING INPUT FOR PROGRAM LIST
def input_prog(n):
    # CREATING A LIST TO STORE PROGRAM LIST
    prog_list = [[0 for x in range(1)] for y in range(n)]

    # TAKING INPUT TO PROGRAM LIST
    for i in range(n):

        # VALIDATING THE INPUT 'k'
        while True:
            k = int(input("Enter the number of pairs: "))
            if k < 1 or k > 10:
                print("number of pairs should be between 1 to 10")
                continue
            break
        # ASSIGNING NUMBER OF
        prog_list[i][0] = k
        for j in range(k):
            ms = int(input("Enter the minimum size required: "))
            t = int(input("Enter the execution time: "))
            prog_list[i].append(ms)
            prog_list[i].append(t)
    return prog_list

main()