"""
Model

The Model in Django serves as the interface for data stored in the database.
It is responsible for maintaining the data and handling the logical data structure for the entire web application. 
Models are typically represented by relational databases such as MySQL or PostgreSQL

View

The View in Django acts as the bridge between the Model data and the Templates.
It handles all the business logic behind the web application. When a user sends a request,
the View retrieves the appropriate data from the database and renders the template along with the retrieved data

Template

The Template in Django is responsible for the entire User Interface.
It handles the static components of the webpage, including the HTML that users encounter.
Templates consist of static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted


Control Flow in MVT

User Request: A user sends a URL request for a resource to Django.

URL Mapping: Django framework searches for the URL resource.

View Handling: If the URL path links up to a View, that particular View is called.

Model Interaction: The View interacts with the Model, retrieving the relevant data from the database.

Template Rendering: The View then renders back an appropriate template along with the retrieved data to the use



"""