import subprocess


def run_check():
    servicos_desnecessarios = ["ModemManager", "avahi-daemon", "cups", "bluetooth"]

    problemas = []

    try:
        for servico in servicos_desnecessarios:
            result = subprocess.run(
                ["systemctl", "is-active", servico],
                capture_output=True,
                text=True
            )

            if result.stdout.strip() == "active":
                problemas.append(f"{servico} esta ativo")

        if not problemas:
            return {
                "name": "Servicos Desnecessarios",
                "status": "PASS",
                "message": "Nenhum servico desnecessario ativo",
                "fix": None
            }
        else:
            return {
                "name": "Servicos Desnecessarios",
                "status": "FAIL",
                "message": "; ".join(problemas),
                "fix": "sudo systemctl disable --now <servico> para cada servico listado"
            }
    except Exception as e:
        return {
            "name": "Servicos Desnecessarios",
            "status": "ERROR",
            "message": f"Erro ao verificar servicos: {str(e)}",
            "fix": None
        }
                                        
                 










if __name__ == "__main__":
    resultado = run_check()
    print(f"[{resultado['status']}] {resultado['name']}")
    print(f"  Mensagem: {resultado['message']}")
    if resultado["fix"]:
        print(f"  Correcao: {resultado['fix']}")
                
                            


