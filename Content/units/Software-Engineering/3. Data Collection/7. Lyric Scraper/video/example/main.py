# %%
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# %%


class LyricScraper():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.go_to_homepage_charts()
        self.driver.get("https://genius.com/#top-songs")
        sleep(1)
        self._accept_cookies()
        sleep(1)

    def _accept_cookies(self):
        accept_button = self.driver.find_element(
            By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')
        accept_button.click()

    def get_song_links(self):
        charts = self.driver.find_element(By.XPATH, '//div[@id="top-songs"]')
        songs = charts.find_elements(By.XPATH, "div/div/a")
        return [song.get_attribute("href") for song in songs]

    def get_lyrics(self, fp):
        lyrics = self.driver.find_element(
            By.XPATH, '//div[@data-lyrics-container="true"]').text
        with open(fp, "w") as f:
            f.write(lyrics)

    def go_to_homepage_charts(self):
        self.driver.get("https://genius.com/#top-songs")
        # self.driver.execute_script("window.scrollBy(0, 600)")

    def get_all_song_lyrics_for_genre(self, genre):
        self.go_to_homepage_charts()
        self.set_genre(genre=genre)
        sleep(1)
        song_links = self.get_song_links()

        folder = os.path.join("data", genre)
        os.makedirs(folder, exist_ok=True)

        for song_link in song_links:
            self.driver.get(song_link)
            song_name = self.driver.current_url.split('/')[-1]
            filename = os.path.join("data", genre, f"{song_name}.txt")
            self.get_lyrics(filename)

    def set_genre(self, genre='Rap'):
        dropdown_button = scraper.driver.find_element(
            By.XPATH, "//div[contains(@class, 'SquareManySelects__Wrapper-sc-1kktot3-0')]")
        dropdown_button.click()
        sleep(1)
        columns = scraper.driver.find_elements(
            By.XPATH, "//div[@class='SquareManySelects__Select-sc-1kktot3-3 gIwQZZ']")[1]
        genres = columns.find_elements(By.XPATH, 'div')[2:]
        print(genre)
        print([g.text for g in genres])
        genre = [g for g in genres if g.text == genre][0].click()
        dropdown_button.click()

    def get_all_song_lyrics_for_all_genres(self):
        genres = ["Rap", "Pop", "R&B", "Rock", "Country"]
        for genre in genres:
            self.get_all_song_lyrics_for_genre(genre=genre)


scraper = LyricScraper()
scraper.get_all_song_lyrics_for_all_genres()
scraper.driver.quit()

# %%
