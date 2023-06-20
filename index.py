from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/'
}

response = requests.get('https://cvr.ac.in/home4/index.php/academics/results', headers=headers)

if response.status_code == 200:
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    iframe_element = soup.find('iframe')

    if iframe_element:
        iframe_src = iframe_element['src']

        iframe_response = requests.get(iframe_src, headers=headers)

        if iframe_response.status_code == 200:
            iframe_content = iframe_response.content

            iframe_soup = BeautifulSoup(iframe_content, 'html.parser')

            with open('iframe_data.txt', 'w', encoding='utf-8') as file:
                file.write(iframe_soup.prettify())

            print('Data saved to iframe_data.txt successfully.')

        else:
            print('Failed to fetch iframe content. Status code:', iframe_response.status_code)
    else:
        print('Iframe element not found.')
else:
    print('Request was not successful. Status code:', response.status_code)
