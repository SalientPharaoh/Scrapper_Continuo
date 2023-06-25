# Scrapper_Continuo
Scrapping [Continuo](https://parents.msrit.edu/) for details of students

## Deployment

To deploy this project follow the following steps

* Start the virtual environment. Run the following command
```bash
 $ source env/bin/activate
 $ pip install -r requirements.txt
```
* Deploy the flask server by running the code
```bash
 $ python app.py
```

## Features

- Simple and easy to use API : To access the data of user, the endpoint that needs to be hit is:
```bash
  <base_url_of_API>/username/date/month/year
```
- The API throws LoginError and InternalServerError to handle the exception properly.
- The API fetches the attendance records of the student.
- The API fetches the internal assessment report of the student.
- The API is built using Flask Farmework.

### File Structure

- ``` app.py ``` contains the Flask code for the web server.
- ``` attendance.py ``` contains the functions for scraping the attendance of the user.
- ``` cie.py ``` contains the functions for scraping the internal assessment report of the user.
- ``` scrapper.py ``` contains the core scraping functions for the application.
- ``` start.py ``` contains the initialization functions for the application.

