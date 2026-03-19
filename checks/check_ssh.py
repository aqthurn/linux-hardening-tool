
def run_check():

    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            linhas = f.readlines()

            for linha in linhas:
                linha = linha.strip()

                if "PermitRootLogin" in linha:
                    if linha.startswith("#"):
                        return{
                            "name": "Check de SSH",
                            "status": "FAIL",
                            "message": f"Configuração SSH comentada, valor permite o login pelo root",
                            "fix": "sudo sed -i 's/.*PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config && sudo systemctl restart sshd"
                            }
                    
                    elif "PermitRootLogin no" in linha:
                        return{
                            
                            "name": "Check de SSH",
                            "status": "PASS",
                            "message": f"Configurado corretamente",
                            "fix": None
                            }
                    else:
                        return{        
                            "name": "Check de SSH",
                            "status": "FAIL",
                            "message": f"Configurado incorretamente, valor errado",
                            "fix": "sudo sed -i 's/.*PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config && sudo systemctl restart sshd"
                            }
        
            return{
                    "name": "Check de SSH",
                    "status": "FAIL",
                    "message": f"não foi possível encontrar a linha de configuração",
                    "fix": "echo 'PermitRootLogin no' | sudo tee -a /etc/ssh/sshd_config && sudo systemctl restart sshd"
                    }
        
    except FileNotFoundError:
        return {
            "name": "Check de SSH",
            "status": "ERROR",
            "message": "Arquivo /etc/ssh/sshd_config nao encontrado",
            "fix": "sudo apt install openssh-server"
        }
    except PermissionError:
        return {
            "name": "Check de SSH",
            "status": "ERROR",
            "message": "Sem permissao para ler /etc/ssh/sshd_config",
            "fix": None
        }
    except Exception as e:
        return {
            "name": "Check de SSH",
            "status": "ERROR",
            "message": f"Erro ao executar o check: {str(e)}",
            "fix": None
        }
                
if __name__ == "__main__":
    resultado = run_check()
    print(f"[{resultado['status']}] {resultado['name']}")
    print(f"  Mensagem: {resultado['message']}")
    if resultado["fix"]:
        print(f"  Correcao: {resultado['fix']}")
                
                    
                    
                    