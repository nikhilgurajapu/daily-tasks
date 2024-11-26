"""#What is Django?
 
Django is a web development framework for Python which offers a  fast and effective website development.
It helps in building and maintaining quality web applications. It enables you to make the development process
smooth and time-saving. Django was released on  July 2005.
 
#Key Advantages?
 
1. Rapid Development: Django's batteries-included approach and extensive libraries enable fast development.
 
2. Secure: Django provides built-in security features to protect against common web vulnerabilities.
 
3. Scalable: Django supports large-scale applications with ease.
 
4. Maintainable: Django's modular design and clean code make maintenance efficient.
 
5. Flexible: Django supports multiple databases and caching systems.
 
6. Extensive Libraries: Django comes with many built-in libraries for tasks like authentication, file uploads, and more.
 
7. Large Community: Django has an active and supportive community.
 
8. Open-Source: Django is free and open-source.
 
#Features of Django?
 
1. Auto-generated admin interface
2. Built-in debugging tools
3. Code reuse through libraries and apps
4. Extensive documentation
5. Large community and ecosystem
6. Support for multiple databases (e.g., MySQL, PostgreSQL)
7. Support for multiple caching systems (e.g., Redis, Memcached)
8. Integrated testing framework
 
#IMPORTANCE  AND APPLICATIONS OF DJANGO :
 
1. Web Development: Django is widely used for complex web applications.
 
2. Enterprise Software: Django's scalability and security make it suitable for enterprise software.
 
3. E-commerce: Django's flexibility and libraries support e-commerce platforms.
 
4. Social Media: Django's scalability handles high traffic social media platforms.
 
5. Data Analysis: Django integrates well with data analysis tools.
 
6. Machine Learning: Django supports machine learning model deployment.
 
7. IoT: Django's real-time capabilities support IoT applications.
 
#Real-World Applications:
 
1. Instagram
2. Pinterest
3. Dropbox
4. National Geographic
5. The Washington Post
6. Mozilla
7. Bitbucket
 
 
 
 
#TYPES OF VIEWS:
 
*1. Function-based views (FBVs)*
 
- Defined as a Python function.
- Takes an HttpRequest object as an argument.
- Returns an HttpResponse object.
 
 
*2. Class-based views (CBVs)*
 
- Defined as a Python class.
- Inherits from View or a subclass.
- Methods handle HTTP requests.
 
 
*3. Generic views*
 
- Pre-built views for common tasks.
- Examples: ListView, DetailView, CreateView, UpdateView, DeleteView.
- Can be extended or customized.
 
 
*4. Built-in views*
 
- Provided by Django for specific tasks.
- Examples: login, logout, password_reset, password_change.
- Can be used directly or extended.
 
 
*5. API views*
 
- Used for building RESTful APIs.
- Examples: APIView, ViewSet.
- Part of Django Rest Framework (DRF).
 
 
*6. Viewsets*
 
- Used for building RESTful APIs.
- Combination of multiple views.
- Part of Django Rest Framework (DRF)
 
 
 
 
#VIEW :
 
A view is a function or method that takes http requests as arguments, imports the relevant model(s),
and finds out what data to send to the template, and returns the final result.
 
The views are usually located in a file called views.py.
 
*Types of Views:*
 
1. Function-based views (FBVs): Simple functions that handle requests.
2. Class-based views (CBVs): Classes that handle requests, providing more structure.
3. Generic views: Pre-built views for common tasks, such as listing objects.
4. Viewsets: Collections of views for handling complex APIs.
 
*View Structure:*
 
1. Import necessary modules.
2. Define the view function/class.
3. Handle HTTP requests (e.g., GET, POST, PUT, DELETE).
4. Return an HTTP response.
 
#TEMPLATES:
 
A template is a file where you describe how the result should be represented.
 
The templates of an application is located in a folder named templates.
 
 
WHATE IS REST FRAMEWORK IN DJANGO ?
 
Django Rest Framework (DRF) is a powerful toolkit for building RESTful APIs in Django. It provides a simple,
flexible, and scalable way to create APIs that can be consumed by web, mobile, and other applications.
 
*Key Features:*
 
1. Serializers: Convert complex data to/from native Python datatypes.
2. Views: Handle HTTP requests and return responses.
3. Viewsets: Combine multiple views into a single class.
4. Routers: Automatically generate URLs for viewsets.
5. Authentication and Permission: Built-in support for authentication and permission.
6. API Documentation: Automatic generation of API documentation.
7. Support for multiple formats: JSON, XML, CSV, etc.
 
*Advantages:*
 
1. Easy to use: Simplifies API development with Django.
2. Flexible: Supports multiple API architectures.
3. Scalable: Handles large-scale APIs.
4. Secure: Built-in support for authentication and permission.
5. Well-documented: Extensive documentation and community support.
 
*Use Cases:*
 
1. Building RESTful APIs for web applications.
2. Creating APIs for mobile applications.
3. Integrating with third-party services.
4. Building microservices architecture.
5. Real-time data processing and streaming.
 
REQUESTS AND REPONSES :
 
In Django, requests and responses are the fundamental components of the HTTP protocol.
 
*Requests:*
 
1. HttpRequest object: Represents an HTTP request.
2. Methods: GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH.
3. Attributes:
    - path: Requested URL path.
    - method: HTTP method.
    - user: Authenticated user.
    - GET/POST: Query/data sent with the request.
 
*Responses:*
 
1. HttpResponse object: Represents an HTTP response.
2. Status codes: 200 (OK), 404 (Not Found), 500 (Server Error).
3. Content: HTML, JSON, XML, text.
 
 
MVT (Model-View-Template) is an architectural pattern used in Django, a Python web framework. It's similar to the MVC (Model-View-Controller) pattern but with some differences.
 
*MVT Components:*
 
1. *Model* (M): Represents data structures, typically database tables.
    - Defines data schema
    - Interacts with database
 
2. *View* (V): Handles HTTP requests, interacts with models, and returns responses.
    - Processes requests
    - Retrieves/updates data using models
    - Returns responses (e.g., HTML, JSON)
 
3. *Template* (T): Responsible for rendering the user interface (UI).
    - HTML/CSS/JavaScript files
    - Displays data provided by views
 
*Benefits:*
 
1. Separation of Concerns (SoC): Each component has a distinct responsibility.
2. Reusability: Components can be reused across the application.
3. Maintainability: Easy to update/modify individual components.
 
 
ORM
 
ORM (Object-Relational Mapping) in Django is a technique that allows you to interact with databases using
Python code, rather than writing raw SQL queries.
 
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
 
Django views are Python functions that take http requests and return http response, like HTML documents. A web page that uses Django is full of views with different tasks and missions. Views are usually put in a file called views.py located on your app's folder.
 
 
Django, a popular Python web framework, simplifies the process of building web applications by providing robust tools and functionalities. One fundamental aspect of Django is the models.py file, which defines the structure of the application's database.
 
In many ways, urls.py is the entry point for your project. It is usually the first file I open when I study a Django project. It is like reading a map before exploring a terrain. Essentially, urls.py contains the root URL configuration or URLConf of the entire project.
   
What is the purpose of settings.py? The settings.py file is typically used to store configuration information in Django. It may contain the site URL, paths to various directories, and other values that the executable code may use. By changing and supplementing this file, the developers configure Django projects
 
The admin.py file is used to display your models in the Django admin panel. You can also customize your admin panel.
 
Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.
 
The settings.py file is typically used to store configuration information in Django. It may contain the site URL, paths to various directories, and other values that the executable code may use. By changing and supplementing this file, the developers configure Django projects.
 
Django, a high-level web framework for Python, includes built-in support for using SQLite as a database backend. SQLite is a lightweight, serverless database engine that stores data in a local file
   
uses of settings.py
The settings.py file is typically used to store configuration information in Django. It may contain the site URL, paths to various directories, and other values that the executable code may use. By changing and supplementing this file, the developers configure Django projects.
 """