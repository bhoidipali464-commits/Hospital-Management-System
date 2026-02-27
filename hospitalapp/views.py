
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Doctor,Patient,Appointment


def home(request):
    return render(request, 'home.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})
from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment


def add_doctor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        phone = request.POST.get('phone')

        Doctor.objects.create(
            name=name,
            specialization=specialization,
            phone=phone
        )
        return redirect('doctor_list')

    return render(request, 'add_doctor.html')
from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment


def add_patient(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')

        Patient.objects.create(
            name=name,
            age=age,
            gender=gender,
            phone=phone
        )
        return redirect('patient_list')

    return render(request, 'add_patient.html')
def add_appointment(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    if request.method == "POST":
        doctor_id = request.POST.get('doctor')
        patient_id = request.POST.get('patient')
        date = request.POST.get('date')
        time = request.POST.get('time')

        Appointment.objects.create(
            doctor_id=doctor_id,
            patient_id=patient_id,
            date=date,
            time=time
        )
        return redirect('appointment_list')

    return render(request, 'add_appointment.html', {
        'doctors': doctors,
        'patients': patients
    })
def edit_doctor(request, id):
    doctor = Doctor.objects.get(id=id)

    if request.method == "POST":
        doctor.name = request.POST.get('name')
        doctor.specialization = request.POST.get('specialization')
        doctor.phone = request.POST.get('phone')
        doctor.save()
        return redirect('doctor_list')

    return render(request, 'edit_doctor.html', {'doctor': doctor})
def delete_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('doctor_list')
def edit_patient(request, id):
    patient = Patient.objects.get(id=id)

    if request.method == "POST":
        patient.name = request.POST.get('name')
        patient.age = request.POST.get('age')
        patient.gender = request.POST.get('gender')
        patient.phone = request.POST.get('phone')
        patient.save()
        return redirect('patient_list')

    return render(request, 'edit_patient.html', {'patient': patient})
def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('patient_list')
def edit_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    if request.method == "POST":
        appointment.doctor_id = request.POST.get('doctor')
        appointment.patient_id = request.POST.get('patient')
        appointment.date = request.POST.get('date')
        appointment.time = request.POST.get('time')
        appointment.save()
        return redirect('appointment_list')

    return render(request, 'edit_appointment.html', {
        'appointment': appointment,
        'doctors': doctors,
        'patients': patients
    })
def delete_appointment(request, id):
        appointment = Appointment.objects.get(id=id)
        appointment.delete()
        return redirect('appointment_list')



# ---------------- DOCTOR ----------------

"""@login_required
def doctor_list(request):
    query = request.GET.get('q')
    if query:
        doctors = Doctor.objects.filter(
            Q(name__icontains=query) |
            Q(specialization__icontains=query)
        )
    else:
        doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})


@login_required
def add_doctor(request):
    form = DoctorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('doctor_list')
    return render(request, 'form.html', {'form': form})


@login_required
def edit_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        return redirect('doctor_list')
    return render(request, 'form.html', {'form': form})


@login_required
def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()
    return redirect('doctor_list')


# ---------------- PATIENT ----------------

@login_required
def patient_list(request):
    query = request.GET.get('q')
    if query:
        patients = Patient.objects.filter(name__icontains=query)
    else:
        patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})


@login_required
def add_patient(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('patient_list')
    return render(request, 'form.html', {'form': form})


@login_required
def edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('patient_list')
    return render(request, 'form.html', {'form': form})


@login_required
def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    return redirect('patient_list')


# ---------------- APPOINTMENT ----------------

@login_required
def appointment_list(request):
    query = request.GET.get('q')
    if query:
        appointments = Appointment.objects.filter(
            Q(doctor__name__icontains=query) |
            Q(patient__name__icontains=query)
        )
    else:
        appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})


@login_required
def add_appointment(request):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appointment_list')
    return render(request, 'form.html', {'form': form})


@login_required
def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    return redirect('appointment_list')


# ---------------- REGISTER ----------------

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(request, 'register.html', {'form': form})"""