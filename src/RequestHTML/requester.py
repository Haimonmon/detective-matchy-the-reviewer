import requests
import os
import io

class NoUrlBro(Exception):
    pass

class RequestAuto:
    """
    👉 For Easy request and saving an html file, if file is already existed , returns ` html content `
    """
    def __init__(self,filename:str, url: str = None) -> str:
        if url is not None:
            self.url = url
        else:
            raise NoUrlBro('It needs an url for requesting')

        self.filename = filename
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "Accept-Language": "en-us",
            "Accept-Charset": "utf-8"
        }

        self.html_content = self.request_html(f'{self.filename}.txt')

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

        print('This is a red flag so be careful broda 🚩🚩🚩🚩')
        
        if response.status_code == 200:
            return response.text
        else:
            print('Failed Response request sorry Bro :<')


    def request_html(self, filename) -> str:
        """ Main function

        Request then save to the designated filename
        """
        if os.path.exists(filename) and os.path.getsize(filename):
            html_content = self.load_html_content()

            print('🎉 Loading Saved Html File . . . ✅🐝 - - -')
        else:
            print('Be Careful, Requesting Html . . . 🚩🚀')
            html_content = self.request_amazon_html()

            self.save_html_content(html_content, filename)
            print('File Saved 🎊🎉')
        
        return html_content
    

    def __str__(self):
        return self.html_content
    
if __name__ == "__main__":
      request = RequestAuto()

