def get_report_data():
    x=1
    values = []
    #To match the input format , press enter twice after pasting the values.
    while x==1:
        m = input()
        if m=="":
            x=0
        else: 
            values.append(int(m))

    c = values[0]
    n = values[1]
    weights = values[2:]
    ids = input("Create a shipmentID: ")

    return ids,c,n,weights

def save_report_data(data):
    ids,c,n,weights = data
    report = (
        f"Shipment_ID: {ids}\n"
        f"{c}\n"
        f"{n}\n"
        f"{weights}\n"
        f"{'-' * 80}\n"
    )
    with open("./Solution/reports.txt","a") as storage:
        storage.write(report)

