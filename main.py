from app import createApp
from datetime import datetime, timedelta

app = createApp()

if __name__ == '__main__':
    app.run(port=8080,debug=True)