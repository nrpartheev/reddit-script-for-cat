import requests
import time
import praw
from bs4 import BeautifulSoup


reddit = praw.Reddit(
    client_id="007- bond, james bond",
    client_secret="I'm in love",
    username="Accurate_Pickle2863",
    password="haha sure I will tell you my bank pin also", 
    user_agent="CAT preparation bot"
)


url = "https://cdn.digialm.com/EForms/configuredHtml/32842/89884/login.html"

subreddit_name = "CATpreparation"


offline_message = """The Form is no longer available"""

def is_site_up():
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  
        print(response.status_code)
        soup = BeautifulSoup(response.text, "html.parser")
        return offline_message not in str(soup)
    except Exception as e:
        print(f"Error checking site: {e}")
        return False

def post_to_reddit():
    subreddit = reddit.subreddit(subreddit_name)
    title = "The CAT login page is 99% live! POSTED BY THE BOT (by u/Accurate_Pickle2863)"
    body = (
        "The CAT login page is back up and accessible. Check it out here:\n\n"
        f"[Login Page]({url})"
    )
    subreddit.submit(title, selftext=body, flair_id="dafa230c-44c1-11ee-95e3-a6e52c1c6db6") 
    print("Posted alert to Reddit.")

def main():
    count = 0
    while True:
        if is_site_up():
                print("posting")
                post_to_reddit()
                print("SCRIPT RAN FOR: ",count*3,"s")
                break   
        else:
            print("WEBSITE DOWN")
            count += 1
        
        time.sleep(3)

if __name__ == "__main__":
    main()
