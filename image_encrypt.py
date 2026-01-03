from PIL import Image
import os

def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    image.save(output_path)
    print("✅ Image encrypted successfully!")


def decrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    image.save(output_path)
    print("✅ Image decrypted successfully!")


# ---------------- MAIN PROGRAM ----------------

print("🔐 Image Encryption Tool 🔐")

choice = input("Type encrypt or decrypt: ").strip().lower()
image_name = input("Enter image file name (with extension): ").strip()
key = int(input("Enter secret key (number): "))

if not os.path.exists(image_name):
    print("❌ Image file not found. Please check the file name.")
    exit()

if choice == "encrypt":
    encrypt_image(image_name, key, "encrypted.png")

elif choice == "decrypt":
    encrypt_check = image_name
    decrypt_image(encrypt_check, key, "decrypted.png")

else:
    print("❌ Invalid choice. Please type encrypt or decrypt.")
