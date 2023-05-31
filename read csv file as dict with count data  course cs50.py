

import csv 
# make values 0 
houses={"Gryffindor":0,
        "Slytherin":0,
        "Ravenclaw":0,
        "Hufflepuff":0}
#open file
with open(r"C:\Users\Mohamed Assem\Downloads\houses.csv","r") as f:
    reader=csv.reader(f)
    next(reader) # to skip the head 
# search for values in csv file 
    for row in reader:
        #add values to dict 
        houses[row[1]]+=1
        
        
#print dict values
for i in houses.items():
    print(f"{i[0]}:{i[1]}")
        
        
        
    
