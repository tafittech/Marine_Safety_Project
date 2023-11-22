from django.db import models

# Import from app here.
from Students.models import StudentProfile
from Admin.models import AdminProfile


# Create your models here.

class Course(models.Model):
    id          = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name 



class Subject(models.Model):
    id           = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    course_id    = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff_id     = models.ForeignKey(AdminProfile, on_delete=models.CASCADE)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.subject_name



class Certificate(models.Model):
    id        = models.AutoField(primary_key=True)
    cert_number = models.IntegerField(default=0)
    Date_issued = models.DateTimeField(auto_now_add=True)
    course_id   = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject_id  = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Date_issued



class Attendance(models.Model):
    id              = models.AutoField(primary_key=True)
    subject_id      = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    attendance_date = models. DateTimeField(auto_now_add=True)
    created_at      = models. DateTimeField(auto_now_add=True)
    updated_at      = models. DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.attendance_date
    


class AttendanceReport(models.Model):
    id            = models.AutoField(primary_key=True)
    student_id    = models.ForeignKey(StudentProfile, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status        = models.BooleanField(default=False)
    created_id    = models. DateTimeField(auto_now_add=True)
    updated_id    = models. DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status


