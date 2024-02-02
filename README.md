# image-processing

## INTRODUÇÃO

### Contextualização
Em um mundo cada vez mais orientado pela tecnologia onde o campo da
visão computacional tem se tornado cada vez mais presente, a área de
processamento de imagens se torna crucial para extrair significados, aprimorar a
qualidade e ajudar na automatização de análises de dados visuais.
Essa disciplina tem como objetivo juntar conhecimentos de matemática,
estatística e ciência da computação para criar técnicas de manipulação de imagens,
mas afinal por que ela se torna cada vez mais importante? Bom, isso se dá pelo
crescimento do uso de inteligência artificial e aprendizado de máquina, o
processamento de imagens impulsiona de maneira muito eficaz algoritmos de
aprendizado que detectam padrões em conjuntos massivos de dados visuais, a
extração de informações se torna útil para áreas da medicina, segurança, mas
também abre um caminho promissor para criação de tecnologias inovadoras e
experiências visuais aprimoradas com a melhoria da qualidade de fotos, ou em um
aumento na taxa de quadros(FPS) que melhora a experiência do jogador em um
vídeo game.
### Fundamentação teórica
Conseguimos a partir de agora perceber a importância do processamento de
imagens, então podemos pensar em quão útil pode ser um aplicativo ou website que
forneça a nós usuários algumas das várias funcionalidades que as operações de
processamento de imagens podem nos dar, porém, para implementarmos uma
aplicação como esta devemos primeiro ter uma base e saber como funcionam essas
operações na prática, usando matemática, estatística e estabelecendo nossos
conhecimentos sobre os assuntos, neste trabalho todos os conceitos utilizados
foram extraídos dos slides oferecidos pelo próprio tutor da disciplina, além disso em
alguns momentos foram feitas pesquisas a respeito de certos assuntos que
trouxeram mais dificuldades, mas, em maioria foram-se utilizados os conhecimentos
extraídos das aulas.Objetivos
O objetivo principal deste trabalho é desenvolver uma aplicação web que
comporte muitas operações de processamento de imagens, dessa maneira, deve-se
utilizar as linguagens de programação Python com auxílio de bibliotecas para leitura
de imagens e operações matriciais(OpenCv e Numpy respectivamente) para o
backend e Javascript com uso de HTML e CSS para o frontend. O website tem
como objetivo permitir que o usuário insira uma imagem e possa escolher qual
operação será aplicada na mesma.
## MATERIAIS E MÉTODOS
### Atividades Desenvolvidas
Durante o projeto foram desenvolvidas atividades práticas de processamento
de imagens, implementação de algoritmos para tratamento de imagens, análise e
extração de dados.
### Operações algébricas
As primeiras operações a serem implementadas foram as de dissolve
cruzado uniforme e não-uniforme, essas duas técnicas tem como objetivo
mesclar duas imagens mas se diferenciam um pouco em termos de cálculo
pois no caso do dissolve uniforme um dos parâmetros a serem usados é um
escalar enquanto no dissolve não-uniforme este mesmo parâmetro é uma
matriz.
### Transformações de intensidade
Os algoritmos de transformação de intensidade são responsáveis por
alterar de maneira significativa os valores de intensidade dos pixels de uma
imagem, invertendo totalmente os seus níveis de cinza como no caso datransformação de negativo, ou aumentando o contraste da imagem como na
operação de alargamento de contraste.
### Processamento de histograma
Um histograma representa a distribuição estatística de níveis de cinza
de uma imagem. Operações como a expansão de histograma são usadas
para produzir uma imagem mais rica visualmente, em alguns casos a
expansão de histograma é definida como um alargamento de contraste. Já a
operação de equalização de histogramas busca produzir uma imagem mais
equalizada, com uma distribuição de valores de intensidade mais uniforme. É
importante lembrar que a expansão de histogramas é uma operação pontual,
ou seja, os valores de cada pixel da imagem de saída dependem totalmente
das operações feitas em cada pixel da imagem de entrada diferentemente da
equalização de histogramas que é uma operação local, e por isso, cada pixel
da imagem de saída vai depender de operações feitas nas vizinhanças de
pixels da imagem de entrada.
### Controle de contraste adaptativo
Essa técnica de processamento de imagens ajusta o contraste de uma
imagem de maneira adaptativa, baseando-se em características locais da
imagem, diferentemente do controle de contraste global que aplica a mesma
transformação a todos os pixels da imagem. Pode ser útil em casos de
imagens com variação de iluminação pois possibilitam que partes distintas da
imagem sejam realçadas de diferentes maneiras. Nesta operação é feito um
cálculo que utiliza a média de um vizinhança de pixel n x n , um desvio de
padrão de uma vizinhança n x n e um parâmetro responsável por regular a
intensidade do aumento do contraste.
### Transformações geométricas
Diferentemente das operações de transformação de intensidade, as
transformações geométricas tem o objetivo de modificar a localização dospixels e não os seus valores de níveis de cinza, nesse grupo estão contidas
operações de mudança de escala(zoom in e zoom out) que aumentam ou
diminuem a imagem, rotação(rotaciona a imagem de acordo com um
parâmetro que define a angulação), pinch vertical, warping e outras
operações que tem por objetivo manipular o ponto em que os pixels se
encontram, mudando-os de lugar. Um ponto muito importante nesse tipo de
transformação é a interpolação, essa operação é necessária pois durante o
processo os pixels da imagem original podem não corresponder aos da
imagem transformada, por isso precisamos usar a interpolação para estimar
os valores de intensidade dos novos pontos criados de acordo com os pontos
originais, existem diversos tipos de interpolação mas os mais utilizados são a
interpolação bilinear ou a de vizinho mais próximo(replicação).
### Filtragem linear e não-linear
A filtragem é uma operação muito comum no processamento de
imagens e pode ser dividida entre filtragem linear e não-linear, neste projeto
foram implementados 2 tipos de filtros, o de média e o de mediana.
O primeiro filtro consiste em um processo onde cada pixel da imagem
de saída é a média dos pixels contidos na vizinhança de uma máscara de
filtragem. Esse filtro é chamado de passa-baixa e reduz os detalhes da
imagem, aumentando o grau de suavização. Já a filtragem de mediana é um
processo onde cada pixel de imagem de saída é substituído pela mediana
dos pixels da sua vizinhança, esse tipo de filtro é muito eficaz para eliminar
ruídos do tipo “sal e pimenta” e ruídos impulsivos ao mesmo tempo que
preserva os contornos da imagem.
### Detecção de bordas
A detecção de bordas é uma técnica de processamento de imagens
capaz de determinar pontos de uma imagem digital onde a intensidade
luminosa muda de forma brusca. É fortemente usada na área de extração de
características pois reduz a quantidade de dados a serem analisados
descartando informações irrelevantes para o processo. Neste projeto foiimplementado somente um dos vários tipos de operadores de detecção de
borda, neste caso o escolhido foi o Gradiente de Sobel.
O Gradiente de Sobel é uma operação que calcula o gradiente de
intensidade em cada ponto de uma imagem dando a direção com maior
variação entre o claro e o escuro, com isso é possível obter as bordas
presentes em uma imagem.
### Aguçamento de bordas e High Boost
Aguçamento de bordas é uma técnica que visa melhorar a nitidez de
uma imagem através da intensificação das transições de intensidade
luminosa(bordas), ela é muito útil para destacar detalhes e estruturas finas
presentes em uma imagem. O aguçamento é frequentemente realizado
através de operações de convolução com um kernel apropriado, no caso
deste trabalho, o kernel utilizado foi o próprio operador de Sobel citado logo
acima.
Já quando falamos de High Boost, podemos dizer que ele é uma
extensão do filtro de aguçamento, ele é usado para realçar detalhes de alta
frequência e outras transições abruptas de intensidade adicionando uma
fração amplificada da imagem original a imagem suavizada.
### Convolução
É uma operação matemática fundamental no processamento de
imagens usada para aplicar filtros a uma imagem. Essa técnica envolve a
multiplicação de cada elemento da máscara pelo valor correspondente a ele
na imagem, a soma desses resultados será o novo valor de intensidade na
imagem de saída. No caso deste projeto foi utilizado offset, o offset determina
o quanto a máscara vai se deslocar na imagem.
### Ferramentas utilizadas
A implementação do projeto foi dividida em duas áreas principais, a área de front
end, responsável pelo contato direto com o usuário para escolha de operações einserção de imagens, e back end, responsável por realizar todas as operações já
mostradas e devolver ao usuário o resultado esperado.
Back end
No back end estão organizadas as implementações de todas as
operações de processamento de imagens já mostradas anteriormente, a
linguagem de programação usada foi o Python3, junto a ela foram utilizadas
as bibliotecas Numpy e OpenCV.
NumPy é uma biblioteca de código aberto que serve para manipulação
de dados e computação científica, é usada no domínio da álgebra linear,
matrizes e em campos de ciência de dados. A biblioteca fornece um objeto
array multidimensional que são muito mais rápidos que as listas Python, além
de fornecer ferramentas que permitem trabalhar com esses arrays de forma
mais “confortável”.
OpenCV também é uma biblioteca de código aberto amplamente
usada nos campos da visão computacional, aprendizado de máquina e
processamento de imagens. A partir dela é possível processar imagens,
vídeos, além de outras utilidades.
Neste projeto a junção do Python e essas duas bibliotecas foram as
principais ferramentas no backend, o OpenCV servia para ler as imagens
enquanto a NumPy tinha como funcionalidade principal auxiliar em algumas
operações que envolvessem matrizes, como por exemplo a criação de
matrizes n x n totalmente zeradas. Cabe citar também que em alguns
momentos foram utilizadas as linguagens MATLAB e Octave apenas para
efeitos de comparação com as operações feitas com Python.
### Front end
O Front end é a parte do sistema responsável por interagir diretamente
com o usuário, e neste projeto foram usados o React, o Node e o Npm.
O React é uma biblioteca JavaScript para criação de interfaces de
usuário, essa biblioteca divide uma tela em diversos componentes quepermitem trabalhar de maneira individual em cada um deles, possibilitando o
reaproveitamento de código e uma padronização de interface.
O Node.js é um ambiente de execução JavaScript do lado do servidor,
ou seja, com o Node é possível criar aplicações em JavaScript que podem
rodar de forma autônoma em uma máquina sem a necessidade de um
navegador.
Npm ou Node Package Manager é um gerenciador de pacotes para a
linguagem de programação JavaScript muito utilizado para instalar bibliotecas
e frameworks que são necessários para o desenvolvimento de aplicações em
Node.js.
Conhecimentos utilizados
Os discentes já obtinham um conhecimento prévio e estabelecido nas linguagens de
programação usadas tanto no front end quanto no back end. Mas a respeito das
operações de processamento de imagens, todo o conhecimento aplicado na prática
com o uso das ferramentas já citadas foram adquiridos através dos materiais
fornecidos pelo próprio professor, somente com os slides das aulas ministradas em
sala de aula foram suficientes para possibilitar a implementação.
## RESULTADOS
Os resultados obtidos são extremamente satisfatórios, o sistema desenvolvido trás
uma boa proposta de interação com o usuário que pode escolher qual operação
será executada além de poder inserir as imagens que vão receber as
transformações. As operações tem um ótimo desempenho e retornam ao usuário o
resultado esperado proporcionando uma ótima experiência de uso
## DISCUSSÃO
Mesmo com bons resultados, deve-se esclarecer que nem todas as funções foram
executadas com êxito, as operações de Pinch Vertical e Warping baseado em
campos não desempenharam o seu papel da maneira correta, a sua implementaçãose deu através dos slides disponibilizados durante a aula mas mesmo assim não
houve sucesso.
## CONCLUSÃO
Diante do cenário apresentado é totalmente evidente que o processamento de
imagens desempenha um papel fundamental nos dias atuais, atuando em conjunto
com técnicas de aprendizado de máquina e possibilitando o avanço de tecnologias
que se tornam cada vez mais usadas no cotidiano.
A implementação prática dos conceitos aprendidos através de aplicativos ou
websites permitem ao usuário uma gama diversificada de funcionalidades que
mostram que o processamento de imagens é extremamente versátil, cabe lembrar
que essa área não se limita somente ao ramo acadêmico, mas também tem grande
participação na indústria de entretenimento.
Em resumo, o processamento de imagens não apenas reflete a convergência de
áreas como matemática ou ciência da computação, mas também reflete a sua
grande importância para impulsionar o desenvolvimento tecnológico molhando
positivamente o mundo digital e visual.