import create_report
import report_loader
import functions

cat = r"""
 /\_/\ ♥
 >^,^<
  / \
 (___)_/"""

functions.clear_screen()
while True:
    print("-"*80)
    print(f" 1. Create a new port shipment report\n 2. Load an old port shipment report\n 3. Meow\n 4. Exit")
    print("-"*80)
    try: 
        s = int(input("Select: "))
        if s==1:
            functions.clear_screen()
            data = create_report.get_report_data()
            create_report.save_report_data(data)
            print("REPORT IS SAVED.\n")
        elif s==2:
            functions.clear_screen()
            report_loader.report_viewer()
        elif s==3:
            functions.clear_screen()
            print(cat)
        elif s==4:
            functions.clear_screen()
            print("Closing application.....") 
            break
        else:
            print("Please enter a valid number!")

    except ValueError:
        print("Please enter a valid number!")
        continue


