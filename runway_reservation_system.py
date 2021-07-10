import datetime


# Datetime python lib useful for this mini project
# https://docs.python.org/3/library/datetime.html

# This class represents a node in the BST.
class runway_bst(object):
    def __init__(root, start_time=None, end_time=None, flight_number=None):
        root.start_time = start_time  # Flight start time
        root.end_time = end_time  # Flight end time
        root.flight_number = flight_number  # flight no
        # Left and right child
        root.left = None  # left node in flight tree
        root.right = None  # right node in flight tree

    # Implement the insert method in here.
    # For the node key value comparison, consider start_time of every node
    # consider the boundary case where root is not available
    # remove pass keyword and implement the method
    def insert(root, start_time=None, end_time=None, flight_number=None):
        # check whether given interval is valid or not
        if root.valid_interval(start_time, end_time):
            # check runway is busy or not and accordingly insert node in the flight runway tree
            root.busy_runway(start_time, end_time, flight_number)
        else:
            # Message to user that diff between interval should be half and hour
            print("Please provide a half an hour interval, in 24 Hour clock military format.")

    # insert the flight node in the flight runway tree
    def insertNode(root, start_time=None, end_time=None, flight_number=None):
        # datetime strptime to convert string to Date object.
        request_start_time = datetime.datetime.strptime(start_time, "%H:%M")
        root_start_time = datetime.datetime.strptime(root.start_time, "%H:%M")

        # checking start time less than root
        # if less then insert node at left side
        if request_start_time < root_start_time:
            # if left node is empty then add flight node at left side
            if root.left is None:
                # create new flight node
                root.left = runway_bst(start_time, end_time, flight_number)
                # print the message to user about reservation is made for flight
                print(f"Runway reservation made for flight number {flight_number} from {start_time} to {end_time}")
            else:
                # recursive call to check where to insert node
                root.insertNode(start_time, end_time, flight_number)
        # if more then root then insert node at right side
        elif request_start_time > root_start_time:
            # if right node is empty then add flight node at right side
            if root.right is None:
                # create new flight node
                root.right = runway_bst(start_time, end_time, flight_number)
                # print the message to user about reservation is made for flight
                print(f"Runway reservation made for flight number {flight_number} from {start_time} to {end_time}")
            else:
                # recursive call to check where to insert node
                root.insertNode(start_time, end_time, flight_number)

    # This method validates the interval duration to be 30 mins exact.
    # You need to use datetime strptime to convert string to Date object.
    # And then perform comparisons on datetime objects.
    def valid_interval(root, start_time, end_time):
        # datetime strptime to convert string to Date object.
        request_start_time = datetime.datetime.strptime(start_time, "%H:%M")
        request_end_time = datetime.datetime.strptime(end_time, "%H:%M")

        # checking the interval time of a flight
        tdelta = request_end_time - request_start_time
        # check the time interval is 30 or not and accordingly return the status
        if int(tdelta.total_seconds() / 60) == 30:
            return True
        else:
            return False

    # This method will check if the given time slot is available and no other flight is scheduled
    # remove the pass keyword and implement the logic in this method
    # This method checks if the requested interval overlaps any existing interval.
    # This returns the list [root.flight_number, root.start_time, root.end_time] of scheduled flight
    # if an overlap is found. Returns None otherwise.
    # You need to use datetime strptime to convert string to Date object.
    # And then perform comparisons on datetime objects.

    def busy_runway(root, start_time, end_time, flight_number):
        # datetime strptime to convert string to Date object
        request_start_time = datetime.datetime.strptime(start_time, "%H:%M")
        request_end_time = datetime.datetime.strptime(end_time, "%H:%M")

        # datetime strptime to convert string to Date object for root timings
        root_start_time = datetime.datetime.strptime(root.start_time, "%H:%M")
        root_end_time = datetime.datetime.strptime(root.end_time, "%H:%M")

        # checking request end time should be less than root start time to insert node at left side
        if request_end_time < root_start_time:
            # if left of root is none then insert node at left side
            if root.left is None:
                root.insertNode(start_time, end_time, flight_number)  # insert node
            else:
                # recursive call to check where to insert node
                root.left.busy_runway(start_time, end_time, flight_number)
        # checking root end time should be less than request start time to insert node at right side
        elif root_end_time < request_start_time:
            # if right of root is none then insert node at left side
            if root.right is None:
                root.insertNode(start_time, end_time, flight_number)
            else:
                # recursive call to check where to insert node
                root.right.busy_runway(start_time, end_time, flight_number)
        else:
            # message to user to tell runways status is already booked
            print(f"Runway is booked during: {start_time} to {end_time}")

    # This method will have logical implementation to make the reservation for a particular flight
    # Before booking the reservation it will validate if the slot is getting booked for 30 minutes only
    # It will also check if the no other flight is scheduled over the runway during that time
    # remove pass keyword and write the logic
    # Driver method which makes the reservation and calls all the helper methods.
    def make_reservation(root, flight_start_time, flight_end_time, flight_number):
        # Check the runways status and book reservation according to it
        root.insert(flight_start_time, flight_end_time, flight_number)

    # traverse flight tree using inorder travarsal
    def inorder(root, vals):
        # Check status of root left and Print root of left
        if root.left is not None:
            root.left.inorder(vals)
        # Check status of root start time and Print root start time
        if root.start_time is not None:
            vals.append(root.start_time)
        # Check status of root right and Print root of right
        if root.right is not None:
            root.right.inorder(vals)
        return vals


if __name__ == '__main__':
    # Root node of BST
    test = runway_bst('11:00', '11:30', 'GOI9872')
    # make reservation for flight
    test.make_reservation('11:35', '12:05', 'JET9874')
    # make reservation for flight
    test.make_reservation('12:30', '13:00', 'JET9243')

    # Following case should fail. Runway is busy
    # make reservation for flight
    test.make_reservation('10:45', '11:15', 'VIS9000')
    # make reservation for flight
    test.make_reservation('12:45', '13:15', 'IND3360')
    # make reservation for flight
    test.make_reservation('13:45', '14:45', 'IND3361')

    # New booking. Should pass
    # make reservation for flight
    test.make_reservation('10:10', '10:40', 'JET9243')
    # make reservation for flight
    test.make_reservation('09:30', '10:00', 'AIR2781')

    # verfiying if the data inserted is BST or not
    res = []
    res = test.inorder(res)
    # print all start time of flight
    print(res)
