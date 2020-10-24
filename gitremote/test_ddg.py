import pytest
import requests


url_ddg = 'https://api.duckduckgo.com/?q=presidents%20of%20the%20united%20states&format=json&pretty=1%22'
response = requests.get(url_ddg).json()
# parse the response and put it into responseList
#  list of president name is taken from the response
list_from_response = [response]
# All the 45 presidents are listed in the above array
president_names_list = [
    "George Washington"
    "John Adams"
    "Thomas Jefferson"
    "James Madison"
    "James Monroe"
    "John Quincy Adams"
    "Andrew Jackson"
    "Martin Van Buren"
    "William Henry Harrison"
    "John Tyler"
    "James K. Polk"
    "Zachary Taylor"
    "Millard Fillmore"
    "Franklin Pierce"
    "James Buchanan"
    "Abraham Lincoln"
    "Andrew Johnson"
    "Ulysses S. Grant"
    "Rutherford B. Hayes" 
    "James Garfield"
    "Rutherford B. Hayes" 
    "Rutherford B. Hayes" 
    "Benjamin Harrison " 
    "Grover Cleveland"  
    "William McKinley" 
    "Theodore Roosevelt"  
    "William Howard Taft" 
    "Woodrow Wilson" 
    "Warren G. Harding"  
    "Calvin Coolidge"
    "Herbert Hoover"
    "Franklin D. Roosevelt"
    "Harry S. Truman"
    "Dwight D. Eisenhower"
    "John F. Kennedy"
    "Lyndon B. Johnson"
    "Richard M. Nixon"
    "Gerald R. Ford"
    "James Carter"
    "Ronald Reagan"
    "George H. W. Bush"
    "William J. Clinton"
    "George W. Bush"
    "Barack Obama"
    "Donald J. Trump"
]
# loop through the presidents and append them to the actual list to have data to test
test_data = []
for president in president_names_list:
    test_data.append((president, True))

# test that the president is in the list of names from the response
@pytest.mark.parametrize("president, expected", test_data)
def testEachPresidentInList(president, expected):
    assert (president in list_from_response, expected)