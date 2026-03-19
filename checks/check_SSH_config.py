

def run_check():
    configs_esperadas = {
        "MaxAuthTries": "4",
        "PasswordAuthentication": "no",
        "X11Forwarding": "no"
    }



    problemas = []



    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            linhas = f.readlines()

            for linha in linhas:
                linha = linha.strip()
            
                for config, valor_esperado in configs_esperadas.items():
                    if config in linha:
                        if linha.startswith("#"):
                            problemas.append(f"{config} esta comentado")
                        elif f"{config} {valor_esperado}" not in linha:
                            problemas.append(f"{config} com valor incorreto")
            if not problemas:
                return {
                    "name": "SSH Configuracoes Extras",
                     "status": "PASS",
                     "message": "Todas as configuracoes SSH estao corretas",
                     "fix": None
                                }
            else:
                return{
                        "name": "SSH Configuracoes Extras",
                        "status": "FAIL",
                        "message": "; ".join(problemas),
                        "fix": "Editar /etc/ssh/sshd_config com os valores corretos e rodar sudo systemctl restart sshd"
                            }
    except FileNotFoundError:
        return {
            "name": "SSH Configuracoes Extras",
            "status": "ERROR",
            "message": "Arquivo /etc/ssh/sshd_config nao encontrado",
            "fix": "sudo apt install openssh-server"
        }
    except PermissionError:
        return {
            "name": "SSH Configuracoes Extras",
            "status": "ERROR",
            "message": "Sem permissao para ler /etc/ssh/sshd_config",
            "fix": None
        }
    except Exception as e:
        return {
            "name": "SSH Configuracoes Extras",
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
                
                            

                            