with open('real.txt') as r, open('imag.txt') as i:
    r_data = 1
    L = list()
    k = 0
    while r_data:
        try:
            k += 1 
            r_data = r.readline()
            print(f"line {k}, value: {r_data} of type {type(r_data).__name__}")
            print(float(r_data))
        except ValueError:
            print(f"file reading is over at line {k}")
            break
            
