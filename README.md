# API Server

This is a very simple Flask API that takes CSV files in the specified path and return it's contents as JSON.


## Usage

Once run, the API can be accessed from the same machine or another on the network.

https://localhost:5555/<csv file>

It looks for the csv file in the directory specified in the init.conf and tries to return it as a JSON.

If CSV files are in different folders, you can define them in the init.conf files under a section with the same name as the file.

Headers for the file can also be defined in the section with the same name as the CSV File.
