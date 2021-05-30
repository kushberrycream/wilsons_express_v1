# Wilsons Express Sameday Limited - Booking and New Accounts Site
**Forth Milestone Project: Full Stack Frameworks With Django - Code Institute**
## Introduction
Here is my fourth and final project for Code Institute’s Diploma in Software Development, I have created a booking website for my current employers, Wilson's Express Sameday Ltd. The site consists of a quote form which can be then used to create a booking, a form to submit applications to make a new account, a contact form for any other queries 
and of course the shop so users can also purchase packaging supplies.
It is a simple CRUD application that a user is able to interact with and perform all the basic create, read, update and delete functions.
Users can create online web accounts for my site, Pay for bookings, view old bookings, request a credit account, recieve quotes, book one off deliveries and also send any other messages. 


## Demo

Click the image below to view my Live Portfolio.
<a href="">
  <img alt="am i responsive" src="">
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

I wanted the users 


### Structure
This is a multiple page website, each page will display the main navigation bar with links to pages such as the quote page. Some of the links on the main navigation take you away from my site for things such as Tracking a parcel or rescheduling a delivery. I did not need to build custom versions of these as APC overnight provide us with this functionality.
The homepage displays a large CTA pointing users to use the quote form. If the user chooses to use the form they are taken to the quotes page with all the quote information. On the Quotes page two links are available one to obtain the quote and the other to proceed with the quote and enter delivery/collection information. The Enter details button only works if the form has been filled in and a quote has been obtained, if any fields are changed then the enter details button is disabled. I have two forms which just send emails 


When a user uses the Quote form brings you to the send a parcel page with the form pre-filled and the quote at the very top, the user can then proceed with the quote or they can just navigate to somewhere else on the site. If they proceed they will be able to fill in the booking form and use the stripe payment form to pay for the booking. This then moves the Quote into the booking section on the admin promting an employee to book the collection and delivery.

The Store is very basic and has a selection of categories which each have a number of products, they can choose a product to bring up details and then also use the quantity selector to choose an amount. A shopping bag is provided to give a clear view on the items selected and the total price of all the items. The user can then checkout by filling out a delivery details form and the stripe payment form. 

For any other queries a user may have a contact form is supplied as a user may want to book a sameday delivery or send something we cannot send via an overnight service. They may even have other questions that they need answering regarding current bookings etc.

### Skeleton

### Surface
The Homepage / Landing Page displays a full page background with the quote form with a white background and a small introduction, When a user navigates through the page a white container sits on top allowing on most screen for the APC overnight logo to be visible. Giving the main content a white background helps to keep the contents clear and legable to the end user. The font used is Montserrat as I think it is very clean, minimal and practical. All the forms and buttons all follow the same styling and keeping in with all the companies colors.
The store follows the same design as the rest of the site but displays a list of products in a gallery style layout.

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

<p align="right">
  <a href="#contents">Back to Contents :arrow_heading_up:</a> 
</p>

## Features

### Existing Features

### Features Left to Implement
- [ ] I want to provide a online shop which provides users with packaging equipment.
- [ ] In the future I wish to have the majority of the website to be automatic using the various APC Overnight API's. As once a user has booked a delivery or collection then someone has to manually book this onto the booking portal.

<p align="right">
  <a href="#contents">Back to Contents :arrow_heading_up:</a> 
</p>

## Testing

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
1.

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
- 
### Media
- [APC Overnight Background](https://www.apc-overnight.com) This is the picture used throughout the site as the background as an employee I have access to these images.
- [Favicon](https://www.apc-overnight.com) The APC logo was obtained through my currect employment.

### Acknowledgments
- [Django Documentation](https://docs.djangoproject.com/en/3.1/) This helped me with the syntax and any queries I had with the Django Framework as alot of the Examples, and other questions online dealt with different versions of Django.

<p align="right">
  <a href="#contents">Back to Contents :arrow_heading_up:</a> 
</p>
