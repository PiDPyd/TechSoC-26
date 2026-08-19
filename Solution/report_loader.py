import functions

def report_viewer():
    try:
        with open("./Solution/reports.txt","r") as storage:
            content = storage.read()
            reports = content.split("-" * 40)
            cleaned = []
            for r in reports:
                if r.strip():
                    cleaned.append(r.strip())
            reports = cleaned

            itemized_list = []
            for items in reports:
                data_entries = items.split("\n")
                itemized_list.append(data_entries)

            functions.clear_screen()
            for i in range(len(itemized_list)):
                print(f"{i+1}. {itemized_list[i][0]}")

            try:
                reportid = int(input("Enter the number beside shipmentID to perform functions: \n"))
                listid = reportid - 1
                c=int(itemized_list[listid][1])
                n=int(itemized_list[listid][2])
                weights=list(map(int, itemized_list[listid][3].strip("[]").split(",")))
                functions.clear_screen()
                while True:
                    print(itemized_list[listid][0]+" Has been selected.")
                    print("-"*80)
                    print(" 1. View basic shipment report.\n 2. Sorted Display\n 3. Bar Chart\n 4. Search container by weight\n 5. Find Nth heaviest\n 6. Main menu")
                    print("-"*80)
                    try:
                        selector = int(input("Select: "))
                        if selector==1:
                            functions.clear_screen()
                            print(functions.basic_report(c,n,weights))
                        elif selector==2:
                            functions.clear_screen()
                            items = functions.sorted_display(weights)
                            print("-"*80)
                            print("Sorted items are as follows: ")
                            for i in range(len(items)):
                                print(f"{i+1}. {items[i]}")
                            print("-"*80)
                        elif selector==3:
                            functions.clear_screen()
                            functions.bar_chart(weights)
                        elif selector==4:
                            functions.clear_screen()
                            item = int(input("Enter weight you wanna search: "))
                            results = functions.search(weights, item)
                            print(results)
                            if results == {}:
                                print("-"*80)
                                print("No such item found!")
                                print("-"*80)
                            else:
                                print("-"*80)
                                print(f"Container found!")
                                for i in results:
                                    print(f"Container {results[i]} has weight {i}")
                                print("-"*80)
                                
                        elif selector==5:
                            items = functions.sorted_display(weights)
                            functions.clear_screen()
                            kth = int(input("Enter K for K'th heaviest: "))
                            print(f"The {kth} heaviest container weighs {items[kth-1]}")
                        elif selector==6:
                            functions.clear_screen()
                            break
                        else:
                            print("Please enter a valid selection number!")
                            functions.clear_screen()
                        
                    except ValueError:
                        print("Please enter a valid selection number!")
                        functions.clear_screen()
                        continue
            except ValueError:
                print("Please enter a valid selection number!")
            except IndexError:
                print("Selected report does not exist!")
                    
    except FileNotFoundError:
        print("No reports made yet, Create reports to load them!")
