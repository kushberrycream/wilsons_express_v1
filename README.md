# Wilsons Express Sameday Limited - Booking and New Accounts Site
**Forth Milestone Project: Full Stack Frameworks With Django - Code Institute**
## Introduction
Here is my fourth and final project for Code Institute’s Diploma in Software Development, I have created a booking website for my current employers, Wilson's Express Sameday Ltd. The site consists of a quote form which can be then used to create a booking, a form to submit applications to make a new account, a contact form for any other queries 
and of course the shop so users can also purchase packaging supplies.
It is a simple CRUD application that a user is able to interact with and perform all the basic create, read, update and delete functions.
Users can create online web accounts for my site, Pay for bookings, view old bookings, request a credit account, recieve quotes, book one off deliveries and also send any other messages. 


## Demo

Click the image below to view my Live Portfolio.
<a href="https://wilsons-express-django.herokuapp.com/">
  <img alt="am i responsive" src="https://github.com/kushberrycream/wilsons_express_v1/blob/master/media/wilsons.png?raw=true" width="800">
</a>

## Contents
- [Introduction](#wilsons-express-sameday-limited---booking-and-new-accounts-site-with-packaging-shop)
- [Demo](#demo)
- [UX](#ux)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
    * [Surface](#surface)
- [Technologies Used](#technologies-used)
- [Features](#features)
    * [Existing Features](#existing-features)
    * [Features Left to Implement](#features-left-to-implement)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgments](#acknowledgments)

## UX  
### Strategy
I created my site to allow users to be able to quickly and easily obtain quotes and then if they want to book a delivery once they know the cost. A user is also able to request a credit account via a form and once this application as been reviewed by an employee they can then create an account an send all the information needed manually. If a user has any other needs such as sameday deliveries or any awkward deliveries they are able to contact us via a contact form.

### Scope
| User   | User Stories |
|:------:| ------ |
| Site User | As a site user I want to easily Navigate through the site, create a web account, login and out, recieve confirmation emails for any actions I take and view my user profile. 
| Delivery Sender | As a sender I want to be able to get quotes easily and then be able to book a delivery if the quote is acceptable to me. I may also want to open a credit account so I can have access to the booking portal and send more parcels.
| Admin / Employee | As the admin of the site I want to be able to see all the new quotes generated if a quote is not turned into a booking I want to see contact details so that I can send an email to try and turn it into a booking. I want to see any Bookings that are made as these need to be input to the booking portal. I also want to be able to see any orders that are made on the store so I can get these packed and sent out. I also want to see groups of bookings, each individual booking from a user will have a seperate line item in the admin.

The main Purpose of the site is to have users interact with the website to either book one off deliveries or to get in contact to open accounts 


### Structure
This is a multiple page website, each page will display the main navigation bar with links to pages such as the quote page. Some of the links on the main navigation take you away from my site for things such as Tracking a parcel or rescheduling a delivery. I did not need to build custom versions of these as APC overnight provide us with this functionality.
The homepage displays a large CTA pointing users to use the quote form. If the user chooses to use the form they are taken to the quotes page with all the quote information. On the Quotes page two links are available one to obtain the quote and the other to proceed with the quote and enter delivery/collection information. The Enter details button only works if the form has been filled in and a quote has been obtained, if any fields are changed then the enter details button is disabled. 
I have two forms, one if for requesting a credit account, once completed this will add an entry into the create account section on the admin dashboard, once reviewed a member of the salesteam will be in contact to arrange the account. The Second form is a standard contact form for which sends an email to a member of staff, this can be used for general parcel enquires or site recommendations and even possible bugs.
A FAQ's page is supplied to give users more information. Employees are able to update this from the main site by either going to the FAQs page and editing existing FAQs or they can go to the add FAQ page and enter a new qauestion and answer.
The bookings bag gives the user a clear overview of all the bookings they have made, it also give the ability to delete bookings as they may not be needed no more.
From the bag the user can proceed to the checkout page where a Billing form is provided and another breakdown of the bookings. Once the Checkout is completed the user is presented with a confirmation of purchase. 
A basic profile page is provided so users can keep on record any billing information or they can even view previous bookings.
All Auth has been implemented to help with Authentification as this gives me all the functionality I need i just had to change the styling

### Skeleton
[Homepage](https://github.com/kushberrycream/wilsons_express_v1/blob/master/media/wireframes/homepage.png?raw=true) 

[Quote Page](https://github.com/kushberrycream/wilsons_express_v1/blob/master/media/wireframes/quote_page.png?raw=true)

[Booking Page](https://github.com/kushberrycream/wilsons_express_v1/blob/master/media/wireframes/booking_page.png?raw=true)

[Booking Bag](https://github.com/kushberrycream/wilsons_express_v1/blob/master/media/wireframes/booking_bag.png?raw=true)

[Checkout](https://github.com/kushberrycream/wilsons_express_v1/blob/master/media/wireframes/checkout_page.png?raw=true)

[Profile](https://github.com/kushberrycream/wilsons_express_v1/blob/master/media/wireframes/profile_page.png?raw=true)

[FAQS](https://github.com/kushberrycream/wilsons_express_v1/blob/master/media/wireframes/faqs_page.png?raw=true)

[Contact Page](https://github.com/kushberrycream/wilsons_express_v1/blob/master/media/wireframes/contact_page.png?raw=true)

### Surface
The Homepage / Landing Page displays a full page background with a quote form. A Navbar is visible at the top throughout the site giving users access to almost anywhere from anywhere in the site. The rest of the site is a white container giving the site a clean and ledgable design and keeps it easy to read. Multiple forms are available to users, all with a uniform style and again helping keep the site clean and ledgable. I have used the font Montserrat as i believe it looks very modern and fits nicely with my website. Not many Images are needed for the site as the majority of it is forms for users to fill in.

<p align="right">
  <a href="#contents">Back to Contents :arrow_heading_up:</a> 
</p>

## Technologies Used

Here is a list of all the technologies used throughout the project!

- [Balsamiq Mockups 3](https://balsamiq.com/)
    - I have used Balsamiq to create my wireframes.
- [Python3](https://www.python.org/download/releases/3.0/)
    - I have used Python3 and multiple dependancies to create my website. All dependancies can be viewed within my requirements.txt file.
- [Django](https://www.djangoproject.com/)
    - I have used the Django Framework to create a secure and maintainable website.
- [HTML5](https://www.w3.org/html/)
    - I use HTML to create the templates used within my web apps.
- [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)
    - CSS gives my site its look and style.
- [JQuery](https://www.jquery.com/)
    - JQuery is used to initialize a few components and generally improve user experience.
- [Bootstrap 4.5.3](https://www.getbootstrap.com/)
    - I have used the bootstrap framework to help create a uniform responsive web app.
- [Heroku](https://www.heroku.com/)
    - Heroku is used to host my finished website.
- [SQlite3](https://docs.python.org/3/library/sqlite3.html)
    - Throughout production my database has been SQLite3 but once moved onto production PostgreSQL is used.
- [Heroku PostgresSQL](https://www.heroku.com/postgres)
   - Once my Project is live it is using the built in add on provided by Heroku, This is a fully managed service and also can provide support with any issues.
- [Amazon S3](https://aws.amazon.com/s3/)
    - Amazon S3 is used for online storage of all my images and static files.
- [Font Awesome](https://fontawesome.com/)
  - Font Awesome was used for all of my icons.
- [Google Maps Api](https://developers.google.com/maps/gmp-get-started) 
  - The contact page displays a map allowing users to find our location.

<p align="right">
  <a href="#contents">Back to Contents :arrow_heading_up:</a> 
</p>

## Features

### Existing Features
- [x] My site uses the bootstrap framework for the grid system and to help with the responsive mobile-first desgin with preset classes etc.
- [x] The home page has minimal text, but incorporates a quote form which a user can fill in to obtain quotes, this is also accesable from the navbar. 
- [x] An Authentification system is in place to let users create online accounts.
- [x] A Form is available to request accounts.
- [x] A plain contact form is supplied to allow users to send general messages or to ask for services that are bespoke.
- [x] A Faq page is available for users. This may avoid unwanted questions as the information is already supplied.
- [x] I have made a small covid section to give the public information on what we as a company are doing about the situation.
- [x] We have linked up a bag and checkout to allow users to purchase the bookings they have created.

### Features Left to Implement
- [ ] I want to provide a online shop which provides users with packaging equipment.
- [ ] In the future I wish to have the majority of the website to be automatic using the various APC Overnight API's. As once a user has booked a delivery or collection then someone has to manually book this onto the booking portal.
- [ ] I plan to update the profile page so that it has a little more information and the user can view previous bookings and create new bookings from these. I may even provide a credit system so users can have more discounts and incetives if they purchase in advanced.
- [ ] My boss wishes to have a page or area of the site in which advertisements can be placed with offers or products from current customers. Details would need to be worked out between participating customers and the us before this is possible.

<p align="right">
  <a href="#contents">Back to Contents :arrow_heading_up:</a> 
</p>

## Testing
All the testing throughout the site has been done manually. Such as the Quote form, this was tested manually by completing the form and seeing the results. This was very tedious as it meant filling out the same form possible hundreds of times. There may be a way in which I could do this Automatically. 

All the python code is linted and debugged by gitpod so I have not had to worry about syntax or format as this has let me know throughout when I have not been using the correct syntax or I have input my code incorrectly. I have also been using django which helps as the debug mode gives a full indepth view of the issues. All the HTML and CSS pass validation with [W3 Validators](https://validator.w3.org) but HTML does throw up errors due to the fact I am using djangos templating but there are no major errors.

My site is responsive on multiple media devices and viewports. I used googles DevTools to test all the different viewport resolutions, I also did this on Opera and firefox.
I generally had no issues with this as I mainly used Bootstraps preset classes to help create a flexbox layout. All the pages respond correctly and every link acts in the expected way. I've had no console errors within my code and again act as expected.

To avoid any issues with javascript I have stopped users being able to interact with the quote and booking form if they have javascript disabled, this will stop any bugs later on because users will be able to do things with the forms that I do not wish.

My main issue throughout the development was the quote form as there didnt seem to be anything online to help me create this. Sometimes I would think it was working perfect and i would try it once more and I would get a database error or something similar. After quite sometime it does finally seem to be working as expected.

Here are a few of the manual processes i've done to test my code:

1. NavBar:
    1. Throughout development I checked all links would respond correctly. By clicking links I was able to confirm this.
    2. Next I went into Devtools and turned on mobile emulation to confirm the Toggler button appears, I would click to confirm the button worked correctly.
    3. Once the links were displayed I clicked each to confirm the navbar opened the page and closed the navbar as intended.
    4. I also checked all available viewports within devtools to makes sure it displayed correctly.
    5. I next disabled javascript and can confirm the navbar still works as expected
    6. All tests were a success and the only issues where trying to get the navbar dropdowns to work without javascript.

2. Responsivness:
    1. I went to Devtools on chrome and chose various viewports, checked to see any display issues.
    2. If issues were discovered I would use Unicorn Revealer to see any hard to find padding / margin issues.
    3. If data did not display properly I added relevant media queries or edited javascript or content until it was correct.
    4. I then chose the responsive option on the viewports and checked as many resolutions as possible.
    5. I repeated the processes for any errors in what was displayed.
    6. I also checked the responsiveness on my personal iPhone and work Android as Devtools I find is not always 100% correct.
    7. If any errors did occur I corrected them accordingly.

3. Authentification:
    1. First I navigated to the register page and signed up.
    2. A confirmation message is displayed and confirmation email is sent asking to verify email.
    3. I check my emails and can see a email with a link.
    4. Once clicked I am taken back to my site's confirmation page.
    5. Once confirmed a Success message displayes and now I can login.
    6. When logged in as a superuser I am given complete access including the admin dashboard, when a user logs in they have access to a profile page.
    7. I tested the social accounts by clicking each link and going through the process of linking the social accounts, both worked perfectly.
  
4. Booking Bag:
    1. The booking bag was tested by booking multiple deliveries. Once booked I navigated to the bag.
    2. In the bag I checked the table displayed correctly and also responded well when on different viewports.
    3. This took a little while to get correct but after a few css tweeks it was looking good.

5. Checkout:
    1. Once the bag was full I can then proceed to the checkout.
    2. A form is displayed with a small breakdown of the deliverys booked.
    3. if the form is filled in incorrectly the correct validation errors are displayed.
    4. I filled in the form and card details and confirmed they worked.
    5. I was then shown a success page with a further breakown of the deliveries and cost.
    6. I also selected the save details checkbox and it saved my details to my profile.

6. Contact Form:
    1. I filled in the form then a success message is displayed once submitted.
    2. I checked my emails and it had arrived with the correct info.
    3. I did this multiple times and improved the email each time.

7. FAQS form:
    1. If i am signed in as a superuser I have access to a form for adding FAQs.
    2. The link displays correctly and opens up the form.
    3. Once filled in and submitted the new FAQ is already available to see on the FAQ page.
    4. This also works on the admin page too.

8. Create Account Form:
    1. I fill out the form and it submits correctly.
    2. I then navigate to the admin and can see a new entry is in the create account section.
    3. When selected it gives all the information just provided so a sales person can get in contact.

9. Quote and Booking Forms:
    1. Hundreds of times I filled in the forms and got different results many times.
    2. First the services would not work correctly but that was how the form data was being read.
    3. Next I realised a user can change the postcodes and get a cheaper price, this was avoided by making a user Request an updated quote if any inputs are changed.
    4. Next I realised if the user goes to the booking page again they can change the postcodes so i displayed them as a variable not an input.
    5. I then disabled the item inputs as they could also change these once a booking was partially done.
    6. Many times when doing a dummy booking my data would be too long for the postgres table.
    7. This only happened sometimes and had to change the values on the model and make migrations.
    8. after many attempts this now seems to be working perfectly.

<p align="right">
  <a href="#contents">Back to Contents :arrow_heading_up:</a> 
</p>

## Deployment

### Commiting to Github
1. Using my terminal window I firstly use `git pull ` to pull the most upto date version of my repository.
2. Once upto date I edit everything I need to and use `git add .` to stage all the edited files for commiting.
3. Using `git status` I usually view to see I have staged all the files I want to and I have no unwanted files being commited.
4. Next using `git commit` I commit to the local Repository and then `git push` to finally push the changes to the master branch.

### Deploying to Heroku
1. Firstly I needed to go to my Account dashboard, here I can select New and Create New App.
2. I chose a unique app name, the region of Europe and then pressed create app.
3. Once Created I was brought to the deploy section of my app, here I decided to chose to deploy with Github.
4. Heroku then asked for the repo name of my app I wished to deploy.
5. I selected connect once my repo was found and I was then able to commit to the master branch on Github. 
It will then Deploy Automatically as I have automatic deploys turned on.
6. I then selected resources, searched for Heroku PostgresSQL and selected the free / Hobby Tier.
7. The site is almost deployed but I then needed to go to the settings section and let Heroku know of any enviroment variables such as the ip, Port, Secret key, database URI, etc.

### Using Amazon S3 Data storage
1. Sign up for AWS and navigate to S3.
2. Create a new bucket and name it a sensible name.
3. Unblock all Public Access and acknowledge you understand it is going to be public.
4. In the properties tab turn on static website hosting and enter some default error and index values.
5. Next create a coors configuration, a security policy and set the objects permissions for everyone under the public access section.
6. Using AWS IAM we create an access policy giving the group access to the s3 bucket.
7. Using amazons s3 full access policy I then link this up to the bucket i ish to allow access to.
8. Once a policy is created it can be attatched to the group by crreating a user.
9. Download the csv with the users access key and secret access key

### Connecting Django to S3
1. Install boto3 and django-storages.
2. Add storages to settings in django and also all the AWS variables and settings.
3. Don't add the user access key or the secret key otherwise this will be a security issue.
4. Add the enviroment variables to the heroku config variables.
5. In production I also want to tell django that s3 will be used to collect static data.
6. create a new file called custom storages and create a few custom classes.
7. In settings let django know we want to use the custom storage classes.

### Cloning the repository
To run this repository locally:
1. Click "Code" at the top of this repository.
2. Select Download Zip or Copy the URL to your clipboard. 
3. Open up Terminal and select the location in which you wish to clone this directory.
4. Then type `git clone` and copy `https.` 
5. Press enter and you will have succesfully cloned this Repository. 

### Installing dependencies
Installing Dependencies is very simple and I have supplied a requirements.txt to help with this process. Once the repository has been cloned before it can be ran the user will need to open the terminal on their IDE and type `pip3 install -r requirements.txt`. All the dependencies should now download and you are ready to go.

<p align="right">
  <a href="#contents">Back to Contents :arrow_heading_up:</a> 
</p>

## Credits
### Content
- All External Links are owned and operated by APC Overnight.
- FAQ's have been found on [APC Overnights](https://apc-overnight.com/) Website and also a few other APC Depots websites. 
### Media
- [APC Overnight Background](https://www.apc-overnight.com) This is the picture used throughout the site as the background as an employee I have access to these images.
- [Favicon](https://www.apc-overnight.com) The APC logo was obtained through my currect employment.
### Acknowledgments
- [Django Documentation](https://docs.djangoproject.com/en/3.1/) This helped me with the syntax and any queries I had with the Django Framework as alot of the Examples, and other questions online dealt with different versions of Django.
- [StackOverflow](https://stackoverflow.com/questions/50346326/programmingerror-relation-django-session-does-not-exist/) StackOverflow really helps! 9/10 someone has already asked my questions and have got the answers. It saves alot of time when it comes to working out problems.
- [Google](www.google.co.uk) Google is my biggest resource again someone has usually asked my questions.
- [Boutique Ado](www.code-institute.net) The site was originally built around the boutique ado project and was then updated and turned into a quote / booking platform instead of a store.

<p align="right">
  <a href="#contents">Back to Contents :arrow_heading_up:</a> 
</p>
