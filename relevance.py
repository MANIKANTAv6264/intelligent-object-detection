def is_relevant(detected_object, question):
    question = question.lower()
    obj = detected_object.lower()

    # allow references like "it", "this", "that"
    if obj in question:
        return True

    if any(word in question for word in ["it", "this", "that"]):
        return True

    return False
