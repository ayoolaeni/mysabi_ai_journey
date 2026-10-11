# import os 
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# client = genai.Client(api_key = os.environ["Gemini_API_KEY"])

# response = client.models.generate_content (
#     model = "gemini-3.5-flash-lite",
#     contents = "Explain what an API is to a 10-year-old in 3 sentences."
# )

# print(response.text)



import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key= os.environ["Gemini_API_KEY"])
response = client.models.generate_content(
    model = "gemini-3.5-flash-lite",
    contents = "Tell me a very short history of how AI started"
)

print(response.text)