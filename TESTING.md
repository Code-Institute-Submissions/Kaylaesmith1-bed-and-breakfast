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
  
  ![HTML Validation - Menu page](/documentation/validation/validator-menu-page-superuser.png)
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
  <summary>About Page - XX</summary>
  
![Wave Validation](/documentation/validation/wave-.png)
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
Title | Display | "Add A Booking" is displayed in a card on the booking page | PASS
Title | Display | "Booking" is displayed in a banner as the title of the My Bookings page   | PASS
Title | Display | "Edit Your Booking" is displayed in a card on the Edit Bookings page | PASS
Title | Display | "Delete Your Booking" and 'are you sure' is displayed in a card on the Delete Booking page | PASS
Title | Display | "Sign Up" is displayed on a card with a form to fill out on the Sign Up page | PASS
Title | Display | "Log In" is displayed on a card on the Log In page | PASS
Title | Display | "Log Out" is displayed on the Log Out page on a card with a button asking the user if they're sure | PASS

### Navigation Bar - START HERE
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Menu | Display | Links displayed side by side in the navigation bar for screen sizes with a minimum width of 1200px | PASS
Position | Display | Navigation bar always stays at the top of the screen | PASS
Logo | Click | Navigates to Home page | PASS
Home Link | Click | Navigates to Home page | PASS
Browse Recipes Link | Click |Navigates to Browse Recipes page | PASS
Sign Up Link | Display | Only available if the user is not logged in | PASS
Sign Up Link | Click | Navigates to Sign Up page | PASS
Log In Link | Display | Only available if the user is not logged in | PASS
Log In Link | Click | Navigates to Log In page | PASS
Log Out Link | Display | Only available if the user is logged in | PASS
Log Out Link | Click | Navigates to Log Out page | PASS
My Favourites Link | Display | Only available if the user is logged in | PASS
My Favourites Link | Click| Navigates to My Favourites page | PASS
My Recipes Link | Display | Only available if the user is logged in | PASS
My Recipes Link | Click| Navigates to My Recipes page | PASS
Post a Recipe Link | Display | Only available if the user is logged in | PASS
Post a Recipe Link | Click| Navigates to Post a Recipe page to | PASS
All Links | Hover | Colour changes to green with hover effect | PASS
All Links | Display | Active page is shown in green | PASS

### Hamburger Menu
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Menu | Display | Hamburger menu displayed in the navigation bar for screen sizes less than 1200px in width | PASS
Animation | Click | Animation functions correctly - X is displayed while the menu is open | PASS
Menu Closure | Click | Hamburger menu closes when clicked outside the menu | PASS
Menu Closure | Click | Hamburger menu closes when clicked on X | PASS 
Logo | Click | Navigates to Home page | PASS
Home Link | Click | Navigates to Home page | PASS
Browse Recipes Link | Click | Navigates to Browse Recipes page | PASS
Sign Up Link | Display | Only available if the user is not logged in | PASS
Sign Up Link | Click | Navigates to Sign Up page | PASS
Log In Link | Display | Only available if the user is not logged in | PASS
Log In Link | Click | Navigates to Log In page | PASS
Log Out Link | Display | Only available if the user is logged in | PASS
Log Out Link | Click | Navigates to Log Out page | PASS
My Favourites Link | Display | Only available if the user is logged in | PASS
My Favourites Link | Click| Navigates to My Favourites page | PASS
My Recipes Link | Display | Only available if the user is logged in | PASS
My Recipes Link | Click| Navigates to My Recipes page | PASS
Post a Recipe Link | Display | Only available if the user is logged in | PASS
Post a Recipe Link | Click| Navigates to Post a Recipe page to | PASS
All Links | Hover | Colour changes to green with hover effect | PASS
All Links | Display | Active page is shown in green | PASS

