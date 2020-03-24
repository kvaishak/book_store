# book_store
Playing around with Docker Container and its implementation of micro-service architecture.

## Usage
* Docker must be installed and running.
* Pull the code and navigate inside the folder and run `docker-compose up`. This will start the docker multi-container setup.
* Navigate to `http://localhost:5000/` you will see the page **Welcome to your Book Store** page up and running.
* For adding data to the *book-library* refer to [this](https://github.com/vaishak47/book_store/blob/master/book-library/README.md) API Documentation

## Architecture
Book_store consists of two micro-service or containers working together they are
  1. book-library
  2. website
  
### 1. book-library service

---

- This is where the books are stored hence the book-library name.
- The main api data is stored in `book_registry` folder which contains `__init__.py`
- Using the following for api :
    - `flask` for creating a rest-ful api
    - `shelve` for database
- In the `dockerfile` we mention the image required for our api - in our case python
- In `requirements.txt` we mention the packages required by out python api :
    - Flask
    - flask-restful
    
    
    
### 2. website service

---

- This is a simple website made using php.
- For now fetching data from the book-library micro-service and displaying it.
- In `docker-compose.yml` we define the services that need to be bundled together in the main docker container, also ports
