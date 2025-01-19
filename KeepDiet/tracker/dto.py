from dataclasses import dataclass

@dataclass(frozen=True)
class ProductDTO:
    id: int
    name: str
    brand: str
    calories: float
    serving_amount: float
    serving_unit: str

    @classmethod
    def from_json(cls, json):
        return cls(
            id = json["food_id"],
            name = json["food_name"],
            brand = json["brand_name"],
            calories = json["servings"]["serving"]["calories"],
            serving_amount = json["servings"]["serving"]["metric_serving_amount"],
            serving_unit = json["servings"]["serving"]["metric_serving_unit"]
        )
