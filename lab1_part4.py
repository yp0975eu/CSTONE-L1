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


def print_all_stops(route_json, direction):

    print("\n\t{0}".format(direction["Text"]))
    print("\tStop # : Description ")

    for route in route_json:
        print("\t{0} : {1}".format(str(route["Value"]).rjust(6), str(route["Text"]).ljust(34)))


def get_route_directions(route_num):

    data = get_json_data("http://svc.metrotransit.org/NexTrip/Directions/{0}".format(route_num))

    route_directions_json = data.json()

    return route_directions_json


# for printing all stops, and stop times in an easy to read list in the console
def print_all_stop_times(all_stop_times):

    print("\n\n\tRoute {0} - {1}".format(
        all_stop_times[0]["route"],
        all_stop_times[0]["direction"]["Text"]
        )
    )

    print("\t{0} : {1} : {2}".format(
        "Stop ID".ljust(7),
        "Description".ljust(32),
        "Times".ljust(7)
    ))

    for stop in all_stop_times:
        s = stop['stop']

        stop_time_string = ''

        for stop_times in s['stop_times']:
            stop_time_string += " " + str(stop_times['DepartureText']).ljust(7)

        print("\t{0} : {1} : {2}" .format(
                str(s['stop_info']['Value']).ljust(7),
                str(s['stop_info']['Text']).ljust(32),
                str(stop_time_string).ljust(7)
            )
        )


def get_stop_times(route, direction, stop_json):

    # new data structure to hold a list of stops and their respective stop times
    new_stop_json = []

    # looping through and getting the stop node ids for the api call
    for stop in stop_json:

        data = get_json_data("http://svc.metrotransit.org/NexTrip/{0}/{1}/{2}".format(route, direction["Value"], stop["Value"]))

        new_stop_json.append(
            {
                "route": route,
                "direction": direction,
                'stop': {
                    "stop_info": stop,
                    "stop_times": data.json()
                }
            }
        )

    return new_stop_json


def get_select_route():

    route = input("""
    Enter route
    \n\t""")

    # get route directions, needed for stop information
    directions = get_route_directions(route)

    for direction in directions:

        data = get_json_data("http://svc.metrotransit.org/NexTrip/Stops/{0}/{1}".format(route, direction["Value"]))

        route_info = data.json()

        # route_info = [
        #     {'Text': '66th St and Richfield Pkwy', 'Value': '6617'},
        #     {'Text': 'Chicago Ave and 56th St', 'Value': '56CH'}
        #     ...]
        all_stop_times = get_stop_times(route, direction, route_info)

        print_all_stop_times(all_stop_times)

        # print_all_stops(route_info, direction)


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
            print('\tgoodbye')
            exit()

        else:
            print("\tdefault exit")
            exit()

        selection = menu()
