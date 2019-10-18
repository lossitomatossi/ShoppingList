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
