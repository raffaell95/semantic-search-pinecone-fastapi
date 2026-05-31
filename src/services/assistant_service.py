from src.services.authentication_service import authenticate_openai

client_openai = authenticate_openai()

def assistant_question(question: str, short_extract: str):

    try:
        response = client_openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant, which will respond only based on the excerpt sent to you."
                },
                {
                    "role": "user",
                    "content": f"The question is {question} and the excerpt is {short_extract}"
                }
            ]
        )

        return response.choices[0].message.content
    except Exception as e:
        return {"error": str(e)}

