import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('../db/hospital.db')

def execute_query(query):
    try:
        # Use pandas to execute the query and return a DataFrame
        df = pd.read_sql_query(query, conn)
        return df
    except sqlite3.Error as e:
        print(f"An error occurred: {e.args[0]}")
        return None

# Example query: List all doctors
doctors_df = execute_query("SELECT * FROM DOCTORS")
print("Doctors:")
print(doctors_df)

# Example query: List all patients of a specific doctor
patients_of_doctor_df = execute_query("""
SELECT PATIENTS.P_NAME
FROM PATIENTS
JOIN P_ASSIGNMENT ON PATIENTS.P_ID = P_ASSIGNMENT.P_ID
JOIN DOCTORS ON P_ASSIGNMENT.D_ID = DOCTORS.D_ID
WHERE DOCTORS.D_NAME = 'JAMES SMITH'
""")
print("\nPatients of Doctor James Smith:")
print(patients_of_doctor_df)

# Close the database connection
conn.close()
