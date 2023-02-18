# -Speedtest-with-Google-Studio
This project consists of a python script that is used to measure the speed of the internet which you can connect to a google sheet to use it as a database and then use the data to create a report in google data studio


<details>
<summary> To activate the Google Sheets API and get the JSON file needed for authentication, follow these steps:</summary>


1) Enter the Google Cloud Console.
    Create a new project if you don't have one already created.  
    ![Ejemplo de imagen](/images/1.jpg)
    
2) In the left side navigation panel, select "APIs and services" and then "Library".
    
   ![Ejemplo de imagen](/images/2.jpg)
    
<details>
<summary> 3) Search for "Google Sheets API" and activate it.</summary>
    
    ![Ejemplo de imagen](/images/3.jpg)
    
</details>

<details>
<summary> 4) In the left side navigation pane, select "APIs and services" and then "Credentials".</summary>

   ![Ejemplo de imagen](/images/4.jpg)
   ![Ejemplo de imagen](/images/5.jpg)

</details>

 <details>
<summary> 5)  Click the "Create Credentials" button and select "Service Account." </summary>


   ![Ejemplo de imagen](/images/6.jpg)
   ![Ejemplo de imagen](/images/7.jpg)

</details>
  
    
<details>
<summary> 6) Enter a name for the service account and select the "Editor" role.
In the "Keys" section, click the "Create Key" button and select "JSON File".</summary>

   ![Ejemplo de imagen](/images/7.jpg)
   ![Ejemplo de imagen](/images/8.jpg)

         
A JSON file containing the credentials needed to access the Google Sheets API will be downloaded. Store it in a safe place.
Remember to take security precautions when handling this JSON file, as it contains sensitive information from your Google account.
</details>    
</details>


   
     
    
   
    
  
    
     


    
     
    
    
