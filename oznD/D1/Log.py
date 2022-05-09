import datetime
class Log:
    def __init__(self, key, comment):
        log_file = open("log.txt","a")
        log_file.write(f"{key}---{str(datetime.datetime.now())[:-7]}---{comment}\n")
        log_file.close()
    def clear():
        log_file = open("log.txt","w+")
        log_file.close()
