# HelloFresh-Meal-Planner
Scrape Hello Fresh most popular (>200 Recipes), and makes a grocery list!

Dependencies for py script:
* BeautifulSoup
* selenium
* functools
* Chrome installed

Dependencies for exe:
* Chrome installed

1. Run the script, it'll ask you how many you want.
2. It'll select how many you want from the list at random.
3. Creates a file with the list of recipes (freshRecipes.txt) in the same directory as you are running it from.
4. Creates a file with a unique list of grocery items (freshGrocery.txt)
   * If an item is in 2 or more recipes, they are consilidated and will have a comma delimited list of amounts.
5. Use your favorite app to import these lists to and have fun!  
