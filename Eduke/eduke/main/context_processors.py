from django.db import connection

def total_unread_messages(request):
    user_id = None
    
    if 'class_id' in request.session:
        with connection.cursor() as cursor:
            cursor.execute("SELECT user_id FROM main_classes WHERE id = %s", [request.session['class_id']])
            row = cursor.fetchone()
            if row: user_id = row[0]
            
    elif 'subject_id' in request.session:
        with connection.cursor() as cursor:
            cursor.execute("SELECT user_id FROM main_subjects WHERE id = %s", [request.session['subject_id']])
            row = cursor.fetchone()
            if row: user_id = row[0]
            
    elif 'student_id' in request.session:
        with connection.cursor() as cursor:
            cursor.execute("SELECT user_id FROM main_students WHERE id = %s", [request.session['student_id']])
            row = cursor.fetchone()
            if row: user_id = row[0]
            
    elif 'parent_id' in request.session:
        with connection.cursor() as cursor:
            cursor.execute("SELECT user_id FROM main_parents WHERE id = %s", [request.session['parent_id']])
            row = cursor.fetchone()
            if row: user_id = row[0]
            
    unread_count = 0
    if user_id:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM main_chat WHERE receiver_id = %s AND is_read = 0", [user_id])
            row = cursor.fetchone()
            if row: unread_count = row[0]
            
    return {'global_unread_chat_count': unread_count}
