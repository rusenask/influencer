import scraper
import client
import social
from flask import Flask, jsonify
from datetime import datetime
import os

model = "qwen2.5"

app = Flask(__name__)

@app.route('/action', methods=['POST'])
def run_action():
    # Find some content
    pageURL = scraper.findArticle()
    print(pageURL)

    # Fetch that content
    title, description, content = scraper.fetchPage(pageURL)
    print(title)
    print(description)
    print(content)

    # Construct a prompt
    prompt = f"The content of an article is {content}"
    prompt += """Write some commentary about about a key point of the article's contents and encourage the reader to check it out in a professinal tone for a LinkedIn post.  
    The entire post should be two sentences.  Use a couple emojis too.  
    Respond with only the post, no additional commentary, no notes, no link"""
    print(prompt)

    # Feed that prompt to the LLM to get a response
    postContent = str(client.chat(model, prompt))
    print(postContent)

    # Post to our networks
    social.postLinkedIn(postContent, pageURL, title, description)
    social.postTwitter(postContent, pageURL)
    
    # Return a JSON response with the title, description and content for the caller
    return jsonify({"title": title, "description": description, "content": content})
        

if __name__ == '__main__':
    app.run(debug=True)

