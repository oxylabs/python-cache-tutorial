# Import the required modules
import time
import requests


# Function to get the HTML Content
def get_html_data(url):
    response = requests.get(url)
    return response.text


# Memoize function to cache the data
def memoize(func):
    cache = {}

    # Inner wrapper function to store the data in the cache
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


# Memoized function to get the HTML Content
@memoize
def get_html_data_cached(url):
    response = requests.get(url)
    return response.text


# Get the time it took for a normal function
start_time = time.time()
get_html_data('https://books.toscrape.com/')
print('Time taken (normal function):', time.time() - start_time)

# Get the time it took for a memoized function (manual decorator)
start_time = time.time()
get_html_data_cached('https://books.toscrape.com/')
print('Time taken (memoized function using manual decorator):', time.time() - start_time)