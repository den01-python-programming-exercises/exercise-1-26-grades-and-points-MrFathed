def main():
    #write your code below this line
    grade = int(input("Give points [0-100]:"))

    if grade > 100:
        print("incredible!")
    elif grade >= 90:
        print(5)
    elif grade >= 80:
        print(4)
    elif grade >= 70:
        print(3)
    elif grade >= 60:
        print(2)
    elif grade >= 50:
        print(1)
    elif grade >= 0:
        print("failed")
    else:
        print("impossible!")

if __name__ == '__main__':
    main()
