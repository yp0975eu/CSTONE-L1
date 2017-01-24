# Write a program that fetches data from a web server using an open API.
#  Ask me for the server you should use and the specific data you should fetch.

# You'll need to do some research into how to carry out these tasks in Python. (Hint: the requests library)

# Your Python program will make a request to the website, and get data as JSON.
#  You'll need to process this to extract the data you need.

# You should handle errors, such as access denied, no network connection, invalid response....

# Extra challenge: your program should cache data locally to avoid excessive requests.
# If the user has made a request recently, your program should fetch the data from the cache instead of the website.
import requests


# basic request code from borrowed http://docs.python-requests.org/en/master/user/quickstart/
def get_json_data():

    try:

        # if request is successful - return request object, timeout in milliseconds
        r = requests.get("http://svc.metrotransit.org/", timeout=500)

        return r

    except requests.exceptions.Timeout as to:

        print("Your request timed-out.", to)

    except requests.ConnectionError as ce:

        print("There was a problem with your connection", ce)

    # catch other request errors
    except requests.RequestException as ex:

        print("An error occurred: ", ex)


def get_all_routes():
    pass


def get_select_route():
    pass


# used to display menu
def menu():

    selection = input("""Select an option from the menu:
    1. view all routes
    2. select route
    3. exit
    \n """)

    return selection

if __name__ == "__main__":

    selection = menu()

    # if selection is not one of our options, keep trying
    while selection not in ['1', '2', '3']:
        selection = menu()

    if selection == '1':

        get_all_routes()

    elif selection == '2':

        get_select_route()

    elif selection == '3':
        print('goodbye')
        exit()
    else:
        print("default exit")
        exit()
