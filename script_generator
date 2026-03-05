import openai
import random

openai.api_key = "YOUR_OPENAI_API_KEY"

def gpt_generate_script(title, variations=5):
    scripts = []
    for i in range(variations):
        prompt = f"""
Buatkan script YouTube Shorts berdurasi 45-60s, tajuk: "{title}".
Buat format fast-reveal + hook menarik di awal + list info.
Hasilkan versi variasi ke-{i+1}.
"""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        scripts.append(response['choices'][0]['message']['content'])
    return scripts
