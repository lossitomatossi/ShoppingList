# Disclaimer
(when run locally, works in heroku)
the app assumes in it's current state that you manually enter the first category before adding any items

# ShoppingList
A python based web project to manage your shopping needs. You can track which items you want to buy, which items you've already bought and view virtual shopping list for different occasions.

## Heroku link

[tsoha-shoppinglist](https://tsoha-shoppinglist.herokuapp.com/)

All permissions user for heroku testing.
```
username: admin password: admin
```

## Features currently working in heroku
- logging in and out
- viewing added items (by default all items will be given a category_id of 1 which is the id for the default line in the category table)
- adding items to the database and marking them as bought (both as you are adding them and also as you are updating them
- you can list categories in /categories (link missing)
- you can add new categories in /categories/new (link missing)

## Features
- create users
- delete users (deleting a user will delete all your lists)
- add items to be bought
- mark items as bought
- assign categories to items
- change/remove categories from items
- change the amount of an item you want to buy
- add items to lists
- delete items from lists
- rename lists
- delete lists
- add categories
- delete categories
- assign items different categories

## Database diagram
![diagram](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/tietokantakaavio.png)
