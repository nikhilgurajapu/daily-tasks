'''ORM (Object-Relational Mapping) in Django is a technique that allows you to interact with databases using Python code, rather than writing raw SQL queries.
 
*Key Features:*
 
1. Database Abstraction: Interact with different databases (e.g., MySQL, PostgreSQL, SQLite) using a unified API.
2. Object-Relational Mapping: Represent database tables as Python classes and objects.
3. Querying: Perform complex queries using Python syntax.
4. Data Modeling: Define database schema using Python models.
 
*Django ORM Components:*
 
1. Models: Define database tables as Python classes.
2. Fields: Represent individual columns in a database table.
3. QuerySets: Collections of objects retrieved from the database.
4. Managers: Interface between models and the database.
 
*Django ORM Benefits:*
 
1. Database Portability: Switch between databases without changing code.
2. Improved Productivity: Focus on Python code, not SQL.
3. Reduced SQL Errors: ORM handles SQL generation.
4. Better Security: ORM protects against SQL injection.

templates:-
Templates are a crucial part of Django's MVT (Model-View-Template) architecture.
They are used to define the structure and layout of the HTML pages that are rendered to the user.
Django templates are written in HTML, CSS, and JavaScript, and they can also include dynamic content using the Django Template Language (DTL).


model view templates(MVT):-
Django follows the Model-View-Template (MVT) architecture, which is a variation of the classic Model-View-Controller (MVC) design pattern.
The MVT architecture consists of three main components: Model, View, and Template

types of views:-
         Django views are Python functions that take http requests and return http response, like HTML documents.

A web page that uses Django is full of views with different tasks and missions.

Views are usually put in a file called views.py located on your app's folder.


rest framework:-
        Django REST framework is a powerful and flexible toolkit for building Web APIs.
Some reasons you might want to use REST framework: The Web browsable API is a huge usability win for your developers

requests and response:-
          Django uses request and response objects to pass state through the system.
When a page is requested, Django creates an HttpRequest object that contains metadata about the request.
Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function. Each view is responsible for returning an HttpResponse object.

'''