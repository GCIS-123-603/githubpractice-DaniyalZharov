import random

def random_list(size):
    return [random.randint(0, 100) for _ in range(size)]

def sorted_test(a_list):
    print("Original list:", a_list)
    sorted_list = sorted(a_list)
    print("Sorted list:", sorted_list)

def main():
    list_of_randoms = random_list(10)
    sorted_test(list_of_randoms)

if __name__ == "__main__":
    main()