### Footer
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Position | Display | Footer always stays at the bottom of the screen even when the content does not occupy the full view height | PASS
Facebook Link | Click | Opens Facebook in a new tab | PASS
Twitter Link | Click | Opens Twitter in a new tab | PASS
Instagram Link | Click | Opens Instagram in a new tab | PASS
GitHub Link | Click | Opens GitHub in a new tab | PASS
LinkedIn Link | Click | Opens LinkedIn in a new tab | PASS
All Links | Hover | Colour changes to green with hover effect | PASS

### Sign Up Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Username Field | Leave Empty | Form does not submit | PASS
Username Field | Leave Empty | Error message is displayed | PASS
Username Field | Enter an Empty String | Form does not submit | PASS
Username Field | Enter an Empty String | Error message is displayed | PASS
Username Field | Duplicate Username | Form does not submit | PASS
Username Field | Duplicate Username | Error message is displayed | PASS
Email Field | Leave Empty | Form submits without an email address as this is an optional field | PASS
Email Field | Enter Invalid Format | Form does not submit | PASS
Email Field | Enter Invalid Format | Error message is displayed | PASS
Email Field | Duplicate Email Address | Form does not submit | PASS
Email Field | Duplicate Email Address | Error message is displayed | PASS
Password Field | Leave Empty | Form does not submit | PASS
Password Field | Leave Empty | Error message is displayed | PASS
Password Field | Enter an Empty String | Form does not submit | PASS
Password Field | Enter an Empty String | Error message is displayed | PASS
Password Field | Passwords Not Matched | Form does not submit | PASS
Password Field | Passwords Not Matched | Error message is displayed | PASS
Log In Link | Click | Navigates to Log In page | PASS
Sign Up Link | Click | Once all the required fields are correctly filled in, creates an account | PASS
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
Log In Link | Click | Once the required fields are correctly filled in, logs in the user | PASS
Log In Link | Click | Once the user is logged in, navigates to Home page | PASS
Alert | Submit | Success message is displayed confirming the user has logged in as [username] | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS

### Logo Out Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Log Out Link | Click | Logs out the user | PASS
Log Out Link | Click | Once the user is logged out, navigates to Home page | PASS
Browse Recipes Link | Click | Navigates to Browse Recipes page | PASS
Alert | Submit | Success message is displayed confirming that the user has logged out | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS

### Home Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Sign Up Message | Display | Correct message is displayed if the user is not logged in | PASS
Sign Up Link | Display | Only available if the user is not logged in | PASS
Sign Up Link | Click | Navigates to Sign Up page | PASS
Post a Recipe Message | Display | Correct message is displayed if the user is logged in | PASS
Post a Recipe Link | Display | Only available if the user is logged in | PASS
Post a Recipe Link | Click| Navigates to Post a Recipe page | PASS

### Browse Recipes Page
#### Recipe Filters
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Filter Dropdown Menu | Display | Dropdown menu is displayed correctly for each filter | PASS
Filter Functionality | Click | Filters recipes based on the criteria selected | PASS
Filter Functionality | Click | Clears filters when no criteria are selected | PASS
Filter Functionality | Display | When there are no recipes to display, Browse Recipes button and the correct message are displayed | PASS
Browse Recipes Link | Click | Navigates back to Browse Recipes page without any filter criteria applied | PASS
Pagination | Display | When there are more than 12 recipes to display, the filtered list of recipes is paginated correctly and maintains the filter criteria when navigating through the pages (previous, next, first and last pages) | PASS
Pagination | Display | When there are fewer than 12 recipes to display, pagination is not displayed | PASS

