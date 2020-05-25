import time

hosts_path = r"C:\Windows\System32\Drivers\etc\hosts"
redirect = "127.0.0.1"
# taking input from user :
number = int(input("Enter the number of websites to be blocked:"))

website_list = []
for i in range(1, number + 1):
    website = input("Enter the site of url to block:")
    website_list.append(website)

# blocking of website:
# while True:
with open(hosts_path, 'r+') as file:
    contents = file.read()
    for websites in website_list:
        # if it is already blocked:
        if websites in contents:
            pass  # Pass operation is the null operation where nothing runs or excecutes

        # if you want to add the website url to thew hosts file :
        else:
            file.write(redirect+" "+websites+"\n")
