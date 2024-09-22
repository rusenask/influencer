import scraper
import client
import social
from flask import Flask, jsonify
from datetime import datetime
import time

model = "phi3.5" # phi3.5
port = 5000

app = Flask(__name__)

@app.route('/action', methods=['POST'])
def run_action():
  
    # Start timing for fetch# Start timing for fetch
    fetch_start_time = time.time()
      
    # Find some content
    pageURL = scraper.findArticle()
    print(pageURL)
    
      # Calculate fetch time
    fetch_time = time.time() - fetch_start_time
    print(f"Time taken to fetch data: {fetch_time:.2f} seconds")
    
    scraper_start_time = time.time()

    # Fetch that content
    title, description, content = scraper.fetchPage(pageURL)

    scraper_time = time.time() - scraper_start_time
    print(f"Time taken to scrape data: {scraper_time:.2f} seconds")
    
    print(title)
    print(description)    

    # Construct a prompt
    prompt = f"The content of an article is {content}"
    prompt += """Write some commentary about about a key point of the article's contents and encourage the reader to check it out in a professinal tone for a LinkedIn post.  
    The entire post should be two sentences.  Use a couple emojis too.  
    Respond with only the post, no additional commentary, no notes, no link"""
    
    prompt_start_time = time.time()
    
    print('Prompting the model to generate a post...')    

    # Feed that prompt to the LLM to get a response
    postContent = str(client.chat(model, prompt))
    print(postContent)

    prompt_time = time.time() - prompt_start_time
    print(f"Time taken to prompt: {prompt_time:.2f} seconds")

    # Post to our networks
    # social.postLinkedIn(postContent, pageURL, title, description)
    # social.postTwitter(postContent, pageURL)
    
    # Return a JSON response with the title, description and content for the caller
    return jsonify({"title": title, "description": description, "content": content})
        

if __name__ == '__main__':
    # Starts server on port 5000
    app.run(debug=True, port=port)

