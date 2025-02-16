from tabulate import tabulate
import json

filepath='data_rental.txt'

def loadData():
    try: 
        with open(filepath) as f:
            dataMobil = json.load(f)
            return dataMobil
    except Exception:
        dataMobil = [
    {
        'Registration': 'PR-01',
        'Merk': 'Toyota',
        'Tipe': 'Avanza',
        'Bahan_bakar': 'Bensin',
        'Tahun': 2012,
        'Plat': "D 6478 AN",
        'Ketersediaan': "Tersedia"
    },
    {
        'Registration': 'PR-02',
        'Merk': 'Toyota',
        'Tipe': 'Innova',
        'Bahan_bakar': 'Bensin',
        'Tahun': 2017,
        'Plat': "B 3878 BL",
        'Ketersediaan': "Tidak Tersedia"
    },
    {
        'Registration': 'PR-03',
        'Merk': 'Toyota',
        'Tipe': 'Innova',
        'Bahan_bakar': 'Bensin',
        'Tahun': 2017,
        'Plat': "B 3878 UXJ",
        'Ketersediaan': "Tersedia"
    },
    {
        'Registration': 'PR-04',
        'Merk': 'Ford',
        'Tipe': 'Focus',
        'Bahan_bakar': 'Bensin',
        'Tahun': 2020,
        'Plat': "B 4558 SHG",
        'Ketersediaan': "Tidak Tersedia"
    },
]
        return dataMobil

def MainMenu():
    while True:
        print("=================")
        print("PURWADHIKA CAR RENTAL")
        print("=================")
        print("1. Read")
        print("2. Create")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        print("=================") 
        menu_input=input("Please Select Menu Option: ")
        match menu_input:
            case "1":
                ReadMenu()
                break
            case "2":
                CreateMenu()
                break
            case "3":
                UpdateMenu()
                break
            case "4":
                DeleteMenu()
                break
            case "5":
                break
            case _:
                print("Wrong Input, Please Input Selection That Are Available!")

def filtering(filter_options):
    filteredData=[]
    for i in range(len(dataMobil)):
        if filter_options in dataMobil[i].values():
            filteredData.append(dataMobil[i])
    return filteredData
                
def ReadMenu():
    print("=================")
    print(" DISPLAY CARS   ||")
    print("=================")
    while True:
        print("Filtering Options:")
        print("1. Display All Data")
        print("2. Registration ID")
        print("3. Ketersediaan")
        print("4. Plat Nomor")
        print("5. Bahan Bakar")
        print("6. Merk")
        print("7. Tahun")
        print("8. Back")
        print("=================")
        menu_input=input("\nPlease Select Menu Option: ")
        match menu_input:
            case "1":
                if not dataMobil:
                    print("=================")
                    print("Data Doesn't Exist!")
                    print("=================")
                else:
                    print(tabulate(dataMobil, headers="keys", tablefmt='rst', showindex='always'))
            case "2":
                if dataMobil:
                    filter_options=input("Insert Registration ID: ")
                    filteredData=filtering(filter_options)
                    if filteredData:
                        print(tabulate(filteredData, headers="keys", tablefmt='rst', showindex='always'))
                    else:
                        print("=================")
                        print("Data Doesn't Exist!")
                        print("=================")
                else:
                    print("=================")
                    print("Data Doesn't Exist!")
                    print("=================")
            case "3":
                if dataMobil:
                    filteredData=filtering("Tersedia")
                    if filteredData:
                        print(tabulate(filteredData, headers="keys", tablefmt='rst', showindex='always'))
                    else:
                        print("=================")
                        print("Data Doesn't Exist!")
                        print("=================")
                else:
                    print("=================")
                    print("Data Doesn't Exist!")
                    print("=================")
            case "4":
                if dataMobil:
                    filter_options=input("Insert Car License Plate: ")
                    filteredData=filtering(filter_options)
                    if filteredData:
                        print(tabulate(filteredData, headers="keys", tablefmt='rst', showindex='always'))
                    else:
                        print("=================")
                        print("Data Doesn't Exist!")
                        print("=================")
                else:
                    print("=================")
                    print("Data Doesn't Exist!")
                    print("=================")
            case "5":
                if dataMobil:
                    filter_options=input("Insert Fuel Type: ")
                    filteredData=filtering(filter_options)
                    if filteredData:
                        print(tabulate(filteredData, headers="keys", tablefmt='rst', showindex='always'))
                    else:
                        print("=================")
                        print("Data Doesn't Exist!")
                        print("=================")
                else:
                    print("=================")
                    print("Data Doesn't Exist!")
                    print("=================")
            case "6":
                if dataMobil:
                    filter_options=input("Insert Car Brand: ")
                    filteredData=filtering(filter_options)
                    if filteredData:
                        print(tabulate(filteredData, headers="keys", tablefmt='rst', showindex='always'))
                    else:
                        print("=================")
                        print("Data Doesn't Exist!")
                        print("=================")
                else:
                    print("=================")
                    print("Data Doesn't Exist!")
                    print("=================")
            case "7":
                if dataMobil:
                    filter_options=input("Insert Car Year: ")
                    filteredData=filtering(filter_options)
                    if filteredData:
                        print(tabulate(filteredData, headers="keys", tablefmt='rst', showindex='always'))
                    else:
                        print("=================")
                        print("Data Doesn't Exist!")
                        print("=================")
                else:
                    print("=================")
                    print("Data Doesn't Exist!")
                    print("=================")
            case "8":
                MainMenu()
                break
            case _:
                print("Wrong Input, Please Input Selection That Are Available!")
                
