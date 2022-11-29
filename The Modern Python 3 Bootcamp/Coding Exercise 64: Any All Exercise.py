# Implement your is_all_strings function below:
def is_all_strings(mag):
    return all(isinstance(i, str) for i in mag)
