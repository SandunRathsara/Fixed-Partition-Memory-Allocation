def main():
    m = int(input("Enter the number of memory partitions:"))
    n = int(input("Enter the number of programs: "))
    mSize = []

    for i in range(m):
        size = int(input("Enter the size of the memory partition "+str(i+1)+":"))
        mSize.append(size)

    for i in range(n):


main()