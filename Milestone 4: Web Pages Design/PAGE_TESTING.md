# Page Testing

## Page 1: Landing Page

### Page Description
This is the home page for our website. It will provide a brief description of the services Improve Food provides, as well as two buttons the user can choose to click. One button is intended for consumers who would like to find and order food. The other button is for restaurants who would like to add food to be ordered by others.

#### For mockup, see [Improve Food Web Design PDF: Landing Page](<Improve Food Web Design.pdf>)

### Parameters needed for the page
This page needs parameters such as HTML attributes, including the `<a></a>` tag to include hyperlinks that users can select to be guided to the consumer or restaurant page, as well the `<src ... alt="">` tag to include an image of food on the home page.

### Data needed to render the page
An HTML document will be needed to include all of the test on the home page, as well as the hyperlinks and image. There should be a Cascading Style Sheet (CSS) which then styles the information text and hyperlinks, include font type and size, how text is centered, as well as the background color of the page.

### Link destinations for the page
The desintations of the pages will be found from the frontend component of the repository.

Restaurant button/link -> Restaurant Add Food page

Consumer button/link -> Consumer Choose Food page

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
- The page is formatted according to CSS styling preferences
- The link to restaurant page is clickable and sends user to correct page
- The link to consumer page is clickable and sends user to correct page

## Page 2: Restaurant - Add Food

### Page Description
This page is where restaurants can log the food that they have available to sell. They categorize their food by type and subtype, then add its name and description. Additionally, the price and quantity available for each food item can be added. The restaurant also inputs its restaurant name at the top of the form.

#### For mockup, see [Improve Food Web Design PDF: Restaurant - Add Food](<Improve Food Web Design.pdf>)

### Parameters needed for the page
This page needs parameters such as HTML attributes, including the `<a>``</a>` tag to include a hyperlink that users can select to be guided to the Restaurant Location, Delivery/Pickup Options page, as well the `<src ... alt="">` tag to include an image of more food on the page.

There will need to be an HTML form for the user to input information regarding food type, subtype, name, description, quantity, and price as well as the restaurant name.

### Data needed to render the page
An HTML document will be needed in order to include the text and images, a CSS document will be needed to style the page, and an HTML form will be needed in order to allow for user input to be available and recorded. Since the food quantities decrease as consumers purchase them, this page will also need a connection to the food/product database (via Flask route/API) in order to pull current restaurant name, food item, and quantity for each item. Additionally, a some JavaScript may be needed in order to render the data into the page and to record which items a consumer has purchased, to remove them from the database for future purchases that day.

### Link destinations for the page
Clicking a submit button -> adds food to database

Location button/link -> sends user to restaurant location page

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

#### For mockup, see [Improve Food Web Design PDF: Restaurant - Add Location, Pickup/Delivery Options](<Improve Food Web Design.pdf>)

### Parameters needed for the page
This page needs parameters such as HTML attributes, including the `<iframe></iframe>` tag which displays a map on the page with an address that the user inputs, as well an HTML form for the user to input information regarding restaurant location and closing time.

