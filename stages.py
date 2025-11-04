from datetime import date

class Pessoa:
    def __init__(self, nome: str, email: str, empresa: str):
        self.nome = nome
        self.email = email
        self.empresa = empresa

    def exibir_informacoes(self):
        return f"Nome: {self.nome} | Empresa: {self.empresa} | E-mail: {self.email}"


class Comprador(Pessoa):
    def __init__(self, nome: str, email: str, empresa: str, interesse: int = 1):
        super().__init__(nome, email, empresa)
        self.interesse = interesse

    def tipo_lead(self):
        raise NotImplementedError("Método deve ser implementado pela subclasse.")


class LeadFrio(Comprador):
    def tipo_lead(self):
        return "Lead Frio (baixo interesse)"


class LeadQuente(Comprador):
    def tipo_lead(self):
        return "Lead Quente (alto interesse)"


class Vendedor(Pessoa):
    def __init__(self, nome: str, email: str, empresa: str, setor: str):
        super().__init__(nome, email, empresa)
        self.setor = setor

    def exibir_informacoes(self):
        return f"[Vendedor] {super().exibir_informacoes()} | Setor: {self.setor}"


class Administrador(Pessoa):
    def __init__(self, nome: str, email: str, empresa: str, nivel_acesso: str):
        super().__init__(nome, email, empresa)
        self.nivel_acesso = nivel_acesso

    def exibir_informacoes(self):
        return f"[Administrador] {super().exibir_informacoes()} | Nível de acesso: {self.nivel_acesso}"


class Model:
    def __init__(self, nome: str, empresa: str, email: str, interesse: int = 1, stage: str = "novo"):
        if interesse >= 4:
            self.pessoa = LeadQuente(nome, email, empresa, interesse)
        else:
            self.pessoa = LeadFrio(nome, email, empresa, interesse)

        self.stage = stage
        self.created = date.today().isoformat()

    def to_dict(self):
        return {
            "name": self.pessoa.nome,
            "company": self.pessoa.empresa,
            "email": self.pessoa.email,
            "stage": self.stage,
            "created": self.created,
            "lead_type": self.pessoa.tipo_lead(),
            "interesse": self.pessoa.interesse
        }

    def exibir_informacoes(self):
        return f"{self.pessoa.exibir_informacoes()} | Etapa: {self.stage} | {self.pessoa.tipo_lead()}"
