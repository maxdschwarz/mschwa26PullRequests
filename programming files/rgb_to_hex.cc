#include <iostream>
#include <sstream>
#include <iomanip>


// Main operating function
std::string rgb_to_hex(int r, int g, int b)
{
    // hex for red
    r = std::max(0, std::min(255, r));
    // hex for green
    g = std::max(0, std::min(255, g));
    // hex for blue
    b = std::max(0, std::min(255, b));

    // create a string stream
    std::stringstream ss;
    // this does something I think
    ss << std::uppercase << std::hex << std::setfill('0')
       << std::setw(2) << r << std::setw(2) << g << std::setw(2) << b;

    // return the string stream
    return ss.str();
}

//Test with std::string hexColor = rgb_to_hex(255, 127, 0); // returns "FF7F00"
