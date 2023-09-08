<!-- Output copied to clipboard! -->

<!-----

Yay, no errors, warnings, or alerts!

Conversion time: 1.248 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Fri Sep 08 2023 03:54:10 GMT-0700 (PDT)
* Source doc: Location-Based Restaurant Recommendation Project Scope Document
----->

# Location-Based Restaurant Recommendation Project Scope Document

##### By Abdullah Nafees

Software Engineer

## Project Overview

The Location-Based Restaurant Recommendation project is a web-based application that helps users discover and explore
restaurants based on their location and preferences. This document outlines the project's scope, user stories, and API
routes.

## Project Scope

### Features

#### Brainstorming Session 1:

* User Registration and Authentication: Users can create accounts and log in securely.
* Location Detection: The application can detect the user's location using geolocation provided by the browser using
  the [Navigator and Geolocation interface provided by Web API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation). (
  Will have to figure out a small frontend application with a view to let the User know that we are taking his
  location.)
* Restaurant Search: Users can search for restaurants based on various criteria (e.g., cuisine, price range, ratings).
* Restaurant Recommendations: The application recommends restaurants to users based on their location and preferences.
* Restaurant Details: Users can view detailed information about a restaurant, including its name, address, menu, and
  reviews.
* User Reviews: Users can leave reviews and ratings for restaurants.
* User Favorites: Users can add restaurants to their list of favorites.
* User Profile: Users can update their profiles and view their past reviews and favorite restaurants.

#### Brainstorming Session 2:

* User Registration and Authentication: Users can create accounts securely and log in to access personalized features.
* Location Detection: The application offers the option to detect the user's location automatically using geolocation or
  to input the location manually.
* Restaurant Search: Users can search for restaurants based on criteria such as cuisine, price range, and ratings.
* Restaurant Recommendations: The system provides restaurant recommendations to users based on their location and
  preferences.
* Restaurant Details: Users can view detailed information about a restaurant, including its name, address, menu, and
  reviews.
* User Reviews: Users can leave reviews and ratings for restaurants they have visited.
* User Favorites: Users can add restaurants to their list of favorite places for easy access.
* User Profile Management: Users can update their profile information, including their name, profile picture, and
  password. They can also view their past reviews and favorite restaurants.
* Admin Restaurant Management: Admin users have the capability to manage restaurant listings, including adding new
  restaurants, updating existing ones, and deleting restaurants.
* Admin Review Management: Admin users can oversee user reviews, including moderation and removal if necessary.

### User Roles

* Regular User: Can search for restaurants, view recommendations, leave reviews, and manage their profile.
* Admin User: Can manage restaurant listings, user reviews, and user accounts.

## Location Detection Algorithm and API structure

We can get the location and restaurant data in two ways:

### Using User Inputs

* User can input their own location (e.g., Lahore), this hits the endpoint `/api/location/detect/` and gets the
  longitude and latitude of the user and a search keyword (e.g., 'desi restaurants in DHA Lahore') in the HTML form
  defined in a separate frontend app in my project. So, our parameters will be `longitude, latitude, and keyword`.
* JavaScript gets that data, loops the restaurants, and sends each restaurant's data to the DRF API
  endpoint `/api/create-restaurant/`. DRF uses my already-defined Django Model to save it in PostgreSQL.
* The user is then prompted to click on a button called `Search` the nearby places and DRF API calls the
  endpoint `/api/restaurant/` which gets the list of restaurants we get from the above API.

<p style="text-align: right">
<a href="https://arbisoft.slack.com/archives/D05N4UP9NGM/p1693924118863749">7:28</a></p>

### Using Google Geocoding or Web Navigator API

* When the user clicks the `Search` button, the JavaScript function first checks if geolocation is supported in the
  user's browser.
* If geolocation is supported, it obtains the user's latitude and longitude using the Geolocation API.
* It then constructs a URL for the Google Places API nearby search using the user's location and the provided keyword.
* The nearby search retrieves a list of restaurants near the user's location based on the provided keyword.
* The code loops through the restaurant data and sends each restaurant's information to my DRF API for saving in the
  database.

### Using Maps JavaScript API

