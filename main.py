import gradio as gr

import geocoder
import weather

def main(city: str):
    lat, lon = geocoder.get(city)
    if lat is None:
        return "Invalid city name"
    weather_data = weather.get(lat, lon)
    message = f"Сейчас {weather_data['current']['temperature_2m']} {weather_data['current_units']['temperature_2m']}."
    message += f"\nЗавтра {weather_data['daily']['temperature_2m_max'][1]} {weather_data['daily_units']['temperature_2m_max']}."
    message += f"\nПослезавтра {weather_data['daily']['temperature_2m_max'][2]} {weather_data['daily_units']['temperature_2m_max']}."

    return message


with gr.Blocks() as app:
    city = gr.Textbox(label="Город")
    btn = gr.Button(value="Узнать погоду")
    result = gr.Textbox(value="", label="Результат", lines=3)
    btn.click(main, inputs=[city], outputs=[result])

if __name__ == "__main__":
    app.launch()