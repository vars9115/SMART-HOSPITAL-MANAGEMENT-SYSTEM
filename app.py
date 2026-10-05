from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

patients = []
doctors = [
    {"name": "Dr. Anitha", "specialization": "Cardiologist"},
    {"name": "Dr. Ravi", "specialization": "General Physician"},
    {"name": "Dr. Priya", "specialization": "Dermatologist"}
]
appointments = []


@app.route("/")
def home():
    return render_template(
        "index.html",
        patients=patients,
        doctors=doctors,
        appointments=appointments
    )


@app.route("/patients")
def patient_page():
    return render_template("patients.html", patients=patients)


@app.route("/add_patient", methods=["POST"])
def add_patient():
    patient = {
        "name": request.form["name"],
        "age": request.form["age"],
        "gender": request.form["gender"],
        "phone": request.form["phone"],
        "disease": request.form["disease"]
    }

    patients.append(patient)
    return redirect(url_for("patient_page"))


@app.route("/doctors")
def doctor_page():
    return render_template("doctors.html", doctors=doctors)


@app.route("/appointments")
def appointment_page():
    return render_template(
        "appointments.html",
        appointments=appointments,
        doctors=doctors
    )


@app.route("/book_appointment", methods=["POST"])
def book_appointment():
    appointment = {
        "patient": request.form["patient"],
        "doctor": request.form["doctor"],
        "date": request.form["date"],
        "time": request.form["time"],
        "reason": request.form["reason"]
    }

    appointments.append(appointment)
    return redirect(url_for("appointment_page"))


if __name__ == "__main__":
    app.run(debug=True)