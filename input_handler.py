import threading

latest_question = None

def input_loop():
    global latest_question
    while True:
        q = input("\n Question:\n").strip()
        if q:
            latest_question = q

def start_input_thread():
    thread = threading.Thread(target=input_loop, daemon=True)
    thread.start()
