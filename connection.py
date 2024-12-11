import pyodbc
conn_str = 'DSN=final_test;UID=sa;PWD=123456'

# 创建连接
conn = pyodbc.connect(conn_str)

# 创建游标对象
cursor = conn.cursor()

# 执行SQL查询
cursor.execute("SELECT * FROM college")

# 获取查询结果
for row in cursor:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()