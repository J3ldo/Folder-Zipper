import sys


def main():
    choice = input("What do you want to do?\n"
                   "1) Zip\n"
                   "2) Unpack\n"
                   "> ")

    if choice == '1':
        import zip
        zip.start()
        return True

    elif choice == '2':
        import unpack
        unpack.start()
        return True

    else:
        print('Please choose a valid option.')
        return False


if __name__ == '__main__':
    while True:
        if main():
            sys.exit(0)
