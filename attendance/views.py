import csv
import base64

from datetime import date

from django.http import JsonResponse
from django.http import HttpResponse

from django.shortcuts import render

from django.core.files.base import ContentFile

from .models import Attendance
from .models import Student

from .deepface_utils import identify_person


def dashboard(request):

    students = Student.objects.count()

    attendance = Attendance.objects.count()

    context = {

        "students": students,

        "attendance": attendance
    }

    return render(
        request,
        "attendance/dashboard.html",
        context
    )


def webcam_page(request):

    return render(
        request,
        "attendance/webcam.html"
    )


def mark_attendance(request):

    if request.method == "POST":

        image_data = request.POST.get("image")

        format, imgstr = image_data.split(';base64,')

        image_file = ContentFile(
            base64.b64decode(imgstr),
            name="capture.jpg"
        )

        temp_path = "capture.jpg"

        with open(temp_path, "wb") as f:

            f.write(
                image_file.read()
            )

        result = identify_person(
            temp_path
        )

        if result:

            student = result["student"]

            distance = round(
                result["distance"],
                4
            )

            exists = Attendance.objects.filter(
                student=student,
                date=date.today()
            ).exists()

            if not exists:

                Attendance.objects.create(
                    student=student
                )

            return JsonResponse({

                "success": True,

                "name": student.name,

                "distance": distance
            })

        return JsonResponse({

            "success": False
        })

def export_csv(request):

    response = HttpResponse(
        content_type="text/csv"
    )

    response[
        "Content-Disposition"
    ] = 'attachment; filename="attendance.csv"'

    writer = csv.writer(response)

    writer.writerow([
        "Name",
        "Date",
        "Time",
        "Status"
    ])

    for record in Attendance.objects.all():

        writer.writerow([
            record.student.name,
            record.date,
            record.time,
            record.status
        ])

    return response