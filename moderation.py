import openai

def moderate_text(text):
    response = openai.Moderation.create(input=text)
    return response["results"][0]
