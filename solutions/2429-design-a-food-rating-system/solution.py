from dataclasses import dataclass
from heapq import heapify, heappush, heappop
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.cuisines = {} # dict from cusine to the top food in that cuisine
    
        for f, c, r in zip(foods, cuisines, ratings):
            self.foods[f] = (r, c)

            if c not in self.cuisines:
                foods_list = []
                self.cuisines[c] = foods_list
                heapify(foods_list)
                heappush(foods_list, (-r, f))
            else:
                heappush(self.cuisines[c], (-r, f))
        
        # print(f'cuisines = {self.cuisines}, foods = {self.foods}')

    def changeRating(self, food: str, newRating: int) -> None:
        if food not in self.foods:
            raise KeyError
        rating, cuisine = self.foods[food]
        self.foods[food] = (newRating, cuisine)

        if cuisine not in self.cuisines:
            print(f'Error {cuisine} not in {self.cuisines} but in {self.foods}' )
            return

        heappush(self.cuisines[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:

        while self.cuisines[cuisine]:
            heap_rating, food = self.cuisines[cuisine][0]
            actual_rating, actual_cuisine = self.foods[food]
        
            # print(f'highest rating = {-heap_rating}, ({actual_rating}), cuisine = {cuisine}({actual_cuisine}), food= {food}')

            if -heap_rating == actual_rating:
                return food
            else:
                heappop(self.cuisines[cuisine])
        return None


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

'''
@dataclass
class ShortUrl:
    value: str
    long_url: str
    ttl_days: int
    created_at: datetime

/shorten
def shorten(long_url: str, ttl_days: int) -> str:
    1. Could generate a uniqueid (uuid would be 128 bits - if this is short enough?)
    2. Create a ShortUrl object 
    3. Save the shorturl -> 

def redirect(short_url: str) -> bool: 
    1. is the url unexpired?
    2. does the url have a corresponding mapping to a long url?
    3. ?
    pass

def delete(short_url: str) -> bool:
    pass

def update(short_url: str, new_value: str) -> bool:
    pass

'''

