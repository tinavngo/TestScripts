# Python Recipe App

## Getting started

  1. Install Python v3.8
  2. Set Up a virtual environment
  ```powershell
  mkvirtualenv python-environment
  ```
  3. Create a Python Script
  4. Create a requirements.txt file in virtual environment
  ```powershell 
  pip freeze > requirements.txt
  ```
  5. Create a copy version of original virtual environment
  ```powershell
  mkvirtualenv python-environment-copy
  ```
  5. Copy requirements.txt file into virtual environment copy
  ```powershell
  pip install -r requirements.txt
  ```

## Why Dictionary Data Type?
The dictionary data type is the most suitable data type for the goal of the recipe app. It follows a key:value pair which allows for immutable data types to be within the same data structure. The stucture for a recipe requires: strings, integers and lists which is all possible when using the dictionary. The nature of the structure is sequential, so multiple recipes can be stored, and modified as required.