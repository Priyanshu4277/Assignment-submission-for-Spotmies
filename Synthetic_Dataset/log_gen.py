import random
import time

ACCOUNT_ID = "123456789"
REGION_INTERNAL_IPS = ["10.0.0.", "10.0.1.", "10.0.2."]
EXTERNAL_IPS = [
    "52.95.110.1",     # AWS service
    "8.8.8.8",         # DNS
    "203.0.113.5",     # Public test IP
    "198.51.100.10"    # Public test IP
]

COMMON_PORTS = [22, 80, 443, 3389, 53]
PROTOCOLS = {
    "TCP": 6,
    "UDP": 17
}

def generate_flow_log():
    version = 2
    account_id = ACCOUNT_ID
    eni = f"eni-{random.randint(100,999)}"

    srcaddr = random.choice(REGION_INTERNAL_IPS) + str(random.randint(1, 254))
    dstaddr = random.choice(EXTERNAL_IPS)

    dstport = random.choice(COMMON_PORTS)
    srcport = random.randint(1024, 65535)

    protocol = random.choice(list(PROTOCOLS.values()))

    packets = random.randint(1, 500)
    bytes_transferred = packets * random.randint(40, 1500)

    start = int(time.time())
    end = start + random.randint(30, 120)

    # Inject realistic ACCEPT / REJECT behavior
    action = random.choices(
        ["ACCEPT", "REJECT"],
        weights=[85, 15]
    )[0]

    log_status = "OK"

    return f"{version} {account_id} {eni} {srcaddr} {dstaddr} " \
           f"{dstport} {srcport} {protocol} {packets} {bytes_transferred} " \
           f"{start} {end} {action} {log_status}"

def generate_logs(count=1000, output_file="vpc_flow_logs.log"):
    with open(output_file, "w") as f:
        for _ in range(count):
            f.write(generate_flow_log() + "\n")

    print(f"[+] Generated {count} synthetic VPC Flow Logs -> {output_file}")


if __name__ == "__main__":
    generate_logs(count=1000)
