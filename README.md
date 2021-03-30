# Wilsons Express Sameday Limited - Booking and New Accounts Site with Packaging shop
**Forth Milestone Project: Full Stack Frameworks With Django - Code Institute**
## Introduction
Here is my fourth and final project for Code Institute’s Diploma in Software Development
I have built apon the Boutique Ado Project within the course and created a booking website for my current current employers, Wilson's Express Sameday Ltd.
The site consists of a quote form which can be then used to create a booking, a form to submit applications to make a new account, a contact form for any other queries 
and of course the shop so users can also purchase packaging supplies.
It is a simple CRUD application that a user is able to interact with and perform all the basic create, read, update and delete functions.
Users can create accounts, purchase items, view old orders, request an account to ship parcels, recieve quotes, book one off deliveries and also send any other messages. 


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
I created my site to allow users to be able to quickly and easily obtain quotes and then if they want to book a delivery once they know the cost. A user is also able to request a credit account via a form and once this application as been reviewed by an employee they can then create an account an send all the information needed manaually. If a user has any other needs such as sameday deliveries or any awkward delivries they are able to contact us via a contact form.
As we are a delivery company I also wanted a user to be able to view and buy packaging supplies to help them package their deliverys.

### Scope
| User   | User Stories |
|:------:| ------ |
| Site User | As a site user I want to easily Navigate through the site, create a shopping account, login and out, recieve confirmation emails for any actions I take and view my user profile. 
| Shopper | As a shopper I want to view the products on offer, a detailed view of each product, be able to purchase the products, easily view my bag and order totals and also be able to view any previous orders
| Delivery Sender | As a sender I want to be able to get quotes easily and then be able to book a delivery if the quote is acceptable to me. I may also want to open a credit account so I can have access to the booking portal and send more parcels.
| Admin / Employee | As the admin of the site I want to be able to see all the new quotes generated if a quote is not turned into a booking I want to see contact details so that I can send an email to try and turn it into a booking. I want to see any Bookings that are made as these need to be input to the booking portal. I also want to be able to see any orders that are made on the store so I can get these packed and sent out.


### Structure
This is a multiple page website, each page will display the main navigation bar with links to pages such as the quote page, and the store.
When a user navigates to the store a Second navigation bar appears with all the stores catagories. 
The homepage displays multiple CTA's pointing users to specific parts of the site and also a quote form which is linked to the send a parcel page and also once correctly filled in will save an entry into the quotes section on the admin page allowing employees to see quotes obtained on the website.
Multiple of the links on the main navigation take you away from my site for things such as Tracking a parcel or rescheduling a delivery. I did not need to build custom versions of these as APC overnight provide us with this functionality.

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