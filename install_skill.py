import os
import platform
import subprocess
import sys
import urllib.request

def install():
    print("🚀 Iniciando instalação da Skill: Cripto360 System Builder...")
    
    # 1. Definir caminhos baseados no OS
    home = os.path.expanduser("~")
    if platform.system() == "Windows":
        skill_path = os.path.join(home, ".gemini", "antigravity", "skills", "cripto360-system-builder")
    else:
        skill_path = os.path.join(home, ".gemini", "antigravity", "skills", "cripto360-system-builder")
    
    # 2. Criar diretório se não existir
    if not os.path.exists(skill_path):
        os.makedirs(skill_path)
        print(f"✅ Diretório criado: {skill_path}")
    
    # 3. URL do arquivo Raw no seu GitHub
    # Vamos baixar o HABILIDADE.md e salvar como SKILL.md para o agente reconhecer
    raw_url = "https://raw.githubusercontent.com/decioalmeida2022/Cripto360-System-Builder/main/HABILIDADE.md"
    target_file = os.path.join(skill_path, "SKILL.md")
    
    try:
        print(f"📥 Baixando Skill do GitHub...")
        urllib.request.urlretrieve(raw_url, target_file)
        print(f"🎉 Skill instalada com sucesso em: {target_file}")
        print("\nAgora você pode perguntar ao seu agente: 'Como posso usar a skill Cripto360?'")
    except Exception as e:
        print(f"❌ Erro ao baixar a skill: {e}")
        print("Verifique sua conexão ou se o repositório é público.")

if __name__ == "__main__":
    install()
