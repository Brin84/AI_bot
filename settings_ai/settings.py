from openai import OpenAI
import asyncio
from config import AI_TOKEN

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=AI_TOKEN,
)


async def ask(prompt: str):
    """корутина для асинхронного запроса к OpenRouter"""
    completion = await asyncio.to_thread(
        client.chat.completions.create,
        model="deepseek/deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content


# async def main_test():
#     response = await ask("Как дела, мой друг?")
#     print(response)
#
#
# if __name__ == "__main__":
#     asyncio.run(main_test())
