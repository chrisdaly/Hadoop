def reducer():
"""
Takes sorted key-value pairs from the mapper in the form of "address\twebsite". Counts 
the number of hits for each website.
"""
    import sys

    # Initialize the max key and hits.
    maxKey = None
    hitsMax = 0

    # Initialize the current key and hits.
    oldKey = 0
    hits = 0

    # Loop through the input, stripping white space and splitting on a tab.
    for line in sys.stdin:
        data = line.strip().split()

        # Ensure that the parsed data only continues one value.
        if len(data) != 1:
            # Something has gone wrong. Skip this line.
            continue

        # Assign the parsed data to values.
        thisKey = data
        # When a new key is found check if the old key should be the max.
        if oldKey != thisKey:

          # If so, update the max values.
          if hits >= hitsMax:
            maxKey = oldKey
            hitsMax = hits
            
          # Update the new key and reset the old values.
          hits = 0

        # Increment the hits.
        hits += 1
        oldKey = thisKey;

    print "%s\t%s" %(maxKey, hitsMax)

test_text = """A
A
A
A
A
B
B
C
C
C
D"""

# This function allows you to test the mapper with the provided test string
def main():
  import StringIO
  sys.stdin = StringIO.StringIO(test_text)
  reducer()
  sys.stdin = sys.__stdin__

main()