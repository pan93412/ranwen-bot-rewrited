class DeveloperError(Exception):
    reason: str
    where: str

    def __init__(self, reason: str, where: str = "somewhere"):
        self.reason = reason
        self.where = where

    def __str__(self):
        return f"in {self.where}: {self.reason}"
