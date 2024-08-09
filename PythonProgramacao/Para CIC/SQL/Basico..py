'''
---> Para o código

    O ponto e vírgula determina a quantidade de comandos no código, e não a quantidade de linhas
Indicando assim, o fim do comando.

    Quando o código é iniciado, é necessário atualizar a barra de SCHEMAS, e então aparecerá a tabela escolhida e dentro 
desse diretório, terá as colunas que foram digitadas no código.

    Por algum motivo que eu não sei, o Terminal do WORKBENCH não está abrindo. Não sei se isso será um problema no futuro,
mas de qualquer forma, tem como acessar o código e suas tabelas usando o terminal.
    Siga o seguinte passo a passo:
        1) Abra o temrminal
        2) sudo mysql
        3) show databases;
        4) use <nome_do_diretorio>;
    *caso o que quer acessar estiver dentro de mais um diretório, é só repetir o passo 4*
    *se aparecer 'database changed', você acessou o diretório escolhido
        5) status;      (para mostrar qual foi o database escolhido)
        6) show tables; (para mostrar as tabelas criadas no código)
        7) describe <nome_diretorio_escolhido>;
    *e então deve aparecer ass tabelas com as informações descritas no código*
        8) exit         (para sair)

    Os dados que aparecem no passo 6 também podem ser acessados indo no diretório final em que o código foi digitado
e acessando o ícone que se parece com a letra 'i' e acesssando a área 'Columns'




---> Especificações

    O SQL é dividido em 4 tipos PRIMITIVOS:

-> Numérico:
    Inteiro
        TinyInt, SmallInt, Int, MediumInt, BigInt (a diferença está no tamnho do número utilizado)
    Real
        Decimal, Float, Double, Real
    Lógico
        Bit, Boolean (sim e não , zero e um...)

-> Data/Tempo
        Date, DateTime, TimeStamp, Time, Year (data, data com informações, hora e ano)

-> Literal
    Caractere
        CHAR, VARCHAR (determina a quantidade de caracteres; o primeiro o espaço vazio é preenchido, no segundo, não)
    Texto
        TinyText, Text, MediumText, LongText (para textos em geral)
    Binário
        TinyBlob, Blob, MediumBlob, LongBlob (tipo blob: guardar qualquer coisa em binário)
    Coleções
        Enum, Set (são tipos que pode configurar quais são os valores permitidos)

-> Espaciais
    Geometry, Point, Polygon, MultiPolygon (informações sobre volumétricos)


'''