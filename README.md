# AddressBookApp

Application Name
----------------
Address Book App in Django, 2022

# Technologies
--------------
Languages - Html, Css, Python
Framework - Django

# Build and Installation
------------------------
After pulling the repository, 
1. Go to your local directory
2. In your terminal type python manage.py makemigrations  
3. Type python manage.py migrate --run-syncdb
4. python .\manage.py runserver to start the project
5. Copy http://127.0.0.1:8000/ or your local server in your browser

# Usage
-------
1. The first default page is Login/Registration page
2. Register if you are a new user
3. Upon registration, users can log in with their credentials
4. There will be a main view page for the users after successful login. / Failure to login will take the user back to login page.
5. Users can create new contacts, can see all the existing contacts, can search existing contacts with any keywords for any field.
6. Users can also click on the existing contact and choose to view all the details of the contact or delete it from the contact list.
7. The program supports multiple users and it also supports their own unique contact lists.
8. All of these functionalities are available upon successful authentication.

# Contributors
--------------
Author: Joshua Kyi

#Known Bugs
-----------
Search empty strings after creating multiple accounts can result in showing mixed contact list for search results.

