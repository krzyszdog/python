with open("second_file.txt", "a") as f1:
    f1.write("Dowlony tekst\n")
    f1.write("Inny dowolny tekst\n")

try:
    path = input("Provide path to the file: ")
    with open(path, "r") as f2:
        print(f2.read())
except Exception as e:
    print(f"{e} -->> file does not exist")

