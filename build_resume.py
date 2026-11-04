from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
import os

OUT = os.path.join('output', 'pdf', 'Curriculo_Caua_Assumpcao_Tecnologia_Dados_Seguranca.pdf')
os.makedirs(os.path.dirname(OUT), exist_ok=True)

# DejaVu is bundled on Windows systems commonly enough; fall back safely if unavailable.
font_path = r'C:\Windows\Fonts\arial.ttf'
bold_path = r'C:\Windows\Fonts\arialbd.ttf'
if os.path.exists(font_path) and os.path.exists(bold_path):
    pdfmetrics.registerFont(TTFont('Resume', font_path))
    pdfmetrics.registerFont(TTFont('Resume-Bold', bold_path))
else:
    font_path = r'C:\Windows\Fonts\calibri.ttf'
    bold_path = r'C:\Windows\Fonts\calibrib.ttf'
    pdfmetrics.registerFont(TTFont('Resume', font_path))
    pdfmetrics.registerFont(TTFont('Resume-Bold', bold_path))

NAVY = HexColor('#123047')
BLUE = HexColor('#177EAA')
TEXT = HexColor('#22313A')
MUTED = HexColor('#52616B')
LINE = HexColor('#D5E1E7')
PALE = HexColor('#EEF6F9')

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Name', fontName='Resume-Bold', fontSize=20, leading=23, textColor=NAVY, spaceAfter=2))
styles.add(ParagraphStyle(name='Role', fontName='Resume-Bold', fontSize=9.3, leading=12, textColor=BLUE, spaceAfter=6))
styles.add(ParagraphStyle(name='Contact', fontName='Resume', fontSize=8.5, leading=11, textColor=MUTED))
styles.add(ParagraphStyle(name='Section', fontName='Resume-Bold', fontSize=10.2, leading=13, textColor=NAVY, spaceBefore=10, spaceAfter=4, borderWidth=0, borderColor=LINE))
styles.add(ParagraphStyle(name='Body', fontName='Resume', fontSize=8.65, leading=11.6, textColor=TEXT, spaceAfter=3))
styles.add(ParagraphStyle(name='ProjectTitle', fontName='Resume-Bold', fontSize=8.85, leading=11.5, textColor=NAVY, spaceAfter=1))
styles.add(ParagraphStyle(name='Meta', fontName='Resume', fontSize=8.1, leading=10.2, textColor=MUTED, spaceAfter=2))
styles.add(ParagraphStyle(name='Small', fontName='Resume', fontSize=8.25, leading=10.7, textColor=TEXT, spaceAfter=3))
styles.add(ParagraphStyle(name='SideHead', fontName='Resume-Bold', fontSize=8.7, leading=11, textColor=NAVY, spaceBefore=6, spaceAfter=3))
styles.add(ParagraphStyle(name='Side', fontName='Resume', fontSize=8.05, leading=10.7, textColor=TEXT, spaceAfter=4))

def p(txt, style='Body'):
    return Paragraph(txt, styles[style])

def bullets(items, style='Body'):
    return [Paragraph('&bull; ' + x, styles[style]) for x in items]

def section(title, content):
    return [Paragraph(title.upper(), styles['Section']), Table([['']], colWidths=[17.4*cm], rowHeights=[0.6], style=TableStyle([('LINEABOVE',(0,0),(-1,-1),0.7,LINE),('BOTTOMPADDING',(0,0),(-1,-1),0)])), Spacer(1, 2), *content]

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=1.35*cm, rightMargin=1.35*cm, topMargin=1.15*cm, bottomMargin=1.05*cm)
story = []
story += [p('Cauã Soares dos Santos Assumpção', 'Name'), p('TECNOLOGIA | DESENVOLVIMENTO FULL STACK | DADOS | SEGURANÇA DA INFORMAÇÃO', 'Role')]
story += [p('+55 (65) 99649-1665  |  cauassassumpcao@gmail.com  |  github.com/Whoami-C', 'Contact'), p('Barra do Bugres/MT e Nova Iguaçu/RJ  |  Disponibilidade para trabalho remoto', 'Contact'), Spacer(1, 5)]

story += section('Perfil profissional', [p('Estudante de Ciência da Computação na UNEMAT, com conclusão prevista para dezembro de 2026 e experiência como Desenvolvedor de Software na Coggit, contribuindo para o aplicativo de mobilidade UPPS. Reúne prática em desenvolvimento web, APIs REST, bancos de dados e automação com Python, além de conhecimento em monitoramento de segurança, análise de phishing e triagem inicial de alertas. Busca contribuir com soluções bem documentadas, orientadas a dados e às necessidades do produto.')])

