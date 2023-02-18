import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
import time
import pandas as pd
import threading
import speedtest as st
import socket
import gspread                          
from oauth2client.service_account import ServiceAccountCredentials  
google_ruta = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("name of.json", google_ruta)
client = gspread.authorize(credentials)

#  dataframe
df = pd.DataFrame(columns=['Speed_down','speed_up','Ping','ra_co','da_co','Status','Hora','Today'])
# We save the titles of the columns 
df.to_csv('name.csv', mode='a', header=True)
# we open the spreadsheet and add a new row with the data                                                                                  
sheet = client.open("name").get_worksheet(0) 
# read csv with pandas
d = pd.read_csv('name.csv')
# export df to a sheet
sheet.update([d.columns.values.tolist()] + d.values.tolist())
time.sleep(1)

# function to measure internet speed and save the data in a csv
def speedtest():
    global hora_co
    global today_co
    global status
    global hora_des
    global today_des
    # inicilisamos variables 
    hora_co = 0
    today_co = 0
    status = 0
    hora_des = 0
    today_des = 0

    # Set Best Server
    server = st.Speedtest()
    server.get_best_server()

    while True:
        try:
            # Test Download Speed
            down = server.download()
            down = down / 1000000
            down = round(down,2)
            # Test Upload Speed
            up = server.upload()
            up = up / 1000000
            up = round(up,2)
            # Test Ping
            ping = server.results.ping
            ping = round(ping,2)
            # verificamos la conexion a internet
            try:
                socket.create_connection(("www.google.com", 80))
                print("Connected")
                hora_des = time.strftime("%H:%M:%S")
                today_des = time.strftime("%m/%d/%y")
                status= "OK"
            except OSError:
                status= "off"
                print("No internet")
                hora_co = time.strftime("%H:%M:%S")
                today_co = time.strftime("%m/%d/%y")
            
            # add the data to the dataframe
            df.loc[len(df)] = [down,up,ping,hora_co,today_co,status,hora_des,today_des]
            # we save the dataframe in a csv file
            df.to_csv('name.csv', mode='a', header=False)
            # we open the spreadsheet and add a new row with the data                                                                                  
            sheet = client.open("name").get_worksheet(0) 
            # read csv with pandas
            d = pd.read_csv('name.csv')
            # export df to a sheet
            sheet.update([d.columns.values.tolist()] + d.values.tolist())
            time.sleep(1)
            # we display the dataframe in a sorted table
            print(df.to_string(index=False))
        except KeyboardInterrupt:
            break
        time.sleep(60)

# we execute in a threads

thread2 = threading.Thread(target=speedtest)
thread2.start()


