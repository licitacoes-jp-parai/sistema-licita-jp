request: filter-licitacoes
request url: https://transparencia.joaopessoa.pb.gov.br:8080/filter-licitacoes
request method: post
request payload: parametro padrão: periodo de publicação: data_inicial = "2024-01-01", data_final = "2024-02-01"
request payload example: {data_inicial: "2024-01-01", data_final: "2024-02-01"}
                          data_final: "2024-02-01"
                          data_inicial: "2024-01-01"
request parameters: ano de publicação,
                    período de publicação,
                    número,
                    situação,
                    palavras-chave,
                    modalidade,
                    secretarias/órgãos
                    unidades interessadas
                    participante
                    cnpj do participante
response:   id: numero identificador
            numero: número da licitação
            modalidade: tipo de licitação, pode ter os valores: Adesão (id_modalidade = 3),
                                                                Chamamento Público (id_modalidade = 10),
                                                                Concorrência Pública (id_modalidade = 1),
                                                                Concurso (id_modalidade = 26),
                                                                Convite (id_modalidade = 24),
                                                                Dispensa de Licitação (id_modalidade = 5),
                                                                GN 2349-9-Comparação de Preços (CP) (id_modalidade = 36),
                                                                GN 2349-9-Contratação Direta (CD) (id_modalidade = 37),
                                                                GN 2349-9- Licitação Pública internacional (LPI) (id_modalidade = 35),
                                                                GN 2350-9- Compra Direta (CD) (id_modalidade = 32),
                                                                GN 2350-9- Contratação Direta de Consultor Individual (CDCI) (id_modalidade = 34),
                                                                GN 2350-9- Seleção Baseada em Orçamento Fixo (SBOF) (id_modalidade = 29),
                                                                GN 2350-9- Seleção Baseada na Qualidade (SBQ) (id_modalidade = 28),
                                                                GN 2350-9- Seleção Baseada na Qualidade e Custo (SBQC) (id_modalidade = 27),
                                                                GN 2350-9- Seleçao Baseada nas Qualificações do Consultor (SQC) (id_modalidade = 31),
                                                                GN 2350-9- Seleção Baseada no Menor Custo (SBMC) (id_modalidade = 30),
                                                                GN 2350-9- Seleção e Consultor Individual (CI) (id_modalidade = 33),
                                                                Inexigibilidade (id_modalidade = 11),
                                                                Leilão (id_modalidade = 19),
                                                                Licitação Pública Nacional (id_modalidade = 38),
                                                                Pregão Eletrônico (id_modalidade = 4),
                                                                Pregão Presencial (id_modalidade = 17),
                                                                Tomada de Preços (id_modalidade = 8)

            descricao: descrição da licitação, tipo texto
            secretaria_orgao,
            titulo,
            data_publicacao,
            data_hora_certame,
            id_status,
            status_nome,
            chave_cgm,
            valor_total


O campo numero, presente na response, possui um pop up com informações mais detalhadas