import mechanize, csv
from bs4 import BeautifulSoup

# disclaimer; i have no idea what im doing

# target html for mayor data
url = "https://www.usmayors.org/mayors/meet-the-mayors"

# fill out the search form with mechanize, header set to avoid 403
br = mechanize.Browser()
br.set_header("User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")
br.open(url)


states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
          "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
          "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
          "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
          "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
          "Utah", "Vermont", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
mayors = [("ID", "Name", "Location", "Phone", "Email")]
num = 1
for state in states:
    br.select_form(id="searchform")
    br["searchTerm"] = state
    search_response = br.submit()
    html = BeautifulSoup(search_response.read(), 'lxml')

    # this is so horrendously inefficient im so sorry
    # gather name, town, phone, email
    for ul in html.select('main ul'):
        name = ul.find('b').get_text()

        town = ul.find_all('br', limit=2)[-1]
        location = town.next_sibling

        contact = []
        email = ul.find_all('br')
        for mail in email:
            m = mail.find_next_sibling('a')
            if m is None:
                continue
            elif m.get_text() == "Bio" or m.get_text() == "Web Site":
                continue
            else:
                contact.append(m.get_text())
        if len(contact) == 2:
            mayor = (num, name, location, contact[0], contact[1])
            mayors.append(mayor)
            num += 1

with open('mayors.csv', 'w', newline='') as csvfile:
    write = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for mayor in mayors:
        write.writerow(mayor)
