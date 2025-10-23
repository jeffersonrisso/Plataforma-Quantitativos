#!/usr/bin/env python3
"""
CLI para o Pipeline de Quantitativos
"""

import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="Pipeline de Quantitativos - Extração automatizada de projetos"
    )

    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="Diretório de entrada com arquivos de projeto"
    )

    parser.add_argument(
        "-o", "--output", 
        type=str,
        default="./resultados",
        help="Diretório de saída para resultados"
    )

    parser.add_argument(
        "-c", "--config",
        type=str,
        help="Arquivo de configuração YAML"
    )

    parser.add_argument(
        "--formatos",
        nargs="+",
        default=[".pdf", ".dwg", ".rvt"],
        help="Formatos de arquivo para processar"
    )

    parser.add_argument(
        "--paralelo",
        action="store_true",
        default=True,
        help="Usar processamento paralelo"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Modo verboso"
    )

    args = parser.parse_args()

    try:
        # Importar dentro da função para evitar dependências circulares
        from pipeline_quantitativos import PipelineIntegrado

        # Inicializar pipeline
        config_path = Path(args.config) if args.config else None
        pipeline = PipelineIntegrado(config_path)

        # Processar arquivos
        print("🚀 Iniciando processamento...")
        resultados = pipeline.processar_lote(Path(args.input))

        # Salvar resultados
        output_dir = Path(args.output)
        arquivo_salvo = pipeline.salvar_resultados(resultados, output_dir)

        # Estatísticas
        sucessos = len([r for r in resultados.values() if r.get('status', '').startswith('sucesso')])
        total = len(resultados)

        print("✅ Processamento concluído!")
        print("📊 Estatísticas:")
        print(f"   • Arquivos processados: {total}")
        print(f"   • Sucessos: {sucessos}")
        print(f"   • Taxa de sucesso: {(sucessos/total*100):.1f}%")
        print(f"   • Resultados salvos em: {arquivo_salvo}")

    except Exception as e:
        print(f"❌ Erro durante o processamento: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
