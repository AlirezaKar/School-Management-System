# Education System Management

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)]()

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

Brief summery: This project is a Web-Based application that allows any sort of education organization to manage
their list of every data required to be kept track of

## Features
- [API]: Has REST framework as the api 
- [drf-yasg]: The front view of APIs
- [tkinter]: Has also a tkinter front 

## Technologies Used
- Python (3.12)**
- Django (5.1.2)**
- REST framework**

## Setup Instructions 

Follow these steps to get a copy of the project running on your local machine:

1. Clone the repository:
```bash
git clone https://github.com/AlirezaKar/school-management-system.git
cd school-management-system
```

2. Create a virtual environment and activate it:
python -m venv env
# on Windows: 
env\Scripts\activate
# on Linux:
source env/bin/activate

3. Install dependencies:
# if you're a developer:
pip install -r requirements.txt
pip install -r requirements.dev.txt
# if you're a end-user:
pip install -r requirements.txt

4. Run database migrations
python manage.py migrate

5. start the development server
python manage.py runserver

## Usage

- Visit http://127.0.0.1:8000 or https://aliconday98.pythonanywhere.com/ to access the app 
# for developers 
- To access the admin area: python manage.py createsuperuser 

## Author
- Alireza Kalaie
- Email: alireza.k.python1348@gmail.com