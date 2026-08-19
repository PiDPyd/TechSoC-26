ship = r"""     ~~~             |
~~~~     ~~~~      -----                    |
     ~~~           )___(                  -----
                     |                    )___(
                 ---------                  |
                /         \              -------
               /___________\            /       \
                     |                 /_________\
              ---------------               |
             /               \        -------------
            /                 \      /             \
           /___________________\    /_______________\
         ____________|______________________|__________
          \_                                        _/
            \______________________________________/
     ~~..             ...~~~.           ....~~~...     ..~
"""

txt = r""" ██████╗ █████╗ ██████╗  ██████╗  ██████╗                     
██╔════╝██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗                    
██║     ███████║██████╔╝██║  ███╗██║   ██║                    
██║     ██╔══██║██╔══██╗██║   ██║██║   ██║                    
╚██████╗██║  ██║██║  ██║╚██████╔╝╚██████╔╝                    
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝                     
                                                              
███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝"""

def clear_screen():
    print("\033[H\033[J", end="")
    print(ship)
    print(txt)

weights_unsorted=[]

def basic_report(port_capacity,no_of_containers,weights_list):
    global weights_unsorted
    c = port_capacity
    n = no_of_containers
    weights = weights_list
    weights_unsorted = weights_list

    total_shipment_weight = 0
    for i in range(n):
        total_shipment_weight += weights[i]

    average_container_weight = total_shipment_weight/n

    heaviest_container = max(weights)
    lightest_container = min(weights)

    if total_shipment_weight>=200:
        classification="Heavy"
    else:
        classification="Light"

    if total_shipment_weight<=c:
        status = "Shipment can be unloaded"
    else:
        status = "Shipment exceeds port capacity"

    print(f"Total Shipment Weight: {total_shipment_weight}\n Average Container Weight: {average_container_weight}\n Heaviest Container: {heaviest_container}\n Lightest Container: {lightest_container}\n Classification: {classification}\n Port Capacity: {c}\n Status: {status}")

def sorted_display(unsorted_list):
    sorted_list = [None]*len(unsorted_list)
    index_list = []
    for i in unsorted_list:
        greatness_capacity = 0
        for j in unsorted_list:
            if i < j:
                greatness_capacity += 1
        index_list.append(greatness_capacity)

    for i in range(len(unsorted_list)):
        sorted_list[index_list[i]] = unsorted_list[i]

    return sorted_list

def bar_chart(weights_list):
    for i in range(len(weights_list)):
        multiplier = round(weights_list[i]/5)
        print(f"Container {i} ({weights_list[i]}) : "+"▢"*multiplier)
    print("Each ▢ is 5 units")

def search(container_list, item):
    search_result = {}
    interation_number = 0
    for i in container_list:
        interation_number+=1
        if i==item:
            search_result[i] = interation_number
        
    return search_result
