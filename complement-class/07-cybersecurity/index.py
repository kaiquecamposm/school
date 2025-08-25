from datetime import datetime, timedelta

import numpy as np


def gen_logs_array_access(nums_logs, start_date, seconds_interval):
  dtype = np.dtype([
    ('timestamp', 'datetime64[ns]'),
    ('ip', 'U15'),
    ('user', 'U20'),
    ('status', 'U7')
  ])

  registers = np.empty(nums_logs, dtype)

  ips_list = np.array(["192.168.1.1", "192.168.1.2", "192.168.1.3", "10.0.0.1", "10.0.0.2"])
  users_list = np.array(["user_a", "user_b", "user_c", "user_d"])
  status_list = np.array(["success", "fail"])
  weights_status = np.array([0.8, 0.2])

  current_time = start_date

  for idx in range(nums_logs):
    registers[idx] = (
      np.datetime64(seconds_interval, 'ns'),
      np.random.choice(ips_list),
      np.random.choice(users_list),
      np.random.choice(status_list, p=weights_status) 
    )
    current_time += timedelta(seconds=seconds_interval)

    return registers

def suspect_ips_detector(registers, threshold_failures):
  mask_fails = registers["status"] == "fail"
  fails_ips = registers["ip"][mask_fails]
  unique_ips, counts = np.unique(fails_ips, return_counts=True)

  return unique_ips[counts >= threshold_failures]

def insert_log(registers, new_log):
  dtype = registers.dtype
  register_np = np.array(
    (
      np.datetime64(new_log["timestamp"], "ns"),
      new_log["ip"],
      new_log["user"],
      new_log["status"]
    ),
    dtype
  )

  return np.append(registers, register_np)

def main():
  start_date = datetime.now()
  num_logs = 100
  seconds_interval = 30
  registers = gen_logs_array_access(num_logs, start_date, seconds_interval)

  print("Primeiros cinco logs:\n")
  for log in registers[:5]:
    ts = log["timestamp"].astype("datetime64[ms]").astype(datetime)
    print(f"Timestamp: {ts} | IP: {log['ip']} | Usuario: {log['user']} | Status: {log['status']}")

    new_ts = registers[-1]['timestamp'] + np.timedelta64(seconds_interval, 's')
    new_log = {
      'timestamp': new_ts,
      'ip': '192.168.1.99',
      'user': 'new_user',
      'status': 'fail'
    }
    registers = insert_log(registers, new_log)

    print("\nNovo log inserido:\n")
    new_ts = new_log['timestamp'].astype('datetime64[ms]').astype(datetime)
    print(f"Timestamp: {new_ts} | IP: {new_log['ip']} | Usuario: {new_log['user']} | Status: {new_log['status']}")
    print(f"Total de log apos a insercao {len(registers)}")

if __name__ == "__main__":
  main()