import threading
import os
import time
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False
reference_img = None
capture_reference = False
user_name = None
countdown = 0

def check_face(frame):
    global face_match
    try:
        if reference_img is not None and DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False

def capture_reference_image(user_name):
    global reference_img, countdown
    countdown = 5
    for i in range(5, 0, -1):
        print(f"Capturing in {i}...")
        time.sleep(1)
        countdown = i

    ret, frame = cap.read()
    if ret:
        reference_img = frame.copy()
        print(f"Reference image captured for {user_name}.")
        save_reference_image(user_name, reference_img)
        countdown = 0

def save_reference_image(user_name, image):
    folder_path = f"references"
    os.makedirs(folder_path, exist_ok=True)
    image_path = os.path.join(folder_path, f"{user_name}_reference.jpg")
    cv2.imwrite(image_path, image)
    print(f"Reference image saved to {image_path}.")

# Prompt user for name
user_name = input("Enter the user name: ")

# Start the thread for capturing reference images
reference_thread = threading.Thread(target=capture_reference_image, args=(user_name,))
reference_thread.start()

while countdown > 0:
    ret, frame = cap.read()

    if ret:
        cv2.putText(frame, str(countdown), (280, 240), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)
        cv2.imshow('video', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            print("Exiting program.")
            reference_thread.join()
            cv2.destroyAllWindows()
            exit()

# Main loop for face recognition
while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText(frame, f"Match: {user_name}", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "No Match", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow('video', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        print("Exiting program.")
        break

cv2.destroyAllWindows()
