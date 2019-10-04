# all the inputs are asked when the program is running. 
# all the steps are commented.
# IT18028706
# Rathsara W. A. S

import sys

# ===========================MAIN FUNCTION==============================================================================
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

        # CREATING MEMORY REGION LIST
        memory_region = [[i+1] for i in range(m)]
        for i in range(m):
            size = int(input("Enter the size of the region " + str(i+1) + ":"))
            memory_region[i].append(size)

        # GETTING THE PROGRAM LIST
        prog_list = input_prog(n)

# ===========================EXECUTING THE PROGRAMS=====================================================================
        # VARIABLES TO STORE TIME AND INSERTING ORDER
        time_of_memory = [0] * m
        inserting_order_details = []

        # TO GIVE TURNS TO THE MEMORY REGION
        region_number = -1

        # GETTING THE SORTED PROGRAM LIST
        sorted_prog_list = sorting_program_list(n, prog_list)

        for prog in range(n):
            while True:
                # THIS CODE WILL COUNT THE TURN
                # (WHEN A REGION IS GIVEN A PROGRAM,
                # THAT REGION CANNOT TAKE ANOTHER PROGRAM UNTIL
                # ALL THE OTHER REGIONS GET THEIR TURN AND COME BACK TO THE FIRST REGION)
                region_number = (region_number+1) % m

                if sorted_prog_list[prog][1] <= memory_region[region_number][1]:
                    time_exec_start = time_of_memory[region_number]
                    time_exec_end = time_of_memory[region_number] + sorted_prog_list[prog][2]
                    inserting_order_details.append([sorted_prog_list[prog][0], region_number+1, time_exec_start, time_exec_end])
                    time_of_memory[region_number] = time_of_memory[region_number] + time_exec_end

                    break

        # SORTING THE INSERTED ORDER DETAILS ACCORDING TO PROGRAM NUMBER
        final_program_list = sorted(inserting_order_details, key=lambda program: program[0])

        # CALCULATING AVERAGE TURNAROUND TIME
        total_time = 0
        for progs in range(len(final_program_list)):
            total_time = total_time + final_program_list[progs][3]
        avg_turnaround_time = total_time / n

        # PRINTING THE RESULT
        print("case" + str(case))
        print("Average turnaround time = " + str(avg_turnaround_time))
        for progs in range(len(final_program_list)):
            print("Program " + str(final_program_list[progs][0]) + " runs in region " + str(final_program_list[progs][1]) + " from time " + str(final_program_list[progs][2]) + " to " + str(final_program_list[progs][3]))

        case += 1


# ===========================TAKING INPUT FOR PROGRAM LIST==============================================================
def input_prog(n):
    # CREATING A LIST TO STORE PROGRAM LIST
    prog_list = [[0] for y in range(n)]

    # TAKING INPUT TO PROGRAM LIST
    for i in range(n):

        # VALIDATING THE INPUT 'k'
        while True:
            print("program " + str(i+1))
            k = int(input("Enter the K value: "))
            if k < 1 or k > 10:
                print("number of K should be between 1 to 10")
                continue
            break

        # ASSIGNING 'k' AS THE FIRST ELEMENT TO THE PROGRAM LIST
        prog_list[i][0] = k

        # ASSIGNING MINIMUM REQUIRED SIZE OF MEMORY AND EXECUTION TIME PAIR TO THE PROGRAM LIST
        for j in range(k):
            print("K = " + str(j+1))
            ms = int(input("Enter the minimum size required: "))
            t = int(input("Enter the execution time: "))
            prog_list[i].append(ms)
            prog_list[i].append(t)

    # RETURNING THE PROGRAM LIST
    return prog_list


# ===========================FUNCTION TO SELECT THE MINIMUM SPACE INDEX FOR THE GIVEN K VALUE===========================
def get_lowest_exec_time_index(program=[]):

    # SETTING MINIMUM TIME CATCHING VARIABLE VALUE TO MAXIMUM SIZE AND INDEX NUMBER TO -1
    min_time = sys.maxsize
    min_size_index = -1

    # GETTING THE INDEX NUMBER OF THE MINIMUM MEMORY REQUIREMENT SIZE
    for i in range(1, len(program)):
        if i % 2 == 0:
            if min_time > program[i]:
                min_time = program[i]
                min_size_index = i - 1
    return min_size_index


# ===========================SORTING THE PROGRAM LIST===================================================================
def sorting_program_list(n, programs=[]):
    prog_list = [[i+1] for i in range(n)]

    for progs in range(n):
        min_size_index = get_lowest_exec_time_index(programs[progs])
        prog_list[progs].append(programs[progs][min_size_index])
        prog_list[progs].append(programs[progs][min_size_index+1])

    return sorted(prog_list, key=lambda time: time[2])


# ===========================CALLING THE MAIN FUNCTION TO EXECUTE=======================================================
main()
