def run_check():
    try:
        uid0_users = []
        with open('/etc/passwd', 'r') as f:
            for linha in f:
                partes = linha.strip().split(':')
                if len(partes) > 2 and partes[2] == '0':
                    uid0_users.append(partes[0])
        if uid0_users == ["root"]:
            return {
                "name": "check_uid0",
                "status": "Pass",
                "message": "Apenas o usuário 'root' tem UID 0."
                "fix" : None
            }

        extras = [user for user in uid0_users if user != "root"]
        if extras: 
            return {
                "name": "check_uid0",
                "status": "FAIL",
                "message": f"Usuários com UID 0 além do 'root': {', '.join(extras)}.",
                "fix": f"sudo usermod -u <novo_uid> {extras[0]}"

            
            }
        return {
            "name": "check_uid0",
            "status": "FAIL",
            "message": "Nenhum usuário com UID 0 encontrado.",
            "fix": None
        }
    EXCEPT FileNotFoundError:
        return {
            "name": "check_uid0",
            "status": "FAIL",
            "message": "Arquivo /etc/passwd não encontrado.",
            "fix": None
        }
    EXCEPT PermissionError:
        return {
            "name": "check_uid0",   
            "status": "FAIL",
            "message": "Permissão negada ao acessar /etc/passwd.",
            "fix": None
        }
    EXCEPT Exception as e:
        return {
            "name": "check_uid0",
            "status": "FAIL",
            "message": f"Erro ao verificar usuários com UID 0: {str(e)}
            ",
            "fix": None
        }   

if __name__ == "__main__":
    resultado = run_check()
    print(f"[{resultado['status']}] {resultado['name']}")
    print(f"  Mensagem: {resultado['message']}")
    if resultado["fix"]:
        print(f"  Correcao: {resultado['fix']}")