* The user is provided with a map for setting a pin location, an input field for defining a radius, and an input field
  for providing a keyword for the search.
* The data received from the map pin location fetches the lat and long coordinates that are provided to the Places API
  to search for nearby restaurants
* The results from the API call are stored in the DB for the first time the user performs the search otherwise the user
  is provided with a list of restaurants that match the criteria of the user’s inputs.

## User Stories

* User Story 1: User Registration

  As a new user, I want to create an account by providing my email and password.

* User Story 2: User Authentication

  As a registered user, I want to log in securely using my email and password.

* User Story 3: Location Detection

  As a user, I want the application to detect my location automatically using `Navigator.geolocation` API or Google
  Geocoding or Maps JavaScript APIs and the interface provided by the user’s browser.

* User Story 4: Restaurant Search

  As a user, I want to search for restaurants based on criteria such as cuisine, price range, and ratings.

* User Story 5: Restaurant Recommendations

  As a user, I want the application to recommend nearby restaurants based on my location and preferences.

* User Story 6: Restaurant Details

  As a user, I want to view detailed information about a restaurant, including its name, address, menu, and reviews.

* User Story 7: User Reviews

  As a user, I want to leave reviews and ratings for restaurants I've visited.

* User Story 8: User Favorites

  As a user, I want to add restaurants to my list of favorite places for easy access.

* User Story 9: User Profile Management

  As a user, I want to update my profile information, including my name, profile picture, and password. I also want to
  view my past reviews and favorite restaurants.

* User Story 10: Admin Restaurant Management

  As an admin user, I want to manage restaurant listings, including adding new restaurants and updating existing ones.

* User Story 11: Admin Review Management

  As an admin user, I want to manage user reviews, including moderation and removal if necessary.

## API Routes

### User Endpoints

* `POST /api/user/register/`: User registration.
* `POST /api/user/login/`: User login.
* `POST /api/user/logout/`: User logout.
* `GET /api/user/profile/`: Retrieve user profile (authenticated).
* `PUT /api/user/profile/`: Update user profile (authenticated).

### Location Endpoints

* `POST /api/location/detect/`: Detect the user's location (authenticated).

### Restaurant Endpoints

* `GET /api/restaurants/`: List nearby restaurants based on location and preferences (authenticated).
* `GET /api/restaurants/&lt;restaurant_id>/`: Retrieve restaurant details (authenticated).
* `GET /api/restaurants/search/`: Search for restaurants based on criteria (authenticated).

### Review Endpoints

* `POST /api/reviews/`: Create a review for a restaurant (authenticated).
* `GET /api/reviews/&lt;review_id>/`: Retrieve a review (authenticated).
* `PUT /api/reviews/&lt;review_id>/`: Update a review (authenticated).
* `DELETE /api/reviews/&lt;review_id>/`: Delete a review (authenticated).

### Favorite Endpoints

* `POST /api/favorites/`: Add a restaurant to favorites (authenticated).
* `GET /api/favorites/`: List the user's favorite restaurants (authenticated).
* `DELETE /api/favorites/&lt;restaurant_id>/`: Remove a restaurant from favorites (authenticated).

### Admin Endpoints

* `POST /api/admin/restaurants/`: Add a new restaurant (admin).
* `PUT /api/admin/restaurants/&lt;restaurant_id>/`: Update restaurant details (admin).
* `DELETE /api/admin/restaurants/&lt;restaurant_id>/`: Delete a restaurant (admin).
* `GET /api/admin/reviews/`: List user reviews (admin).
* `DELETE /api/admin/reviews/&lt;review_id>/`: Delete a review (admin).

## Project Structure Outline

Creating a complete Django REST framework project structure with multiple apps and models as requested is a substantial
task that requires detailed code and configuration. I'll provide you with a high-level outline of how you can structure
your Django project, including creating apps and models, along with adding a front-end app for the web page. You will
need to create the actual code files and configurations based on this outline.

### 1. Create a Django Project

First, create a Django project using the following command:

### 2. Create Django Apps

#### User Authentication App

Create an app for user authentication:

This app will handle user registration, authentication, and user profile management.

#### Restaurants App

