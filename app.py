
from flask import Flask
from openai import OpenAI
from azure.identity import AzureCliCredential, DefaultAzureCredential

app = Flask(__name__)

@app.route("/")
def home():

    SCOPE = "https://azure-api.net/aigateway/.default"

    credential = DefaultAzureCredential()

    token = credential.get_token(SCOPE).token

    print("Successfully acquired access token.")

    client = OpenAI(
        base_url="https://ai-gateway-poc.eastus2-01.ai.gateway.azure.com/default/models/openai/v1",
        api_key=token,
    )
    try:
        response = client.responses.create(
            model="poc-model",
            input="Hello!",
        )
    except Exception as e:
        print(f"Error occurred: {e}")
        response = None

    result = {
        "response": response.output_text if response else "Error occurred while getting response"
    }

    print(result)

    if __name__ == "__main__":
        app.run(debug=False)
