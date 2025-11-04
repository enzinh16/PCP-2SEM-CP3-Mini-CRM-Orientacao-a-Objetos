from stages import Model
from repo import ModelRepository


class Main:
    def __init__(self):
        self.repo = ModelRepository()

    # Adiciona um novo lead
    def add_lead(self):
        print("\n=== Adicionar Lead ===")
        nome = input("Nome: ").strip()
        empresa = input("Empresa: ").strip()
        email = input("E-mail: ").strip()

        if not nome or not email or "@" not in email:
            print("Nome e e-mail válidos são obrigatórios.")
            return

        try:
            interesse = int(input("Nível de interesse (1 a 5): ").strip())
            if interesse < 1 or interesse > 5:
                raise ValueError
        except ValueError:
            print("Valor inválido. Informe um número de 1 a 5.")
            return

        lead = Model(nome, empresa, email, interesse)
        self.repo.add_lead(lead.to_dict())
        print(f"Lead adicionado com sucesso! ({lead.pessoa.tipo_lead()})")

    # Lista todos os leads
    def list_leads(self):
        print("\n=== Lista de Leads ===")
        leads = self.repo.read_leads()
        if not leads:
            print("Nenhum lead cadastrado.")
            return

        print(f"\n{'#':<3} {'Nome':<20} {'Empresa':<15} {'E-mail':<30} {'Tipo':<35} {'Interesse':<10}")
        print("-" * 117)
        for i, l in enumerate(leads):
            print(
                f"{i:<3} {l['name']:<20} {l['company']:<15} {l['email']:<30} {l.get('lead_type', '—'):<35} {l.get('interesse', '—')}"
            )

    # Busca leads por nome, empresa ou e-mail
    def search_leads(self):
        print("\n=== Buscar Leads ===")
        q = input("Buscar por: ").strip()
        if not q:
            print("Consulta vazia.")
            return

        results = self.repo.search_leads(q)
        if not results:
            print("Nenhum resultado encontrado.")
            return

        print(f"\n{'#':<3} {'Nome':<20} {'Empresa':<15} {'E-mail':<25} {'Tipo':<22} {'Interesse':<10}")
        print("-" * 95)
        for i, l in enumerate(results):
            print(
                f"{i:<3} {l['name']:<20} {l['company']:<15} {l['email']:<25} {l.get('lead_type', '—'):<22} {l.get('interesse', '—')}"
            )

    # Exporta os leads para CSV
    def export_leads(self):
        path = self.repo.export_csv()
        if path is None:
            print("Erro ao exportar. Feche o arquivo se estiver aberto e tente novamente.")
        else:
            print(f"Exportado com sucesso para: {path}")

    def run(self):
        while True:
            print_menu()
            op = input("Escolha: ").strip()
            if op == "1":
                self.add_lead()
            elif op == "2":
                self.list_leads()
            elif op == "3":
                self.search_leads()
            elif op == "4":
                self.export_leads()
            elif op == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")


def print_menu():
    print("\nMini CRM de Leads")
    print("[1] Adicionar lead")
    print("[2] Listar leads")
    print("[3] Buscar leads")
    print("[4] Exportar CSV")
    print("[0] Sair")


if __name__ == "__main__":
    Main().run()
