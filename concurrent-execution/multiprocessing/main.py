import multiprocessing

def print_cube(num):
    print("Cube: ", num * num * num)

def print_square(num):
    print("Square: ", num * num)

if __name__ == "__main__":
    process1 = multiprocessing.Process(target= print_square, args= (10,))
    process2 = multiprocessing.Process(target= print_cube, args= (10,))
    
    process1.start()
    process2.start()

    #wait till process 1 is finished
    process1.join()
    #wait till process 2 is finished
    process2.join()

    print("done executing")

