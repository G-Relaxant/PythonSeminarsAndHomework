import datetime
 
a = datetime.datetime.today().strftime("%Y%m%d")
print(a) # 20230502
 
today = datetime.datetime.today()
print(today.strftime("%m/%d/%Y") ) # 05/02/2023
 
print(today.strftime("Data: %d-%m-%y") )  # Data: 02-05-23
print(today.strftime("Vremya: %H.%M.%S")) # Vremya: 18.36.40

print(today) # 2023-05-02 18:36:40.212582
