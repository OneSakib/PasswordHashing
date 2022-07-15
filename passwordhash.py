import bcrypt


def password_hash():
    # MY Password
    my_pass = 'MYPassword'
    # Change My password into byte form
    bytepwd = my_pass.encode('utf-8')
    # Generate salt
    mySalt = bcrypt.gensalt()
    # Hash password of your password
    pass_hash = bcrypt.hashpw(bytepwd, mySalt)
    # Now you can save this hash code in your database
    #     Now Check password with the hash code
    # print(bcrypt.checkpw(password=my_pass, hashed_password=hash))  # it gives error because its string format
    input_pass = input("Enter Your password:\t")
    byte_input_pass = input_pass.encode("utf-8")
    if bcrypt.checkpw(password=byte_input_pass, hashed_password=pass_hash):
        print("Password is Match")
    else:
        print("password is wrong")


if __name__ == "__main__":
    password_hash()
