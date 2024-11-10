import urllib.request
import os


def download_images(urls, canhcua, save_as_prefix):
    # Create the folder if it doesn't exist
    os.makedirs(canhcua, exist_ok=True)

    for i, url in enumerate(urls):
        save_as = os.path.join(canhcua, f"{save_as_prefix}_{i + 1}.jpg")
        try:
            urllib.request.urlretrieve(url, save_as)
            print(f"Downloaded {save_as}")
        except urllib.error.HTTPError as e:
            print(f"Failed to download {url}: {e}")


# Example usage:
image_urls = []
folder_path = ''
save_as_prefix = 'image'

download_images(image_urls, folder_path, save_as_prefix)
