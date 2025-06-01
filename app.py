import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model dan scaler
model = joblib.load("rf.pkl")
scaler = joblib.load("scaler.pkl")

# Mapping untuk tampilan ramah pengguna
marital_status_map = {
    1: "Lajang", 2: "Menikah", 3: "Duda/Janda", 4: "Cerai", 5: "Kohabitasi", 6: "Pisah Hukum"
}

application_mode_map = {
    1: "Fase 1 - Umum", 2: "Peraturan 612/93", 5: "Khusus Azores", 7: "Lulusan PT lain",
    10: "Peraturan 854-B/99", 15: "Mahasiswa Internasional", 16: "Khusus Madeira",
    17: "Fase 2 - Umum", 18: "Fase 3 - Umum", 26: "Rencana Berbeda", 27: "Institusi Lain",
    39: "Usia >23 tahun", 42: "Transfer", 43: "Ganti jurusan", 44: "Spesialis Teknologi",
    51: "Ganti kampus/jurusan", 53: "Diploma Siklus Pendek", 57: "Transfer Internasional"
}

course_map = {
    33: "Biofuel", 171: "Desain Multimedia", 8014: "Sosial (malam)", 9003: "Agronomi",
    9070: "Desain Komunikasi", 9085: "Keperawatan Hewan", 9119: "Teknik Informatika",
    9130: "Ilmu Kuda", 9147: "Manajemen", 9238: "Pelayanan Sosial", 9254: "Pariwisata",
    9500: "Keperawatan", 9556: "Kebersihan Gigi", 9670: "Iklan & Marketing",
    9773: "Jurnalisme", 9853: "Pendidikan Dasar", 9991: "Manajemen (malam)"
}

nationality_map = {
    1: "Portugal", 2: "Jerman", 6: "Spanyol", 11: "Italia", 13: "Belanda", 14: "Inggris",
    17: "Lithuania", 21: "Angola", 22: "Cape Verde", 24: "Guinea", 25: "Mozambik",
    26: "Santome", 32: "Turki", 41: "Brasil", 62: "Romania", 100: "Moldova",
    101: "Meksiko", 103: "Ukraina", 105: "Rusia", 108: "Kuba", 109: "Kolombia"
}
mother_qual_map = {
    1: "Secondary Education - 12th Year of Schooling or Eq.",
    2: "Higher Education - Bachelor's Degree",
    3: "Higher Education - Degree",
    4: "Higher Education - Master's",
    5: "Higher Education - Doctorate",
    6: "Frequency of Higher Education",
    9: "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    22: "Technical-professional course",
    26: "7th year of schooling",
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th year of schooling",
    34: "Unknown",
    35: "Can't read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle (4th/5th year) or equiv.",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    41: "Specialized higher studies course",
    42: "Professional higher technical course",
    43: "Higher Education - Master (2nd cycle)",
    44: "Higher Education - Doctorate (3rd cycle)"
}
father_qual_map = {
    1: "Secondary Education - 12th Year of Schooling or Eq.",
    2: "Higher Education - Bachelor's Degree",
    3: "Higher Education - Degree",
    4: "Higher Education - Master's",
    5: "Higher Education - Doctorate",
    6: "Frequency of Higher Education",
    9: "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    13: "2nd year complementary high school course",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    20: "Complementary High School Course",
    22: "Technical-professional course",
    25: "Complementary High School Course - not concluded",
    26: "7th year of schooling",
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th year of schooling",
    31: "General Course of Administration and Commerce",
    33: "Supplementary Accounting and Administration",
    34: "Unknown",
    35: "Can't read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle (4th/5th year) or equiv.",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    41: "Specialized higher studies course",
    42: "Professional higher technical course",
    43: "Higher Education - Master (2nd cycle)",
    44: "Higher Education - Doctorate (3rd cycle)"
}
mother_occ_map = {
    0: "Student", 1: "Legislative/Executive Managers", 2: "Intellectual & Scientific Activities",
    3: "Intermediate Technicians", 4: "Administrative staff", 5: "Personal Services/Security/Sellers",
    6: "Farmers/Fishers/Forestry", 7: "Industry/Construction Workers", 8: "Machine Operators",
    9: "Unskilled Workers", 10: "Armed Forces", 90: "Other Situation", 99: "(blank)",
    122: "Health professionals", 123: "Teachers", 125: "ICT Specialists",
    131: "Science/Engineering Technicians", 132: "Health Technicians",
    134: "Legal/Social/Cultural Technicians", 141: "Secretaries/Data Operators",
    143: "Finance/Registry Operators", 144: "Admin Support", 151: "Service Workers",
    152: "Sellers", 153: "Personal Care", 171: "Construction Workers",
    173: "Printing/Artisans", 175: "Food/Textile/Crafts Workers", 191: "Cleaning Workers",
    192: "Unskilled Agriculture Workers", 193: "Unskilled Industry Workers",
    194: "Meal Prep Assistants"
}

