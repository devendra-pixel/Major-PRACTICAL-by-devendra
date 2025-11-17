from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


parameters = dh.generate_parameters(generator=2, key_size=512, backend=default_backend())


alice_private_key = parameters.generate_private_key()
alice_public_key = alice_private_key.public_key()


bob_private_key = parameters.generate_private_key()
bob_public_key = bob_private_key.public_key()

alice_shared_key = alice_private_key.exchange(bob_public_key)


bob_shared_key = bob_private_key.exchange(alice_public_key)


print(f"Alice's Shared Secret: {alice_shared_key}")
print(f"Bob's Shared Secret:   {bob_shared_key}")

if alice_shared_key == bob_shared_key:
    print("\nSuccess! Shared keys match.")
else:
    print("\nError! Shared keys do not match.")
