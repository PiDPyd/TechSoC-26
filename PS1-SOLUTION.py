#nbh = neighbourhood
#gen = generation
#all inputs start with Capital Letter
import time

title = r""" ▄████▄   ▒█████   ███▄    █  █     █░ ▄▄▄     ▓██   ██▓  ██████      ▄████  ▄▄▄       ███▄ ▄███▓▓█████  ▒█████   ██▓     ██▓  █████▒▓█████ 
▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █ ▓█░ █ ░█░▒████▄    ▒██  ██▒▒██    ▒     ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▒██▒  ██▒▓██▒    ▓██▒▓██   ▒ ▓█   ▀ 
▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▒█░ █ ░█ ▒██  ▀█▄   ▒██ ██░░ ▓██▄      ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   ▒██░  ██▒▒██░    ▒██▒▒████ ░ ▒███   
▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒░█░ █ ░█ ░██▄▄▄▄██  ░ ▐██▓░  ▒   ██▒   ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ ▒██   ██░▒██░    ░██░░▓█▒  ░ ▒▓█  ▄ 
▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░░░██▒██▓  ▓█   ▓██▒ ░ ██▒▓░▒██████▒▒   ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒░ ████▓▒░░██████▒░██░░▒█░    ░▒████▒
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▓░▒ ▒   ▒▒   ▓▒█░  ██▒▒▒ ▒ ▒▓▒ ▒ ░    ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░▓  ░░▓   ▒ ░    ░░ ▒░ ░
  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░  ▒ ░ ░    ▒   ▒▒ ░▓██ ░▒░ ░ ░▒  ░ ░     ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░  ░ ▒ ▒░ ░ ░ ▒  ░ ▒ ░ ░       ░ ░  ░
░        ░ ░ ░ ▒     ░   ░ ░   ░   ░    ░   ▒   ▒ ▒ ░░  ░  ░  ░     ░ ░   ░   ░   ▒   ░      ░      ░   ░ ░ ░ ▒    ░ ░    ▒ ░ ░ ░       ░   
░ ░          ░ ░           ░     ░          ░  ░░ ░           ░           ░       ░  ░       ░      ░  ░    ░ ░      ░  ░ ░             ░  ░
░                                               ░ ░                                                                                         """

MAX_GRID_SIZE = 100
MAX_GENERATIONS = 1000

#Cosmetic function
def clear_screen():
    print("\033[H\033[J", end="")
    print(title)

#Cosmetic function
def show_generation(gen: list):
    for row in gen:
        for column in row:
            print(column, end=" ")
        print()

#Cosmetic function
def show_animation(gen_audit: list, interval=1):
    clear_screen()
    for gen in gen_audit:
        show_generation(gen)
        time.sleep(interval)
        clear_screen()

#Essential Functions 
def check_population(gen: list):
    population=0
    for row in gen:
        for col in row:
            if col=="#":
                population+=1
    return population

#Essential Functions 
def check_nbh_population(nbh: list):
    population=0
    for cell in nbh:
        if cell=="#":
            population+=1
    return population

#Essential Functions
def view_nbh(row: int, col: int, array: list, mode: int):
    #Because size is len but index is size-1
    indx_rw_len = len(array)-1
    indx_cl_len = len(array[0])-1
    the_hood= [-1,0,1]
    nbh = []
    for drow in the_hood:
        for dcol in the_hood:
            if mode==1:
                cr = row+drow
                cc = col+dcol
                if drow==0 and dcol==0:
                    continue
                elif (cr<0 or cr>indx_rw_len) or (cc<0 or cc>indx_cl_len):
                    continue
                else:
                    nbh.append(array[cr][cc])
            else:
                cr = (row+drow+(indx_rw_len+1)) % (indx_rw_len+1)
                cc = (col+dcol+(indx_cl_len+1)) % (indx_cl_len+1)
                if drow==0 and dcol==0:
                    continue
                else:
                    nbh.append(array[cr][cc])     
    return nbh

#Main function (Accepts Mode = 1 / 2)
def gen_iterations(array: list, mode: int, iterations: int):
    initial_population = check_population(array) 
    gen_population_log = [] 
    gen_population_log.append(initial_population)

    gen_audit = [] 
    gen_audit.append([i.copy() for i in array])

    for i in range(iterations):
        previous_gen = gen_audit[-1]
        for r in range(len(array)):
            for c in range(len(array[0])):
                if previous_gen[r][c]=="#":
                    nbh = check_nbh_population(view_nbh(r,c,previous_gen,mode))
                    if nbh<2:
                        array[r][c]="."
                    elif nbh>3:
                        array[r][c]="."
                else:
                    if check_nbh_population(view_nbh(r,c,previous_gen,mode)) == 3:
                        array[r][c]="#"

        gen_population_log.append(check_population(array))
        gen_audit.append([i.copy() for i in array])

    return gen_population_log,gen_audit

