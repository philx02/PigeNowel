#include "SendEmail.h"

#include <random>
#include <fstream>
#include <string>

#include <boost/asio.hpp>

void pige(const std::vector< std::pair< std::string, std::string > > &iOne, std::vector< std::string > &iTwo)
{
  std::random_device rd;
  std::mt19937 g(rd());
  while (true)
  {
    std::shuffle(iTwo.begin(), iTwo.end(), g);
    bool wDuplicateFound = false;
    for (size_t wIter = 0; wIter < iOne.size(); ++wIter)
    {
      if (iOne[wIter].first == iTwo[wIter])
      {
        wDuplicateFound = true;
        break;
      }
    }
    if (!wDuplicateFound)
    {
      break;
    }
  }
}

int main(int argc, char *argv[])
{
  if (argc != 2)
  {
    std::cout << "need list in argument" << std::endl;
    exit(1);
  }
  std::vector< std::string > wSplit;
  std::string wLine;
  std::ifstream wFile(argv[1]);
  std::vector< std::pair< std::string, std::string > > wOne;
  std::vector< std::string > wTwo;
  while (std::getline(wFile, wLine))
  {
    boost::split(wSplit, wLine, boost::is_any_of(","));
    wOne.emplace_back(wSplit[0], wSplit[1]);
    wTwo.emplace_back(wSplit[0]);
  }
  pige(wOne, wTwo);
  for (size_t wIter = 0; wIter < wOne.size(); ++wIter)
  {
    sendEmail("127.0.0.1", wOne[wIter].first, wOne[wIter].second, "no-reply@spoluck.ca", "Vous avez pigé...", wTwo[wIter]);
  }
  return 0;
}
