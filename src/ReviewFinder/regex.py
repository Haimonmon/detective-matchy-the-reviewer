import re

class FindReview:
    """
    Returns a list of reviews including the top review of the product
    """
    def __init__(self, html_content:str) -> None:
        self.__html_content = html_content


    def clean_text_review(self, list_of_reviews:str) -> list:
        if list_of_reviews is None:
            return None 

        cleaned_reviews = []

        for reviews in list_of_reviews:
            clean_text = re.sub(r'<br\s\/>', ' ', reviews)  # Remove <br> tags and replace with space
            cleaned_reviews.append(clean_text)
        
        print(f'\n{len(cleaned_reviews)} <- Reviews has been Cleaned ✅✨')

        return cleaned_reviews

    def find_review_container(self) -> str:
        """
        Gets the review Container first in html
        """

        """
        As i inspect the html code on the amazon i want to get the review container 

        * <div id="cm-cr-dp-review-list" data-hook="top-customer-reviews-widget" class="a-section review-views celwidget"> <-- This is the starting div of the main container of the reviews

        But the problem is i cant just get its ending tag as its so many ending divs so i just get the after code block of the ending tag of this div tag
        
        *  <div id="reviews-medley-footer" data-hook="reviews-medley-footer" class="a-section"><div class="a-row"></div><div class="a-row a-spacing-medium"> <-- this is the after block code of the cm-cr-dp-review
        
        so i make this the ending point on the regex... i make this method, idk i just want to guarantee that every product link, this code will still work lmao kabado eh haha ✌️💀
        """

        pattern = r'<div id="cm-cr-dp-review-list".*?<\/div>(\s*<div id="reviews-medley-footer")'

        # * REFERENCE: https: // www.w3schools.com/python/python_regex.asp
        # * REFERENCE: https://docs.python.org/3/library/re.html
        match = re.search(pattern, self.__html_content, re.DOTALL)

        if match:
            review_container = match.group(0)
            return review_container
        
        return None
            

    def find_reviews(self,html_review_container):
        container = html_review_container

        pattern = r'<div data-hook="review-collapsed".*?<span>(.*?)<\/span>.*?<\/div>'

        list_of_reviews = re.findall(pattern, container, re.DOTALL)

        if len(list_of_reviews) != 0:
           cleaned_text = self.clean_text_review(list_of_reviews)
           return cleaned_text


    def get_review_html(self):
        if self.__html_content:
            html_review_container = self.find_review_container()

            if html_review_container:
                return self.find_reviews(html_review_container)

        return None




class DetectiveNLP:
    """
    🔎 Just See if its Match the user review
    """
    def __init__(self, html_content: str) -> None:
        self.__html_content = str(html_content)
        self.__finder = FindReview(self.__html_content)
        self.__reviews = self.__finder.get_review_html()



    def wrap_review(self, review):
        """
        Just wrap the text in 80 characters using regex
        """
        pattern = r'(.{1,80})(?:\s+|$)'

        # * REFERENCE: ideal ref for the wrapping using regex, change mind of using import textwrap, i wanna highlight the powerfull regex :), https://stackoverflow.com/questions/16430200/a-good-way-to-make-long-strings-wrap-to-newline
        # * Add 1 new Line Break r'\1\n'
        wrapped_review = re.sub(pattern, r'\1\n ', review)

        return wrapped_review



    def print_review(self, index:int, review:str) -> None:
        if index == 1:
            print('\n')
            print(' '*25, '✨ ✨ 👑 Top Review 👑 ✨ ✨')
            print('\033[33m' + '-' * 82 + '\033[0m')
            print(f'\n \033[33m{self.wrap_review(review)}\033[0m')
            print('\033[33m' + '-' * 82 + '\033[0m')
            print('\n')
        else:
            print('\n')
            print(82*'-')
            print(f'\n { self.wrap_review(review)}')
            print(82*'-')
            print('\n')
    


    def calculate_review(self,index:int , review:str) -> None:
        """
        using the library NLTK we were able to detect the ` Positive ` ` Neutral ` ` Negative ` Words
        """
        self.print_review(index, review)

      


    def get_nlp(self):
        print('\n\n')
        for index, review in enumerate(self.__reviews, 1):
            self.calculate_review(index, review)

        print('\033[33m' + '-' * 82 + '\033[0m')
        print(f'\n \033[33m In Total of {len(self.__reviews)} Reviews have been found by our ` Review Finder ` ✅\033[0m \n')
        print('\033[33m' + '-' * 82 + '\033[0m')



if __name__ == "__main__":
    finder = FindReview()

