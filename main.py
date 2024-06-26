import requests
import config

def send_line_notify(message, token, image_url=None, image_path=None, sticker_package_id=None, sticker_id=None):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }
    data = {
        "message": message if message else " "  # 確保message參數不為空
    }
    files = None

    if image_url:
        data["imageThumbnail"] = image_url
        data["imageFullsize"] = image_url
    elif image_path:
        files = {"imageFile": open(image_path, "rb")}
    
    if sticker_package_id and sticker_id:
        data["stickerPackageId"] = sticker_package_id
        data["stickerId"] = sticker_id

    response = requests.post(url, headers=headers, data=data, files=files)
    
    if files:
        files["imageFile"].close()  # 關閉文件
    
    return response.status_code

if __name__ == "__main__":
    token = config.token

    # 1. 發送文字
    message = "Hello, this is a test message!"
    status_code = send_line_notify(message, token)
    if status_code == 200:
        print("Text message sent successfully!")
    else:
        print(f"Failed to send text message. Status code: {status_code}")

    # 2. 發送圖片
    image_url = "https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2023/03/28/0/20888602.jpg&x=0&y=0&sw=0&sh=0&exp=3600&sl=W&fw=800&nt=1"  # 替換成你的圖片URL  
    status_code = send_line_notify("", token, image_url=image_url)
    if status_code == 200:
        print("Image sent successfully!")
    else:
        print(f"Failed to send image. Status code: {status_code}")
    
    # 3. 發送貼圖
    sticker_package_id = 11537  # 替換成你要使用的貼圖包ID
    sticker_id = 52002753  # 替換成你要使用的貼圖ID
    status_code = send_line_notify("", token, sticker_package_id=sticker_package_id, sticker_id=sticker_id)
    if status_code == 200:
        print("Sticker sent successfully!")
    else:
        print(f"Failed to send sticker. Status code: {status_code}")
