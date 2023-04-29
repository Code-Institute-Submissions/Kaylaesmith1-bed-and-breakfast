# The Wine Garden BnB | Testing

Return to [README](https://github.com/Kaylaesmith1/bed-and-breakfast/blob/main/README.md)

## Code Validation

### HTML
All HTML pages were validated using the [W3C HTML Validator](https://validator.w3.org/) to check for any problems or syntax errors. Please see the results below for each page.

<details>
  <summary>Home Page - No errors</summary>
  
  ![HTML Validation - Home page](/documentation/validation/validator-home-page.png)

</details>

<details>
  <summary>Sign Up Page - No errors</summary>
  
  ![HTML Validation - Sign up page](/documentation/validation/validator-signup-page.png)
</details>

<details>
  <summary>Log In Page - No errors</summary>
  
  ![HTML Validation - Log in page](/documentation/validation/validator-login-page.png)
</details>


<details>
  <summary>Log Out Page - No errors</summary>
  
  ![HTML Validation - Log out page](/documentation/validation/validator-logout-page.png)
</details>


<details>
  <summary>About Page - No errors</summary>
  
  ![HTML Validation - About page](/documentation/validation/validator-about-page.png)
</details>

<details>
  <summary>Menu Page (non-authenticated user) - No errors</summary> 
  
  ![HTML Validation - Menu page](/documentation/validation/validator-menu-page.png)
</details>

<details>
  <summary>Menu Page (superuser) - No errors</summary> 
  
  ![HTML Validation - Menu page](/documentation/validation/validator-menu-superuser.png)
</details>
<details>
  <summary>Add Menu Item Page - No errors</summary>
  
  ![HTML Validation - Add Menu Item page](/documentation/validation/validator-add-menu-item-page.png)
</details>
<details>
  <summary>Edit Menu Item Page - No errors</summary>
  
  ![HTML Validation - Edit Menu Item page](/documentation/validation/validator-edit-menu-item-page.png)
</details>
<details>
  <summary>Delete Menu Item Page - No errors</summary>
  
  ![HTML Validation - Delete Menu Item page](/documentation/validation/validator-delete-menu-item-page.png)
</details>

<details>
  <summary>Contact Us Page - No errors</summary>
  
  ![HTML Validation - Contact Us page](/documentation/validation/validator-contact-us-page.png)
</details>

<details>
  <summary>Book A Room Page - No errors</summary> 
  
  ![HTML Validation - Add Booking page](/documentation/validation/validator-add-booking.png)

</details>

<details>
  <summary>My Bookings Page - No errors</summary> 
  
  ![HTML Validation - My Bookings page](/documentation/validation/validator-my-bookings-page.png)

</details>  

<details>
  <summary>Edit A Booking Page - No errors</summary> 
  
  ![HTML Validation - Edit Booking page](/documentation/validation/validator-edit-bookings-page.png)

</details> 
<details>
  <summary>Delete A Booking Page - No errors</summary> 
  
  ![HTML Validation - Delete Booking page](/documentation/validation/validator-delete-booking-page.png)

</details> 

<details>
  <summary>404 Error Page - No errors</summary> 
  
  ![HTML Validation - Delete Booking page](/documentation/validation/validator-404-error-page.png)
</details>


### CSS
CSS codes used in the website were validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). No errors were found, though one warning was mentioned regarding importing style sheets. I imported Google Fonts. Both the passing validation and the warning can be seen below.

<details>
  <summary>CSS Codes - No errors, one warning</summary> 
  
![CSS Validation - Full CSS, no error](/documentation//css-validator.png)

![CSS Validation - Warning](/documentation/validation/css-validator-warning.png)
</details>

### JavaScript
JavaScript codes used on the website were validated using [JSHint](https://jshint.com/). No errors were found, though there were a few warnings regarding undefined / unused variables. Please see the image below for explanations.

<details>
  <summary>JavaScript Codes - A few warnings that don't affect the functionality of the page. See explanations.</summary> 
  
![JS Validation - Warnings](/documentation/validation/js-validator.png)
</details>

### Python
Python codes used throughout the application were validated using [CI Python Linter](https://pep8ci.herokuapp.com/) and no issues or errors were found.
Please see the results for each page below.

#### wine_garden_bnb App
<details>
  <summary>asgi.py - No errors</summary> 
  
![Python Validation](/documentation/validation/python-asgi.png)
</details>

<details>
  <summary>settings.py - No errors</summary> 
  
![Python Validation](/documentation/validation/python-settings.png)
</details>

Note: `# noqa` was added to Django generated codes under `AUTH_PASSWORD_VALIDATORS` and to Cloudinary storage under `STATICFILES_STORAGE` to combat the "line too long" errors that originally arose. `# noqa` forces these errors to be ignored as the text could not be shortened in the file.

<details>
  <summary>urls.py - No errors</summary> 
  
![Python Validation](/documentation/validation/python-urls.png)
</details>

<details>
  <summary>wsgi.py - No errors</summary> 
  
![Python Validation](/documentation/validation/python-wsgi.png)

</details>

#### bnb App
<details>
  <summary>admin.py - No errors</summary> 
  
![Python Validation](/documentation/validation/python-admin.png)
</details>

<details>
  <summary>apps.py - No errors</summary> 
  
![Python Validation](/documentation/validation/python-apps.png)
</details>

<details>
  <summary>forms.py - No errors</summary> 
  
![Python Validation](/documentation/validation/python-forms.png)
</details>

<details>
  <summary>models.py - No errors</summary> 
  
![Python Validation](/documentation/validation/python-models.png)
</details>

Note: `# noqa` was added to line 94 to combat the "line too long" error that originally arose.

<details>
  <summary>urls.py - No errors</summary> 
  
![Python Validation](/documentation/validation/python-bnb-urls.png)
</details>

Note: `# noqa` was added to lines 3, 21 and 22 to combat the "line too long" errors that originally arose.

<details>
  <summary>views.py - No errors</summary> 
  
![Python Validation](/documentation/validation/python-views.png)

</details>

Note: `# noqa` was added to line 1 to combat the "line too long" error that originally arose.

## Accessibility
[Wave Web Accessibility Evaluation Tools](https://wave.webaim.org/) were used to test accessibility. Please see the results below for each page.

<details>
  <summary>Home Page - No errors</summary>
  
![Wave Validation](/documentation/validation/wave-home.png)

</details>

<details>
  <summary>Sign Up Page - No errors</summary>
  
![Wave Validation](/documentation/validation/wave-signup.png)

</details>

<details>
  <summary>Log In Page - No errors</summary>
  
![Wave Validation](/documentation/validation/wave-login.png)

</details>
 
<details>
  <summary>About Page - No errors</summary>
  
![Wave Validation](/documentation/validation/wave-about.png)
</details>

<details>
  <summary>Menu Page - No errors</summary>
  
![Wave Validation](/documentation/validation/wave-breakfast.png)
</details>

<details>
  <summary>Add Menu Item Page - Missing form label error, see documentation</summary>

![Wave Validation](/documentation/validation/wave-add-menu.png)
</details>
There are two missing form label errors due to crispy forms. Neither affect the fuctionality of the page and were therefore left as is.

<details>
  <summary>Edit Menu Item Page - Missing form label error, see documentation</summary>
  
![Wave Validation](/documentation/validation/wave-edit-menu.png)
</details>
There are two missing form label errors due to crispy forms. Neither affect the fuctionality of the page and were therefore left as is.

<details>
  <summary>Delete Menu Item Page - No errors</summary>
  
![Wave Validation](/documentation/validation/wave-delete-menu.png)
</details>

<details>
  <summary>Contact Us Page -  Missing form label error, see documentation</summary> 
  
![Wave Validation](/documentation/validation/wave-contact.png)
</details>
One error was identified for a missing form label for the email field. This label is present and follows the same style as the other three fields in the form that are free of errors. This error does not affect the functionality of the form nor of the app overall.

<details>
  <summary>Add A Booking Page - No errors</summary> 
  
![Wave Validation](/documentation/validation/wave-add-booking.png)

</details>

<details>
  <summary>My Bookings Page - No errors</summary> 
  
![Wave Validation](/documentation/validation/wave-my-bookings.png)

</details>

<details>
  <summary>Edit A Booking - No errors</summary> 
  
![Wave Validation](/documentation/validation/wave-edit-booking.png)

</details>

<details>
  <summary>Delete A Booking - No errors</summary> 
  
![Wave Validation](/documentation/validation/wave-delete-booking.png)

</details>

<details>
  <summary>404 Error Page - No errors</summary> 
  
![Wave Validation](/documentation/validation/wave-404.png)
</details>

## Browser Testing
The Website was tested on Google Chrome, Firefox and Safari browsers. No functionality issues were noted, though the Get to Know Us section on the About page in Safari was slightly elongated when viewed on a MacBook Air laptop. This was not an issue when opened through Safari on an iphone.

## Device Testing
The website was tested manually on a variety of devices, either personally by the site creator (Kayla Smith) or by friends and family members. Devices included laptop computers, iPhone8 plus, iPhoneXR, iPad and Android devices to ensure responsiveness on various screen sizes. The website performed as intended. Responsive design was also checked throughout all stages of development using Chrome developer tools through inspect.

## Features Testing
Manual testing was done using Google Chrome to verify that all the features worked as designed. No issues were found. 

### Browser Tab
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Favicon | Display | Favicon is displayed correctly in the browser tab on all pages | PASS
Title | Display | "About" is displayed in a banner as the title of the About page | PASS
Title | Display | "Contact Us" is displayed in a banner as the title of the Contact Us page  | PASS
Title | Display | "Breakfast" is displayed in a banner as the title of the Menu page  | PASS
Title | Display | "Add A Menu Item" is displayed in a banner as the title of the Menu page  | PASS
Title | Display | "Edit Menu Item" is displayed in a banner as the title of the Menu page  | PASS
Title | Display | "Delete Menu Item" is displayed in a banner as the title of the Menu page  | PASS
Title | Display | "Add A Booking" is displayed in a card on the booking page | PASS
Title | Display | "Booking" is displayed in a banner as the title of the My Bookings page   | PASS
Title | Display | "Edit Your Booking" is displayed in a card on the Edit Bookings page | PASS
Title | Display | "Delete Your Booking" and 'are you sure' is displayed in a card on the Delete Booking page | PASS
Title | Display | "Sign Up" is displayed on a card with a form to fill out on the Sign Up page | PASS
Title | Display | "Log In" is displayed on a card on the Log In page | PASS
Title | Display | "Log Out" is displayed on the Log Out page on a card with a button asking the user if they're sure | PASS

### Navigation Bar
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Menu | Display | Links displayed side by side in the navigation bar for screen sizes with a minimum width of 992px | PASS
Logo | Click | Navigates to Home page | PASS
Home Link | Click | Navigates to Home page | PASS
About Link | Click | Navigates to About page | PASS
Menu Link | Click | Navigates to Breakfast page | PASS
Contact Us Link | Click | Navigates to Contact Us page | PASS
My Account Link (unauthenticated) | Click | Opens a dropdown menu for  unauthenticated users with 'Log in' and 'Sign up' buttons| PASS
My Account Link (uthenticated) | Click | Opens a dropdown menu for  authenticated users with 'My Bookings' and 'Book A Room' buttons| PASS
Sign Up Link | Display | Only available if the user is not logged in | PASS
Sign Up Link | Click | Navigates to Sign Up page | PASS
Log In Link | Display | Only available if the user is not logged in | PASS
Log In Link | Click | Navigates to Log In page | PASS
Log Out Link | Display | Only available if the user is logged in | PASS
Log Out Link | Click | Navigates to Log Out page and asks user if they're sure they want to log out | PASS
My Bookings Link | Display | Shows logged-in users their bookings | PASS
Book A Room Link | Display | Shows logged-in users a form to book a room | PASS
All Links | Hover | Color changes from pomegranate color to dark mint green with hover effect | PASS

### Hamburger Menu
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Menu | Display | Hamburger menu displayed in the navigation bar for screen sizes less than 992px in width | PASS
Animation | Click | Animation functions correctly - menu options are listed on the left-hand side under the page logo | PASS
Menu Closure | Click | Hamburger menu closes when clicked a second time or when clicking a page link | PASS
Logo | Click | Navigates to Home page | PASS
Home Link | Click | Navigates to Home page | PASS
About Link | Click | Navigates to About page | PASS
Menu Link | Click | Navigates to Breakfast page | PASS
Contact Us Link | Click | Navigates to Contact Us page | PASS
Sign Up Link | Display | Only available if the user is not logged in | PASS
Sign Up Link | Click | Navigates to Sign Up page | PASS
Log In Link | Display | Only available if the user is not logged in | PASS
Log In Link | Click | Navigates to Log In page | PASS
Log Out Link | Display | Only available if the user is logged in | PASS
Log Out Link | Click | Navigates to Log Out page and asks user if they're sure they want to log out | PASS
My Bookings Link | Display | Shows logged-in users their bookings | PASS
Book A Room Link | Display | Shows logged-in users a form to book a room | PASS
All Links | Hover | Color changes from pomegranate color to dark mint green with hover effect | PASS

### Footer
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Position | Display | Footer remains at the bottom of each page, even if the content of the page doesn't occupy the full view height | PASS
GitHub Link | Click | Opens my personal GitHub page in a new tab | PASS
Twitter Link | Click | Opens Twitter in a new tab | PASS
Instagram Link | Click | Opens Instagram in a new tab | PASS
Facebook Link | Click | Opens Facebook in a new tab | PASS
All Links | Hover | Color changes from pomegranate color to dark mint green with hover effect | PASS

### Sign Up Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Username Field | Leave Empty | Form does not submit | PASS
Username Field | Leave Empty | Error message is displayed | PASS
Username Field | Enter an Empty String | Form does not submit | PASS
Username Field | Enter an Empty String | Error message is displayed saying field is required | PASS
Username Field | Duplicate Username | Form does not submit | PASS
Username Field | Duplicate Username | Error message is displayed | PASS
Email Field | Leave Empty | Form submits without an email address as this is an optional field | PASS
Email Field | Enter Invalid Format | Form does not submit, error message shown | PASS
Email Field | Duplicate Email Address | Form does not submit | PASS
Email Field | Duplicate Email Address | Error message is displayed | PASS
Password Field | Leave Empty | Form does not submit | PASS
Password Field | Enter an Empty String | Form does not submit | PASS
Password Field | Enter an Empty String | Error message is displayed | PASS
Password Field | Passwords Not Matched | Form does not submit | PASS
Password Field | Passwords Not Matched | Error message is displayed | PASS
Log In Link | Click | Link on Sign Up page for users who already have an account. Navigates to Log In page | PASS
Sign Up Link | Click | An account is created after having correctly filled in the required fields | PASS
Sign Up Link | Click | Once an account is created, logs in the user | PASS
Sign Up Link | Click | Once the user is logged in, navigates to Home page | PASS
Alert | Submit | Success message is displayed confirming the user has logged in as [username] | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS

### Log In Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Username Field | Leave Empty | Form does not submit | PASS
Username Field | Leave Empty | Error message is displayed | PASS
Username Field | Enter an Empty String | Form does not submit | PASS
Username Field | Enter an Empty String | Error message is displayed | PASS
Password Field | Leave Empty | Form does not submit | PASS
Password Field | Leave Empty | Error message is displayed | PASS
Password Field | Enter an Empty String | Form does not submit | PASS
Password Field | Enter an Empty String | Error message is displayed | PASS
Login Fields | Incorrect Details | Form does not submit | PASS
Login Fields | Incorrect Details | Error message is displayed | PASS
Sign Up Link | Click | Navigates to Sign Up page | PASS
Log In Link | Click | Once the required fields are correctly filled in, the user is logged in and taken to the homepage | PASS
Alert | Submit | Success message is displayed confirming the user has logged in as [username] | PASS
Alert | Submit | Success message fades automatically after 3 seconds | PASS

### Logo Out Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Log Out Link | Click | Redirects the user to the logout page, asking if they're sure they want to log out | PASS
Log Out Link | Click | Once the user is logged out, navigates to Home page | PASS
Alert | Submit | Success message is displayed confirming that the user has logged out | PASS
Alert | Submit | Success message fades automatically after 3 seconds | PASS

### Home Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Plan Your Stay Message | Display | Start planning your trip message if user is logged in | PASS
Enjoy a Relaxing Stay Message | Display | Displayed if user is not logged in | PASS
Book Now Link | Click | Navigates to Log In page if user is not logged in | PASS
Book Now Link | Click | Navigates to Book A Room page if user is logged in | PASS

### About Page
#### This is a completely static page, barring the header and footer links, which have been previously discussed. 


### Menu Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Item Category Cards | Display | Items displayed in each category properly| PASS
Add A Menu Item (superuser) | Link | Redirects to Add A Menu Item form | PASS
Add A Menu Item (superuser) | Display | Add item name, description, choose food category from dropdown | PASS
Menu Item Categories Card Height | Display | Cards are displayed at the same height for each row regardless of the height of the card body content (when the height of a card is higher, the rest of the cards in the same row are stretched to the same height) | PASS  
Edit A Menu Item (superuser) | Link | Redirects to Edit A Menu Item form | PASS
Edit A Menu Item (superuser) | Link | Superuser can change item name, description, food category and save changes| PASS
Delete A Menu Item (superuser) | Link | Redirects to Delete A Menu Item form, asking if superuser is sure they want to delete | PASS
Delete A Menu Item (superuser) | Click | clicking 'delete' deletes the menu item from live site and from database | PASS
Alert | Delete Item | Success message fades automatically after 3 seconds | PASS

### Contact Us Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
First Name Field | Leave Empty | Form does not submit | PASS
First Name Field | Leave Empty | Error message is displayed | PASS
First Name Field | Enter an Empty String | Form does not submit | PASS
First Name Field | Enter an Empty String | Error message is displayed | PASS
Last Name Field | Leave Empty | Form does not submit | PASS
Last Name Field | Leave Empty | Error message is displayed | PASS
Last Name Field | Enter an Empty String | Form does not submit | PASS
Last Name Field | Enter an Empty String | Error message is displayed | PASS
Email Field | Leave Empty | Form does not submit | PASS
Email Field | Leave Empty | Error message is displayed | PASS
Email Field | Enter an Empty String | Form does not submit | PASS
Email Field | Enter an Empty String | Error message is displayed | PASS
Email Field | Enter Invalid Format | Form does not submit, error message shown | PASS
Message Field | Enter an Empty String | Form does not submit | PASS
Message Field | Leave Blank | Form does not submit | PASS
Alert | Submit | Success message is displayed confirming the message has been sent | PASS
Alert | Submit | Success message fades automatically after 3 seconds | PASS
Alert | Submit | Error message is displayed if fields are not filled out completely or properly | PASS
Alert | Submit | Error message fades automatically after 3 seconds | PASS


### 404 Error Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Custom 404 Error Page | Enter URL that does not exist | Custom 404 error message is displayed | PASS
Home Link | Click | Navigates to Home page with clickable button | PASS

## Bugs - START HERE
### Resolved Bugs

* **Homepage breaks**  

  ***Bug:***  
Homepage breaks over 991px, both in structure and font size. 

  ***Solution:***  
There was a transition in CSS that was erroenous and causing the 'layout breakage' at 991px. That portion of the CSS was removed.

  Font size was changed using media queries for the hero image and text layout. Both issues are solved now.


* **Contact Form 'uncaught reference error'**  

  ***Bug:***  
  Though the form submitted correctly and, to my knowledge, the overall functionality of the form was unaffected, there was an error in the console. After speaking with my mentor, Harry, I was advised that leaving this error would cause the project to fail.   

  ![Bug-ref error](/documentation/readme_images/BUG-uncaught-ref-error.png)
  ![Bug-ref error fixed](/documentation/readme_images/BUG-uncaught-ref-fixed.png)


    ***Solution:***  
    In lne 37 of my email.js file, I had the form resetting fields after submission. Removing this line of code (commented out in the screenshot above) solved the problem and did not affect the functionality of the contact form.  

* **Menu items not added**  

  ***Bug:***  
  Menu items were not being added to the database from the livesite.   


    ***Solution:***  
    After speaking to Ian_alumni on slack, he mentioned adding the 'Item' model to my admin site to make sure they appear on the page. This solved the problem as I was originally calling the wrong model. Speaking with colleagues on slack and on tutoring resolved the problem.

* **Never getting to the 'Are you sure' page**  

  ***Bug:***  
  Clicking the delete button does not take the user to the 'are you sure you want to delete' page.


    ***Solution:***  
    I had been calling the url ‘friendly name’ incorrectly. Once I understood that and changed the url pathway, the problem was fixed and everything worked as designed.


* **Able to book a room as another user**  

  ***Bug:***  
  A logged-in user can book a room under any other logged in user via the dropdown menu on the Book A Room page. 
  
    ***Solution:***  
    Oisin from tutoring alerted me to adding line 166 of code to my views.py file and changing line 31 to line 32 of my forms.py file. After making these changes, screen shots three and four below are not visible, rather the user cannot choose a User field when filling out this form. The User field is automatically filled in as the user they're logged in as.
    
    ![BUG](/documentation/readme_images/BUG-user-booking-form.png)
    ![BUG](/documentation/readme_images/BUG-user-code-added.png)
    ![BUG](/documentation/readme_images/BUG-user-field-dropdown.png)
    ![BUG](/documentation/readme_images/BUG-user-field-removed.png)


* **Wave validation not working on authenticated pages**  

  ***Bug:***  
  Any page put through the Wave validation tool would not show up if it was a page only an authenticated user could enter (CRUD menu functionality, all booking pages). 
  
    ***Solution:***  
    I downloaded the Chrome extension for Wave and used that for authenticated pages. This solved the problem and I was able to include all pages' Wave validation in the TESTING.md document.


### Unresolved Bugs

* **Double booking**   

  ***Bug:***  
Users can double book rooms.  

  ![BUG](/documentation/readme_images/BUG-double-booking.png)  

  ***Status:***  
I noticed this bug when I was running booking tests for CRUD functionality. I looked through some resources for creating an availability form or having some way to check room availability based on DateTimeFields.

  This is an aspect that could be implemented in future versions of this project to make it more realistic and 'real world ready'.  


* **Midnight booking time by default**   

  ***Bug:***  
Check in and check out times are midnight by default.  

  ![BUG](/documentation/readme_images/BUG-booking-time.png)  

  ***Status:***  
Originally I had created an availability form that checked room availability based on check-in and check-out times. I was unable to get that form working correctly and opted to change my DateTimeField to a DateField so users could not choose a time, just a calendar date. 

  The default time still appears as midnight for both fields. Like the double booking bug mentioned above, this is something that would have to be rectified if and when this application is launched in a real world scenario. For the scope of this project, I left the default times as midnight.
  

To my knowledge, there are no other bugs.