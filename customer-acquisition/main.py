from sheety import Sheety
from sheety import post_data


def main():
    sheety = Sheety()
    sheety.get_data()
    users = sheety.users
    print(users)
    print("Welcome to Amanuel's Flight Club.\nWe find the best flight deals and email you.")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")

    while True:
        email = input("What is your email?\n")
        confirm_email = input("Type your email again.\n")
        if email == confirm_email:
            break
        print("Email does not match. Please enter your email correctly.")

    for user in users:
        if user["firstName"] == first_name and user["lastName"] == last_name and \
                user["email"] == email:
            print("Oops... there exists an account for this user.")
            return 0

    user_info = {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
    post_data(user_info)

    return 0


if __name__ == "__main__":
    main()
