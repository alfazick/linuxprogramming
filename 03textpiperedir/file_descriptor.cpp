#include <iostream>
#include <string>
#include <fstream>

int main()
{
    
    std::ofstream outFile("output.txt", std::ios_base::app);;
    std::cout << "Keep Typing,type ESC to stop" << std::endl;
    std::string result;
    while (std::getline(std::cin,result)){
        if (result == "ESC"){
            break;
        }
        std::cout << result << std::endl;
        outFile << result << std::endl;
        result.clear();
    }
    
    outFile.close();
    return 0;
}
