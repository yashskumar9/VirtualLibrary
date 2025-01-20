## Virtual Bookshelf

A simple web application to manage a virtual bookshelf. This app helps to keep track of books that the user have read, along with their authors and ratings for them.

## Features

- Add new books to the virtual bookshelf by providing the title, author, and your rating. All the added books can be viewed in a neat and organized manner. Additionally, there is an option to update the rating of a specific book that has already been added or to remove books from the virtual bookshelf.

## Technologies Used
- **Backend**: Flask (Python)
- **Database**: SQLite (via SQLAlchemy ORM)
- **Frontend**: HTML templates rendered using Jinja2

##  Setup Instructions
Follow these steps to run the project locally:

01. Prerequisites
    - Python 3.9 or higher installed on your system

02. Installation
    1) Clone the repository:

        ```bash
        git clone https://github.com/yashskumar9/virtual-bookshelf.git
        cd virtual-bookshelf
        ```
    
    2) Create and activate a virtual environment:
        
        ```bash
        python -m venv venv
        source venv/bin/activate  # For Linux/Mac
        venv\Scripts\activate     # For Windows
        ```
    3) Install the required packages:
    
        ```bash
        pip install flask flask_sqlalchemy
        ```

    4) Run the application:
        
        ```bash
        python app.py
        ```
        
    5) Open your browser and navigate to:
        
        ```arduino
        http://127.0.0.1:5000/
        ```
    
03. Usage

    1. Add a New Book
       - Click on the "Add Book" button on the homepage.
  
          <p align="center">
            <a>
              <img src='https://github.com/user-attachments/assets/b01a5670-7868-48dd-9c95-7b998be6fcb0' width=500>
            </a>
          </p>
          
       - Fill in the title, author, and rating, and click "Add".
  
          <p align="center">
            <a>
              <img src='https://github.com/user-attachments/assets/38df4716-faab-455b-83e6-b81f287e5931' width=500>
            </a>
          </p>
          
    2. Adding Duplicate Book
       - If a duplicate book is added to the bookshelf, an error message will be displayed indicating that the book already exists in the bookshelf. Otherwise, a success message will confirm that the book has been successfully added to the bookshelf.
  
          <p align="center">
            <a>
              <img src='https://github.com/user-attachments/assets/082eadb7-5d51-467a-8ad0-104fe3253818' width=500>
            </a>
          </p>
  
          <p align="center">
            <a>
              <img src='https://github.com/user-attachments/assets/3b5500f0-9642-4418-b67c-8070f580991b' width=500>
            </a>
          </p>

    3. Edit a Book Rating

       - Click on the "Edit" button next to the book you want to update.
       - Enter the new rating and submit the form.
  
          <p align="center">
            <a>
              <img src='https://github.com/user-attachments/assets/6e14712a-9094-4579-b337-0bd9138afd0a' width=500>
            </a>
          </p>
          
    4. Delete a Book
       - Click on the "Delete" button next to the book you want to remove.
    
    