father_occ_map = {
    0: "Student", 1: "Legislative/Executive Managers", 2: "Intellectual & Scientific Activities",
    3: "Intermediate Technicians", 4: "Administrative staff", 5: "Personal Services/Security/Sellers",
    6: "Farmers/Fishers/Forestry", 7: "Industry/Construction Workers", 8: "Machine Operators",
    9: "Unskilled Workers", 10: "Armed Forces", 90: "Other Situation", 99: "(blank)",
    101: "Armed Forces Officers", 102: "Armed Forces Sergeants", 103: "Other Armed Forces",
    112: "Admin/Commercial Directors", 114: "Hotel/Catering Directors", 121: "Physical Sciences Specialists",
    122: "Health professionals", 123: "Teachers", 124: "Finance/Admin Specialists",
    131: "Science/Engineering Technicians", 132: "Health Technicians",
    134: "Legal/Social/Cultural Technicians", 135: "ICT Technicians",
    141: "Secretaries/Data Operators", 143: "Finance/Registry Operators",
    144: "Admin Support", 151: "Service Workers", 152: "Sellers", 153: "Personal Care",
    154: "Security Services", 161: "Market Farmers", 163: "Subsistence Farmers/Fishers",
    171: "Construction Workers", 172: "Metal Workers", 174: "Electrical Workers",
    175: "Food/Textile/Crafts Workers", 181: "Plant Operators", 182: "Assembly Workers",
    183: "Drivers", 192: "Unskilled Agriculture Workers",
    193: "Unskilled Industry Workers", 194: "Meal Prep Assistants",
    195: "Street Vendors"
}
st.set_page_config(page_title="Student Dropout Predictor", layout="wide")
st.title("🎓 Prediksi Risiko Dropout Mahasiswa")

st.markdown("Isi data lengkap berikut untuk memprediksi apakah mahasiswa berisiko **dropout** atau **graduate**.")

