from project.auth import app
import threading
import time
import multiprocessing


# 每隔10秒钟执行


if __name__ == '__main__':
    app.run(port=5050,debug=True)

    
