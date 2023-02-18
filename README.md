# -Speedtest-with-Google-Studio
This project consists of a python script that is used to measure the speed of the internet which you can connect to a google sheet to use it as a database and then use the data to create a report in google data studio



Next I will describe the steps to make it work in code.
We must first create a virtual environment before installing the dependencies that will allow our code to function

1) create a virtual environment python -m venv virtual

We already have the virtual environment installed, we can proceed with its activation    
   2) we activate the virtual environment 
    .\virtual\Scripts\activate
    
Now we are going to install the dependencies in our virtual environment
and I will explain the libraries that we are going to use in our code


1) os: This library provides a way to interact with the operating system. In this case, it is used to set the TK_SILENCE_DEPRECATION environment variable to 1, which prevents deprecation warnings from being displayed in the console output.
To install this library, you don't need to do anything, since it comes included with Python.

2) time: This library provides functions to work with time. In this case, it is used to measure the duration of an operation.
To install this library, you don't need to do anything, as it is also included with Python.

3) pandas: This library is a popular tool for data analysis and manipulation in Python. In this case, it is used to work with tabular data.
To install this library, you can use pip, the Python package manager, by running the following command at the command line: pip install pandas.

4) threading: This library provides an approach to working with threads in Python. In this case, it is used to execute a function on a separate thread.
To install this library, you don't need to do anything, as it is also included with Python.

5) speedtest: This library provides a way to measure the speed of the Internet. In this case, it is used to measure download and upload speed.
To install this library, you can use pip, by running the following command on the command line: pip install speedtest-cli.

6) socket: This library provides a way to interact with sockets in Python. In this case, it is used to obtain information about the IP address of the system.
To install this library, you don't need to do anything, as it is also included with Python.

7) gspread: This library provides an interface to work with Google spreadsheets. In this case, it is used to write the speed test results to a spreadsheet.
To install this library, you can use pip by running the following command at the command line: pip install gspread.

To use gspread, you will also need to install oauth2client. You can install it using pip by running the following command at the command line: pip install oauth2client.    
    