#### Recipe Cards
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Recipe Card | Display | Recipes published are displayed in descending order based on creation dates| PASS
Recipe Card | Display | Draft recipes are not displayed | PASS
Recipe Card | Click | Stretched link is applied correctly and clicking anywhere on a card navigates to the correct Recipe Details page | PASS
Recipe Card | Hover | Box shadow is applied with hover effect | PASS
Recipe Card Height | Display | Recipe cards are displayed at the same height for each row regardless of the height of the card body content (when the height of a card is higher, the rest of the cards in the same row are stretched to the same height) | PASS  
Recipe Card Width | Display | Recipe cards are displayed in the same width for each column and column width is the same for all columns displayed | PASS
Recipe Image | Display | When a recipe image is uploaded, the image is displayed correctly from Cloudinary | PASS
Recipe Image | Display | When a recipe image is not uploaded, the placeholder image is displayed correctly from Cloudinary | PASS
Image Size | Display | Images are displayed in the same height and width regardless of the size or aspect ratio of the images uploaded | PASS
Recipe Title | Display | First letter is always capitalised regardless of whether the title entered is capitalised | PASS
Number of Likes | Display | The number of likes is displayed correctly with a grey love heart and the number indicating the number of likes | PASS
Recipe Description | Display | First letter is always capitalised regardless of whether the description entered is capitalised | PASS
Recipe Description | Display | Description is truncated to 70 characters for display on the recipe cards | PASS  
Pagination | Display | When there are more than 12 recipes to display, pagination is added and functions correctly | PASS
Pagination | Display | When there are fewer than 12 recipes to display, pagination is not displayed | PASS

### Recipe Details Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Recipe Image | Display | When a recipe image is uploaded, the image is displayed correctly from Cloudinary | PASS
Recipe Image | Display | When a recipe image is not uploaded, the placeholder image is displayed correctly from Cloudinary | PASS
Image Size | Display | For screen sizes with a minimum width of 992px, the image height is set to occupy the maximum height of the recipe summary container next to the image | PASS
Recipe Title | Display | First letter is always capitalised regardless of whether the title entered is capitalised | PASS
Edit/Delete Recipe Button | Display | Edit/Delete button is available if the user is logged in and is the author of the recipe | PASS
Edit Recipe Button | Click | Opens Update Recipe page with the original details populated from the database | PASS
Edit Recipe Cancel Button | Click | Navigates back to Recipe Detail page | PASS
Delete Recipe Button | Click | Displays the modal asking the user to confirm deletion | PASS
Like/Unlike Button | Display | Like/Unlike button is available if the user is logged in and the recipe is published | PASS
Like/Unlike Button | Display | Like/Unlike button is greyed out and not clickable if the user is not logged in or the recipe is not yet published | PASS
Like/Unlike Button | Click | Toggles between Like (a love heart & plus icon) and Unlike (a love heart icon) if the user is logged in and the recipe is published | PASS
Number of Likes | Display | The number of likes is displayed and increases or decreases correctly when the recipe is liked or unliked | PASS
Recipe Description | Display | First letter is always capitalised regardless of whether the description entered is capitalised | PASS
Ingredients | Display | Details are displayed correctly from the Summernote field in the default font and font size | PASS
Method | Display | Details are displayed correctly from the Summernote field in the default font and font size | PASS
Comments | Display | If there are no comments, the correct message is displayed | PASS
Comments | Display | Displays comments, authors and dates in ascending order if there are comments | PASS
Post Comment | Display | If the user is not logged in, the correct message is displayed | PASS
Post Comment | Display | If the recipe is not published, the correct message is displayed | PASS
Post Comment | Display | Comment form is only available if the user is logged in and the recipe is published | PASS
Post Comment | Display | First letter is always capitalised regardless of whether the comment entered is capitalised | PASS
Post Comment | Leave Empty | Form does not submit | PASS
Post Comment | Submit | Form submits and comment is added in ascending order based on posting dates | PASS
Alert | Submit | Success message is displayed confirming the comment has been added successfully | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS
Edit/Delete Comment Dropdown Menu | Display | Edit/Delete button is available if the user is logged in and is the author of the comment | PASS
Edit Comment Button | Click | Opens Update Comment page with the original details populated from the database | PASS
Delete Comment Button | Click | Displays the modal asking the user to confirm deletion | PASS

