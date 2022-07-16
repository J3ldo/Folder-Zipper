import os
import time
import pickle
#import base64
import threading

out = {}
path2 = ""
def start():
    global out
    location = input("Location of directory: ")
    location = location.replace('\\', '/')
    path = location + '/'

    def go_deeper(path, path2):
        global out

        for item2 in os.listdir(path):
            if os.path.isdir(path+item2):
                '''out[item2] = {
                    'name': item,
                    'type': 'dir',
                    'path': path2
                }'''
                thread = threading.Thread(target=go_deeper, args=(path + f'{item2}/', path2+f"/{item2}",))
                thread.start()
                thread.join()
                continue

            try:
                with open(f'{path}/{item2}', 'r') as f:
                    out[f'{path2}/{item2}'] = {
                        'name': f'{path2}/{item2}',
                        'type': 'file',
                        'content': f.read()
                    }
            except UnicodeError:
                with open(f'{path}/{item2}', 'rb') as f:
                    out[f'{path2}/{item2}'] = {
                        'name': f'{path2}/{item2}',
                        'type': 'bytes',
                        'content': f.read()  # base64.b64encode(f.read()).decode()
                    }


    startt = time.perf_counter()
    for item in os.listdir(location):
        if os.path.isdir(path+item):
            '''out[item] = {
                'name': item,
                'type': 'dir',
                'path': "/"
            }'''
            thread = threading.Thread(target=go_deeper, args=(path + f'{item}/', path2+f"/{item}",))
            thread.start()
            thread.join()
            continue

        try:
            with open(path+item, 'r') as f:
                out[item] = {
                    'name': item,
                    'type': '0',
                    'content': f.read()
                }

        except UnicodeError:
            with open(path+item, 'rb') as f:
                out[item] = {
                    'name': item,
                    'type': '1',
                    'content': f.read()  # base64.b64encode(f.read()).decode()
                }

    while threading.active_count() > 1:
        continue

    '''with open('out.json', 'w') as f:
        json.dump(out, f, indent=4)'''
    with open('out.zipt', 'wb') as f:
        pickle.dump(out, f, protocol=pickle.HIGHEST_PROTOCOL)

    print(f'Succesfully zipped the directory in {round(time.perf_counter() - startt, 2)} seconds.')

if __name__ == '__main__':
    start()
