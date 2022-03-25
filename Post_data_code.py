#author:Arjun D
#date:25-3-2022

from array import array
import csv
import json
from re import X
import string
import numpy
from numpy import loadtxt



def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
   
      
    #read csv file
    with open(csvFilePath, 'r') as csvf: 
       
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader:
            #add this python dict to json array
            jsonArray.append(row)
      
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath,'w') as jsonf:
        jsonString = json.dumps(jsonArray,indent=100)  
         
        #convert json to string data
        d2 = json.loads(jsonString)
        a = { "index":{} }
       # for i in range(len(d2)):
         #print(a)
        for object in d2:
         #print(object)
        
         numpy.savetxt(jsonf,[a,object],newline='\n\n',fmt='%s')
      
 
csvFilePath = r'C:\Users\arju3\OneDrive\Desktop\ECE_BR\ECE_BR.csv'
jsonFilePath = r'C:\Users\arju3\OneDrive\Desktop\converted_CSV_file\HDFC_BANK_NODE_123.txt'
csv_to_json(csvFilePath,jsonFilePath)


