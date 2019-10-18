 # SQL-queries used in the app
 Below you'll find lists of items queries grouped by the class which uses them
 ## User(Table: Account)
 
 - Method for finding accounts with no items
 ```
 SELECT Account.id, Account.name FROM Account
  LEFT JOIN Item ON Item.account_id = Account.id
  WHERE (Item.bought IS null OR Item.bought = TRUE)
  GROUP BY Account.id
  HAVING COUNT(Item.id) = 0;
 ```
                    
 - Method for deleting all items a user has
```
DELETE FROM Item
  WHERE Item.account_id = user.id;
```                    
                    
- Count existing users
```
SELECT COUNT(*) FROM Account;
```

- Used to create default admin account when the app starts, if there are no users in the database
```
INSERT INTO Account
  (name, username, password, role)
  values ('admin', 'admin', 'admin', 'ADMIN');
```

- Make (id, username) pairs of all users, used for listing
```
SELECT id, username, role from Account;
```

- Get amount of items for each user
```
SELECT account.id, account.username, COUNT(item.account_id)
  FROM Account
  LEFT JOIN Item ON account.id = item.account_id
  GROUP BY account.id;
 ```
- Delete user by user_id
```
DELETE FROM Account
  WHERE (id = user_id);
```

## Item
- Delete singly item by item_id
```
DELETE FROM ITEM WHERE Item.id = item_id;
```        
- Find all items for a user 
```
SELECT Item.id, Item.name, Item.bought, Item.amount, Item.list_id, Item.category_id FROM Item
 WHERE (Item.account_id = user_id);
```
- Count items for a user
```
SELECT COUNT(id) FROM Item
 WHERE (Item.account_id = user_id);
```
- Delete item by item_id
```
DELETE FROM Item
 WHERE Item.account_id = item_id;
```
- Currently not functional method to update all fields in an item
```
UPDATE Item
 SET name = name, amount = amount, bought = bought, list_id = list_id, category_id = category_id
 WHERE (id = item_id);
```
## List
- Find all lists for a user
```
SELECT List.id, List.name, List.info FROM List
 WHERE (List.account_id = user_id);
```
- Used to create a python dictionary of (list_id, list_name) tuples for a user
```
SELECT List.id, List.name FROM List
 WHERE (List.account_id = user_id);
```
- Amount of lists for a user
```
SELECT COUNT(id) FROM List
 WHERE (List.account_id = user_id);
```
- Checks if a user has default list, used by the application to make sure each user has a list where an item can be added
```
SELECT name FROM List
 WHERE (List.account_id = user_id)
 AND name = 'default';
```
- Get id of users default list, this is where items will be added by default
```
SELECT id FROM List
 WHERE (List.account_id = user_id)
 AND name = 'default';
```
- If default list is missing, this is used to create it
```
l = List("default", "default list to ensure proper functioning")
l.account_id = id
        
db.session.add(l)
db.session.commit()
```
- Find all items for a list by list_id
```
SELECT Item.id, Item.name, Item.bought, Item.amount, Item.category_id FROM Item
 WHERE (Item.list_id = user_id);
```
- Deletes all lists by user_id
```
DELETE From List
 WHERE (List.account_id = user_id);
```
- Used to create python dict for (list_id, list_name) tuples                 
```
SELECT List.id, List.name FROM List;
```
