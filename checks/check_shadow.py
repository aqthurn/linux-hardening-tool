import os
import stat


def run_check():
    try: 
        info = os.stat("/etc/shadow")

        permissoes = stat.S_IMODE(info.st_mode)

        if permissoes <= 0o640:
            return{
                "name": "Check de permissões",
                "status": "PASS",
                "message": "Seguro",
                "fix": None
            }
        else: 
            return{
                "name": "Check de permissões",
                "status": "FAIL",
                "message": "Não seguro permissoes abertas",
                "fix": "sudo chmod 640 /etc/shadow"
            }
    except FileNotFoundError:
        return{
                "name": "Check de permissões",
                "status": "ERROR",
                "message": "Não foi possível ler as permissões",
                "fix": None
        }
    except PermissionError:
        return{
                "name": "Check de permissões",
                "status": "ERROR",
                "message": "Sem permissao para verificar /etc/shadow", 
                "fix": None
            }
    
    except Exception as e:
        return{
                "name": "Check de permissões",
                "status": "FAIL",
                "message": f"Erro ao executar o check: {str(e)}",
                "fix": None
            }
    

if __name__ == "__main__":
    resultado = run_check()
    print(f"[{resultado['status']}] {resultado['name']}")
    print(f"  Mensagem: {resultado['message']}")
    if resultado["fix"]:
        print(f"  Correcao: {resultado['fix']}")