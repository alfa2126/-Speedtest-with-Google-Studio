# Description: This code is an example of how to read and write data from a Google Sheet using Python
import gspread                                              
from oauth2client.service_account import ServiceAccountCredentials  
import pandas as pd                              
#########################################################################################################################
# Credenciais do Google Sheets and file path
google_ruta = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive"]
# Credenciais do Google Sheets
credentials = ServiceAccountCredentials.from_json_keyfile_name("name of.json", google_ruta)
client = gspread.authorize(credentials)
sheet = client.create("name") # create a new database
sheet.share('exaple@gmail.com', perm_type='user', role='writer') # share database with mail

##########################################################################################################################
# this code is an example of reading data from the sheet using python
sheet = client.open("name").sheet1
data = sheet.get_all_values()
headers = data.pop(0)
df = pd.DataFrame(data, columns=headers)
# we save the read data in the CSV
df.to_csv("name.csv", index=False)
##########################################################################################################################
# we open the spreadsheet and add a new row with the data                                                                                  
sheet = client.open("name").get_worksheet(0)                                                                
# read csv with pandas 
d = pd.read_csv('name.csv')                                                                              
# export df to a sheet                                                                                   
sheet.update([d.columns.values.tolist()] + d.values.tolist())                                            
##########################################################################################################################