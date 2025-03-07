from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.schema import HumanMessage

# Load environment variables
load_dotenv()

# Fetch API key from environment variables
GEMINI_API_KEY="AIzaSyBM2Xj-1r8RKRiEIooOFnL1c-yYeJvxYRU"

# Ensure API key is provided
if not GEMINI_API_KEY:
    raise ValueError("Error: GEMINI_API_KEY is not set. Check your .env file!")

# Initialize the Gemini chat model
chat_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=GEMINI_API_KEY
)

def analyze_sentiment(scraped_data):
    # Prepare the prompt for sentiment analysis
    prompt = f"Analyze the sentiment of the following data: {scraped_data}"
    
    # Get the response from the model
    response = chat_model.invoke([HumanMessage(content=prompt)])
    
    # Extract and return the content of the response
    return response.content