with st.form("dropout_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        marital_status = st.selectbox("Status Pernikahan", list(marital_status_map.keys()), format_func=lambda x: marital_status_map[x])
        application_mode = st.selectbox("Jalur Masuk", list(application_mode_map.keys()), format_func=lambda x: application_mode_map[x])
        application_order = st.slider("Urutan Pilihan", 0, 9, 0)
        course = st.selectbox("Program Studi", list(course_map.keys()), format_func=lambda x: course_map[x])
        daytime_evening = st.selectbox("Kuliah Pagi/Malam", [0, 1], format_func=lambda x: "Pagi" if x == 1 else "Malam")
        prev_qualification = st.selectbox("Kualifikasi Sebelumnya", list(range(1, 44)))
        prev_qualification_grade = st.number_input("Nilai Kualifikasi Sebelumnya", value=120.0)
        nationality = st.selectbox("Kebangsaan", list(nationality_map.keys()), format_func=lambda x: nationality_map[x])

    with col2:
        mother_qual = st.selectbox("Pendidikan Ibu (kode)", list(mother_qual_map.keys()), format_func=lambda x: mother_qual_map[x])
        father_qual = st.selectbox("Pendidikan Ayah (kode)", list(father_qual_map.keys()), format_func=lambda x: father_qual_map[x])
        mother_occ = st.selectbox("Pekerjaan Ibu (kode)", list(mother_occ_map.keys()), format_func=lambda x: mother_occ_map[x])
        father_occ = st.selectbox("Pekerjaan Ayah (kode)", list(father_occ_map.keys()), format_func=lambda x: father_occ_map[x])
        admission_grade = st.number_input("Nilai Masuk", value=120.0)
        displaced = st.selectbox("Pengungsi?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
        special_needs = st.selectbox("Kebutuhan Khusus?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
        debtor = st.selectbox("Punya Tunggakan?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")

    with col3:
        tuition_up_to_date = st.selectbox("Pembayaran Lunas?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
        gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
        scholarship = st.selectbox("Penerima Beasiswa?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
        age_enroll = st.slider("Usia Saat Masuk", 17, 70, 20)
        international = st.selectbox("Mahasiswa Internasional?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
        unemployment = st.number_input("Tingkat Pengangguran", value=10.0)
        inflation = st.number_input("Inflasi", value=1.5)
        gdp = st.number_input("GDP", value=1.0)

    st.markdown("### 📚 Semester 1 & 2 Info")
    col4, col5 = st.columns(2)
    with col4:
        c1_credited = st.number_input("1st Sem: Credited Units", 0)
        c1_enrolled = st.number_input("1st Sem: Enrolled Units", 0)
        c1_eval = st.number_input("1st Sem: Evaluations", 0)
        c1_approved = st.number_input("1st Sem: Approved Units", 0)
        c1_grade = st.number_input("1st Sem: Average Grade", 0.0)
        c1_wo_eval = st.number_input("1st Sem: Without Evaluations", 0)

    with col5:
        c2_credited = st.number_input("2nd Sem: Credited Units", 0)
        c2_enrolled = st.number_input("2nd Sem: Enrolled Units", 0)
        c2_eval = st.number_input("2nd Sem: Evaluations", 0)
        c2_approved = st.number_input("2nd Sem: Approved Units", 0)
        c2_grade = st.number_input("2nd Sem: Average Grade", 0.0)
        c2_wo_eval = st.number_input("2nd Sem: Without Evaluations", 0)

    submitted = st.form_submit_button("🔍 Prediksi")

if submitted:
    input_dict = {
        'Marital_status': marital_status,
        'Application_mode': application_mode,
        'Application_order': application_order,
        'Course': course,
        'Daytime_evening_attendance': daytime_evening,
        'Previous_qualification': prev_qualification,
        'Previous_qualification_grade': prev_qualification_grade,
        'Nacionality': nationality,
        'Mothers_qualification': mother_qual,
        'Fathers_qualification': father_qual,
        'Mothers_occupation': mother_occ,
        'Fathers_occupation': father_occ,
        'Admission_grade': admission_grade,
        'Displaced': displaced,
        'Educational_special_needs': special_needs,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_up_to_date,
        'Gender': 1 if gender == "Male" else 0,
        'Scholarship_holder': scholarship,
        'Age_at_enrollment': age_enroll,
        'International': international,
        'Curricular_units_1st_sem_credited': c1_credited,
        'Curricular_units_1st_sem_enrolled': c1_enrolled,
        'Curricular_units_1st_sem_evaluations': c1_eval,
        'Curricular_units_1st_sem_approved': c1_approved,
        'Curricular_units_1st_sem_grade': c1_grade,
        'Curricular_units_1st_sem_without_evaluations': c1_wo_eval,
        'Curricular_units_2nd_sem_credited': c2_credited,
        'Curricular_units_2nd_sem_enrolled': c2_enrolled,
        'Curricular_units_2nd_sem_evaluations': c2_eval,
        'Curricular_units_2nd_sem_approved': c2_approved,
        'Curricular_units_2nd_sem_grade': c2_grade,
        'Curricular_units_2nd_sem_without_evaluations': c2_wo_eval,
        'Unemployment_rate': unemployment,
        'Inflation_rate': inflation,
        'GDP': gdp
    }

    df_input = pd.DataFrame([input_dict])
    df_scaled = scaler.transform(df_input[scaler.feature_names_in_])
    df_input[scaler.feature_names_in_] = df_scaled

    prediction = model.predict(df_input)[0]
    label = "Dropout" if prediction == 1 else "Graduate"

    st.success(f"Hasil Prediksi: **{label}**")
    st.markdown("### 🔎 Data Lengkap yang Dimasukkan")
    st.write(pd.DataFrame([input_dict]))