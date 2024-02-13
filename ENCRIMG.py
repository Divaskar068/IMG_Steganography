from PIL import Image
import time

def encrypt_image(key, image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    width, height = image.size

    # Create a new image for the encrypted pixels
    encrypted_image = Image.new("RGB", (width, height))

    # Encrypt each pixel
    for y in range(height):
        for x in range(width):
            # Get the pixel value
            pixel = image.getpixel((x, y))

            # XOR each channel value with the corresponding key value
            encrypted_pixel = tuple(channel ^ key for channel in pixel)

            # Set the encrypted pixel value
            encrypted_image.putpixel((x, y), encrypted_pixel)

    # Save the encrypted image
    encrypted_image.save(output_path)

def decrypt_image(key, encrypted_image_path, output_path):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    width, height = encrypted_image.size

    # Create a new image for the decrypted pixels
    decrypted_image = Image.new("RGB", (width, height))

    # Decrypt each pixel
    for y in range(height):
        for x in range(width):
            # Get the encrypted pixel value
            encrypted_pixel = encrypted_image.getpixel((x, y))

            # XOR each channel value with the corresponding key value
            decrypted_pixel = tuple(channel ^ key for channel in encrypted_pixel)

            # Set the decrypted pixel value
            decrypted_image.putpixel((x, y), decrypted_pixel)

    # Save the decrypted image
    decrypted_image.save(output_path)

# Example usage
key = 123  # Replace with your desired key
input_image_path = "crybg.png"  # Replace with the path to your input image
encrypted_image_path = "encrypted_image.png"
decrypted_image_path = "decrypted_image.png"

# Encrypt the image
encrypt_image(key, input_image_path, encrypted_image_path)
print("Image encrypted successfully!")

# Decrypt the image
decrypt_image(key, encrypted_image_path, decrypted_image_path)
decryption_time = time.time() - start_time
print("Image decrypted successfully!")
