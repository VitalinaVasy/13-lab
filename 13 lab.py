import random

class AllergyError(Exception):
    def __init__(self, allergic_medications):
        self.allergic_medications = allergic_medications
class Doctor:
    def __init__(self, surname, first_name, middle_name, specialization):
        self._id = random.randint(10000, 99999)
        self._surname = surname
        self._first_name = first_name
        self._middle_name = middle_name
        self._specialization = specialization

    @property
    def id(self):
        return self._id

    @property
    def surname(self):
        return self._surname

    @property
    def first_name(self):
        return self._first_name

    @property
    def middle_name(self):
        return self._middle_name

    @property
    def specialization(self):
        return self._specialization

    def __str__(self):
        return f"ID: {self.id}, Лікар: {self.surname} {self.first_name} {self.middle_name}, Спеціалізація: {self.specialization}"


class Appointment:
    def __init__(self, patient, doctor, appointment_date):
        self._id = random.randint(10000, 99999)
        self._patient = patient
        self._doctor = doctor
        self._appointment_date = appointment_date
        self._diagnosis = None
        self._prescription = None

    @property
    def id(self):
        return self._id

    @property
    def patient(self):
        return self._patient

    @property
    def doctor(self):
        return self._doctor

    @property
    def appointment_date(self):
        return self._appointment_date

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value

    @property
    def prescription(self):
        return self._prescription

    @prescription.setter
    def prescription(self, value):
        self._prescription = value

    def __str__(self):
        return f"ID: {self.id}, Дата прийому: {self.appointment_date}, Пацієнт: {self.patient}, Лікар: {self.doctor}, Діагноз: {self.diagnosis}, Призначення: {self.prescription}"


class Diagnosis:
    def __init__(self, name, description):
        self._id = random.randint(10000, 99999)
        self._name = name
        self._description = description

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def __str__(self):
        return f"ID: {self.id}, Діагноз: {self.name}, Опис: {self.description}"


class Prescription:
    def __init__(self, medication, dosage):
        self._id = random.randint(10000, 99999)
        self._medication = medication
        self._dosage = dosage

    @property
    def id(self):
        return self._id

    @property
    def medication(self):
        return self._medication

    @property
    def dosage(self):
        return self._dosage

    def __str__(self):
        return f"ID: {self.id}, Ліки: {self.medication}, Доза: {self.dosage}"


class Patient:
    def __init__(self, surname, first_name, middle_name, address, phone,medication, diagnosis=None ):
        self._id = random.randint(10000, 99999)
        self._surname = surname
        self._first_name = first_name
        self._middle_name = middle_name
        self._address = address
        self._phone = phone
        self._medical_card_number = random.randint(100000, 999999)
        self._diagnosis_history = []  # історія хвороби
        if diagnosis:
            self.add_diagnosis(diagnosis)
        self._medication = medication

    @property
    def medication(self):
        return self._medication

    @property
    def id(self):
        return self._id

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def medical_card_number(self):
        return self._medical_card_number

    @property
    def diagnosis_history(self):
        return self._diagnosis_history

    def add_diagnosis(self, diagnosis):
        self._diagnosis_history.append(diagnosis)

    def add_diagnosis_from_strings(self, diagnosis_name, diagnosis_description):
        diagnosis = Diagnosis(diagnosis_name, diagnosis_description)
        self.add_diagnosis(diagnosis)

    def prescribe_medication(self, medication):
        allergic_to = ["Аспірин", "Антибіотики"]  # Припустимий список алергійних препаратів

        if medication in allergic_to:
            raise AllergyError(allergic_to)


    def __str__(self):
        return f"ID: {self.id}, Ім'я: {self.surname} {self.first_name} {self.middle_name}, Адреса: {self.address}, Телефон: {self.phone}, Номер медичної картки: {self.medical_card_number},Пацієнту призначено препарат: {self.medication}, Історія хвороби: {self.diagnosis_history}"


