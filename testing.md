# Testing

## Manual Function Testing
Manual testing was carried out in different browsers and screen sizes to ensure site is not just responsive but also the apprearance and functionality is consisnte to all viewing platforms. The primary tool used for this was [Google Developer Tool](https://developers.google.com/web/tools/chrome-devtools) and the tests were done using the following screen sizes:
* Samsung Note 10
* Samsung S9+
* Iphone 5/SE
* Iphone 6/7/8
* Ipad/Ipad Pro
* Laptop 1024px

#### Browser Compatibility Testing
Browser testing was done using below browsers to ensure website can be viewed for all users. The website is responsive on all browsers except for the IE, the adding an image button overlaps in small screen. 

* Chrome
* Firefox
* Edge
* Safari
* IE

Summary of the testing result can be found [here](https://github.com/gideongannaban/althea/blob/master/Readme/Images/testing/responsivess.PNG)

## Testing User Stories 

### Viewing and Navigation

1. As a shopper, I should have information regarding delivery

 - Once the customer visits the site, they'll see the information regarding delivery fee, time and location in the home page. Additional information like minimum purchase to avail of free delivery can also be viewed on this site.


2. As a shopper, I should be able to view a list of all products and select some to purchase.

- From the home page, the user has couple of options to view the list of products. They can either click on the "Our Store" on the navbar, click on the product images in the home page or click on the "Shop" at the footer. 


3. As a shopper, I should be able view all the items in my shopping list with description/quantity/size and total cost at any time

- In the Our Store page, the customer needs to click on a product to view its description and price. From this page, the customer will have the option to add the item in the shopping bag by clicking on the "ADD TO BAG" button. They will get a pop-up message letting them know that they've successfully added the item in their bag. Then click on the bag icon on the upper right corner of the page to access the items added in their shopping bag.
  
### Sorting and Searching

1. As a shopper, I should be able to sort products available by name, price and category.

- In the Our Store page, the customer has the ability to sort by Name(A-Z or Z-A), Price(low - high or high - low) and Category(A-Z or Z-A). This button is located on the right part of their page. 

2. As a shopper, I should be able to search for a product by name, price and description.

 - Conveniently on top of the page, the customer can find a search field their for them to quickly find if an item is available for sale. They'll just need to type in their search critera then the site will look for a product that contains the search critera. 

3. As a shopper, I should be able to see what I've searched for and the number of results.

 - Once the customer clicks the magnifying glass it will show them the list of products that contains their search parameter
 
### Purchasing and Checkout

1. As a shopper, I should be able to select quantity and size if applicable when purchasing

 - On the Our Store page, the customer clicks on the product image then the next page will show them additional information of the product. On this page, the customer will have the option to select the quantity prior to adding it to the shopping bag.
 
2. As a shopper, I should be able to modify my order prior to paying for it.

 - After the customer clicks on the ADD TO BAG button they will see a small pop up message letting them know that they've successfully added the product in their bag. Once they've clicked on GO TO SECURE CHECKOUT, they'll be directed to the SHOPPING BAG page where they can see a summary of the item they are about to purchase. This will serve as their final checkpoint if they want to modify the quantity or remove it altogether. 

3. As a shopper, I should be able to enter my payment information securely.

 - Once the customer clicks on the Secure Checkout, they will directed to the CHECKOUT page where they'll enter their delivery details as well as the credit card they will use for payment. We use the payment service Stripe that takes over the payment on the site. There is a secure communication with our database and with Stripe. It will only allow payments if we have a secure secret key that approves the communication of both sides.

4. As a shopper, I should be able to view a summary of my orders before finalizing the purchase.

 - On the CHECKOUT Page, the customer will once again be shown the items that they're about to purchase as well as the amount and quantity.

5. As a shopper, I should be able to get a confirmation after checkout and receive an email with a confirmation of the order.

 - When the payment has been approved the customer will be redirected to the checkout success page where they can see an overview of there order. The customer will also receive a confirmation email with all the details of the order and shipping information when the payment has been approved.
  
### Registration and User Accounts 

1. As a Site user, I should be able to Easily Register to an account to be able to view my profile and purchase history.

 - On the Home page, the customer needs to click on the My Account then Register. They'll just need to provide their email address, username and Password. They will then receive an email where they'll need to click on verify so their account will be verified in the database.

2. As a Site user, I should be able to login and logout from my personal account.

 - Once the customer's account has been verified, they can now Login and Logout from the My Account page easliy. Once they've successfully login or logout they will be redirected to the Home page with toast message of success.

3. As a Site user, I should be able to recover my password just in case I forget it.

 - On the SIGN IN Page, the customer will have the ability to recover password by clicking on the Forgot Password. They will need to enter their email address then the store owner will send them an email to reset their password.

4. As a Site user, I should be able to Receive an email confirmation after registration.

 - Once the customer has successfully verified their accounts, they will receive another email confirming their account has been verified.

5. As a Site user, I should be able to update information on my profile anytime.

 - Customer can update their information anytime by logging in to their profile from the My Account. As of now, only their delivery details can be updated. 


### As an Admin
  
1. As an Admin, I should be able to add a product.

 - For the Admin User to be able to add a product, they would need first to login on their Admin Account. Then on the My Account they will need to chose Product Management. They will chose which category the product will be in then add the needed Product information like SKU, Name, description, Price and the Image Url. Adding image is optional. 

2. As an Admin, I should be able to edit or Delete a product.

 - The easiest way for an Admin User to edit or delete a product is by going to the Our Store Page. They will see the Edit | Delete option at the bottom of the product image. 

## Code Validation

### Validation of Python Code:

[pep8online.com](http://pep8online.com/checkresult) - used to inspect my Python code against the style conventions in PEP 8.

[Flake8](https://flake8.pycqa.org/en/latest/) - used to check if codes are in compliance with pep8. By using the following command I was able to check the problems across all my files without having to open each individual file.

  * python3 - m flake8

PEP8 Errors/Warnings:

* Line too long

  - Most of the errors were fixed but there were lines that I ignored to avoid breaking any variables

* Migration warnings and Avoid using null=True

  - These were ignored as it doesn't affect the functionality of the code

### Validation for jQuerry

- jQuerry code was validated using [jshint](https://jshint.com/) with 0 error.

### Validation for [CSS](https://jigsaw.w3.org/css-validator/)

No error warning messages were recevied.


### Validation for [HTML](https://validator.w3.org/)

  - I did "CTRL + U" in Google Chrome then copied the codes. 

Most of the errors detected were duplicate use of ID however per further checking the duplicates where located on the mobile version of the page thus I decided to ignore the messages. 

### Google Chrome Dev Lighthouse

[Lighthouse] was used to test the quality of the web pages.

Here are the results:

* Home Page

Desktop version

![desktop](https://github.com/gideongannaban/althea/blob/master/Readme/Images/testing/lighthouse-desktop-home%20v1.PNG)

Mobile version

![mobile](https://github.com/gideongannaban/althea/blob/master/Readme/Images/testing/lighthouse-home-mobile%20v1.PNG)

* Store Page

Desktop version

![desktop](https://github.com/gideongannaban/althea/blob/master/Readme/Images/testing/lighthouse-desktop-store%20v1.PNG)

Mobile version

![mobile](https://github.com/gideongannaban/althea/blob/master/Readme/Images/testing/lighthouse-store-mobile%20v1.PNG)


# Bugs:

The journey of this website is not with-out bugs either minor or major ones. These are some of the ones that took me sometime to debug. 

* At the beginning of the project, I decided to replaced some images from the admin account. After doing this, I run check on the progress of my project and I was getting below error.

![error1](https://github.com/gideongannaban/althea/blob/master/Readme/Images/testing/error1.PNG)

Steps done to Resolve:

  - I deleted the session ID from the cache as it's possible that the image I created was already in the bag. This works however whenever I add another item in the bag I was getting the same error. 

  - Finally contacted a Tutor for clarification. Looks like the value I put under the FREE_DELIVERY_THRESHOLD in settings.py was a decimal and but my contexts.py was a whole number. I added the Decimal in my free_delivery_delta under the bag_contents method.


* I was getting this error when I updated my checkout models to add country, province and town_or_city. 


![error2](https://github.com/gideongannaban/althea/blob/master/Readme/Images/testing/error2.PNG)


Steps done to Resolve:

  - I added default=None and changed null=True but now it's giving me the below error.

![error3](https://github.com/gideongannaban/althea/blob/master/Readme/Images/testing/error3.PNG)

  - I ended up deleting the previous Migrations then added default="" for the newly added variables. Then finally this worked.


* I was getting an error manually accessing the edit products url. I was typing in /store/edit/1/ on the page and it was giving below error.

![error4](https://github.com/gideongannaban/althea/blob/master/Readme/Images/testing/error4.PNG)


Steps done to Resolve:

  - I went back to the store page and then click on the same product then I noticed that it has a different product item number from the Product Details Page. It was showing as store/edit/77/ and futher research I learned that this is because I manually replaced these products from the admin. 


* After Deploying to Heroku, the images and css were not loading on the deployed project. There was no error prompt in the console so I was having a hard time debugging it. 

Steps done to Resolve:

  - I check with Tutors and worked with Tim and Igor to find a solution the whole day. Tim suggested to create a new postgres file on Heroku and retry. This fixed the bug I was experiencing. 