#Feature Function
def auto_pattern_classifier(array: list, mode: int, step=10):
    #copiying the array
    self_array = [i.copy() for i in array]
    simulations = gen_iterations(self_array, mode, step) #running iterations again cz stepsize can be bigger than original iterations given.
    audit = simulations[1]

    dead_life=False
    if 0 in simulations[0]:
        dead_life=True        

    period = 0
    for i in range(step):
        found = False
        for j in range(i+1):
            if audit[i+1]==audit[j]:
                period=i+1-j
                found = True
                break

        if found == True:
            break

    print(f"Auto-Classifier Verdict [at step size {step}]")
    if dead_life==True:
        print("Classification: Extinct")
    elif period==1:
        print("Classification: Still life")
    elif period>1:
        print(f"Classification: Oscilatory period => {period}")
    else:
        print("Classfication: Active life")
    

#Feature Functions
def combb(array):
    rows=[]
    cols=[]
    for r in range(len(array)):
        for c in range(len(array[0])):
            if array[r][c]=="#":
                rows.append(r)
                cols.append(c)

    N = len(rows)
    if N!=0:
        H = max(rows) - min(rows)+1
        W = max(cols) - min(cols)+1
        com = (round(sum(rows)/N,2) , round(sum(cols)/N,2))
        print(f"Live cells: {N}")
        print(f"Bounding Box: {H} x {W} (Rows {min(rows)}-{max(rows)}, Cols {min(cols)}-{max(cols)})")
        print(f"Center of Mass: {com}")
    else:
        print(f"Live cells: 0")
        print(f"Bounding Box: 0 x 0")
        print(f"Center of Mass: N/A")


print(title)
while True:
    print("Provide a grid to start performing actions on it... [In the input format]")
    try:    
        RnC = list(map(int, input().split(" ")))
    
        if len(RnC)==2:
            Iterations = int(input())
            array = []
            for i in range(RnC[1]):
                Row = input()
                if len(list(Row))==RnC[0]:
                    array.append(list(Row))
                else: 
                    raise ValueError("ERR: Insufficient row size.")
                

            if 1<=RnC[0]<=MAX_GRID_SIZE and 1<=RnC[1]<= MAX_GRID_SIZE and 0<= Iterations <=MAX_GENERATIONS:
                clear_screen()
                print("Grid accepted, Choose generation mode.")
                print("1. Normal Game\n2. Toroidal-Wrap Game\n")
                Mode = int(input("Choose Mode: "))
                clear_screen()
                simulation = gen_iterations(array, Mode, Iterations)
                print("Simulation overview: ")
                print(f"Initial population: {simulation[0][0]}")
                print(f"Final population: {simulation[0][-1]}")
                print(f"Peak population: {max(simulation[0])}")
                print("Final State of Grid:")
                show_generation(simulation[1][-1])
                print("-"*80)
                print("Press 'Enter' to continue...")
                input()
                while True:
                    clear_screen()
                    print("Perform actions on your simulation => \n1. Auto-Pattern Classifier\n2. Custom step Auto-Pattern Classifer\n3. COM and Bounding Box [Applied to Starting grid]\n4. Live cell Replay\n5. Exit")
                    Action = int(input("Choose Action: "))
                    if Action==1:
                        clear_screen()
                        auto_pattern_classifier(simulation[1][0], Mode)
                        print("Press 'Enter' to continue...")
                        if input()=="":
                            continue
                    elif Action==2:
                        clear_screen()
                        Stepsize = int(input("Enter custom step: "))
                        auto_pattern_classifier(simulation[1][0], Mode ,Stepsize)
                        print("Press 'Enter' to continue...")
                        if input()=="":
                            continue
                    elif Action==3:
                        clear_screen()
                        combb(simulation[1][0])
                        print("Press 'Enter' to continue...")
                        if input()=="":
                            continue
                    elif Action==4:
                        ms = input("Press 'Enter' for given simulation or type custom animation interval(sec): ")
                        clear_screen()
                        if ms=="":
                            show_animation(simulation[1])
                        else:
                            show_animation(simulation[1],float(ms))
                        print("Press 'Enter' to continue...")
                        if input()=="":
                            continue
                    elif Action==5:
                        clear_screen()
                        break
                    else:
                        clear_screen()
                        print("ERR: Chose a valid action")

            else:
                clear_screen()
                print("ERR: Overflow of allowed grid size or generation iterations")

        else:
            clear_screen()
            print("ERR: Enter valid input format!")

    except:
            clear_screen()
            print("ERR: Enter valid input format!")
