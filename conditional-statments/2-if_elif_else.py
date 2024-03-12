score = -1

if not  (score >= 0 and score <= 100):
    print("Invalid score.\nPlease enter a score between 0 to 100.")
else:
    if not score > 40:
        print("Sorry!, you are failed")
    else:
        if score >= 80:
            print("First class")
        elif score >= 60:
            print("Second class")
        elif score >= 40:
            print("Third class")
        