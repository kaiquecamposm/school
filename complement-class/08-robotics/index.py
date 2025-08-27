import random
import time


def gen_sensors(num_tasks):
    tasks = []
    sensors = ["LIDAR", "camera", "ultrassonico"]
    priorities = ["alta", "media", "baixa"]

    for i in range(1, num_tasks + 1):
        task = {
            "id": i,
            "descricao": f"Processar dados do sensor {random.choice(sensors)}",
            "prioridade": random.choice(priorities),
        }

        tasks.append(task)

    return tasks


def add_task(queue_tasks, task):
    queue_tasks.append(task)

    return queue_tasks


def process_task(queue_tasks):
    if len(queue_tasks) > 0:
        task = queue_tasks.pop(0)
        print(
            f"Processando tarefa ID: {task['id']}, Descrição: {task['descricao']}, Prioridade: {task['prioridade']}"
        )
        time.sleep(1)
    else:
        print("Nenhuma tarefa para processar.")
    return queue_tasks


def main():
    num_initial_tasks = 5
    queue_tasks = gen_sensors(num_initial_tasks)
    print("Fila inicial de tarefas:")
    for task in queue_tasks:
        print(task)

    print("\nProcessamento das tarefas em tempo real:")
    while queue_tasks:
        queue_tasks = process_task(queue_tasks)

    new_task = {
        "id": num_initial_tasks + 1,
        "description": "Processar dados do sensor GPS",
        "prioridade": "alta",
    }
    queue_tasks = add_task(queue_tasks, new_task)
    print("\nNova tarefa adicionada. Fila atual:")
    print(queue_tasks)


if __name__ == "__main__":
    main()
