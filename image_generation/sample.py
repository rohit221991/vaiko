from openai import OpenAI
client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="On a busy Indian street, Arjun, looking curious and empathetic, watches a group of children trying to play a game on an old, glitchy phone. The children appear frustrated as the game keeps stopping. The background shows a typical bustling street scene.",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url

print(image_url)

print(response.data)
