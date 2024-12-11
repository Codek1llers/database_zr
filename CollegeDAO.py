class CollegeDAO:
    def __init__(self, connection):
        self.conn = connection

    def add_college(self, code, name, total_admission, recommendation_admission):
        sql = "INSERT INTO college (college_code, college_name, total_admission, recommendation_admission) VALUES (%s, %s, %s, %s)"
        with self.conn.cursor() as cursor:
            cursor.execute(sql, (code, name, total_admission, recommendation_admission))
            self.conn.commit()

    def delete_college(self, name):
        sql = "DELETE FROM college WHERE college_name = %s"
        with self.conn.cursor() as cursor:
            cursor.execute(sql, (name,))
            self.conn.commit()
