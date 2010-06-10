#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<list>
#include<cstdlib>

#include<types.h>

using namespace std;


/**
 * Imprime uma mensagem de ajuda para executar o programa.
 */
inline void helpMessage()
{
    cerr << endl << "Modo de uso:" << endl;
    cerr << "\trandomgraph -n <n>" << endl;
    cerr << "\t-n: Número de vértices. Obrigatorio." << endl;
    //    cerr << "\t-t: Caminho do diretorio de armazenamento de arquivos temporarios. Default: \"/var/tmp\". Opcional." << endl;
    cerr << "\t-h: Exibe esta mensagem e termina." << endl;

    cerr << endl;
}

/**
 * Imprime a mensagem de ajuda e termina.
 */
inline void help()
{
    helpMessage();
    exit(0);
}

/**
 * Imprime a mensagem de ajuda e termina com código de erro.
 */
inline void invalidExecution()
{
    helpMessage();
    exit(-1);
}

/**
 * Imprime uma mensagem de erro devido a um arquivo que não foi lido
 * com sucesso e termina.
 *
 * @param file O nome do arquivo não lido.
 */
inline void readFileError(const string& file)
{
    cerr << "Erro ao ler o arquivo \"" << file << "\". Terminando." << endl;
    exit(-1);
}


/**
 * Executa o programa.
 *
 * @param argc O número de parâmetros na linha de comando.
 * @param argv Os parâmetros da linha de comando.
 */
int main(int argc, char** argv)
{
    int32 option; //Código ASCII da opção atual.

    uint32 n = 0;

    while ((option = getopt(argc, argv, "n:h")) != -1)
    {
        switch(option)
        {
            case 'n':
                n = atoi(optarg);
                break;
            case 'h':
                helpMessage();
                exit(0);
                break;
            default:
                invalidExecution();
                break;
        }
    }

    //É obrigatório que um nome seja definido para o arquivo de
    //entrada.
    if(n <= 0) invalidExecution();

    srand(time(NULL));
    cout << n << endl;
    vector<vector<uint8> >g;
    for(uint32 i=0; i<n; ++i)
    {
        g.push_back(vector<uint8>());
        for(uint32 j=0; j<n; ++j) g[i].push_back(0);
    }
    for(uint32 i=0; i<n; ++i)
    {
        for(uint32 j=i+1; j<n; ++j)
        {
            uint8 tmp = rand() % 2;
            g[i][j] = tmp;
            g[j][i] = tmp;
        }
    }
    for(uint32 i=0; i<n; ++i)
    {
        for(uint32 j=0; j<n; ++j) cout << (uint32)g[i][j] << " ";
        cout << endl;
    }




    return 0;
}
