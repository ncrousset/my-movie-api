class WithOutCategoryError(Exception):
    def __init__(self):
        self.message = "Movie must have at least one category"
