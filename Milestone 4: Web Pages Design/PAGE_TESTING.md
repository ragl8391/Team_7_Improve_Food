# Page Testing

## Page 1: Landing Page

### Page Description
This is the home page for our website. It will provide a brief description of the services Improve Food provides, as well as two buttons the user can choose to click. One button is intended for consumers who would like to find and order food. The other button is for restaurants who would like to add food to be ordered by others.

#### For mockup, see Improve Food Web Design PDF: Landing Page

### Parameters needed for the page
This page needs parameters such as HTML attributes, including the <a></a> tag to include hyperlinks that users can select to be guided to the consumer or restaurant page, as well the <src ... alt=""> tag to include an image of food on the home page.

### Data needed to render the page
An HTML document will be needed to include all of the test on the home page, as well as the hyperlinks and image. There should be a Cascading Style Sheet (CSS) which then styles the information text and hyperlinks, include font type and size, how text is centered, as well as the background color of the page.

### Link destinations for the page
The desintations of the page can be found from the frontend component of the repository.

#### Landing Page HTML Document
*landing.html*

#### Website CSS Document
*improve_food_style.css*

#### Restaurant Page - Add Food
*<a href="restaurant_add_food.html"Restaurant - Add Food Page</ a>*

#### Consumer Page - Choose Food
*<a href="consumer_choose_food.html"Consumer - Choose Food Page</ a>*

### List of tests for verifying the rendering of the page
- Test that home page displays text and images
- Test that page is formatting according to CSS styling preferences
- Test that link to restaurant page is clickable and sends user to correct page
- Test that link to consumer page is clickable and sends user to correct page

## Page 2: Restaurant - Add Food

### Page Description
This page is where restaurants can log the food that they have available to sell. They categorize their food by type and subtype, then add its name and description. Additionally, the price and quantity available for each food item can be added. The restaurant also inputs its restaurant name at the top of the form.

#### For mockup, see Improve Food Web Design PDF: Restaurant - Add Food

### Parameters needed for the page
This page needs parameters such as HTML attributes, including the <a></a> tag to include a hyperlink that users can select to be guided to the Restaurant Location, Delivery/Pickup Options page, as well the <src ... alt=""> tag to include an image of more food on the page.

There will need to be an HTML form for the user to input information regarding food type, subtype, name, description, quantity, and price as well as the restaurant name.

### Data needed to render the page
An HTML document will be needed in order to include the text and images, a CSS document will be needed to style the page, and an HTML form will be needed in order to allow for user input to be available and recorded.

### Link destinations for the page

#### Restaurant - Add Food Page
*restaurant_add_food.html*

#### Restaurant - Add Foof HTML Form
*restaurant_add_food_form.html*

#### Restaurant - Add Location, Pickup/Delivery Options Page
*<a href="restaurant_add_location.html"Restaurant - Add Location Page</ a>*

### List of tests for verifying the rendering of the page
- Test that all expected text and images appear on the page
- Test that page is styled as expected
- Test that restaurant name can be input (string)
- Test that food category can be selected from set of options (drop-down menu)
- Test that food subcategory can be selected from set of options (drop-down menu)
- Test that food name can be added (string)
- Test that food description can be added (string)
- Test that food quantity can be added (integer)
- Test that price can be added (float with two decimal places)
- Test that form can be submitted
- Test that hyperlink to Restaurant Location, Delivery/Pickup Options page sends user to correct web page

## Page 3: Restaurant - Add Location, Pickup/Delivery Options
### Page Description

#### For mockup, see Improve Food Web Design PDF

### Parameters needed for the page
### Data needed to render the page
### Link destinations for the page
### List of tests for verifying the rendering of the page

## Page 4: Consumer - Choose Food

### Page Description

#### For mockup, see Improve Food Web Design PDF

### Parameters needed for the page
### Data needed to render the page
### Link destinations for the page
### List of tests for verifying the rendering of the page

## Page 5: Consumer - Pickup/Delivery

### Page Description

#### For mockup, see Improve Food Web Design PDF

### Parameters needed for the page
### Data needed to render the page
### Link destinations for the page
### List of tests for verifying the rendering of the page