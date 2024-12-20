# Python Recipe App

## Context
This project focuses on creating a web application using the Django framework. To work with Django, you need an understanding of application design patterns and internal language, which you gained in Achievement 1 when using Python to make a command line Recipe app. Now, in Achievement 2, it’s time for you to rebuild your app using Django. Django has the advantage of being neatly moduralized and developer friendly, while also being powerful enough to run some of the world’s most popular websites. In your project, working with Python-based Django, you’ll develop a full-stack web application using the Django development server. You’ll then deploy the application using Heroku, with a Postgres database at the backend, HTML, and CSS-based rendered pages at the frontend and Python-based Django as your web application framework. Your final web application will be dynamic and multi-user, letting users sign up and create their own content. It’ll also have statistical dashboards, implementing your new data analytics and data visualization skills. Finally, you’ll demonstrate coding best practices by putting your well-tested and well-documented code on GitHub.


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

### Exercise 1: Getting Started with Django
- Create and manage virtual environments
- Install Django on macOS, Windows, and Linux
  
### Exercise 2: Django Project Set Up
- Create Django project and apps
- Explore components and settings of Django project
- Create superuser and explore Django admin panel

### Exercise 3: Django Models
- Create Django models and database tables
- Register Django models with Django project
- Add database records using Django admin panel
- Start writing automated tests

### Exercise 4: Django Views and Templates
- Define views for Django application 
- Develop Django templates 
- Render web pages in Django application 
- Define URLs and routes for the application

### Exercise 5: Django MVT Revisited
- Update database tables containing recipe and ingredient data 
- Enter recipe data using Django admin panel 
- Develop a welcome page for application 
- Develop subpages to display recipe information

### Exercise 6: User Authentication in Django 
- Set up user authentication for application 
- Add login and logout features 
- Protect Django views 

### Exercise 7: Data Analysis and Visualization in Django 
- Implement search features in the application 
- Provide data analytics dashboard 

### Exercise 8: Deploying a Django Project 
- Prepare application code to upload to GitHub 
- Package Django application and deploy it on web server

## Requirements
- Compatibility: Works on Python 3.6+ installations and Django version 3.
- Error Handling: Manages exceptions and errors during user input, displaying user-friendly error messages.
- Database: Connects to a PostgreSQL database hosted locally (uses SQLite during development).
- User Interface: Provides an easy-to-use interface with simple input forms and clear instructions. Menus for features like login and logout are presented neatly with concise prompts.
- Code Quality: Includes proper documentation and automated tests. Code is uploaded on GitHub.
- Dependencies: A requirements.txt file is provided, listing all necessary modules.
- Instructions: A README file with instructions for downloading and running the app locally is included.

## Contribution
Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.