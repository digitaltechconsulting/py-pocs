class Logger:
    def LogInfo(self,message):
        print(message)
    def LogWarning(self, message):
        print(message);
    def LogError(self,message):
        print(message)
        


if __name__ == "__main__":
    logger = Logger();
    logger.LogInfo("This is test info message")
    logger.LogWarning("This is test warning message")
    logger.LogError("This is test error message")