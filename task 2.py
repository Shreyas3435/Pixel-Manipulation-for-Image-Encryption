from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)

    # Encrypt the image by adding the key to each pixel value
    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))

    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)

    # Decrypt the image by subtracting the key from each pixel value
    decrypted_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))

    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    print("Image Encryption Tool")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? ")

    if choice.lower() == 'e':
        image_path = input("Enter the path to the image to encrypt: ")
        output_path = input("Enter the path to save the encrypted image: ")
        key = int(input("Enter the encryption key (integer): "))
        encrypt_image(image_path, output_path, key)
    elif choice.lower() == 'd':
        image_path = input("Enter the path to the image to decrypt: ")
        output_path = input("Enter the path to save the decrypted image: ")
        key = int(input("Enter the decryption key (integer): "))
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
