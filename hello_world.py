import random 
print("hello")

fruits = "Apples"
print(fruits[5])

def replace_email(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
print(replace_email("aikerim@mail.ru", "mail.ru", "gmail.com"))


