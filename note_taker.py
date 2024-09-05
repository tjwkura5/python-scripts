from urllib.parse import urlparse

import requests
import textwrap


api_key = "2d22deaf7amshc8de22a0526b67ap191f28jsn5141be13d462"

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def format_text(text):
    text = textwrap.dedent(text)
    text = textwrap.fill(text, width=70)
    return ' '.join(text.split())


def extract(payload):
    host = "https://news-article-data-extract-and-summarization1.p.rapidapi.com/extract/"

    headers = {
	    "x-rapidapi-key": api_key,
	    "x-rapidapi-host": "news-article-data-extract-and-summarization1.p.rapidapi.com",
	    "Content-Type": "application/json"
    }

    try:
        response = requests.post(host, headers=headers, json=payload)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f'An error occured: {e}')

def summarize(payload):
    host = "https://gpt-summarization.p.rapidapi.com/summarize"

    headers = {
	    "x-rapidapi-key": api_key,
	    "x-rapidapi-host": "gpt-summarization.p.rapidapi.com",
	    "Content-Type": "application/json"
    }

    try:
        response = requests.post(host, headers=headers, json=payload)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f'An error occured: {e}')

print('Hi! This is a note taker script where you can create notes/summaries of blogs and articles')

while True:
    website = input("Please provide the website to your article: ")

    if is_valid_url(website):
        extract_request_body = {"url": website}
        extract_response = extract(extract_request_body)
        extract_json = extract_response.json()

        print(f'The following is a description of the extracted text: \n\n{format_text(extract_json["description"])}\n\n')

        while True:
            user_input = input("Does this description look correct? Please enter 'yes' or 'no': ").strip().lower()
            if user_input in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
        
        if user_input == 'yes':
            break
        else:
            print('Please provide the website to your article again')

    else:
        print("The URL is invalid. Please provide a valid URL.")

print(f"\n----- Here is your extracted text it contains {extract_json["length"] } words. -----\n")

print(format_text(extract_json['text']))

while True:
    sentences = input("\nHow many sentences would you like your summary to be?: ")
    try:
        # Attempt to convert the input to an integer
        num_sentences = int(sentences)
        break  
    except ValueError:
        # If conversion fails, prompt the user to try again
        print("Please enter a valid number.")

chat_payload = {
    "text": extract_json['text'],
    "num_sentences": num_sentences

}

notes_response = summarize(chat_payload)
notes_json = notes_response.json()

print(f'\nHere is the summary from the extracted text: \n\n{format_text(notes_json["summary"])}\n\n')


