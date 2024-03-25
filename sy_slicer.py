# -----Project - Email Slicer #---------------


# Get user email
email = input ("Please enter your email address: ").strip()

# Slice out username
user_name = email[:email.index("@")]


# Slice out domain
domain_name = email[email.index("@") + 1:]


# Format message
str1 = "Your user name is {} and your domain name is {}"
out1 = str1.format(user_name, domain_name)


# Display output message
print(out1)

