# Pitoko - Arendente virtal de petshop para pequeno empreendedor, usando modelo de IA-LLM para respostas
Pitoko é o atendente virtual da Pit Shop, feito em Python com um toque de inteligência artificial. Ele usa a API da OpenAI pra conversar de forma simpática e natural com os clientes, e se conecta ao Google Docs pra buscar informações atualizadas sobre produtos, serviços, horários e promoções. Tudo isso roda com Flask, que faz a ponte entre o back-end e o chat do site.

O projeto também tem uma parte visual simples e acolhedora, feita com HTML, CSS e JavaScript, onde o cliente pode conversar com o Pitoko como se fosse um atendente de verdade. Ele responde com carinho, dá dicas e sempre tenta manter o foco nos cuidados com os pets.

Pra funcionar direitinho, o Pitoko precisa de dois elementos principais: a chave da OpenAI, que deve ser adicionada como variável de ambiente (OPENAI_API_KEY), e o arquivo credentials.json, que contém as credenciais da conta de serviço do Google Cloud. Esse arquivo é o que permite que o Pitoko leia o conteúdo do Google Docs de forma segura e automática.

Depois de configurar tudo, é só rodar o projeto no Replit e em poucos segundos, o Pitoko estará online.
