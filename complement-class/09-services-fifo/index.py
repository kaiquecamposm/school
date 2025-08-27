import time


def gen_requests(num_requests):
    requests = []
    client_names = ["Cliente_A", "Cliente_B", "Cliente_C", "Cliente_D"]
    problems = [
        "Problema de conexão",
        "Erro no sistemas",
        "Dúvida sobre faturamento",
        "Solicitação de suporte",
    ]

    for i in range(1, num_requests + 1):
        request = {
            "id": i,
            "cliente": client_names[i % len(client_names)],
            "problema": problems[i % len(problems)],
            "horario": f"{time.strftime('%H:%M:%S')}",
        }

        requests.append(request)
        time.sleep(0.1)

    return requests


def add_request(queue_requests, new_request):
    queue_requests.append(new_request)
    return queue_requests


def process_request(queue_requests):
    if queue_requests:
        request = queue_requests.pop(0)
        print(
            f"Processando requisição ID: {request['id']} | Cliente: {request['cliente']} | Problema: {request['problema']} | Horario: {request['horario']}"
        )
        time.sleep(1)
    else:
        print("Nenhuma requisição para processar.")
    return queue_requests


def main():
    num_initial_requests = 5
    queue_requests = gen_requests(num_initial_requests)

    print("Fila inicial de requisições:")
    for request in queue_requests:
        print(request)

    print("\nProcessamento das requisições em ordem:")
    while queue_requests:
        queue_requests = process_request(queue_requests)

    new_request = {
        "id": num_initial_requests + 1,
        "cliente": "Cliente_E",
        "problema": "Reclamação de atraso no serviço",
        "horario": f"{time.strftime('%H:%M:%S')}",
    }
    queue_requests = add_request(queue_requests, new_request)
    print("\nNova requisição adicionada. Fila atual:")
    print(queue_requests)


if __name__ == "__main__":
    main()