Create an app for restaurant-related functionality:

This app will handle restaurant listings, reviews, and favorites.

### 3. Define Models

#### Users App

In the `users` app, define models for user registration and profile management, including user profile pictures, if
needed.

#### Restaurants App

In the `restaurants` app, define models for restaurants, reviews, and favorites:

### 4. Configure Django REST Framework

Configure the Django REST framework by adding it to the `INSTALLED_APPS` in your project's settings:

Also, configure authentication classes, permissions, and serializers for your models in your Django REST framework
settings.

### 5. Create API Views and URLs

In each app, create API views and define URLs for various API endpoints, following the Django REST framework's
conventions.

### 6. Frontend App

Create a front-end app for the web page using Django templates or a front-end framework like React or Vue.js, as per
your preference. For integrating Google Maps JavaScript API to get the pin location, you can use JavaScript and AJAX
calls to interact with the REST API endpoints you've defined in your Django project.

Create HTML templates for the search form, map, and display of restaurant results. Use JavaScript to handle user
interactions, including capturing the location, radius, and search keywords from the form, and making AJAX requests to
your Django API.

### 7. URL Routing

Configure URL routing in your project's `urls.py` to route requests to the appropriate views and templates for your
front-end app.

### 8. Templates and Static Files

Configure settings to handle templates and static files (for CSS and JavaScript) in your Django project settings.

### 9. Migrations and Database Setup

Run migrations and apply them to create the database schema based on your defined models:

### 10. Development Server

Start the development server to test your project:

This is a high-level outline of how I will structure your Django project, including apps, models, and front-end
integration. Additionally, I will configure Django settings, including database, authentication, and CORS settings, as
needed for your project.

## Frontend App Structure

Creating a file structure for a React frontend app in a Django project typically involves organizing your React
components, styles, and other assets. Below is a basic suggested file structure for a React app within a Django project:

Here's a brief description of the key directories and files:

* **public** This directory contains your HTML template (`index.html`) and any other public assets like favicons.
  The `index.html` file is the entry point for your React app.
* **src** This is where your React source code resides.
* **components** This directory holds your React components. Each component should have its own folder containing the
  component file (`ComponentName.js`) and any associated styles (`ComponentName.css`).
* **styles** CSS or SCSS files for styling your components. You can also organize styles based on components or pages.
* **assets** This is where you can store images, fonts, or any other static assets that your app uses.
* **index.js** The entry point for your React app, which usually renders the main component (e.g., `App.js`) into
  the `index.html` template.
* **App.js** The root component of your React app, where you typically set up routes, global state management, or other
  app-wide logic.
* **package.json** This file contains your project's dependencies, scripts, and configuration for Node.js packages.
* **.env** Environment variables file if you need to configure any environment-specific settings.
* **.gitignore** A file specifying which files and directories should be ignored by Git.
* **README.md** Documentation for your React app, providing an overview of the project and how to get started.

This is a basic structure, and you can adapt it based on your project's specific needs. You may also need to set up a
build process using tools like Webpack or create-react-app to bundle your React code for production use. Additionally,
consider configuring a development server or proxy settings in your Django project to interact with the React app during
development.

## Project Conventions and Best Practices

### Naming conventions

* Django Convention: Django itself follows snake_case naming conventions in its core codebase and documentation.
  Adhering to the same convention can make your project more consistent with Django's style.
* Python PEP 8: PEP 8, the official Python style guide, recommends using snake_case for variable and function names in
  Python. Django is built using Python, and following PEP 8 conventions aligns with Python best practices.
* Database Table Names: In Django, model classes represent database tables. By default, Django converts class names to
  snake_case for database table names. Using the same convention for model classes and their attributes helps maintain
  consistency.
* Readability: Snake_case is generally considered more readable for Python code, especially when variable or attribute
  names consist of multiple words. It uses underscores to separate words, making the names easier to distinguish.

#### Decisions

* Using `snake_case` for Python code, including Django models, views, and functions.
* Using `camelCase` for JavaScript/React components, functions, and variables.
* Using hyphen-separated kebab-case for HTML/CSS class names and attributes (e.g., `class="my-component"`).