def main():
    #write your code below this line
    score = int(input("Give points [0-100]:"))
    grade = ""

    if score > 100:
        grade = "incredible!"
    elif score >= 90:
        grade = str(5)
    elif score >= 80:
        grade = str(4)
    elif score >= 70:
        grade = str(3)
    elif score >= 60:
        grade = str(2)
    elif score >= 50:
        grade = str(1)
    elif score >= 0:
        grade = "failed"
    else:
        grade = "impossible!"

    print("Grade: " + grade)

if __name__ == '__main__':
    main()
