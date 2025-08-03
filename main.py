import asyncio
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes

async def fetch_server_random_number():
    await asyncio.sleep(1)  # Wait for 1 second
    return get_random_bytes(16)  # Return 16 random bytes


async def main():
    # Gets the relevant parameters for the key derivation function
    client_random_number = get_random_bytes(16)
    server_random_number = await fetch_server_random_number()
    premaster_secret = b'my_premaster_secret'

    # Combine the random numbers and the pre-master secret
    combined_secret = client_random_number + server_random_number + premaster_secret

    salt = get_random_bytes(16)  # Derive keys using PBKDF2
    session_key = PBKDF2(combined_secret, salt, 64, count=1000000, hmac_hash_module=SHA512)

    print("Session Key:", session_key.hex())  # prints session key as a hex value

asyncio.run(main())  # runs main script
