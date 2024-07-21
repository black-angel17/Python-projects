import clipboard
import instaloader
# Get the clipboard contents
def downlaoder(x):
    url = x

    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Download the video
    try:
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
        loader.download_post(post, target="#directory_path#")
        print("Video downloaded successfully.")
    except Exception as e:
        print("Failed to download video:", str(e))


checker = ''
while True:
    clipboard_text = clipboard.paste()

    if checker == clipboard_text:
        continue
    else:
        downlaoder(clipboard_text)
        checker = clipboard_text


