# 🎓 Sistema de Certificados (Python)

Projeto pessoal para **geração automática de certificados** a partir de uma planilha CSV, usando **Pandas** e **Pillow**.

O sistema lê os dados de alunos (nomes fictícios) e suas porcentagens de presença, insere o nome no modelo de certificado e exporta em **PDF** para os que atingirem a presença mínima.

---

## ✨ Funcionalidades

- **Leitura de planilha**: nomes e presenças via `pandas`.
- **Verificação automática**: só gera certificado para quem atinge a presença mínima.
- **Personalização visual**: insere o nome no modelo usando fonte e tamanho definidos.
- **Exportação em PDF**: certificados salvos na pasta `certificados_gerados`.

---

## 📚 Bibliotecas

- **Pandas** → Utilizada para ler e manipular os dados da planilha CSV.
- **Pillow (PIL)** → Usada para abrir o modelo de certificado, inserir o nome com formatação personalizada e exportar em PDF.
- **os** → Responsável por criar a pasta de saída automaticamente e gerenciar caminhos de arquivos no sistema.

> 📌 Todos os nomes no CSV são **fictícios** e usados apenas para demonstração.
