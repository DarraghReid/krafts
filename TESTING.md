# Testing

## Contents
* [Validation](#validation)
    * [W3C Markup Validator](#W3C-Markup-Validator)
    * [W3C CSS Validator Services](#W3C-CSS-Validator-Services)
    * [JSHint](#JSHint)
    * [Pep8 Online](#Pep8-Online)
    * [Lighthouse](#lighthouse)
* [Testing User Stories](#Testing-User-Stories)
* [Testing Features](#Testing-Features)
    * [Header](#Header)
    * [Home Page](#HOME-PAGE)
    * [Products Page](#PRODUCTS-PAGE)
    * [Product Detail Page](#PRODUCT-DETAIL-PAGE)
    * [Product Management Page](#PRODUCT-MANAGEMENT-PAGE)
    * [Profile Page](#PROFILE-PAGE)
    * [Checkout Page](#CHECKOUT-PAGE)
    * [Checkout Success Page](#CHECKOUT-SUCCESS-PAGE)
    * [Order History Page](#ORDER-HISTORY-PAGE)
    * [Sign In Page](#SIGN-IN-PAGE)
    * [Sign Up Page](#SIGN-UP-PAGE)
    * [Verify Account Page](#VERIFY-ACCOUNT-PAGE)
    * [404 page](#404-PAGE)
    * [500 page](#500-PAGE)
* [Site Responsiveness](#Site-Responsiveness)
* [User Testing](#User-Testing)
    * [Known Bugs and Issues Section](#known-bugs-and-issues)
    * [Remaining Bugs and Issues Section](#Remaining-Bugs-and-Issues)

## Validation

[W3C Markup Validator](https://validator.w3.org/), [W3C CSS Validator Services](https://jigsaw.w3.org/css-validator/),  [JSHint](https://jshint.com/) and [Pep8 Online](http://pep8online.com/) were used to validate this project's code and to make sure there were no syntax errors in the project.

[Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test the site's performance.

### W3C Markup Validator

The [W3C Markup Validator](https://validator.w3.org/) flagged multiple issues. Many of these issued turned out to stem from ie=edge being typed instead of IE=edge. However, more errors stemmed from how the code was designed to be responsive. 

Throughout the development of the site, includes were heavily depended upon to break up code that was meant from different screen sizes. The same elements were written in different files, but styled differently for different screen sizes. This resulted in duplicate ids appearing in the validator. It took a lot of work to find and rename these duplicate ids.

The other warnings that were repeatedly present were related to the "text/javascript" type attribute of the script element being unnecessary. These were also removed.

All HTML templates now pass through the validator without issue, and display the as the below image

![W3C Markup Validator](media/testing-imgs/homeval.png)

[^ Back To Top ^](#Contents)


### W3C CSS Validator Services

All CSS code from all CSS passed through the [W3C CSS Validator Services](https://jigsaw.w3.org/css-validator/) without issue.

![W3C CSS Validator Services](media/testing-imgs/css1.png)

[^ Back To Top ^](#Contents)


### JSHint

[JSHint](https://jshint.com/)
All Javascript code, including those within script tags in html file, passed through the JSHint validator without any major issues. Any issues flagged related to ES6 syntax, as can be seen in the above below.

![JSHint](media/testing-imgs/hint.png)

[^ Back To Top ^](#Contents)


### Pep8 Online

All Python code from .py files passed through [Pep8 Online](http://pep8online.com/) without issue, apart from 4 errors in settings.py relating to lines too long.
![Pep8 Online](media/testing-imgs/pep8.png)

[^ Back To Top ^](#Contents)


### Lighthouse
The main templates of this site were all tested for performance using [Lighthouse](https://developers.google.com/web/tools/lighthouse).
The results were as follows:

#### Home Page

![Home Page](media/testing-imgs/home-lh.png)

[^ Back To Top ^](#Contents)


#### Products Page

![Products Page](media/testing-imgs/products-lh.png)

[^ Back To Top ^](#Contents)


#### Profile Page

![Profile Page](media/testing-imgs/profile-lh.png)

[^ Back To Top ^](#Contents)


#### Product Management Page

![Product Management Page](media/testing-imgs/product-management-lh.png)

[^ Back To Top ^](#Contents)


#### Contact Page

![Contact Page](media/testing-imgs/contact-lh.png)

[^ Back To Top ^](#Contents)


#### Cart

![Cart](media/testing-imgs/cart-lh.png)

[^ Back To Top ^](#Contents)


#### Checkout Page

![Checkout Page](media/testing-imgs/checkout-lh.png)

[^ Back To Top ^](#Contents)


#### Checkout Success Page

![Checkout Success Page](media/testing-imgs/success-lh.png)

[^ Back To Top ^](#Contents)


#### Product Detail Page

![Product Detail Page](media/testing-imgs/detail-lh.png)

[^ Back To Top ^](#Contents)


#### Sign In Page

![Sign In Page](media/testing-imgs/signin-lh.png)

[^ Back To Top ^](#Contents)


#### Sign Up Page
![Sign Up Page](media/testing-imgs/signup-lh.png)

[^ Back To Top ^](#Contents)


## Testing User Stories
|**As a...**|**I want to...**|**So I can...**|**Image**|**RESULT**|
|:----|:----|:----|:----|:----|
|Potential customer|Immediately understand the purpose of the site|Decide if the site is for me| ![Intuitive Home Page](media/testing-imgs/intuitive.png)|The Home page is the landing page and acts as the introduction to the site. The hero carousel has specially selected images that represent handmade craftwork. The caption is further concrete confirmation of the site's purpose, informing the potential customer that the site aims to delivery handmade products to their door. Finally, both the header and category links are a clear indication of the type of products features on the site.|
||Easily browse products|Decide if I'm interested in them base on look, price, description and rating| ![Easily Browse Products](media/testing-imgs/browse.png)|Links to the products are accessible at all times from all pages in the site via the header. The Home page provides further visual-based links to product categories. The Products page has an additional side navigation on larger screens that provides visual indication of the type of products currently being displayed on the screen, as well as choices of other categories available to the customer. Active category links are displayed at the the top of the Products page on smaller screens. The product cards provide sufficient introductory information about the products, while the Product Detail page is easily accessible via the product cards.|
||Easily browse the site|Instinctively find what site services I am looking for|![Easily Browse Services](media/testing-imgs/services.png)|The Header is a multi-line element that conveys all services available to all users depending on their user status. It contains access links to all products of all categories, a search form, and links to all site pages not related to checkout.|
||Easily create an account|Purchase, rate, and comment on products|![Sign Up Link](media/testing-imgs/sign-up.png)![Sign Up Form](media/testing-imgs/sign-up2.png)|Sign Up and Login links are provided in the My Account tab which leads users to Sign Up or Login pages. Products can be added to the cart via both the Products page as well as the Product Details page. The ever present cart link leads directly to the Cart page from which users can go to a secure Checkout page from the click of a button. The Product Detail page contains a visual-based rating form, with ratings represented by prominent star emojis. Directly under the rating form is a simple and intuitive comment form, the purpose of which is immediately evident to the user.|
||Add items to my shopping cart prior to registration|Purchase products without committing to registering an account|![Add Products Unregistered](media/testing-imgs/unregistered.png)|Any user can add products to their cart and securely purchase products. The Order model's UserProfile ForeignKey is optional, and therefore allows users who are not registered to purchase products.|
||Easily access product detail|Learn more about the product before purchase|![Product Detail Access](media/testing-imgs/detail-access.png)![Product Detail](media/testing-imgs/detail.png)|The Product Detail page of each product is easily and intuitively accessible via the respective product's card in the Product's page. The Product Detail page contains all customer-related information about the product in a simple and intuitive visual display.|
||Search for products using key words|Find specific products|![Search Key Words](media/testing-imgs/search.png)|Due to the sticky Header, the search form is always accessible to the user. The search form takes key words and returns all products with matching keywords in both the title and description to the Products page.|
||Filter by price|Find products within my price range|![Filter By Price](media/testing-imgs/filter-price.png)|The Products page has a prominent filter selector box at the top of the products display. Using this filter selector box, users can filter products by price, from cheapest as well as from most expensive.|Filter by rating|See the popularity of the products|![Filter By Rating](media/testing-imgs/filter-rating.png)|Users may also use the filter selector box to filter products by name, category, and rating - including in reverse order.|
||Read product comments/see ratings|Make an informed purchase decision|![Access Product Ratings and Comments](media/testing-imgs/ratings-comments.png)|While commenting on products is only available to registered users, non registered users can easily access the comments section of the Product Detail page to see what other users are saying about a particular product. Each product's rating is visually represented by star emojis, both on the product's card element on the Products page, and on the product's Product Detail page. This image-led rating is designed to be maximally intuitive to the user. Equally, the rating form is also visually designed, with rating options represented by star emojis.|
|Registered user|Save my details|Checkout more easily for future purchases|![Save Detail](media/testing-imgs/save-info.png)|Users can access their Profile through the Account menu item in the Header. There, they will find a form immediately visible to them where they can add or update their details. This can also be done during checkout, by clicking the "Save this delivery information to my profile" checkbox. This ensures that their information is pre-populated for future checkouts|
||View my purchase history|Keep track of my purchases|![Purchase History](media/testing-imgs/order-history.png)|A brief summary of each user's purchase history is available in a table format on their Profile page. A more detailed document of each purchase/order can be access via the Order Number link of each order on that table.|
||Comment on products|Express my opinion or inquire about different products|![Make Comments](media/testing-imgs/make-comment.png)|All registered users have access to a comments form on each product's Product Detail page. Intuitively designed, users need only write the comment, with the rest of the information preefilled and hidden, before being submitted to the Comments model. Only admins have the privilege of replying to comments. This ensures that the comments section remains appropriate to the purpose of the site.|
||Rate products|Express my opinion on different products|![Rate Product](media/testing-imgs/rate-product.png)|As previously discussed, comments can be rated easily through the intuitive rating form on the Product Detail page. Opinions on products can also be expressed via the comments form directly under the rating form.|
||Contact the site owner|Express concerns and make inquiries|![Contact Site Owner](media/testing-imgs/contact.png)|A link to the Contact page is prominentely displayed in the Header, next to the other nav items. The contact page features a contact form from which users can send emails directly to the site owner. The address of the company, as well as a visual Google Maps iframe provides an additional means of communication, and confidence in the company.|
||View my cart prior to checkout|review my order|![View Cart First](media/testing-imgs/view-first.png)|The checkout page cannot be accessed directly. Users are first brought to the Shopping Cart where they can review their order, adjust the quantity of their items, and even remove items before proceeding to checkout.|
||Receive confirmation of purchases|Keep account of my purchases|![Confirmation of Purchase](media/testing-imgs/confirmation.png)|After each purchase, an email is sent an email confirming their order. Each customer can also access their order history in their Profile.|
||Easily know free delivery threshold|Know how much I need to spend to qualify for free delivery|![Free Delivery Threshold](media/testing-imgs/free-delivery.png)|Visual representation of the free delivery threshold is display is a progress bar in the Header. This progress bar gives visual and written feedback to the user about how much more they need to spend to qualify for free delivery.|
|Site owner|View, add, edit and delete all products|Rotate stock and keep stock up to date|![Admin CRUD](media/testing-imgs/crud.png)|The site owner can upload products to the database by navigating to the Product Manage page via the account link in the Header. There the site owner will find a form to add products to the site. The site owner can also edit and delete products as they please via "Edit" and "Delete" buttons that are visible exclusively to admin in the product cards as well as in the Product Detail page.|
||Have an easy user experience|Manage my site without need for advanced computer skills|![Intuitive Home Page](media/testing-imgs/intuitive.png)|The site is intuitively designed for both customers and admins, with all potential actions prominently visible to respective users.|
||Facilitate the needs of customers|Retain custom and engage with customers when needed||The ease of navigation is sure to provide a positive user experience to all customers. Customers are easily accommodated to explore, view and purchase products. They can also easily interact with products via rating and commenting, and can readily contact the site owner via the contact form.|

## Testing Features

[^ Back To Top ^](#Contents)

### HEADER
![Header Large](media/readme-imgs/header-lg.png)
![Header Medium](media/readme-imgs/header-md.png)
![Header Small](media/readme-imgs/header-sm.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|HEADER|Toggle all dropdown menu items|All dropdown items should toggle their respective menu items||PASS||
||Click all links to to navigate to their correct respective destinations|All links lead to their correct destinations||PASS||
||Add a product to the cart|1. The cart icon should change colour||PASS||
|||2. The cart total should update by the price of the item||PASS||
|||3. The success toast should pop down from cart icon displaying a success message and cart summary||PASS||
|||4. The progress bar and free delivery delta should update in proportion to the price of the item||PASS|The progress bar occasionally collapses. If this happens, hard reload the page and it should reappear|
||Enter a key word into the search bar|Products with the key word in their description and/or name should be displayed on the Products page||PASS||


[^ Back To Top ^](#Contents)

### HOME PAGE
![Home Page](media/testing-imgs/home.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|HOME PAGE|Observer the carousel|1. The carousel should auto slide||PASS||
|||2. The carousel can be controlled by clicking the navigation bars at the bottom||PASS||
|||3. The correct text and images are displayed||PASS||
||Click each image-based category link to navigate to their respective destinations|The category links should lead to their correct destinations||PASS||
||Scroll to the bottom of the page|The category links should have a parallax effect||PASS||
|FOOTER|Click all links in the footer to navigate to their respective destinations|All links lead to their correct destinations||PASS||


[^ Back To Top ^](#Contents)

### PRODUCTS PAGE
![Products Page](media/testing-imgs/products.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|PRODUCTS PAGE|Observe the page on larger screens|1. The product cards should be displayed in rows of 4||PASS||
|||2. The side nav should be visible and fixed||PASS||
|||3. The filter selector box should appear in the top right of the products container||PASS||
|||4. A link to the home page, followed by a search results count should appear on the top left of the products container||PASS||
||Toggle the filter selector box|The selector box should drop down the correct sorting options||PASS||
||Click each sorting option in the selector box|Appropriately filtered products in the correct order should be displayed in the products container||PASS||
||Click each category in the side nav|1. All subcategories of clicked category should be highlighted in the side nav||PASS||
|||2. All products in the clicked category should be displayed in the products container||PASS||
||Click each subcategory in the side nav|1. The subcategory should be highlighted in the side nav||PASS||
|||2. All products in the subcategory should appear in the products container||PASS||
||Observer the product cards|1. Each card should display an its own image/default image, name, price, category, and star rating||PASS||
|||2. Each card should contain an "Add To Cart" button||PASS||
|||3. Each card should contain "Edit" and "Delete" icons for admin users only||PASS||
||Click the "Add To Cart" button of any product.|The product should be added to the cart||PASS||
||Click the "Edit" icon of any product to navigate to the Edit Product Page.|The "Edit" icon should lead to the Edit Product page||PASS||
||Click the "Delete" icon of any product.|A modal requesting confirmation of deletion should appear||PASS||
||Click the "Delete" button of the modal.|The product should be deleted and a success confirmation toast should be displayed under the cart icon||PASS||
||Observe the page on medium screen|The product cards should be displayed in rows of 2 or 3.||PASS||
||Observe the page on small screen|1. The product cards should be stacked vertically.||PASS||
|||2. The filter selector box should appear at the top of the products container, with the search result count displayed directly beneath it||PASS||


[^ Back To Top ^](#Contents)

### PRODUCT DETAIL PAGE
![Product Detail Page](media/readme-imgs/detail1.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|PRODUCT DETAIL PAGE|Observe the Product Detail page of any particular product on medium and larger screens|1. The product image and product details & actions should appear inline in two columns||PASS||
|||2. The product details column should include the product's name, price, category, rating (represented by stars/"no rating" if the product has received any ratings), and description||PASS||
|||3. An input form to adjust the quantity of the product should appear directly under the product description||PASS||
|||4. "Add To Cart" and "Keep Shopping" buttons should appear directly under the quantity input form, stacked vertically||PASS||
|||3. "Edit This Product" and "Delete" this product should be displayed directly under the "Add To Cart" and "Keep Shopping" buttons only to admin users||PASS||
|||4. A rating form, with inputs represented by stars, will be displayed directly under the row containing the product image and product details & actions buttons||PASS||
|||5. The message "You have already rated this product" should appear in place of this form if the user has already rated this product"||PASS||
|||6. A message instructing the user to sign in in order to to rate the product should appear in place of this form, should the user not be logged in.||PASS||
|||7. A comment form with one input for users to write a comment, along "Cancel" and "Post" buttons beneath, should appear directly under the rating form.||PASS||
|||8. A message instructing the user to sign in in order to comment on the product appear in place of the comment form, should the user not be logged in||PASS||
|||9. A comments section displaying all comments made about the product should appear directly under the comment form||PASS||
|||10. Each comment should display the author's name, date and time of posting, as well as the comment itself||PASS||
|||11. "Edit" and "Delete" buttons should appear in the top right of the comment if the user is also the author of the comment||PASS||
|||12. A "Reply" button should appear at the bottom of the comment only to admin users.||PASS||
|||13. Replies by admin users are nested and indented beneath the comments they are in reply to.||PASS||
|||14. A message encouraging the user to be the first to comment on the product should appear in place of the comments section, should there not be any comments to display||PASS||
||Observe the Product Detail page of any particular product on smaller screens|The product image and product details & actions should appear stacked vertically||PASS||
||Change the product quantity to an invalid number by manually typing a specific quantity into the input box. Then attempt to add the product to the cart.|An error message should appear indicating the proper value range for the product.||PASS||
||Add the product to the cart|1. A success toast should appear indicating that the product has been successfully added to the cart, with the cart summary below including the product that has just been added||PASS||
||Rate the product by clicking of the stars in the rating form|1. The stars' opacity should change on hover||PASS||
|||2. The product should appear in the cart||PASS||
|||2. A success toast should appear informing the user they have successfully rated the product||PASS||
|||3. The product's rating should be updated by the amount the user has rated it by||PASS||
|||4. The product's average rating should be adjusted appropriatley||PASS||
|||5. The rating form should be replaced by a message indicating the user has already rated the product||PASS||
||Comment on the product|1. A success message informing the user that they have successfully commented on the product should appear in a success toast||PASS||
|||2. The comment should appear at the top of the comment form as it should be the most recent comment||PASS||
||Click the "Edit" button on the comment|An edit comment form should appear directly below the comment being edited.||PASS||
||Edit the comment|1. A success toast should appear indicated that the comment has been successfully edited||PASS||
||Edit the comment|The edited comment should appear at the top of the comments section||PASS||
||Click the "Delete" button of the comment to delete it.|1. A success toast should appear indicating the comment has been successfully deleted||PASS||
|||2. The comment should be removed from the comments section||PASS||
||Click the reply button of any comment|A reply form should appear directly beneath the comment being replied to||PASS||
||Reply to the comment|1. A success toast should appear indicating that the reply has successfully been posted||PASS||
|||2. The reply should be nested and indented beneath the comments that has been replied to||PASS||


[^ Back To Top ^](#Contents)

### CART
![Cart](media/testing-imgs/cart.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|CART|Observe the Shopping Cart Page on large and medium screens|The products should be displayed in a tables, with the cart total, delivery information, grand total, and Keep Shopping & Secure checkout buttons displayed beneath||Pass||
||Observe the table|The table should organise the products into 4 columns; Product Info for product image, name & sku, Price for product price, Quantity for a quantity input form displaying current product quantity and a means to adjust it, and Subtotal which displays the subtotal for a particular product ||PASS||
||Change the product quantity by clicking the increment and decrement buttons on the of the input form|1. The quantity should not go below one, or above 99.||PASS||
||Change the product quantity to an invalid number by manually typing a specific quantity into the input box and clicking "Update".|An error message should appear indicating the proper value range for the product.||FAIL|This control seems to have stopped working. See [Remaining Bugs and Issues Section](#Remaining-Bugs-and-Issues) for more details|
||Click the "Remove" button of any cart item|1. A success toast indicating that the item has been successfully removed should appear||PASS||
|||2. The item should be removed from the cart||PASS||
||Click the "Keep Shopping" and "Secure Checkout buttons to verify that they lead to their correct respective destinations|The "Keep Shopping" and "Secure Checkout" buttons should lead to their correct destinations||PASS||


[^ Back To Top ^](#Contents)

### PRODUCT MANAGEMENT PAGE
![Product Management Page](media/testing-imgs/p-management.png)
![Product Management Page](media/testing-imgs/management-edit.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|PRODUCT MANAGEMENT PAGE: Add|Observe the Product Management page for adding a product|The Add A Product form should be correctly formatted, with the correct fields displayed appropriately, required fields marked, any the the appropriate fields autofilled.||PASS||
||Add a product|1. A success toast should appear indicating that the product has been successfully added.||PASS||
|||2. The product's individual Product Detail page should be redirected to||PASS||
|Add a product with invalid details||1. The form should not submit||PASS||
|||2. A tooltip should appear instructing to fill in any required field that was left blank||PASS||
|||3. In the case of invalid information being input, an error toast should appear indicating that adding the product had failed, and instructing to check that the form is valid||PASS||
|PRODUCT MANAGEMENT PAGE: Edit|Observe the Product Management page for editing a product|1. The form should be autofilled with the details of the product being edited||PASS||
|||2. An information toast should appear indicating which product is being edited||PASS||
||Edit the product|1. The product's Product Detail page should be redirected to||PASS||
|||2. A success toast should appear indicating that the product has been successfully updated.||PASS||
|||3. The update made to the product should appear in the product's details.||PASS||


[^ Back To Top ^](#Contents)

### PROFILE PAGE
![Profile Page](media/testing-imgs/profile.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|PROFILE PAGE|Observe the Profile page of an empty profile.|1. The Default Delivery Information form should be correctly rendered and empty.||PASS||
|||2. The Order History table is empty ||PASS||
|||3. The Default Delivery form and Order History table are displayed inline on larger and medium screen, and stacked vertically on smaller screens. ||PASS||
||Make an order and check the "Save Delivery Information checkbox|The profile Default Delivery Information form should be pre-filled with the delivery details provided during checkout||PASS||
||Edit the Default Delivery form and submit|A success toast should appear indicating that the profile has been updated successfully||PASS||
||Observe the Profile page of a profile with saved information and an order history.|1. The Default Delivery Information form should be correctly rendered and pre-filled.||PASS||
|||2. The Order History table displayed past orders in the correct format.||PASS||


[^ Back To Top ^](#Contents)

### CHECKOUT PAGE
![Checkout Page](media/testing-imgs/checkout.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|CHECKOUT PAGE|Observe the checkout page with an empty profile|1. The checkout form should render empty||PASS||
|||2. The order summary should display the product image, name, quantity, subtotal, along with the order total, delivery cost (if any) and the grand total.||PASS||
|||3. The order summary and checkout form should be displayed inline on medium and large screen, and stacked vertically on smaller screens.||PASS||
||Submit a valid order|1. A success toast should appear indicating that the order has been successfully places, display the order number, and inform that a confirmation email has been sent to the email entered during checkout||PASS||
|||2. The page should redirect to the Checkout Success page||PASS||
|||3. A confirmation email should be sent to the email provided in the checkout form||PASS||
||Submit an invalid order|1. A tooltip should indicate if a field has been left black||PASS||
|||2. An incorrect card number should show up in red, with a message below the card number input indicating that the card details are invalid.||PASS||


[^ Back To Top ^](#Contents)

### CHECKOUT SUCCESS PAGE
![Checkout Success Page](media/testing-imgs/success.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|CHECKOUT SUCCESS PAGE|Observe the Checkout Success page|1. A thank you message followed by a message indicating that a confirmation email has been sent to the email provided during checkout||PASS||
|||2. An order summary containing all of the appropriate order details is displayed, followed by a "Back To Shop" button||PASS||
||Click the "Back To Shop" button to navigate to the Products page|The "Back To Shop" button should navigate to the Products page||PASS||


[^ Back To Top ^](#Contents)

### ORDER HISTORY PAGE
![Order History Page](media/testing-imgs/order-history2.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|ORDER HISTORY PAGE|Observe the Order History page|It should be a replica of the Checkout Success page of the particular order that was clicked||PASS||


[^ Back To Top ^](#Contents)

### SIGN IN PAGE
![Sign In Page](media/testing-imgs/signin.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|SIGN IN PAGE|Observe the Sign In page|1. The sign in form should be correctly rendered with all the correct fields displayed, including a "Remember Me" checkbox.||PASS||
|||2. "Sign In" and "Home" buttons should appear below the form||PASS||
|||3. A "Forgot password" link should appear below the "Sign In" and "Home" buttons||PASS||
|||4. A link to sign up should appear above the form||PASS||
||Click the sign up link to navigate to the Sign Up form|The link should navigate to the Sign Up form||PASS||
||Click the "Forgot password?" link|The link should navigate to the Password Reset form||PASS||
||Sign into an account|The page should redirect to the Home Page||PASS||
||Enter invalid information into the Sign In form|An error indicating that an incorrect username and/or password has been entered||PASS||


[^ Back To Top ^](#Contents)

### SIGN UP PAGE
![Sign Up Page](media/testing-imgs/signup.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|SIGN UP PAGE|Observe the Sign Up page|1. The sign up form should be correctly rendered with all the correct fields displayed.||PASS||
|||2. "Sign Up" and "Back To Login" buttons should appear below the form||PASS||
|||4. A link to Sign In should appear above the form||PASS||
||Click the Sign In link to navigate to the Sign In form|The link should navigate to the Sign In form||PASS||
||Click the "Back To Login" button|The button should navigate to the Sign In form||PASS||
||Register an account|The page should redirect to the Accounts page where it is indicated that an email from which the user can verify their account has been sent to the email provided during registration||PASS||
||Enter invalid information into the Sign Up form|An error indicating that an incorrect username and/or password has been entered||PASS||


[^ Back To Top ^](#Contents)

### VERYIFY ACCOUNT PAGE
![Verify Account Page](media/testing-imgs/verify.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|VERIFY ACCOUNT|Observe the accounts/confirm email page|A message instructing to press the confirm button to verify the email provided during registration should be visible||PASS||
||Click the "Confirm" button|1. The page should be redirected to the Sign In page||PASS||
|||2. A success toast should appear indicating that the email has been confirmed||PASS||


### 404 Page
![Verify Account Page](media/testing-imgs/404.png)
|**Feature**|**Test Description**|**Expected Results/s**||**PASS/FAIL**|**Comments**|
|:----|:----|:----|:----|:----|:----|
|404 Page|Enter an invalid url|1. The page should redirect to the 404 error page||PASS||
|||2. The 404 error page should consist of a single card element with detail of the error and a button offering a route back to the home page||PASS||
||Click the "Return Home" button|The page should redirect to the Home Page||PASS|500, 404 pages are identical to 500|
||Click the "Return Home" button|The page should redirect to the Home Page||PASS||

## Site Responsiveness

![Responsive](media/testing-imgs/responsive.png)

[Krafts](https://krafts-dreid.herokuapp.com/) was tested across a range of devices and internet browsers to assess the responsiveness of the site. The site was also tested on all available devices in Google Dev Tools to ensure it was visually appropriate on all screen sizes.

The site was tested on the following devices: 

* MacBook Pro (Retina, 13-inch, Early 2015)
* iPhone 8 Plus
* Samsung Galaxy S10
* Huawei LYO-L01
* Windows 10(desktop)
* iPad Air

And on the following browsers: 

* Google Chrome 
* Safari 
* Opera 
* Samsung Internet

## User Testing

The site was tested by various peers and family members throughout the building process. Known bug were confirmed and some new ones pointed out.

## Known Bugs and Issues
* Django auto sets a secret key in settings.py. When I made my first commit and push, this secret key was therefore exposed. To rectify this, I created an env.py file and set the secret key there as an environment variable, then accessed it from settings.py.

* Upon adding reply functionality to the comments model, bugs started to appear that would take a whole day to resolve. I had initially intended to use one view (product_detail) for all comment functionality. I modified the url to include the comment.id of the comment being replied to (the parent comment) so I could use it inside the view and submit it in the form. 

I changed the comments form to display all fields (instead of only the comment field) while I was working on implementing the functionality. I commented out the if statement that dealt with hiding the other fields. However, nothing changed -  the comment field was still the only one rendering. I figured I had made mistakes in the view and the url, so I changed them back to before I had added the reply functionality.

The problem remained. I ended up undoing all changes in all files that were related to the reply functionality. I compared my code from previous commits to the current code, and they were identical. Still, only the comment field would appear and the form would not submit. I was presented with the error “context referenced before assignment”. It seemed as though the context in my view wasn’t being read. However, the context (and the form and product inside it) would print to the terminal without issue. It would just not display on the template.

I deleted the whole comment model and rebuilt it, and built a separate view for adding comments (instead of using the product_detail view), but the problem was still present. The only thing that I hadn’t done was rewrite the if statement that rendered the fields in the comment form. Instead of commenting out the code that dealt with hiding certain fields, I deleted the code entirely. This commented out code was the source of the whole issue, it seems. Everything worked fine after that.

* The carousel on the Home page cause a lot of issues with responsiveness. Eventually, they had to be removed and replaced with background images with css.

* The side nav would not scroll when implemented. To counter this shortcoming, I made the navbar responsive so that all options in the navbar are visible on all screen sizes.


## Remaining Bugs and Issues
* The quantity input form in the Cart allows product quantities to be updated with negative values and values above 99 to be entered, if typed. If time allowed, this would most likely be a simple fix.

* When inspecting the site in Google Dev Tools, on larger displays, the header seems to be wider than the rest of the body. None of the fixes I tried to implement seemed to help. I does not happen on any laptop that the site has been tested on.

* The code to prevent the increment and decrement buttons from increasing or decreasing item quantities beyong specified values has ceased to work. This could be due to code refactoring done while correcting HTML validation errors. Time does not allow to revisit the issue.

* The progress bar can collapse at times. This is usually resolved by refreshing the page.

* The footer may appear to float on longer screens, although the issue seems to have resolved at the time of submission.

* An 90 minutes prior to submission of this project, the local version of the site and was still unresponsive at the time of submission. Both Tutor Support recommended submission, regardless due to the fact that the deployed site appears to be functioning at the time of submission.