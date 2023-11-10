import hashlib
import uuid
import os

def get_machine_id():
    # Bilgisayarın MAC adresini al
    mac = ':'.join(['{:02x}'.format(b) for b in uuid.getnode().to_bytes(6, 'big')])
    return mac

def hash_machine_id():
    # Bilgisayarın MAC adresini SHA-256 ile hashle
    machine_id = get_machine_id()
    return hashlib.sha256(machine_id.encode()).hexdigest()

def main():
    # Kayıtlı bilgisayarın benzersiz kimliğini al
    registered_machine_id = "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"

    # Anlık bilgisayarın kimliğini al
    current_machine_id = hash_machine_id()

    # Kimlikleri karşılaştır
    if current_machine_id != registered_machine_id:
        print(registered_machine_id)
        print(current_machine_id)
        print("Programı kullanabilirsiniz.")
    else:
        print("Bu bilgisayarda program kullanılamaz.")

if __name__ == "__main__":
    main()
