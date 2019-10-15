# Installing ShoppingList

## Required programs
When run locally, you need Python3 and sqlite3. You can download them using the terminal or from the links below.
- Python3 can be downloaded from https://www.python.org/downloads/
- Sqlite3 can be downloaded from https://www.sqlite.org/download.html

## Downloading the app
- If you have git you can paste the following in your terminal
```
git clone https://github.com/lossitomatossi/ShoppingList/
```

- Or click the green button on the right
![ShoppingList frontpage](https://github.com/lossitomatossi/ShoppingList/blob/master/documentation/Pictures/asennusohje1.png)

If the file was packaged in zip format then extract it to your desired folder.

## Preparing for usage
- Next you should navigate to the root of the shoppinglist folder (it's the folder that contains for example README.md and Procfile).
```
~$ cd projekti
```
- Then paste the following in to the terminal
```
~/projekti$ python3 -m venv venv
```
```
~/projekti$ source venv/bin/activate
```
## Installing requirements
```
(venv) ~/projekti$ pip install -r requirements.txt
```
-If there are problems with "wheel", then try the following:
```
(venv) ~/projekti$ pip install wheel
```
```
(venv) ~/projekti$ pip install -r requirements.txt
```
## Now you can start the program

```
(venv) ~/projekti$ python3 run.py
```
