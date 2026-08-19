# How to use Cargo Manager

---

### Workings of the program
The program is upgraded to a multiport and multiship manager. [No unique ship and port identification, it works on individual report basis]
To begin with You need to create a report, provide any shipment-ID you want, Enter the data [Same input format as given in Level-1]
press **Enter** when you all the weights have been entered.
the program saves the report for the respective port and shipment in a txt file.

You can now perform actions for each shipment report you give, by loading it.
Upon loading it 
1. Viewing basic report is Solution of Level-1 
2. other Options are solutions of individual parts of Level-2

## Run main.py to start the program

---

### Custom features

1. Stylized the whole program
2. Added Error handling
3. Added multiport managing , on individual report basis
4. Integrated both problem statements into a application


### To maintain clean code , code has been divided into modules.
```
report_loader.py──────►Main.py◄──────create_report.py
        ▲                ▲
        └───────┬────────┘
                ▲
           Functions.py
```