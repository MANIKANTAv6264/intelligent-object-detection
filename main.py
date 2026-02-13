import cv2
import time

from detector import detect_object
from brain import ask_brain
from speaker import speak
import input_handler 

cap = cv2.VideoCapture(0)

cooldown = 3
last_answer_time = 0
last_question_used = None

print("\n🎯 INSTRUCTIONS:")
print("1. Show an object to the camera")
print("2. Ask ANY question about it")
print("3. System answers using internet knowledge\n")

input_handler.start_input_thread()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detected_object = detect_object(frame)

    if detected_object:
        cv2.putText(
            frame,
            f"Detected: {detected_object}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    if (
        detected_object
        and input_handler.latest_question
        and input_handler.latest_question != last_question_used
        and time.time() - last_answer_time > cooldown
    ):
        contextual_question = (
            f"The object detected is a {detected_object}. "
            f"User question: {input_handler.latest_question}. "
            f"Answer clearly and briefly."
        )

        answer = ask_brain(contextual_question)

        print("\n Detected Object :", detected_object)
        print("\n Question :")
        print(input_handler.latest_question)

        print("\n Answer :")
        print(answer)
        speak(answer)


        last_question_used = input_handler.latest_question
        last_answer_time = time.time()

    cv2.imshow("Vision AI Agent", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
