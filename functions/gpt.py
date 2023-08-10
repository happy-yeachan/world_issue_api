import openai
from secret import *

def gpt(content):
    # 발급받은 API 키 설정
    OPENAI_API_KEY = gpt_key

    # openai API 키 인증
    openai.api_key = OPENAI_API_KEY

    # 모델 - GPT 3.5 Turbo 선택
    model = "gpt-3.5-turbo"

    # 질문 작성하기
    query = content + "/n 이 기사를 3개의 한국어 말머리로 요약해줘"

    # 메시지 설정하기
    messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query}
    ]

    # ChatGPT API 호출하기
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    answer = response['choices'][0]['message']['content']
    return(answer)