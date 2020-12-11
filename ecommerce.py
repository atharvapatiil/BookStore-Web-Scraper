from bs4 import BeautifulSoup
import requests
import csv

num_dic ={'Zero':0, 'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}

csv_file = open('books.csv','w',encoding="utf-8", newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['book_name', 'book_price_euros', 'book_rating', 'book_availability'])

for i in range(1,51):

	source = requests.get(f"http://books.toscrape.com/catalogue/page-{i}.html").text

	soup = BeautifulSoup(source, 'lxml')
	# print(soup.prettify())

	for product in soup.find_all('article',class_="product_pod"):
	# print(product.prettify())

		book_name = product.h3
		book_name = book_name.find('a')['title']
		print(book_name)

		book_price_euros = product.find('p', class_="price_color").text
		book_price_euros = book_price_euros[2:]
		print(book_price_euros) 

		book_rating = product.find('p', class_="star-rating")['class'][-1]
		print(num_dic[book_rating])

		book_availability = product.find('p', class_="instock availability").text
		book_availability = book_availability.strip()
		print(book_availability)

		print()

		csv_writer.writerow([book_name, book_price_euros, book_rating, book_availability])

	print("Page", i)

csv_file.close()