### My Favourites Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Defensive Measure | Not Logged-in and Try to Acess the Page by Changing URL | Navigates the user to Log In page | PASS
Recipe Card | Display | Recipes liked by the user are displayed in descending order based on creation dates | PASS
Recipe Card | Click | Stretched link is applied correctly and clicking anywhere on a card navigates to the correct Recipe Details page | PASS
Recipe Card | Hover | Box shadow is applied with hover effect | PASS
Recipe Card Height | Display | Recipe cards are displayed at the same height for each row regardless of the height of the card body (when the height of a card is higher, the rest of the cards in the same row are stretched to the same height) | PASS  
Recipe Card Width | Display | Recipe cards are displayed in the same width for each column and column width is the same for all columns displayed | PASS
Recipe Card | Display | When there are no recipes to display, Browse Recipes button and the correct message are displayed | PASS
Browse Recipes Link | Click | Navigates to Browse Recipes page | PASS
Recipe Image | Display | When a recipe image is uploaded, the image is displayed correctly from Cloudinary | PASS
Recipe Image | Display | When a recipe image is not uploaded, the placeholder image is displayed correctly from Cloudinary | PASS
Image Size | Display | Images are displayed in the same height and width regardless of the size or aspect ratio of the images uploaded | PASS
Recipe Title | Display | First letter is always capitalised regardless of whether the title entered is capitalised | PASS
Number of Likes | Display | The number of likes is displayed correctly with a grey love heart and the number indicating the number of likes | PASS
Recipe Description | Display | First letter is always capitalised regardless of whether the description entered is capitalised | PASS
Recipe Description | Display | Description is truncated to 70 characters for display on the recipe cards | PASS  
Pagination | Display | When there are more than 12 recipes to display, pagination is added and functions correctly | PASS
Pagination | Display | When there are fewer than 12 recipes to display, pagination is not displayed | PASS

### My Recipes Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Defensive Measure | Not Logged-in and Try to Acess the Page by Changing URL | Navigates the user to Log In page | PASS
Recipe Card | Display | Recipes posted by the user are displayed in descending order based on creation dates | PASS
Recipe Card | Click | Stretched link is applied correctly and clicking anywhere on a card navigates to the correct Recipe Details page | PASS
Recipe Card | Hover | Box shadow is applied with hover effect | PASS
Recipe Card Height | Display | Recipe cards are displayed at the same height for each row regardless of the height of the card body content (when the height of a card is higher, the rest of the cards in the same row are stretched to the same height) | PASS  
Recipe Card Width | Display | Recipe cards are displayed in the same width for each column and column width is the same for all columns displayed | PASS
Recipe Card | Display | [Draft] in red font is added to the recipe title if the recipe is not published | PASS
Recipe Card | Display | When there are no recipes to display, Post a Recipe button, Browse Recipes button and correct messages are displayed | PASS
Post a Recipe Link | Click | Navigates to Post Recipe page | PASS
Browse Recipes Link | Click | Navigates to Browse Recipes page | PASS
Recipe Image | Display | When a recipe image is uploaded, the image is displayed correctly from Cloudinary | PASS
Recipe Image | Display | When a recipe image is not uploaded, the placeholder image is displayed correctly from Cloudinary | PASS
Image Size | Display | Images are displayed in the same height and width regardless of the size or aspect ratio of the images uploaded | PASS
Recipe Title | Display | First letter is always capitalised regardless of whether the title entered is capitalised | PASS
Number of Likes | Display | The number of likes is displayed correctly with a grey love heart and the number indicating the number of likes | PASS
Recipe Description | Display | First letter is always capitalised regardless of whether the description entered is capitalised | PASS
Recipe Description | Display | Description is truncated to 70 characters for display on the recipe cards | PASS  
Pagination | Display | When there are more than 12 recipes to display, pagination is added and functions correctly | PASS
Pagination | Display | When there are fewer than 12 recipes to display, pagination is not displayed | PASS