story += section('Experiência profissional', [
    p('Desenvolvedor de Software | Coggit', 'ProjectTitle'),
    p('Atuação no desenvolvimento do UPPS, aplicativo de mobilidade urbana e transporte sob demanda, colaborando com a equipe na implementação e evolução de funcionalidades.', 'Body')
])

story += section('Competências técnicas', [
    p('<b>Desenvolvimento:</b> Python, JavaScript, React, HTML, CSS, lógica de programação, orientação a objetos, APIs REST e aplicações full stack.', 'Small'),
    p('<b>Dados:</b> SQL, SQLite, JSON, fundamentos de bancos de dados, análise e organização de dados, consumo de APIs e visualização planejada com Power BI.', 'Small'),
    p('<b>Segurança:</b> SIEM, Windows, análise básica de logs, triagem de alertas e phishing, Nmap, Burp Suite, coleta de evidências, escalonamento e documentação.', 'Small'),
    p('<b>Ferramentas:</b> Git/GitHub, Telegram Bot API, Tkinter, Flask, Socket.IO, sockets TCP, PyInstaller.', 'Small'),
])

story += section('Projetos e resultados', [
    p('Lice Hunter - Monitor de Licitações Públicas | Python, API REST, JSON, Tkinter, Telegram Bot API e PyInstaller', 'ProjectTitle'),
    p('&bull; Consulta a API oficial do PNCP com paginação, retentativas e controle de limite; filtra editais e classifica oportunidades por prazo, município e prioridade.', 'Small'),
    p('&bull; Mantém mais de 6.000 registros brutos e 2.700 oportunidades estruturadas em JSON, com cache para preservar dados válidos durante falhas de API.', 'Small'),
    p('Firewall Simulator | Python, Flask, Socket.IO e sockets TCP', 'ProjectTitle'),
    p('&bull; Simula filtragem por IP, porta e protocolo, gerencia blacklist e regras em JSON e registra conexões em tempo real.', 'Small'),
    p('Caverna Streetwear | React/Vite | cavernastreetwear.com.br', 'ProjectTitle'),
    p('&bull; Website responsivo para loja de tênis, com catálogo, navegação de produtos e carrinho.', 'Small'),
    p('HACKAMT | 1º lugar em 2023 | 2º lugar em 2024', 'ProjectTitle'),
    p('&bull; Criação em equipe de aplicativos voltados ao turismo e comércio local e à contratação no agronegócio.', 'Small'),
])

story += section('Projetos em desenvolvimento', [
    p('Painel Analítico de Licitações Públicas | Python, Pandas, SQL, API PNCP e Power BI', 'ProjectTitle'),
    p('&bull; Em andamento: estruturação de pipeline para consolidar dados de editais e criar indicadores de volume, prazo, município, categoria e oportunidades prioritárias.', 'Small'),
    p('Análise de Dados de Mobilidade Urbana | Python, Pandas, SQL e Power BI', 'ProjectTitle'),
    p('&bull; Em andamento: desenvolvimento de base analítica e dashboards para acompanhar demanda, horários, regiões e padrões de deslocamento, apoiando decisões operacionais.', 'Small'),
    p('Laboratório SOC com SIEM e Windows | Wazuh, Windows e Sysmon', 'ProjectTitle'),
    p('&bull; Em andamento: ambiente para coleta de logs, investigação de alertas e documentação de playbooks de atendimento N1.', 'Small'),
    p('Assistente de Triagem de Phishing | Python', 'ProjectTitle'),
    p('&bull; Em andamento: aplicação para extrair cabeçalhos, URLs e indicadores de e-mails suspeitos e gerar relatório de risco para escalonamento.', 'Small'),
])

story += section('Formação e idiomas', [
    p('<b>Bacharelado em Ciência da Computação</b> | Universidade do Estado de Mato Grosso (UNEMAT) | Conclusão: dezembro de 2026', 'Small'),
    p('Português: fluente | Inglês: intermediário', 'Small'),
])

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE); canvas.setLineWidth(.5)
    canvas.line(doc.leftMargin, 0.75*cm, A4[0]-doc.rightMargin, 0.75*cm)
    canvas.setFont('Resume', 7.4); canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 0.48*cm, 'Cauã Soares dos Santos Assumpção')
    canvas.drawRightString(A4[0]-doc.rightMargin, 0.48*cm, f'Página {doc.page}')
    canvas.restoreState()

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
