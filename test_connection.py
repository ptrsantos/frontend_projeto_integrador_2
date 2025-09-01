import pymysql

# Teste de conexão simples
try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='clinica_mentalize',
        charset='utf8mb4'
    )
    print("✅ Conexão com MySQL bem-sucedida!")
    
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print(f"📋 Tabelas encontradas: {[table[0] for table in tables]}")
        
    connection.close()
    
except Exception as e:
    print(f"❌ Erro de conexão: {e}")
    print("\n💡 Tente ajustar as credenciais:")
    print("- Para MySQL com senha: user='root', password='sua_senha'")
    print("- Para XAMPP/WAMP: user='root', password=''")
    print("- Para outro usuário: user='seu_usuario', password='sua_senha'")