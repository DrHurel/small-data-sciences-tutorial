def main():
    print("This is the main function of the script.")

    with open('assets/example.txt', 'r') as file:
        content = file.read()
        print("Content of example.txt:")
        print(content)


if __name__ == "__main__":
    main()