### Data needed to render the page
An HTML document will be needed in order to include the text and map, a CSS document will be needed to style the page, and an HTML form will be needed in order to allow for user input to be available and recorded regarding location, delivery options, and closing time. This page will need a connection to the food data (the restaurant's food item and quantity) carried over from the Add Food page, as well as a connection to the consumer database to pull each consumer's name and location who has ordered from a restaurant. A connection to a pickup/delivery time database or schedule (via Flask route/API) will be needed to populate the list of available time windows to deliver to consumers or for consumers to pick up their items. JavaScript will be needed to conditionally render either the pickup flow or the delivery flow based on the restaurant's delivery preference and the customer's selection, as well as to validate and store the restaurant address entered.

### Link destinations for the page
Submit button -> submits data regarding restaurant address, closing time, and delivery option

Add more food button (optional) -> restaurant can select to go back to the Add Food page for additional items

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

#### For mockup, see [Improve Food Web Design PDF: Consumer - Choose Food](<Improve Food Web Design.pdf>)

### Parameters needed for the page

This page needs HTML attributes including `<a href="...">` tag to include a hyperlink that allows user to navigate to the Cart/Checkout page. It can also include `<img src="..." alt="">` tags for image displays of each food item. 

The list of items needs to update based on restaurant input so `<div>` or `<li>` elements for each food listing will need to be dynamically generated rather than hard-coded, and a <button> or clickable element for each item so the consumer can select it to add to their cart. 

### Data needed to render the page

An HTML document will be needed in order to include the text, images, and links, and a CSS document will be needed to style the page. Since the food offerings change based on restaurant input, this page will also need a connection to the food/product database (via Flask route/API) to pull current restaurant name, food type, subtype, name, description, price, and quantity for each item, and a small amount of JavaScript (or server-side templating) to render that data into the page and to record which items a consumer selects into their cart.

### Link destinations for the page

Clicking an item/select button -> adds item to cart (updates cart data)

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
This page enables customers to checkout with their current order items and select pickup or delivery options. The page will display the order total and have a button for pickup or delivery. 

If pickup is selected, the customer will be directed to a confirmation page that confirms the order items, item total, restuarant name, and restaurant location. A list of pickup times will be displayed, allowing the customer to select their desired pickup window. 

If delivery is selected, the customer will be prompted to enter their address. A confirmation page will display with the order items, item total, restaurant name, and restaurant location. A list of possible delivery times will display and the customer will select their desired pickup window. 

#### For mockup, see [Improve Food Web Design PDF: Consumer - Pickup/Delivery](<Improve Food Web Design.pdf>)

### Parameters needed for the page
This page needs parameters such as HTML attributes, including `<button>` elements for the user to select either "Pickup" or "Delivery." A `<form>` will be needed to collect the customer's address if "Delivery" is selected, with `<input type="text">` fields for street address, city, state, and zip. A `<select>` (dropdown) or radio button group (`<input type="radio">`) will be needed to display and let the customer choose from the list of available pickup or delivery time windows. An `<a href="...">` tag or '`button>` will be needed to allow the customer to proceed from the time-selection screen to order confirmation, and `<a href="...">` tags will also be needed to link the restaurant name/location to that Restaurant's Location page.

### Data needed to render the page
An HTML document will be needed to include the text and layout for the checkout, address form, and confirmation screens, and a CSS document will be needed to style the page. This page will need a connection to the cart data (order items and item total) carried over from the Choose Food page, as well as a connection to the restaurant database to pull restaurant name and location. A connection to a pickup/delivery time database or schedule (via Flask route/API) will be needed to populate the list of available time windows. JavaScript or server-side logic (e.g. Flask/Jinja) will be needed to conditionally render either the pickup flow or the delivery flow based on the customer's button selection, and to validate and store the delivery address if entered.

### Link destinations for the page
Pickup button -> Pickup confirmation page

Delivery button -> Delivery address entry form

Address form submission -> Delivery confirmation page

Confirm time selection -> Order confirmation/Receipt page 

### List of tests for verifying the rendering of the page
- Page loads and correctly displays the current order items and item total

- "Pickup" and "Deliery" buttons render and are clickable

- Selecting "Pickup" correctly navigates to the pickup confirmation screen with order items, item total, restaurant name, and restuarant location

- Selecting "Delivery" correctly displays the address input form

- Address form validates required fields before proceeding

- Delivery confirmation screen correctly displays order items, item total, restaurant name, and restaurant location after address is submitted

- List of pickup times renders correctly and reflects actual avaliable windows

- List of delivery times renders correct and reflects actual available windows

- Customer selected time window is correctly recorded/passed to next step

- Page displays an appropriate error/empty state if no pickup or delivery times are currently available 
