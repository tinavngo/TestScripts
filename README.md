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
