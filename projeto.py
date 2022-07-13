'''Participantes: João Felipe Milesi Camargo, Luan Moura de Lima e Luiz Henrique Marcucci'''

gabarito=['b','d','c','a','a','c','e','a','d','e']
resposta=[]
explicacao=['A resposta correta da pergunta 1 é a B, pois a a principal fonte de energia utilizada no mundo é de combustíveis fósseis (fontes não renovaveis)',
            'A resposta correta da pergunta 2 é a D, pois atualmente, 90% da energia elétrica consumida no Brasil advém de usinas hidrelétricas',
            'A resposta correta da pergunta 3 é a C, pois fontes de energia como Combustíveis fósseis são finitas, um dia pode acabar',
            'A resposta correta da pergunta 4 é a A, pois o gás natural não pode ser reutilizado e é um recurso finito',
            'A resposta correta da pergunta 5 é a A, por conta dos alagamentos, as árvores na região alagada apodrecem e se decompõe. O processo de decomposição de algumas plantas dessa forma pode causar a emissão de gás metano.',
            'A resposta correta da pergunta 6 é a C, pois as placas de energia solar são compostas de várias camadas diferentes. Uma delas, a célula fotovoltaica só pode ser produzida com a utilização do silício como matéria-prima.',
            'A resposta correta da pergunta 7 é a E, pois durante o processo de geração de energia, transforma-se agua liquida em vapor. Para isso, queima-se alguma combustível, o que causa a emissão de CO2. O CO2 é considerado o principal gás responsável pelo aquecimento global.',
            'A resposta correta da pergunta 8 é a A, pois a principal fonte de energia renovável no Brasil é a hidrelétrica, que representa mais de 60%, seguida pela eólica (cerca de 9%), biomassa e biogás (cerca de 9%) e solar centralizada (cerca de 1%).',
            'A resposta correta da pergunta 9 é a D, pois os maiores parques estão na região Nordeste. Em julho, foram quatro recordes de geração eólica média e quatro de geração instantânea (pico). Segundo o ministério, em um único dia, a média inédita chegou a 11.399 MW, suficiente para abastecer a 102% da região Nordeste durante 24 horas.',
            'A resposta correta da pergunta 10 é a E, pois a energia solar é a que mais cresce no Brasil. Por estar situado próximo a linha do Equador, o Brasil tem excelentes níveis de insolação e de irradiação solar, então, com o desenvolvimento tecnológico das placas solares, dos equipamentos solares, isso proporcionou a redução dos custos. Para se ter uma ideia, no mês de agosto, o Brasil alcançou 10 gigawatts de capacidade instalada.']

def pergunta1():
    print('Qual a fonte de energia mais utilizada no mundo?')
    print('a) Solar\nb) Combustíveis Fósseis\nc) Eólica\nd) Hídrica')
    resposta1=input('Digite a sua resposta: ').lower()
    while resposta1 != 'a' and resposta1 != 'b' and resposta1 != 'c' and resposta1 != 'd':
        resposta1=input('Digite a sua resposta: ').lower()
    resposta.append(resposta1)

def pergunta2():
    print('Qual é a principal fonte de energia do brasil?')
    print('a) Combustíveis Fósseis\nb) Núclear\nc) Eólica\nd) Hidroelétrica\ne) Solar')
    resposta2=input('Digite a sua resposta: ').lower()
    while resposta2 != 'a' and resposta2 != 'b' and resposta2 != 'c' and resposta2 != 'd' and resposta2 != 'e':
        resposta2=input('Digite a sua resposta: ').lower()
    resposta.append(resposta2)

def pergunta3():
    print('Por que fontes de energias limpas são soluções para o futuro?')
    print('a) São mais baratas.\nb) Maior facilidade para produzir\nc) As outras fontes são finitas\nd) Nunca afeta o meio ambiente')
    resposta3=input('Digite a sua resposta: ').lower()
    while resposta3 != 'a' and resposta3 != 'b' and resposta3 != 'c' and resposta3 != 'd':
        resposta3=input('Digite a sua resposta: ').lower()
    resposta.append(resposta3)

def pergunta4():
    print('Todos os recursos que tem capacidade de se refazer ou não são limitados são renováveis. Sendo assim, assinale a alternativa que NÃO corresponde a uma fonte de energia renovável:')
    print('a) Gás natural\nb) Eólica\nc) Biocombustível\nd) Hidrelétrica')
    resposta4=input('Digite a sua resposta: ').lower()
    while resposta4 != 'a' and resposta4 != 'b' and resposta4 != 'c' and resposta4 != 'd':
        resposta4=input('Digite a sua resposta: ').lower()
    resposta.append(resposta4)

def pergunta5():
    print('A fonte de energia renovável hidraulica (usinas hidrelétricas) é a mais utilizada no Brasil. Como benefício, há a não emissão de CO2 na produção de energia. Como prejuízo, tem-se os alagamentos na construção de barragens. Por que os alagamentos são prejudiciais ao meio ambiente?')
    print('a) Podem causar a emissão de gás metano (CH4)\nb) Os alagamentos aumentam demais a umidade em certa região de um rio, o que pode causar um desequilíbrio ambiental.\nc) As zonas alagadas facilitam a pesca. Isso faz a população de peixes diminuir e causa um desequilíbrio na cadeia alimentar.\nd) Isso estimula o uso por seres humanos dos lagos que se formam ao redor. Como consequência, muitos animais aquáticos deixam de habitar a região.\ne) Nem sempre as barragens, causadoras dos alagamentos, suportam segurar tanta água. Assim, O rompimento das barragens inibe o fluxo normal do rio.')
    resposta5=input('Digite a sua resposta: ').lower()
    while resposta5 != 'a' and resposta5 != 'b' and resposta5 != 'c' and resposta5 != 'd' and resposta5 != 'e':
        resposta5=input('Digite a sua resposta: ').lower()
    resposta.append(resposta5)

