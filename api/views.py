from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


# -----------instructor---------
@api_view(['GET'])
def getInstructors(request):
    
    instructors = instructor.objects.all()
    serializer = InstructorSerializer(instructors, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addInstructor(request):
    serializer = InstructorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST','PATCH','PUT'])
def updateInstructor(request, pk):
    update = instructor.objects.get(id=pk)
    serializer = InstructorSerializer(instance=update, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteInstructor(request, pk):
    instructors = instructor.objects.get(id=pk)
    instructors.delete()

    return Response("Deleted Successfully")


# -------student---------

@api_view(['GET'])
def getStudents(request):
    
    students = student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateStudent(request, pk):
    update = student.objects.get(id=pk)
    serializer = StudentSerializer(instance=update, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteStudent(request, pk):
    students = student.objects.get(id=pk)
    students.delete()

    return Response("Deleted Successfully")



# -------schedule---------

@api_view(['GET'])
def getSchedule(request):
    
    schedules = schedule.objects.all()
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addSchedule(request):
    serializer = ScheduleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateSchedule(request, pk):
    update = schedule.objects.get(id=pk)
    serializer = ScheduleSerializer(instance=update, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteSchedule(request, pk):
    schedules = schedule.objects.get(id=pk)
    schedules.delete()

    return Response("Deleted Successfully")



# -------enrollment---------

@api_view(['GET'])
def getEnrollment(request):
    
    enrollments = enrollment.objects.all()
    serializer = EnrollmentSerializer(enrollments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addEnrollment(request):
    serializer = EnrollmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateEnrollment(request, pk):
    update = enrollment.objects.get(id=pk)
    serializer = EnrollmentSerializer(instance=update, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteEnrollment(request, pk):
    enrollments = enrollment.objects.get(id=pk)
    enrollments.delete()

    return Response("Deleted Successfully")


# -------payments---------

@api_view(['GET'])
def getPayment(request):
    
    payments = payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPayment(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updatePayment(request, pk):
    update = payment.objects.get(id=pk)
    serializer = PaymentSerializer(instance=update, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deletePayment(request, pk):
    payments = payment.objects.get(id=pk)
    payments.delete()

    return Response("Deleted Successfully")