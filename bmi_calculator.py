"""
BMI (Body Mass Index) Calculator Module
Provides functionality to calculate BMI with proper validation and categorization.
"""

class BMICalculator:
    """
    Calculator for Body Mass Index (BMI).
    
    BMI is calculated as: weight (kg) / (height (m))^2
    """
    
    # BMI categories based on WHO standards
    CATEGORIES = {
        'underweight': (0, 18.5),
        'normal': (18.5, 25),
        'overweight': (25, 30),
        'obese': (30, float('inf'))
    }
    
    @staticmethod
    def calculate(height_cm, weight_kg):
        """
        Calculate BMI from height and weight.
        
        Args:
            height_cm (float): Height in centimetres
            weight_kg (float): Weight in kilograms
            
        Returns:
            dict: Dictionary containing BMI value and category
            
        Raises:
            ValueError: If height or weight are invalid (zero or negative)
        """
        # Validate inputs
        if height_cm <= 0:
            raise ValueError("Height must be greater than zero")
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than zero")
        
        # Convert height from cm to meters
        height_m = height_cm / 100
        
        # Calculate BMI
        bmi = weight_kg / (height_m ** 2)
        
        # Determine category
        category = BMICalculator._get_category(bmi)
        
        return {
            'bmi': round(bmi, 1),
            'category': category,
            'height_cm': height_cm,
            'weight_kg': weight_kg
        }
    
    @staticmethod
    def _get_category(bmi):
        """
        Determine BMI category based on WHO standards.
        
        Args:
            bmi (float): Calculated BMI value
            
        Returns:
            str: BMI category name
        """
        for category, (lower, upper) in BMICalculator.CATEGORIES.items():
            if lower <= bmi < upper:
                return category
        return 'unknown'
    
    @staticmethod
    def is_valid_input(height_cm, weight_kg):
        """
        Check if height and weight inputs are valid.
        
        Args:
            height_cm (float): Height in centimetres
            weight_kg (float): Weight in kilograms
            
        Returns:
            tuple: (is_valid, error_message)
        """
        try:
            height_cm = float(height_cm)
            weight_kg = float(weight_kg)
            
            if height_cm <= 0:
                return False, "Height must be greater than zero"
            if weight_kg <= 0:
                return False, "Weight must be greater than zero"
            if height_cm > 300:
                return False, "Height seems unrealistic (>300cm)"
            if weight_kg > 500:
                return False, "Weight seems unrealistic (>500kg)"
                
            return True, None
            
        except (ValueError, TypeError):
            return False, "Height and weight must be valid numbers"
