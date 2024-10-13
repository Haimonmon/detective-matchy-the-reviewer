import requests
import os
import io

class NoUrlBro(Exception):
    pass

class Request:
    """
    👉 For Easy request and saving an html file
    """
    def __init__(self, url: str = None) -> None:
        if url is not None:
            self.url = self.url
        else:
            raise NoUrlBro('It needs an url for requesting')

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "Accept-Language": "en-us",
            "Accept-Charset": "utf-8"
        }

    def load_html_content(self) -> str:
        """
        Loads the html content from amazon ;)
        """
        with open("html_content.txt", "r", encoding='utf-8') as file:
            return file.read()


    def save_html_content(self, text_to_save: str, filename) -> None:
        """
        Saving html content from scraping 
        """
        with open(filename, 'w+', encoding='utf-8') as file:
            file.write(text_to_save)

        io_string = io.StringIO(text_to_save)

        io_string.close()


    def request_amazon_html(self) -> str:
        """
        sends a requests on a given url to have the page html code
        """
        response = requests.get(self.url ,headers=self.headers)

        if response.status_code == 200:
            return response.text
        else:
            print('Failed Response request sorry Bro :<')


    def request_html(self, filename) -> None:
        """ Main function

        Request then save to the designated filename
        """
        if os.path.exists(filename) and os.path.getsize(filename):
            html_content = self.load_html_content()
        else:
            html_content = self.request_amazon_html()

            self.save_html_content(html_content, filename)
        
        return html_content


if __name__ == "__main__":
      request = Request()