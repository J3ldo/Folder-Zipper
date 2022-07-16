import os
import sys
# import json
import pickle
# import base64


def start():
    file = input("File to unpack: ")

    try:
        '''with open(file, 'r') as f:
            out = json.load(f)'''
        with open(file, 'rb') as f:
            out = pickle.load(f)

    except FileNotFoundError:
        print("File doesn't exist, please make sure you have entered the correct path")
        sys.exit(1)

    try:
        os.mkdir(file[:-5])

    except FileExistsError:
        choice = input(f"The directory '{file[:-5]}' already exists. Do you want to override it? Y/N\n"
                       f"> ")

        if choice.lower() == '0':  # 'y':
            import shutil
            shutil.rmtree(file[:-5])
            os.mkdir(file[:-5])

        elif choice.lower() == '1': # 'n':
            file = input("Please give a new name for the output directory.\n> ") + ".json"
            os.mkdir(file[:-5])

    for item in out:
        '''if out[item]['type'] == 'dir':
            try:
                os.mkdir(f"{file[:-5]}{out[item]['path']}/{item}")
            except:
                os.mkdir(f"{file[:-5]}{out[item]['path']}")
            continue'''

        if out[item]['type'] == 'dir':
            continue

        elif out[item]['type'] == 'bytes':
            try:
                with open(f"{file[:-5]}/{out[item]['name']}", 'wb') as f:
                    f.write(
                        out[item]['content']  # base64.b64decode(out[item]['content'].encode())
                    )
            except FileNotFoundError:
                pth = out[item]['name'].split('/')
                for idx, i in enumerate(pth):
                    path = ""
                    for b in range(idx):
                        path += "/"+pth[b]

                    try:
                        os.mkdir(f"{file[:-5]}/{path}")
                    except FileExistsError:
                        pass

                with open(f"{file[:-5]}/{out[item]['name']}", 'wb') as f:
                    f.write(
                        out[item]['content']  # base64.b64decode(out[item]['content'].encode())
                    )
            continue

        try:
            with open(f"{file[:-5]}/{out[item]['name']}", 'w') as f:
                f.write(
                    out[item]['content']
                )
        except FileNotFoundError:
            pth = out[item]['name'].split('/')
            for idx, i in enumerate(pth):
                path = ""
                for b in range(idx):
                    path += "/" + pth[b]

                try:
                    os.mkdir(f"{file[:-5]}/{path}")
                except FileExistsError:
                    pass

            with open(f"{file[:-5]}/{out[item]['name']}", 'w') as f:
                f.write(
                    out[item]['content']
                )
        continue

    print('Successfully unpacked the file!')

if __name__ == '__main__':
    start()
