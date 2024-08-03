import requests
import bs4


res = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text, "lxml")
authors = set([a.text for a in soup.select(".author")])
quotes = [q.text for q in soup.select(".text")]

print(authors)
print(quotes)

# class_entry_content = soup.select(".entry-content")
# print(title[0])
# print(class_entry_content)

# Loop through different pages until not found -invalid page be reached
page_still_valid = True
authors = set()
page = 1
url = "http://quotes.toscrape.com/page/"

while page_still_valid:

    # Concatenate to get new page URL
    page_url = url + str(page)

    # Obtain Request
    res = requests.get(page_url)

    # Check to see if we're on the last page
    if "No quotes found!" in res.text:
        break

    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text, "lxml")

    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)

    # Go to Next Page
    page += 1

print("\n")
print("---------------------------")
print("unique authors among all the pages: ", authors)
