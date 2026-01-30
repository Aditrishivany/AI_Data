feedback=input("Please provide your feedback about our service: ")
with open("feedback.txt","a") as file:
    file.write(feedback+"\n")
print("Thankyou")