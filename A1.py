import cv2

user_image = input('Enter your file location: ')
image = cv2.imread(user_image)

if image is None:
    print("Could not load image")

else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Select a choice:\n 1. Show image \n 2. Save image")
    choice = int(input("Enter your choice 1 or 2:"))
    if choice == 1:
         print("Select a choice:\n 1. colorful image \n 2. grayscale image")
         sub_choice = int(input("Enter your choice 1 or 2:"))
         if sub_choice == 1:
             cv2.imshow('Colorful Image Display', image)
             cv2.waitKey(0)
             cv2.destroyAllWindows()
         elif sub_choice == 2:
             cv2.imshow('grayscale image display', gray)
             cv2.waitKey(0)
             cv2.destroyAllWindows() 
         else:
             print("Invalid choice")       
    elif choice == 2:
        filename = input("Enter filename to save the image:")
        print("Select a choice:\n 1. colorful image \n 2. grayscale image")
        sub_choice = int(input("Enter your choice 1 or 2:"))
        
        if sub_choice == 1:
            success = cv2.imwrite(filename, image)
        elif sub_choice == 2:
            success = cv2.imwrite(filename, gray)
                
        else:
            print("Invalid choice")
            success = False
        if success:
            print("File saved successfully")
        else:
            print("file did not saved.")
    else:
        print("Invalid choice for main menu")                  