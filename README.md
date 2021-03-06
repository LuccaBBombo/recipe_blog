# YourCookBook
This is a web application where people can share their families recipes as well as those who want to find out new recipes to try at home. In our application, anyone can post their recipes and give a little description on how this recipe came to be known by them and why they love is so much!


## UX
In the application we developed we wish to make finding new and interesting recipes fun and exciting. We created a system where it is very easy for the user to search for recipes they want and also making it simple to add your own recipes for other people to enjoy. You can sort recipes based on various aspects making it easier to find recipes that are within your interest.
We wish to have a communtiy of food enthusiasts who can give each other ideas, advices on each other recipes and have a good time!

### User Stories
* As a user I wish to find new recipes in an easy and uncomplicated manner.
* As a user I wish to post a recipe so that other people can cook it.
* As a user, I want to find a recipes that are cooked with vegan ingredients only.
* As a user, I want to find a recipes that are vegetarian.
* As a user, I want to find a recipes that are gluten-free.
* As a user, I want to be able to filter the results so I can find recipes that interest me in a fast and easy manner.
* As a user, I want to be able to review other people recipes and give them different.

[Mockup](mockup/recipe_website.pdf)

## Features 
* Users can sort recipes based on certain aspects.
* Users can post their own recipes.
* Users can post reviews about the recipes they tried.
* User can contact the website developers through the Contact page to discuss doubts and changes that need to be made on the recipe they posted.

## Existing Features
* Feature 1 - Allows users to sort recipes based on certain aspects by clicking the "Sort by" collapsible making it easier to find recipes that interests them.
* Feature 2 - Users can post reviews on the recipes they want, by entering the wanted recipe page and filling out the review form and clicking on the "Submit" button.
* Feature 3 - Users can contact the developers if they have any doubts by filling out the contact form on the Contact page.
* Feature 4 - Users can post their own recipes to share with the website community.

## Future Features
* Users will be able to upload their own images of their recipe.
* Create a page where the best recipes will be made by the website team, displaying different techniques and equipments. Also give advice on how to prepare certain foods.

## Technologies Used

* [Python](https://www.python.org/)

* [JavaScript](https://www.javascript.com/)

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    * The project uses Flask framework for its speed and simplicity for creating webpages.
* [MongoDB](https://www.mongodb.com/)
    * The project uses MongoDB as the website database.
* [JQuery](https://jquery.com/)
    * The project uses JQuery to simplify DOM manipulation.

### Testing
* The HTML and CSS files were tested by using the W3C Mark Validator Service by direct input of the files on the validator.
* The Python file was tested by direct input at the (extendsclass.com) file validator.
* The JavaScript files were tested using JSLint by direct input of the files on the validator.
* To test the responsiveness of the website in phones, tablets, and desktops screens, I was used the Chrome Developer Tools, verifying how the site reacted in different screen sizes.
1. Contact form
    1. Go to the 'Home' page
    1. Try to submit the empty form and verify that an error message about the required fields appears.
    1. Try to submit the form with an invalid email address and verify that a relevant error message appears.
    1. Try to submit the form with an empty input field and verify that a relevant error message appears.
    1. Try to submit the form with all inputs valid and verify that the form reloads, meaning that the form was correctly sent.
2. Add your recipe form
    1. Go to the 'Add your own recipe' page
    1. Try to submit the empty form and verify that an error message about the required fields appears.
    1. Try to submit the form with an invalid email address and verify that a relevant error message appears.
    1. Try to submit the form with an empty input field and verify that a relevant error message appears.
    1. Try to submit the form with all inputs valid and verify that the form is sent and you are redirected to the 'Recipes' page. 
3. Add your recipe form
    1. Go to a recipe page
    1. Try to submit the empty form and verify that an error message about the required fields appears.
    1. Try to submit the form with an invalid email address and verify that a relevant error message appears.
    1. Try to submit the form with an empty input field and verify that a relevant error message appears.
    1. Try to submit the form with all inputs valid and verify that the form is sent and you are redirected to the 'Recipes' page. 

 ## Bugs
 * Had an issue showing the reviews on the recipe-page that are only relevant to that recipe. Fixed it by passing the recipe._id and matching it with the review_id so that it displayed correctly.
 * Had an issue with the filter function, it was not targeting the correct recipe.category_name, fixed it by moving the name and id of query to the select option instead of the child options displayed for selection.
 * Having an issue setting up the emailJS on the home page to send the contact form. Fixed it by targeting the form input by the name attribute and realting it with the template created in emailJS. 
### Deployment
* All the changes made to the code where added and committed with the correct commentaries.
* To test the responsiveness of the website in phones, tablets, and desktops screens, I was used the Chrome Developer Tools, verifying how the site reacted in different screen sizes.
* To locally run the code, verify that all the items listed inside the "requirements.txt" file have been installed, there are no inputs required for the code to be able to run properly.

### Credits
* Website was designed based on the lessons that I had in Code Institute.
* Example recipes added to live website were taken from 'allrecipes'
### Acknowledgement
Special thanks to all the team from Code Institute on helping me on this project, tutors, mentors and also the students on the Slack community.


