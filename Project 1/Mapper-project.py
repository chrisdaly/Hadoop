def mapper():
"""
Takes in anonymized Web server log files in the form of "address identity username
date timezone request status size". It then strips and splits the data and checks to see if 
there are six items before parsing the data and printing the output in the
form of "address".
"""

    import sys

    # Loop through the input splitting on white space.
    for line in sys.stdin:
        data = line.strip().split()

        # Ensure that the parsed data only continues ten values.
        if len(data) == 10:

            # Parse the data into its components.
            ip, id, user, datetime, timezone, method, path, proto, status, size = data

            # Strips out the redundant part of URL if present.
            if path[:17]=='http://www.the-as':
                path = path[31:]

            # Print out the data that will be passed to the reducer.
            print path



            #['/assets/css/combined.css']  117352
