# Retrieval of data from a json 
This function and primary aim of this repo is to retrieve data from a json(data) file

- ##  [roster_data.json](https://github.com/chryzcodez/py-projects/blob/master/all-python-codes/retrieve-school-data/roster_data.json)
    **Note:**_This file was made available for the tweaking and test-running of the python codes/ program made available in this repo!
    
    This is a json file that is filled with data in which we are going to be parsing and printing out our desired piece of data/ information needed or intented.
    ```json
    [
    "Gaia",
    "si110",
    1
  ],
  [
    "Rio",
    "si110",
    0
  ]
  ```
  A block of the json code/ program is exactly like this code snippet above. 
  - **"Gaia"**: Is represented here as the name of a teacher.
  - **"si110"**: is represented as the course taught by the teacher aformentioned.
  - **"1"**: is represented as here as a tescher's post
  - **"0"**: is represented as here as the post of a student
  
- ## [rosterdb.py](https://github.com/chryzcodez/py-projects/blob/master/all-python-codes/retrieve-school-data/rosterdb.py)
   The other python file `rosterdb.py` is python code with a bit of sqlite. This code is to retrieve your data and store it into an sqlite database for later use. To use this you need to download an sqlite browser [here](https://sqlitebrowser.org/dl/).
   
- ## [rosters.py](https://github.com/chryzcodez/py-projects/blob/master/all-python-codes/retrieve-school-data/rosters.py)
    This is same as the the `rosterdb.py` python file except from the sqlite database which this code does not have. You can simply run it on your terminal and get your data without saving any pich of it.
