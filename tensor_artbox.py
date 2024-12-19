import openai
import matplotlib.pyplot as plt
from PIL import Image
import io
import requests
import os  # Import the os module to read environment variables

# Define the OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Generate a tattoo image based on user prompt
def generate_tattoo(prompt):
    # Make a request to OpenAI to generate an image based on the prompt
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    # Get the image data from the response
    image_url = response['data'][0]['url']
    return image_url

# Display the generated tattoo image
def display_image(image_url):
    # Load the image from the URL
    image = Image.open(io.BytesIO(requests.get(image_url).content))
    plt.figure(figsize=(4, 4))
    plt.imshow(image)
    plt.axis('off')
    plt.show()

# Main function to get user input and display the generated tattoo
def main():
    # Get user input for the tattoo description
    user_prompt = input("Enter a description for the tattoo: ")
    
    # Generate the tattoo based on the user prompt
    generated_tattoo_url = generate_tattoo(user_prompt)
    
    # Display the generated tattoo image
    display_image(generated_tattoo_url)

if __name__ == "__main__":
    main()