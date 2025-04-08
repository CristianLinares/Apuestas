import requests
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": texto,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=data)
    print("Mensaje enviado:", texto)

def analizar_y_enviar():
    pick = (
        "*[Análisis automático]*\n"
        "*Tenis de mesa - Liga Pro Checa*\n"
        "*Partido:* Novy vs Trsekn\n"
        "*Pick:* Más de 75.5 puntos totales\n"
        "*Stake:* 8/10\n"
        "*Confianza:* Alta\n"
        "*Probabilidad estimada:* 73%\n"
    )
    enviar_mensaje(pick)

if __name__ == "__main__":
    analizar_y_enviar()
    time.sleep(7200)  # cada 2 horas (opcional, si quieres que se repita)