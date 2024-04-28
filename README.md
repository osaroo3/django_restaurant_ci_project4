# Portfolio Project 4 -  Africana Eatery booking system
![](staticfiles/images/readme-images/am-i-responsive.png)

The deployed [Africana](https://django-africana-eatery-ed503b69cf5f.herokuapp.com/) app.

The [GitHub repository](https://github.com/osaroo3/django_restaurant_ci_project4) 

## Project goals
The goals of this project is to develop an eatery/resturant web application with features, such as date/time-based bookings,
multiple table occupancies, cancellations, menu and double bookings prevention. This portfolio project 4 is a requirement in order to obtain a Diploma from Code Institute in Fullstack Software Development (E-Commerce Applications).

# Table of content

- [**UX (User Experience)**](#ux-user-experience)
  - [**User Stories**](#user-stories)
- [**Design and Site Structure**](#design-structure)
  - [**Functional Structure**](#functional-structure)
  - [**Wireframes**](#wireframes)
- [**Features**](#features)
  - [**Responsive Design**](#responsive-design)
- [**Technologies**](#technologies)
  - [**Languages**](#languages)
  - [**Frameworks and Libraries**](#frameworks)
  - [**Tools**](#tools)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
  - [**Code**](#code)
  - [**Content and media**](#content)
  - [**Acknowledgments**](#acknowledgments)



## UX (User Experience)

### User stories

#### First time visitor goals

As a first time visitor, I want:
* to know the purpose of the site at first glance.
* to navigate the site intuitively.
* to have access to all features of the site after registering an account.
* to be able to make online reservations.
* to be able to sign out of my user account.
       
        
#### Returning and frequent user goals

As a returning user, I want:
* to access my user account by signing in.
* to make and view my reservations.
* to be able to update and delete my reservations. 
* to edit my booking details or delete them.
* to be able to sign out of my account as a safety measure.


#### Site Administrator goals
As a site administrator, I want to create, read, update and delete bookings/reservations.    


### Agile tools

GitHub Projects feature was used as a [Kanban board](https://github.com/users/osaroo3/projects/2) for the development of this project, which made is easy to track the progress made and goals attained.
[User stories](https://github.com/osaroo3/django_restaurant_ci_project4/issues) was used to structure the project into sections of tasks to be achieved, with the kenban board providing the platform. 


## Design and Site structure

The site mirrors what an african eatery would look like in the United Kingdom or Europe to give diaspora africans a taste of home.
The main page is as viewed below.

<details>
<summary>Africana website look at first glance</summary>

![Home page](staticfiles/images/readme-images/home-page2.png)

</details>
<br />

### Functional Structure

**Home page:** The home page has navigation bar features and also some images of the varieties of the african dishes available to users.

**Menu page:** For access to the menu to make reservations, the user must have an account and sign in.

**My bookings page:** A logged in user has access to all bookings/reservations made. The user can manage bookings by either modifying them or deleting them if they want to.

**Book now page:** A logged in user has full access to the book now page features and can make bookings if they wish to.

**Registration page:** The registration page is where the user can register an account and get access to all available features of the site

**Login page:** The login page offers a user with a user account access to all the features of the site when they log in with their login details.

**Edit booking page:** The feature is only available to registered users who wish to modify their bookings.


### Wireframes

The wireframes used are shown below although modified in the project work:

**Models**

<details>
<summary>Menu model</summary>

![Menu model](staticfiles/images/wireframes/menu-model.png)

</details>

<details>
<summary>Booking model</summary>

![Booking model](staticfiles/images/wireframes/booking-model.png)

</details>
</br>

**For Mobile view and small screens**

<details>
<summary>Book now page</summary>

![Book now page](staticfiles/images/wireframes/book-now.png)

</details>

<details>
<summary>Home page</summary>

![Home page](staticfiles/images/wireframes/home.png)

</details>

<details>
<summary>Menu page</summary>

![Menu page](staticfiles/images/wireframes/menu.png)

</details>

<details>
<summary>My bookings page</summary>

![My bookings page](staticfiles/images/wireframes/mybooking.png)

</details>


<br />

**For Desktop view**
<details>
<summary>Home page</summary>

![Home page](staticfiles/images/wireframes/homepage.png)

</details>

<details>
<summary>Menu page</summary>

![Menu page](staticfiles/images/wireframes/ourmenu.png)

</details>

<details>
<summary>My bookings page</summary>

![My bookings page](staticfiles/images/wireframes/my-booking.png)

</details>

<details>
<summary>Book now page</summary>

![Book now page](staticfiles/images/wireframes/booknow.png)

</details>
<br />


## Features

### Navbar

Due to the base extension, the navigation bar is present on all pages of the site. If the user is logged in, the right end of the nav bar changes from "Welcome, AnonymousUser to welcome, John(depending on the name of the user)". The nav bar also collapses into a hamburger icon for smaller screen sizes.

Navigation bar for user's without an account.

![Navigation bar for unauthorised user's](staticfiles/images/readme-images/nav-bar2.png)

Navigation bar for logged in users.
![Authenticated user's Navigation](staticfiles/images/readme-images/nav-bar1.png)

### Home page

On the Home page, unauthorised users cannot see my bookings and book now links on the nav bar . 
![Home page](staticfiles/images/readme-images/home-page.png)

### Sign up page

This page allows unauthorised users to create an account by following the instructions.
![Sign up page](staticfiles/images/readme-images/sign-up.png)


### Login page

This page allows user's with account to login by providing their credentials.

![Sign in page](staticfiles/images/readme-images/sign-in.png)


### Menu page

The menu button on the bav bar when clicked, takes the user to the menu page which provides users with available menu and the corresponding price to choose from.
![Menu page](staticfiles/images/readme-images/menu-page.png)


### Book now page

The Book now button when clicked, takes the user to the book now page. For logged in user's, a table to fill to make bookings shows up. However, for user's without an account, there is a link provided to redirect them to sign up.

#### Book Now page for a logged in user

![Book Now page](staticfiles/images/readme-images/book-now-page.png)

#### Book Now page for an unauthorised user

![Book now page](staticfiles/images/readme-images/book-now-page2.png)


### My Bookings page

The booking page displays bookings made by the logged in user, with details about the bookings.

![Booking page](staticfiles/images/readme-images/my-bookings-page.png)

If there is no booking yet, the logged in user is told with a further suggestion to make bookings with a provided a link to the page to make bookings. If the user is not logged in, they are redirected to sign up page.

### Edit booking page

Every bookings made by a logged in user can be modified by either editing the bookings or deleting them. The modify and delete button exist on my bookings page.

![Edit booking page](staticfiles/images/readme-images/edit-booking.png)

### Double booking prevention

When a user makes a booking that already exits, the server renders the 500.html file in the templates folder, telling the user that the booking exists. 
![Double booking prevention](staticfiles/images/readme-images/double-booking-page.png)


### Delete button

Only a logged in user has access to this feature. Once this button is clicked the JavaScript code renders a modal to further get assurance that the user wants to delete that booking before deletion is done.

![Delete booking page](staticfiles/images/readme-images/delete-booking.png)


### Logout page

A logged in user can log out by clicking the log out button on the nav bar. This action takes the user to the sign out page to get confirmation before the user is logged out.

![Logout page](staticfiles/images/readme-images/log-out.png)


### Responsive design

The site was designed to be responsive for both desktop and mobile use.
This project has been tested using the Google Chrome Developer multi-device emulator with different screen sizes.


## Future features

- Email confirmation after booking is made.
- Blog page about african foods and their receipes.
- Contact page
- Comment page for customers comment about the services provided by africana.
- After been served by africana, the modify and delete buttons on the users bookings should not be visible any longer.
- The modify and delete button becomes inactive once services have been provided by africana.


## Technologies Used

### Languages

  - HTML5
  - CSS3
  - JavaScript
  - Python
 

### Frameworks, Libraries, Programs

  - [Django](https://www.djangoproject.com/): python framework was used to create the backend 


### Database:
  - [PostgreSQL](https://www.postgresql.org/): the database was used to store all the data.


### Programs & Tools

- [Google Fonts](https://fonts.google.com/): Was used for the font styling.  
- [Font Awesome](https://fontawesome.com/): was used to generate the icons on the website.
- [Bootstrap](https://getbootstrap.com/): Was used to create the front-end design.
- [Gitpod](https://Gitpod.io/): was used as IDE to commit and push the project to GitHub.
- [GitHub](https://github.com/): Was used as the version control system to manage the code
- [Canva:](https://www.canva.com/) Was used to create wireframes
- [Am I Responsive](http://ami.responsivedesign.is/): was used to generate an image showing the website's responsiveness on different screen sizes 
- [Pip3](https://pypi.org/project/pip/): is the package manager to install Python modules and libraries.
- [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/): "Green Unicorn" is a Python Web Server Gateway to translate HTTP Requests for Python to understand.
- [Spycopg2](https://pypi.org/project/psycopg2/): PostgreSQL database adapter to manage the Database in Python. 
- [Heroku](https://dashboard.heroku.com/): the hosting service used to host my website.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
- [W3C Validator](https://validator.w3.org/): was used to validate HTML5 codes for this website.
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS codes for this website.
- [Github Projects and Kanban board](https://github.com/users/LarisaLG/projects/17/views/1): was used to track the progress of the project.
- [CI python linter](https://pep8ci.herokuapp.com/): was used to validate python codes.
- [JS Hint](https://jshint.com/): was used to validate JavaScript codes.


## Testing

### Bugs

#### Fixed Bugs
- The booking form was not rendering. This was fixed after I installed Django crispy forms
- The use of modal via JavaScript to delete booking was not working. I used the wrong url to trigger the delete action. I fixed the 
 by replacing urls pattern = [ path('delete_booking/<int:booking_id>/', views.booking_delete,name='booking_delete'),] with 
 urls pattern = [ path('bookings/delete_booking/<int:booking_id>/', views.booking_delete,name='booking_delete'),]

#### Unresolved Bugs

- The code does not look broken, I don't know why there is validator error.
 ![signup page W3C  code testing](staticfiles/images/readme-images/unfixed-bug.png)

- There is an uncaught type error in the console of developer tools, however, it does not affect the site in any way.
 ![Uncaught type error](staticfiles/images/readme-images/uncaught-type-error.png)
### Manual Testing

#### Device Testing

This Project was tested via a multi-device emulator with different display sizes in the Google Chrome Developer Dashboard.
The devices tested are below:

- Galaxy fold (Mobile)
- Samsung Glaxy s8 (Mobile)
- Nest HubMax (Desktop)
- Nest Hub (Desktop)
- iPad Air (Tablet)
- iPad Mini (Tablet)
- iPhone 12 pro (Mobile)
- iPhone 14 pro max (Mobile)


#### Browsers Tested

The browsers used for testing were as follows: 
  - Google Chrome
  - Firefox
  - Microsoft Edge

Site testing was done on the Gitpod environment and Heroku.
The available functionality and user experience is reflected in the table below.

| Goals/actions  | As a guest | As a logged user  | Result | Comment |
|--|:--:|:--:|:--:|--|
| I can see the home page | &check; | &check; | Pass | Unauthorised users can't see My bookings page and Book now page |
| I can see the Login page  | &check; |&check;  |  Pass| |
| I can see the Register page | &check; |&check;  |  Pass| |
| I can see the Logout page  | &cross; |&check;  |  Pass| Available only to an authorized users |
| I can see the Menu page | &check; |&check;  |  Pass| |
| I can click on My bookings and make bookings as a logged in user | &cross; | &check; | Pass | Available only to an authorized users|
| I can modify bookings | &cross; |&check;  |  Pass| Available only to an authorized users | Available only to an authorized users
| I can delete bookings | &cross; |&check;  |  Pass| Available only to an authorized users | Available only to an authorized users
| I can click the Book now nav link and see the Book now page | &cross; |&check;  |  Pass| Available only to an authorized users
| I can fill fields in the Book now form | &cross; | &check;  | Pass |Available only to an authorized users |
| I can see the Bookings page   | &cross; | &check;  | Pass | Available only to an authorized users|

<br/>


## Validation

### HTML Validation:

The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website. 
Errors was noticed when carrying out HTML validation for the sign up page. Since it's a generated form from CI codestar blog project, there is no access to the form to do the neccessary modification of the code.


<details><summary>Home page</summary>

![](staticfiles/images/readme-images/checker-home-page.png)
</details>
<details><summary>Menu page</summary>

![](staticfiles/images/readme-images/checker-menu-page.png)
</details>
<details><summary>Sign up page</summary>

![](staticfiles/images/readme-images/checker-signup-page.png)
</details>
<details><summary>Login page</summary>

![](staticfiles/images/readme-images/checker-login-page.png)
</details>

<details><summary>My bookings page</summary>

![](staticfiles/images/readme-images/checker-mybookings-page.png)
</details>

<details><summary>Book Now page</summary>

![](staticfiles/images/readme-images/checker-booknow-page.png)
</details>

</details>
<details><summary>Modify booking page</summary>

![](staticfiles/images/readme-images/checker-editbooking-page.png)
</details>
<details><summary>Delete booking page</summary>

![](staticfiles/images/readme-images/checker-deletebooking-page.png)
</details>
<details><summary>Logout page</summary>

![](staticfiles/images/readme-images/checker-logout-page.png)
</details>

---
### CSS Validation:

The website CSS styling was validated using [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/). 
![](staticfiles/images/readme-images/checker-styling.png)

---
### JavaScript Validation:

The website JavaScript code was validated using [JSHint Validation](https://jshint.com/). 
![](staticfiles/images/readme-images/check-js.png)

---
<br/>

### Python Validation (PEP8)

All Python code was checked manually with the aid of  [CI Python Linter](https://pep8ci.herokuapp.com/). Errors observed have all been fixed. 

- urls.py
![urls.py](staticfiles/images/readme-images/checker-urls.png)
- models.py
![models.py](staticfiles/images/readme-images/checker-models.png)
- forms.py
![forms.py](staticfiles/images/readme-images/checker-forms.png)
- views.py
![views.py](staticfiles/images/readme-images/checker-views.png)

---


##  Deployment

The development of this project was done with Gitpod, stored on GitHub and deployed using Heroku.
1. Visit [Heroku](https://heroku.com/)
2. Log in or create an account if applicable.
3. On the Heroku dashboard click on the 'new' button.
4. From the drop-down menu select 'Create new app'.
5. Choose your preferred app name.
6. Select the applicable region and click 'Create App'.
7. Navigate to 'Settings' and scroll down to the 'Config Vars' section. Click on 'Reveal Config Vars' and enter 'PORT' for the key and '8000' for the value and then click 'Add'. Repeat the key and value entry for your DATABASE_URL(the database you are using) and SECRET_KEY(you generated during production).
8. Click on the 'Deploy' tab. Select GitHub and the connect to the relevant repository. Click 'Deply branch'. You can also select 'Automatic Deploys' so that the site updates when updates are pushed to GitHub, however, you must set 'DEBUG = False' in your settings.py to avoid security concerns for your site.
9. After your deployment is successful click 'Open app' to view thelive app.


### Forking the GitHub Repository

To use this code and make changes without affecting the original code, it is possible to 'fork' the code on the GitHub repository through the following steps:

1. Create  or log into your GitHub account.
2. Go to the GitHub [repository](https://github.com/osaroo3/django_restaurant_ci_project4).
3. Click the 'Fork' button in the upper right-hand corner of the page.
A copy of the repository will be available in your own repository.


### Making a Local Clone
1. Log in to GitHub and locate the GitHub Repository
2. Under the repository name choose button "Code",  click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open your development editor of choice and open a terminal window in a directory of your choice
5. Type *git clone*, and then paste the URL you copied in Step 3.

``> git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY``

Press Enter. 

Your local clone will be created.

For more information follow this [link](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop).


[Back to the top](#table-of-contents)


## Credits

### Code

The idea for structure and the code of this project was from Code Institute's Codestar blog walkthrough project and LarisLG [Barbershop](https://github.com/LarisaLG/barbershop) project:
  * The base.html code and styling is a modification of that of the codestar blog project.
  * Credit to LarisaLG for the idea of the menu, my bookings and book now html page with styling.
  * Credit to LarisaLG for Date picker field and minimum date validator.
  * The javaScript code for deleting a booking was from codestar blog project.
  * The idea for my models.py was from Codestar blog and barbarshop by LarisaLG.
  * Credit to [W3schools](https://www.w3schools.com/django/django_404.php) for the idea to handle double booking server error.
  * Credit to [Django documentation](https://docs.djangoproject.com/en/5.0/) for "Everything you need to know about Django".



### Content and Media

  * credit to LarisaLG for the readme structure.
  * Credit to LarisaLG on how to fork a GitHub repository or make a local clone.

Credit to the following for the images of my homepage:
1. [Abacha](https://apocomkitchen.co.uk/assets/front/img/product/sliders/615b138763c10.jpg)
2. [Nkwobi](https://worldlytreat.com/wp-content/uploads/2023/03/Nkwobi-spicy-cow-leg-7.jpg)
3. [Jollof](https://www.tastingtable.com/1000081/jollof-wars-the-dispute-surrounding-this-west-african-rice-dish/)
4. [Fried rice](https://www.sweetnspicee.com/wp-content/uploads/2020/11/LEY_1301-scaled.jpg)
5. [Yam porridge](https://guardian.ng/wp-content/uploads/2020/05/Vegetable-Yam-Porridge.-Photo-My-diaspora-kitchen.jpeg)
6. [Egusi soup](https://www.forksandfingers.co.uk/wp-content/uploads/2019/06/Pounded-Yam.jpg.pagespeed.ce.GB0JCqfsKY.jpg)
7. [Afang Soup](https://guardian.ng/wp-content/uploads/2018/09/Afang-soup-recipe-579x598.png)
8. [Oha soup](https://www.vemscrunch.co.uk/wp-content/uploads/2022/08/Oha-Soup.jpg)
9. [Banga soup](https://i.pinimg.com/736x/f3/d8/03/f3d803ce13eec61ea8a1a6bbd7d1fff3.jpg)

Note: The use of these images were strictly for educational purposes only


### Acknowledgments

I wish to acknowledge my mentor Martina Terlevic , Code Institute's 'Tutor me' and the CI slack community for all the support thus far.
