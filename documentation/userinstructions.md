# User instructions
 <!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->
 - [Item](#item)
 - [List](#list)
 - [Category](#category)
 <!-- /TOC -->
## Frontpage
The frontpage of Shopping list looks something like this:
![frontpage](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/index.PNG)
Inside the red square in the top right is where you can create users and log in
## Account management
### Creating a user
You can create new user by clicking create new user from the previous picture. It will lead to a view where you'll see the form to create a new user. Fill the fields with your desired information and then press the button. If there was something wrong with one of the fields, the app will notify you.
![Createuser](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/create%20user.PNG)
If user creation was succesful, you will be directed to the login screen.
### Logging in
Fill the fields with your username and password and hit the button. As before, the app will inform you if there is a problem.
![Login](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/login.PNG)
## Navbar
At the top of the page you can see the navbar, by clicking links you can access new pages
![navbar](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/user_navbar.PNG)
## Items
### Add items
By clicking "Add items" you will access this form. The amount line can be left empty, but you should name your item. If you wish to add an already bought item you can do so by clicking the box at the bottom of the form. When you are ready, hit the button and you will be forwarded to a list of your items.
![add items](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/adding%20item.PNG)
### My items
Here you can see all your items and change whether or not they are bought, and even delete them. If you wish to do more, you can access that page by clicking the number under the # column. Make sure to click on the correct row!
![my items](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/my%20items.PNG)
### Edit item
In this view you can edit every attribute of an item, excluding it's name. Just change the value in the column you wish to edit, and hit the button next to it. This will update the value in the database, and redirect you back to this page so you can see the change. If you delete the item, you will be return to "my items".
![edit item](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/edit%20item.PNG)
## Categories
A list of categories can be accessed from the navbar by clicking "show categories". Unless there was a problem, there will always be at least one category in this list.
![categories](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/categories.PNG)
## Lists
## My lists
You can view all your lists from here. The first time you try creating an item, a default list will be created for you. This is to make sure that there will be as few errors as possible. If you click the name of a list, you will be taken to a list specific view.
![my lists](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/my%20lists.PNG)
### List page
In this page you can see more info about a list, and all the items it contains. As in "my items", if you click on the number in an item you will be taken to a page where you can edit this item.
![list page](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/list_page.PNG)
### Add list
From here you can add lists to your user, so you can assign items to these specific lists. Assigning items to list happens from "edit item" view.
![add list](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/add%20list.PNG)

## Profile
Your profile will show you how many items you have. You can also change your password here and even delete all your items from the database.
![profile](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/profile.PNG)

# Admin features
Admins can access all pages a user can.
At first startup, the program will create an admin user. You should change the password to something more secure.
```
username: admin
password: admin
```
## Admin navbar
After logging in as an admin you will see more things in your navbar.
![admin navbar](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/admin%20navbar.PNG)

### All users
This view will list all users with no items, and give an admin the option to give anyone else admin rights. The admin rights can also be revoked for all but the main admin account. This will make sure that you will always have control of your Shopping List.
![all users](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/all%20users.PNG)

### Item amounts
This view will list all users and the amount of items they have. If a user has 0 items attached to them, a button to delete said will appear. This button is disabled for now.
![item amounts](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/items%20amounts.PNG)

### All items
This view lists all items in the database.
![all items](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/all%20items.PNG)

### Add categories
Only admins have access to add categories. This is because categories aren't user specific so giving users access to this might make the app unusable.
![add categories](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/new%20category.PNG)
