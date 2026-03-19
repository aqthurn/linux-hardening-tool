import subprocess

def run_check():
    try: 
        result = subprocess.run(
            ["sudo", "ufw", "status"],
            capture_output=True,
            text=True
        )
        if "Status: active" in result.stdout:
            return{
                "name": "UFW Firewall",
                "status": "Pass",
                "message": "Firewall UFW está ativo",
                "fix": None
            }
        else:
            return{
                "name": "UFW Firewall",
                "status": "Fail",
                "message": "Firewall UFW está desativado ou nao instalado",
                "fix": "sudo ufw enable"
            }
   
    
    
    except FileNotFoundError:
        return{
            "name": "UFW Firewall",
                "status": "ERROR",
                "message": "Comando UFW nao encontrado. UFW nao esta instalado",
                "fix": "sudo apt install ufw"
        }
    except Exception as e:
        return{
            "name": "UFW Firewall",
                "status": "Fail",
                "message": f"Erro ao executar o check: {str(e)}",
                "fix": None
            }


if __name__ == "__main__":
    resultado = run_check()
    print(f"[{resultado['status']}] {resultado['name']}")
    print(f"  Mensagem: {resultado['message']}")
    if resultado["fix"]:
        print(f"  Correcao: {resultado['fix']}")