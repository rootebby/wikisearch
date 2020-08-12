import wikipedia
import time
print("""
                 _    ____       _     _
 _ __ ___   ___ | |_ / __ \  ___| |__ | |__  _   _ 
| '__/ _ \ / _ \| __/ / _` |/ _ \ '_ \| '_ \| | | |
| | | (_) | (_) | || | (_| |  __/ |_) | |_) | |_| |
|_|  \___/ \___/ \__\ \__,_|\___|_.__/|_.__/ \__, |
                     \____/                  |___/
""")

time.sleep(2)

print("""
          _ _    _                         _
__      _(_) | _(_)___  ___  __ _ _ __ ___| |__
\ \ /\ / / | |/ / / __|/ _ \/ _` | '__/ __| '_  |
 \ V  V /| |   <| \__ \  __/ (_| | | | (__| | | |
  \_/\_/ |_|_|\_\_|___/\___|\__,_|_|  \___|_| |_|

""")

while True:
    print("""
1. Search all titles about the word.
2. Search word.
    """)
    _cho_ = int(
        input("Option : ")
    )

    if _cho_ == 1:
        ebby = input("Search :  ")
        print(
            wikipedia.search(
                ebby
            )
        )
    
    elif _cho_ == 2:
        ebby = input("Search :  ")
        print(
            wikipedia.summary(
                ebby
            )
        )
    
    else:
        print("Choose one of the printed options !!!")