### Post Recipe Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Defensive Measure | Not Logged-in and Try to Acess the Page by Changing URL | Navigates the user to Log In page | PASS
Title | Leave Empty | Form does not submit | PASS
Title | Leave Empty | Error message is displayed | PASS
Title | Enter an Empty String | Form does not submit | PASS
Title | Enter an Empty String | Error message is displayed | PASS
Description | Leave Empty | Form does not submit | PASS
Description | Leave Empty | Error message is displayed | PASS
Description | Enter an Empty String | Form does not submit | PASS
Description | Enter an Empty String | Error message is displayed | PASS
Meal Type | Leave Empty | Form does not submit | PASS
Meal Type | Leave Empty | Error message is displayed | PASS
Main Ingredient | Leave Empty | Form does not submit | PASS
Main Ingredient | Leave Empty | Error message is displayed | PASS
Diet Type | Not Selected | Form submits as this is not a required field | PASS
Difficulty | Leave Empty | Form does not submit | PASS
Difficulty | Leave Empty | Error message is displayed | PASS
Preparation Time | Leave Empty | Form does not submit | PASS
Preparation Time | Leave Empty | Error message is displayed | PASS
Preparation Time | Enter Anything Other Than a Positive Integer | Form does not submit | PASS
Preparation Time | Enter Anything Other Than a Positive Integer | Error message is displayed | PASS
Cooking Time | Leave Empty | Form does not submit | PASS
Cooking Time | Leave Empty | Error message is displayed | PASS
Cooking Time | Enter Anything Other Than a Positive Integer | Form does not submit | PASS
Cooking Time | Enter Anything Other Than a Positive Integer | Error message is displayed | PASS
Serves | Leave Empty | Form does not submit | PASS
Serves | Leave Empty | Error message is displayed | PASS
Serves | Enter Anything Other Than a Positive Integer | Form does not submit | PASS
Serves | Enter Anything Other Than a Positive Integer | Error message is displayed | PASS
Ingredients | Leave Empty | Form does not submit | PASS
Ingredients | Leave Empty | Error message is displayed | PASS
Ingredients | Enter an Empty String | Form does not submit | PASS
Ingredients | Enter an Empty String | Error message is displayed | PASS
Method | Leave Empty | Form does not submit | PASS
Method | Leave Empty | Error message is displayed | PASS
Method | Enter an Empty String | Form does not submit | PASS
Method | Enter an Empty String | Error message is displayed | PASS
Image | Not Uploaded | Form submits as this is not a required field | PASS
Image | Click to Upload | Opens a file explorer to choose an image from | PASS
Image | Click to Upload | Chosen image file is displayed in the 'Choose File' field | PASS
Status | Save as Draft | Once all the required fields are filled in correctly, saves the recipe | PASS
Status | Save as Draft | Once the recipe is saved as Draft, the recipe is displayed on My Recipe page | PASS
Status | Publish Now | Once all the required fields are filled in correctly, saves the recipe | PASS
Status | Publish Now  | Once the recipe is saved, the recipe is displayed on Browse Recipes page | PASS
Post Recipe | Submit | Displays the Recipe Details page which has been generated | PASS
Alert | Submit | Success message is displayed confirming [recipe title] has been added successfully | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS
Post Recipe Cancel Button | Click | Navigates back to Browse Recipes page | PASS