def CreateMenu():
    while True:
        print("\n=================")
        print("ADD NEW CAR")
        print("=================")
        print("Menu Selection:")
        print("1. Add Car Details")
        print("2. Back")
        menu_input=input("\nPlease Select Menu Option: ")
        match menu_input:
            case "1":
                insertData()
            case "2":
                MainMenu()
                break
            case _:
                print("Wrong Input, Please Input Selection That Are Available!")
        
def insertData():
    newcar_list=[]
    x=1
    while True:
        car_plate=input("Insert Car Plate Number: ")
        if any(data.values() == car_plate for data in dataMobil):
            print("Car Already Exist!")
            break
        else:
            car_brand=input("Insert Car Brand: ")
            car_type=input("Insert Car Type: ")
            car_fuel=input("Insert Car Fuel Type: ")
            car_year=int(input("Insert Car Year: "))
            print(car_fuel)
            if not (car_brand and car_type and car_fuel and car_year and car_plate):
                return print('\nCar Details Cannot Be Empty!')
            elif car_year>2025 or type(car_year)!=int:
                return print("\nThe Car hasn't been produced yet")
            elif car_year<2016 or type(car_year)!=int:
                return print("\nThe Car is too old!")
            elif (car_fuel!="Bensin") and (car_fuel!="Diesel"):
                return print("Car Fuel Must Be 'Bensin' or 'Diesel'!")
            newData={
                        'Registration': 'PR-0'+str(len(dataMobil)+x),
                        'Merk': car_brand,
                        'Tipe': car_type,
                        'Bahan_bakar': car_fuel,
                        'Tahun': car_year,
                        'Plat': car_plate,
                        'Ketersediaan': "Tersedia"
                    }
            newcar_list.append(newData)
            print(tabulate(newcar_list, headers="keys", tablefmt='rst', showindex='always'))
            menu_input=input("Add More Cars? \n1. Yes\n2. No\nMenu Selection: ")
            match menu_input:
                    case "1":
                        x+=1
                    case "2":
                        saveData(newcar_list)
                        break
                    case _:
                        print("Wrong Input, Please Input Selection That Are Available!")

def exportData():
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(json.dumps(dataMobil))

def saveData(car):
    for i in range(len(car)):
        dataMobil.append(car[i])
    return dataMobil, print("Car Details Saved Successfully!")

def UpdateMenu():
    while True:
        print("\n=================")
        print("UPDATE CAR DETAILS")
        print("=================")
        print("Menu Selection:")
        print("1. Update Car Details")
        print("2. Back")
        menu_input=input("\nPlease Select Menu Option: ")
        match menu_input:
            case "1":
                idx=findData()
                changeData(idx)
            case "2":
                MainMenu()
                break
            case _:
                print("Wrong Input, Please Input Selection That Are Available!")
                
def findData():
    idx=0
    while True:
        print("\n=================")
        print("CAR LISTS")
        print("=================")
        print(tabulate(dataMobil, headers="keys", tablefmt='rst', showindex='always'))
        car_reg=input("Insert Car ID: ")
        for i in range(len(dataMobil)):
            if car_reg == dataMobil[i]['Registration']:
                idx=i
                print('\n'+tabulate([dataMobil[idx]], headers="keys", tablefmt='rst', showindex='always'))
                return idx
        if idx == 0:
            print("Data Doesn't Exist!")
            
def changeData(i):
    while True:
        print("Do you want to edit this car detail?:")
        print("1. Yes")
        print("2. No")
        print("=================")
        menu_input=input("Menu Selection:")
        match menu_input:
            case "1":
                try:
                    column_input=input("Select Column Name:")
                    data_input=input("Input Data: ")
                except Exception as e:
                    print("Wrong input, Please try again!")
                finally:
                    while True:
                        decision_input=input("\nAre you sure to edit this record? \n1. Yes\n2. No\nMenu Selection: ")
                        match decision_input:
                            case "1":
                                if column_input == "Tahun":
                                    dataMobil[i][column_input]=int(data_input)
                                else:
                                    dataMobil[i][column_input]=data_input
                                print("Changes Saved!")
                                exportData()
                            case "2":
                                break
                            case _:
                                print("Wrong Input, Please Try Again!")
                break
            case "2":
                break
            case _:
                print("Wrong Input, Please try again!")
        
def DeleteMenu():
    while True:
        print("\n=================")
        print("DELETE CAR DETAILS")
        print("=================")
        print("Menu Selection:")
        print("1. Delete By Registration ID")
        print("2. Back")
        menu_input=input("Menu Selection:")
        match menu_input:
            case "1":
                idx=findData()
                deleteData(idx)
                exportData()
            case "2":
                MainMenu()
                break
            case _:    
                print("Wrong input, please try again!")
    return

def deleteData(i):
    while True:
        print("Do you want to delete this car?:")
        print("1. Yes")
        print("2. No")
        print("=================")
        menu_input=input("Menu Selection:")
        match menu_input:
            case "1":
                print(i)
                dataMobil.pop(i)
                print('Data deleted succesfully!')
                break
            case "2":
                break
            case _:
                print("Wrong Input, Please try again!")

#Main Function
dataMobil=loadData()       
MainMenu()