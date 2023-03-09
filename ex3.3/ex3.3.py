import sys

def main():
    lst = []
    prev_capacity = 0
    for i in range(64):
        lst.append(i)
        capacity = sys.getsizeof(lst) // (8 * 1.125)    #8 bytes and the 12.5% overallocation
        if capacity > prev_capacity:
            print(f"List capacity changed to {capacity}")
            prev_capacity = capacity

if __name__ == '__main__':
    main()