### Update Recipe Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Defensive Measure | Not Logged-in and Try to Access the Page by Changing URL | Navigates the user to Log In page | PASS
Defensive Measure | Logged-in and Try to Access Another User's Recipe by Changing URL | 403 error page is displayed | PASS
Update Recipe | Display | Update Recipe form contains the original details from the database | PASS
Title | Leave Empty | Form does not submit | PASS
Title | Leave Empty | Error message is displayed | PASS
Title | Enter an Empty String | Form does not submit | PASS
Title | Enter an Empty String | Error message is displayed | PASS
Description | Leave Empty | Form does not submit | PASS
Description | Leave Empty | Error message is displayed | PASS
Description | Enter an Empty String | Form does not submit | PASS
Description | Enter an Empty String | Error message is displayed | PASS
Meal Type | Leave Empty | Form does not submit | PASS
Meal Type | Leave Empty | Error message is displayed | PASS
Main Ingredient | Leave Empty | Form does not submit | PASS
Main Ingredient | Leave Empty | Error message is displayed | PASS
Diet Type | Not Selected | Form submits as this is not a required field | PASS
Difficulty | Leave Empty | Form does not submit | PASS
Difficulty | Leave Empty | Error message is displayed | PASS
Preparation Time | Leave Empty | Form does not submit | PASS
Preparation Time | Leave Empty | Error message is displayed | PASS
Preparation Time | Enter Anything Other Than a Positive Integer | Form does not submit | PASS
Preparation Time | Enter Anything Other Than a Positive Integer | Error message is displayed | PASS
Cooking Time | Leave Empty | Form does not submit | PASS
Cooking Time | Leave Empty | Error message is displayed | PASS
Cooking Time | Enter Anything Other Than a Positive Integer | Form does not submit | PASS
Cooking Time | Enter Anything Other Than a Positive Integer | Error message is displayed | PASS
Serves | Leave Empty | Form does not submit | PASS
Serves | Leave Empty | Error message is displayed | PASS
Serves | Enter Anything Other Than a Positive Integer | Form does not submit | PASS
Serves | Enter Anything Other Than a Positive Integer | Error message is displayed | PASS
Ingredients | Leave Empty | Form does not submit | PASS
Ingredients | Leave Empty | Error message is displayed | PASS
Ingredients | Enter an Empty String | Form does not submit | PASS
Ingredients | Enter an Empty String | Error message is displayed | PASS
Method | Leave Empty | Form does not submit | PASS
Method | Leave Empty | Error message is displayed | PASS
Method | Enter an Empty String | Form does not submit | PASS
Method | Enter an Empty String | Error message is displayed | PASS
Image | Not Uploaded | Form submits as this is not a required field | PASS
Image | Click to Upload | Opens a file explorer to choose an image from | PASS
Image | Click to Upload | Chosen image file is displayed in the 'Choose File' field | PASS
Status | Save as Draft | Once all the required fields are filled in correctly, saves the recipe | PASS
Status | Save as Draft | Once the recipe is saved as Draft, the recipe is displayed on My Recipe page | PASS
Status | Publish Now | Once all the required fields are filled in correctly, saves the recipe | PASS
Status | Publish Now  | Once the recipe is saved, the recipe is displayed on Browse Recipes page | PASS
Update Recipe | Submit | Displays the Recipe Details page which has been updated | PASS
Alert | Submit | Success message is displayed confirming the [recipe title] has been updated successfully | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS
Update Recipe Cancel Button | Navigates back to Recipe Detail page | PASS

### Delete Recipe Modal
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Delete Recipe | Submit | Once the user confirms deletion in the modal, the recipe is deleted | PASS
Alert | Submit | Success message is displayed confirming that the recipe has been deleted | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS
Delete Recipe Cancel Button | Click | Modal is closed | PASS
Modal Closure | Click Outside Menu | Modal is closed | PASS

### Update Comment Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Defensive Measure | Not Logged-in and Try to Access the Page by Changing URL | Navigates the user to Log In page | PASS
Defensive Measure | Logged-in and Try to Access Another User's Comment by Changing URL | 403 error page is displayed | PASS
Update Comment| Display | Update Comment form contains the original details from the database | PASS
Comment Field | Leave Empty | Form does not submit | PASS
Comment Field | Leave Empty | Error message is displayed | PASS
Update Comment | Click | Comment is updated | PASS
Alert | Submit | Success message is displayed confirming the comment has been updated successfully | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS
Update Comment Cancel Button | Click | Navigates back to Recipe Detail page | PASS

