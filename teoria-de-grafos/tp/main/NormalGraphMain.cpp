#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<list>
#include<cstdlib>


#include <boost/config.hpp>
#include <boost/graph/adjacency_matrix.hpp>
#include <boost/tuple/tuple.hpp>

#include <types.h>


using namespace std;
typedef boost::adjacency_matrix<boost::undirectedS> UGraph;


/**
 * Imprime uma mensagem de ajuda para executar o programa.
 */
inline void helpMessage()
{
    cerr << endl << "Modo de uso:" << endl;
    cerr << "\tgraph -a <arquivo_de_entrada>" << endl;
    cerr << "\t-a: Nome do arquivo de entrada. Obrigatorio." << endl;
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
    string inputFileName = ""; //Nome do arquivo de entrada.

    ifstream inputFile; //O handler do arquivo de entrada.
    ofstream log("log.txt");
    //ofstream log("/dev/null");

    UGraph *graph = NULL; //A matriz de adjacência
    vector<uint32> mvc; //A cobertura mínima de vértices

    uint32 n = 0; //Número de vértices
    uint32 edges = 0; //Número de arestas
    uint32 lasti = 0;
    uint32 tmp = 0;

    //Lendo as opções
    while ((option = getopt(argc, argv, "a:h")) != -1)
    {
        switch(option)
        {
            case 'a':
                inputFileName.assign(optarg);
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
    if(inputFileName.empty()) invalidExecution();

    inputFile.open(inputFileName.c_str());
    if(!inputFile.good())
    {
        inputFile.close();
        readFileError(inputFileName);
    }

    //Lendo o número de vértices
    inputFile >> n;
    graph = new UGraph(n);

    //Lendo a matriz de adjacência
    for(uint32 i=0; i < n; ++i)
    {
        for(uint32 j=0; j < n; ++j)
        {
            inputFile >> tmp;
            if(j<=i) continue;

            if(tmp == 1)
            {
                add_edge(i, j, *graph);
                ++edges;
            }
        }
    }

    //Enquanto existirem arestas...
    while(edges > 0)
    {
        log << "Edges: " << edges << endl;

        uint32 i = 0;
        uint32 j = 0;
        for(i=lasti; i<n; ++i)
        {
            bool found = false;
            for(j=i+1; j<n; ++j)
            {
                if(edge(i, j, *graph).second)
                {
                    log << "Found edge: " << i << "-" << j << endl;
                    lasti = i;
                    found = true;
                    break;
                }
            }
            if(found) break;
        }

        log << "Pushing: " << (i+1) << endl;
        log << "Pushing: " << (j+1) << endl;
        log << endl;

        //Acrescentando o vértice escolhido à cobertura mínima de
        //vértices.
        mvc.push_back(i);
        mvc.push_back(j);

        //Removendo as arestas incidentes ao vértice escolhido.
        for(uint32 k=0; k<n; ++k)
        {
            if(edge(k, i, *graph).second)
            {
                remove_edge(k, i, *graph);
                --edges;
            }
            if(edge(k, j, *graph).second)
            {
                remove_edge(k, j, *graph);
                --edges;
            }
        }
    }

    //Ordenando o conjunto dos vértices do MVC.
    sort(mvc.begin(), mvc.end());

    //Imprimindo o resultado
    cout << "1. Vertex Cover(" << mvc.size() << "):";
    for(uint32 k=0; k<mvc.size(); ++k)
    {
        cout << " " << (mvc[k]+1);
    }
    cout << endl;


    delete graph;
    inputFile.close();
    log.close();

    return 0;
}
