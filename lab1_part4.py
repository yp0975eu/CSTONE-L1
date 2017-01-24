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
def get_json_data(url, options=None):

    # params

    params = {}

    # if we have options add them to  params

    if options is not None:

        params.update(options)

    # default headers

    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    try:

        # if request is successful - return request object, timeout in milliseconds

        r = requests.get(url, params=params, headers=headers, timeout=500)

        return r

    except requests.exceptions.Timeout as to:

        print("Your request timed-out.", to)

    except requests.ConnectionError as ce:

        print("There was a problem with your connection", ce)

    # catch other request errors
    except requests.RequestException as ex:

        print("An error occurred: ", ex)


def get_all_routes():
    return get_json_data("http://svc.metrotransit.org/NexTrip/Routes")


def print_all_routes(route_json):

    print("Route # : Description ")

    for route in route_json:
        print("{0} : {1}".format(str(route["Route"]).rjust(7), route["Description"]))


def get_select_route():
    pass


# used to display menu
def menu():

    selection = input("""
    Select an option from the menu:
    1. view all routes
    2. select route
    3. exit
    \n\t""")

    # if selection is not one of our options, keep trying
    while selection not in ['1', '2', '3']:
        selection = menu()

    return selection

if __name__ == "__main__":

    selection = menu()

    while True:

        if selection == '1':

            all_routes = get_all_routes()
            route_json = all_routes.json()
            print_all_routes(route_json)

        elif selection == '2':

            get_select_route()

        elif selection == '3':
            print('goodbye')
            exit()

        else:
            print("default exit")
            exit()

        selection = menu()
