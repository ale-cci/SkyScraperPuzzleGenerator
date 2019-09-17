/**
 * Parse .puzzle file to pzl
 */
#include <iostream>
#include <fstream>
#include <bitset>
#define cchar(x) reinterpret_cast<const char*>(&x), sizeof(x)

int main(int argc, const char* argv[]){
	if (argc != 3) {
		std::cout << "Missing Arguments\n";
		exit(EXIT_FAILURE);
	}
	std::ifstream input(argv[1]);
	std::ofstream output(argv[2], std::ios::binary);
	int boardSize, nofCells, firstCell, secondCell;
	uint8_t byte;
	input >> boardSize;
	nofCells = (boardSize + 2) * (boardSize + 2);
	//std::cout << std::bitset<4>(boardSize);
	byte = std::bitset<4>(boardSize).to_ulong();
	output.write(cchar(byte));

	for(int i = 0; i < (nofCells); ++i) {
		input >> firstCell >> secondCell;
		auto first = std::bitset<4>(firstCell).to_string<char,std::string::traits_type,std::string::allocator_type>();
		auto second = std::bitset<4>(secondCell).to_string<char,std::string::traits_type,std::string::allocator_type>();
		byte = (std::bitset<8>(first + second)).to_ulong();
		output.write(cchar(byte));
	}
	input.close();
	output.close();
	return 0;
}
