# Line Notify 通知機器人

這是一個使用 Line Notify API 的通知機器人，您可以使用它來發送消息到您的 Line 群組或個人聊天室。此專案提供了一個簡單且易於使用的介面來與 Line Notify 進行互動。

## 功能特點

- **簡單易用**：輕鬆發送通知到 Line。
- **自動化**：可用於自動化系統通知。
- **靈活配置**：支援自訂消息內容。

## 安裝

請按照以下步驟安裝並配置此專案：

1. 下載這個專案到你的本地環境：

    ```bash
    git clone https://github.com/your-username/line-notify-bot.git
    ```

2. 進入專案目錄：

    ```bash
    cd line-notify-bot
    ```

3. 安裝所需的依賴項：

    ```bash
    pip install -r requirements.txt
    ```

## 使用方法

1. 取得 Line Notify Token

    前往 [Line Notify 官網](https://notify-bot.line.me/en/) 取得您的個人或群組的 Token。

2. 設置環境變數

    修改config.test為config文件，並將您的 Token 設置為環境變數 `LINE_NOTIFY_TOKEN`：

    ```bash
     token = "YOUR_LINE_NOTIFY_TOKEN"
    ```
    
3. 發送通知

    使用以下命令發送通知：

    ```bash
    python Line_Notify.py
    ```

![LineBot](https://github.com/fwtutu/line-notify/assets/171393477/1dd68b02-e659-4eb4-999f-0e5cf600061c)

