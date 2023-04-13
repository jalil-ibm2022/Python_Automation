import requests
import argparse
import os


parser= argparse.ArgumentParser()
parser.add_argument("prompt",help="The prompt to send to the OpenAI API")
parser.add_argument("file_name",help="Name of the file to save")
args= parser.parse_args()

api_endpoint= "https://api.openai.com/v1/completions"
api_key= os.getenv("openai_api_key")


request_headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key} "


}
request_data = {
    "model": "text-davinci-003",
    #"prompt": f"explain the tasks of {args.prompt}",
    "prompt": f"write python script to {args.prompt}.Provide only code , no text ",
    "max_tokens": 1000,
    "temperature": 0.5

}
response = requests.post(api_endpoint, headers=request_headers, json=request_data)

#print(response)


if response.status_code == 200:  # HTTP RESPONSE STATUS CODES 
   
   response_text= response.json()["choices"][0]["text"]
   #response_text= response.json()
   with open(args.file_name,"w") as file:
      #while token in response_text:
        file.write(response_text)

else:    
   print(f"Request failed with status code:{response.status_code}")     