import time
import requests
import json

# Função para enviar requests
def enviar_requests(start_number, end_number, interval):
    if start_number > end_number:
        print("Erro: O número inicial deve ser menor ou igual ao número final.")
        return

    if interval < 1:
        print("Erro: O intervalo deve ser maior ou igual a 1 segundo.")
        return

    print("Enviando requests...")
    for i in range(start_number, end_number + 1):
        data = {"loop": i}

        try:
            response = requests.post(
                url="https://webhook.andrealencar.com.br/webhook/ab5296c4-546d-49ae-86b1-ac3ee8907655",
                headers={"Content-Type": "application/json"},
                data=json.dumps(data)
            )

            if response.status_code == 200:
                result = response.json()
                if result.get("message") == "Workflow was started":
                    print(f"Loop {i} enviado com sucesso.")
                else:
                    print(f"Erro no loop {i}: {result.get('message', 'Mensagem desconhecida')}")
            else:
                print(f"Erro no loop {i}: {response.status_code} - {response.reason}")

        except requests.RequestException as e:
            print(f"Erro no loop {i}: {e}")

        # Aguarda o intervalo antes de enviar o próximo request
        if i < end_number:
            time.sleep(interval)

    print("Todos os requests foram enviados.")

# Parâmetros fixos (ou configure-os dinamicamente)
start_number = 24  
end_number = 4358   
interval = 15  #em segundos

enviar_requests(start_number, end_number, interval)
