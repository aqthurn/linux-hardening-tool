from checks.check_ufw import run_check as check_ufw
from checks.check_shadow import run_check as check_shadow
from checks.check_ssh import run_check as check_ssh
from utils import GREEN, RED, YELLOW, BOLD, RESET
from reports.reporter import save_json

checks = [check_ufw, check_shadow, check_ssh]

total_pass = 0
total_fail = 0
total_error = 0
resultados = []


for check in checks:
    resultado = check()
    resultados.append(resultado)
    if resultado["status"] == "PASS":
        cor = GREEN
        total_pass += 1
    elif resultado["status"] == "FAIL":
        cor = RED
        total_fail += 1
    else:
        cor = YELLOW
        total_error += 1
    
    print(f"{cor}[{resultado['status']}]{RESET} {BOLD}{resultado['name']}{RESET}")
    print(f"  Mensagem: {resultado['message']}")
    if resultado["fix"]:
        print(f"  {YELLOW}Correcao: {resultado['fix']}{RESET}")

print(f"\n{BOLD}Total: {GREEN}{total_pass} PASS{RESET} | {RED}{total_fail} FAIL{RESET} | {YELLOW}{total_error} ERROR{RESET}")


save_json(resultados)