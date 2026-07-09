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
- The home page displays text and images which render properly
- The page is formatting according to CSS styling preferences
- The link to restaurant page is clickable and sends user to correct page
- The link to consumer page is clickable and sends user to correct page

## Page 2: Restaurant - Add Food

### Page Description
This page is where restaurants can log the food that they have available to sell. They categorize their food by type and subtype, then add its name and description. Additionally, the price and quantity available for each food item can be added. The restaurant also inputs its restaurant name at the top of the form.

#### For mockup, see [Improve Food Web Design PDF: Restaurant - Add Food](Improve Food Web Design.pdf)

### Parameters needed for the page
This page needs parameters such as HTML attributes, including the <a></a> tag to include a hyperlink that users can select to be guided to the Restaurant Location, Delivery/Pickup Options page, as well the <src ... alt=""> tag to include an image of more food on the page.

There will need to be an HTML form for the user to input information regarding food type, subtype, name, description, quantity, and price as well as the restaurant name.

### Data needed to render the page
An HTML document will be needed in order to include the text and images, a CSS document will be needed to style the page, and an HTML form will be needed in order to allow for user input to be available and recorded.

### Link destinations for the page

#### Restaurant - Add Food Page
*restaurant_add_food.html*

#### Restaurant - Add Food HTML Form
*restaurant_add_food_form.html*

#### Restaurant - Add Location, Pickup/Delivery Options Page
*<a href="restaurant_add_location.html"Restaurant - Add Location Page</ a>*

### List of tests for verifying the rendering of the page
- All expected text and images appear on the page and render properly
- The page is styled as expected
- User can input restaurant name (string)
- Food category can be selected from set of options (drop-down menu)
- Food subcategory can be selected from set of options (drop-down menu)
- Food name can be input by user (string)
- Food description can be input by user (string)
- Food quantity can be input by user (integer)
- Price can be input by user (float with two decimal places)
- The form can be submitted
- The hyperlink to Restaurant Location, Delivery/Pickup Options page sends user to correct web page

## Page 3: Restaurant - Add Location, Pickup/Delivery Options
### Page Description
This page is where the restaurant can input its location, and select if it would like to offer a delivery option. Additionally, the restaurant reports when it closes that day to help coordinate orders during open hours.

#### For mockup, see Improve Food Web Design PDF

### Parameters needed for the page
This page needs parameters such as HTML attributes, including the <iframe></iframe> tag which displays a map on the page with an address that the user inputs, as well an HTML form for the user to input information regarding restaurant location and closing time.

### Data needed to render the page
An HTML document will be needed in order to include the text and map, a CSS document will be needed to style the page, and an HTML form will be needed in order to allow for user input to be available and recorded regarding location, delivery options, and closing time.

### Link destinations for the page
*restaurant_add_location.html*

### List of tests for verifying the rendering of the page
- User can input address of restaurant (string)
- User can select closing time that day (dropdown menu)
- Map with user input address renders properly
- User can select if they would like to offer delivery (dropdown menu)
- User can submit their input information
- All text and styling on the page renders as expected

## Page 4: Consumer - Choose Food

### Page Description
This page enables consumers to browse and select current food offerings. It will update available food based on restuarant input and display details including restaurant name, and food type, subtype, name, description, price, and quantity. Consumers can scroll through the current offerrings and select items to add to their cart. 

#### For mockup, see Improve Food Web Design PDF

### Parameters needed for the page

This page needs HTML attributes including <a href="..."> tag to include a hyperlink that allows user to navigate to the Cart/Checkout page. It can also include <img src="..." alt=""> tags for image displays of each food item. 

The list of items needs to update based on restaurant input so <div> or <li> elements for each food listing will need to be dynamically generated rather than hard-coded, and a <button> or clickable element for each item so the consumer can select it to add to their cart. 

### Data needed to render the page

An HTML document will be needed in order to include the text, images, and links, and a CSS document will be needed to style the page. Since the food offerings change based on restaurant input, this page will also need a connection to the food/product database (via Flask route/API) to pull current restaurant name, food type, subtype, name, description, price, and quantity for each item, and a small amount of JavaScript (or server-side templating) to render that data into the page and to record which items a consumer selects into their cart.

### Link destinations for the page

Clicking an item/select button -> adds item to cart (updates car data)

Cart icon/link -> Cart/Checkout page

### List of tests for verifying the rendering of the page

- Page loads and correctly displays all current food listings with restaurant name, food type, subtype, name, description, price and quantity

- Each image rengers correctly and includes appropriate alt text

- Food listings update correctly when a restaurant adds, edits or removes an item

- Selecting an item correctly adds it to the consumer's cart

- Page displays an appropriate empty state when no food is currently available

- Scrolling through the offerings works without layout or rendering errors 

## Page 5: Consumer - Pickup/Delivery

### Page Description

#### For mockup, see Improve Food Web Design PDF

### Parameters needed for the page
### Data needed to render the page
### Link destinations for the page
### List of tests for verifying the rendering of the page
