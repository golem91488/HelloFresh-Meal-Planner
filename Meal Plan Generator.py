#!/usr/bin/env python
# coding: utf-8
from bs4 import BeautifulSoup
import requests
import sys, os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from functools import reduce

URL = "https://www.hellofresh.com/recipes/most-popular-recipes?page=50"
driver = webdriver.Chrome()
driver.get(URL)
time.sleep(5)
list_links = [ele.find_element(By.TAG_NAME, 'a').get_attribute('href') for ele in driver.find_elements(By.XPATH, "//div[@data-test-id='recipe-image-card']")]
driver.close()
uniqLinks = reduce(lambda accu,curr: accu+[curr] if curr not in accu else accu, list_links, [])
uniqLinks = uniqLinks[:len(uniqLinks)-6]

#creates dataframe with the recipe title and link to recipe
num_recipes = int(input("Number of recipes: "))
random_recipes = random.choices(uniqLinks, k=num_recipes)


output = open(os.path.join(os.path.dirname(sys.executable),'freshRecipes.txt'), 'w')
output.write("\r\n\r\n".join(list(random_recipes)))
output.close

raw_ingredients = []
for row in random_recipes:
    rPage = requests.get(row)
    soup = BeautifulSoup(rPage.content, "html.parser")
    raw_ingredients.append([list(map(lambda x: x.replace(" | ", ""),ingr.get_text(separator = " | ").split(" | ", 1))) for ingr in soup.find_all('div',{'data-test-id':'ingredient-item-shipped'})])

ingredients = {}
for row in raw_ingredients:
    for item in row:
      amt = ingredients.get(item[1].replace('  ',' '),'') + ', ' + item[0].strip()
      ingredients[item[1].replace('  ',' ')] = amt[2:] if amt.startswith(', ') else amt

output = open(os.path.join(os.path.dirname(sys.executable),'freshGrocery.txt'), 'w')
output.write(str(ingredients).replace("', '", "'\r\n'").replace("{","").replace("}",""))
output.close