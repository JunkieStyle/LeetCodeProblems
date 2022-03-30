#include <vector>
#include <cmath>
#include <unordered_map>
#include <string>
#include <cassert>

class Solution {
public:
    using point = std::pair<int, int>;
    using key = std::pair<int, point>;

    double minAreaFreeRect(std::vector<std::vector<int>>& points) {
        auto d2 = [](const point& a, const point& b) {
            return std::pow(a.first - b.first, 2) + std::pow(a.second - b.second, 2);
        };

        auto KeyHash = [](const key& k) {
           return std::hash<std::string>()(
                std::to_string(k.first) +
                std::to_string(k.second.first) +
                std::to_string(k.second.second)
            );
        };

        long result = 0;
        std::unordered_map<key, std::vector<std::pair<point,point>>, decltype(KeyHash)> h(10, KeyHash);

        for (std::size_t p1 = 0; p1 < points.size(); ++p1) {
            for (std::size_t p2 = p1 + 1; p2 < points.size(); ++p2) {
                auto x = point(points[p1][0], points[p1][1]);
                auto y = point(points[p2][0], points[p2][1]);
                point mid {x.first + y.first, x.second + y.second};
                float diag = d2(x, y);
                key k {diag, mid};
                h[k].push_back(std::pair<point, point>(x, y));
            }
        }

        for (const auto& [key, pairs] : h) {
           for (std::size_t i = 0; i < pairs.size() - 1; ++i) {
                for(std::size_t j = i + 1; j < pairs.size(); ++j) {
                    const auto& [p1, p2] = pairs[i];
                    const auto& [p3, p4] = pairs[j];
                    long area = d2(p1, p3) * d2(p1, p4);
                    if (result == 0 or area < result) {
                        result = area;
                    }
                }
            }
        }

        return pow(result, 0.5);
    }
};

int main () {
    std::vector<std::vector<int>> points {{0,1},{2,1},{1,1},{1,0},{2,0}};
    assert(Solution().minAreaFreeRect(points) == 1);
    return 0;
}

