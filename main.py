import requests

def send_line_notify(message, token, image_url=None, sticker_package_id=None, sticker_id=None):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }
    data = {
        "message": message
    }
    if image_url:
        data["imageThumbnail"] = image_url
        data["imageFullsize"] = image_url

    if sticker_package_id and sticker_id:
        data["stickerPackageId"] = sticker_package_id
        data["stickerId"] = sticker_id

    response = requests.post(url, headers=headers, data=data)
    return response.status_code


if __name__ == "__main__":
    token = "LXFuuXKMM3BLyxCY9z0k5iPavVhZanycLSJE2dOLwDz"  # 替換成你的LINE Notify Token
    message = "Hello, this is a test message with an image and a sticker!"
    image_url = "https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2023/03/28/0/20888602.jpg&x=0&y=0&sw=0&sh=0&exp=3600&sl=W&fw=800&nt=1"  # 替換成你的圖片URL  
    sticker_package_id = 11537  # 替換成你要使用的貼圖包ID
    sticker_id = 52002753  # 替換成你要使用的貼圖ID


    status_code = send_line_notify(message, token)
    status_code = send_line_notify("", token, image_url=image_url)
    status_code = send_line_notify("", token, sticker_package_id=sticker_package_id, sticker_id=sticker_id)   
    
    if status_code == 200:
        print("Notification sent successfully with image!")
    else:
        print("Failed to send notification. Status code:", status_code)
