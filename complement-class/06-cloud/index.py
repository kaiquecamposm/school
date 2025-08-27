import random
from datetime import datetime, timedelta


def generate_registers(num_registers, start_date, temp_interval):
    registers = []
    current_time = start_date

    for i in range(1, num_registers + 1):
        registers.append(
            {
                "id": i,
                "timestamp": start_date,
                "value": round(random.uniform(10.0, 500.0), 2),
                "id_dispositivo": random.choice(
                    ["disp_001", "disp_002", "disp_003", "disp_004"]
                ),
            }
        )
        current_time += timedelta(seconds=temp_interval)

    return registers


def registers_for_value_filter(registers, min_value):
    filtered_registers = [
        register for register in registers if register["value"] >= min_value
    ]

    return filtered_registers


def add_register(registers, new_register, position=None):
    if position is None or position >= len(registers):
        registers.append(new_register)
    else:
        registers.insert(position, new_register)
    return registers


def remove_prev_registers(registers, limit):
    updated_registers = [
        register for register in registers if limit <= register["timestamp"]
    ]

    return updated_registers


def main():
    start = datetime.now()
    num_registers = 50
    temp_interval = 30

    registers = generate_registers(num_registers, start, temp_interval)

    print("Exibindo os primeiros 5 registros gerados:")

    for register in registers[:5]:
        print(
            f"ID: {register['id']} | Timestamp: {register['timestamp']} | Valor: {register['value']} | Dispositivo: {register['id_dispositivo']}"
        )

    new_register = {
        "id": len(registers) + 1,
        "timestamp": registers[-1]["timestamp"] + timedelta(seconds=temp_interval),
        "value": round(random.uniform(10.0, 500.0), 2),
        "id_dispositivo": "disp_005",
    }

    registers = add_register(registers, new_register)
    print(
        f"\nNovo registro inserido: ID: {register['id']} | Timestamp: {register['timestamp']} | Valor: {register['value']} | Dispositivo: {register['id_dispositivo']}"
    )
    print(f"Total de registros após inserção: {len(registers)}")

    limit = start + timedelta(minutes=2)
    updated_registers = remove_prev_registers(registers, limit)
    print(
        f"\nQuantidade de registros apís remoção dos antigos (antes de {limit}): {len(updated_registers)}"
    )


if __name__ == "__main__":
    main()
