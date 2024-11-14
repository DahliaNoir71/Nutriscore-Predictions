from flask_sqlalchemy import SQLAlchemy
from app import db



class NutriScorePrediction(db.Model):
    """
    This class represents a NutriScore prediction record in the database.

    Attributes:
    id (int): The unique identifier for the prediction record.
    energy_kcal_100g (float): Energy in kilocalories per 100g.
    fat_100g (float): Fat content per 100g.
    saturated_fat_100g (float): Saturated fat content per 100g.
    sugars_100g (float): Sugar content per 100g.
    fiber_100g (float): Fiber content per 100g.
    proteins_100g (float): Protein content per 100g.
    salt_100g (float): Salt content per 100g.
    fruits_vegetables_nuts_estimate_from_ingredients_100g (float): Estimated fruits, vegetables, and nuts content per 100g.
    predicted_score (str): The predicted NutriScore ('a', 'b', 'c', 'd', or 'e').
    prediction_date (datetime): The date and time when the prediction was made.
    """

    __tablename__ = 'nutriscore_predictions'

    id = db.Column(db.Integer, primary_key=True)
    energy_kcal_100g = db.Column(db.Float, nullable=False)
    fat_100g = db.Column(db.Float, nullable=False)
    saturated_fat_100g = db.Column(db.Float, nullable=False)
    sugars_100g = db.Column(db.Float, nullable=False)
    fiber_100g = db.Column(db.Float, nullable=False)
    proteins_100g = db.Column(db.Float, nullable=False)
    salt_100g = db.Column(db.Float, nullable=False)
    fruits_vegetables_nuts_estimate_from_ingredients_100g = db.Column(db.Float, nullable=False)
    predicted_score = db.Column(db.String(1), nullable=False)  # 'a', 'b', 'c', 'd', or 'e'
    prediction_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    

    def __init__(self, 
                 energy_kcal_100g, 
                 fat_100g, 
                 saturated_fat_100g, 
                 sugars_100g, 
                 fiber_100g, 
                 proteins_100g, 
                 salt_100g, 
                 fruits_vegetables_nuts_estimate_from_ingredients_100g,
                 predicted_score):
        """
        Initialize a new NutriScorePrediction instance.

        Parameters:
        energy_kcal_100g (float): Energy in kilocalories per 100g.
        fat_100g (float): Fat content per 100g.
        saturated_fat_100g (float): Saturated fat content per 100g.
        sugars_100g (float): Sugar content per 100g.
        fiber_100g (float): Fiber content per 100g.
        proteins_100g (float): Protein content per 100g.
        salt_100g (float): Salt content per 100g.
        fruits_vegetables_nuts_estimate_from_ingredients_100g (float): Estimated fruits, vegetables, and nuts content per 100g.
        predicted_score (str): The predicted NutriScore ('a', 'b', 'c', 'd', or 'e').
        prediction_date (datetime): The date and time when the prediction was made.
        """
        self.predicted_score = predicted_score
        self.energy_kcal_100g = energy_kcal_100g
        self.fat_100g = fat_100g
        self.saturated_fat_100g = saturated_fat_100g
        self.sugars_100g = sugars_100g
        self.fiber_100g = fiber_100g
        self.proteins_100g = proteins_100g
        self.salt_100g = salt_100g
        self.fruits_vegetables_nuts_estimate_from_ingredients_100g = fruits_vegetables_nuts_estimate_from_ingredients_100g