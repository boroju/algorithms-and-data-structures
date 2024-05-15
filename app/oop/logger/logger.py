from abc import ABC, abstractmethod
import json


# Logger Interface (Abstract Base Class):
# Define an abstract base class Logger that will serve as the interface for all logger implementations.
# This class will declare abstract methods for logging messages at different levels and in different formats.

class LoggerBase(ABC):
    @abstractmethod
    def debug(self, message):
        pass

    @abstractmethod
    def info(self, message):
        pass

    @abstractmethod
    def error(self, message):
        pass


# Concrete Logger Implementations: Create concrete logger classes for each combination of format and writer.
# For example, ConsoleJsonLogger, FileXmlLogger, etc. Each concrete logger will implement the methods defined in the Logger interface.
class ConsoleLogger(LoggerBase):
    def debug(self, message):
        self._log("DEBUG", message)

    def info(self, message):
        self._log("INFO", message)

    def error(self, message):
        self._log("ERROR", message)

    def _log(self, level, message):
        print(f"[{level}] {message}")


class FileXmlLogger(LoggerBase):
    def __init__(self, filename):
        self._filename = filename

    def debug(self, message):
        self._log("DEBUG", message)

    def info(self, message):
        self._log("INFO", message)

    def error(self, message):
        self._log("ERROR", message)

    def _log(self, level, message):
        with open(self._filename, 'a') as file:
            file.write(f"<{level}>{message}</{level}>\n")


class FileJsonLogger(LoggerBase):
    def __init__(self, filename):
        self._filename = filename

    def debug(self, message):
        self._log("DEBUG", message)

    def info(self, message):
        self._log("INFO", message)

    def error(self, message):
        self._log("ERROR", message)

    def _log(self, level, message):
        log_entry = {"level": level, "message": message}
        with open(self._filename, 'a') as file:
            file.write(json.dumps(log_entry) + '\n')


# Usage
if __name__ == "__main__":
    console_logger = ConsoleLogger()
    console_logger.debug("Debug message")
    console_logger.info("Info message")
    console_logger.error("Error message")

    xml_logger = FileXmlLogger("log.xml")
    xml_logger.debug("Debug message")
    xml_logger.info("Info message")
    xml_logger.error("Error message")

    json_logger = FileJsonLogger("log.json")
    json_logger.debug("Debug message")
    json_logger.info("Info message")
    json_logger.error("Error message")

