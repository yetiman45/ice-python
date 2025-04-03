import stun

def get_public_ip():
    nat_type, external_ip, external_port = stun.get_ip_info()
    return nat_type, external_ip, external_port
