# **Kommunist Autorun v0.1**

Este é um executável autorun engraçado que fiz para ser usado dentro de um pen drive ou similares, com o objetivo de conscientizar as pessoas sobre os riscos potenciais de inserir pen drives desconhecidos em seu computador. O executável sozinho não faz nada, apenas mostra a tela do programa com uma imagem e toca uma música, o único botão disponível apenas fecha o programa.

Este programa ou quaisquer arquivos associados a ele não fazem nada prejudicial ou coletam quaisquer dados do usuário do computador, o único objetivo aqui é causar algum tipo de surpresa ao usuário.

**AVISO LEGAL:** Para evitar problemas de direitos autorais não vou postar aqui imagens e sons usados para minha versão pessoal, mas se você realmente quer ver algo bem próximo ao que eu fiz procure pelo Hino da URSS e a foto do Pernalonga comunista...

## **Como Compilar Esse Programa**

1. Baixe todos os arquivos: `autorun.py` e `autorun.spec`
2. Coloque na mesma pasta dos arquivos baixados um arquivo de imagem e um arquivo de música
3. Pessoalmente eu sugiro um arquivo de imagem com 600x600 pixels e no formato jpeg, do contrário serão necessárias modificações no código
4. Para o arquivo de música eu sugiro um arquivo no formato wav, ou também serão necessárias modificações no código
5. Mude o nome do arquivo de música para `music.wav` e do arquivo de imagem para `image.jpeg`
6. No console do python execute o seguinte código: `pyinstaller autorun.spec`
7. O arquivo executável estará na pasta `dist`

## **Dicas Avançadas**

Se você realmente sabe sobre as coisas, não precisa de dicas, certo? Mas se eu puder dar meus 2 centavos de conselho, aqui vão algumas dicas:

1. Você pode modificar o tamanho da tela do programa e do arquivo de imagem no código
2. A função `def resource_path` no código é necessária para um gerenciamento correto dos arquivos e para que o autorun funcione perfeitamente em apenas um arquivo. Mais informações podem ser encontradas nos links abaixo:
   1.  [Auto-py-to-exe: Only One File – WITH IMAGES – For Our Python Apps](https://pythonprogramming.altervista.org/auto-py-to-exe-only-one-file-with-images-for-our-python-apps/)
   2. [Stack Overflow - Bundling data files with PyInstaller (--onefile)](https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741)
3. Se você desejar um ícone personalizado minha sugestão é utilizar o pacote `auto-py-to-exe` para isso, eu pessoalmente não consegui fazer isso funcionar diretamente com o `Python Installer`. Para isso dê uma olhada no primeiro link acima.

### **Pacotes Necessários**

- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pygame](https://www.pygame.org/news)
- [Pyinstaller](https://pyinstaller.org/en/stable/index.html)
- [OS](https://docs.python.org/3/library/os.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [Pillow](https://pypi.org/project/Pillow/)