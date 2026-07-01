import os

from deepface import DeepFace

from .models import Student


MATCH_THRESHOLD = 0.80


def identify_person(captured_image):

    students = Student.objects.all()

    best_match = None
    best_distance = 999

    for student in students:

        try:

            result = DeepFace.verify(
                img1_path=captured_image,
                img2_path=student.image.path,
                model_name="Facenet",
                detector_backend="opencv",
                enforce_detection=False
            )

            distance = result["distance"]

            print(
                f"{student.name} => {distance}"
            )

            if distance < best_distance:

                best_distance = distance
                best_match = student

        except Exception as e:

            print(e)
            continue

    if best_match and best_distance < MATCH_THRESHOLD:

        return {
            "student": best_match,
            "distance": best_distance
        }

    return None