class PatientDatabase:
    def __init__(self):
        self._patients = []
        self._doctors = []
        self._appointments = []  # Список прийомів

    def add_patient(self, patient):
        self._patients.append(patient)

    def add_doctor(self, doctor):
        self._doctors.append(doctor)

    def display_patients(self, patients_list):
        for patient in patients_list:
            diagnosis_info = ""
            if patient.diagnosis_history:
                diagnosis_info = ", ".join([f"{diagnosis.name}: {diagnosis.description}" for diagnosis in patient.diagnosis_history if isinstance(diagnosis, Diagnosis)])

            print(f"Пацієнт: {patient}")
#Діагнози: {diagnosis_info}

    def display_doctors(self):
        for doctor in self._doctors:
            print(doctor)

    # Методи для роботи з прийомами
    def schedule_appointment(self, patient, doctor, appointment_date):
        appointment = Appointment(patient, doctor, appointment_date)
        self._appointments.append(appointment)

    def view_patient_history(self, patient_id):
        patient = self.find_patient_by_id(patient_id)
        if patient:
            print(patient)
        else:
            print("Пацієнта з таким ID не знайдено.")

    def find_patient_by_id(self, patient_id):
        for patient in self._patients:
            if patient.id == patient_id:
                return patient
        return None

def display_menu():
    print("Меню:")
    print("1. Список пацієнтів")
    print("2. Список лікарів")
    print("3. Записатися на прийом до лікаря")
    print("4. Подивитися історію хвороби пацієнта")
    print("5. Вийти")


db = PatientDatabase()

#Лікарі
db.add_doctor(Doctor("Петров", "Іван", "Іванович", "Терапевт"))
db.add_doctor(Doctor("Сидорова", "Ольга", "Вікторівна", "Лікар загальної практики"))
db.add_doctor(Doctor("Іванов", "Михайло", "Петрович", "Невролог"))

#пацієнти
db.add_patient(Patient("Ахремчюк", "Іван", "Іванович", "Пушкінська 10, Харків", "+380996356245",  "ОРИ", "Аспірин"))
db.add_patient(Patient("Забівко", "Олександер", "Андрійович", "Пр. Інженерний 10, Харків", "+380996358525", "Короновірус", "Аспірин"))
db.add_patient(Patient("Надійко", "Ванеса", "Юрівна", "Пр. Інженерний 4, Харків", "380962366455", "Артріт", "Аспірин"))


while True:
    display_menu()
    choice = input("Виберіть опцію: ")

    if choice == "1":
        print("Список пацієнтів:")
        db.display_patients(db._patients)
    elif choice == "2":
        print("Список лікарів:")
        db.display_doctors()
    elif choice == "3":
        print("Записатися на прийом до лікаря:")

        # Показати доступних лікарів
        print("Доступні лікарі:")
        db.display_doctors()

        # Введення даних пацієнта
        patient_id = input("Введіть ID пацієнта: ")
        patient = db.find_patient_by_id(int(patient_id))
        if patient:
            # Введення даних лікаря
            doctor_id = input("Введіть ID лікаря, до якого ви хочете записатися на прийом: ")
            doctor = next((doc for doc in db._doctors if doc.id == int(doctor_id)), None)
            if doctor:
                # Введення дати прийому
                appointment_date = input("Введіть дату прийому (формат: рік-місяць-день година:хвилина): ")

                # Запис на прийом
                db.schedule_appointment(patient, doctor, appointment_date)
                medication = input("Призначте ліки: ")
                try:
                    patient.prescribe_medication(medication)
                except AllergyError as e:
                    print(f"Пацієнт алергічний на такі препарати: {', '.join(e.allergic_medications)}")
                    print("Введіть інші ліки.")
                print("Ви успішно записалися на прийом до лікаря.")
            else:
                print("Лікаря з таким ID не знайдено.")
        else:
            print("Пацієнта з таким ID не знайдено.")
    elif choice == "4":
        print("Подивитися історію хвороби пацієнта:")
        patient_id = input("Введіть ID пацієнта: ")
        db.view_patient_history(int(patient_id))
    elif choice == "5":
        print("Дякую за використання нашої програми!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")