### Delete Comment Modal
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Delete Comment| Submit | Once the user confirms deletion in the modal, the comment is deleted | PASS
Alert | Submit | Success message is displayed confirming that the comment has been deleted | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS
Delete Comment Cancel Button | Click | Modal is closed | PASS
Modal Closure | Click Outside Menu | Modal is closed | PASS 

### 403 Error Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Custom 403 Error Page  | Change URL to Acess Another User's Recipe | Custom 403 error message is displayed | PASS
Custom 403 Error Page | Change URL to Acess Another User's Comment | Custom 403 error message is displayed | PASS
Home Link | Click | Navigates to Home page | PASS
Browse Recipes Link | Click | Navigates to Home page | PASS

### 404 Error Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Custom 404 Error Page | Enter URL that does not exist | Custom 404 error message is displayed | PASS
Home Link | Click | Navigates to Home page | PASS
Browse Recipes Link | Click | Navigates to Home page | PASS

## Bugs
### Resolved Bugs

* **Pagination for a Filtered List of Recipes**  

  ***Issue:***  
When [Django filters](https://django-filter.readthedocs.io/en/stable/) were added to Browse Recipes page, the standard [Django pagination](https://docs.djangoproject.com/en/3.2/topics/pagination/) no longer worked.
With the standard Django pagination, the filter criteria were no longer applied when navigating to another page and showed recipes that did not fall under the selected criteria.  

  ***Solution:***  
While searching for a solution, I learnt that this is a common issue with Django filters. 
Having reviewed many possible solutions to the issue, I decided to implement the solution found in [Django Filter and Pagination](https://www.youtube.com/watch?v=dkJ3uqkdCcY) tutorial.
This solution uses [QueryString Template Tags](https://simpleisbetterthancomplex.com/snippet/2016/08/22/dealing-with-querystring-parameters.html) and works with Django filters.
RecipeList view codes and pagination codes for Browse Recipes page were updated to incorporate this solution for the Django filters.  

  Please click on the image to watch the GIF as auto looping is turned off to minimise distraction.  
  *Note: These recipes were created with filter categories in their titles to demonstrate the functionality of the filters.  

  <img src="docs/images/testing/recipe-filter-pagination.gif">

* **Positioning of Remember Me Box**  

  ***Issue:***  
  The "Remember Me" box on Log In page was initially horizontally centralised with the rest of the contents.
  During the manual testing on iPhone 11, it was noted that the box was positioned to the left, although this was not the case in Chrome Dev Tools.
  It appeared the issue resulted from how Apple Safari rendered the codes.   

    <img src="docs/images/testing/remember-me-box-before-fix.jpeg" width=300>  

    ***Solution:***  
    CSS codes were added to target the "Remember Me" box and moved to the right of the "Remember Me" text.
    The text and the box are now centralised together. 
    I felt that this was a more appropriate position for the box.  

    <img src="docs/images/testing/remember-me-box-after-fix.jpeg" width=300>
### Unresolved Bugs

* **Integrity Error for Slug Key Value Violation**   

  ***Issue:***  
During the manual testing, when a recipe titled "Bob" was submitted in the deployed site, server error 500 occurred.
The error in the development environment showed that it was caused by the duplicate key value as there was already a slug value "Bob" existing in the database and the slug key value must be unique.  

  <img src="docs/images/testing/server-error-500.png" width=700>  

  In the admin panel, it was verified that there was indeed a recipe titled "Bob" saved as a draft by a user. When the draft recipe was deleted from the database, the error no longer occurred.  

  ***Status:***  
Post Recipe form prevents a recipe entry with the same title as an existing recipe and raises an error.  

  <img src="docs/images/testing/no-server-error.png" width=500>   

    Attempts were made to recreate the error to investigate the issue further, however, I was never able to recreate the error. Since the error could not be recreated, this bug was not addressed.  

There are no other known bugs.