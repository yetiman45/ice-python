import socket
from stun_client import get_public_ip

def gather_candidates():
    local_ip = socket.gethostbyname(socket.gethostname())
    nat_type, public_ip, public_port = get_public_ip()
    return {
        "local": (local_ip, 5000),
        "stun": (public_ip, public_port)
    }

def establish_connection(peer_candidates):
    for candidate in peer_candidates:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(b"ICE Probe", candidate)
            sock.settimeout(2)
            data, addr = sock.recvfrom(1024)
            if data:
                print(f"Connection established with {addr}")
                return sock
        except Exception:
            continue
    return None
