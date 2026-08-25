def login_required(func):
    def wrapper():
        print("checking login....")
        func()
    return wrapper


@login_required
def dashword():
    print("welcome to dashboard")


dashword()


@login_required
def profile():
    print("welcome to our profile")

profile()