def pergunta6():
    print('O Brasil é um país com forte potencial na produção de energia fotovoltaica (energia gerada por placas de energia solar) por conta da alta presença de radiação solar no seu território. Um outro fator a favor do crescimento dessa fonte de energia no país é:')
    print('a) A acessibilidade a esse meio de energia no caso de instalação de placas fotovoltaicas em casas, pois a riqueza é bem distribuída no país.\nb) A presençao de diamante na construção de placas solares, mineral abundante em território brasileiro.\nc)A presençao de silício na construção de placas solares, mineral abundante em território brasileiro.\nd) As placas solares são amplamente comercializadas no bloco econômico Mercosul, do qual o Brasil faz parte e, por isso, tem privilégios nas negociações internas.\ne) As placas solares são amplamente comercializadas pela China, importante parceiro comercial do Brasil.')
    resposta6=input('Digite a sua resposta: ').lower()
    while resposta6 != 'a' and resposta6 != 'b' and resposta6 != 'c' and resposta6 != 'd' and resposta6 != 'e':
        resposta6=input('Digite a sua resposta: ').lower()
    resposta.append(resposta6)

def pergunta7():
    print('As usinas termelétricas são instalações insdustriais que utilizam-se da queima de combustíveis para gerar energia elétrica. Apesar de ser responsável por grande parte da energia gerada no mundo, esta não é considerada uma fonte sustentável, pois:')
    print('a) Frequentemente causam acidentes nucleares, como foi o caso da usina de Chernobyl.\nb) O vapor de água gerado no processo de geração energética não é bom para o meio-ambiente.\nc) É necessário se desmatar alguma área verde antes de se construir uma termelétrica.\nd) Contribui para o efeito estufa por conta da emissão de CH4.\ne) Contribui para o efeito estufa por conta das emissões de CO2.')
    resposta7=input('Digite a sua resposta: ').lower()
    while resposta7 != 'a' and resposta7 != 'b' and resposta7 != 'c' and resposta7 != 'd' and resposta7 != 'e':
        resposta7=input('Digite a sua resposta: ').lower()
    resposta.append(resposta7)

def pergunta8():
    print('Com o passar dos anos o Brasil, vêm se tornando um pais com grande destaque no mercado internacional, com relação a energia renovável, assim pode-se dizer que as principais formas de energia renovável no Brasil em ordem decrescente de produção são:')
    print('a) Hidrelétrica, Eólica, Biomassa, Solar Centralizada\nb) Hidrelétrica, Biomassa, Eólica, Solar Centralizada\nc) Solar Centralizada, Biomassa, Eólica, Hidrelétrica\nd) Eólica, Hidrelétrica, Biomassa, Solar Centralizada')
    resposta8=input('Digite a sua resposta: ').lower()
    while resposta8 != 'a' and resposta8 != 'b' and resposta8 != 'c' and resposta8 != 'd':
        resposta8=input('Digite a sua resposta: ').lower()
    resposta.append(resposta8)

def pergunta9():
    print('Conforme os anos foram se passando a energia eólica vem aumentando seu destaque no mercado brasileiro, e algumas regiões por possuírem o clima e o tempo típico para a produção em larga escala dessa energia conseguem se beneficiar da utilização dela, assim pode-se dizer que a região com maior produção de energia eólica no Brasil é:')
    print('a) Sudeste\nb) Sul\nc) Norte\nd) Nordeste\ne) Centro-Oeste')
    resposta9=input('Digite a sua resposta: ').lower()
    while resposta9 != 'a' and resposta9 != 'b' and resposta9 != 'c' and resposta9 != 'd' and resposta9 != 'e':
        resposta9=input('Digite a sua resposta: ').lower()
    resposta.append(resposta9)

def pergunta10():
    print('Com um clima tropical típico o Brasil, passou a fazer uma importante parte no cenário internacional, com sua grande diversidade de vegetação e diversos tipos de climas, o Brasil passou a ser um pais com crescimento muito acentuado na produção de energia renovável, e aquela que mais vêm crescendo conforme os anos é a:')
    print('a) Hidrelétrica\nb) Eólica\nc) Biomassa\nd) Biogás\ne) Solar')
    resposta10=input('Digite a sua resposta: ').lower()
    while resposta10 != 'a' and resposta10 != 'b' and resposta10 != 'c' and resposta10 != 'd' and resposta10 != 'e':
        resposta10=input('Digite a sua resposta: ').lower()
    resposta.append(resposta10)


def correcao_avaliacao():
    pontos=100
    for i in range(10):
        if gabarito[i]==resposta[i]:
            print('Resposta correta, você ganhou 10 pontos!!!')
            pontos= pontos+10
        else:
            print('Resposta incorreta, você perdeu 10 pontos!!!')
            print(explicacao[i])
            pontos= pontos-10
    print(f'Você terminou o jogo com {pontos} pontos!!!')

    if pontos<100:
        print('Você só perdeu pontos!!!')
    elif pontos<150:
        print('Seu desempenho foi ruim!!!')
    elif pontos <180:
        print('Seu desempenho foi satisfatório!!!')
    elif pontos<=199:
        print('Parabéns, seu desempenho foi excelente!!!')
    else:
        print('Parabéns, você é um gênio!!!')

def main():
    pergunta1()
    pergunta2()
    pergunta3()
    pergunta4()
    pergunta5()
    pergunta6()
    pergunta7()
    pergunta8()
    pergunta9()
    pergunta10()
    correcao_avaliacao()
main()
