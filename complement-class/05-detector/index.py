import random


def generate_data_detector(temps):
  data_detector = [round(random.uniform(15.0, 35.0), 2) for _ in range(temps)]
  return data_detector

def higher_temps_filter(data_detector, limit=30.0):
  higher_temps = [temp for temp in data_detector if temp > limit]
  return higher_temps

def insert_data_detector(data_detector, new_temp, position=None):
  if position in None or position >= len(data_detector):
    data_detector.append(new_temp)
  return data_detector

def remove_abnormal_temps(data_detector, lower_limit=15.0, higher_limit=35.0):
  data = [temp for temp in data_detector if lower_limit <= temp <= higher_limit]
  return data

def main():
  temps = 10000
  data = generate_data_detector(temps)

  print(f"Quantidade de leituras geradas: {len(data)}")

  higher_temps = higher_temps_filter(data)
  print(f"Quantidade de leituras acima de 30°C: {len(higher_temps)}")

  clean_data = remove_abnormal_temps(data)
  print(f"Qauntidade de leituras após remoção de anomálias: {len(clean_data)}")


main()