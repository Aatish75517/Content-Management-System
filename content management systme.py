content=[["laptop","how to download windows in your laptop"],["phone","how to download apps in your phones"],
        ["games","how to download games in pc"],["pc games","how to download pc games"]]
while True:
    print("Content Management System (CMS)")
    print("1:  search content")
    print("2:  add content")
    print("3:  view all contents")
    print("4:  update content")
    print("5:  delete content")
    print("6:  save content to file")
    print("7:  load content form file")
    print("8:  quit")
    choice=input("what do you want enter number:")
    if choice=="1":
        while True:
            a=input("enter your title:").lower()
            b=False
            for i in content:
                if a in i[0].lower():
                    print("Title:", i[0])
                    print("Description:", i[1])
                    b=True
            if not b:
                print("not available")
            c=input("do you want to search other:").lower()
            if c=="yes":
                print("no worry sir")
            else:
                break
        input("Press Enter to continue...")
    elif choice=="2":
        a=input("enter your title:")
        b=input("enter your description:")
        content.append([a,b])
        print("add succesfully")
        input("Press Enter to continue...")
    elif choice=="3":
        print("all contents")
        for i, j in enumerate(content, start=1):
            print(f"{i}. title: {j[0]}")
            print(f"description: {j[1]}\n")
        input("Press Enter to continue...")    
    elif choice=="4":
        a=input('enter your title name:').lower()
        b=False
        for i in content:
                if a in i[0].lower():
                    print("Title:", i[0])
                    print("Description:", i[1])
                    b=True
                    c=input("enter your new title:")
                    d=input("enter your description:")
                    i[0]=c
                    i[1]=d
                    print("update succesfully")
                    print(i[0],i[1])
                    break
        if not b:
                print("not available")
        input("Press Enter to continue...")
    elif choice=="5":
            a=input('enter your title name:').lower()
            b=False
            for i in content:
                if a in i[0].lower():
                    print("Title:", i[0])
                    print("Description:", i[1])
                    b=True
                    c=input("do you want to delete:").lower()
                    if c=="yes":
                        content.remove(i)
                        print("delete succesfully")
                    else:
                         print("ok sir")
            if not b:
                print("not available")
            input("Press Enter to continue...")
    elif choice=="6":
            a=input("enter your title:").lower()
            b=False
            for i in content:
                if a in i[0].lower():
                    print("Title:", i[0])
                    print("Description:", i[1])
                    b=True
                    file=input("enter your file name:")
                    c=open(file,"a")
                    c.write(f"{i[0]}:{i[1]}\n")
                    c.close()
                    print("saved succesfully;")
            if not b:
                print("not available")
            input("Press Enter to continue...")
    elif choice=="7":
        a=input("enter your file name:")
        try:
            with open(a, "r") as file:
                for i in file:
                    if ":" in i:
                        title, description = i.strip().split(":", 1)
                        content.append([title, description])
            print("content loaded successfully from file!")
        except FileNotFoundError:
            print("no saved file found.")
        input("Press Enter to continue...")
    elif choice=="8":
         print("bye sir")
         break

    
