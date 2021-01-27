![Responsive](https://github.com/gideongannaban/althea/blob/master/Readme/Images/responsive.PNG)

# ALTHEA ONLINE STORE

## Purpose
The purpose of this project is to create an e-commerce website for our "Sari-Sari" or small Store in our Municipality. Due to the unending community lockdowns we have in our province, most of our regular consumers are not able to go to our Store physically to buy their usual needs. Thus, I came up with an idea of an e-commerce site selling the same products we have from our stockrooms but this time we will deliver it to their doorsteps for everyone's safety and convenience. 

In reality though most or all of our customers will prefer either cash on delivery payments but for the purpose of the project only card payments will be accepted. 

For this project, I will be using python and Django as my primary programming language and html, CSS, JavaScript and bootstrap4 for the front end. 

# UX

## Project Goals:

* Create an e-commerce site where consumers can purchase their basic daily needs from grocery food to household cleaning needs

* Provide option for customers to do their grocery purchases in the comfort of their homes rather than risk getting infected of the pandemic when going out.

## User Stories:

* Viewing and Navigation
  - As a shopper, I should be able to view a list of all products and select some to purchase.
  - As a shopper, I should be able view all the items in my shopping list with description/quantity/size and total cost at any time
  
* Sorting and Searching
  - As a shopper, I should be able to sort products available by name, price and category.
  - As a shopper, I should be able to search for a product by name, price and description.
  - As a shopper, I should be able to see what I've searched for and the number of results.
 
* Purchasing and Checkout
  - As a shopper, I should be able to select quantity and size if applicable when purchasing .
  - As a shopper, I should be able to modify my order prior to paying for it.
  - As a shopper, I should be able to enter my payment information securely.
  - As a shopper, I should be able to view a summary of my orders before finalizing the purchase.
  - As a shopper, I should be able to get a confirmation after checkout and receive an email with a confirmation of the order.
  
* Registration and User Accounts 
   - As a Site user, I should be able to Easily Register to an account to be able to view my profile and purchase history.
   - As a Site user, I should be able to login and logout from my personal account.
   - As a Site user, I should be able to recover my password just in case I forget it.
   - As a Site user, I should be able to Receive an email confirmation after registration.
   - As a Site user, I should be able to Receive an email confirmation after registration.
   - As a Site user, I should be able to update information on my profile anytime.
   - As a Site user, I should be able to delete my profile.

* As an Admin
  - As an Admin, I should be able to add a product.
  - As an Admin, I should be able to edit a product.
  - As an Admin, I should be able to delete a product.
  
## Design

### Fonts

I chose easy to read and light fonts for this app. I am keeping it simple and will only use one type of font, Lato. 

### Color Fonts

I opted for this color pallete to make it simple and easy to combine with other major colors

![Color Pallette](https://github.com/gideongannaban/althea/blob/master/Readme/Images/Color%20Pallette.PNG)

### Icons

On this project I have used easily identifiable Font Awesome icons.

I designed my site moc-ups using [balsamiq](https://balsamiq.com/) wireframes.
The idea was to create a basic layout structure of the site and identify how it will display on different screen sizes.

For more details please click [wireframe](https://github.com/gideongannaban/althea/blob/master/wireframes.md)

## Wireframes

# Technology Used
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - To create the structure and content of the page
* [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics) - Used to style the website
* [jQuery](https://jquery.com/) - jQuery came with Materialize to make the components used responsive.
* [Python](https://www.python.org/) - Primary tool used to create function 
* [Bootstrap4](https://getbootstrap.com/) - CSS framework used to assist with website responsiveness.
* [Django](https://www.djangoproject.com/) - Python web framework for quick development.
* [Font Awesome](https://fontawesome.com/) - I used the font awesome icons for the social media, location and contact details
* [Google Fonts](https://fonts.google.com/) - Used to style the fonts of the website
* [Git](https://git-scm.com/) - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
* [Github](https://github.com/) - GitHub is used to store the project code after being pushed from Git.
* [Heroku](https://dashboard.heroku.com/) - Heroku was used to deploy the project
* [Trello](https://trello.com/b/a3dsnJ58/ms2-project) - Tools used for project management
* [Favicon](https://favicon.io/) - Tool used to generate the website icon
* [AWS](https://aws.amazon.com/) - Used to store static files.
* [Stripe](https://dashboard.stripe.com/) - payment infrastructure to validate and accept credit card payments securely.
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Used to configure and manage s3 buckets
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - Used mostly for DOM manipulation upon user interaction
* [Django-aullauth](https://django-allauth.readthedocs.io/en/latest/index.html) - Django authentication toolset
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - to style the django forms.
* [Jinja2](https://pypi.org/project/Jinja2/) - Used as the main language for template manipulation.
* [Pillow](https://pillow.readthedocs.io/en/stable/) - Python imaging library to support opening, manipulating, and saving images.
* [Psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for Python.
* [Gunicorn](https://pypi.org/project/gunicorn/) - Python WSGI HTTP Server.
* [Balsamiq](https://balsamiq.cloud/) - used to create the wireframes for this project.
* [Trello](https://trello.com/b/a3dsnJ58/ms2-project) - Tools used for project management
* [Favicon](https://favicon.io/) - Tool used to generate the website icon

# Features

## Existing Features

### Delivery Banner
* Delivery Banner contains information how the customer can avail of free delivery
* The banner is only shown on the home page

### Navbar
* navbar is fixed and always remain on top of the page.
* includes all links for an easy navigation through all the sections of the website 
* Search bar so users can look up a particular item

### My Account Page
* A My Account Page where a user can register, login and logout
* Profile page where the user can view their delivery details and previous purchases

### Our Store Page
* An Our Store page where a shopper can see items that are currently for sale
* Dropdown box to sort items by price, name or category
* Dropdown button for each Product Header to show the product categories
* add to bag functionality is present with a quantity selector and add to bag button.
* "Keep Shopping" button to return to products page.
* Admin User will have the access to edit/delete items on this page

### Shopping Bag
* when empty will show an empty bag message and a link to products page.
* A summary of all added products that contains the image, name, price, description, quantity and subtotal
* Quantity can be updated or product removed within the page.
* A total cost breakdown is presented to the user with information about bag total/delivery/discount.
* A user can continue shopping by clicking on "Keep Shopping".
* User can check out using "Secure Checkout" button.

### Checkout
* User will provide delivery and billing details as well as the card to be used for payment
* Adjust bag button presented to user for easier navigation if any changes need to be made.
* A summary of what the user will purchase will be presented prior to purchasing it

### About
* A history and story of how the business works

### Contact
* Page where a user can send message to the business owner

## Features left to Implement

* Give other form of payment option like paypal 
* Give the customer ability to register using their social media
* Add a loyalty page where customer can earn points for every purchases they'll do
* Give discounts if the customer will spend more than 3000Php 

# Testing 
For testing procedure please click [Testing.md](https://github.com/gideongannaban/althea/blob/master/testing.md)

## Deploying to Heroku

The project was deployed to Heroku with all static and media files stored on Amazon S3. I also set up automatic deployment to ensure my Heroku app was always up to date with my GitPod repository.

1. Login to Heroku, click on "New" then on the dropdown choose "Create App".

![Heroku](https://github.com/gideongannaban/althea/blob/master/Readme/Images/deployment/Heroku.JPG)

2. Give the app a unique name and choose the region closest to your location then click "Create App"

![Heroku2](https://github.com/gideongannaban/althea/blob/master/Readme/Images/deployment/Heroku2.png)

3. Then on the 'Resources' tab, search and add on the Heroku Postgres database.

4. To use Postgres, install dj_database_url, and psycopg2 in the project terminal using the following commands:

  * pip3 install dj_database_url
  * pip3 install psycopg2

5. Freeze the requirements to ensure Heroku installs all the apps requirements when deployed using the following command:
  
  * pip3 freeze > requirements.txt

6. To migrate to the postgres, go to settings.py and import dj_database_url:
 
   ![postgres]()

    Note: The database URL can be accessed through the VARS Settings from the Heroku dashboard

7. Apply all migrations using the following command:

  * python3 manage.py migrate

  After migrations have been applied amend your database configurations t0:

  ![database]

  * This will ensure the Postgres database is used in deployment and your sqlite3 in development.

8. Create a superuser login:

  * python3 manage.py createsuperuser

9. Go to the Settings Tab, scroll to the "Config Vars" then click on "Reveal Config Vars".

![Heroku5](https://github.com/gideongannaban/althea/blob/master/Readme/Images/deployment/Heroku5.JPG)

10. Enter variables(key and value)

![vars](https://github.com/gideongannaban/althea/blob/master/Readme/Images/deployment/Vars.PNG)

11. Install gunicorn and freeze to the requirements.txt

  * pip3 install gunicorn
  * pip3 freeze > requirements.txt

12. Create a Procfile and add the following:

  * web: gunicorn (name of your django app).wsgi:application

  This tells Heroku to create a web dyno which will run gunicorn and serve the Django app.

13. Temporarily disable collectstatic to ensure that Heroku won't try to collect static files when we deploy. Add the following in the config VARS in heroku:

  * DISABLE_COLLECSTATIC = 1

14. Add the hostname of your Heroku app to allowed hosts in settings.py

  * ALLOWED_HOSTS = ['xxxxxxxx.herokuapp.com', 'localhost']

15. Commit and push all changes to github.

16. If you created your app on the website you will need to initialize your Heroku git remote:

  * heroku git:remote -a (heroku app name)
  * git push heroku master
  
16. From the deploy tab, select the Deployment method 'Github'.

![Heroku3](https://github.com/gideongannaban/althea/blob/master/Readme/Images/deployment/Heroku3.png)

17. After clicking the "Connect to Github", make sure Github profile name is displayed then type in your repository name then click "Search". Once repo is found click on "Connect".

![Heroku4](https://github.com/gideongannaban/althea/blob/master/Readme/Images/deployment/Heroku4.JPG)

18. Go to the Deploy Tab in Heroku and under the Automatic Deployment section click on "Enable Automatic Deploys". 

![Heroku7](https://github.com/gideongannaban/althea/blob/master/Readme/Images/deployment/Heroku7.JPG)

19. Under the Manual Deploy, click on the "Deploy Branch".

![Heroku8](https://github.com/gideongannaban/althea/blob/master/Readme/Images/deployment/Heroku8.JPG)

20. Heroku will now build the app using the required package

21. Once done, you will receive the message "Your app was successfully deployed" and click "View" to launch the app.

## Deploying AWS S3 Static and Media Files

## Making a Github Clone

1. In the [repository page](https://github.com/gideongannaban/althea), click on the Clone or Download button ( right beside the Gitpod button).
2. To clone the repository using HTTPS, copy the link in the "Clone with HTTPS".
3. Open Git Bash.
* Make sure Git Bash App is downloaded in your laptop/desktop
* Paste the Cloned link using the "Git Bash here" option.

![gitbash](https://github.com/gideongannaban/althea/blob/master/Readme/Images/deployment/gitbash.png)

4. Type "git clone" in the Git Bash command page, then paste the URL you copied.

![gitclone](https://github.com/gideongannaban/althea/blob/master/Readme/Images/deployment/gitclone.JPG)

5. Press Enter to create the local clone. 

![local clone](https://github.com/gideongannaban/althea/blob/master/Readme/Images/deployment/localclone.JPG)

## Environment Variable

### For this project I decided to add my environment variables from the gitpod settings.

1. Click the dropdown button besides you gitpod image in the gitpod workspace dashboard, then click on settings:

![gitpod1](https://github.com/gideongannaban/althea/blob/master/Readme/Images/deployment/gitpod1.PNG)

2. In the Environment variables Page, I manually added the needed keys and valuue:

![gitpod2](https://github.com/gideongannaban/althea/blob/master/Readme/Images/deployment/gitpod2.PNG)


# Credits

## Content
Product images and details for the Food Grocery, Fresh Goods and non-alcoholic Drinks were obtained from the following websites:
* [antshop](https://antshop.ph/)
* [mygroceryph](https://mygroceryph.com/)
* [gorobinsons](https://gorobinsons.ph/)
* [savvys](https://www.savvys.ph/)
* [agriculture](https://www.agriculture.com.ph/2018/11/21/native-chicken-farming/)
* [eggs](https://media.karousell.com/media/photos/products/2019/08/01/110019_243137255_thumbnail_progressive_thumbnail.jpg)

Alcoholic drinks images and details were obtained from below website:
* [alak](https://alak.ph/)

* Favicon logo was created from [canva](https://www.canva.com/)

## Acknowledgement 
Main source of inspiration for all my projects is our 2 years old daughter and my ever supportive wife. 

[Code Institute](https://codeinstitute.net/) For the excellent overall content and mini projects from the course
Thanks to [Tim](https://github.com/TravelTimN) and Igor Basuga for their endless support and patience. 


















 



