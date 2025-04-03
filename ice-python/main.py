from ice_agent import gather_candidates, establish_connection
from signaling import exchange_candidates

if __name__ == "__main__":
    local_candidates = gather_candidates()
    peer_candidates = exchange_candidates(local_candidates)
    connection = establish_connection(peer_candidates)
    if connection:
        connection.sendto(b"Hello", peer_candidates[0])
