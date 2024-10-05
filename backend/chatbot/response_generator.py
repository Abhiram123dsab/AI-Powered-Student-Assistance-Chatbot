from database.db_connector import get_db_connection

def generate_response(intent, message):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()

        if intent == "admission":
            cursor.execute("SELECT admission_info FROM college_info LIMIT 1")
            admission_info = cursor.fetchone()[0]
            return f"Regarding admissions: {admission_info}"

        elif intent == "fee":
            cursor.execute("SELECT fee_structure FROM college_info LIMIT 1")
            fee_info = cursor.fetchone()[0]
            return f"Here's information about fees: {fee_info}"

        elif intent == "scholarship":
            cursor.execute("SELECT scholarship_info FROM college_info LIMIT 1")
            scholarship_info = cursor.fetchone()[0]
            return f"About scholarships: {scholarship_info}"

        else:
            return "I'm sorry, I couldn't understand your query. Could you please rephrase or ask about admissions, fees, or scholarships?"

    finally:
        cursor.close()
        conn.close()