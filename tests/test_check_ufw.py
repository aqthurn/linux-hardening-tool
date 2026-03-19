from checks.check_ufw import run_check

resultado = run_check()

assert "name" in resultado, "Faltou a chave 'name'"
assert "status" in resultado, "Faltou a chave 'status'"
assert "message" in resultado, "Faltou a chave 'message'"
assert "fix" in resultado, "Faltou a chave 'fix'"


assert resultado["status"] in ["PASS", "FAIL", "ERROR"], "Status invalido"

print(f"Resultado: [{resultado['status']}] {resultado['name']}")
print(f"Mensagem: {resultado['message']}")
print("Todos os testes passaram")

