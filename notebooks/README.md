# 🏗️ Pipeline de Quantitativos - Versão 1.0.0

## 📋 Descrição

Pipeline automatizado para extração e processamento de quantitativos de projetos arquitetônicos nos formatos PDF, DWG e RVT.

## 🚀 Instalação

### Instalação via pip
```bash
pip install pipeline_quantitativos
```

### Instalação a partir do código fonte
```bash
git clone https://github.com/empresa/pipeline-quantitativos
cd pipeline-quantitativos
pip install -e .
```

## 💻 Uso Básico

### Via linha de comando
```bash
pipeline-quantitativos --input ./projetos --output ./resultados
```

### Via Python
```python
from pipeline_quantitativos import PipelineIntegrado

# Inicializar pipeline
pipeline = PipelineIntegrado()

# Processar diretório
resultados = pipeline.processar_lote('./projetos')

# Salvar resultados
pipeline.salvar_resultados(resultados)
```

### Via API REST
```bash
# Iniciar API
python -m pipeline_quantitativos.api

# Fazer upload de arquivo
curl -X POST -F "file=@projeto.pdf" http://localhost:5000/upload
```

## 📁 Estrutura do Projeto

```
pipeline_quantitativos/
├── core/           # Módulos principais
├── processadores/  # Processadores de arquivos
├── api/           # API REST
├── utils/         # Utilitários
└── cli.py         # Interface de linha de comando
```

## 🔧 Configuração

Crie um arquivo `config.yaml`:

```yaml
diretorio_entrada: ./data/raw
diretorio_saida: ./data/processed
formatos_suportados: [.pdf, .dwg, .rvt]
processamento_paralelo: true
max_workers: 4
```

## 📊 Formatos Suportados

- **PDF**: Extração de texto e tabelas
- **DWG**: Entidades CAD e textos
- **RVT**: Elementos BIM (em desenvolvimento)

## 🛠️ Desenvolvimento

### Configurar ambiente de desenvolvimento
```bash
git clone https://github.com/empresa/pipeline-quantitativos
cd pipeline-quantitativos
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
pip install -e .
```

### Executar testes
```bash
python -m pytest tests/
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📞 Suporte

- 📧 Email: suporte@empresa.com
- 🐛 Issues: [GitHub Issues](https://github.com/empresa/pipeline-quantitativos/issues)
- 📚 Documentação: [Wiki](https://github.com/empresa/pipeline-quantitativos/wiki)
