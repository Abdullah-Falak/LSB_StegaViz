import cv2
import numpy as np

def hide_image(cover_path, secret_path, output_path):
    """Handles the bitwise math to hide a secret image inside a cover image."""
    try:
        cover = cv2.imread(cover_path)
        secret = cv2.imread(secret_path)

        if cover is None or secret is None:
            return False, "Could not read one or both images."

        # Resize secret image to match the exact dimensions of the cover image
        secret = cv2.resize(secret, (cover.shape[1], cover.shape[0]))

        # --- THE LSB MATH ---
        cover_cleared = cv2.bitwise_and(cover, 240)
        secret_shifted = cv2.bitwise_and(secret, 240) >> 4
        stego_image = cv2.bitwise_or(cover_cleared, secret_shifted)

        # Save the final image
        cv2.imwrite(output_path, stego_image)
        return True, f"Stego-image saved successfully to:\n{output_path}"
        
    except Exception as e:
        return False, f"An error occurred during hiding:\n{str(e)}"


def extract_image(stego_path, output_path):
    """Handles the bitwise math to extract a secret image from a stego image."""
    try:
        stego = cv2.imread(stego_path)

        if stego is None:
            return False, "Could not read the stego image."

        # --- THE LSB MATH ---
        extracted = cv2.bitwise_and(stego, 15) << 4

        # Save the extracted secret image
        cv2.imwrite(output_path, extracted)
        return True, f"Extracted secret saved successfully to:\n{output_path}"
        
    except Exception as e:
        return False, f"An error occurred during extraction:\n{str(e)}"
