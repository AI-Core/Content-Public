# services/dob_service.py
from bs4 import BeautifulSoup
import json
import re
import httpx

async def get_dob(first_name: str, last_name: str, city: bool=False):
    infobox_data = await get_infobox_async(first_name, last_name)
    if not infobox_data:
        return None
    birthday = infobox_data.find('span', {'class': 'bday'})

    report = {'first name': first_name,
              'last_name': last_name,
              'Date of Birth': birthday.text}
    if city:
        birthplace = infobox_data.find('div', {'class': 'birthplace'})
        report['City'] = birthplace.text

    return report

async def get_infobox_async(first_name: str, last_name: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f'https://en.wikipedia.org/wiki/{first_name}_{last_name}')
        html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    if soup.find_all('b', text=re.compile('Wikipedia does not have an article with this exact name')):
        return None
    celeb_infobox = soup.find('table', {'class': 'infobox biography vcard'})
    return celeb_infobox.find('td', {'class': 'infobox-data'})