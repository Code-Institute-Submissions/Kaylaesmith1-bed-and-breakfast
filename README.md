# The Wine Garden BnB


The Wine Garden BnB is a Bed & Breakfast website that gives users and potential guests a glimpse of the tranquility of staying at a BnB located in a picturesque Midwest vineyard.


The site is targets users wanting to spend a few days away from home but not necessarily in a cookie-cutter hotel. Visitors to the site can learn about the history of the BnB, view the amenities it offers, and book a room. Users can also contact us with any questions or comments.


A link to the live site can be found here - [The Wine Garden BnB](https://wine-garden-bnb.herokuapp.com/)


![Responsive site design]("")


## Table of Contents


- [The Wine Garden BnB](#the-wine-garden-bnb)
 * [User Experience (UX)](#user-experience-ux)
   + [User Stories](#user-stories)
   + [Design](#design)
     - [Color Scheme](#color-scheme)
     - [Imagse](#images)
     - [Fonts](#fonts)
     - [Wireframes](#wireframes)
 * [Agile Methodology](#agile-methodology)
 * [Data Model](#data-model)
 * [Testing](#testing)
 * [Security Features and Defensive Design](#security-features-and-defensive-design)
   + [User Authentication](#user-authentication)
   + [Form Validation](#form-validation)
   + [Database Security](#database-security)
   + [Custom error pages:](#custom-error-pages-)
 * [Features](#features)
   + [Header](#header)
   + [Footer](#footer)
   + [Home Page](#home-page)
   + [User Account Pages](#user-account-pages)
   + [Browse Recipes](#browse-recipes)
   + [Recipe Detail Page](#recipe-detail-page)
   + [Add Recipe Form](#add-recipe-form)
   + [Update Recipe Form](#update-recipe-form)
   + [Delete Recipe](#delete-recipe)
   + [My Meal Plan](#my-meal-plan)
   + [My Recipes Page](#my-recipes-page)
   + [My Bookmarks Page](#my-bookmarks-page)
   + [Error Pages](#error-pages)
   + [Future Features](#future-features)
 * [Deployment - Heroku](#deployment---heroku)
 * [Forking this repository](#forking-this-repository)
 * [Cloning this repository](#cloning-this-repository)
 * [Languages](#languages)
 * [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
 * [Credits](#credits)
 * [Acknowledgments](#acknowledgments)


<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>
## User Experience (UX)


A visitor The Wine Garden BnB website would likely be an adult looking to spend time away but who would also want all the amenities of home. This website provides information about a family-run business that meets those needs.


### User Stories 


#### EPIC | Project Environment Setup
#### As the developer, I can create a new project so that I can develop the website.
- Create project (GitHub)
- Install Django
- Create env.py file with secure variables in .gitignore file
- Test and ensure project works locally


#### EPIC | Landing Page
- 


#### EPIC | Initial Deployment
- As a Site User, I can input my favourite recipes onto the app through an easy to use interface so that I can share them with other users.
- As a Site User, I can edit and delete recipes that I have created so that I can easily make changes without having to start over.
- As a Site User I can view my recipes so that I can see and manage all recipes I have created in the one location.
- As a Site User I can view my bookmarked recipes so I can find them easily in the one location.


#### EPIC | Website Aesthetics
- As a Site User, I can save other user's recipes to my bookmarks so that I can find them easily at a later date.
- As a Site User, I can comment on other people's recipes so I can give my feedback.
- As a Site User, I can edit and delete comments that I have created so that I can easily make changes if I have made a mistake.


#### EPIC | User Account
- 


#### EPIC | Site Administration & Booking
- As a Site Administrator, I can create, read, update and delete recipes, comments and meal plan items so that I can manage the app content.

#### EPIC | Testing & Documentation
- As a Site Administrator, I can create, read, update and delete recipes, comments and meal plan items so that I can manage the app content.

#### EPIC | Error Pages
- 


#### User stories not yet implemented -- ARE THERE ANY ??

The following user stories were not included within the scope of Portfolio Project 4. They are intended to be implemented in the future.

### Design -- DONE

The website design is set in simple, paragraph form, which is intended to make it easier for the reader to navigate. The navigation bar is clear on each page, as is the footer and the pages are labelled with a 'banner' format thus ensuring users know where they are at all times. 


The color scheme was chosen to reflect a 'red wine' color and incorporate rich, earthy tones to encompass the vineyard theme.


#### Color Scheme -- DONE
The color palette was created using the palette generator [Coolers](https://coolors.co/).


The background of all site pages is the lightest color, a shade of beige, alowing for a stark contrast with the burgundy color when used as an accent. Shades of the green are used to accent other pages or as background for text or as a hover color. The darker beige color was used mainly as a visual cue to the user when links or buttons were hovered over.


All combinations of the colors used illustrate a contrast between background and text to ensure maximum user accessibility.


![Color Palette](/documentation/readme_images/color-palette.png)


#### Imagery -- DONE
Two different static images are included on the site depicting a homestead in a vineyard. Other images are used as the banner backgrounds on the About, Contact Us and Menu pages.
 

#### Fonts -- DONE
The 'Quicksand' font is the main font used on the page, while 'Montserrat' in a bolder weight was used for the navbar and 'Kanit' for other accent areas. The 'Sans-serif' font is noted as a backup and will be used in the event that the main fonts aren't imported correctly to the site. These font style were chosen for their ease of legibility and general letter spacing and were imported from [Google Fonts](https://fonts.google.com/).

#### Wireframes

<details>

 <summary>Landing Page</summary>

![Landing Page](documentation/wire_frames/landing.png)
</details>

<details>

<summary>About</summary>

![About](documentation/wire_frames/about.png)
</details>


<details>

<summary>Contact Us</summary>

![Contact Us](documentation/wire_frames/contact-us.png)
</details>

<details>

<summary>XX My Bookings XX</summary>

![My Bookings](XX)
</details>

<details>

<summary>XX Menu XX</summary>

![Menu](documentation/wire_frames/menu.png)
</details>

<details>

<summary>Sign Up</summary>

![Account sign up](documentation/wire_frames/signup.png)
</details>

<details>

<summary>Login</summary>

![Account login](documentation/wire_frames/login.png)
</details>
<details>

<summary>Log out</summary>

![Account logout](documentation/wire_frames/logout.png)
</details>

## Agile Methodology -- DONE

The agile methodology was used throughout project development. EPICS, user stories and the steps of the process are shown on [GitHub projects](https://github.com/users/Kaylaesmith1/projects/2/views/1).

In total, there were 8 EPICs that encompassed all user stories, depending on subject matter. Each user story was created as an 'issue' that outlined the goal to implement and the acceptance criteria. Once these criteria were developed and met, the user story moved through the process to the 'done' column. When all user stories specfic to an EPIC were completed, the EPIC itself was moved to the 'done' column. 

Creating EPICs and user stories for this project facilitated a smooth working environment where both general and specific goals were visualized, more easily tackled and brought to fruition. 

## Data Model -- FINISH THIS W NEW MODELS
I used principles of Object-Oriented Programming throughout this project and Django’s Class-Based Generic Views. Django AllAuth was used for user authentication.

A custom Menu model was made to incorporate CRUD functionality for admin users. This allows logged in, admin users to add, edit or delete a menu item, both from the live site and from the Django admin page.

The Customer model displays a working contact form on the Contact Us page. [Email js](https://www.emailjs.com/) was also used to ensure queries are addressed. For the purpose of this project, the emails arrive in my personal inbox.


The diagram below details the database schema.

![Database Schema]() -- IS NECESSARY?

## Testing

Details of all testing done can be viewed in depth in the [TESTING.md](https://github.com/Kaylaesmith1/bed-and-breakfast/blob/main/TESTING.md) documentation.
## Security Features and Defensive Design - DO THIS

### User Authentication - DONE

- Django's LoginRequiredMixin is used to ensure that any requests to access secure pages by non-authenticated or, in some cases, non-admin users, are redirected to the login page. 


### Form Validation - DONE
All fields in the contact form are required. If a user attempts to submit the form without filling in all fields, a warning text will appear at the bottom of the form asking them to complete the fields. The form will not submit until all fields are filled in. Once this is done, a message will pop up that the form was submitted successfully.

### Database Security - DONE
The database url and secret key are stored in the env.py file to prevent unwanted connections to the database. The env.py file was created before the initial push to GitHub.

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site, barring the contact form.

### Custom error pages: DONE

Custom Error Pages were created to give the user more information on the error and to provide them with buttons to guide them back to the site.

- 404 Page Not Found - "Sorry! The page you're looking for doesn't exist. Click below to return to the homepage." Below, there is a clickable button that will take the user back to the home page.
- 500 Server Error - "Sorry! The Wine Garden BnB can't handle this request at the moment. Please return to the home page." Below this, there is a button that will take the user back to the home page.

## Features

### Header

![Header](/documentation/readme_images/header.png)

**Logo**
- A customized logo was created using the free logo generator, [Hatchful](https://www.shopify.com/tools/logo-maker), by Shopify.
- The logo is positioned at the top left of the navigation bar. The logo is linked to the home page so the user can easily navigate the site.

![Header](/documentation/readme_images/navbar-logo.png)

**Navigation Bar** DONE

- The navigation bar is present at the top of every page and includes all links to the other pages.
- The My Account navigation link is a drop down menu that includes the Sign up and Log in links. 

![Header](/documentation/readme_images/navbar-no-user.png)

- When a user is logged in, the title changes to the user's name with a profile icon and the dropdown menu includes the Book A Room, My Bookings and Logout page links.

![Header](/documentation/readme_images/navbar-authenticated-user.png)

- The navigation bar is fully responsive and collapses into a hamburger menu icon on smaller screen sizes. collapsing into a hamburger menu when the screen size becomes too small. When the hamburger is clicked, the menu options open on the left-hand side just under the page logo.

![Header](/documentation/readme_images/navbar-hamburger.png)

- Hovering over the links will change the color to a light green.

![Header](/documentation/readme_images/navbar-hover.png)


### Footer - DONE
- The footer section includes working links to GitHub, Twitter, Instagram and Facebook. Clicking each link will open a separate browser page to the login of that website, barring the GitHub icon, which opens to my personal GitHub page.

![Footer](/documentation/readme_images/footer.png)

- Hovering over the links will change the color to a light green, identical to the navbar. 

![Footer](/documentation/readme_images/footer-hover.png)

### Home Page

**Call to Action Section** DONE
- The landing page includes a call to action section which encourages the user to book a room at The Wine Garden BnB. If the user is logged in, the message above the 'Book Now' button is, "Start planning your stay at The Wine Garden BnB". 

![Landing Page - Call to Action](/documentation/readme_images/landing-hero-image-authenticated.png)
- If the user is not logged in, "Enjoy a relaxing stay and a glass of wine in the tranquility of a Midwest vineyard!" appears. Below, a 'Book Now' button is visible and will take the user to the login page where they can either log in or sign up to continue the booking process.

![Landing Page - Call to Action](/documentation/readme_images/landing-hero-image.png)



**Why a BnB Section**
- The "Why a bed and breakfast' section gives a brief overview of why users should choose a bed and breakfast over a 'cookie cutter' hotel experience. Under that, a few of the ammenities are listed in short paragraphs with three icons of the most important features The Wine Garden has to offer.

![Landing Page - Why a BnB](/documentation/readme_images/landing-why-bnb.png)


### User Account Pages

**Sign Up**

![Sign Up](/documentation/readme_images/sign-up.png)

**Log In**

![Log In](/documentation/readme_images/login.png)

**Log Out**

![Log Out](/documentation/readme_images/logout.png)

- Django allauth was installed and used to create the Sign up, Log In and Log Out functionality and pages. 

![Successful Log In](/documentation/readme_images/success-login.png)
![Successful Log Out](/documentation/readme_images/success-logout.png)

- Success messages inform the user if they have logged in and logged out successfully and are present on the site for 3 seconds before automatically disappearing.

### About Page
**Get To Know Us Section**

- In this section there is an image of a cottage in a vineyard on the left and a 'Get to Know Us' section on the right describing the BnB and some of the features a person would find upon visiting.

![About Page - Get to know us](/documentation/readme_images/about-know-us.png)

**Customer Reviews Section**
- This is a static section that shows four customer reviews of The Wine Garden BnB.

![About Page - Customer Reviews](/documentation/readme_images/about-customer-reviews.png)

### Menu Page
**Menu Section for non-authenticated and non-admin visitors**

- This page displays the breakfast banner and six categories of menu items. 
- Non logged in visitors and non-admin users will see a static page with items, they will not be able to add, edit, or delete items.

![Menu Page - non-admin users](/documentation/readme_images/bfast-menu1.png)
![Menu Page - non-admin users](/documentation/readme_images/bfast-menu2.png)

**Menu Section for admin users**

- The overall look of the page is the same. If a user is logged in as an Admin super user, they can add, edit and delete menu items.

![Menu Page - non-admin users](/documentation/readme_images/bfast-menu1-authenticated.png)
![Menu Page - non-admin users](/documentation/readme_images/bfast-menu2-authenticated.png)

- The 'Edit A Menu Item' appears with fields pre-filled in and the Admin user can change them and update the product card.

![Menu Page - non-admin users](/documentation/readme_images/bfast-edit-item.png)

- If the Admin user chooses to delete a menu item, they are asked if they're sure they want to delete that specific menu item. Once they click the 'Delete Item' button, the item is deleted permanently from the live site and the Django database.

![Menu Page - non-admin users](/documentation/readme_images/bfast-delete-item.png)


### Contact Us Page
The Contact Us page includes a Google Map of a winery in existence in Iowa. Given that The Wine Garden BnB is not a real place, a substitute, Summerset Winery, was used for the purpose of this project. 

![Contact Us Page - non-admin users](/documentation/readme_images/contact.png)

- The page includes a contact form on the left-hand side that was implemented with [Email JS](https://www.emailjs.com/) and a Google Map on the right side.

- Filling out the contact form will send a message to my personal in box. The user is alerted both after successfully filling out and submitting the form and if they need to fill in a field. All fields are obligatory. The success or error messages stay for three seconds and disappear automatically.

![Contact Us Page - non-admin users](/documentation/readme_images/contact-success.png)

![Contact Us Page - non-admin users](/documentation/readme_images/contact-error-fields.png)

**Meal Plan Modal** START HERE

![header](docs/readme_images/features/mealplan_modal.png)

- The meal plan modal includes a form which allows the user to select a day of the week.
- Once the user clicks the add to meal plan button, the recipe is added to the user's meal plan for the selected day.
- Only one recipe can be added per day so if a user already has a meal plan item for a particular day, adding another one will overwrite the existing one. 
- The user receives a success message notifiying them that the recipe has been successfully added to their meal plan.

**Recipe Details Section**

![header](docs/readme_images/features/recipe_details.png)

- The main body of the page consists of the recipe description, ingredients, and method. 

**Comments Section**

![header](docs/readme_images/features/comment.png)

![header](docs/readme_images/features/add_comment.png)

- The comments section lists all comments left by users for that particular recipe.
- Comments can only be left if a user is logged in. Any comments left by the user that is currently signed in can be updated or deleted using the buttons in the comment header. 
    
![header](docs/readme_images/features/edit_comment.png)

![header](docs/readme_images/features/delete_comment.png)

- The user receives a success message notifying them that the comment has been successfully added, updated or deleted.
- If a user tries to edit or delete a comment (by changing the url) without being signed in they are redirected to the log in page.
- If a user tries to edit/delete another user's comment (by changing the url) they receive a custom 403 error.

### Add Recipe Form

![header](docs/readme_images/features/add_recipe.png)

- If the user is logged in, then they can add a recipe by clicking the link on the navigation bar.
- The form fields for 'Ingredients' and 'Method' include a WYSIWYG editor called Summernote to help the user format their content by adding bullet points, headings etc.
- The user can upload a photo if they wish. If they choose not to, a default image displays as their recipe image.
- The user can choose to publish the recipe now or save for later through a drop down menu. If they choose to 'save for later', the recipe will not appear on the Browse Recipe page but the user will be able to access it in their 'My Recipes' page and it will be labelled as 'DRAFT'.
- Failing to fill out the recipe's Title, Description, Ingredients, or Method, results in the form failing and rendering a message stating which fields you have missed.
- If a user tries to add a recipe (by changing the url) without being signed in they are redirected to the log in page.
- The user will receive a success message notifying them that the recipe has been successfully added.

### Update Recipe Form

![header](docs/readme_images/features/update_recipe.png)

- If the user is logged in and is the author or the recipe they can choose to edit the recipe by clicking the edit button on the recipe detail page. 
- The form opens with all fields populated with the original content.
- If a user tries to update a recipe (by changing the url) without being signed in they are redirected to the log in page.
- If a user tries to update another user's recipe (by changing the url) they receive a custom 403 error.
- The user will receive a success message notifying them that the recipe has been successfully updated.

### Delete Recipe

 ![header](docs/readme_images/features/delete_recipe.png)

- If the user is logged in and is the author or the recipe they can choose to delete the recipe by clicking the delete button on the recipe detail page.  
- The user is asked to confirm if they wish to delete the recipe or cancel.
- The user will receive a success message notifying them that the recipe has been successfully deleted.

### My Meal Plan

![header](docs/readme_images/features/mealplan_page.png)

- This page displays the logged in user's meal plan for the week.
- The meal plan cards are ordered Monday to Sunday. 
- If a user has added a recipe to their meal plan for a particular day, the card will display the recipe image and title. Clicking anywhere inside the meal plan card will take you directly to that recipe's detailed page.
- If there is no meal plan for a particular day, that card will display a plus icon and the text "Add Recipe". Clicking anywhere inside the meal plan card will take you to the browse recipes page.
- If a user tries to access this page (by changing the url) without being signed in they are redirected to the log in page.

### My Recipes Page

![header](docs/readme_images/features/myrecipes_page.png)

- This page displays all recipes which the logged in user has created.
- The recipe cards are paginated after every 8 recipes. 
- Each card displays the recipe's image, Title and Cook Time. 
- If the recipe is not yet published the word 'DRAFT' will appear in red next to the recipe title.
- Clicking anywhere inside the recipes card will take you directly to that recipe's detailed page.
- If a user tries to access this page (by changing the url) without being signed in they are redirected to the log in page.

### My Bookmarks Page

![header](docs/readme_images/features/my_bookmarks.png)

- This page displays all recipes which the logged in user has added to their bookmarks.
- Clicking anywhere inside the recipes card will take you directly to that recipe's detailed page.
- If a user tries to access this page (by changing the url) without being signed in they are redirected to the log in page.

### Error Pages

Custom Error Pages were created to give the user more information on the error and to guide them back to the site.

![header](docs/readme_images/features/403_error.png)

- 400 Bad Request - The Easy Eater is unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - The Easy Eater is currently unable to handle this request

### Future Features
The following user stories were scoped out of the project due to time constraints and labelled as "Could Have" on the project board in Github. It is intended that these user stories will be implemented at a later date. 

- As a Site User, I can export the ingredients from the recipes on my meal plan to a shopping list and remove the ones that are not necessary so that I can have all my required ingredients for the week in one place.
- As a Site User, I can search and filter recipes so that I can find the one I want.
Searching and filtering

Other potential features include:
- Adding extra categories on the Meal Plan Item for breakfast, lunch, dinner and snacks so the user can plan out their meals for the full day rather than just for dinner.
- Adding vegan and vegetarian labels to the recipe so the user can filter by these options.

## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next select your region.
- Click on the Create App button.

### Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file:
- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add Cloudinary URL to env.py
- Add the cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

### Create files / directories
- Create requirements.txt file
- Create three directories in the main directory; media, storage and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi

### Update Heroku Config Vars
Add the following Config Vars in Heroku:
- SECRET_KEY value 
- CLOUDINARY_URL
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1

### Deploy
- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live and operational.
## Forking this repository
- Locate the repository at this link [The Easy Eater](https://github.com/AliOKeeffe/PP4_My_Meal_Planner).
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available. 
- A copy of the repository is now created.

## Cloning this repository
To clone this repository follow the below steps: 

1. Locate the repository at this link [The Easy Eater](https://github.com/AliOKeeffe/PP4_My_Meal_Planner). 
2. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the prefered cloning option, and then copy the link provided. 
3. Open **Terminal**.
4. In Terminal, change the current working directory to the desired location of the cloned directory.
5. Type **'git clone'**, and then paste the URL copied from GitHub earlier. 
6. Type **'Enter'** to create the local clone. 

## Languages

- Python
- HTML
- CSS
- Javascript

## Frameworks - Libraries - Programs Used
- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [PostgreSQL](https://www.postgresql.org/) was used as the database for this project.
- [Heroku](https://dashboard.heroku.com/login) - was used as the cloud based platform to deploy the site on.
- [Responsinator](http://www.responsinator.com/) - Used to verify responsiveness of website on different devices.
- [Balsamiq](https://balsamiq.com/) - Used to generate Wireframe images.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and performance.
- [Font Awesome](https://fontawesome.com/) - Used for icons in information bar.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [PEP8 Online](http://pep8online.com/) - used to validate all the Python code
- [Jshint](https://jshint.com/) - used to validate javascript
- [Coolors](https://coolors.co/) - Used to create colour palette.
- [Favicon](https://favicon.io/) - Used to create the favicon.
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database schema design
- [Grammerly](https://app.grammarly.com/) - used to proof read the README.md
- [Summernote](https://summernote.org/): A WYSIWYG editor to allow users to edit their posts
- [Techsini](https://techsini.com/multi-mockup/index.php) - Site mockup generator
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to manage Django Forms
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/): CSS Framework for developing responsiveness and styling
- [Hatchful](https://hatchful.shopify.com/): Used to generate custom logo
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables): Used to convert excel testing tables to markdown

## Credits

- [W3Schools](https://www.w3schools.com/)
- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 4.6 Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Stack Overflow](https://stackoverflow.com/)
- [Pexels](https://www.pexels.com/): All imagery on the site was sourced from Pexels.com
- [BBC Goodfood](https://www.bbcgoodfood.com/): All recipe content was sourced from BBC Goodfood.
- [Update View](https://pytutorial.com/django-updateview-example)
- [Pagination](https://docs.djangoproject.com/en/2.2/topics/pagination/#using-paginator-in-a-view)
- [AutoSlugField](https://django-extensions.readthedocs.io/en/latest/field_extensions.html)
- [Code Institute - Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/Django3blog)
- [Ian Meigh - Custom Validator function](eateasy/validators.py)

## Acknowledgments

Many thanks to my mentor Antonio for his support and advice. Thanks to 
The Code Institute slack community for their quick responses and very helpful feedback in particular Ian Meigh.