from texttable import Texttable

def display_table():
    # Create an instance of Texttable
    text = Texttable()
    
    # Add columns with headers
    text.add_row(['Name', 'Age', 'City'])
    
    # Add data to the table
    text.add_row(['Alice', 30, 'New York'])
    text.add_row(['Bob', 25, 'Los Angeles'])
    text.add_row(['Charlie', 35, 'Chicago'])
    
    # Print the formatted table
    print(text.draw())