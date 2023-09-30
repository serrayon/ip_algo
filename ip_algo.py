# Assign `import_file` to the name of the file 
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information. 
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:

  # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
  ip_addresses = file.read()

# Use '.split()' to convert 'ip_addressses' from a string to a list
ip_addresses = ip_addresses.split()

# Build iterative statement
# name loop variable 'element'
# loop through 'ip_addresses' 
for element in ip_addresses:
  
  # Display 'element' in every iteration
  print(element)

# Display `ip_addresses`
print(ip_addresses)