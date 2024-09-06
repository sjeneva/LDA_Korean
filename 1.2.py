import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to scrape
base_url = 'https://www.sdcexec.com'
path = '/sourcing-procurement/article/'

# Parameters for the GET request
params = {
    'view_type': 'sm',
    'sc_word': 'ESG'
}

# Set the number of pages you want to scrape
number_of_pages = 10

# Initialize a list to store the scraped data
articles_data = []

# Loop over the range of pages you want to scrape
for page in range(1, number_of_pages + 1):
    # Update the 'page' parameter in the params dictionary
    params['page'] = page

    # Create the full URL with parameters
    full_url = base_url + path
    response = requests.get(full_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <h4> elements with class 'titles' which contain the article titles and links
        article_titles = soup.find_all('h4', class_='titles')

        # Check if any articles were found
        if article_titles:
            # Extract links and prepend base URL if necessary
            for title in article_titles:
                a_tag = title.find('a')
                if a_tag:
                    link = a_tag['href']
                    # Ensure the link is absolute by checking if it already starts with http(s)
                    if not link.startswith('http'):
                        link = base_url + link
                    # Add the data to the list
                    articles_data.append({"Page": page, "Link": link})
        else:
            print(f"No articles found on page {page}. Check your selector.")
    else:
        print(f"Failed to retrieve page {page}, status code: {response.status_code}")

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(articles_data)

# Specify the filename and path for the Excel file
filename = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESGL_Korean\supplychaindigital.xlsx'


# Write the DataFrame to an Excel file
df.to_excel(filename, index=False)

print(f"Scraped data has been saved to {filename}.")
