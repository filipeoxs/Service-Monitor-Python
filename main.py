import subprocess
import sys

# Verifica se o nome do serviço foi especificado como argumento
if len(sys.argv) != 2:
    print("Uso: python monitor.py nomedoservico")
    sys.exit(1)

# Nome do serviço a ser monitorado
service_name = sys.argv[1]

# Função para verificar e reiniciar o serviço, se necessário
def monitorar_e_reiniciar_servico(service_name):
    try:
        # Verifica o status do serviço
        subprocess.check_output(["systemctl", "is-active", "--quiet", service_name])

        print(f"O serviço {service_name} está ativo.")
    except subprocess.CalledProcessError:
        print(f"O serviço {service_name} está inativo. Reiniciando...")
        try:
            subprocess.check_call(["systemctl", "restart", service_name])
            print("Reinicialização concluída.")
        except subprocess.CalledProcessError:
            print("Erro ao reiniciar o serviço.")
            sys.exit(1)

if __name__ == "__main__":
    monitorar_e_reiniciar_servico(service_name)
