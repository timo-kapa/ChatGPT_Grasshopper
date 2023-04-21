              
import rhinoscriptsyntax as rs
import urllib2
import json
                
                
url = "https://api.openai.com/v1/completions"
                
                
data = json.dumps({ "model": "text-davinci-003", "prompt": user_input, "temperature": 0.5,  "max_tokens": 1024})
headers = { "Content-Type": "application/json", "Authorization": "Bearer {0}".format(api) }
                
GPT_output = "Send to request to Open AI"
                
if generate:
                
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
                
                
    response_text = response.read()
    response_json = json.loads(response_text)
                
                
    GPT_output = response_json["choices"][0]["text"]
                
print(GPT_output)
                
        
