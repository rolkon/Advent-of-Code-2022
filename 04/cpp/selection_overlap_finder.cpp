#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <array>

int detect_overlap(std::array<int, 4> &ranges) {
	//0 if not overlapping, 1 if partly overlapping, 2 if one contains another
	int containedness = 0;

	int lowerb = ranges[0] - ranges[2];
	int upperb = ranges[1] - ranges[3];

	//check for partial overlap
	if(lowerb <= 0) {
		if((ranges[1] - ranges[2]) * lowerb <= 0)
			containedness += 1;
	}else{
		if((ranges[0] - ranges[3]) * lowerb <= 0)
			containedness += 1;
	}

	//check if fully contained
	if(lowerb * upperb <= 0)
		containedness += 1;

	return containedness;
}

void update_overlap_counter(std::array<int, 4> &ranges, std::array<int, 2> & overlap) {

	int containedness = detect_overlap(ranges);

	if(containedness > 0)
		overlap[0]++;
	if(containedness > 1)
		overlap[1]++;
}

std::array<int, 2> calculate_overlap(std::string input) {
	std::array<int, 4> ranges = {0, 0, 0, 0};
	int ranges_index = 0;

	std::array<int, 2> overlap = {0, 0};

	for(int i=0; i<input.size(); i++){

		if(input[i] == '-' || input[i] == ',')
			ranges_index++;

		else if(input[i] == '\n'){
			update_overlap_counter(ranges, overlap);

			ranges.fill(0);

			ranges_index = 0;
		}else{

			// decimal-shift value and add ASCII-symbol transformed to int and offset-corrected
			ranges[ranges_index] *= 10;
			ranges[ranges_index] += int(input[i]) - 48;
		}
	}

	update_overlap_counter(ranges, overlap);

	return overlap;
}

int main(int argc, char** argv) {
	std::ifstream file_ptr("../bigboy.txt");
	std::string input;
	std::array<int, 2> overlap;

	if (file_ptr) {
		std::stringstream ss;
		ss << file_ptr.rdbuf();

		input = ss.str();
	}

	//std::cout << input.size() << std::endl;
	overlap = calculate_overlap(input);
	std::cout << "Full overlap: " << overlap[1] << std::endl;
	std::cout << "Partial overlap: " << overlap[0] << std::endl;

}