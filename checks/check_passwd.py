import os
import stat


def run_check():
    try: 
        info = os.stat("/etc/passwd")

        permissoes = stat.S_IMODE(info.st_mode)

        if permissoes <= 0o644:
            return{
                "name": "Check de passwd",
                "status": "PASS",
                "message": "Seguro",
                "fix": None
            }
        else: 
            return{
                "name": "Check de passwd",
                "status": "FAIL",
                "message": "Não seguro permissoes abertas",
                "fix": "sudo chmod 644 /etc/passwd"
            }
    except FileNotFoundError:
        return{
                "name": "Check de passwd",
                "status": "ERROR",
                "message": "Não foi possível ler as permissões",
                "fix": None
        }
    except PermissionError:
        return{
                "name": "Check de passwd",
                "status": "ERROR",
                "message": "Sem permissao para verificar /etc/passwd", 
                "fix": None
            }
    
    except Exception as e:
        return{
                "name": "Check de passwd",
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