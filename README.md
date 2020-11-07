Welcome to my project! Cooking is something I have always enjoyed, but I always found it hard to keep track of my recipes. This projects aims to serve as a database that users can
upload all of their favourite recipes.

You can find my live project hosted here; https://recipes-lashmore.herokuapp.com/. 

## Contents
- [User Experience](#user-experience) 
    - [Overall Project Goals](#overall-project-goals)
    - [Target Audience Goals](#target-audience-goals)
    - [User Stories](#user-stories)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
- [Design Choices](#design-choices) 
    - [Fonts](#fonts)
    - [Icons](#icons)
    - [Colours](#colours)
    - [Images](#images)
- [Planning](#planning)
- [Wireframes](#wireframes)
    - [Website Layout](#website-layout)
    - [Database Design](#database-design)
- [Features](#features)
    - [Features that have been developed](#features-that-have-been-developed)
    - [Features that will be implemented in the future](#features-that-will-be-implemented-in-the-future)
- [Technologies Used](#technologies-used)
- [Planning + Testing:](#planning-+-testing)
- [Bugs](#bugs) 
- [Deployment](#deployment)
	- [Deploying to Heroku](#deploying-to-heroku)
- [Credits](#credits)
- [Disclaimer](#disclaimer)

## User Experience: 

### Overall Project Goals:
The goal of this project is to serve as a database that users can go to and search tried and tested recipes. 

### Target Audience Goals:
- The ability to access the site both from web and mobile.
- To be able to browse different recipes.
- Add filters to the recipes to narrow the search, e.g. breakfast, lunch etc.
- Rate recipes that they try. 
- Build up a collection of favourite recipes.
- Log in and upload their own recipes.
- Ability to edit recipes they upload. 

### User Stories:

Edel says:
"I like cooking, but I always dread finding a good recipe for dinner! It always takes so long and I don't know what to choose!"

Catriona says:
"I'm always looking for somewhere to store my favourite recipes. Otherwise, I end up losing them and when I go to cook them again I can't remember which online recipe I used". 

Ellie says:
"Often I have to ask my family and friends for new recipes. I'd love somewhere I could go to search for certain recipes, that have been tried and tested so I can rely on them."

### User Requirements and Expectations:

#### Requirements:
- Experience a nice design that looks well.
- Find recipes of different categories easily.
- Access information in a clear and user-friendly way.
- Navigate the website quickly, with fast load times.

#### Expectations:
- Users should be able to rely on information security.
- Content is compatible with web and mobile devices.
- The website loads with acceptable speed.
- The users can navigate the different pages of the website.-

## Design Choices: 
As cooking should be a hobby, the website design was intended to be light, playful and enjoyable. 

### Fonts:
I chose to use the sans-serif Montserrat font for the website. Sans-serif was a good choice here for readability, and also it would be a less formal font which was suitable here for the 
playful website design.

### Icons:
I decided to use font awesome for the icons. In this project, icons were important for easy reading, as the content for the recipes had to be split. For example, an icon should indicate 
which part of the recipe shows ingredients and which part shows the method. FOnt awesome provide clear and well made icons perfect for this purpose.

### Colours:
The colour scheme chosen was bright which was intended to echo the fun side to cooking and sharing recipes. I went for a colour scheme that showed darker pastels, so they still had that 
bright and enjoyable look, but were a bit bolder than the average pastel to ensure readability.

- Primary: #ffafb0 This coral pink colour was chosen for the logo. 
- Secondary: #52057b This purple shade was perfect for other elements of the site, and compliments the pink well. It was used for headings to add a splash of colour.
- Additional: #686d76 This charcoal grey was perfect for the nav bar headings and body text, as it is slightly less harsh than black but still very readable. 

### Images:
The images on the website were chosen specifically to encourage people to get cooking, and are to be uploaded alongside recipes as the users add them. These show images of 
different delicious recipes, which should inspire the users to cook. 

## Wireframes: 
The wireframes have been built to show on different sized devices. These include desktop, mobile and tablet. 
* [Link to desktop wireframes here](static/wireframes/desktop-wireframes.png)
* [Link to tablet wireframes here](static/wireframes/tablet-wireframes.png)
* [Link to mobile wireframes here](static/wireframes/mobile-wireframes.png)
 
### Database Design:
The project was built around NoSQL features provided by MongoDB. I used these to prepare the following collections.

### Data Storage Types:
The types of data that are stored in the MongoDB database.
- ObjectID
- String
- Boolean
- Object
- Array
- Binary

Recipes  Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Recipe ID|_id|ObjectID
Recipe Name|name|String
Recipe Author|author|String
Category|category_name|String
Health Rating|health_rating|String
Serves|serves|Integer
Date Baked|date_baked|String
Notes|notes|String
Ingredients|ingredients|Array
Method|method|Array
Created by|created_by|String
Photo URL|photo_url|String

Users Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
User ID|_id|ObjectID
Username|username|String
Password|password|Binary

Health Rating Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Health ID|_id|ObjectID
Health Rating|health_rating|String

Categories Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Category ID|_id|ObjectID
Category name|category_name|String

## Features: 

* Users can create an account and log in 
* Users can add recipes to the database
* Users can edit the recipes they have added to the database
* Users can delete the recipes they have added to the database
* Users can upload a photo alongside their recipe


### Features that have been developed:
* When a user adds a recipe, it pushes the details from the add recipe form into Mongo. This means that the recipe is then within Mongo. Recipes are then pulled from 
mongo on the main page, which allows all of the uplaoded recipes to be shown there. 
* When a user has uploaded a recipe, they  have the ability to edit them too. When they click the edit button, they are brought to a form that has the current values 
for that recipe prepopulated (except for the image, see below for more on this). The user can then edit what they like here. 
* In order to input the ingredients and method, the user must add a "/" in between each ingredient and step in the method. This is for formatting purposes. It was 
considered to use JavaScript here for dynamic form fields, where the user could add an extra input for each ingredient and step in the method. Although this would have 
looked quite nice, the main issue with the functionality is that it would take much longer for the user to upload the recipe as they would have to copy and paste or add 
each ingredient and step individually. 
* In order to remove a recipe, the user can just select remove on the recipe card or page which will remove the recipe from Mongo, and thus remove it from the database 
and the website.
* On the main home page for the recipes, the user can see a list of all recipes uploaded by themselves and also other users. 


### Features that will be developed in the future:
* The first thing on the list for future builds will be pagination. This will allow better organisation of the recipes that are added to the database and also it will allow 
filtering based on user who uploaded the recipe, category and create date. 
* While users can edit their recipes, they can't edit the photo they added to that recipe. This is because the file upload was much harder to pull through into the edit 
form option. I would like to add this option to edit the photo going forward.
* At the moment the user can create an account, but they don't have the ability to edit their password or change it if they have forgotten it. This would be good to add in 
future so that the users can have better access to their accounts in the event of forgotten passwords. 


## Technologies Used: 
#### Languages:
* <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a>
* <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS</a>
* <a href="https://www.w3schools.com/js/">JavaScript</a>
* <a href="https://www.json.org/json-en.html">JSON</a>
* <a href="https://www.python.org/">Python</a>

#### Tools & Libraries: 

* <a href="https://jquery.com/">jQuery</a>
* <a href="https://git-scm.com/">Git</a>
* <a href="https://getbootstrap.com/">Bootstrap</a>
* <a href="https://fontawesome.com/icons?d=gallery">Font-Awesome</a>
* <a href="https://tinypng.com/">TinyPng (image compression)</a>
* <a href="https://www.mongodb.com/cloud/atlas">MongoDB Atlas</a>
* <a href="https://pymongo.readthedocs.io/en/stable/">PyMongo</a>
* <a href="https://flask.palletsprojects.com/en/1.0.x/">Flask</a>
* <a href="https://jinja.palletsprojects.com/en/2.10.x/">Jinja</a>

## Planning:  + Testing:

#### Planning: 

There was a significant amount of time that went into planning this project, especially as I hadn't used the a lot of the technologies before. This involved researching 
the different technologies I would be using quite extensively. I also planned out my wireframes and had an idea of how I was going to build the project visually, while also
trying to identify how I would manage each of the CRUD elements from a technical point of view. 

## Bugs

Problem: The form was throwing an error when trying to upload a photo. I hadn't used a form to upload a file before, so hadn't come across this. 
Solution: After some troubleshooting, I noticed that I had missed adding the enctype to the form, so added in "enctype="multipart/form-data"", which solved this issue. 

Problem: When users go to add ingredients and methods to their recipes, the idea is that these will then display in list form on the recipe page. However, this proved to be 
an issue as when the form was first built all of the ingredients and method steps came through in one string. I realized that I needed to display these as arrays in MongoDB, 
and also to try and figure out a way to pull the values from the arrays and display them on the recipe page.
Solution: After investigating, I thought the best way to do this would be to use the split method and split the ingredients and method at the comma. This means the user has to 
insert the ingredients and method with a comma in between each ingredient. I did consider using dynamic form fields for each ingredient and step which I could have implemented 
with JavaScript, but I thought this would mean the user would have to paste individually each value rather than being able to paste directly from their favourite recipe site. I 
thought this would be a better solution, and if the user misses a comma they can always edit this using the edit recipe function. 

Problem: When editing a recipe, the current values for each of the form fields should populate into the form automatically. This was an issue for the ingredients and method section, 
because the value for those would be the full array including the opening and closing brackets - "[]". This meant that when the user resubmitted the form to update the recipe, the 
brackets were then added again into the array. 
Solution: It was necessary to add the contents of the ingredients and method arrays, into one string separated by commas. I achieved this by building a variable in the app route 
and using the python join() method. The new variable was then referenced in the template. 

## Deployment

### Deploying to Heroku

In order to deploy to Heroku I took the following steps; 
* Created a requirements.txt file to show Heroku the dependcies in my project, this was achieved by typing the following into the terminal "pip3 freeze --local > requirements.txt"
* The next step is creating a Procfile in my application, which I achieved my typing "echo web: python app.py > Procfile" into the terminal
* After committing these changes to Github, I went onto the Heroku website and created an account
* I created a new app in Heroku 
* Within the deploy tab of this app, I decided to choose GitHub to deploy
* This made things easier as each time I pushed any new content to GitHub it automatically pushed to Heroku too
* I connected to the relevant repository in Github
* Within the Heroku settings I went to Config Vars and added different variables used in my repository, including those needed for Cloudinary

** IP = 0.0.0.0
** MONGO_DBNAME = [Name of MongoDB] <br>
** MONGO_URI = mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
** PORT = 5000
** SECRET_KEY = [Secret key]
** API_KEY = [API key]
** API_SECRET = [API secret]
** CLOUD_NAME = [Cloud name]

* Finally, I selected Deploy Branch within Heroku, using the master branch 
* The project was successfully deployed to Heroku 


#### Testing: 

This involved testing the different forms and then comparing the data that ended up in the database. Especially with adding recipes, it was tricky to format them in the way I wanted. This was 
especially relevant for the ingredients and method section, as these were arrays which the users would have to add and then they would need to be formatted to appear in 
a list. 

Testing was also carried out in different browsers and screen sizes to ensure that the code would support the popular browsers and also all different screen sizes. 

#### Credits: 

Used this tutorial here to get the date picker in the form up and running - https://formden.com/blog/date-picker. 

#### Disclaimer

This website was built for education purposes.
