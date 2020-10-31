Welcome to my project! Cooking is something I have always enjoyed, but I always found it hard to keep track of my recipes. This projects aims to serve as a database that users can
upload all of their favourite recipes.

## Contents
- UX 👍
    - Project Goals
    - Target Audience Goals
    - User Stories
    - User Requirements and Expectations
- Design Choices 🎨
    - Fonts
    - Icons
    - Colours
    - Images
- Planning✏️
- Wireframes 🔧
    - Website Layout
    - Account Creation Flowchart
    - Database Design
- Features 🎡
    - Features that have been developed
    - Features that will be implemented in the future
- Technologies Used 👨‍💻
- Planning + Testing: ✏️ 🔌
- Bugs 🐞
- Deployment 🚀
	- Deploying to Heroku
    - Locally run this project
- Credits 💳
- Disclaimer

## User Experience: 👍

### Project Goals:
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

## Design Choices: 🎨
As cooking should be a hobby, the website design was intended to be light, playful and enjoyable. 

### Fonts:
I chose to use the sans-serif Roboto font for the website. Sans-serif was a good choice here for readability, and also it would be a less formal font which was suitable here for the 
playful website design.

### Icons:
I decided to use font awesome for the icons. In this project, icons were important for easy reading, as the content for the recipes had to be split. For example, an icon should indicate 
which part of the recipe shows ingredients and which part shows the method. FOnt awesome provide clear and well made icons perfect for this purpose.

### Colours:
The colour scheme chosen was bright which was intended to echo the fun side to cooking and sharing recipes. I went for a colour scheme that showed darker pastels, so they still had that 
bright and enjoyable look, but were a bit bolder than the average pastel to ensure readability. \

- Primary: #ffbcbc This coral pink colour was chosen for the nav bar. 
- Secondary: #99d8d0 This greenish blue shade was perfect for other elements of the site, and compliments the pink well. 
- Additional: b7efcd This sea green was used for any other contrasting elements, which also matches the above two colours. 

### Images:
The images on the website were chosen specifically to encourage people to get cooking. These show images of different delicious recipes, and people enjoying their time in the kitchen. 
Users are also encouraged to upload pictures of the recipes that they have tried. 

## Wireframes/Flowcharts: 🔧
The wireframes have been built to show on different sized devices.
 
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

Recipe  Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:

Category|category_name|String
Recipe Name|name|String
Recipe Author|author|String
Health Rating|health_rating|String
Serves|serves|Integer
create_date|2 October, 2020|String


Users Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
User ID|_id|ObjectID
Name|name|String
Password|password|Binary
Recipes|recipes|array
Favourites|favourites|array

## Features: 🎡

### Features that have been developed:

### Features that will be developed in the future:


## Technologies Used: 👨‍💻
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

## Planning:  + Testing: ✏️ 🔌

#### Planning: 
There was a significant amount of time that went into planning this project, especially as I hadn't used the a lot of the technologies before. 

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
Solution:


#### Testing: 

#### Credits: 

Used this tutorial here to get the date picker in the form up and running - https://formden.com/blog/date-picker. 