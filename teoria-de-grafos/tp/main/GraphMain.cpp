#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<list>
#include<cstdlib>

#include<types.h>

#include <boost/config.hpp>
#include <boost/graph/adjacency_matrix.hpp>
#include <boost/tuple/tuple.hpp>


using namespace std;
typedef boost::adjacency_matrix<boost::undirectedS> UGraph;


/**
 * Imprime uma mensagem de ajuda para executar o programa.
 */
inline void helpMessage()
{
    cerr << endl << "Modo de uso:" << endl;
    cerr << "\tgraph -a <arquivo_de_entrada> [-t <threshold>]" << endl;
    cerr << "\t-a: Nome do arquivo de entrada. Obrigatorio." << endl;
    cerr << "\t-t: Threshold de poda da busca. Opcional." << endl;
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

inline uint32 countNeighbour(uint32 pos, uint32 currentCount, vector<uint32>& d, UGraph* graph)
{
    uint32 n = num_vertices(*graph);
    uint32 result = 0;

    for(uint32 i=0; i<n; ++i)
    {
        if(edge(pos, i, *graph).second && d[i] == currentCount) ++result; 
    }
    //cout << "COUNT_NEIGHBOUR " << (pos+1) << "-" << currentCount << "-" << result << endl;

    return result;
}

inline uint32 findNeighbourCount(uint32 pos, uint32 currentCount, vector<uint32>& d,
        vector<list<pair<uint32, uint32> > >& lists, 
        vector<list<pair<uint32, uint32> >::iterator>& itList, 
        UGraph* graph)
{
    //cout << "NEIGHBOUR " << (pos+1) << " " << lists[pos].size() << endl;
    uint32 result = 0;
    if(lists[pos].empty() || lists[pos].back().first < currentCount)
    {
        result = countNeighbour(pos, currentCount, d, graph);
        lists[pos].push_back(pair<uint32, uint32>(currentCount, result));
    }
    else
    {
        list<pair<uint32, uint32> >::iterator it = itList[pos];
        for(; it!=lists[pos].end(); ++it)
        {
            if(it->first == currentCount)
            {
                result = it->second;
                break;
            }
        }
        itList[pos] = it;
    }

    return result;
}

/*
inline bool removable(uint32 pos, vector<uint32>& mvc, UGraph* graph)
{
    uint32 n = num_vertices(*graph);
    for(uint32 i=0; i<n; ++i)
    {
        if(edge(pos, i, *graph).second && mvc[i] == 0) return false;
    }
    return true;
}
*/

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

    UGraph *graph = NULL;
    //UGraph *originalGraph = NULL;
    vector<list<pair<uint32, uint32> > > lists;
    vector<list<pair<uint32, uint32> >::iterator> itList;
    vector<uint32> mvc;
    uint32 mvcSize = 0;
    vector<uint32> d;

    uint32 n = 0;
    uint32 tmp = 0;
    uint32 t = 0;

    while ((option = getopt(argc, argv, "a:t:h")) != -1)
    {
        switch(option)
        {
            case 'a':
                inputFileName.assign(optarg);
                break;
            case 't':
                t = atoi(optarg);
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

    inputFile >> n;
    graph = new UGraph(n);
    //originalGraph = new UGraph(n);
    if(t==0 || n<t) t = n;
    else ++t;

    for(uint32 i=0; i < n; ++i)
    {
        for(uint32 j=0; j < n; ++j)
        {
            inputFile >> tmp;
            if(j<=i) continue;

            if(tmp == 1)
            {
                add_edge(i, j, *graph);
                //add_edge(i, j, *originalGraph);
            }
        }
    }


    lists.resize(n);
    itList.resize(n);
    d.resize(n);
    mvc.resize(n, 0);
    while(num_edges(*graph) > 0)
    {
        for(uint32 i=0; i<lists.size(); ++i) lists[i].clear();

        uint32 biggestPos = 0;
        bool init = false;


        log << "Edges: " << num_edges(*graph) << endl;

        for(uint32 i=0; i<n; ++i)
        {
            d[i] = in_degree(i, *graph);
            log << "Degree["<<(i+1)<<"]: " << d[i] << endl;
        }

        for(uint32 i=0; i<n; ++i)
        {
            if(d[i] == 0) continue;

            bool change = false;
            if(!init)
            {
                init = true;
                biggestPos = i;
                continue;
            }

            for(uint32 j=0; j<n; ++j) itList[j] = lists[j].begin();

            uint32 currentCount = 1;
            log << "Comparing: " << (i+1) << " - " << (biggestPos+1) << endl;
            while(currentCount < t)
            {
                int8 nFlag = 0;
                int8 eFlag = 0;

                log << "Current count: " << currentCount << endl;
                uint32 iCount = findNeighbourCount(i, currentCount, d, lists, itList, graph);
                uint32 bCount = findNeighbourCount(biggestPos, currentCount, d, lists, itList, graph);
                log << "\tCandidate neighbour count: " << iCount << endl;
                log << "\tBest neighbour count: " << bCount << endl;
                log << "\tCandidate edges count: " << d[i] << endl;
                log << "\tBest edges count: " << d[biggestPos] << endl;

                if(iCount < bCount) nFlag = -1;
                if(iCount > bCount) nFlag = 1;
                if(d[i] < d[biggestPos]) eFlag = -1;
                if(d[i] > d[biggestPos]) eFlag = 1;


                if(currentCount == 1)
                {
                    if(nFlag == -1) break;
                    if(nFlag == 0 && eFlag == -1) break;
                }
                else
                {
                    if(eFlag == -1) break;
                    if(eFlag == 0 && nFlag == -1) break;
                }
                if(nFlag == 1 || eFlag == 1)
                {
                    change = true;
                    break;
                }

                ++currentCount;
            }

            if(change || !init)
            {
                biggestPos = i;
            }

        }

        log << "Pushing: " << (biggestPos+1) << endl;
        log << endl;
        mvc[biggestPos] = 1;
        ++mvcSize;
        for(uint32 j=0; j<n; ++j)
        {
            if(edge(biggestPos, j, *graph).second)
            {
                remove_edge(biggestPos, j, *graph);
            }
        }
    }

    /*
    for(uint32 i=0; i<mvc.size(); ++i)
    {
        if(mvc[i] == 1 && removable(i, mvc, originalGraph))
        {
            mvc[i] = 0;
            --mvcSize;
        }
    }
    */

    cout << "1. Vertex Cover(" << mvcSize << "):";
    for(uint32 i=0; i<mvc.size(); ++i)
    {
        if(mvc[i] == 1) cout << " " << (i+1);
    }
    cout << endl;



    delete graph;
    //delete originalGraph;
    inputFile.close();
    log.close();

    return 0;
}
