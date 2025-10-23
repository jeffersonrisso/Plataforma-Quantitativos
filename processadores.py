# processadores.py
"""
MÓDULO COMPARTILHADO - PROCESSADORES MULTIFORMATO
Todos os notebooks importam deste arquivo
"""

import re
from pathlib import Path
from collections import Counter

try:
    import dxfgrabber
    DWG_SUPORTADO = True
except ImportError:
    DWG_SUPORTADO = False

try:
    import clr
    RVT_SUPORTADO = True  
except ImportError:
    RVT_SUPORTADO = False

# =============================================================================
# PROCESSADOR DWG
# =============================================================================

class ProcessadorDWG:
    """Processador para arquivos DWG (AutoCAD)"""
    
    def __init__(self):
        self.entidades_relevantes = [
            'LINE', 'CIRCLE', 'ARC', 'TEXT', 'MTEXT', 
            'INSERT', 'DIMENSION', 'LWPOLYLINE', 'LAYER'
        ]
        self.padroes_materiais = self._criar_padroes_materiais()
    
    def _criar_padroes_materiais(self):
        """Padrões regex para identificar materiais em textos DWG"""
        return {
            'codigo_descricao': r'(M\d{2,4})\s*[-–]?\s*([^-–]+?)',
            'dimensoes': r'(\d+)\s*x\s*(\d+)(?:\s*x\s*(\d+))?\s*(cm|m|mm)',
            'quantidade': r'(\d+)\s*(un|UN|pç|pc|und|m²|m³)'
        }
    
    def extrair_dados(self, dwg_path):
        """Extrai dados de arquivo DWG"""
        print(f"   🔧 Processando DWG: {dwg_path.name}")
        
        if not DWG_SUPORTADO:
            return {'erro': 'Dependências DWG não disponíveis'}
        
        try:
            import dxfgrabber
            
            # Ler arquivo DWG
            dwg = dxfgrabber.readfile(str(dwg_path))
            
            dados_extraidos = {
                'metadados': self._extrair_metadados(dwg),
                'entidades': self._extrair_entidades(dwg),
                'textos': self._extrair_textos(dwg),
                'blocos': self._extrair_blocos(dwg),
                'camadas': self._extrair_camadas(dwg)
            }
            
            # Interpretar quantitativos
            quantitativos = self._interpretar_quantitativos(dados_extraidos)
            
            return {
                'status': 'sucesso',
                'arquivo': dwg_path.name,
                'dados_brutos': dados_extraidos,
                'quantitativos': quantitativos
            }
            
        except Exception as e:
            print(f"   ❌ Erro no processamento DWG: {e}")
            return {'status': 'erro', 'erro': str(e)}
    
    # ... (implementações completas das outras métodos)
    def _extrair_metadados(self, dwg):
        return {
            'versao_dxf': getattr(dwg, 'dxfversion', 'Desconhecida'),
            'numero_entidades': len(dwg.entities),
            'camadas': len(dwg.layers),
            'blocos': len(dwg.blocks)
        }
    
    def _extrair_entidades(self, dwg):
        entidades = []
        for entity in dwg.entities:
            if entity.dxftype in self.entidades_relevantes:
                entidade_data = {
                    'tipo': entity.dxftype,
                    'camada': getattr(entity, 'layer', '0'),
                    'cor': getattr(entity, 'color', 0)
                }
                if entity.dxftype in ['TEXT', 'MTEXT']:
                    entidade_data['texto'] = getattr(entity, 'text', '')
                elif entity.dxftype == 'INSERT':
                    entidade_data['nome_bloco'] = getattr(entity, 'name', '')
                entidades.append(entidade_data)
        return entidades
    
    def _extrair_textos(self, dwg):
        textos = []
        for entity in dwg.entities:
            if entity.dxftype in ['TEXT', 'MTEXT']:
                texto = getattr(entity, 'text', '').strip()
                if texto and len(texto) > 2:
                    textos.append({
                        'texto': texto,
                        'camada': getattr(entity, 'layer', '0'),
                        'tipo': entity.dxftype
                    })
        return textos
    
    def _extrair_blocos(self, dwg):
        return [{'nome': block.name, 'numero_entidades': len(block.entities)} 
                for block in dwg.blocks]
    
    def _extrair_camadas(self, dwg):
        return [{'nome': layer.name, 'cor': layer.color, 'visivel': not layer.off}
                for layer in dwg.layers]
    
    def _interpretar_quantitativos(self, dados):
        contagem_entidades = Counter([e['tipo'] for e in dados['entidades']])
        materiais = self._extrair_materiais_textos(dados['textos'])
        mobiliario = self._analisar_mobiliario(dados['blocos'], dados['entidades'])
        
        return {
            'estatisticas_entidades': dict(contagem_entidades),
            'total_entidades': len(dados['entidades']),
            'total_textos': len(dados['textos']),
            'materiais_encontrados': materiais,
            'mobiliario_equipamentos': mobiliario,
            'numero_camadas': len(dados['camadas']),
            'numero_blocos': len(dados['blocos'])
        }
    
    def _extrair_materiais_textos(self, textos):
        materiais = []
        for texto_info in textos:
            texto = texto_info['texto']
            for padrao_nome, padrao_regex in self.padroes_materiais.items():
                matches = re.finditer(padrao_regex, texto, re.IGNORECASE)
                for match in matches:
                    materiais.append({
                        'texto_original': texto,
                        'padrao': padrao_nome,
                        'match': match.group(),
                        'camada': texto_info['camada']
                    })
        return materiais
    
    def _analisar_mobiliario(self, blocos, entidades):
        keywords = ['cadeira', 'mesa', 'armario', 'estante', 'sofá', 'poltrona']
        mobiliario = []
        for bloco in blocos:
            nome_bloco = bloco['nome'].lower()
            for keyword in keywords:
                if keyword in nome_bloco:
                    mobiliario.append({
                        'tipo': 'bloco', 'nome': bloco['nome'],
                        'categoria': keyword, 'entidades': bloco['numero_entidades']
                    })
                    break
        return mobiliario

# =============================================================================
# PROCESSADOR RVT (para futuro)
# =============================================================================

class ProcessadorRVT:
    """Processador para arquivos RVT (Revit)"""
    def extrair_dados(self, rvt_path):
        return {'status': 'nao_implementado', 'mensagem': 'Revit API em desenvolvimento'}

print("✅ Módulo processadores.py carregado!")
print(f"📊 Status: DWG_SUPORTADO = {DWG_SUPORTADO}")